#!/usr/bin/env python3
import os
import re
import sys
import json
import time
import shutil
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

# Dependency Checks
try:
    from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
    MOVIEPY_AVAILABLE = True
except ImportError:
    print("❌ MoviePy v2 not found. Please install: pip install moviepy")
    MOVIEPY_AVAILABLE = False

try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False

try:
    from google.cloud import texttospeech
    import google.auth
    GCLOUD_AVAILABLE = True
except ImportError:
    GCLOUD_AVAILABLE = False

# Configuration
GCLOUD_DEFAULT_VOICE_MALE = "en-US-Studio-M"
GCLOUD_DEFAULT_VOICE_FEMALE = "en-US-Studio-O"

class SlidevVideoGenerator:
    def __init__(self, input_file, tts_provider='auto', voice=None, 
                 with_clicks=True, cleanup=True, timeout=120000):
        self.input_file = Path(input_file).resolve()
        self.work_dir = self.input_file.parent
        self.project_root = self.input_file.parent.parent # Assuming data structure slidev/project/slides.md
        
        # Audio/Video Config
        self.tts_provider = tts_provider
        self.custom_voice = voice
        self.with_clicks = with_clicks
        self.cleanup = cleanup
        self.export_timeout = timeout
        
        # Paths
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.temp_dir = self.work_dir / f"temp_gen_{self.timestamp}"
        self.excludes_dir = self.temp_dir / "slides"
        self.audio_dir = self.temp_dir / "audio"
        self.output_video = self.work_dir / f"{self.input_file.stem}_video.mp4"
        
        # GCloud Client
        self.gcloud_client = None
        self.gcloud_project_id = None
        
        # State
        self.processing_mode = 'slide' # 'slide' or 'click'
        self.speaker_mode = 'mono' # 'mono' or 'multi'
        self.temp_files = []

    def run(self, max_slides=None):
        """Main execution flow"""
        if not MOVIEPY_AVAILABLE:
            return False

        print(f"🚀 Starting Video Generation for: {self.input_file.name}")
        
        # 1. Setup
        self._setup_directories()
        
        # 2. Parse Content & Detect Modes
        # We parse first to determine speaker mode (Mono/Multi)
        slides_data = self._parse_slidev_file(max_slides)
        if not slides_data:
            print("❌ No content found to process")
            return False

        # 3. Initialize Services (Now dependent on detected mode)
        self._initialize_tts()

        print(f"📊 Detected Modes: {self.processing_mode.upper()} Sync | {self.speaker_mode.upper()} Speaker")
        
        # 4. Export Slides
        if not self._export_slides():
            return False
            
        # 4. Generate Audio & Video Clips
        video_clips = []
        total_duration = 0
        
        # Map exported images
        image_map = self._map_slide_images()
        
        print("\n🎬 Generating Clips...")
        for slide in slides_data:
            print(f"   Processing Slide {slide['number']}: {slide.get('title', 'Unknown')}")
            
            # Identify segments based on mode
            segments = slide.get('click_segments') if self.processing_mode == 'click' else [{'click': 0, 'narration': slide['narration']}]
            
            if not segments:
                print(f"      ⚠️ No narration found, skipping audio.")
                # We could add a silent clip here if needed, but for now skipping
                continue

            for segment in segments:
                # Get Image
                img_path = self._get_image_for_segment(slide['number'], segment.get('click', 0), image_map)
                if not img_path:
                    print(f"      ⚠️ Missing image for Slide {slide['number']} Click {segment.get('click', 0)} - Skipping segment")
                    continue
                
                # Generate Audio
                narration = segment['narration']
                if not narration.strip():
                    continue

                audio_path = self.audio_dir / f"s{slide['number']}_c{segment.get('click', 0)}.mp3"
                
                if self.speaker_mode == 'multi':
                    success = self._generate_multispeaker_audio(narration, audio_path)
                else:
                    success = self._generate_monospeaker_audio(narration, audio_path)
                
                if success:
                    try:
                        clip = self._create_video_clip(img_path, audio_path)
                        video_clips.append(clip)
                        total_duration += clip.duration
                        print(f"      ✅ Segment {segment.get('click', 0)} ({clip.duration:.1f}s)")
                    except Exception as e:
                        print(f"      ❌ Clip creation failed: {e}")
                else:
                    print("      ❌ Audio generation failed")

        # 5. Assemble Video
        if video_clips:
            self._assemble_video(video_clips, total_duration)
        else:
            print("❌ No clips generated.")

        # 6. Cleanup
        if self.cleanup:
            self._cleanup()

    def _setup_directories(self):
        os.makedirs(self.excludes_dir, exist_ok=True)
        os.makedirs(self.audio_dir, exist_ok=True)

    def _initialize_tts(self):
        # We need GCloud if explicitly requested OR matches criteria (Multi-speaker / No gTTS)
        should_init_gcloud = (
            self.tts_provider == 'gcloud' or 
            (self.tts_provider == 'auto' and (not GTTS_AVAILABLE or self.speaker_mode == 'multi'))
        )

        if should_init_gcloud and GCLOUD_AVAILABLE:
            try:
                credentials, project_id = google.auth.default()
                self.gcloud_client = texttospeech.TextToSpeechClient(credentials=credentials)
                self.gcloud_project_id = project_id
                print("☁️  GCloud TTS Initialized")
            except Exception as e:
                print(f"⚠️ GCloud Init Failed: {e}")
                
        # Fallback check for Auto: If Multi-speaker detected but GCloud failed, revert to Mono
        if self.speaker_mode == 'multi' and not self.gcloud_client:
            if self.tts_provider == 'auto':
                 print("⚠️  Warning: Multi-speaker detected but GCloud not available. Falling back to MONO (gTTS).")
                 self.speaker_mode = 'mono'
            else:
                 print("❌ Error: Multi-speaker detected but GCloud initialization failed.")

    def _export_slides(self):
        print("\n🖼️  Exporting Slides via Slidev...")
        
        # Check if we are in a valid Slidev project (simplified check)
        if not (self.work_dir / 'package.json').exists() and not (self.project_root / 'package.json').exists():
             print("⚠️  Warning: package.json not found nearby. 'npx slidev' might fail.")

        cmd = [
            "npx", "slidev", "export", 
            str(self.input_file),
            "--output", str(self.excludes_dir),
            "--format", "png",
            "--timeout", str(self.export_timeout)
        ]
        
        if self.with_clicks:
            cmd.append("--with-clicks")
            
        print(f"   Executing: {' '.join(cmd)}")
        
        try:
            # We run this in the directory of the slides to ensure dependencies resolve if local
            result = subprocess.run(cmd, cwd=self.work_dir, capture_output=True, text=True)
            
            if result.returncode != 0:
                print("❌ Export Failed:")
                print(result.stderr)
                return False
                
            print("✅ Export Complete")
            return True
        except Exception as e:
             print(f"❌ Export Execution Error: {e}")
             return False

    def _parse_slidev_file(self, max_slides=None):
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()

        if '[click]' in content and self.with_clicks:
            self.processing_mode = 'click'



        # Robust split (handling frontmatter and code blocks)
        # We cannot use simple regex split because '---' can appear inside code blocks (e.g. YAML examples)
        slides, _ = self._parse_items_recursive(content, os.path.dirname(self.input_file), max_slides)
        return slides

    def _parse_items_recursive(self, content, base_dir, max_slides=None, current_count=0):
        """Recursively key items from content, handling src: imports."""
        sections = self._split_content_robust(content)
        parsed_slides = []
        
        # Determine where to start processing
        # If the file starts with '---', sections[0] is empty, and sections[1] is Frontmatter/Config.
        # We should skip S0 and S1, UNLESS S1 contains 'src:' (Global Import).
        # If file starts with content (no '---'), S0 is the first slide.
        
        start_index = 0
        if sections and not sections[0].strip():
            # File started with ---
            # Check S1
            if len(sections) > 1:
                has_src = re.search(r'^\s*src:\s+', sections[1], re.MULTILINE)
                if has_src:
                    # S1 is a valid slide/import defined in frontmatter block style
                    start_index = 1
                else:
                    # S1 is just configuration (theme, title, etc) -> Skip S0 and S1
                    start_index = 2
            else:
                 start_index = 1 # Just empty start?
        
        for i, section in enumerate(sections):
            if i < start_index:
                continue
                
            # Skip empty sections
            if not section.strip():
                continue

            # Check for Import (src: ...)
            src_match = re.search(r'^\s*src:\s+(.*)', section, re.MULTILINE)
            if src_match:
                import_path = src_match.group(1).strip()
                full_import_path = os.path.join(base_dir, import_path)
                
                if os.path.exists(full_import_path):
                    print(f"   ↪ Parsing imported slides from: {import_path}")
                    with open(full_import_path, 'r', encoding='utf-8') as f:
                        imported_content = f.read()
                        
                        # Recurse
                        imported_items, new_count = self._parse_items_recursive(
                            imported_content, 
                            os.path.dirname(full_import_path), 
                            max_slides, 
                            current_count
                        )
                        parsed_slides.extend(imported_items)
                        current_count = new_count
                        if max_slides and current_count >= max_slides:
                            break
                continue

            # Check for title to protect content slides
            has_title = re.search(r'^#\s', section, re.MULTILINE)

            # Skip config/setup (ONLY if no title found)
            if not has_title and (
                re.search(r'^\s*theme:\s+', section, re.MULTILINE) or 
                re.search(r'^\s*layout:\s+', section, re.MULTILINE) or
                re.search(r'^\s*transition:\s+', section, re.MULTILINE) or
                re.search(r'^\s*level:\s+', section, re.MULTILINE) or
                # src handled above
                re.search(r'^\s*foo:\s+', section, re.MULTILINE) or
                re.search(r'^\s*dragPos:\s+', section, re.MULTILINE) or
                re.search(r'^\s*class:\s+', section, re.MULTILINE) or
                ('background:' in section and 'title:' in section and '# ' not in section)):
                continue
                
            current_count += 1
            
            if max_slides and current_count > max_slides:
                break
                
            # Parse the slide note: The slide number is current_count
            slide_data = self._parse_single_slide(section, current_count)
            if slide_data:
                parsed_slides.append(slide_data)
        
        if max_slides:
             # Just returning the count needed for recursion context
             pass
             
        return parsed_slides, current_count

    def _parse_slidev_file_wrapper(self, max_slides=None):
        """Wrapper to maintain signature if needed, but we replaced the body above"""
        pass

    def _split_content_robust(self, content):
        """Split content by '---' separators, but ignore those inside code blocks."""
        lines = content.split('\n')
        sections = []
        current_section = []
        in_code_block = False
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            
            # Toggle code block state
            if stripped.startswith('```'):
                in_code_block = not in_code_block
            
            # Check for separator
            # Must be '---', not inside code block
            is_separator = (stripped == '---' and not in_code_block)
            
            if is_separator:
                # If it's a separator, push current section
                if current_section:
                    sections.append('\n'.join(current_section))
                else:
                    sections.append('') # Empty section (e.g. frontmatter start)
                
                current_section = []
            else:
                current_section.append(line)
        
        # Append final section
        if current_section:
            sections.append('\n'.join(current_section))
            
        return sections

    def _parse_single_slide(self, content, number):
        data = {'number': number, 'raw': content, 'title': '', 'narration': '', 'click_segments': []}
        
        data['title'] = ''
        lines = content.strip().split('\n')
        for line in lines:
            if line.startswith('# '):
                data['title'] = line[2:].strip()
                break
        
        # Extract Notes (Find the comment that looks like speaker notes)
        notes_matches = re.findall(r'<!--\s*(.*?)\s*-->', content, re.DOTALL)
        if not notes_matches:
            return data
            
        # Heuristic: The speaker notes block usually contains "[click]" or "Speaker:"
        # or is the longest block if multiple are found.
        # We search from the end backwards.
        speaker_notes = ""
        for note in reversed(notes_matches):
            if '[click]' in note or re.search(r'(?:Dr\. James|Sarah|Speaker \d):', note):
                speaker_notes = note.strip()
                break
        
        # Fallback: If no markers, take the last comment if it's substantial (e.g., > 100 chars)
        # effectively ignoring short config comments like <!-- step 4 -->
        if not speaker_notes and len(notes_matches[-1].strip()) > 50:
             speaker_notes = notes_matches[-1].strip()

        if not speaker_notes: 
             return data
             
        data['narration'] = speaker_notes
        
        # Check for Multispeaker in this slide (ONLY if using GCloud or Auto)
        if self.tts_provider in ['gcloud', 'auto'] and re.search(r'(?:Dr\. James|Sarah|Speaker \d):', speaker_notes):
            self.speaker_mode = 'multi'
            
        # Parse Clicks if enabled
        if self.processing_mode == 'click':
            parts = re.split(r'\[click(?::(\d+))?\]', speaker_notes)
            current_click = 0
            
            # Initial segment (before first click)
            if parts[0].strip():
                data['click_segments'].append({'click': 0, 'narration': parts[0].strip()})
                
            i = 1
            while i < len(parts):
                click_idx = parts[i]
                text = parts[i+1] if i+1 < len(parts) else ""
                
                if click_idx: current_click = int(click_idx)
                else: current_click += 1
                
                if text.strip():
                    data['click_segments'].append({'click': current_click, 'narration': text.strip()})
                
                i += 2
            
            # Sort
            data['click_segments'].sort(key=lambda x: x['click'])
            
        return data

    def _map_slide_images(self):
        images = sorted(list(self.excludes_dir.glob("*.png")))
        mapping = {} # {slide_num: {click_num: path}}
        
        for img in images:
            # Format: 001.png or 001-02.png
            match = re.match(r'(\d+)(?:-(\d+))?\.png', img.name)
            if match:
                s_num = int(match.group(1))
                # Slidev exports steps starting at 01 (initial state = click 0)
                # So 01 -> Click 0, 02 -> Click 1
                c_num = int(match.group(2)) - 1 if match.group(2) else 0 
                
                if s_num not in mapping: mapping[s_num] = {}
                mapping[s_num][c_num] = img.resolve()
        
        return mapping

    def _get_image_for_segment(self, slide_num, click_num, mapping):
        if slide_num not in mapping:
            return None
        
        # Exact match
        if click_num in mapping[slide_num]:
            return mapping[slide_num][click_num]
            
        # Fallback to nearest previous click
        available = sorted(mapping[slide_num].keys())
        prev = [c for c in available if c <= click_num]
        if prev:
            return mapping[slide_num][prev[-1]]
            
        return None

    def _generate_monospeaker_audio(self, text, output_path):
        # Strip speaker tags for mono mode
        clean_text = re.sub(r'(?:Dr\. James|Sarah|Speaker \d+):\s*', '', text).strip()
        if not clean_text: return False
        
        # Provider selection
        provider = self.tts_provider
        if provider == 'auto':
            provider = 'gtts' if GTTS_AVAILABLE else 'gcloud'

        if provider == 'gtts' and GTTS_AVAILABLE:
            try:
                tts = gTTS(text=clean_text, lang='en', tld='co.uk')
                tts.save(str(output_path))
                return True
            except Exception as e:
                print(f"      ❌ gTTS Error: {e}")
                return False
                
        elif (provider == 'gcloud' or provider == 'auto') and self.gcloud_client:
            return self._call_gcloud(clean_text, output_path, self.custom_voice or GCLOUD_DEFAULT_VOICE_MALE)
            
        return False

    def _generate_multispeaker_audio(self, text, output_path):
        if not self.gcloud_client:
            print("      ❌ GCloud required for multispeaker but not initialized.")
            return False
            
        # Parse dialogue
        segments = []
        # Regex to split by Speaker: Text
        parts = re.split(r'(Dr\. James|Sarah):', text)
        
        current_speaker = "Dr. James" # Default
        
        if parts[0].strip():
             segments.append((current_speaker, parts[0].strip()))
             
        i = 1
        while i < len(parts):
            speaker = parts[i]
            content = parts[i+1] if i+1 < len(parts) else ""
            if content.strip():
                segments.append((speaker, content.strip()))
            i += 2
            
        # Generate audio for each part and combine
        temp_clips = []
        for idx, (speaker, content) in enumerate(segments):
            voice = GCLOUD_DEFAULT_VOICE_FEMALE if "Sarah" in speaker else GCLOUD_DEFAULT_VOICE_MALE
            part_path = output_path.parent / f"{output_path.stem}_part{idx}.mp3"
            
            if self._call_gcloud(content, part_path, voice):
                temp_clips.append(str(part_path))
                
        # Combine clips using MoviePy (AudioFileClip doesn't support direct concatenation easily without ffmpeg or pydub, 
        # so we'll use MoviePy's concatenate_audioclips if possible, or just file concatenation if same format)
        if temp_clips:
            # Simple file concatenation for MP3 (works generally)
            with open(output_path, 'wb') as outfile:
                for clip_path in temp_clips:
                    with open(clip_path, 'rb') as infile:
                        outfile.write(infile.read())
            return True
            
        return False

    def _call_gcloud(self, text, output_path, voice_name):
        try:
            synthesis_input = texttospeech.SynthesisInput(text=text)
            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US",
                name=voice_name
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3
            )
            response = self.gcloud_client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )
            with open(output_path, "wb") as out:
                out.write(response.audio_content)
            return True
        except Exception as e:
            print(f"      ❌ GCloud Error: {e}")
            return False

    def _create_video_clip(self, image_path, audio_path):
        audio = AudioFileClip(str(audio_path))
        image = ImageClip(str(image_path), duration=audio.duration)
        if hasattr(image, 'with_audio'):
            return image.with_audio(audio)
        else:
            return image.set_audio(audio)

    def _assemble_video(self, clips, duration):
        print(f"\nExample: 📼 Assembling {len(clips)} clips ({duration:.1f}s)...")
        
        if clips:
            print(f"   ▶ Clip 0 (Start): {clips[0].duration:.2f}s, Res: {clips[0].size}")

        # Use compose to handle potential resolution mismatches
        final = concatenate_videoclips(clips, method="compose")
        final.write_videofile(
            str(self.output_video),
            fps=24,
            codec='libx264',
            audio_codec='aac',
            logger=None 
        )
        print(f"\n✨ Video Saved: {self.output_video}")

    def _cleanup(self):
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)
            print("🧹 Parsed temp files removed.")

def main():
    parser = argparse.ArgumentParser(description="Unified Slidev to Video Converter")
    parser.add_argument("input", help="Path to slidev.md file")
    parser.add_argument("--tts", choices=['auto', 'gtts', 'gcloud'], default='auto')
    parser.add_argument("--voice", help="Custom GCloud voice name")
    parser.add_argument("--no-clicks", action="store_true", help="Disable click synchronization")
    parser.add_argument("--no-cleanup", action="store_true", help="Keep temporary files")
    parser.add_argument("--max-slides", type=int, help="Max slides to process")
    
    args = parser.parse_args()
    
    gen = SlidevVideoGenerator(
        args.input,
        tts_provider=args.tts,
        voice=args.voice,
        with_clicks=not args.no_clicks,
        cleanup=not args.no_cleanup
    )
    
    gen.run(max_slides=args.max_slides)

if __name__ == "__main__":
    main()
