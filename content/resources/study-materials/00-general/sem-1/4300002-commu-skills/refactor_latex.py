
import re
import sys
import os

def refactor_latex(file_path):
    with open(file_path, 'r') as f:
        content = f.read()

    # 1. Standardize Header/Preamble
    # Locate \begin{document}
    if "\\begin{document}" in content:
        body = content.split("\\begin{document}")[1]
        # Remove \end{document} from the very end if it exists, to avoid duplication if we append it back? 
        # Actually pandoc output usually ends nice. Let's just keep the body.
        if "\\end{document}" in body:
            body = body.replace("\\end{document}", "")
    else:
        # Fallback if no begin document found (snippet?)
        body = content

    # New Header
    header = r"""\documentclass[10pt,a4paper]{article}
\input{../../../../../../latex-templates/gtu-solutions/preamble.tex}
\input{../../../../../../latex-templates/gtu-solutions/english-boxes.tex}

\begin{document}

"""
    
    # 2. Process Body Line by Line for Answer Wrapping
    lines = body.split('\n')
    new_lines = []
    in_solution_box = False
    
    # Regex to detect start of answer
    # Matches "\textbf{Answer}:" or "\textbf{Answer}: "
    answer_start_re = re.compile(r'\\textbf{Answer}\s*:')
    
    # Regex to detect start of Mnemonic
    mnemonic_start_re = re.compile(r'\\textbf{Mnemonic}\s*:')

    # Regex to identify "Mermaid" blocks (Shaded environment)
    in_shaded = False
    shaded_buffer = []

    for line in lines:
        stripped = line.strip()

        # Check for Mermaid Block Start
        if "\\begin{Shaded}" in line:
            in_shaded = True
            shaded_buffer = [line]
            continue
        
        if in_shaded:
            shaded_buffer.append(line)
            if "\\end{Shaded}" in line:
                in_shaded = False
                # Check if it was a graph
                full_block = "\n".join(shaded_buffer)
                if "graph LR" in full_block or "graph TD" in full_block or "mermaid" in full_block:
                    new_lines.append(r"\begin{center}")
                    new_lines.append(r"% TODO: MERMAID DIAGRAM DETECTED. PLEASE CONVERT TO TIKZ.")
                    new_lines.append(r"% Original Code:")
                    # Comment out the original code
                    for bl in shaded_buffer:
                        new_lines.append("% " + bl)
                    new_lines.append(r"\end{center}")
                else:
                    # Convert to verbatim if it's not a diagram
                    new_lines.append(r"\begin{verbatim}")
                    # Remove the \begin{Shaded}, \end{Shaded}, \begin{Highlighting}, \end{Highlighting} lines
                    # from the buffer before adding content
                    for bl in shaded_buffer:
                        if "\\begin{Shaded}" in bl or "\\end{Shaded}" in bl:
                            continue
                        if "\\begin{Highlighting}" in bl or "\\end{Highlighting}" in bl:
                            continue
                        # Also replace \NormalTok etc if present?
                        # Pandoc produces: \NormalTok{graph LR}
                        # We need to strip the macros. This is getting messy.
                        # Easier approach: Use regex to strip TeX commands from the line?
                        # Or just accept that we need to clean it up manually.
                        # BUT, for the email drafts (if any end up here), they shouldn't have highlighting macros if they were plain text.
                        # If they were stylized code blocks, they have macros.
                        # Let's try basic Macro stripping.
                        clean_line = re.sub(r'\\[a-zA-Z]+{([^}]*)}', r'\1', bl) # Simple strip \Cmd{Content} -> Content
                        clean_line = re.sub(r'\\[a-zA-Z]+', '', clean_line) # Strip standalone commands
                        new_lines.append(clean_line)
                    new_lines.append(r"\end{verbatim}")
                shaded_buffer = []
            continue

        # Logic to CLOSE solution box
        # We close if we see:
        # - \item
        # - \subsection
        # - \section
        # - \end{enumerate}
        # - Another \textbf{Answer} (unlikely nested)
        # - Start of Mnemonic
        
        is_break_point = (
            stripped.startswith(r"\item") or 
            stripped.startswith(r"\subsection") or 
            stripped.startswith(r"\section") or 
            stripped.startswith(r"\end{enumerate}") or
            mnemonic_start_re.search(line)
        )

        if in_solution_box and is_break_point:
            new_lines.append(r"\end{solutionbox}")
            in_solution_box = False

        # Logic to OPEN solution box
        if answer_start_re.search(line):
            # If we were already in one (shouldn't happen with proper structure), close it
            if in_solution_box:
                new_lines.append(r"\end{solutionbox}")
            
            new_lines.append(r"\begin{solutionbox}")
            in_solution_box = True
            # We want to keep the "Answer:" text inside? Or remove it?
            # Creating a clean box usually implies removing the redundant label "Answer:",
            # BUT the regex match might be in the middle of a line. 
            # For safety, let's keep the line as is for now, user can refine content later.
            # Actually, let's try to wrap it nicely.
            new_lines.append(line)
            continue
            
        # Mnemonic Handling
        # Usually one line? Or block?
        # Standard: \textbf{Mnemonic:} "..."
        # We can just wrap this single line or block.
        if mnemonic_start_re.search(line):
             # If solution box was open, close it (Mnemonics usually follow answers)
            if in_solution_box:
                new_lines.append(r"\end{solutionbox}")
                in_solution_box = False
            
            new_lines.append(r"\begin{mnemonicbox}")
            new_lines.append(line)
            new_lines.append(r"\end{mnemonicbox}")
            continue

        new_lines.append(line)

    # End of file cleanup
    if in_solution_box:
        new_lines.append(r"\end{solutionbox}")

    new_lines.append(r"\end{document}")

    # Write back
    final_content = header + "\n".join(new_lines)
    
    with open(file_path, 'w') as f:
        f.write(final_content)
    
    print(f"Refactored: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python refactor_latex.py <file_path>")
        sys.exit(1)
    
    path = sys.argv[1]
    if os.path.exists(path):
        refactor_latex(path)
    else:
        print(f"File not found: {path}")
