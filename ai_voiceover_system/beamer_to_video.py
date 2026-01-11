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
    new_visual: bool = False  # True if this segment triggers a new PDF slide

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
        cursor = 0
        frame_counter = 0
        
        while True:
            start_idx = self.content.find("\\note{", cursor)
            if start_idx == -1:
                break
            
            content_start = start_idx + 6 
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
            
            note_content = note_content.strip()
            if not note_content:
                continue
                
            segments = self._parse_note_content(note_content)
            frames.append(FrameData(frame_index=frame_counter, audio_segments=segments))
            frame_counter += 1
            
        return frames

    def _parse_note_content(self, text: str) -> List[AudioSegment]:
        # Logic:
        # 1. Split by [click] -> logical visual steps.
        # 2. Inside each step, split by Lines/Speakers -> logical audio chunks.
        
        raw_visual_steps = re.split(r'\[click\]', text, flags=re.IGNORECASE)
        
        parsed_segments = []
        
        for i, step in enumerate(raw_visual_steps):
            step = step.strip()
            if not step:
                # Can happen if [click] is at start
                continue
            
            # This step corresponds to ONE visual state (image).
            # We assume "One Speaker Per Line" as requested by user.
            # So we split by newlines.
            
            lines = step.split('\n')
            
            first_sub_segment = True
            
            current_speaker = None
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                # Check for "Name: Text"
                match = re.match(r'^([A-Za-z\s\.]+):\s*(.+)', line)
                if match:
                    current_speaker = match.group(1).strip()
                    content = match.group(2).strip()
                else:
                    # Continuation of previous speaker? Or narrator?
                    content = line
                    # Keep current_speaker
                
                # New audio segment
                # Only the VERY first segment of the `step` gets new_visual=True
                is_visual_start = (i == 0 or (i > 0)) and first_sub_segment
                # Wait logic check:
                # `step` comes from `re.split([click])`.
                # If we have `[click] Step1`, then Step1 is new visual.
                # If we have `Start [click] Next`, Start is new (visual #0), Next is new (visual #1).
                # So yes, every `step` iteration implies a new visual block (except maybe the very first if no click?)
                
                # Actually, `re.split` gives:
                # "Text1 [click] Text2" -> ["Text1", "Text2"]
                # Text1 is associated with image N.
                # Text2 is associated with image N+1.
                # So the FIRST segment of "Text1" has new_visual=True (if it's the start of the note block).
                # The FIRST segment of "Text2" has new_visual=True (because of [click]).
                
                # So logic: 
                # For each `step`: The first audio segment defined in it gets `new_visual=True`.
                # Subsequent lines in matching `step` get `new_visual=False`.
                
                parsed_segments.append(AudioSegment(text=content, speaker=current_speaker, new_visual=first_sub_segment))
                first_sub_segment = False

        return parsed_segments

# --- PDF Processor and Audio Generator (UNCHANGED) ---
# ... (PDFProcessor and AudioGenerator classes omitted for brevity in tool call, usually we'd keep them or use multi_replace but replace_file_content is full file or range)
# Assuming user wants me to patch the file, I will provide the context carefully.
# Wait, I must provide START and END line for replace_file_content.
# I will rewrite the Parser class and the top Data/Structs.

# --- Video Stitcher ---
# We need to change the stitching mapping logic in MAIN.

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

    def to_images(self, output_dir: Path, target_width: int = 1920) -> List[Path]:
        doc = fitz.open(self.pdf_path)
        
        # Calculate scale factor based on first page to match target width exactly
        page0 = doc[0]
        # page.rect.width is in points
        zoom = target_width / page0.rect.width
        mat = fitz.Matrix(zoom, zoom)
        
        print(f"🖼️ Rasterizing PDF (PyMuPDF): {self.pdf_path}")
        print(f"   Input Width: {page0.rect.width:.2f}pts -> Target: {target_width}px (Zoom: {zoom:.4f})")
        
        image_paths = []
        
        for i, page in enumerate(doc):
            # Use matrix for precise scaling (avoiding integer DPI rounding errors)
            pix = page.get_pixmap(matrix=mat) 
            
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
        gender = texttospeech.SsmlVoiceGender.FEMALE
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
    from moviepy import ImageClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False

class VideoStitcher:
    def __init__(self, output_path: str):
        self.output_path = output_path
        if not MOVIEPY_AVAILABLE:
            raise ImportError("moviepy not installed. Please install: pip install moviepy")

    def stitch(self, image_paths: List[Path], audio_map: List[List[Path]], is_4k: bool = False):
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
                audio_clip = concatenate_audioclips(audio_objs) if len(audio_objs) > 1 else audio_objs[0]
                duration = audio_clip.duration
            
            # Create Image Clip
            # Note: ImageClip accepts path as string
            video_clip = ImageClip(str(img_path)).with_duration(duration)
            
            if audio_clip:
                video_clip = video_clip.with_audio(audio_clip)
                
            clips.append(video_clip)
            
        final_video = concatenate_videoclips(clips)
        
        # Quality Settings
        audio_bitrate = '320k'
        video_bitrate = '50000k' if is_4k else '8000k' # 50Mbps for 4k, 8Mbps for 1080p
        preset = 'slow' # Better compression
        
        print(f"⚙️  Encoding: {video_bitrate} video, {audio_bitrate} audio, preset={preset}")
        final_video.write_videofile(
            self.output_path, 
            fps=24, 
            codec='libx264', 
            audio_codec='aac', 
            audio_bitrate=audio_bitrate,
            bitrate=video_bitrate,
            preset=preset
        )

# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="Beamer to Video Converter")
    parser.add_argument("tex_file", help="Path to .tex file")
    parser.add_argument("--pdf", help="Path to existing PDF (optional)")
    parser.add_argument("--tts", choices=['gtts', 'gcloud'], default='gtts', help="TTS Provider")
    parser.add_argument("--output", help="Output video filename")
    parser.add_argument("--force", action="store_true", help="Force regeneration of audio/images (clean cache)")
    parser.add_argument("--resolution", choices=['720p', '1080p', '4k'], default='1080p', help="Output resolution (default: 1080p)")
    
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
    
    # Calculate DPI based on first page dimensions
    # DPI = (Target Px / Width Inches)
    # Width Inches = Width Points / 72
    
    # We pass target_width to PDFProcessor instead of calculating DPI here
    target_width = 1920
    if args.resolution == '4k':
        target_width = 3840
    elif args.resolution == '720p':
        target_width = 1280
        
    print(f"🎯 Target Width: {target_width}px ({args.resolution})")
    
    image_paths = pdf_proc.to_images(images_dir, target_width=target_width)
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
        
    # Calculate logical visual steps
    visual_steps = sum(1 for seg in all_segments if seg.new_visual)
    
    print(f"Found {len(all_segments)} audio segments across {visual_steps} logical visual steps.")
    
    if visual_steps > len(image_paths):
        print(f"⚠️ Warning: More visual steps ({visual_steps}) than images ({len(image_paths)}). Video might be cutoff.")
    elif visual_steps < len(image_paths):
         print(f"⚠️ Warning: More images ({len(image_paths)}) than visual steps ({visual_steps}). Trailing images will be silent.")
        
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
        
    # Map: image_index -> [audio_path1, audio_path2...]
    # Using new_visual flag to handle multiple segments per image.
    
    audio_map = []
    # Pre-fill audio_map with empty lists for each image
    for _ in range(len(image_paths)):
        audio_map.append([])
        
    current_image_idx = -1
    
    for i, seg in enumerate(all_segments):
        # Generate Audio
        audio_path = audio_gen.generate(seg.text, seg.speaker, i)
        
        # Determine placement
        if seg.new_visual:
            current_image_idx += 1
            
        if current_image_idx >= len(image_paths):
            print(f"⚠️ Warning: Audio segment {i} ('{seg.text[:20]}...') exceeds available images ({len(image_paths)}). Skipping visual sync.")
            break
            
        # Ensure we don't write before first image
        target_idx = max(0, current_image_idx)
        audio_map[target_idx].append(audio_path)
    
    # 4. Stitch
    stitcher = VideoStitcher(str(output_video))
    
    is_4k = (args.resolution == '4k')
    stitcher.stitch(image_paths, audio_map, is_4k=is_4k)
    
    print(f"✅ Comparison Video Created: {output_video}")

if __name__ == "__main__":
    main()
