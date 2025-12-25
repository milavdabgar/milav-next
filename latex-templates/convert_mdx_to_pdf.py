#!/usr/bin/env python3
"""
MDX to PDF Converter for Study Materials
Converts MDX files to LaTeX, refactors them, and generates PDFs.

Usage:
    python3 convert_mdx_to_pdf.py <mdx_file>
    python3 convert_mdx_to_pdf.py <mdx_file> --no-pdf  # Skip PDF generation
    python3 convert_mdx_to_pdf.py <mdx_file> --keep-aux  # Keep auxiliary files
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path

# Import the refactor function from refactor_latex.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from refactor_latex import refactor_latex


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
    1. Convert MDX to LaTeX using Pandoc
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
    
    # Determine output paths
    tex_path = mdx_path.with_suffix('.tex')
    pdf_path = mdx_path.with_suffix('.pdf')
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
        
        # Step 4: Clean up auxiliary files
        if not keep_aux:
            aux_extensions = ['.aux', '.log', '.out', '.toc', '.lof', '.lot']
            for ext in aux_extensions:
                aux_file = mdx_path.with_suffix(ext)
                if aux_file.exists():
                    aux_file.unlink()
                    print(f"🗑️  Removed: {aux_file.name}")
    
    print(f"\n{'='*60}")
    print(f"✅ SUCCESS: Conversion complete!")
    print(f"{'='*60}")
    print(f"LaTeX: {tex_path}")
    if generate_pdf and pdf_path.exists():
        print(f"PDF:   {pdf_path}")
    print(f"{'='*60}\n")
    
    return True


def main():
    parser = argparse.ArgumentParser(
        description='Convert MDX study materials to PDF via LaTeX',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert MDX to PDF (full pipeline)
  python3 convert_mdx_to_pdf.py 4300003-winter-2023-solution.mdx
  
  # Convert to LaTeX only (skip PDF generation)
  python3 convert_mdx_to_pdf.py 4300003-winter-2023-solution.mdx --no-pdf
  
  # Keep auxiliary files (.aux, .log, etc.)
  python3 convert_mdx_to_pdf.py 4300003-winter-2023-solution.mdx --keep-aux
        """
    )
    
    parser.add_argument(
        'mdx_file',
        help='Path to the MDX file to convert'
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
    
    success = convert_mdx_to_pdf(
        args.mdx_file,
        generate_pdf=not args.no_pdf,
        keep_aux=args.keep_aux
    )
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
