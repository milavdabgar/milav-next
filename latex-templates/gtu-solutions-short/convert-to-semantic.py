#!/usr/bin/env python3
"""
Convert LaTeX solution file to use semantic commands and proper environments.
This script performs systematic conversion while preserving code integrity.
"""

import re
import sys

def convert_question_headings(content):
    """Convert section headings to semantic questionmarks command."""
    # Pattern: \section*{Question X(Y) [Z marks]}
    #          \textbf{Question text}
    pattern = r'\\section\*\{Question\s+([^[]+)\s+\[(\d+)\s+marks\]\}\s*\n\\textbf\{([^}]+)\}'
    replacement = r'\\questionmarks{\1}{\2}{\3}'
    return re.sub(pattern, replacement, content)

def convert_tables(content):
    """Convert center+captionof to proper table environment."""
    # This is complex, needs manual review
    # For now, just document the pattern
    return content

def convert_figures(content):
    """Convert center+captionof to proper figure environment with caption AFTER content."""
    # Pattern: \begin{center}
    #          \captionof{figure}{Title}
    #          \begin{tikzpicture}...
    #          \end{tikzpicture}
    #          \end{center}
    
    # This needs careful handling to move caption after tikzpicture
    # For now, document the manual process
    return content

def convert_keywords(content):
    """Convert \textbf{Term}: to \keyword{Term}:"""
    # Only in itemize environments
    pattern = r'\\item\s+\\textbf\{([^}]+)\}:'
    replacement = r'\\item \\keyword{\1}:'
    return re.sub(pattern, replacement, content)

def convert_mnemonics(content):
    """Convert "text" to \mnemonic{text} in mnemonicbox."""
    # Only inside mnemonicbox
    lines = content.split('\n')
    result = []
    in_mnemonic = False
    
    for line in lines:
        if '\\begin{mnemonicbox}' in line:
            in_mnemonic = True
            result.append(line)
        elif '\\end{mnemonicbox}' in line:
            in_mnemonic = False
            result.append(line)
        elif in_mnemonic and line.strip().startswith('"'):
            # Convert "text" to \mnemonic{text}
            text = line.strip().strip('"')
            result.append(f'\\mnemonic{{{text}}}')
        else:
            result.append(line)
    
    return '\n'.join(result)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 convert.py input.tex")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Apply conversions
    content = convert_question_headings(content)
    content = convert_keywords(content)
    content = convert_mnemonics(content)
    
    # Write output
    output_file = filename.replace('.tex', '-semantic.tex')
    with open(output_file, 'w') as f:
        f.write(content)
    
    print(f"Converted file written to: {output_file}")
    print("\nManual steps still needed:")
    print("1. Convert tables: \\begin{center}\\captionof{table} -> \\begin{table}[htbp]")
    print("2. Convert figures: Move \\caption{} AFTER tikzpicture")
    print("3. Review all conversions")

if __name__ == '__main__':
    main()
