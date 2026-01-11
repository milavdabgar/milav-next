
import os
import re
from pathlib import Path
from typing import Optional, List, Tuple

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

# Default Voices
GCLOUD_DEFAULT_VOICE_MALE = "en-US-Studio-M"
GCLOUD_DEFAULT_VOICE_FEMALE = "en-US-Studio-O"


class AudioGenerator:
    def __init__(self, output_dir: Path, provider: str = 'auto', custom_voice: Optional[str] = None):
        """
        Unified Audio Generator.
        :param output_dir: Directory to save audio files.
        :param provider: 'auto', 'gtts', or 'gcloud'.
        :param custom_voice: Optional GCloud voice name override.
        """
        self.output_dir = output_dir
        self.provider = provider
        self.custom_voice = custom_voice
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # GCloud Client Lazy Init
        self.gcloud_client = None
        
        # If 'gcloud' is explicitly requested, try init immediately to fail fast
        if self.provider == 'gcloud':
            self._init_gcloud()

    def _init_gcloud(self) -> bool:
        if self.gcloud_client:
            return True
            
        if not GCLOUD_AVAILABLE:
            print("⚠️ Google Cloud TTS not installed/available.")
            return False
            
        try:
            credentials, project_id = google.auth.default()
            self.gcloud_client = texttospeech.TextToSpeechClient(credentials=credentials)
            return True
        except Exception as e:
            print(f"⚠️ GCloud Init Failed: {e}")
            return False

    def generate(self, text: str, speaker_name: Optional[str], index: int, section_index: int = 0) -> Path:
        """
        Generate audio for a text segment.
        :param index: Primary index (e.g. slide number or sequence number).
        :param section_index: Secondary index (e.g. click number) for filename uniqueness.
        """
        filename = f"audio_{index:04d}_{section_index:04d}.mp3"
        filepath = self.output_dir / filename
        
        if filepath.exists():
            return filepath
            
        # Decision Logic: Which Engine?
        use_gcloud = False
        
        # 1. 'gcloud' forced
        if self.provider == 'gcloud':
            use_gcloud = True
            
        # 2. 'auto': Use gcloud if speaker is named OR if gtts is missing
        elif self.provider == 'auto':
            if speaker_name: # Named speaker -> Implies multi-speaker quality needed
                use_gcloud = True
            elif not GTTS_AVAILABLE:
                use_gcloud = True
                
        # 3. Fallback: If gcloud wanted but failed init, fallback to gtts
        if use_gcloud:
            if not self._init_gcloud():
                print(f"⚠️ Fallback to gTTS for segment {index}-{section_index}")
                use_gcloud = False

        printable_text = text[:30].replace('\n', ' ')
        print(f"🎤 Generating ({'gCloud' if use_gcloud else 'gTTS'}): {printable_text}...")

        if use_gcloud:
            self._generate_gcloud(text, speaker_name, filepath)
        else:
            self._generate_gtts(text, filepath)
            
        return filepath

    def _generate_gtts(self, text: str, filepath: Path):
        try:
            # Strip speaker tags if they exist in text (redundant safety)
            clean_text = re.sub(r'^[A-Za-z\s\.]+: ', '', text)
            tts = gTTS(text=clean_text, lang='en', tld='co.uk')
            tts.save(str(filepath))
        except Exception as e:
            print(f"❌ gTTS Error: {e}")
            # Create silent placeholder? Or raise?
            # For now, create 1s silence to avoid crash
            self._create_silent_mp3(filepath)

    def _generate_gcloud(self, text: str, speaker: Optional[str], filepath: Path):
        try:
            # Cleaning: Start of line speaker names are usually stripped by parser, 
            # but we double check.
            clean_text = text
            
            # Voice Selection
            voice_name = self.custom_voice
            if not voice_name:
                # Default Logic
                if speaker and ("Sarah" in speaker or "Female" in speaker):
                     voice_name = GCLOUD_DEFAULT_VOICE_FEMALE
                else:
                     voice_name = GCLOUD_DEFAULT_VOICE_MALE

            synthesis_input = texttospeech.SynthesisInput(text=clean_text)
            
            voice_params = texttospeech.VoiceSelectionParams(
                language_code="en-US",
                name=voice_name
            )
            
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
                speaking_rate=1.0
            )

            response = self.gcloud_client.synthesize_speech(
                input=synthesis_input, voice=voice_params, audio_config=audio_config
            )

            with open(filepath, "wb") as out:
                out.write(response.audio_content)
                
        except Exception as e:
            print(f"❌ GCloud Error: {e}")
            self._create_silent_mp3(filepath)

    def _create_silent_mp3(self, filepath: Path):
        # Fallback for errors: empty file or silence
        # Minimal valid MP3 header? No, just touch file and moviepy handles silence usually
        # Actually MoviePy might choke on empty file.
        # Let's try to just touch it and handle it in video.
        print("⚠️  Generating silence due to error.")
        with open(filepath, 'wb') as f:
            pass 
