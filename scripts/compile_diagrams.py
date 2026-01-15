
import os
import glob
import subprocess
import shutil

# Constants
SEARCH_ROOT = "/Users/milav/Code/milav-next/content/resources/study-materials"
PROJECT_ROOT = "/Users/milav/Code/milav-next"
LATEX_TEMPLATES_DIR = os.path.join(PROJECT_ROOT, "latex-templates/gtu-solutions-short")
PREAMBLE_PATH = os.path.join(LATEX_TEMPLATES_DIR, "preamble.tex")
GUJARATI_BOXES_PATH = os.path.join(LATEX_TEMPLATES_DIR, "gujarati-boxes.tex")
ENGLISH_BOXES_PATH = os.path.join(LATEX_TEMPLATES_DIR, "english-boxes.tex")

def compile_diagram(tex_file):
    print(f"Compiling: {tex_file}")
    
    # Determine type
    is_gujarati = tex_file.endswith(".gu.tex")
    
    # Create build directory for this file to avoid clutter
    # We'll use a temp dir in the same folder or in /tmp?
    # Better in the same folder structure but temp 
    # file_dir/build/filename/
    
    file_dir = os.path.dirname(tex_file)
    filename = os.path.basename(tex_file)
    basename = os.path.splitext(filename)[0] # remove .tex
    
    build_dir = os.path.join(file_dir, "build", basename)
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    
    pdf_output_dir = os.path.join(os.path.dirname(file_dir), "pdf")
    if not os.path.exists(pdf_output_dir):
        os.makedirs(pdf_output_dir)
        
    wrapper_filename = "wrapper.tex"
    wrapper_path = os.path.join(build_dir, wrapper_filename)
    
    # Construct absolute path for inputting snippet
    snippet_abs_path = os.path.abspath(tex_file)
        
    # Create a local clean preamble with ONLY required packages/styles
    # This avoids all layout/header/footer issues from the main preamble
    clean_preamble_path = os.path.join(build_dir, "clean_preamble.tex")
    
    minimal_preamble = r"""
\usepackage{amsmath,amssymb,amsthm}
\usepackage{xcolor}
\usepackage{tcolorbox}
\tcbuselibrary{breakable,skins}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{circuitikz}
\usepackage[version=4]{mhchem}
\usepackage{graphicx}
\usepackage{caption}
\pgfplotsset{compat=1.18}
\usetikzlibrary{shapes,arrows,positioning,calc,patterns,decorations.pathmorphing,decorations.markings,arrows.meta,circuits.logic.US,shapes.geometric,fit}
\usepackage{pgf-pie}

% Register circuitikz environment for standalone cropping
\standaloneenv{circuitikz}

% Colors
\definecolor{headcolor}{RGB}{0,102,204}
\definecolor{keycolor}{RGB}{220,20,60}
\definecolor{solutioncolor}{RGB}{34,139,34}
\definecolor{mnemoniccolor}{RGB}{148,0,211}
\definecolor{codecolor}{RGB}{0,0,100}

% TikZ Styles
\tikzset{
  gtu block/.style={rectangle, draw, fill=blue!10, align=center, rounded corners, minimum height=2em, font=\small},
  gtu class/.style={rectangle, draw, fill=yellow!10, align=center, minimum width=2cm},
  gtu interface/.style={rectangle, draw, fill=green!10, align=center, minimum width=2cm, dashed},
  gtu state/.style={draw, circle, fill=blue!10, align=center, minimum width=2.5em},
  gtu container/.style={draw, rectangle, fill=blue!5, rounded corners, minimum width=4.5cm},
  gtu arrow/.style={draw, -latex},
  gtu dashed arrow/.style={draw, -latex, dashed},
  gtu decision/.style={diamond, draw, fill=green!10, align=center, aspect=2, font=\small},
  gtu flow/.style={node distance=2cm, auto, >=latex},
  gtu start/.style={draw, ellipse, fill=red!10, align=center, minimum height=2em},
  gtu stop/.style={gtu start},
  gtu input/.style={trapezium, trapezium left angle=70, trapezium right angle=110, draw, fill=orange!10, align=center, minimum height=2em},
  gtu output/.style={gtu input},
  gtu process/.style={gtu block},
  gtu tree/.style={grow=down, level 1/.style={sibling distance=3cm}, level 2/.style={sibling distance=1.5cm}},
  gtu root/.style={gtu block, fill=purple!10},
  gtu child/.style={gtu block, fill=yellow!10},
  wave/.style={decorate, decoration={snake, amplitude=0.4mm, segment length=2mm, post length=1mm}},
  zigzag/.style={decorate, decoration={zigzag, amplitude=0.4mm, segment length=2mm, post length=1mm}}
}
"""
    with open(clean_preamble_path, 'w') as f:
        f.write(minimal_preamble)

    # Generate Wrapper Content
    latex_content = []
    # explicit Crop via class option? standalone defaults to crop. 
    # But we also add "preview" just in case. 
    latex_content.append(r"\documentclass[tikz,border=0pt]{standalone}")
    # Don't pass geometry options!
    latex_content.append(f"\\input{{{clean_preamble_path}}}")
    # commands.tex is needed for \renewcommand in gujarati-boxes.tex
    COMMANDS_PATH = os.path.join(LATEX_TEMPLATES_DIR, "commands.tex")
    latex_content.append(f"\\input{{{COMMANDS_PATH}}}")
    
    # Disable headers/footers explicitly just in case
    latex_content.append(r"\pagestyle{empty}")
    
    if is_gujarati:
         latex_content.append(f"\\input{{{GUJARATI_BOXES_PATH}}}")
    # else:
    #      latex_content.append(f"\\input{{{ENGLISH_BOXES_PATH}}}")
    
    latex_content.append(r"\begin{document}")
    latex_content.append(f"\\input{{{snippet_abs_path}}}")
    latex_content.append(r"\end{document}")
    
    with open(wrapper_path, 'w') as f:
        f.write("\n".join(latex_content))
        
    # Compile
    # Use xelatex for font support
    cmd = [
        "xelatex",
        "-interaction=nonstopmode",
        "-output-directory", build_dir,
        wrapper_path
    ]
    
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=60)
        if result.returncode != 0:
            print(f"Error compiling {filename}:")
            print(result.stdout)
            print("---")
            # print(result.stderr) # xelatex output is mostly stdout
            return False
            
        # Move PDF to output
        generated_pdf = os.path.join(build_dir, "wrapper.pdf")
        target_pdf_name = filename.replace(".tex", ".pdf") # e.g. .gu.tex -> .gu.pdf is wrong? no. .gu.tex -> .gu.pdf ok. 
        # Wait, filename extension replace: if .gu.tex, basename is .gu? No.
        # os.path.splitext("a.gu.tex") -> ("a.gu", ".tex")
        # so basename variable has "a.gu"
        target_pdf_name = basename + ".pdf"
        target_pdf_path = os.path.join(pdf_output_dir, target_pdf_name)
        
        if os.path.exists(generated_pdf):
            shutil.copy2(generated_pdf, target_pdf_path)
            print(f"Success: {target_pdf_path}")
            return True
        else:
            print(f"PDF not found: {generated_pdf}")
            return False
            
    except Exception as e:
        print(f"Exception during compilation: {e}")
        return False
        
    finally:
        # Cleanup build dir
        # shutil.rmtree(build_dir)
        pass

def main():
    # Find targets
    # Hardcoded target for now as requested
    target_path = "/Users/milav/Code/milav-next/content/resources/study-materials/11-ec/sem-2/4321103-eca/GTU Solutions Short/figures/tex-diagrams/tex"
    
    tex_files = glob.glob(os.path.join(target_path, "*.tex"))
    
    
    
    # User requested to test few files first - Limit removed
    # Test specific file for fix - Removed
    # tex_files = [f for f in tex_files if "q1c.gu.tex" in f]
    
    print(f"Found {len(tex_files)} diagram files to compile.")
    
    success_count = 0
    failed_files = []
    
    for tf in tex_files:
        if compile_diagram(tf):
            success_count += 1
        else:
            failed_files.append(tf)
            
    print(f"Compilation Complete. Success: {success_count}, Failed: {len(failed_files)}")
    if failed_files:
        print("\nFailed Files:")
        for f in failed_files:
            print(f"- {os.path.basename(f)}")

if __name__ == "__main__":
    main()
