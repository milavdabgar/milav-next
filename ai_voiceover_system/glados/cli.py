
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
    parser.add_argument("--max-slides", type=int, help="Limit processing to first N Logical Slides")
    parser.add_argument("--slide-range", help="Process specific slide range (e.g. '1-12' or '5-10')")
    parser.add_argument("--voice", help="Custom Voice Name (GCloud)")

    args = parser.parse_args()
    input_path = Path(args.input).resolve()
    
    if not input_path.exists():
        print(f"❌ File not found: {input_path}")
        sys.exit(1)

    # 1. Select Parser
    is_slidev = (input_path.suffix == '.md')
    if input_path.suffix == '.tex':
        print("🤖 Detected Beamer (LaTeX) project.")
        parser_engine = BeamerParser(input_path)
    elif is_slidev:
        print("🤖 Detected Slidev (Markdown) project.")
        parser_engine = SlidevParser(input_path)
    else:
        print(f"❌ Unsupported file extension: {input_path.suffix}")
        sys.exit(1)

    # 2. Setup Cache
    cache = CacheManager(input_path, keep_residuals=args.keep_residuals)
    images_dir, audio_dir = cache.setup()
    
    try:
        # Determine Range
        start_slide = 1
        end_slide = None
        range_str = None
        
        if args.slide_range:
            parts = args.slide_range.split('-')
            if len(parts) == 2:
                start_slide = int(parts[0])
                end_slide = int(parts[1])
                range_str = args.slide_range
        elif args.max_slides:
             end_slide = args.max_slides
             range_str = f"1-{end_slide}"

        # 3. Parse Content
        print(f"📖 Parsing {input_path.name}...")
        # Note: We parse ALL content to look for correct Logical IDs.
        # Ideally we could optimize parser to stop early, but recursion makes it tricky.
        # Parsing is fast (text). Image generation is slow.
        result = parser_engine.parse()
        if len(result) == 3:
            segments, estimated_steps, _ = result
        else:
            segments, estimated_steps = result
        
        if not segments:
            print("❌ No content found to process.")
            return

        # Filter Segments (If Slidev/Logical IDs are present)
        # Beamer segments default string slide_id=0.
        has_logical_ids = any(s.slide_id > 0 for s in segments)
        
        if has_logical_ids and (end_slide is not None or start_slide > 1):
            print(f"✂️ Filtering Segments: Range {start_slide}-{end_slide if end_slide else 'Max'}")
            filtered = []
            for s in segments:
                if s.slide_id < start_slide: continue
                if end_slide is not None and s.slide_id > end_slide: continue
                filtered.append(s)
            segments = filtered
            if not segments:
                print("❌ No segments in requested range.")
                return

        # 4. Rasterize Visuals
        print(f"🖼️ Generating Visuals (Range: {range_str if range_str else 'All'})...")
        
        # Pass range_str to generate_images if supported (SlidevParser only)
        # BeamerParser.generate_images signature might not support it?
        # Python allows kwargs? No, it's abstract method.
        # I updated BaseParser? No, I only updated SlidevParser implementation.
        # BaseParser definition in base.py still has (output_dir, resolution).
        # Python doesn't enforce signature match strictly unless called.
        # But cleaner way: Check isinstance(parser_engine, SlidevParser).
        
        if is_slidev:
             image_paths = parser_engine.generate_images(images_dir, args.resolution, range_str=range_str)
        else:
             image_paths = parser_engine.generate_images(images_dir, args.resolution)
             # Legacy Beamer Slicing logic
             if args.max_slides:
                 limit = min(len(image_paths), args.max_slides)
                 image_paths = image_paths[:limit]
        
        # 5. Map Audio to Images
        # Pre-allocate map
        audio_map: List[List[Path]] = [[] for _ in range(len(image_paths))]
        current_image_idx = -1
        
        audio_gen = AudioGenerator(audio_dir, provider=args.tts, custom_voice=args.voice)
        
        print(f"🎤 Synthesizing Audio ({len(segments)} segments)...")
        
        for i, seg in enumerate(segments):
            # Advance visual if needed
            if seg.new_visual:
                current_image_idx += 1
                
            if current_image_idx >= len(image_paths):
                # Overflow
                if current_image_idx == len(image_paths):
                     # print("⚠️ Info: Audio logic suggests more steps than images. Attaching to last frame.")
                     pass
                current_image_idx = len(image_paths) - 1
            
            # Generate Audio
            audio_path = audio_gen.generate(seg.text, seg.speaker, i)
            
            if current_image_idx >= 0:
                audio_map[current_image_idx].append(audio_path)

        # 6. Stitch Video
        output_video = args.output
        if not output_video:
            output_video = str(input_path.with_name(f"{input_path.stem}_video.mp4"))
            
        stitcher = VideoStitcher(output_video)
        stitcher.stitch(image_paths, audio_map, resolution=args.resolution)
        
        print("✅ Done!")
        
    finally:
        # 7. Cleanup
        cache.cleanup()


if __name__ == "__main__":
    main()
