#!/usr/bin/env python3
"""
Enhanced LaTeX Refactoring Script - v2
Critical improvements for 98/100 quality
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
    
    # Greek letters (lowercase)
    greek_lower = {
        'α': r'\alpha', 'β': r'\beta', 'γ': r'\gamma', 'δ': r'\delta',
        'ε': r'\epsilon', 'ζ': r'\zeta', 'η': r'\eta', 'θ': r'\theta',
        'ι': r'\iota', 'κ': r'\kappa', 'λ': r'\lambda', 'μ': r'\mu',
        'ν': r'\nu', 'ξ': r'\xi', 'π': r'\pi', 'ρ': r'\rho',
        'σ': r'\sigma', 'τ': r'\tau', 'υ': r'\upsilon', 'φ': r'\phi',
        'χ': r'\chi', 'ψ': r'\psi', 'ω': r'\omega',
    }
    
    # Greek letters (uppercase)
    greek_upper = {
        'Α': r'\Alpha', 'Β': r'\Beta', 'Γ': r'\Gamma', 'Δ': r'\Delta',
        'Ε': r'\Epsilon', 'Ζ': r'\Zeta', 'Η': r'\Eta', 'Θ': r'\Theta',
        'Ι': r'\Iota', 'Κ': r'\Kappa', 'Λ': r'\Lambda', 'Μ': r'\Mu',
        'Ν': r'\Nu', 'Ξ': r'\Xi', 'Π': r'\Pi', 'Ρ': r'\Rho',
        'Σ': r'\Sigma', 'Τ': r'\Tau', 'Υ': r'\Upsilon', 'Φ': r'\Phi',
        'Χ': r'\Chi', 'Ψ': r'\Psi', 'Ω': r'\Omega',
    }
    
    # Mathematical symbols
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
        '°': r'^\circ',  # Degree symbol
        '′': r"'",  # Prime
        '″': r"''",  # Double prime
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
    
    # Apply conversions (order matters - do superscripts/subscripts first)
    for unicode_char, latex_cmd in superscripts.items():
        content = content.replace(unicode_char, latex_cmd)
    
    for unicode_char, latex_cmd in subscripts.items():
        content = content.replace(unicode_char, latex_cmd)
    
    # DISABLED: Greek letters are already properly formatted in source
    # Converting them causes math mode issues in tables
    # for unicode_char, latex_cmd in greek_lower.items():
    #     content = content.replace(unicode_char, latex_cmd)
    
    # for unicode_char, latex_cmd in greek_upper.items():
    #     content = content.replace(unicode_char, latex_cmd)
    
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
    """Separate multi-line equations - CRITICAL FIX."""
    formatted_lines = []
    
    for line in lines:
        stripped = line.strip()
        
        # Detect: "α = ... α = ... α = ..."
        if '=' in stripped and not stripped.startswith('\\'):
            eq_count = stripped.count('=')
            
            if eq_count >= 2:
                # Simple split: look for variable names followed by =
                # Pattern: "α = result α = next"
                import re
                parts = re.split(r'(?<=[^\s=])\s+(?=[α-ωΑ-Ωa-zA-Z]\s*=)', stripped)
                
                if len(parts) > 1:
                    for part in parts:
                        if part.strip():
                            formatted_lines.append(part.strip())
                            formatted_lines.append('')  # Blank line
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

# Import original functions from refactor_latex.py
from refactor_latex import refactor_latex as original_refactor

def refactor_latex(file_path):
    """Enhanced refactor with all improvements."""
    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # IMPROVEMENT 1: Fix escaped brackets (CRITICAL)
    content = clean_escaped_brackets(content)
    
    # IMPROVEMENT 2: Convert Unicode to LaTeX (NEW - CRITICAL)
    content = convert_unicode_to_latex(content)
    
    # IMPROVEMENT 3: Fix section titles
    content = fix_section_titles(content)
    
    # Write temp file
    temp_path = file_path + '.temp'
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Run original refactor on temp file
    original_refactor(temp_path)
    
    # Read result
    with open(temp_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract body for further processing
    if "\\begin{document}" in content:
        header = content.split("\\begin{document}")[0] + "\\begin{document}"
        body = content.split("\\begin{document}")[1]
        if "\\end{document}" in body:
            body = body.replace("\\end{document}", "")
    else:
        header = ""
        body = content
    
    lines = body.split('\n')
    
    # IMPROVEMENT 3: Format calculations (CRITICAL)
    lines = format_calculation_steps(lines)
    
    # IMPROVEMENT 4: Clean enumerate
    lines = clean_enumerate_env(lines)
    
    # Reconstruct
    final_content = header + '\n'.join(lines) + '\n\\end{document}\n'
    
    # IMPROVEMENT 5: Simplify labels
    final_content = simplify_labels(final_content)
    
    # Write final
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    # Clean up temp
    if os.path.exists(temp_path):
        os.remove(temp_path)
    
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
