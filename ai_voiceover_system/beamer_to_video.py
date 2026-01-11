import os
import re
import argparse
from dataclasses import dataclass
from typing import List, Optional, Tuple
from pathlib import Path

# --- Data Structures ---

@dataclass
class AudioSegment:
    text: str
    speaker: Optional[str] = None
    is_click: bool = False

@dataclass
class FrameData:
    frame_index: int
    audio_segments: List[AudioSegment]

# --- Parser ---

class BeamerParser:
    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def parse(self) -> List[FrameData]:
        frames = []
        # Find all \note{...} blocks. 
        # Since regex is bad at nested braces, we use a simple state machine to extracting the content of \note{...}
        
        # We iterate through the file looking for "\note{"
        # Then we count braces to find the matching end.
        
        cursor = 0
        frame_counter = 0
        
        while True:
            # Simple heuristic: searching for \note{
            # Note: This finds notes in order of appearance. 
            # In Beamer, \note{} usually follows the frame it belongs to or is inside it.
            # We assume logical mapping: 1st note -> 1st frame (or rather, the overlay sequence start)
            # However, for video generation, we usually map notes sequentially to visual changes.
            # Given the "Protocol" defined in the task:
            # We assume the order of \note{} blocks corresponds to the order of frames/overlays in the PDF.
            
            start_idx = self.content.find("\\note{", cursor)
            if start_idx == -1:
                break
            
            # Found a note start
            content_start = start_idx + 6 # len("\\note{")
            brace_balance = 1
            current_idx = content_start
            
            note_content = ""
            
            while brace_balance > 0 and current_idx < len(self.content):
                char = self.content[current_idx]
                if char == '{':
                    brace_balance += 1
                elif char == '}':
                    brace_balance -= 1
                
                if brace_balance > 0:
                    note_content += char
                current_idx += 1
            
            cursor = current_idx
            
            # Now process the note content
            # Clean up whitespace
            note_content = note_content.strip()
            if not note_content:
                continue
                
            segments = self._parse_note_content(note_content)
            frames.append(FrameData(frame_index=frame_counter, audio_segments=segments))
            frame_counter += 1
            
        return frames

    def _parse_note_content(self, text: str) -> List[AudioSegment]:
        # Split by [click]
        # We use a regex to split but keep the delimiter to know where clicks are
        # But actually, [click] marks the START of a new segment usually.
        # "Intro text. [click] Next point."
        # Segment 1: "Intro text."
        # Segment 2 (Click): "Next point."
        
        raw_segments = re.split(r'(\[click\])', text, flags=re.IGNORECASE)
        
        parsed_segments = []
        
        # Helper to parse speaker from text
        def parse_speaker_text(t: str) -> Tuple[Optional[str], str]:
            # Regex for "Name: Text..."
            match = re.match(r'^\s*([A-Za-z\s\.]+):\s*(.+)', t, re.DOTALL)
            if match:
                return match.group(1).strip(), match.group(2).strip()
            return None, t.strip()

        # Iterate
        current_speaker = None # specific default? Or None means "Narrator"
        
        for segment in raw_segments:
            segment = segment.strip()
            if not segment:
                continue
                
            if segment.lower() == "[click]":
                # The NEXT segment corresponds to a click event (new PDF page)
                # We flag the next added segment as 'is_click=True'
                # Or we can treat [click] as a marker that the *following* text belongs to a new slide state.
                # Let's model it: AudioSegment has `is_click`.
                # If we encounter [click], the next text segment we add will have is_click=True.
                parsed_segments.append(AudioSegment(text="", is_click=True))
            else:
                # Text content
                speaker, clean_text = parse_speaker_text(segment)
                if speaker:
                    current_speaker = speaker
                
                # If the previous item was a click marker (empty segment with is_click=True),
                # we merge this text into it? 
                # No, [click] creates a barrier. 
                # Wait, if `[click]` is standalone, it implies visual change.
                # Usually: "Text 1 [click] Text 2"
                # This maps to:
                # Image 1 plays with Audio("Text 1")
                # Image 2 plays with Audio("Text 2")
                
                # Our list should be logical audio chunks.
                # [Audio("Text 1"), Audio("Text 2", click=True)]
                
                if parsed_segments and parsed_segments[-1].is_click and not parsed_segments[-1].text:
                     # We have a pending click marker from the previous loop iteration
                     parsed_segments[-1].text = clean_text
                     parsed_segments[-1].speaker = current_speaker
                else:
                    parsed_segments.append(AudioSegment(text=clean_text, speaker=current_speaker, is_click=False))
                    
        return parsed_segments

if __name__ == "__main__":
    # Test Parser
    # Test Parser
    import sys
    # if len(sys.argv) > 1:
    #     p = BeamerParser(sys.argv[1])
    #     frames = p.parse()
    #     for i, f in enumerate(frames):
    #         print(f"--- Note Block {i} ---")
    #         for seg in f.audio_segments:
    #             print(f"  [Click={seg.is_click}] Speaker: {seg.speaker} | Text: {seg.text[:50]}...")

# --- PDF Processor ---

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None

class PDFProcessor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        if fitz is None:
            raise ImportError("pymupdf not installed. Please install: pip install pymupdf")

    def to_images(self, output_dir: Path) -> List[Path]:
        print(f"🖼️ Rasterizing PDF (PyMuPDF): {self.pdf_path}")
        doc = fitz.open(self.pdf_path)
        image_paths = []
        
        for i, page in enumerate(doc):
            # dpi=150 is usually sufficient for 1080p video (A4 size approx)
            # Default PDF size is small points, so we need higher density.
            # Slide size is usually 128mm x 96mm (4:3) or 160mm x 90mm (16:9)
            # 160mm ~ 6.3 inches. 6.3 * 300 = 1900 px width. 300 DPI is good.
            pix = page.get_pixmap(dpi=200) 
            
            img_path = output_dir / f"{i:04d}.png"
            pix.save(str(img_path))
            image_paths.append(img_path)
            
        doc.close()
        return image_paths

# --- Audio Generator ---

try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False

try:
    from google.cloud import texttospeech
    GCLOUD_AVAILABLE = True
except ImportError:
    GCLOUD_AVAILABLE = False

class AudioGenerator:
    def __init__(self, output_dir: Path, provider: str = 'gtts'):
        self.output_dir = output_dir
        self.provider = provider
        self.client = None
        
        if self.provider == 'gcloud':
            if not GCLOUD_AVAILABLE:
                print("⚠️ Google Cloud TTS not available, falling back to gTTS")
                self.provider = 'gtts'
            else:
                self.client = texttospeech.TextToSpeechClient()

    def generate(self, text: str, speaker: Optional[str] = None, index: int = 0) -> Path:
        filename = f"audio_{index:04d}.mp3"
        filepath = self.output_dir / filename
        
        if filepath.exists():
            return filepath
            
        print(f"🎤 Generating Audio ({self.provider}): {text[:30]}...")
        
        if self.provider == 'gcloud' and self.client:
            self._generate_gcloud(text, speaker, filepath)
        else:
            self._generate_gtts(text, filepath)
            
        return filepath

    def _generate_gtts(self, text: str, filepath: Path):
        # Simple gTTS implementation
        tts = gTTS(text=text, lang='en')
        tts.save(str(filepath))

    def _generate_gcloud(self, text: str, speaker: str, filepath: Path):
        # Basic mapping based on name
        gender = texttospeech.SsmlVoiceGender.NEUTRAL
        name = "en-US-Studio-O" # Default Female
        
        if speaker and "James" in speaker:
             name = "en-US-Studio-M" # Male
             gender = texttospeech.SsmlVoiceGender.MALE
        elif speaker and "Sarah" in speaker:
             name = "en-US-Studio-O" # Female
             gender = texttospeech.SsmlVoiceGender.FEMALE
             
        input_text = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name=name,
            ssml_gender=gender
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = self.client.synthesize_speech(
            input=input_text, voice=voice, audio_config=audio_config
        )

        with open(filepath, "wb") as out:
            out.write(response.audio_content)

# --- Video Stitcher ---

try:
    from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False

class VideoStitcher:
    def __init__(self, output_path: str):
        self.output_path = output_path
        if not MOVIEPY_AVAILABLE:
            raise ImportError("moviepy not installed. Please install: pip install moviepy")

    def stitch(self, image_paths: List[Path], audio_map: List[List[Path]]):
        """
        image_paths: List of paths to images (one per visual state)
        audio_map: List of lists. audio_map[i] contains the audio clips that play *during* image[i].
        """
        print("🎬 Stitching Video...")
        
        clips = []
        
        for i, img_path in enumerate(image_paths):
            if i >= len(audio_map):
                # Extra images with no audio? Skip or show briefly?
                # Usually shouldn't happen if logic is correct.
                continue
                
            frame_audios = audio_map[i]
            
            if not frame_audios:
                # Silent frame?
                duration = 2 # Default 2s silence
                audio_clip = None
            else:
                # Concatenate audios for this frame
                audio_objs = [AudioFileClip(str(a)) for a in frame_audios]
                audio_clip = concatenate_videoclips(audio_objs) if len(audio_objs) > 1 else audio_objs[0]
                duration = audio_clip.duration
            
            # Create Image Clip
            # Note: ImageClip accepts path as string
            video_clip = ImageClip(str(img_path)).with_duration(duration)
            
            if audio_clip:
                video_clip = video_clip.with_audio(audio_clip)
                
            clips.append(video_clip)
            
        final_video = concatenate_videoclips(clips)
        final_video.write_videofile(self.output_path, fps=24, codec='libx264', audio_codec='aac')

# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="Beamer to Video Converter")
    parser.add_argument("tex_file", help="Path to .tex file")
    parser.add_argument("--pdf", help="Path to existing PDF (optional)")
    parser.add_argument("--tts", choices=['gtts', 'gcloud'], default='gtts', help="TTS Provider")
    parser.add_argument("--force", action="store_true", help="Force regeneration of audio/images (clean cache)")
    
    args = parser.parse_args()
    
    tex_path = Path(args.tex_file)
    if not tex_path.exists():
        print(f"❌ File not found: {tex_path}")
        return
        
    # Default outputs
    pdf_path = Path(args.pdf) if args.pdf else tex_path.with_suffix(".pdf")
    output_video = args.output if args.output else f"{tex_path.stem}_video.mp4"
    
    work_dir = tex_path.parent / "video_work"
    
    if args.force and work_dir.exists():
        print("🧹 Cleaning work directory...")
        import shutil
        shutil.rmtree(work_dir)
    
    # 1. Parse Notes
    print(f"📖 Parsing Notes from: {tex_path}")
    bp = BeamerParser(str(tex_path))
    frames = bp.parse()
    
    # 2. Rasterize PDF
    if not pdf_path.exists():
        print(f"❌ PDF not found: {pdf_path}. Please compile your latex first.")
        return
        
    work_dir = tex_path.parent / "video_work"
    work_dir.mkdir(exist_ok=True)
    images_dir = work_dir / "images"
    audio_dir = work_dir / "audio"
    images_dir.mkdir(exist_ok=True)
    audio_dir.mkdir(exist_ok=True)
    
    pdf_proc = PDFProcessor(str(pdf_path))
    image_paths = pdf_proc.to_images(images_dir)
    print(f"📸 Extracted {len(image_paths)} frames from PDF.")
    
    # 3. Generate Audio & Map
    # Mapping Strategy:
    # A 'Frame' in our parser corresponds to a \note{} block.
    # Usually a \note{} block corresponds to a PDF slide (visual state).
    # But overlays (<+->) create multiple PDF pages for one \frame environment.
    # And we assumed [click] markers advance the visual state.
    
    # Let's align:
    # We have N PDF images (visual states).
    # We have M Note Blocks (one per \note{}).
    # Inside each Note Block, we have K segments (split by [click]).
    
    # Total logical steps = Sum(segments in all blocks).
    # We expect Total Logical Steps == Total PDF Images.
    
    # Flatten the audio segments
    all_segments = []
    for f in frames:
        all_segments.extend(f.audio_segments)
        
    print(f"Found {len(all_segments)} audio segments (narration chunks).")
    
    if len(all_segments) > len(image_paths):
        print(f"⚠️ Warning: More audio segments ({len(all_segments)}) than images ({len(image_paths)}). Video might be cutoff.")
    elif len(all_segments) < len(image_paths):
        print(f"⚠️ Warning: More images ({len(image_paths)}) than audio segments ({len(all_segments)}). Trailing images will be silent.")
        
    audio_gen = AudioGenerator(audio_dir, provider=args.tts)
    
    # Map: image_index -> [audio_path1, audio_path2...]
    # Actually, usually 1 segment = 1 image.
    # But we might want to support multiple segments per image if [click] isn't present?
    # No, our parser splits by [click]. If no [click], it's one big text -> 1 image.
    # If [click] is present, it splits -> multiple segments -> multiple images.
    
    audio_map = []
    
    for i, seg in enumerate(all_segments):
        if i >= len(image_paths):
            break
            
        audio_path = audio_gen.generate(seg.text, seg.speaker, i)
        audio_map.append([audio_path])
        
    # 4. Stitch
    stitcher = VideoStitcher(str(output_video))
    stitcher.stitch(image_paths, audio_map)
    
    print(f"✅ Comparison Video Created: {output_video}")

if __name__ == "__main__":
    main()
