
import argparse
import sys
from pathlib import Path
from typing import List

from .core.audio import AudioGenerator
from .core.video import VideoStitcher
from .core.cache import CacheManager
from .parsers.beamer import BeamerParser
from .parsers.slidev import SlidevParser

def main():
    parser = argparse.ArgumentParser(description="Glados: Unified AI Voiceover System")
    parser.add_argument("input", help="Input file (.tex or .md)")
    parser.add_argument("--pdf", help="Path to existing PDF (for Beamer)")
    parser.add_argument("--tts", choices=['auto', 'gtts', 'gcloud'], default='auto', help="TTS Provider")
    parser.add_argument("--output", help="Output video filename")
    parser.add_argument("--resolution", choices=['720p', '1080p', '4k'], default='1080p', help="Output resolution")
    parser.add_argument("--keep-residuals", action="store_true", help="Keep temporary files")
    parser.add_argument("--max-slides", type=int, help="Limit processing to N slides (Preview Mode)")
    parser.add_argument("--voice", help="Custom Voice Name (GCloud)")

    args = parser.parse_args()
    input_path = Path(args.input).resolve()
    
    if not input_path.exists():
        print(f"❌ File not found: {input_path}")
        sys.exit(1)

    # 1. Select Parser
    if input_path.suffix == '.tex':
        print("🤖 Detected Beamer (LaTeX) project.")
        parser_engine = BeamerParser(input_path)
    elif input_path.suffix == '.md':
        print("🤖 Detected Slidev (Markdown) project.")
        parser_engine = SlidevParser(input_path)
    else:
        print(f"❌ Unsupported file extension: {input_path.suffix}")
        sys.exit(1)

    # 2. Setup Cache
    cache = CacheManager(input_path, keep_residuals=args.keep_residuals)
    images_dir, audio_dir = cache.setup()
    
    try:
        # 3. Parse Content
        print(f"📖 Parsing {input_path.name}...")
        segments, estimated_steps = parser_engine.parse()
        
        if not segments:
            print("❌ No content found to process.")
            return

        # 4. Rasterize Visuals
        # Note: BaseParse.generate_images should return sorted paths
        print("🖼️ Generating Visuals...")
        image_paths = parser_engine.generate_images(images_dir, args.resolution)
        
        # 5. Map Audio to Images
        # Generic Logic: 
        # Iterate segments. If segment.new_visual=True, advance image index.
        # Else, append to current image.
        
        audio_map: List[List[Path]] = [[] for _ in range(len(image_paths))]
        current_image_idx = -1
        
        audio_gen = AudioGenerator(audio_dir, provider=args.tts, custom_voice=args.voice)
        
        processed_visuals = 0
        
        print(f"🎤 Synthesizing Audio ({len(segments)} segments)...")
        
        for i, seg in enumerate(segments):
            # Advance visual if needed
            if seg.new_visual:
                current_image_idx += 1
                processed_visuals += 1
                
            # --max-slides logic
            if args.max_slides and processed_visuals > args.max_slides:
                print(f"🛑 Reached max slides limit ({args.max_slides}). Stopping.")
                break
                
            if current_image_idx >= len(image_paths):
                # Overflow check
                # For Beamer overlay logic, sometimes logic steps > PDF pages if parser is out of sync?
                # Or if [click] counts mismatch.
                # We log warning and skip sync, OR attach to last image?
                # Attaching to last image is safer than dropping audio.
                # But let's stick to safe bound.
                if current_image_idx == len(image_paths): # Just one over
                     print("⚠️ Warning: More logical steps than visual frames. Attaching remaining audio to last frame.")
                     current_image_idx = len(image_paths) - 1
                else:
                     current_image_idx = len(image_paths) - 1
            
            # Generate Audio
            # We use `i` as primary index, but we might want `current_image_idx` as prefix?
            # Let's use linear index `i` for unique filename.
            audio_path = audio_gen.generate(seg.text, seg.speaker, i)
            
            # Map
            if current_image_idx >= 0:
                audio_map[current_image_idx].append(audio_path)

        # 6. Stitch Video
        output_video = args.output
        if not output_video:
            output_video = str(input_path.with_name(f"{input_path.stem}_video.mp4"))
            
        stitcher = VideoStitcher(output_video)
        
        # If max-slides used, slice image_paths and audio_map
        if args.max_slides:
             limit = min(len(image_paths), args.max_slides)
             image_paths = image_paths[:limit]
             audio_map = audio_map[:limit]
             
        stitcher.stitch(image_paths, audio_map, resolution=args.resolution)
        
        print("✅ Done!")
        
    finally:
        # 7. Cleanup
        cache.cleanup()

if __name__ == "__main__":
    main()
