#!/usr/bin/env python3
"""
MDX to PDF Converter for Study Materials
Converts MDX files to LaTeX, refactors them, and generates PDFs.

Usage:
    # Single file
    python3 convert_mdx_to_pdf.py <mdx_file>
    
    # Directory (processes all *-solution.mdx and *-solution.gu.mdx files)
    python3 convert_mdx_to_pdf.py <directory>
    
    # With options
    python3 convert_mdx_to_pdf.py <path> --no-pdf --keep-aux
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path
import re

# Import the refactor function from refactor_latex_v2.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refactor_latex_v2 import refactor_latex


def is_solution_file(filename):
    """Check if filename matches the solution file pattern."""
    pattern = r'.*-solution(\.gu)?\.mdx$'
    return re.match(pattern, filename) is not None


def find_solution_files(path):
    """
    Find all solution MDX files in the given path.
    
    Args:
        path: Path object (file or directory)
    
    Returns:
        List of Path objects for solution files
    """
    if path.is_file():
        # Single file - check if it matches pattern
        if is_solution_file(path.name):
            return [path]
        else:
            print(f"⚠️  WARNING: File does not match solution pattern: {path.name}")
            print(f"Expected pattern: *-solution.mdx or *-solution.gu.mdx")
            return []
    
    elif path.is_dir():
        # Directory - find all matching files
        solution_files = []
        for mdx_file in path.glob('*.mdx'):
            if is_solution_file(mdx_file.name):
                solution_files.append(mdx_file)
        
        if not solution_files:
            print(f"⚠️  WARNING: No solution files found in: {path}")
            print(f"Looking for files matching: *-solution.mdx or *-solution.gu.mdx")
        
        return sorted(solution_files)
    
    else:
        print(f"❌ ERROR: Path does not exist: {path}")
        return []


def run_command(cmd, cwd=None, description=""):
    """Run a shell command and handle errors."""
    print(f"{'='*60}")
    print(f"Step: {description}")
    print(f"Command: {' '.join(cmd)}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ ERROR: {description} failed!")
        print(f"Exit code: {e.returncode}")
        if e.stdout:
            print(f"STDOUT:\n{e.stdout}")
        if e.stderr:
            print(f"STDERR:\n{e.stderr}")
        return False


def convert_mdx_to_pdf(mdx_file, generate_pdf=True, keep_aux=False):
    """
    Convert MDX file to PDF through LaTeX pipeline.
    
    Steps:
    1. Convert MDX to LaTeX using Pandoc (with -pandoc suffix)
    2. Refactor LaTeX using refactor_latex.py
    3. Compile LaTeX to PDF using XeLaTeX (optional)
    4. Clean up auxiliary files (optional)
    """
    mdx_path = Path(mdx_file).resolve()
    
    if not mdx_path.exists():
        print(f"❌ ERROR: File not found: {mdx_path}")
        return False
    
    if not mdx_path.suffix == '.mdx':
        print(f"❌ ERROR: File must have .mdx extension: {mdx_path}")
        return False
    
    # Determine output paths with -pandoc suffix
    # Example: 4300003-summer-2022-solution.gu.mdx -> 4300003-summer-2022-solution-pandoc.gu.tex
    stem = mdx_path.stem  # e.g., "4300003-summer-2022-solution.gu" or "4300003-summer-2022-solution"
    
    # Handle .gu.mdx files (double extension)
    if stem.endswith('.gu'):
        base_stem = stem[:-3]  # Remove .gu
        tex_name = f"{base_stem}-pandoc.gu.tex"
        pdf_name = f"{base_stem}-pandoc.gu.pdf"
    else:
        tex_name = f"{stem}-pandoc.tex"
        pdf_name = f"{stem}-pandoc.pdf"
    
    tex_path = mdx_path.parent / tex_name
    pdf_path = mdx_path.parent / pdf_name
    work_dir = mdx_path.parent
    
    print(f"\n{'='*60}")
    print(f"MDX to PDF Conversion Pipeline")
    print(f"{'='*60}")
    print(f"Input:  {mdx_path.name}")
    print(f"Output: {tex_path.name}")
    if generate_pdf:
        print(f"PDF:    {pdf_path.name}")
    print(f"Dir:    {work_dir}")
    print(f"{'='*60}\n")
    
    # Step 1: Pandoc conversion
    if not run_command(
        ['pandoc', str(mdx_path), '-o', str(tex_path)],
        cwd=work_dir,
        description="Converting MDX to LaTeX with Pandoc"
    ):
        return False
    
    print(f"✅ Generated: {tex_path.name}\n")
    
    # Step 2: Refactor LaTeX
    print(f"{'='*60}")
    print(f"Step: Refactoring LaTeX")
    print(f"{'='*60}")
    try:
        refactor_latex(str(tex_path))
        print(f"✅ Refactored: {tex_path.name}\n")
    except Exception as e:
        print(f"❌ ERROR: Refactoring failed!")
        print(f"Error: {e}")
        return False
    
    # Step 3: Compile to PDF (optional)
    if generate_pdf:
        # Run XeLaTeX twice for proper references
        for run_num in [1, 2]:
            if not run_command(
                ['xelatex', '-interaction=nonstopmode', tex_path.name],
                cwd=work_dir,
                description=f"Compiling LaTeX to PDF (pass {run_num}/2)"
            ):
                print(f"⚠️  WARNING: XeLaTeX compilation failed on pass {run_num}")
                if run_num == 1:
                    print("Attempting second pass anyway...")
                else:
                    return False
        
        if pdf_path.exists():
            print(f"✅ Generated PDF: {pdf_path.name}\n")
        else:
            print(f"❌ ERROR: PDF was not generated")
            return False
        
        # Step 4: Clean up auxiliary files (with -pandoc suffix)
        if not keep_aux:
            aux_extensions = ['.aux', '.log', '.out', '.toc', '.lof', '.lot']
            # Build base name for aux files (matches tex_path stem)
            tex_stem = tex_path.stem
            if tex_stem.endswith('.gu'):
                tex_stem = tex_stem[:-3]  # Remove .gu for aux file matching
            
            for ext in aux_extensions:
                # Try both with and without .gu
                aux_file = work_dir / f"{tex_stem}{ext}"
                if aux_file.exists():
                    aux_file.unlink()
                    print(f"🗑️  Removed: {aux_file.name}")
                
                # Also try .gu version
                aux_file_gu = work_dir / f"{tex_stem}.gu{ext}"
                if aux_file_gu.exists():
                    aux_file_gu.unlink()
                    print(f"🗑️  Removed: {aux_file_gu.name}")
    
    print(f"\n{'='*60}")
    print(f"✅ SUCCESS: Conversion complete!")
    print(f"{'='*60}")
    print(f"LaTeX: {tex_path}")
    if generate_pdf and pdf_path.exists():
        print(f"PDF:   {pdf_path}")
    print(f"{'='*60}\n")
    
    return True


def process_files(files, generate_pdf=True, keep_aux=False):
    """
    Process multiple MDX files.
    
    Args:
        files: List of Path objects
        generate_pdf: Whether to generate PDFs
        keep_aux: Whether to keep auxiliary files
    
    Returns:
        Tuple of (success_count, failure_count)
    """
    if not files:
        return 0, 0
    
    total = len(files)
    success_count = 0
    failure_count = 0
    
    print(f"\n{'#'*60}")
    print(f"BATCH PROCESSING: {total} file(s)")
    print(f"{'#'*60}\n")
    
    for i, mdx_file in enumerate(files, 1):
        print(f"\n{'#'*60}")
        print(f"Processing file {i}/{total}: {mdx_file.name}")
        print(f"{'#'*60}\n")
        
        if convert_mdx_to_pdf(mdx_file, generate_pdf, keep_aux):
            success_count += 1
        else:
            failure_count += 1
            print(f"\n⚠️  Failed to process: {mdx_file.name}\n")
    
    # Summary
    print(f"\n{'#'*60}")
    print(f"BATCH PROCESSING COMPLETE")
    print(f"{'#'*60}")
    print(f"Total:   {total}")
    print(f"Success: {success_count} ✅")
    print(f"Failed:  {failure_count} ❌")
    print(f"{'#'*60}\n")
    
    return success_count, failure_count


def main():
    parser = argparse.ArgumentParser(
        description='Convert MDX study materials to PDF via LaTeX',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert single file to PDF
  python3 convert_mdx_to_pdf.py 4300003-winter-2023-solution.mdx
  
  # Convert all solution files in a directory
  python3 convert_mdx_to_pdf.py /path/to/subject/directory
  
  # Convert to LaTeX only (skip PDF generation)
  python3 convert_mdx_to_pdf.py /path/to/directory --no-pdf
  
  # Keep auxiliary files (.aux, .log, etc.)
  python3 convert_mdx_to_pdf.py /path/to/directory --keep-aux

Pattern Matching:
  Only files matching these patterns will be processed:
  - *-solution.mdx (English solutions)
  - *-solution.gu.mdx (Gujarati solutions)
  
  Files like "4300003.mdx" or "notes.mdx" will be skipped.
        """
    )
    
    parser.add_argument(
        'path',
        help='Path to MDX file or directory containing solution files'
    )
    
    parser.add_argument(
        '--no-pdf',
        action='store_true',
        help='Skip PDF generation (only convert to LaTeX)'
    )
    
    parser.add_argument(
        '--keep-aux',
        action='store_true',
        help='Keep auxiliary files (.aux, .log, etc.)'
    )
    
    args = parser.parse_args()
    
    # Find files to process
    path = Path(args.path).resolve()
    files = find_solution_files(path)
    
    if not files:
        print("❌ No files to process!")
        sys.exit(1)
    
    # Process files
    success_count, failure_count = process_files(
        files,
        generate_pdf=not args.no_pdf,
        keep_aux=args.keep_aux
    )
    
    # Exit with appropriate code
    sys.exit(0 if failure_count == 0 else 1)


if __name__ == '__main__':
    main()
