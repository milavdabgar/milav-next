#!/usr/bin/env .venv/bin/python
"""
Slidev Comprehensive Video Processor
===================================

Ultimate video processor combining all capabilities:
- All TTS providers: gtts, gcloud (API & client), elevenlabs, coqui
- Multi-speaker support with intelligent detection
- Single-speaker fallback for regular content
- Click-synchronized and slide-level processing
- Advanced SSML markup support
- Automatic provider fallback hierarchy

Usage:
    python slidev_comprehensive_processor.py <slidev_file.md> [max_slides] [--tts=provider] [--with-clicks]
    
TTS Providers:
    - gtts (default): Google TTS UK English (free)
    - gcloud: Google Cloud TTS (premium HD voices, API or client library)
    - elevenlabs: ElevenLabs with voice cloning
    - coqui: Coqui TTS neural models
    - auto: Automatic fallback hierarchy
"""

import os
import sys
import time
import re
import subprocess
import argparse
from pathlib import Path
import requests
import json
import base64
import xml.etree.ElementTree as ET

# Set TTS environment
os.environ['COQUI_TOS_AGREED'] = '1'
os.environ['COQUI_TTS_AGREED'] = '1'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.expanduser('~/.config/gcloud/application_default_credentials.json')

# Import dependencies with availability tracking
try:
    from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False

try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False

try:
    from TTS.api import TTS
    COQUI_TTS_AVAILABLE = True
except ImportError:
    COQUI_TTS_AVAILABLE = False

try:
    from pydub import AudioSegment
    PYDUB_AVAILABLE = True
except ImportError:
    PYDUB_AVAILABLE = False

# Google Cloud TTS availability check (CLI)
try:
    result = subprocess.run(['gcloud', 'auth', 'list', '--filter=status:ACTIVE', '--format=value(account)'], 
                          capture_output=True, text=True, timeout=5)
    GCLOUD_CLI_AVAILABLE = bool(result.returncode == 0 and result.stdout.strip())
except (FileNotFoundError, subprocess.TimeoutExpired):
    GCLOUD_CLI_AVAILABLE = False

# Google Cloud TTS Client Library availability check
try:
    from google.cloud import texttospeech_v1beta1 as texttospeech
    GCLOUD_CLIENT_AVAILABLE = True
except ImportError:
    GCLOUD_CLIENT_AVAILABLE = False

# ElevenLabs configuration
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
ELEVENLABS_VOICE_ID = "Milav English"
ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1"
ELEVENLABS_AVAILABLE = bool(ELEVENLABS_API_KEY)

# Google Cloud TTS configuration
GCLOUD_TTS_API_URL = "https://texttospeech.googleapis.com/v1/text:synthesize"
GCLOUD_DEFAULT_VOICE = "en-US-Chirp3-HD-Achernar"
GCLOUD_HD_VOICES = [
    "en-US-Chirp3-HD-Achernar", "en-US-Chirp3-HD-Algieba", "en-US-Studio-M", "en-US-Studio-O",
    "en-GB-Studio-B", "en-GB-Studio-C", "en-AU-Standard-B"
]

class SlidevComprehensiveProcessor:
    """Comprehensive processor combining all Slidev video generation capabilities"""
    
    def __init__(self, slidev_file, tts_provider='gtts', with_clicks=False):
        self.slides_dir = "temp_comprehensive_slides"
        self.slidev_md_file = slidev_file
        self.temp_audio_files = []
        self.tts_provider = tts_provider
        self.with_clicks = with_clicks
        self.processing_mode = None
        
        # TTS provider configurations
        self.elevenlabs_voice_id = None
        self.coqui_vits_model = None
        self.coqui_tacotron2_model = None
        self.gcloud_access_token = None
        self.gcloud_project_id = None
        self.gcloud_voice_name = GCLOUD_DEFAULT_VOICE
        self.gcloud_client = None
        
        print("🎯 Slidev Comprehensive Video Processor")
        print("=" * 50)
        self._display_capabilities()
        self._initialize_tts_provider()
    
    def _display_capabilities(self):
        """Display available capabilities and TTS providers"""
        print(f"📦 Available Components:")
        print(f"   ✅ MoviePy: {MOVIEPY_AVAILABLE}")
        print(f"   {'✅' if GTTS_AVAILABLE else '❌'} Google TTS (Free): {GTTS_AVAILABLE}")
        print(f"   {'✅' if GCLOUD_CLI_AVAILABLE else '❌'} Google Cloud TTS (CLI): {GCLOUD_CLI_AVAILABLE}")
        print(f"   {'✅' if GCLOUD_CLIENT_AVAILABLE else '❌'} Google Cloud TTS (Client): {GCLOUD_CLIENT_AVAILABLE}")
        print(f"   {'✅' if ELEVENLABS_AVAILABLE else '❌'} ElevenLabs: {ELEVENLABS_AVAILABLE}")
        print(f"   {'✅' if COQUI_TTS_AVAILABLE else '❌'} Coqui TTS: {COQUI_TTS_AVAILABLE}")
        print(f"   {'✅' if PYDUB_AVAILABLE else '❌'} PyDub (Multi-speaker): {PYDUB_AVAILABLE}")
        
        print(f"\n🎤 TTS Provider: {self.tts_provider.upper()}")
        print(f"🎭 Multi-speaker Support: {'✅' if GCLOUD_CLIENT_AVAILABLE and PYDUB_AVAILABLE else '❌'}")
        
        available_providers = []
        if GTTS_AVAILABLE:
            available_providers.append("gtts")
        if GCLOUD_CLI_AVAILABLE or GCLOUD_CLIENT_AVAILABLE:
            available_providers.append("gcloud")
        if ELEVENLABS_AVAILABLE:
            available_providers.append("elevenlabs")
        if COQUI_TTS_AVAILABLE:
            available_providers.append("coqui")
        
        print(f"🔄 Available Providers: {', '.join(available_providers)}")
    
    def _initialize_tts_provider(self):
        """Initialize the selected TTS provider"""
        if self.tts_provider == 'elevenlabs' and ELEVENLABS_AVAILABLE:
            self._initialize_elevenlabs()
        elif self.tts_provider == 'coqui' and COQUI_TTS_AVAILABLE:
            self._initialize_coqui()
        elif self.tts_provider == 'gcloud':
            self._initialize_gcloud()
        elif self.tts_provider == 'gtts' and not GTTS_AVAILABLE:
            print("⚠️ Google TTS (free) not available, switching to auto fallback")
            self.tts_provider = 'auto'
    
    def _initialize_elevenlabs(self):
        """Initialize ElevenLabs connection"""
        try:
            print("🔍 Initializing ElevenLabs...")
            headers = {
                "xi-api-key": ELEVENLABS_API_KEY,
                "Content-Type": "application/json"
            }
            
            response = requests.get(f"{ELEVENLABS_API_URL}/voices", headers=headers)
            if response.status_code == 200:
                voices = response.json()["voices"]
                for voice in voices:
                    if voice["name"] == ELEVENLABS_VOICE_ID:
                        self.elevenlabs_voice_id = voice["voice_id"]
                        print(f"   ✅ Found voice '{ELEVENLABS_VOICE_ID}': {self.elevenlabs_voice_id}")
                        return
                
                print(f"   ❌ Voice '{ELEVENLABS_VOICE_ID}' not found")
                self.tts_provider = 'auto'
            else:
                print(f"   ❌ ElevenLabs API error: {response.status_code}")
                self.tts_provider = 'auto'
        except Exception as e:
            print(f"   ❌ ElevenLabs initialization error: {str(e)}")
            self.tts_provider = 'auto'
    
    def _initialize_coqui(self):
        """Initialize Coqui TTS models"""
        try:
            print("🧠 Initializing Coqui TTS models...")
            print("   ✅ Coqui TTS ready (models load on demand)")
        except Exception as e:
            print(f"   ❌ Coqui TTS initialization error: {str(e)}")
            self.tts_provider = 'auto'
    
    def _initialize_gcloud(self):
        """Initialize Google Cloud TTS (both CLI and client library)"""
        try:
            print("☁️ Initializing Google Cloud TTS...")
            
            # Try client library first (preferred for multi-speaker)
            if GCLOUD_CLIENT_AVAILABLE:
                try:
                    self.gcloud_client = texttospeech.TextToSpeechClient()
                    print("   ✅ Google Cloud TTS Client library ready")
                    print("   🎭 Multi-speaker support enabled")
                    return
                except Exception as e:
                    print(f"   ⚠️ Client library failed: {str(e)}")
            
            # Fallback to CLI API
            if GCLOUD_CLI_AVAILABLE:
                # Get access token
                token_result = subprocess.run(['gcloud', 'auth', 'print-access-token'], 
                                            capture_output=True, text=True, timeout=10)
                if token_result.returncode != 0:
                    raise Exception("Failed to get access token")
                
                self.gcloud_access_token = token_result.stdout.strip()
                
                # Get project ID
                project_result = subprocess.run(['gcloud', 'config', 'list', '--format=value(core.project)'], 
                                              capture_output=True, text=True, timeout=10)
                if project_result.returncode != 0:
                    raise Exception("Failed to get project ID")
                
                self.gcloud_project_id = project_result.stdout.strip()
                
                if not self.gcloud_project_id:
                    raise Exception("No active Google Cloud project found")
                
                print(f"   ✅ Google Cloud TTS API ready")
                print(f"   🏢 Project: {self.gcloud_project_id}")
                print(f"   🎤 Voice: {self.gcloud_voice_name}")
                return
            
            raise Exception("Neither client library nor CLI available")
            
        except Exception as e:
            print(f"   ❌ Google Cloud TTS initialization error: {str(e)}")
            self.tts_provider = 'auto'
    
    def detect_processing_mode(self, slidev_file):
        """Detect whether to use click-based or slide-based processing"""
        if not os.path.exists(slidev_file):
            return 'slide'
        
        with open(slidev_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for [click] markers in presenter notes
        click_markers = re.findall(r'\[click(?::\d+)?\]', content)
        html_comments = re.findall(r'<!--.*?-->', content, re.DOTALL)
        
        if self.with_clicks and click_markers and html_comments:
            print(f"🖱️ Detected {len(click_markers)} click markers - Using CLICK-BASED processing")
            self.processing_mode = 'click'
            return 'click'
        else:
            print("📄 Using SLIDE-BASED processing")
            self.processing_mode = 'slide'
            return 'slide'
    
    def detect_multispeaker_content(self, narration_text):
        """Detect if content contains multi-speaker dialogue"""
        if not narration_text:
            return False
        
        # Check for SSML format
        if narration_text.strip().startswith('<speak>') and '<voice' in narration_text:
            return True
        
        # Check for speaker dialogue format (Speaker: text)
        lines = narration_text.strip().split('\n')
        speaker_lines = 0
        for line in lines:
            line = line.strip()
            if ':' in line and any(name in line.split(':')[0] for name in ['Dr.', 'Sarah', 'James', 'Speaker', 'Host', 'Guest']):
                speaker_lines += 1
        
        return speaker_lines >= 2  # At least 2 speaker lines for multi-speaker
    
    def parse_multispeaker_content(self, narration_text):
        """Parse speaker dialogue and extract turns"""
        turns = []
        
        # Check if it's SSML format
        if narration_text.strip().startswith('<speak>'):
            try:
                root = ET.fromstring(narration_text)
                for voice_elem in root.findall('.//voice'):
                    voice_name = voice_elem.get('name', 'en-US-Studio-M')
                    speaker = 'R' if 'Studio-M' in voice_name or 'Algieba' in voice_name else 'S'
                    
                    voice_content = ET.tostring(voice_elem, encoding='unicode', method='xml')
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
                
                if any(name in speaker_name for name in ['Dr. James', 'James', 'Dr.']):
                    turns.append({
                        'text': text,
                        'speaker': 'R',
                        'voice': 'en-US-Chirp3-HD-Algieba',
                        'is_ssml': False
                    })
                elif 'Sarah' in speaker_name:
                    turns.append({
                        'text': text,
                        'speaker': 'S', 
                        'voice': 'en-US-Chirp3-HD-Achernar',
                        'is_ssml': False
                    })
                else:
                    # Default speaker
                    turns.append({
                        'text': text,
                        'speaker': 'R',
                        'voice': 'en-US-Chirp3-HD-Algieba',
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
    
    def clean_speaker_names_from_text(self, text):
        """Remove speaker names from text for single-speaker fallback"""
        if not text:
            return text
        
        # Handle SSML format - extract just the text content
        if text.strip().startswith('<speak>'):
            try:
                root = ET.fromstring(text)
                # Extract all text content, ignoring voice tags
                clean_text = ''.join(root.itertext()).strip()
                return clean_text
            except ET.ParseError:
                # If SSML parsing fails, try regex approach
                clean_text = re.sub(r'<[^>]+>', '', text)
                return clean_text.strip()
        
        # Handle speaker dialogue format (Speaker: text)
        lines = text.strip().split('\n')
        clean_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check if line has speaker format
            if ':' in line:
                speaker_part, text_part = line.split(':', 1)
                speaker_name = speaker_part.strip()
                
                # If this looks like a speaker name, extract just the text
                if any(name in speaker_name for name in ['Dr.', 'Sarah', 'James', 'Speaker', 'Host', 'Guest']) and len(speaker_name) < 50:
                    clean_lines.append(text_part.strip())
                else:
                    # Not a speaker name, keep the full line
                    clean_lines.append(line)
            else:
                clean_lines.append(line)
        
        return ' '.join(clean_lines)
    
    def generate_audio(self, script, output_file):
        """Generate audio using the selected TTS provider with multi-speaker detection"""
        # Check if content is multi-speaker and we have the capability
        is_multispeaker = self.detect_multispeaker_content(script)
        
        if is_multispeaker and self.gcloud_client and PYDUB_AVAILABLE:
            print(f"   🎭 Multi-speaker content detected - using advanced processing")
            return self.generate_multispeaker_audio(script, output_file)
        else:
            if is_multispeaker:
                print(f"   ⚠️ Multi-speaker content detected but advanced support unavailable - using single-speaker fallback")
                # Clean speaker names from the script for single-speaker fallback
                cleaned_script = self.clean_speaker_names_from_text(script)
                print(f"   🧹 Cleaned speaker names from text")
                return self.generate_single_speaker_audio(cleaned_script, output_file)
            return self.generate_single_speaker_audio(script, output_file)
    
    def generate_single_speaker_audio(self, script, output_file):
        """Generate single-speaker audio using the selected TTS provider with fallbacks"""
        if self.tts_provider == 'gtts':
            return self._generate_audio_gtts(script, output_file)
        elif self.tts_provider == 'elevenlabs':
            return self._generate_audio_elevenlabs(script, output_file)
        elif self.tts_provider == 'coqui':
            return self._generate_audio_coqui(script, output_file)
        elif self.tts_provider == 'gcloud':
            return self._generate_audio_gcloud(script, output_file)
        elif self.tts_provider == 'auto':
            return self._generate_audio_auto_fallback(script, output_file)
        else:
            print(f"   ❌ Unknown TTS provider: {self.tts_provider}")
            return False
    
    def generate_multispeaker_audio(self, narration_text, output_file):
        """Generate multi-speaker audio using Google Cloud TTS client library"""
        if not self.gcloud_client or not PYDUB_AVAILABLE:
            print("   ❌ Multi-speaker TTS not available")
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
                temp_file = f"temp_turn_{i}_{int(time.time())}.wav"
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
                
                # High-quality audio configuration
                audio_config = texttospeech.AudioConfig(
                    audio_encoding=texttospeech.AudioEncoding.LINEAR16,
                    effects_profile_id=['small-bluetooth-speaker-class-device'],
                    speaking_rate=1.0,
                    pitch=0.0
                )
                
                # Generate audio for this turn
                response = self.gcloud_client.synthesize_speech(
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
                        segment = AudioSegment.from_wav(temp_file)
                        segment = segment.normalize()
                        
                        # Add pause between speakers
                        if i > 0:
                            silence = AudioSegment.silent(duration=300)
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
                combined = AudioSegment.empty()
                for segment in audio_segments:
                    combined += segment
                
                combined = combined.normalize()
                combined.export(output_file, format="mp3", bitrate="320k")
                
                # Clean up temp files
                for temp_file in temp_files:
                    if os.path.exists(temp_file):
                        os.remove(temp_file)
                
                if os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
                    speaker_voices = [f"{t['speaker']}:{t['voice']}" for t in turns]
                    print(f"      🎤 Voices: {', '.join(speaker_voices)}")
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
    
    def _generate_audio_gtts(self, script, output_file):
        """Generate audio using Google TTS UK English"""
        if not GTTS_AVAILABLE:
            return False
        
        try:
            print(f"   🇬🇧 Generating audio with Google TTS UK English")
            tts = gTTS(text=script, lang='en', tld='co.uk', slow=False)
            tts.save(output_file)
            
            if os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
                print(f"   ✅ Audio generated successfully")
                return True
            else:
                print(f"   ❌ Audio file too small or not created")
                return False
        except Exception as e:
            print(f"   ❌ Google TTS failed: {str(e)[:50]}...")
            return False
    
    def _generate_audio_elevenlabs(self, script, output_file):
        """Generate audio using ElevenLabs API"""
        if not ELEVENLABS_AVAILABLE or not self.elevenlabs_voice_id:
            return False
        
        try:
            print(f"   🎙️ Generating audio with ElevenLabs (Milav English)")
            
            headers = {
                "xi-api-key": ELEVENLABS_API_KEY,
                "Content-Type": "application/json"
            }
            
            data = {
                "text": script,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.8,
                    "style": 0.0,
                    "use_speaker_boost": True
                }
            }
            
            response = requests.post(
                f"{ELEVENLABS_API_URL}/text-to-speech/{self.elevenlabs_voice_id}",
                headers=headers,
                json=data,
                timeout=30
            )
            
            if response.status_code == 200:
                with open(output_file, 'wb') as f:
                    f.write(response.content)
                
                if os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
                    print(f"   ✅ Audio generated successfully")
                    return True
                else:
                    print(f"   ❌ Audio file too small or not created")
                    return False
            else:
                print(f"   ❌ ElevenLabs API error: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"   ❌ ElevenLabs TTS failed: {str(e)[:50]}...")
            return False
    
    def _generate_audio_coqui(self, script, output_file):
        """Generate audio using Coqui TTS neural models"""
        if not COQUI_TTS_AVAILABLE:
            return False
        
        try:
            print(f"   🧠 Generating audio with Coqui VITS Neural")
            if not self.coqui_vits_model:
                self.coqui_vits_model = TTS("tts_models/en/ljspeech/vits")
            
            self.coqui_vits_model.tts_to_file(text=script, file_path=output_file)
            
            if os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
                print(f"   ✅ Audio generated successfully")
                return True
            else:
                print(f"   ❌ Audio file too small or not created")
                return False
        except Exception as e:
            print(f"   ❌ Coqui TTS failed: {str(e)[:50]}...")
            return False
    
    def _generate_audio_gcloud(self, script, output_file):
        """Generate audio using Google Cloud TTS API"""
        # Try client library first if available
        if self.gcloud_client:
            return self._generate_audio_gcloud_client(script, output_file)
        
        # Fallback to CLI API
        if not GCLOUD_CLI_AVAILABLE or not self.gcloud_access_token:
            return False
        
        try:
            print(f"   ☁️ Generating audio with Google Cloud TTS API ({self.gcloud_voice_name})")
            
            headers = {
                "Content-Type": "application/json",
                "X-Goog-User-Project": self.gcloud_project_id,
                "Authorization": f"Bearer {self.gcloud_access_token}"
            }
            
            payload = {
                "input": {
                    "markup": script
                },
                "voice": {
                    "languageCode": "en-US",
                    "name": self.gcloud_voice_name,
                    "voiceClone": {}
                },
                "audioConfig": {
                    "audioEncoding": "LINEAR16"
                }
            }
            
            response = requests.post(
                GCLOUD_TTS_API_URL,
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                audio_content = result.get('audioContent')
                
                if audio_content:
                    audio_data = base64.b64decode(audio_content)
                    
                    wav_file = output_file.replace('.mp3', '.wav')
                    with open(wav_file, 'wb') as f:
                        f.write(audio_data)
                    
                    # Convert WAV to MP3 if needed
                    if output_file.endswith('.mp3'):
                        try:
                            subprocess.run([
                                'ffmpeg', '-i', wav_file, '-acodec', 'libmp3lame', 
                                '-ab', '128k', '-y', output_file
                            ], capture_output=True, check=True, timeout=30)
                            
                            if os.path.exists(wav_file):
                                os.remove(wav_file)
                        except (subprocess.CalledProcessError, FileNotFoundError):
                            if os.path.exists(wav_file):
                                os.rename(wav_file, output_file)
                    
                    if os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
                        print(f"   ✅ Audio generated successfully")
                        return True
                    else:
                        print(f"   ❌ Audio file too small or not created")
                        return False
                else:
                    print(f"   ❌ No audio content in response")
                    return False
            else:
                print(f"   ❌ Google Cloud TTS API error: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"   ❌ Google Cloud TTS failed: {str(e)[:50]}...")
            return False
    
    def _generate_audio_gcloud_client(self, script, output_file):
        """Generate audio using Google Cloud TTS client library"""
        try:
            print(f"   ☁️ Generating audio with Google Cloud TTS Client ({self.gcloud_voice_name})")
            
            synthesis_input = texttospeech.SynthesisInput(text=script)
            
            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US",
                name=self.gcloud_voice_name
            )
            
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.LINEAR16,
                effects_profile_id=['small-bluetooth-speaker-class-device'],
                speaking_rate=1.0,
                pitch=0.0
            )
            
            response = self.gcloud_client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config
            )
            
            # Save as WAV first
            wav_file = output_file.replace('.mp3', '.wav')
            with open(wav_file, 'wb') as out:
                out.write(response.audio_content)
            
            # Convert to MP3 if needed
            if output_file.endswith('.mp3'):
                try:
                    subprocess.run([
                        'ffmpeg', '-i', wav_file, '-acodec', 'libmp3lame', 
                        '-ab', '320k', '-y', output_file
                    ], capture_output=True, check=True, timeout=30)
                    
                    if os.path.exists(wav_file):
                        os.remove(wav_file)
                except (subprocess.CalledProcessError, FileNotFoundError):
                    if os.path.exists(wav_file):
                        os.rename(wav_file, output_file)
            
            if os.path.exists(output_file) and os.path.getsize(output_file) > 1000:
                print(f"   ✅ Audio generated successfully")
                return True
            else:
                print(f"   ❌ Audio file too small or not created")
                return False
                
        except Exception as e:
            print(f"   ❌ Google Cloud TTS Client failed: {str(e)[:50]}...")
            return False
    
    def _generate_audio_auto_fallback(self, script, output_file):
        """Generate audio using automatic fallback hierarchy"""
        # Try Google Cloud TTS first (highest quality)
        if GCLOUD_CLIENT_AVAILABLE or (GCLOUD_CLI_AVAILABLE and self.gcloud_access_token):
            if self._generate_audio_gcloud(script, output_file):
                return True
        
        # Try ElevenLabs if available (voice cloning)
        if ELEVENLABS_AVAILABLE and self.elevenlabs_voice_id:
            if self._generate_audio_elevenlabs(script, output_file):
                return True
        
        # Try free Google TTS UK (reliable fallback)
        if GTTS_AVAILABLE:
            if self._generate_audio_gtts(script, output_file):
                return True
        
        # Try Coqui TTS as last resort
        if COQUI_TTS_AVAILABLE:
            if self._generate_audio_coqui(script, output_file):
                return True
        
        print(f"   ❌ All TTS providers failed!")
        return False
    
    def parse_click_notes(self, slidev_file):
        """Parse slidev markdown for [click] markers in presenter notes"""
        if not os.path.exists(slidev_file):
            print(f"❌ Slidev file not found: {slidev_file}")
            return []
        
        with open(slidev_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        sections = content.split('---')
        slide_data_list = []
        
        slide_counter = 1
        for i, section in enumerate(sections):
            if i == 0:  # Skip YAML frontmatter
                continue
            
            # Skip config sections
            if (section.strip().startswith('theme:') or 
                section.strip().startswith('layout:') or
                ('background:' in section and 'title:' in section and '# ' not in section)):
                continue
            
            slide_data = self._parse_slide_clicks(section, slide_counter)
            if slide_data:
                slide_data_list.append(slide_data)
                slide_counter += 1
        
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
    
    def parse_slide_content(self, slidev_file):
        """Parse slidev markdown for slide-level content"""
        if not os.path.exists(slidev_file):
            print(f"❌ Slidev file not found: {slidev_file}")
            return []
        
        with open(slidev_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        sections = content.split('---')
        slide_data_list = []
        
        slide_counter = 1
        for i, section in enumerate(sections):
            if i == 0:  # Skip YAML frontmatter
                continue
            
            # Skip config sections
            if (section.strip().startswith('theme:') or 
                section.strip().startswith('layout:') or
                ('background:' in section and 'title:' in section and '# ' not in section)):
                continue
            
            slide_data = self._parse_slide_section(section, slide_counter)
            if slide_data:
                slide_data_list.append(slide_data)
                slide_counter += 1
        
        print(f"✅ Parsed {len(slide_data_list)} slides with content")
        return slide_data_list
    
    def _parse_slide_section(self, section, slide_number):
        """Parse individual slide section for content and speaker notes"""
        lines = section.strip().split('\n')
        
        slide_data = {
            'number': slide_number,
            'title': '',
            'content': [],
            'bullet_points': [],
            'speaker_notes': '',
            'raw_content': section.strip()
        }
        
        # Extract speaker notes from HTML comments
        html_comment_pattern = r'<!--\s*(.*?)\s*-->'
        comment_matches = re.findall(html_comment_pattern, section, re.DOTALL)
        
        if comment_matches:
            speaker_notes = comment_matches[-1].strip()
            speaker_notes = re.sub(r'\s+', ' ', speaker_notes)
            slide_data['speaker_notes'] = speaker_notes
        
        # Parse content
        for line in lines:
            line = line.strip()
            
            # Skip various non-content lines
            if (not line or line.startswith('layout:') or line.startswith('class:') or 
                line.startswith('<') or line.startswith('```') or 
                line.startswith('<!--') or line.endswith('-->') or 
                line.startswith('theme:') or line.startswith('background:')):
                continue
            
            # Extract title
            if line.startswith('# ') and not slide_data['title']:
                slide_data['title'] = line[2:].strip()
                continue
            
            # Extract subtitles
            if line.startswith('## '):
                subtitle = line[3:].strip()
                subtitle = re.sub(r'[🔄🎯🔒💡⚡🛡️📊🔍⚠️✅❌🎪🔧📱💻🌐]', '', subtitle)
                subtitle = re.sub(r'\*\*([^*]+)\*\*', r'\1', subtitle)
                slide_data['content'].append(subtitle)
                continue
            
            # Extract bullet points
            if line.startswith('- '):
                bullet = line[2:].strip()
                bullet = re.sub(r'\*\*([^*]+)\*\*', r'\1', bullet)
                bullet = re.sub(r'\*([^*]+)\*', r'\1', bullet)
                bullet = re.sub(r'`([^`]+)`', r'\1', bullet)
                bullet = re.sub(r'[🔄🎯🔒💡⚡🛡️📊🔍⚠️✅❌🎪🔧📱💻🌐]', '', bullet)
                
                if 5 < len(bullet) < 200:
                    slide_data['bullet_points'].append(bullet)
                continue
            
            # Extract regular content
            if len(line) > 10 and not line.startswith('#') and not line.startswith('<'):
                text = re.sub(r'\*\*([^*]+)\*\*', r'\1', line)
                text = re.sub(r'\*([^*]+)\*', r'\1', text)
                text = re.sub(r'`([^`]+)`', r'\1', text)
                
                if len(text) > 10:
                    slide_data['content'].append(text)
        
        return slide_data if (slide_data['title'] or slide_data['content'] or 
                            slide_data['bullet_points'] or slide_data['speaker_notes']) else None
    
    def generate_narration_from_content(self, slide_data):
        """Generate narration from slide content, prioritizing speaker notes"""
        speaker_notes = slide_data.get('speaker_notes', '')
        
        # Use speaker notes if available
        if speaker_notes and len(speaker_notes) > 20:
            return speaker_notes
        
        # Fallback to content parsing
        script_parts = []
        slide_num = slide_data['number'] 
        title = slide_data.get('title', '')
        content = slide_data.get('content', [])
        bullets = slide_data.get('bullet_points', [])
        
        # Add title
        if title:
            if slide_num == 1:
                script_parts.append(f"Welcome to {title}.")
            else:
                script_parts.append(f"Let's now examine {title}.")
        
        # Add content
        for item in content:
            if len(item) > 10:
                script_parts.append(item)
        
        # Add bullet points
        if bullets:
            script_parts.append("The key points are:" if len(bullets) <= 3 else "The main concepts include:")
            
            for i, bullet in enumerate(bullets[:8]):
                if len(bullet) > 5:
                    if i == 0:
                        script_parts.append(f"First, {bullet}.")
                    elif i == 1:
                        script_parts.append(f"Second, {bullet}.")
                    elif i == 2:
                        script_parts.append(f"Third, {bullet}.")
                    elif i < len(bullets) - 1:
                        script_parts.append(f"Additionally, {bullet}.")
                    else:
                        script_parts.append(f"Finally, {bullet}.")
        
        script = ' '.join(script_parts)
        script = re.sub(r'\s+', ' ', script)
        script = script.replace('..', '.').replace(' .', '.').strip()
        
        # Ensure minimum length
        if len(script) < 50:
            script = f"This slide presents important information about our topic. {script}"
        
        return script
    
    def export_slides(self, slidev_file, with_clicks=False):
        """Export slides using slidev export command"""
        export_type = "click states" if with_clicks else "slides"
        print(f"📤 Exporting {export_type}...")
        
        # Get absolute path of the slidev file
        slidev_file_abs = os.path.abspath(slidev_file)
        if not os.path.exists(slidev_file_abs):
            print(f"❌ Slidev file not found: {slidev_file_abs}")
            return False
        
        os.makedirs(self.slides_dir, exist_ok=True)
        
        try:
            slidev_dir = os.path.dirname(slidev_file_abs)
            slidev_filename = os.path.basename(slidev_file_abs)
            output_dir = os.path.abspath(self.slides_dir)
            
            # Try different slidev command paths
            slidev_commands = [
                "slidev",  # Global installation
                "npx slidev",  # NPX 
                "/Users/milav/.nvm/versions/node/v24.5.0/bin/slidev"  # Direct path
            ]
            
            success = False
            for cmd in slidev_commands:
                try:
                    if cmd.startswith("npx"):
                        export_cmd = ["npx", "slidev", "export"]
                    else:
                        export_cmd = [cmd, "export"]
                    
                    export_cmd.extend([
                        slidev_filename,
                        "--output", output_dir,
                        "--format", "png",
                        "--timeout", "60000"
                    ])
                    
                    if with_clicks:
                        export_cmd.append("--with-clicks")
                    
                    print(f"   🚀 Trying: {' '.join(export_cmd)}")
                    print(f"   📁 Working directory: {slidev_dir}")
                    
                    result = subprocess.run(
                        export_cmd,
                        cwd=slidev_dir,
                        capture_output=True,
                        text=True,
                        timeout=180,  # Increased timeout
                        env={**os.environ, "NODE_ENV": "production"}
                    )
                    
                    if result.returncode == 0:
                        print(f"   ✅ {export_type.title()} exported successfully!")
                        success = True
                        break
                    else:
                        print(f"   ⚠️ {cmd} failed with code {result.returncode}")
                        if result.stderr:
                            print(f"   Error: {result.stderr[:200]}...")
                        continue
                        
                except FileNotFoundError:
                    print(f"   ⚠️ {cmd} not found, trying next...")
                    continue
                except subprocess.TimeoutExpired:
                    print(f"   ⚠️ {cmd} timed out, trying next...")
                    continue
            
            if not success:
                print(f"   ⚠️ All slidev commands failed - checking for fallback images")
                # Don't return False yet, check for slide images below
            
            # Check if files were actually exported
            slide_files = list(Path(self.slides_dir).glob("*.png"))
            if slide_files:
                print(f"   📊 Exported {len(slide_files)} {export_type}")
                return True
            else:
                print(f"   ⚠️ No PNG files found after export")
                # Fallback: check if we have existing slide images to use
                fallback_dirs = [
                    "ai_voiceover_system/slide_images",
                    "slide_images", 
                    "enhanced_podcast_output",
                    "python_slide_images"
                ]
                
                for fallback_dir in fallback_dirs:
                    if os.path.exists(fallback_dir):
                        fallback_files = list(Path(fallback_dir).glob("*.png"))
                        if fallback_files:
                            print(f"   🔄 Using fallback slide images from {fallback_dir}")
                            print(f"   📊 Found {len(fallback_files)} fallback images")
                            # Update slides directory to point to fallback
                            self.slides_dir = fallback_dir
                            return True
                
                print(f"   ❌ No slide images available for video generation")
                return False
                
        except Exception as e:
            print(f"   ❌ Export error: {str(e)}")
            return False
    
    def create_comprehensive_video(self, slidev_file, max_slides=None):
        """Create video using comprehensive processing (auto-detects everything)"""
        print("🎬 Comprehensive Video Creation")
        print("=" * 50)
        
        # Step 1: Detect processing mode
        mode = self.detect_processing_mode(slidev_file)
        
        if mode == 'click':
            return self._create_click_synchronized_video(slidev_file, max_slides)
        else:
            return self._create_slide_level_video(slidev_file, max_slides)
    
    def _create_click_synchronized_video(self, slidev_file, max_slides=None):
        """Create click-synchronized video"""
        print("🖱️ Creating click-synchronized video...")
        
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
        
        return self._process_click_video(click_data_list, slidev_file)
    
    def _create_slide_level_video(self, slidev_file, max_slides=None):
        """Create slide-level video"""
        print("📄 Creating slide-level video...")
        
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
        
        return self._process_slide_video(slide_data_list, slidev_file)
    
    def _process_click_video(self, click_data_list, slidev_file):
        """Process click-synchronized video clips"""
        slide_files = list(Path(self.slides_dir).glob("*.png"))
        slide_files.sort(key=lambda x: (
            int(re.search(r'(\d{3})', x.stem).group()),
            int(re.search(r'-(\d{2})', x.stem).group(1))
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
                
                # Generate audio
                audio_file = f"temp_comprehensive_slide_{slide_num}_click_{click_num}.mp3"
                self.temp_audio_files.append(audio_file)
                
                if self.generate_audio(narration, audio_file):
                    try:
                        audio_clip = AudioFileClip(audio_file)
                        duration = audio_clip.duration
                        total_duration += duration
                        
                        image_clip = ImageClip(str(slide_image), duration=duration)
                        video_clip = image_clip.set_audio(audio_clip)
                        video_clips.append(video_clip)
                        
                        print(f"      ✅ Processed ({duration:.1f}s)")
                    except Exception as e:
                        print(f"      ❌ Video clip error: {str(e)[:50]}...")
                        continue
        
        return self._assemble_final_video(video_clips, total_duration, slidev_file, "COMPREHENSIVE_CLICK")
    
    def _process_slide_video(self, slide_data_list, slidev_file):
        """Process slide-level video clips"""
        slide_files = list(Path(self.slides_dir).glob("*.png"))
        slide_files.sort(key=lambda x: int(re.search(r'(\d+)', x.stem).group()))
        
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
            
            # Generate narration
            script = self.generate_narration_from_content(slide_data)
            print(f"   📝 Script ({len(script)} chars): {script[:100]}...")
            
            # Generate audio
            audio_file = f"temp_comprehensive_slide_{slide_num}.mp3"
            self.temp_audio_files.append(audio_file)
            
            if self.generate_audio(script, audio_file):
                try:
                    audio_clip = AudioFileClip(audio_file)
                    duration = audio_clip.duration
                    total_duration += duration
                    
                    image_clip = ImageClip(str(slide_file), duration=duration)
                    video_clip = image_clip.set_audio(audio_clip)
                    video_clips.append(video_clip)
                    
                    print(f"   ✅ Processed ({duration:.1f}s)")
                except Exception as e:
                    print(f"   ❌ Video clip error: {str(e)[:50]}...")
                    continue
        
        return self._assemble_final_video(video_clips, total_duration, slidev_file, "COMPREHENSIVE_SLIDE")
    
    def _assemble_final_video(self, video_clips, total_duration, slidev_file, prefix):
        """Assemble final video from clips"""
        if not video_clips:
            print("❌ No video clips to process")
            self.cleanup_temp_files()
            return False
        
        print(f"\n📹 Assembling final video...")
        print(f"   📊 Total clips: {len(video_clips)}")
        print(f"   ⏱️ Total duration: {total_duration:.1f} seconds ({total_duration/60:.1f} minutes)")
        
        try:
            final_video = concatenate_videoclips(video_clips)
            
            input_basename = os.path.splitext(os.path.basename(slidev_file))[0]
            tts_suffix = "ElevenLabs" if self.tts_provider == "elevenlabs" else self.tts_provider.upper()
            output_file = f"{input_basename}-{tts_suffix}.mp4"
            
            print("📤 Exporting comprehensive video...")
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
                
                print(f"\n🎉 SUCCESS! Comprehensive video created!")
                print("=" * 50)
                print(f"📹 **{prefix.replace('_', ' ').title()} Video ({tts_suffix}):**")
                print(f"   File: {output_file}")
                print(f"   Duration: {total_duration:.1f} seconds ({total_duration/60:.1f} minutes)")
                print(f"   Size: {file_size:.1f} MB")
                print(f"   Clips: {len(video_clips)}")
                print(f"   TTS Provider: {self.tts_provider.upper()}")
                print(f"   Processing Mode: {self.processing_mode.upper()}")
                print(f"   Multi-speaker Support: {'✅' if self.gcloud_client and PYDUB_AVAILABLE else '❌'}")
                
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
        
        # Preserve audio files if using ElevenLabs (for user to hear)
        if self.tts_provider == 'elevenlabs':
            print("   💾 Keeping ElevenLabs audio files for you to listen to:")
            for audio_file in self.temp_audio_files:
                if os.path.exists(audio_file):
                    print(f"   🎵 Preserved: {audio_file}")
        else:
            # Remove temporary audio files for other providers
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
                shutil.rmtree(self.slides_dir)
                print(f"   🗑️ Removed directory: {self.slides_dir}")
        except Exception as e:
            print(f"   ⚠️ Could not remove directory {self.slides_dir}: {e}")
        
        print("✅ Cleanup completed!")

def main():
    """Main execution with argument parsing"""
    parser = argparse.ArgumentParser(
        description="Slidev Comprehensive Video Processor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Comprehensive Features:
  - All TTS providers: gtts, gcloud (API & client), elevenlabs, coqui
  - Multi-speaker support with intelligent detection
  - Single-speaker fallback for regular content
  - Click-synchronized and slide-level processing
  - Advanced SSML markup support
  - Automatic provider fallback hierarchy

TTS Providers:
  gtts        Google TTS UK English (free, default)
  gcloud      Google Cloud TTS (premium HD voices, API or client library)
  elevenlabs  ElevenLabs with voice cloning (requires ELEVENLABS_API_KEY)
  coqui       Coqui TTS neural models
  auto        Automatic fallback hierarchy

Processing Modes:
  The processor automatically detects whether to use click-based or slide-based
  processing by looking for [click] markers in presenter notes.
  
  Multi-speaker content is automatically detected and processed using advanced
  Google Cloud TTS voices when available, with fallback to single-speaker mode.

Requirements:
  1. Multi-speaker: pip install google-cloud-texttospeech pydub
  2. Setup: gcloud auth application-default login
  3. Enable: gcloud services enable texttospeech.googleapis.com

Examples:
  python slidev_comprehensive_processor.py slides.md
  python slidev_comprehensive_processor.py slides.md 5 --tts=gcloud
  python slidev_comprehensive_processor.py slides.md --tts=elevenlabs --with-clicks
  python slidev_comprehensive_processor.py slides.md --tts=auto
        """
    )
    
    parser.add_argument('slidev_file', help='Path to Slidev markdown file')
    parser.add_argument('max_slides', nargs='?', type=int, help='Maximum number of slides to process')
    parser.add_argument('--tts', choices=['gtts', 'gcloud', 'elevenlabs', 'coqui', 'auto'], 
                       default='gtts', help='TTS provider to use (default: gtts)')
    parser.add_argument('--with-clicks', action='store_true', help='Enable click-based processing (step-by-step reveals)')
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.slidev_file):
        print(f"❌ Slidev file not found: {args.slidev_file}")
        return
    
    if not args.slidev_file.lower().endswith('.md'):
        print(f"⚠️ Warning: File doesn't have .md extension: {args.slidev_file}")
    
    # Create processor
    processor = SlidevComprehensiveProcessor(args.slidev_file, args.tts, args.with_clicks)
    
    print(f"\n📁 Input file: {args.slidev_file}")
    if args.max_slides:
        print(f"🎬 Processing: {args.max_slides} slides max")
    else:
        print(f"🎬 Processing: All slides")
    print()
    
    try:
        processor.create_comprehensive_video(args.slidev_file, args.max_slides)
    except KeyboardInterrupt:
        print("\n⚠️ Process interrupted by user")
        processor.cleanup_temp_files()
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        processor.cleanup_temp_files()

if __name__ == "__main__":
    main()