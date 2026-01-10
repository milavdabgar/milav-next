#!/usr/bin/env python3
"""
Slidev Multi-Speaker Video Processor
===================================

Enhanced video processor with Google Cloud TTS multispeaker and SSML support:
- Multi-speaker conversations with distinct voices
- Advanced SSML markup for natural speech patterns
- Google Cloud TTS client library integration
- Professional podcast-style educational content

Usage:
    python slidev_multispeaker_processor.py <slidev_file.md> [max_slides]
"""

import os
import sys
import re
import subprocess
import argparse
import time
from pathlib import Path
import xml.etree.ElementTree as ET

# Set TTS environment
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.expanduser('~/.config/gcloud/application_default_credentials.json')

# Import dependencies with availability tracking
try:
    # Try MoviePy v2 import structure first
    from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
    MOVIEPY_AVAILABLE = True
except ImportError:
    try:
        # Fallback to MoviePy v1 structure
        from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
        MOVIEPY_AVAILABLE = True
    except ImportError:
        MOVIEPY_AVAILABLE = False

try:
    from google.cloud import texttospeech_v1beta1 as texttospeech
    GCLOUD_TTS_CLIENT_AVAILABLE = True
except ImportError:
    GCLOUD_TTS_CLIENT_AVAILABLE = False

class SlidevMultiSpeakerProcessor:
    """Enhanced processor with multi-speaker TTS and SSML support"""
    
    def __init__(self, slidev_file, with_clicks=False):
        self.slides_dir = "temp_multispeaker_slides"
        self.slidev_md_file = slidev_file
        self.temp_audio_files = []
        self.processing_mode = 'click' if with_clicks else 'slide'
        self.tts_client = None
        self.with_clicks = with_clicks
        
        print("🎯 Slidev Multi-Speaker Video Processor")
        print("=" * 50)
        self._display_capabilities()
        self._initialize_tts_client()
    
    def _display_capabilities(self):
        """Display available capabilities"""
        print(f"📦 Available Components:")
        print(f"   ✅ MoviePy: {MOVIEPY_AVAILABLE}")
        print(f"   {'✅' if GCLOUD_TTS_CLIENT_AVAILABLE else '❌'} Google Cloud TTS Client: {GCLOUD_TTS_CLIENT_AVAILABLE}")
        print(f"   🎤 Multi-Speaker Support: {GCLOUD_TTS_CLIENT_AVAILABLE}")
        print(f"   🎭 SSML Support: {GCLOUD_TTS_CLIENT_AVAILABLE}")
    
    def _initialize_tts_client(self):
        """Initialize Google Cloud TTS client"""
        if not GCLOUD_TTS_CLIENT_AVAILABLE:
            print("❌ Google Cloud TTS client library not available")
            return False
        
        try:
            print("☁️ Initializing Google Cloud TTS Client...")
            self.tts_client = texttospeech.TextToSpeechClient()
            print("   ✅ Google Cloud TTS Client ready")
            print("   🎭 Multi-speaker voices available")
            print("   🎤 SSML markup supported")
            return True
        except Exception as e:
            print(f"   ❌ Google Cloud TTS Client initialization error: {str(e)}")
            return False
    
    def _split_slides_correctly(self, content):
        """Split slides correctly by finding real slide separators, not markdown table syntax"""
        lines = content.split('\n')
        sections = []
        current_section = []
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Check if this is a slide separator: '---' on its own line
            if line == '---':
                # Check context - is this a real slide separator?
                prev_line = lines[i-1].strip() if i > 0 else ""
                next_line = lines[i+1].strip() if i < len(lines)-1 else ""
                
                # Real slide separator patterns:
                # 1. At very start of file (i==0)
                # 2. After HTML comment, before empty line or YAML  
                # 3. After empty line, before YAML or content
                # 4. At end of file
                is_slide_separator = (
                    # Pattern 1: Very first line of file
                    i == 0 or
                    # Pattern 2: After content/comment, before YAML or empty line
                    (prev_line == "" or prev_line.startswith("<!--") or prev_line.endswith("-->")) and 
                    (next_line == "" or ':' in next_line or next_line.startswith('#')) or
                    # Pattern 3: At end of file
                    i == len(lines)-1
                )
                
                # Additional check: if we're in a markdown table, don't split
                in_table = False
                for j in range(max(0, i-5), min(len(lines), i+5)):
                    if '|' in lines[j] and ('---' in lines[j] or 'kbd>' in lines[j]):
                        in_table = True
                        break
                
                if is_slide_separator and not in_table:
                    # This is a real slide separator
                    if current_section:
                        sections.append('\n'.join(current_section))
                        current_section = []
                    # Don't include the separator line itself
                else:
                    # This is just content (like table separator)
                    current_section.append(lines[i])
            else:
                current_section.append(lines[i])
            
            i += 1
        
        # Add the last section
        if current_section:
            sections.append('\n'.join(current_section))
        
        return sections
    
    def detect_processing_mode(self, slidev_file):
        """Detect whether to use click-based or slide-based processing"""
        if not os.path.exists(slidev_file):
            return 'slide'
        
        with open(slidev_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for [click] markers in presenter notes
        click_markers = re.findall(r'\[click(?::\d+)?\]', content)
        html_comments = re.findall(r'<!--.*?-->', content, re.DOTALL)
        
        if click_markers and html_comments:
            print(f"🖱️ Detected {len(click_markers)} click markers - Using CLICK-BASED processing")
            self.processing_mode = 'click'
            return 'click'
        else:
            print("📄 No click markers found - Using SLIDE-BASED processing")
            self.processing_mode = 'slide'
            return 'slide'
    
    def parse_click_notes(self, slidev_file):
        """Parse slidev markdown for [click] markers in presenter notes - FIXED FOR MARKDOWN TABLES"""
        if not os.path.exists(slidev_file):
            print(f"❌ Slidev file not found: {slidev_file}")
            return []

        with open(slidev_file, 'r', encoding='utf-8') as f:
            content = f.read()

        slide_data_list = []
        slide_counter = 1
        
        # Use the improved splitting that handles markdown tables correctly
        sections = self._split_slides_correctly(content)
        
        i = 0
        while i < len(sections):
            section = sections[i].strip()
            
            if not section:
                i += 1
                continue
                
            # Handle Section 0 (global YAML + first slide)
            if i == 0:
                # Extract first slide content from Section 0 (same as slide-based parsing)
                first_slide_content = self._extract_first_slide_from_section_0(section)
                if first_slide_content:
                    slide_data = self._parse_slide_clicks(first_slide_content, slide_counter)
                    if slide_data:
                        slide_data_list.append(slide_data)
                        slide_counter += 1
                i += 1
                continue
                
            # Check if this section is slide YAML followed by content
            if self._is_slide_yaml_section(section):
                # This is slide YAML, next section should be content
                if i + 1 < len(sections):
                    slide_content = sections[i + 1].strip()
                    if slide_content:
                        # Combine YAML and content
                        full_slide = section + '\n---\n' + slide_content
                        slide_data = self._parse_slide_clicks(full_slide, slide_counter)
                        if slide_data:
                            slide_data_list.append(slide_data)
                            slide_counter += 1
                        i += 2  # Skip both YAML and content sections
                        continue
                        
            # This section contains slide content directly
            if '# ' in section or '<!--' in section:
                slide_data = self._parse_slide_clicks(section, slide_counter)
                if slide_data:
                    slide_data_list.append(slide_data)
                    slide_counter += 1
                    
            i += 1

        print(f"✅ Parsed {len(slide_data_list)} slides with click notes")
        return slide_data_list
    
    def _parse_slide_clicks(self, section, slide_number):
        """Parse individual slide section for [click] markers"""
        lines = section.strip().split('\n')
        
        slide_data = {
            'number': slide_number,
            'title': '',
            'click_segments': [],
            'raw_content': section.strip()
        }
        
        # Extract title
        for line in lines:
            line = line.strip()
            if line.startswith('# ') and not slide_data['title']:
                slide_data['title'] = line[2:].strip()
                break
        
        # Find HTML comment with presenter notes
        html_comment_pattern = r'<!--\s*(.*?)\s*-->'
        comment_matches = re.findall(html_comment_pattern, section, re.DOTALL)
        
        if not comment_matches:
            return slide_data if slide_data['title'] else None
        
        presenter_notes = comment_matches[-1].strip()
        
        # Parse click markers
        click_pattern = r'\[click(?::(\d+))?\]'
        parts = re.split(click_pattern, presenter_notes)
        
        current_click = 0
        
        # First part is always before any clicks (click 0)
        if parts[0].strip():
            slide_data['click_segments'].append({
                'click': 0,
                'narration': parts[0].strip(),
                'duration': None
            })
        
        # Process remaining parts
        i = 1
        while i < len(parts):
            click_num_str = parts[i] if parts[i] else None
            content = parts[i + 1] if i + 1 < len(parts) else ""
            
            if click_num_str:
                current_click = int(click_num_str)
            else:
                current_click += 1
            
            if content.strip():
                slide_data['click_segments'].append({
                    'click': current_click,
                    'narration': content.strip(),
                    'duration': None
                })
            
            i += 2
        
        slide_data['click_segments'].sort(key=lambda x: x['click'])
        return slide_data if slide_data['title'] or slide_data['click_segments'] else None
    
    def parse_multispeaker_content(self, narration_text):
        """Parse speaker dialogue and extract turns"""
        turns = []
        
        # Check if it's SSML format
        if narration_text.strip().startswith('<speak>'):
            try:
                # Parse SSML content
                root = ET.fromstring(narration_text)
                for voice_elem in root.findall('.//voice'):
                    voice_name = voice_elem.get('name', 'en-US-Studio-M')
                    speaker = 'R' if 'Studio-M' in voice_name else 'S'
                    
                    # Extract text content including SSML markup
                    voice_content = ET.tostring(voice_elem, encoding='unicode', method='xml')
                    # Remove outer voice tags but keep inner SSML
                    voice_content = re.sub(r'^<voice[^>]*>', '', voice_content)
                    voice_content = re.sub(r'</voice>$', '', voice_content)
                    
                    if voice_content.strip():
                        turns.append({
                            'text': voice_content.strip(),
                            'speaker': speaker,
                            'voice': 'en-US-Chirp3-HD-Algieba' if speaker == 'R' else 'en-US-Chirp3-HD-Achernar',
                            'is_ssml': True
                        })
                
                return turns if turns else [{'text': narration_text, 'speaker': 'R', 'voice': 'en-US-Chirp3-HD-Algieba', 'is_ssml': False}]
            
            except ET.ParseError as e:
                print(f"   ⚠️ SSML parsing failed: {e}")
                return [{'text': narration_text, 'speaker': 'R', 'voice': 'en-US-Chirp3-HD-Algieba', 'is_ssml': False}]
        
        # Check for simple speaker dialogue format
        lines = narration_text.strip().split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Parse "Speaker: text" format
            if ':' in line:
                speaker_part, text_part = line.split(':', 1)
                speaker_name = speaker_part.strip()
                text = text_part.strip()
                
                if 'Dr. James' in speaker_name or 'James' in speaker_name:
                    turns.append({
                        'text': text,
                        'speaker': 'R',
                        'voice': 'en-US-Chirp3-HD-Algieba',  # Male premium Chirp3-HD voice
                        'is_ssml': False
                    })
                elif 'Sarah' in speaker_name:
                    turns.append({
                        'text': text,
                        'speaker': 'S', 
                        'voice': 'en-US-Chirp3-HD-Achernar',  # Female premium Chirp3-HD voice
                        'is_ssml': False
                    })
            else:
                # Single speaker text
                turns.append({
                    'text': line,
                    'speaker': 'R',
                    'voice': 'en-US-Chirp3-HD-Algieba',
                    'is_ssml': False
                })
        
        return turns if turns else [{'text': narration_text, 'speaker': 'R', 'voice': 'en-US-Chirp3-HD-Algieba', 'is_ssml': False}]
    
    def generate_multispeaker_audio(self, narration_text, output_file):
        """Generate multi-speaker audio using individual Google Cloud TTS voices"""
        if not self.tts_client:
            print("   ❌ TTS client not available")
            return False
        
        try:
            print(f"   🎭 Generating multi-speaker audio...")
            
            # Parse the content for speakers
            turns = self.parse_multispeaker_content(narration_text)
            
            if len(turns) == 0:
                print("   ❌ No turns found")
                return False
                
            # Generate individual audio segments for each turn
            audio_segments = []
            temp_files = []
            
            for i, turn in enumerate(turns):
                temp_file = f"temp_turn_{i}_{int(time.time())}.wav"  # Use WAV for LINEAR16
                temp_files.append(temp_file)
                
                # Prepare synthesis input
                if turn['is_ssml']:
                    synthesis_input = texttospeech.SynthesisInput(ssml=f"<speak>{turn['text']}</speak>")
                else:
                    synthesis_input = texttospeech.SynthesisInput(text=turn['text'])
                
                # Use the specific voice for this speaker
                voice = texttospeech.VoiceSelectionParams(
                    language_code="en-US",
                    name=turn['voice']
                )
                
                # High-quality audio configuration matching Google TTS console
                audio_config = texttospeech.AudioConfig(
                    audio_encoding=texttospeech.AudioEncoding.LINEAR16,  # Uncompressed for quality
                    effects_profile_id=['small-bluetooth-speaker-class-device'],  # Better than headphone
                    speaking_rate=1.0,
                    pitch=0.0
                    # No volume_gain_db to avoid distortion
                )
                
                # Generate audio for this turn
                response = self.tts_client.synthesize_speech(
                    input=synthesis_input,
                    voice=voice,
                    audio_config=audio_config
                )
                
                # Save temporary audio file
                with open(temp_file, 'wb') as out:
                    out.write(response.audio_content)
                
                # Load the audio segment
                if os.path.exists(temp_file) and os.path.getsize(temp_file) > 100:
                    try:
                        # Using pydub to combine audio segments  
                        from pydub import AudioSegment
                        segment = AudioSegment.from_wav(temp_file)  # Load WAV (LINEAR16)
                        
                        # Light normalization only - preserve original quality
                        segment = segment.normalize()  # Just normalize, no aggressive boosting
                        
                        # Add a small pause between speakers
                        if i > 0:
                            silence = AudioSegment.silent(duration=300)  # 300ms pause
                            audio_segments.append(silence)
                        
                        audio_segments.append(segment)
                    except Exception as e:
                        print(f"   ❌ Error loading audio segment {i}: {e}")
                        return False
                else:
                    print(f"   ❌ Failed to generate audio for turn {i}")
                    return False
            
            # Combine all segments
            if audio_segments:
                from pydub import AudioSegment
                combined = AudioSegment.empty()
                for segment in audio_segments:
                    combined += segment
                
                # Final gentle normalization to maintain quality
                combined = combined.normalize()  # Just normalize, no additional gain
                
                # Export as high-quality MP3 to maintain original TTS quality
                combined.export(output_file, format="mp3", bitrate="320k")  # Highest quality MP3
                
                # Clean up temp files
                for temp_file in temp_files:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                
                if os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
                    speaker_voices = [f"{t['speaker']}:{t['voice']}" for t in turns]
                    print(f"      🎤 Individual voices: {', '.join(speaker_voices)}")
                    print(f"   ✅ Multi-speaker audio generated successfully")
                    return True
                else:
                    print(f"   ❌ Combined audio file too small or not created")
                    return False
            else:
                print(f"   ❌ No audio segments to combine")
                return False
            
        except Exception as e:
            print(f"   ❌ Multi-speaker TTS failed: {str(e)}")
            # Clean up temp files on error
            for temp_file in temp_files:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            return False
    
    def export_slides(self, slidev_file, with_clicks=False):
        """Export slides using slidev export command"""
        export_type = "click states" if with_clicks else "slides"
        print(f"📤 Exporting {export_type}...")
        
        if not os.path.exists(slidev_file):
            print(f"❌ Slidev file not found: {slidev_file}")
            return False
        
        os.makedirs(self.slides_dir, exist_ok=True)

        # Check if slides already exist
        existing_slides = list(Path(self.slides_dir).glob("*.png"))
        if existing_slides:
            print(f"   ⚠️ Found {len(existing_slides)} existing slides in {self.slides_dir}. Skipping export.")
            return True
        
        try:
            slidev_dir = os.path.dirname(slidev_file)
            slidev_filename = os.path.basename(slidev_file)
            
            export_cmd = [
                "npx", "slidev", "export", 
                slidev_filename,
                "--output", os.path.abspath(self.slides_dir),
                "--format", "png",
                "--timeout", "60000"
            ]
            
            if with_clicks:
                export_cmd.append("--with-clicks")
            
            print(f"   🚀 Running: {' '.join(export_cmd)}")
            
            result = subprocess.run(
                export_cmd,
                cwd=slidev_dir,
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                print(f"   ✅ {export_type.title()} exported successfully!")
                
                slide_files = list(Path(self.slides_dir).glob("*.png"))
                if slide_files:
                    print(f"   📊 Exported {len(slide_files)} {export_type}")
                    return True
                else:
                    print(f"   ❌ No PNG files found after export")
                    return False
            else:
                print(f"   ❌ Slidev export failed:")
                print(f"   Error: {result.stderr}")
                return False
                
        except subprocess.TimeoutExpired:
            print(f"   ❌ Slidev export timed out")
            return False
        except FileNotFoundError:
            print(f"   ❌ Slidev not found. Install with: npm install -g @slidev/cli")
            return False
        except Exception as e:
            print(f"   ❌ Export error: {str(e)}")
            return False
    
    def create_multispeaker_video(self, slidev_file, max_slides=None):
        """Create video using multi-speaker processing"""
        print("🎬 Multi-Speaker Video Creation")
        print("=" * 50)
        
        # Use the mode set during initialization
        if self.processing_mode == 'click':
            print("🖱️ Click-based processing enabled (--with-clicks)")
            return self._create_click_synchronized_multispeaker_video(slidev_file, max_slides)
        else:
            print("📄 Slide-based processing (default)")
            return self._create_slide_level_multispeaker_video(slidev_file, max_slides)
    
    def _create_click_synchronized_multispeaker_video(self, slidev_file, max_slides=None):
        """Create click-synchronized multi-speaker video"""
        print("🖱️ Creating click-synchronized multi-speaker video...")
        
        # Parse click notes
        click_data_list = self.parse_click_notes(slidev_file)
        if not click_data_list:
            print("❌ No click data found")
            return False
        
        if max_slides:
            click_data_list = click_data_list[:max_slides]
        
        # Export slides with clicks
        if not self.export_slides(slidev_file, with_clicks=True):
            print("❌ Failed to export click-state slides")
            return False
        
        return self._process_click_multispeaker_video(click_data_list, slidev_file)
    
    def _create_slide_level_multispeaker_video(self, slidev_file, max_slides=None):
        """Create slide-level multi-speaker video"""
        print("📄 Creating slide-level multi-speaker video...")
        
        # Export regular slides
        if not self.export_slides(slidev_file, with_clicks=False):
            print("❌ Failed to export slides")
            return False
        
        # Parse slide content
        slide_data_list = self.parse_slide_content(slidev_file)
        if not slide_data_list:
            print("❌ No slide content found")
            return False
        
        if max_slides:
            slide_data_list = slide_data_list[:max_slides]
        
        return self._process_slide_multispeaker_video(slide_data_list, slidev_file)
    
    def parse_slide_content(self, slidev_file):
        """Parse slidev markdown for slide-level content with multi-speaker notes - SIMPLE APPROACH"""
        if not os.path.exists(slidev_file):
            print(f"❌ Slidev file not found: {slidev_file}")
            return []

        with open(slidev_file, 'r', encoding='utf-8') as f:
            content = f.read()

        slide_data_list = []
        slide_counter = 1
        
        # Use regex to split on '---' only when it's a dedicated line
        # This handles tables with '---' correctly and ensures cleaner splits
        parts = re.split(r'(?m)^---$', content)
        
        i = 0
        while i < len(parts):
            part = parts[i].strip()
            
            if not part:
                i += 1
                continue
                
            # Skip global YAML frontmatter (contains theme, background, etc.)
            if ('theme:' in part and 'background:' in part) or ('title: Welcome to Slidev' in part):
                i += 1
                continue
                
            # If this part has YAML indicators but no content, it might be slide YAML
            # Check if next part has slide content
            if i + 1 < len(parts) and ('layout:' in part or 'transition:' in part or 'level:' in part):
                # This is slide YAML, next part should be content
                slide_content = parts[i + 1].strip()
                if slide_content and ('# ' in slide_content or '<!--' in slide_content):
                    # Combine YAML and content
                    full_slide = part + '\n---\n' + slide_content
                    slide_data = self._parse_slide_section(full_slide, slide_counter)
                    if slide_data:
                        slide_data_list.append(slide_data)
                        slide_counter += 1
                    i += 2  # Skip both YAML and content parts
                    continue
                    
            # This part contains slide content directly
            if '# ' in part or '<!--' in part:
                slide_data = self._parse_slide_section(part, slide_counter)
                if slide_data:
                    slide_data_list.append(slide_data)
                    slide_counter += 1
                    
            i += 1

        print(f"✅ Parsed {len(slide_data_list)} slides with content")
        return slide_data_list
    
    def _is_yaml_section(self, section):
        """Check if a section contains only YAML frontmatter"""
        if not section:
            return False
        
        lines = section.split('\n')
        yaml_indicators = [':', 'theme:', 'layout:', 'transition:', 'level:', 'background:', 'class:', 'title:']
        markdown_content_indicators = ['# ', '## ', '### ', '```', '<!--', '<div', '![', '[', '*', '>', '|']
        
        has_yaml = any(indicator in section for indicator in yaml_indicators)
        
        # Count non-comment, non-empty lines that look like markdown content
        markdown_lines = 0
        yaml_lines = 0
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):  # Empty or comment lines
                continue
            
            if any(line.startswith(indicator) for indicator in markdown_content_indicators):
                markdown_lines += 1
            elif ':' in line and not line.startswith('http'):  # Looks like YAML key:value
                yaml_lines += 1
        
        # It's YAML if it has YAML indicators and mostly YAML lines, with minimal markdown
        return has_yaml and yaml_lines > 0 and markdown_lines == 0
    
    def _is_slide_yaml_section(self, section):
        """Check if a section contains slide-specific YAML (not global frontmatter)"""
        if not section:
            return False
        
        # Global YAML contains theme, fonts, drawings, etc.
        # Slide YAML contains layout, level, background, transition, etc.
        global_yaml_indicators = ['theme:', 'fonts:', 'drawings:', 'htmlAttrs:', 'info:', 'author:', 'keywords:']
        slide_yaml_indicators = ['layout:', 'level:', 'background:', 'transition:', 'class:', 'clicks:', 'hide:', 'disabled:']
        
        # Check if this looks like YAML first
        if not self._is_yaml_section(section):
            return False
        
        # If it has global YAML indicators, it's probably global frontmatter
        has_global_indicators = any(indicator in section for indicator in global_yaml_indicators)
        if has_global_indicators:
            return False
        
        # If it has slide-specific indicators, it's slide YAML
        has_slide_indicators = any(indicator in section for indicator in slide_yaml_indicators)
        if has_slide_indicators:
            return True
        
        # If it's YAML but we can't determine type, assume it's slide YAML if it's short
        # (global frontmatter is typically longer)
        return len(section.split('\n')) < 10
    
    def _extract_first_slide_from_section_0(self, section_0):
        """Extract first slide content from Section 0 (which contains global YAML + first slide)"""
        lines = section_0.split('\n')
        
        # Find the end of YAML frontmatter (look for '---' that closes the YAML)
        yaml_end_index = -1
        for i, line in enumerate(lines):
            if line.strip() == '---' and i > 0:  # Skip the opening --- at line 0
                yaml_end_index = i
                break
        
        if yaml_end_index == -1:
            return None  # No YAML closing found
        
        # Everything after the closing --- is the first slide content
        first_slide_lines = lines[yaml_end_index + 1:]
        first_slide_content = '\n'.join(first_slide_lines).strip()
        
        return first_slide_content if first_slide_content else None
    
    def _parse_slide_section(self, section, slide_number):
        """Parse individual slide section for content and speaker notes"""
        lines = section.strip().split('\n')
        
        slide_data = {
            'number': slide_number,
            'title': '',
            'content': [],
            'speaker_notes': '',
            'raw_content': section.strip()
        }
        
        # Extract speaker notes from HTML comments
        html_comment_pattern = r'<!--\s*(.*?)\s*-->'
        comment_matches = re.findall(html_comment_pattern, section, re.DOTALL)
        
        if comment_matches:
            speaker_notes = comment_matches[-1].strip()
            slide_data['speaker_notes'] = speaker_notes
        
        # Extract title
        for line in lines:
            line = line.strip()
            if line.startswith('# ') and not slide_data['title']:
                slide_data['title'] = line[2:].strip()
                break
        
        # Debug output
        print(f"🔍 Debug Slide {slide_number}: title='{slide_data['title']}', notes_length={len(slide_data['speaker_notes'])}")
        if not (slide_data['title'] or slide_data['speaker_notes']):
            print(f"❌ Slide {slide_number} rejected - no title or speaker notes")
            print(f"   First 100 chars: {section.strip()[:100]}")
        
        return slide_data if (slide_data['title'] or slide_data['speaker_notes']) else None
    
    def _process_slide_multispeaker_video(self, slide_data_list, slidev_file):
        """Process slide-level multi-speaker video clips"""
        slide_files = list(Path(self.slides_dir).glob("*.png"))
        slide_files.sort(key=lambda x: int(re.search(r'(\d+)', x.stem).group()) if re.search(r'(\d+)', x.stem) else 0)
        
        print(f"📊 Processing {len(slide_data_list)} slides")
        
        video_clips = []
        total_duration = 0
        
        # Process each slide
        for i, slide_data in enumerate(slide_data_list):
            if i >= len(slide_files):
                break
            
            slide_file = slide_files[i]
            slide_num = slide_data['number']
            
            print(f"\n🎞️ Processing slide {slide_num}: {slide_data.get('title', '')[:50]}...")
            
            # Get narration content
            narration = slide_data.get('speaker_notes', '')
            if not narration:
                print(f"   ⚠️ No speaker notes found for slide {slide_num}")
                continue
            
            print(f"   📝 Multi-speaker content: {narration[:100]}...")
            
            # Generate multi-speaker audio
            audio_file = f"temp_multispeaker_slide_{slide_num}.mp3"
            self.temp_audio_files.append(audio_file)
            
            if self.generate_multispeaker_audio(narration, audio_file):
                try:
                    audio_clip = AudioFileClip(audio_file)
                    duration = audio_clip.duration
                    total_duration += duration
                    
                    abs_slide_path = str(slide_file.resolve())
                    print(f"   🖼️ Loading image: {abs_slide_path}")
                    image_clip = ImageClip(abs_slide_path, duration=duration)
                    if hasattr(image_clip, 'with_audio'):
                        video_clip = image_clip.with_audio(audio_clip)
                    else:
                        video_clip = image_clip.set_audio(audio_clip)
                    video_clips.append(video_clip)
                    
                    print(f"   ✅ Processed ({duration:.1f}s)")
                except Exception as e:
                    print(f"   ❌ Video clip error: {str(e)[:50]}...")
                    continue
        
        return self._assemble_final_multispeaker_video(video_clips, total_duration, slidev_file)
    
    def _process_click_multispeaker_video(self, click_data_list, slidev_file):
        """Process click-synchronized multi-speaker video clips"""
        slide_files = list(Path(self.slides_dir).glob("*.png"))
        slide_files.sort(key=lambda x: (
            int(re.search(r'(\d{3})', x.stem).group()) if re.search(r'(\d{3})', x.stem) else 0,
            int(re.search(r'-(\d{2})', x.stem).group(1)) if re.search(r'-(\d{2})', x.stem) else 0
        ))
        
        print(f"📊 Processing {len(click_data_list)} slides with {len(slide_files)} click states")
        
        video_clips = []
        total_duration = 0
        
        # Create slide file mapping
        slide_file_map = {}
        for img_file in slide_files:
            match = re.search(r'(\d{3})-(\d{2})\.png', img_file.name)
            if match:
                slide_num = int(match.group(1))
                click_num = int(match.group(2))
                if slide_num not in slide_file_map:
                    slide_file_map[slide_num] = {}
                slide_file_map[slide_num][click_num] = img_file
        
        # Process each slide's click segments
        for slide_data in click_data_list:
            slide_num = slide_data['number']
            click_segments = slide_data.get('click_segments', [])
            
            print(f"\n🎞️ Processing slide {slide_num}: {slide_data.get('title', '')[:50]}...")
            
            if slide_num not in slide_file_map:
                continue
            
            slide_images = slide_file_map[slide_num]
            
            for segment in click_segments:
                click_num = segment['click']
                narration = segment['narration']
                
                # Find corresponding image
                image_state = click_num + 1
                if image_state not in slide_images:
                    available_states = sorted(slide_images.keys())
                    if available_states:
                        image_state = min(image_state, max(available_states))
                    else:
                        continue
                
                slide_image = slide_images[image_state]
                
                print(f"   🖱️ Click {click_num} → {slide_image.name}: {narration[:50]}...")
                
                # Generate multi-speaker audio
                audio_file = f"temp_multispeaker_slide_{slide_num}_click_{click_num}.mp3"
                self.temp_audio_files.append(audio_file)
                
                if self.generate_multispeaker_audio(narration, audio_file):
                    try:
                        audio_clip = AudioFileClip(audio_file)
                        duration = audio_clip.duration
                        total_duration += duration
                        
                        abs_slide_path = str(slide_image.resolve())
                        print(f"      🖼️ Loading image: {abs_slide_path}")
                        image_clip = ImageClip(abs_slide_path, duration=duration)
                        if hasattr(image_clip, 'with_audio'):
                            video_clip = image_clip.with_audio(audio_clip)
                        else:
                            video_clip = image_clip.set_audio(audio_clip)
                        video_clips.append(video_clip)
                        
                        print(f"      ✅ Processed ({duration:.1f}s)")
                    except Exception as e:
                        print(f"      ❌ Video clip error: {str(e)[:50]}...")
                        continue
        
        return self._assemble_final_multispeaker_video(video_clips, total_duration, slidev_file)
    
    def _assemble_final_multispeaker_video(self, video_clips, total_duration, slidev_file):
        """Assemble final multi-speaker video from clips"""
        if not video_clips:
            print("❌ No video clips to process")
            self.cleanup_temp_files()
            return False
        
        print(f"\n📹 Assembling final multi-speaker video...")
        print(f"   📊 Total clips: {len(video_clips)}")
        print(f"   ⏱️ Total duration: {total_duration:.1f} seconds ({total_duration/60:.1f} minutes)")
        
        try:
            final_video = concatenate_videoclips(video_clips)
            
            input_basename = os.path.splitext(os.path.basename(slidev_file))[0]
            output_file = f"{input_basename}-MULTISPEAKER.mp4"
            
            print("📤 Exporting multi-speaker video...")
            final_video.write_videofile(
                output_file,
                fps=30,
                codec='libx264',
                audio_codec='aac',
                bitrate="8000k"
            )
            
            # Cleanup
            for clip in video_clips:
                clip.close()
            final_video.close()
            
            if os.path.exists(output_file):
                file_size = os.path.getsize(output_file) / (1024 * 1024)
                
                print(f"\n🎉 SUCCESS! Multi-Speaker video created!")
                print("=" * 50)
                print(f"📹 **Multi-Speaker Conversational Video:**")
                print(f"   File: {output_file}")
                print(f"   Duration: {total_duration:.1f} seconds ({total_duration/60:.1f} minutes)")
                print(f"   Size: {file_size:.1f} MB")
                print(f"   Clips: {len(video_clips)}")
                print(f"   TTS Provider: Google Cloud Multi-Speaker")
                print(f"   Processing Mode: {self.processing_mode.upper()}")
                
                self.cleanup_temp_files()
                return True
            else:
                print("❌ Video file not created")
                self.cleanup_temp_files()
                return False
                
        except Exception as e:
            print(f"❌ Final video creation failed: {e}")
            self.cleanup_temp_files()
            return False
    
    def cleanup_temp_files(self):
        """Clean up temporary files"""
        print("\n🧹 Cleaning up temporary files...")
        
        # Remove temporary audio files
        for audio_file in self.temp_audio_files:
            try:
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                    print(f"   🗑️ Removed: {audio_file}")
            except Exception as e:
                print(f"   ⚠️ Could not remove {audio_file}: {e}")
        
        # Remove temporary slides directory
        try:
            if os.path.exists(self.slides_dir):
                import shutil
                # shutil.rmtree(self.slides_dir)
                # print(f"   🗑️ Removed directory: {self.slides_dir}")
                pass
        except Exception as e:
            print(f"   ⚠️ Could not remove directory {self.slides_dir}: {e}")
        
        print("✅ Cleanup completed!")

def main():
    """Main execution with argument parsing"""
    parser = argparse.ArgumentParser(
        description="Slidev Multi-Speaker Video Processor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Multi-Speaker Features:
  - Google Cloud TTS with multispeaker voices
  - Advanced SSML markup support
  - Natural conversation flow between speakers
  - Professional podcast-style educational content

Requirements:
  1. Install: pip install google-cloud-texttospeech
  2. Setup: gcloud auth application-default login
  3. Enable: gcloud services enable texttospeech.googleapis.com

Examples:
  python slidev_multispeaker_processor.py slides-conversational.md
  python slidev_multispeaker_processor.py slides-conversational.md 3
  python slidev_multispeaker_processor.py slides-conversational.md --with-clicks
  python slidev_multispeaker_processor.py slides-conversational.md 5 --with-clicks
        """
    )
    
    parser.add_argument('slidev_file', help='Path to Slidev markdown file')
    parser.add_argument('max_slides', nargs='?', type=int, help='Maximum number of slides to process')
    parser.add_argument('--with-clicks', action='store_true', help='Enable click-based processing (step-by-step reveals)')
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.slidev_file):
        print(f"❌ Slidev file not found: {args.slidev_file}")
        return
    
    if not args.slidev_file.lower().endswith('.md'):
        print(f"⚠️ Warning: File doesn't have .md extension: {args.slidev_file}")
    
    # Create processor
    processor = SlidevMultiSpeakerProcessor(args.slidev_file, with_clicks=args.with_clicks)
    
    print(f"\n📁 Input file: {args.slidev_file}")
    if args.max_slides:
        print(f"🎬 Processing: {args.max_slides} slides max")
    else:
        print(f"🎬 Processing: All slides")
    print()
    
    try:
        processor.create_multispeaker_video(args.slidev_file, args.max_slides)
    except KeyboardInterrupt:
        print("\n⚠️ Process interrupted by user")
        processor.cleanup_temp_files()
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        processor.cleanup_temp_files()

if __name__ == "__main__":
    main()