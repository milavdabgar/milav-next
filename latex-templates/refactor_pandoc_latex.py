#!/usr/bin/env python3
"""
Enhanced LaTeX Refactoring Script - v2
Critical improvements for 98/100 quality
Now standalone (merged with refactor_latex.py logic)
"""

import re
import sys
import os
from pathlib import Path

def get_project_root():
    """Find project root by looking for package.json or .git directory."""
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / 'package.json').exists() or (current / '.git').exists():
            return current
        current = current.parent
    return Path(__file__).resolve().parent.parent

def clean_escaped_brackets(content):
    """Remove unnecessary bracket escaping - CRITICAL FIX."""
    content = content.replace(r'{[}', '[')
    content = content.replace(r'{]}', ']')
    content = content.replace(r'{(}', '(')
    content = content.replace(r'{)}', ')')
    return content

def convert_unicode_to_latex(content):
    """Convert common Unicode characters to LaTeX equivalents."""
    
    # Superscripts (most common in scientific notation)
    superscripts = {
        '⁰': r'^{0}', '¹': r'^{1}', '²': r'^{2}', '³': r'^{3}', '⁴': r'^{4}',
        '⁵': r'^{5}', '⁶': r'^{6}', '⁷': r'^{7}', '⁸': r'^{8}', '⁹': r'^{9}',
        '⁺': r'^{+}', '⁻': r'^{-}', '⁼': r'^{=}', '⁽': r'^{(}', '⁾': r'^{)}',
        'ⁿ': r'^{n}', 'ⁱ': r'^{i}', 'ˣ': r'^{x}',
    }
    
    # Subscripts
    subscripts = {
        '₀': r'_{0}', '₁': r'_{1}', '₂': r'_{2}', '₃': r'_{3}', '₄': r'_{4}',
        '₅': r'_{5}', '₆': r'_{6}', '₇': r'_{7}', '₈': r'_{8}', '₉': r'_{9}',
        '₊': r'_{+}', '₋': r'_{-}', '₌': r'_{=}', '₍': r'_{(}', '₎': r'_{)}',
        'ₐ': r'_{a}', 'ₑ': r'_{e}', 'ₒ': r'_{o}', 'ₓ': r'_{x}',
        'ₕ': r'_{h}', 'ₖ': r'_{k}', 'ₗ': r'_{l}', 'ₘ': r'_{m}',
        'ₙ': r'_{n}', 'ₚ': r'_{p}', 'ₛ': r'_{s}', 'ₜ': r'_{t}',
    }
    
    # Math symbols
    math_symbols = {
        '×': r'\times',
        '÷': r'\div',
        '±': r'\pm',
        '∓': r'\mp',
        '≈': r'\approx',
        '≠': r'\neq',
        '≤': r'\leq',
        '≥': r'\geq',
        '∞': r'\infty',
        '∫': r'\int',
        '∑': r'\sum',
        '∏': r'\prod',
        '√': r'\sqrt',
        '∂': r'\partial',
        '∇': r'\nabla',
        '°': r'^\circ',  
        '′': r"'",  
        '″': r"''",  
        '‰': r'\text{\textperthousand}',
        '℃': r'^\circ C',
        '℉': r'^\circ F',
        'Å': r'\AA',
        '→': r'\rightarrow',
        '←': r'\leftarrow',
        '↔': r'\leftrightarrow',
        '⇒': r'\Rightarrow',
        '⇐': r'\Leftarrow',
        '⇔': r'\Leftrightarrow',
        '∈': r'\in',
        '∉': r'\notin',
        '⊂': r'\subset',
        '⊃': r'\supset',
        '∪': r'\cup',
        '∩': r'\cap',
        '∅': r'\emptyset',
        '∀': r'\forall',
        '∃': r'\exists',
        '∧': r'\wedge',
        '∨': r'\vee',
        '¬': r'\neg',
        '⊕': r'\oplus',
        '⊗': r'\otimes',
    }
    
    for unicode_char, latex_cmd in superscripts.items():
        content = content.replace(unicode_char, latex_cmd)
    
    for unicode_char, latex_cmd in subscripts.items():
        content = content.replace(unicode_char, latex_cmd)
    
    for unicode_char, latex_cmd in math_symbols.items():
        content = content.replace(unicode_char, latex_cmd)
    
    return content

def fix_section_titles(content):
    """Fix multi-line section titles."""
    lines = content.split('\n')
    fixed_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        if r'\subsection*{' in line and not line.rstrip().endswith('}'):
            title_parts = [line]
            i += 1
            while i < len(lines) and not lines[i-1].rstrip().endswith('}'):
                title_parts.append(lines[i])
                i += 1
                if i >= len(lines):
                    break
            
            full_title = ' '.join(part.strip() for part in title_parts)
            full_title = full_title.replace('{[}', '[')
            full_title = full_title.replace('{]}', ']')
            fixed_lines.append(full_title)
        else:
            fixed_lines.append(line)
            i += 1
    
    return '\n'.join(fixed_lines)

def format_calculation_steps(lines):
    """Separate multi-line equations."""
    formatted_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        if '=' in stripped and not stripped.startswith('\\'):
            eq_count = stripped.count('=')
            
            if eq_count >= 2:
                import re
                parts = re.split(r'(?<=[^\s=])\s+(?=[α-ωΑ-Ωa-zA-Z]\s*=)', stripped)
                
                if len(parts) > 1:
                    for part in parts:
                        if part.strip():
                            formatted_lines.append(part.strip())
                            formatted_lines.append('')
                else:
                    formatted_lines.append(line)
            else:
                formatted_lines.append(line)
        else:
            formatted_lines.append(line)
    
    return formatted_lines

def clean_enumerate_env(lines):
    """Remove verbose enumerate formatting."""
    cleaned_lines = []
    
    for i, line in enumerate(lines):
        if r'\def\labelenumi' in line or r'\setcounter{enumi}' in line:
            continue
        
        if line.strip() == r'\tightlist' and i > 0:
            if r'\begin{enumerate}' in lines[i-1]:
                continue
        
        cleaned_lines.append(line)
    
    return cleaned_lines

def simplify_labels(content):
    """Convert verbose labels to q1a, q2b format."""
    
    def create_label(match):
        full_match = match.group(0)
        title = match.group(1)
        old_label = match.group(2)
        
        q_pattern = r'(?:પ્રશ્ન|Question)\s*(\d+)\s*\(\s*([a-zA-Z])\s*\)'
        q_match = re.search(q_pattern, title)
        
        if q_match:
            num = q_match.group(1)
            letter = q_match.group(2).lower()
            new_label = f'q{num}{letter}'
            return full_match.replace(old_label, new_label)
        
        return full_match
    
    pattern = r'(\\subsection\*\{[^}]+\})\\label\{([^}]+)\}'
    content = re.sub(pattern, create_label, content)
    
    return content

def apply_box_structure(content, file_path):
    """Applies solution boxes, headers, and structural fixes (Replacing original refactor_latex.py logic)."""
    
    # 1. Standardize Header/Preamble
    if "\\begin{document}" in content:
        body = content.split("\\begin{document}")[1]
        if "\\end{document}" in body:
            body = body.replace("\\end{document}", "")
    else:
        body = content

    # New Header Logic
    is_gujarati = ".gu.tex" in file_path or ".gu." in file_path
    box_template = "gujarati-boxes.tex" if is_gujarati else "english-boxes.tex"
    
    basename = os.path.basename(file_path)
    filename_no_ext = os.path.splitext(basename)[0]
    
    subject_code = "Unknown Code"
    exam_season = "Study Material"
    subject_name = "Subject Name"

    # Minimal Subject Map (Expand as needed)
    subject_map = {
        "4300003": "Environment and Sustainability",
        "4300002": "Communication Skills", 
        "DI01000061": "Modern Physics",
        "DI01000071": "Chemistry",
        "DI01000021": "Mathematics-I",
        "DI01000051": "Basic Electronics",
        "DI01000101": "Basic Electronics"
    }

    parts = filename_no_ext.split('-')
    if len(parts) >= 1:
        subject_code = parts[0]
        if subject_code in subject_map:
            subject_name = subject_map[subject_code]
    
    if len(parts) >= 3:
        season = parts[1].capitalize()
        year = parts[2]
        if season in ["Summer", "Winter"] and year.isdigit():
            exam_season = f"{season} {year}"

    if is_gujarati:
        header_title = r"{\Huge\bfseries\color{headcolor} %s (Gujarati)}\\[5pt]" % subject_name
    else:
        header_title = r"{\Huge\bfseries\color{headcolor} %s Solutions}\\[5pt]" % subject_name

    header = r"""\documentclass[10pt,a4paper]{article}
\input{../../../../../../latex-templates/gtu-solutions/preamble.tex}
\input{../../../../../../latex-templates/gtu-solutions/%s}

\begin{document}

\begin{center}
%s
{\LARGE %s -- %s}\\[3pt]
{\large Semester 1 Study Material}\\[3pt]
{\normalsize\textit{Detailed Solutions and Explanations}}
\end{center}

\vspace{10pt}

""" % (box_template, header_title, subject_code, exam_season)
    
    lines = body.split('\n')
    new_lines = []
    in_solution_box = False
    in_mnemonic_box = False
    
    answer_start_re = re.compile(r'\\textbf{(?:Answer|જવાબ)[:\s}]')
    mnemonic_start_re = re.compile(r'\\textbf{(?:Mnemonic|યાદશક્તિ સૂત્ર|મેમરી ટ્રીક)[:\s}]')
    table_caption_re = re.compile(r'\\textbf{(?:Table|કોષ્ટક)\s*:\s*(.*)}')
    
    pending_caption = None
    
    # NOTE: Shaded block handling removed to rely on Pandoc's lstlisting + listings package
    
    for line in lines:
        stripped = line.strip()

        # Fix Section/Subsection Numbering
        if line.strip().startswith(r"\subsection{"):
            line = line.replace(r"\subsection{", r"\subsection*{")
        if line.strip().startswith(r"\section{"):
            line = line.replace(r"\section{", r"\section*{")

        # Break Point Detection
        is_section_break = (
            stripped.startswith(r"\section") or 
            stripped.startswith(r"\subsection") or
            stripped.startswith(r"\subsubsection") or
            stripped.startswith(r"\paragraph") or
            stripped.startswith(r"\subparagraph")
        )
        
        is_horizontal_rule = r"\begin{center}\rule{" in line
        is_mnemonic_start = mnemonic_start_re.search(line)
        is_answer_start = answer_start_re.search(line)

        # Logic to CLOSE boxes
        if is_section_break or is_mnemonic_start or is_answer_start or is_horizontal_rule:
            if pending_caption:
                new_lines.append(r"\textbf{Table: %s}" % pending_caption)
                pending_caption = None

            if in_solution_box:
                new_lines.append(r"\end{solutionbox}")
                in_solution_box = False
            if in_mnemonic_box:
                new_lines.append(r"\end{mnemonicbox}")
                in_mnemonic_box = False

        # Logic to OPEN boxes
        
        # 1. Answer Box
        if is_answer_start:
            new_lines.append(r"\begin{solutionbox}")
            in_solution_box = True
            clean_line = re.sub(r'\\textbf{(?:Answer|જવાબ)[^}]*}(\s*:)?', '', line).strip()
            if clean_line:
                new_lines.append(clean_line)
            continue
            
        # 2. Mnemonic Box
        if is_mnemonic_start:
            new_lines.append(r"\begin{mnemonicbox}")
            in_mnemonic_box = True
            clean_line = re.sub(r'\\textbf{(?:Mnemonic|યાદશક્તિ સૂત્ર|મેમરી ટ્રીક)[^}]*}(\s*:)?', '', line).strip()
            if clean_line:
                new_lines.append(clean_line)
            continue
            
        # 3. Table Caption Detection
        caption_match = table_caption_re.match(line.strip())
        if caption_match:
            pending_caption = caption_match.group(1)
            continue # Don't print this line yet

        # 4. Table Start Detection (Inject Caption)
        if r"\begin{longtable}" in line:
             if pending_caption:
                 new_lines.append(r"\vspace{-5pt}") 
                 new_lines.append(r"\captionof{table}{%s}" % pending_caption)
                 new_lines.append(r"\vspace{-10pt}") 
                 pending_caption = None
             new_lines.append(line)
             continue
        
        # 5. Flush pending caption
        if pending_caption and stripped and not stripped.startswith(r"{\def\LTcaptype") and not stripped.startswith(r"\begin{longtable}") and not stripped.startswith(r">") and not stripped.startswith(r"@"):
             if stripped.startswith("%") or stripped.startswith(r"{\def\LTcaptype"):
                 pass 
             else:
                 new_lines.append(r"\textbf{Table: %s}" % pending_caption)
                 pending_caption = None
        
        new_lines.append(line)

    if in_solution_box:
        new_lines.append(r"\end{solutionbox}")
    if in_mnemonic_box:
        new_lines.append(r"\end{mnemonicbox}")

    new_lines.append(r"\end{document}")
    
    return header + "\n".join(new_lines)

def refactor_latex(file_path):
    """Enhanced refactor with all improvements."""
    
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Pre-processing Fixes
    content = clean_escaped_brackets(content)
    content = convert_unicode_to_latex(content)
    content = fix_section_titles(content)
    
    # 2. Apply Structural Changes (Box Logic) - Merged from refactor_latex.py
    content = apply_box_structure(content, file_path)

    # 3. Post-processing on the structured content
    # Extract body again since apply_box_structure adds headers
    if "\\begin{document}" in content:
        header = content.split("\\begin{document}")[0] + "\\begin{document}"
        body = content.split("\\begin{document}")[1]
        if "\\end{document}" in body:
            body = body.replace("\\end{document}", "")
    else:
        header = ""
        body = content
    
    lines = body.split('\n')
    
    lines = format_calculation_steps(lines)
    lines = clean_enumerate_env(lines)
    
    final_content = header + '\n'.join(lines) + '\n\\end{document}\n'
    final_content = simplify_labels(final_content)
    
    # Write final
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"✅ Refactored with improvements: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python refactor_latex_v2.py <file_path>")
        sys.exit(1)
    
    path = sys.argv[1]
    if os.path.exists(path):
        refactor_latex(path)
    else:
        print(f"❌ File not found: {path}")
