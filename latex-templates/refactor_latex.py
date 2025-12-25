
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
    is_gujarati = ".gu.tex" in file_path or ".gu." in file_path
    box_template = "gujarati-boxes.tex" if is_gujarati else "english-boxes.tex"
    
    # Extract Metadata from filename
    # Expected format: CODE-Season-Year-solution.tex or CODE.tex
    basename = os.path.basename(file_path)
    filename_no_ext = os.path.splitext(basename)[0]
    
    subject_code = "Unknown Code"
    exam_season = "Study Material"
    subject_name = "Subject Name"

    # Minimal Subject Map
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
        # Try to parse Season-Year e.g. Summer-2022 or Winter-2023
        season = parts[1].capitalize()
        year = parts[2]
        if season in ["Summer", "Winter"] and year.isdigit():
            exam_season = f"{season} {year}"

    # Verify Gujarati Titles if needed (Optional: Logic to localized titles)
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
    
    # Regex to detect start of answer
    # Matches "\textbf{Answer}:", "\textbf{Answer:}" or similar
    # Also support Gujarati "Jawab" -> \textbf{જવાબ}
    answer_start_re = re.compile(r'\\textbf{(?:Answer|જવાબ)[:\s}]')
    
    # Regex to detect start of Mnemonic
    # Also support Gujarati "Yadshakti Sutra" -> \textbf{યાદશક્તિ સૂત્ર} and "Memory Trick" -> \textbf{મેમરી ટ્રીક}
    mnemonic_start_re = re.compile(r'\\textbf{(?:Mnemonic|યાદશક્તિ સૂત્ર|મેમરી ટ્રીક)[:\s}]')

    # Regex to identify "Mermaid" blocks (Shaded environment)
    # Regex for Table Caption (e.g. \textbf{Table: Title})
    # We want to capture the Title part.
    # Also support Gujarati "Koshtak" -> \textbf{કોષ્ટક}
    table_caption_re = re.compile(r'\\textbf{(?:Table|કોષ્ટક)\s*:\s*(.*)}')
    pending_caption = None
    
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
                full_block = "\n".join(shaded_buffer)
                
                # Check if we have a pending caption (flush it if we hit a code block)
                if pending_caption:
                    new_lines.append(r"\textbf{Table: %s}" % pending_caption)
                    pending_caption = None

                if "graph LR" in full_block or "graph TD" in full_block or "mermaid" in full_block:
                    new_lines.append(r"\begin{center}")
                    new_lines.append(r"\textbf{Mermaid Diagram (Code)}")
                    new_lines.append(r"\begin{verbatim}")
                    for bl in shaded_buffer:
                        clean_line = re.sub(r'\\(NormalTok|StringTok|KeywordTok|DataTypeTok|DecValTok|BaseNtTok|FloatTok|CharTok|CommentTok|OtherTok|AlertTok|FunctionTok|RegionMarkerTok|ErrorTok){([^}]*)}', r'\2', bl)
                        clean_line = re.sub(r'\\[a-zA-Z]+', '', clean_line) 
                        new_lines.append(clean_line)
                    new_lines.append(r"\end{verbatim}")
                    new_lines.append(r"\end{center}")
                else:
                    new_lines.append(r"\begin{verbatim}")
                    for bl in shaded_buffer:
                        if "\\begin{Shaded}" in bl or "\\end{Shaded}" in bl:
                            continue
                        if "\\begin{Highlighting}" in bl or "\\end{Highlighting}" in bl:
                            continue
                        clean_line = re.sub(r'\\[a-zA-Z]+{([^}]*)}', r'\1', bl) 
                        clean_line = re.sub(r'\\[a-zA-Z]+', '', clean_line) 
                        new_lines.append(clean_line)
                    new_lines.append(r"\end{verbatim}")
                shaded_buffer = []
            continue

        # Fix Section/Subsection Numbering (Indent to unnumbered)
        if line.strip().startswith(r"\subsection{"):
            line = line.replace(r"\subsection{", r"\subsection*{")
        if line.strip().startswith(r"\section{"):
            line = line.replace(r"\section{", r"\section*{")

        # Break Point Detection (New Section, Subsection, or Mnemonic Start)
        # We need to cover \section, \subsection, \subsubsection, \paragraph, \subparagraph
        is_section_break = (
            stripped.startswith(r"\section") or 
            stripped.startswith(r"\subsection") or
            stripped.startswith(r"\subsubsection") or
            stripped.startswith(r"\paragraph") or
            stripped.startswith(r"\subparagraph")
        )
        
        is_mnemonic_start = mnemonic_start_re.search(line)
        is_answer_start = answer_start_re.search(line)

        # Logic to CLOSE boxes if we hit a break point
        if is_section_break or is_mnemonic_start or is_answer_start:
            # Flush pending caption if we hit a section break (unlikely table follows)
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
        # Check if this line STARTS a longtable
        if r"\begin{longtable}" in line:
             if pending_caption:
                 # Inject captionof BEFORE the table starts
                 new_lines.append(r"\vspace{-5pt}") 
                 new_lines.append(r"\captionof{table}{%s}" % pending_caption)
                 new_lines.append(r"\vspace{-10pt}") # Pull table closer
                 pending_caption = None
             
             new_lines.append(line)
             continue
        
        # 5. Flush pending caption if line is not related to table start and not empty
        if pending_caption and stripped and not stripped.startswith(r"{\def\LTcaptype") and not stripped.startswith(r"\begin{longtable}") and not stripped.startswith(r">") and not stripped.startswith(r"@"):
             # Wait, Pandoc sometimes puts {\def\LTcaptype...} before table.
             # If it's a part of table def (lines starting with > or @), wait.
             if stripped.startswith("%") or stripped.startswith(r"{\def\LTcaptype"):
                 pass # keep pending
             else:
                 # Flush it, it wasn't a table
                 new_lines.append(r"\textbf{Table: %s}" % pending_caption)
                 pending_caption = None
        
        if pending_caption and r"\def\LTcaptype{none}" in line:
            # We skip this line if we have a pending caption, 
            # OR we keep it? 
            # If we keep it, longtable won't try to be a float, which is good.
            # \captionof handles the caption.
            pass
            
        new_lines.append(line)

    # End of file cleanup
    if in_solution_box:
        new_lines.append(r"\end{solutionbox}")
    if in_mnemonic_box:
        new_lines.append(r"\end{mnemonicbox}")

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
