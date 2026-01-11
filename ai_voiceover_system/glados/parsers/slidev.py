
import re
import os
import subprocess
from pathlib import Path
from typing import List, Tuple, Dict
from datetime import datetime

from .base import BaseParser, AudioSegment

class SlidevParser(BaseParser):
    def __init__(self, input_path: Path):
        super().__init__(input_path)
        self.work_dir = input_path.parent
        self.project_root = input_path.parent  # Simplified assumption

    def parse(self) -> Tuple[List[AudioSegment], int]:
        """
        Parses slidev markdown.
        """
        with open(self.input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for [click] mode
        processing_mode = 'slide'
        if '[click]' in content:
            processing_mode = 'click'
            
        # Parse Slides (Legacy Logic ported)
        # Note: We are simplifying heavily here to fit the contract.
        # We assume the legacy logic for splitting slides holds.
        
        slides = self._split_content_robust(content)
        
        segments = []
        visual_step_count = 0
        
        # Skip Frontmatter logic (simplified: if start with ---, skip 0 and 1)
        start_index = 0
        if slides and not slides[0].strip():
             start_index = 2 if len(slides) > 1 else 1
             
        for i, slide_content in enumerate(slides):
            if i < start_index: continue
            if not slide_content.strip(): continue
            
            # Extract Notes
            notes_match = re.search(r'<!--\s*(.*?)\s*-->', slide_content, re.DOTALL)
            if not notes_match:
                # If no notes, we still have a visual slide?
                # Yes, but no audio.
                # Do we emit a segment with empty text?
                # The BaseParser contract implies AudioSegments drive the flow.
                # If there's a visual slide but no audio, we need 1 segment with empty text.
                segments.append(AudioSegment(text="", speaker=None, new_visual=True))
                visual_step_count += 1
                continue
                
            raw_notes = notes_match.group(1).strip()
            
            # Helper to parse clicks in notes
            slide_segments = self._parse_slide_notes(raw_notes, processing_mode)
            
            for idx, seg in enumerate(slide_segments):
                # First segment determines new visual?
                # In Slidev:
                # Click 0 -> Initial State (New Visual)
                # Click 1 -> Next State (New Visual)
                # Text continuation -> Same Visual
                
                # In our _parse_slide_notes, we get list of (click_id, text).
                # Each click ID represents a visual state change in Slidev export.
                
                segments.append(AudioSegment(
                    text=seg['text'],
                    speaker=self._extract_speaker(seg['text'])[0], # Extract speaker if present
                    new_visual=True # In slidev, generally every click is a visual change
                ))
            
            visual_step_count += len(slide_segments)
            
        return segments, visual_step_count

    def generate_images(self, output_dir: Path, resolution: str) -> List[Path]:
        """
        Exports slides via npx slidev export.
        """
        print(f"🖼️ Exporting Slidev to PNG (Resolution: {resolution})...")
        
        # Resolution mapping for Slidev?
        # Slidev export usually takes --width / --height or pixel density.
        # Default is 1920x1080.
        # We can pass --output and format.
        
        # Note: Slidev export is tricky with resolution. We might trust default or add args.
        # For now, let's stick to default 1920x1080 logic unless we want to hack CLI args.
        
        cmd = [
            "npx", "slidev", "export",
            str(self.input_path),
            "--output", str(output_dir),
            "--format", "png",
            "--timeout", "120000"
        ]
        
        # Check for --with-clicks
        # If we detected clicks in parse, we should export with clicks.
        # (Optimisation: Cache this detection)
        with open(self.input_path) as f:
            if '[click]' in f.read():
                cmd.append("--with-clicks")

        print(f"   Executing: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=self.work_dir, capture_output=True, text=True)
        
        if result.returncode != 0:
             print(f"❌ Export Failed: {result.stderr}")
             return []
             
        # Collect images
        images = sorted(list(output_dir.glob("*.png")))
        # Logic to return sorted list
        return images

    def _split_content_robust(self, content):
        """Simplistic split for now."""
        return content.split("\n---\n")

    def _parse_slide_notes(self, notes: str, mode: str) -> List[Dict]:
        segments = []
        if mode == 'click':
            parts = re.split(r'\[click(?::(\d+))?\]', notes)
            # Part 0 is pre-click (Click 0)
            if parts[0].strip():
                segments.append({'click': 0, 'text': parts[0].strip()})
            
            i = 1
            while i < len(parts):
                # part[i] is click ID, part[i+1] is text
                text = parts[i+1] if i+1 < len(parts) else ""
                if text.strip():
                     segments.append({'click': i, 'text': text.strip()})
                i += 2
        else:
            segments.append({'click': 0, 'text': notes})
            
        return segments

    def _extract_speaker(self, text: str) -> Tuple[Optional[str], str]:
        match = re.search(r'^([A-Za-z\s\.]+):\s*(.+)', text)
        if match:
            return match.group(1).strip(), match.group(2).strip()
        return None, text
