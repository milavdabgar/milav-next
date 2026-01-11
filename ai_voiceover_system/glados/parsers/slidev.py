
import re
import os
import subprocess
from pathlib import Path
from typing import List, Tuple, Dict, Optional
from datetime import datetime

from .base import BaseParser, AudioSegment

class SlidevParser(BaseParser):
    def __init__(self, input_path: Path):
        super().__init__(input_path)
        self.work_dir = input_path.parent
        self.project_root = input_path.parent  # Simplified assumption

    def parse(self, start_slide_id: int = 1) -> Tuple[List[AudioSegment], int, int]:
        """
        Parses slidev markdown (recursive).
        Returns:
            - List[AudioSegment]
            - visual_step_count (total visual states)
            - next_slide_id (ID for the next slide after this file)
        """
        with open(self.input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for [click] mode
        processing_mode = 'slide'
        if '[click]' in content:
            processing_mode = 'click'
            
        slides = self._split_content_robust(content)
        segments = []
        visual_step_count = 0
        current_slide_id = start_slide_id  # 1-based logical numbering
        
        # We process chunks sequentially.
        # Metadata chunks do NOT increment current_slide_id.
        # Content chunks increment current_slide_id.
        # Import chunks increment current_slide_id by the number of slides in import.
        
        for i, slide_content in enumerate(slides):
            if not slide_content.strip(): continue

            # Filter out Metadata-only blocks
            src_import = self._extract_src(slide_content)
            
            if not src_import and self._is_metadata_only(slide_content):
                print(f"   (Skipping Metadata Block at chunk {i})")
                continue
            
            if src_import:
                # Recursive Parse
                import_path = (self.input_path.parent / src_import).resolve()
                if import_path.exists():
                    print(f"📖 Recursive Parsing: {import_path.name} (Start ID: {current_slide_id})")
                    sub_parser = SlidevParser(import_path)
                    sub_segments, sub_visuals, next_id = sub_parser.parse(start_slide_id=current_slide_id)
                    segments.extend(sub_segments)
                    visual_step_count += sub_visuals
                    
                    # Determine how many slides were added
                    # next_id is the ID *after* the import.
                    current_slide_id = next_id 
                else:
                    print(f"⚠️ Import Not Found: {import_path}")
                continue
            
            # Normal Content Slide
            # Only increment ID if we actually process it as a slide
            this_slide_id = current_slide_id
            
            notes_matches = re.findall(r'<!--\s*(.*?)\s*-->', slide_content, re.DOTALL)
            if not notes_matches:
                # Visual slide with no notes
                print(f"   (Visual Hold) No notes for slide {i} (ID: {this_slide_id})")
                segments.append(AudioSegment(
                    text="", 
                    speaker=None, 
                    new_visual=True,
                    slide_id=this_slide_id,
                    click_id=0
                ))
                visual_step_count += 1
                current_slide_id += 1
                continue
                
            raw_notes = notes_matches[-1].strip() # Use the last comment
            
            # Helper to parse clicks AND multiple speakers
            slide_segments = self._parse_slide_notes(raw_notes, processing_mode)
            
            for seg in slide_segments:
                segments.append(AudioSegment(
                    text=seg['text'],
                    speaker=seg['speaker'],
                    new_visual=seg['new_visual'],
                    slide_id=this_slide_id,
                    click_id=seg['click_id']
                ))
            
            visual_states = set([s['click_id'] for s in slide_segments])
            visual_step_count += len(visual_states)
            
            current_slide_id += 1
            
        return segments, visual_step_count, current_slide_id

    def generate_images(self, output_dir: Path, resolution: str, range_str: Optional[str] = None) -> List[Path]:
        """
        Exports slides via npx slidev export.
        """
        print(f"🖼️ Exporting Slidev to PNG (Resolution: {resolution})...")
        
        cmd = [
            "npx", "slidev", "export",
            str(self.input_path),
            "--output", str(output_dir),
            "--format", "png",
            "--timeout", "120000"
        ]
        
        if range_str:
             cmd.extend(["--range", range_str])

        with open(self.input_path) as f:
            if '[click]' in f.read():
                cmd.append("--with-clicks")

        print(f"   Executing: {' '.join(cmd)}")
        result = subprocess.run(cmd, cwd=self.work_dir, capture_output=True, text=True)
        if result.returncode != 0:
             print(f"❌ Export Failed: {result.stderr}")
             return []
             
        images = sorted(list(output_dir.glob("*.png")))
        return images

    def _split_content_robust(self, content):
        """Split content by '---' separators, skipping those in code blocks."""
        lines = content.split('\n')
        sections = []
        current_section = []
        in_code_block = False
        
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('```'):
                in_code_block = not in_code_block
            
            is_separator = (stripped == '---' and not in_code_block)
            
            if is_separator:
                if current_section:
                    sections.append('\n'.join(current_section))
                else:
                    sections.append('') 
                current_section = []
            elif i == len(lines) - 1:
                current_section.append(line)
                sections.append('\n'.join(current_section))
            else:
                current_section.append(line)
            
        return sections

    def _is_metadata_only(self, content: str) -> bool:
        """
        Heuristic to check if a block is purely YAML metadata.
        Logic:
        - If it has explicit CONTENT (Plain text, HTML, List), it is a Slide.
        - If it has KEYS and NO CONTENT, it is Metadata.
        - If it has neither (e.g. just Comments or just a Header), assume Slide (Content).
        """
        lines = content.split('\n')
        has_key = False
        has_explicit_content = False
        
        for line in lines:
            # Check indentation BEFORE stripping (YAML multiline values are indented)
            is_indented = line.startswith(' ') or line.startswith('\t')
            stripped = line.strip()
            if not stripped: continue
            if stripped.startswith('<!--'): continue
            
            if is_indented:
                continue
                
            # Ambiguous: Headers/Comments (#)
            if stripped.startswith('#'):
                continue
            
            # Checks for Explicit Content
            # 1. HTML
            src_match = re.search(r'^src:\s', stripped)
            if not src_match and stripped.startswith('<') and not stripped.startswith('<<'): 
                has_explicit_content = True
                break
                
            # 2. Lists (could be YAML list or Markdown list - tricky?)
            # YAML: key:\n  - val.  OR top level list?
            # Slidev Config doesn't usually use top-level lists. 
            # Slidev Content uses lists (- Item).
            if stripped.startswith('- ') and not ':' in stripped: 
                 # Heuristic: Dash without colon might be list item. 
                 # But YAML List can be "- value".
                 # Let's count it as content if we are unsure? 
                 # Actually, usually YAML lists are indented under a key.
                 # Top level list in YAML is valid, but rare in Slidev Config.
                 has_explicit_content = True
                 break

            # 3. Plain Text (No colon, no dash)
            if ':' in stripped:
                has_key = True
            elif not stripped.startswith('-') and not stripped.startswith('`'):
                has_explicit_content = True
                break
                
        # Decision:
        if has_explicit_content:
            return False
        if has_key:
            return True
            
        # Default: If just `#` lines (Title Only) or empty -> Treat as Slide
        return False

    def _extract_src(self, content: str) -> Optional[str]:
        """Extracts src path from metadata block."""
        match = re.search(r'^src:\s*(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
        return None

    def _parse_slide_notes(self, notes: str, mode: str) -> List[Dict]:
        """
        Parses notes into segments, handling both [click] markers AND multi-speaker conversation.
        """
        click_blocks = []
        if mode == 'click':
            parts = re.split(r'\[click(?::(\d+))?\]', notes)
            if parts[0].strip():
                click_blocks.append({'click_id': 0, 'raw_text': parts[0].strip()})
            
            i = 1
            while i < len(parts):
                text = parts[i+1] if i+1 < len(parts) else ""
                click_id = int(parts[i]) if parts[i] else (click_blocks[-1]['click_id'] + 1 if click_blocks else 1)
                
                if text.strip():
                     click_blocks.append({'click_id': click_id, 'raw_text': text.strip()})
                i += 2
        else:
            click_blocks.append({'click_id': 0, 'raw_text': notes})
            
        final_segments = []
        for block in click_blocks:
            # Detect speakers: Split by (Name): 
            # We iterate lines to be safe.
            lines = block['raw_text'].split('\n')
            current_speaker = None
            current_buffer = []
            
            sub_segments = []
            
            # Helper to flush buffer
            def flush(spk, buf):
                if buf:
                    sub_segments.append({'speaker': spk, 'text': ' '.join(buf)})

            for line in lines:
                line = line.strip()
                if not line: continue
                
                # Check for "Name: Message" pattern
                match = re.match(r'^([A-Za-z\s\.]+):\s*(.+)', line)
                if match:
                    flush(current_speaker, current_buffer)
                    current_speaker = match.group(1).strip()
                    current_buffer = [match.group(2).strip()]
                else:
                    current_buffer.append(line)
            
            flush(current_speaker, current_buffer)
                
            if not sub_segments:
                sub_segments.append({'speaker': None, 'text': block['raw_text']})
                
            for j, sub in enumerate(sub_segments):
                # new_visual is True ONLY for the FIRST sub-segment of this click block
                is_start_of_click = (j == 0)
                final_segments.append({
                    'click_id': block['click_id'],
                    'text': sub['text'],
                    'speaker': sub['speaker'],
                    'new_visual': is_start_of_click 
                })
                
        return final_segments

    def _extract_speaker(self, text: str) -> Tuple[Optional[str], str]:
        # Redundant: Speaker extracted in _parse_slide_notes
        return None, text
