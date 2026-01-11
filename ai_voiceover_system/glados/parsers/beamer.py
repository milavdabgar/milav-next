
import re
from pathlib import Path
from typing import List, Tuple, Optional, Set
import fitz # PyMuPDF

from .base import BaseParser, AudioSegment

class BeamerParser(BaseParser):
    def __init__(self, input_path: Path):
        super().__init__(input_path)
        self.IGNORED_SPEAKERS = {'Section', 'Slide', 'Frame', 'Note', 'Narrator'}

    def parse(self) -> Tuple[List[AudioSegment], int]:
        r"""
        Parses .tex file for \note{...} blocks.
        Supports automatic recursion for \input{filename}.
        """
        segments = []
        visual_step_count = 0
        
        # We start recursion from the main file
        segments = self._parse_recursive(self.input_path)
        
        # Count visual steps (segments where new_visual=True)
        visual_step_count = sum(1 for s in segments if s.new_visual)
        
        return segments, visual_step_count
        
    def _parse_recursive(self, file_path: Path, processed_files: Set[Path] = None) -> List[AudioSegment]:
        if processed_files is None:
            processed_files = set()
            
        # Resolve path 
        if not file_path.suffix: 
             # Handle \input{chapter1} (no extension)
             potential_tex = file_path.with_suffix(".tex")
             if potential_tex.exists():
                 file_path = potential_tex
        
        if not file_path.exists():
            print(f"⚠️ Warning: Included file not found: {file_path}")
            return []
            
        if file_path.resolve() in processed_files:
            print(f"⚠️ Warning: Circular input detected: {file_path}")
            return []
            
        processed_files.add(file_path.resolve())
        print(f"📖 Parsing: {file_path.name}")
        
        segments = []
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex Update: Matches \note{...} allowing nested braces using recursive pattern logic isn't trivial in Python regex.
        # So we use a custom brace balancer logic.
        
        # Also need to detect \input{...} and inject it in order.
        # This implies we scan the file linearly.
        
        # Simplified Linear Scan
        lines = content.split('\n')
        iterator = iter(lines)
        
        for line in iterator:
            line = line.strip()
            
            # Check for \input{...}
            # Simplistic regex, might miss multiple inputs on one line or commented inputs
            input_match = re.search(r'\\input\{([^}]+)\}', line)
            if input_match and not line.startswith('%'):
                included_filename = input_match.group(1)
                included_path = file_path.parent / included_filename
                
                # Recurse
                sub_segments = self._parse_recursive(included_path, processed_files)
                segments.extend(sub_segments)
                continue
            
            # Check for \note{
            if r'\note{' in line and not line.startswith('%'):
                # Extract the full note block (handling multi-line)
                note_content = self._extract_brace_content(line, iterator)
                if note_content:
                    segments.extend(self._parse_note_content(note_content))
                    
        return segments

    def _extract_brace_content(self, first_line: str, iterator) -> str:
        """
        Extracts content inside \note{ ... }. Handles nested braces basic counting.
        """
        content = ""
        open_braces = 0
        
        # We need to find where \note{ starts in first_line
        start_idx = first_line.find(r'\note{')
        if start_idx == -1: return ""
        
        current_text = first_line[start_idx + 6:] # Skip \note{
        open_braces = 1
        
        # Process first line remnant
        for i, char in enumerate(current_text):
            if char == '{': open_braces += 1
            elif char == '}': open_braces -= 1
            
            if open_braces == 0:
                return content + current_text[:i]
        
        content += current_text + "\n"
        
        # Continue with next lines
        for line in iterator:
            for i, char in enumerate(line):
                if char == '{': open_braces += 1
                elif char == '}': open_braces -= 1
                
                if open_braces == 0:
                    return content + line[:i]
            content += line + "\n"
            
        return content

    def _parse_note_content(self, text: str) -> List[AudioSegment]:
        segments = []
        # Split by [click]
        # Regex split keeps delimiters if capturing group used
        parts = re.split(r'(\[click\])', text)
        
        # Logic: 
        # Part 0: Initial text (New Visual = True for the frame, but what if multiple notes?)
        # Actually in BeamerParser logic:
        # Each \note{} command usually corresponds to a slide state.
        # But commonly users put one big \note{} block for a frame with multiple <+-> overlays.
        # So we assume the *Start* of a note block triggers a visual step (or continues the previous if it was just a continuation?)
        # For safety, let's assume Start of Note = New Visual Step.
        
        is_first_part_of_note = True
        
        for part in parts:
            if part == '[click]':
                is_first_part_of_note = False # Next text part is triggered by click
                continue
                
            clean_text = part.strip()
            if not clean_text: continue
            
            # Parse Speaker
            speaker, message = self._extract_speaker(clean_text)
            
            # Determine if this segment triggers a new visual (PDF page)
            # If it's the very first part of the note block -> Yes.
            # If it follows a [click] -> Yes.
            
            # However, if we split a single line into speaker/text, that doesn't trigger visual.
            pass
            
            lines_in_part = clean_text.split('\n')
            for i, subline in enumerate(lines_in_part):
                subline = subline.strip()
                if not subline: continue
                
                spk, msg = self._extract_speaker(subline)
                
                # Logic from original script:
                # new_viz = True if (is_first_part_of_note AND i==0) OR (preceded by click)
                # But wait, [click] applies to the chunk.
                # If we have:
                # Text A (Part 1)
                # [click]
                # Text B (Part 2)
                
                # Text A (Line 1) -> New Visual = True
                # Text A (Line 2) -> New Visual = False
                
                # Text B (Line 1) -> New Visual = True (because of click)
                
                is_start_of_chunk = (i == 0)
                
                # Visual Advance condition:
                # 1. It is the start of a [click] chunk.
                # 2. OR it is the start of the Note block (implicit first click).
                
                new_visual = False
                if is_start_of_chunk:
                     # If it's the first part of the note, yes.
                     # If it's a subsequent part (after click), yes.
                     new_visual = True
                     
                # BUT: Original script logic said:
                # "Only the VERY first segment of the `step` gets new_visual=True"
                # Here `step` == `part`.
                
                # Wait, if `part` has multiple lines, only the first line gets new_visual.
                
                segments.append(AudioSegment(
                    text=msg,
                    speaker=spk,
                    new_visual=new_visual
                ))
            
            is_first_part_of_note = False 
            
        return segments

    def _extract_speaker(self, text: str) -> Tuple[Optional[str], str]:
        match = re.search(r'^([A-Za-z\s\.]+):\s*(.+)', text)
        if match:
            possible_name = match.group(1).strip()
            content = match.group(2).strip()
            
            if possible_name not in self.IGNORED_SPEAKERS:
                return possible_name, content
                
        return None, text

    def generate_images(self, output_dir: Path, resolution: str) -> List[Path]:
        pdf_path = self.input_path.with_suffix(".pdf")
        if not pdf_path.exists():
             raise FileNotFoundError(f"PDF not found: {pdf_path}. Compile latex first.")
             
        print(f"🖼️ Rasterizing PDF (PyMuPDF): {pdf_path.name}")
        doc = fitz.open(pdf_path)
        image_paths = []
        
        # Resolution Logic
        resolutions = {
            '720p': (1280, 720),
            '1080p': (1920, 1080),
            '4k': (3840, 2160)
        }
        target_w, target_h = resolutions.get(resolution, (1920, 1080))
        
        for i, page in enumerate(doc):
             # Matrix scaling (ported from original)
             rect = page.rect
             zoom_x = target_w / rect.width
             zoom_y = target_h / rect.height
             mat = fitz.Matrix(zoom_x, zoom_y)
             
             pix = page.get_pixmap(matrix=mat)
             img_path = output_dir / f"{i:04d}.png"
             pix.save(img_path)
             image_paths.append(img_path)
             
        return image_paths
