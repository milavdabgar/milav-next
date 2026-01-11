
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

        if not segments:
            print("❌ No content found to process.")
            return

        # Filter Segments logic
        # We need to know WHICH segments to keep, and their original indices (for Beamer image slicing)
        all_segments = segments
        valid_indices = []

        # Check if IDs actally exist
        has_logical_ids = any(s.slide_id > 0 for s in all_segments)
        
        if end_slide is not None or start_slide > 1:
            if has_logical_ids:
                 print(f"✂️ Filtering Segments: Logical Range {start_slide}-{end_slide if end_slide else 'Max'}")
                 for i, s in enumerate(all_segments):
                     if s.slide_id < start_slide: continue
                     if end_slide is not None and s.slide_id > end_slide: continue
                     valid_indices.append(i)
            else:
                 # Beamer fallback if parser fails to assign IDs (unlikely now)
                 # Or manual range logic if no IDs
                 pass
                 # If IDs are missing, we should probably fall back to index slicing? 
                 # But BeamerParser assigns IDs now.
                 valid_indices = list(range(len(all_segments)))
        else:
             valid_indices = list(range(len(all_segments)))
             
        if not valid_indices:
             print("❌ No segments in requested range.")
             return

             valid_indices = list(range(len(all_segments)))
             
        if not valid_indices:
             print("❌ No segments in requested range.")
             return

        # 4. Map Segments to Images (Global)
        seg_to_img_idx = {}
        current_global_img_idx = -1
        # Re-scan all segments to build map
        # Note: BeamerParser segments logic: new_visual typically means "Needs a new image".
        # Initial segment usually has new_visual=True.
        for i, s in enumerate(all_segments):
            if s.new_visual:
                current_global_img_idx += 1
            # Handle standard case where first segment might not be marked new_visual? 
            # (Unlikely with BeamerParser logic, but safe to clamp to 0)
            target = max(0, current_global_img_idx) 
            seg_to_img_idx[i] = target

        # 5. Filter Segments & Images
        filtered_segments_data = [] # List of (segment, global_img_idx)
        needed_global_img_indices = set()
        
        for idx in valid_indices:
            global_img = seg_to_img_idx[idx]
            needed_global_img_indices.add(global_img)
            filtered_segments_data.append((all_segments[idx], global_img))
            
        segments = [x[0] for x in filtered_segments_data]
            
        # 6. Generate/Slice Images
        print(f"🖼️ Generating Visuals (Range: {range_str if range_str else 'All'})...")
        
        needed_sorted = sorted(list(needed_global_img_indices))
        
        if is_slidev:
             image_paths = parser_engine.generate_images(images_dir, args.resolution, range_str=range_str)
        else:
             all_image_paths = parser_engine.generate_images(images_dir, args.resolution)
             print(f"--- DEBUG: Sync Check ---")
             print(f"Total Segments: {len(all_segments)}")
             print(f"Total Images: {len(all_image_paths)}")
             
             image_paths = []
             # Map Global Img Index -> Local Img Index (0..N)
             global_to_local_img = {}
             
             for local_i, global_i in enumerate(needed_sorted):
                 if global_i < len(all_image_paths):
                     image_paths.append(all_image_paths[global_i])
                     global_to_local_img[global_i] = local_i
                 else:
                     print(f"⚠️ Warning: Image Index {global_i} out of bounds (Max {len(all_image_paths)})")
        
        # 7. Map Audio to Images
        # Pre-allocate map
        audio_map: List[List[Path]] = [[] for _ in range(len(image_paths))]
        
        audio_gen = AudioGenerator(audio_dir, provider=args.tts, custom_voice=args.voice)
        
        print(f"🎤 Synthesizing Audio ({len(segments)} segments)...")
        
        if is_slidev:
             # Legacy linear loop for Slidev (since we rely on parser range logic)
             current_image_idx = -1
             for i, seg in enumerate(segments):
                 if seg.new_visual:
                     current_image_idx += 1
                 
                 # Safety overflow check
                 target_idx = current_image_idx
                 if target_idx >= len(image_paths):
                     target_idx = len(image_paths) - 1
                 
                 if target_idx >= 0:
                      audio_map[target_idx].append(audio_gen.generate(seg.text, seg.speaker, i))
        else:
             # Beamer Map Loop
             # Iterate our filtered data which has Global Indices
             for i, (seg, global_img_idx) in enumerate(filtered_segments_data):
                  if global_img_idx in global_to_local_img:
                      local_idx = global_to_local_img[global_img_idx]
                      audio_path = audio_gen.generate(seg.text, seg.speaker, i)
                      audio_map[local_idx].append(audio_path)
                  else:
                      # Should typically not happen if image generation worked
                      pass

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
