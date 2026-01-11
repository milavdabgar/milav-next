
from pathlib import Path
from typing import List, Optional
import shutil

try:
    from moviepy import ImageClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips
    MOVIEPY_AVAILABLE = True
except ImportError:
    MOVIEPY_AVAILABLE = False


class VideoStitcher:
    def __init__(self, output_file: str):
        self.output_path = output_file
        if not MOVIEPY_AVAILABLE:
            raise ImportError("MoviePy not installed. Please install: pip install moviepy")

    def stitch(self, image_paths: List[Path], audio_map: List[List[Path]], resolution: str = '1080p'):
        """
        Stitch images and audio into a video.
        :param image_paths: List of paths to slide images.
        :param audio_map: List of Lists. audio_map[i] = [audio1, audio2] for image i.
        :param resolution: '720p', '1080p', or '4k'. Controls bitrate.
        """
        print(f"🎬 Stitching Video into {self.output_path}...")
        
        clips = []
        
        for i, img_path in enumerate(image_paths):
            if i >= len(audio_map):
                continue
                
            frame_audios = audio_map[i]
            
            # Create Audio Clip for this frame
            audio_objs = []
            frame_duration = 0.0
            
            if frame_audios:
                for a_path in frame_audios:
                    if not a_path.exists(): continue
                    
                    # Check for Silence Marker
                    is_silence = False
                    try:
                        if a_path.stat().st_size < 100:
                            with open(a_path, 'r') as f:
                                if f.read().strip() == "SILENCE_MARKER":
                                    is_silence = True
                    except: pass
                    
                    if is_silence:
                        # For silence, we just add duration. We don't add an audio clip.
                        # Wait, we need to effectively append "silence".
                        # MoviePy concatenation of [Audio, None] isn't standard.
                        # Easier: Just increment frame_duration. 
                        # BUT: If we have [Speech, Silence, Speech], we need gap.
                        # So we MUST create a SilentAudioClip.
                        # Since we don't want to depend on AudioArrayClip (numpy), 
                        # we can't easily make silence without pydub/numpy.
                        
                        # Alternative: Just add 0.5s to frame_duration. 
                        # The ImageClip will play for longer. 
                        # But speech alignment?
                        # If [AudioA, Silence, AudioB] -> map to [AudioA, AudioB] with duration A+0.5+B?
                        # Yes.
                        frame_duration += 0.5
                    
                    elif a_path.stat().st_size > 500:
                         try:
                             ac = AudioFileClip(str(a_path))
                             audio_objs.append(ac)
                             frame_duration += ac.duration
                         except Exception as e:
                             print(f"⚠️ Bad Audio {a_path}: {e}")
            
            # Combine Audio
            final_audio_clip = None
            if audio_objs:
                final_audio_clip = concatenate_audioclips(audio_objs) if len(audio_objs) > 1 else audio_objs[0]

            # Final Duration logic
            # If we had silence markers, frame_duration is > final_audio_clip.duration
            # We should set VideoClip duration to frame_duration.
            # And set audio to final_audio_clip.
            
            if frame_duration == 0:
                 frame_duration = 2.0 # Default fallback
            
            # Create Video Clip
            video_clip = ImageClip(str(img_path)).with_duration(frame_duration)
            if final_audio_clip:
                video_clip = video_clip.with_audio(final_audio_clip)
                
            clips.append(video_clip)
            
        if not clips:
            print("❌ No clips to stitch.")
            return

        final_video = concatenate_videoclips(clips)
        
        # Bitrate Logic
        is_4k = (resolution == '4k')
        audio_bitrate = '320k'
        video_bitrate = '50000k' if is_4k else '8000k' 
        preset = 'slow'
        
        print(f"⚙️  Encoding: {resolution} ({video_bitrate}), {audio_bitrate} audio, preset={preset}")
        
        final_video.write_videofile(
            self.output_path, 
            fps=24, 
            codec='libx264', 
            audio_codec='aac', 
            bitrate=video_bitrate,
            audio_bitrate=audio_bitrate,
            preset=preset,
            threads=4
        )
