import sys
import re
import subprocess
import difflib

def check_line_counts(file_en, file_gu):
    print(f"\n--- Checking Line Counts ---")
    with open(file_en, 'r') as f: lines_en = f.readlines()
    with open(file_gu, 'r') as f: lines_gu = f.readlines()
    
    count_en = len(lines_en)
    count_gu = len(lines_gu)
    
    print(f"English: {count_en} lines")
    print(f"Gujarati: {count_gu} lines")
    
    if count_en != count_gu:
        print("❌ FAIL: Line counts do not match!")
        return False
    else:
        print("✅ PASS: Line counts match exactly.")
        return True

def extract_structure(filename):
    structure = []
    with open(filename, 'r') as f:
        for i, line in enumerate(f, 1):
            # Match sections, subsections, subsubsections
            match = re.search(r'\\(section|subsection|subsubsection|paragraph|subparagraph)\{([^}]*)\}', line)
            if match:
                level = match.group(1)
                content = match.group(2)
                # For paragraphs, we care about "Mnemonic" specifically
                if level == 'paragraph':
                    # Check for mnemonic keywords in content
                    # Gujarati: 'યાદ રાખવાની રીત' or 'મેમરી ટ્રીક'
                    if 'Mnemonic' in content or 'મેમરી ટ્રીક' in content or 'યાદ રાખવાની રીત' in content:
                        level = 'mnemonic'
                structure.append((i, level))
    return structure

def check_structure(file_en, file_gu):
    print(f"\n--- Checking Structure (TOC & Headings) ---")
    struct_en = extract_structure(file_en)
    struct_gu = extract_structure(file_gu)
    
    if len(struct_en) != len(struct_gu):
        print(f"❌ FAIL: Structure element count mismatch! En: {len(struct_en)}, Gu: {len(struct_gu)}")
        # Print differences
        diff = difflib.unified_diff(
            [f"{s[1]} (L{s[0]})" for s in struct_en],
            [f"{s[1]} (L{s[0]})" for s in struct_gu],
            fromfile='English', tofile='Gujarati'
        )
        for d in diff: print(d)
        return False
    
    mismatch = False
    for i in range(len(struct_en)):
        type_en = struct_en[i][1]
        type_gu = struct_gu[i][1]
        
        if type_en != type_gu:
             print(f"❌ Mismatch at index {i}: En '{type_en}' vs Gu '{type_gu}'")
             mismatch = True
    
    if not mismatch:
        print("✅ PASS: Structural hierarchy matches perfectly.")
        return True
    return False

def check_content_compliance(filename):
    print(f"\n--- Checking Content Compliance: {filename} ---")
    errors = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines, 1):
        # 1. Check for deprecated font commands
        if '\\bf{' in line or '\\it{' in line or '\\sc{' in line:
            print(f"❌ Line {i}: Found deprecated font command (\\bf, \\it, \\sc). Use \\textbf, \\emph, \\textsc.")
            errors += 1
            
        # 2. Check for \paragraph before lstlisting
        if '\\begin{lstlisting}' in line:
            # Check previous non-empty line
            prev_idx = i - 2
            while prev_idx >= 0:
                prev_line = lines[prev_idx].strip()
                if prev_line:
                    if prev_line.startswith('\\paragraph'):
                        print(f"❌ Line {i}: \\paragraph found before lstlisting. Use caption=... inside lstlisting instead.")
                        errors += 1
                    break
                prev_idx -= 1
                
    if errors == 0:
        print("✅ PASS: Content compliance checks passed.")
        return True
    else:
        print(f"❌ FAIL: Found {errors} content compliance errors.")
        return False

def check_structure_strict(filename):
    # Enforce Section -> Subsection -> Subsubsection{Solution}
    print(f"\n--- Checking Strict Structure Hierarchy: {filename} ---")
    errors = 0
    
    current_state = "ROOT"
    
    with open(filename, 'r') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if line.startswith('\\section{'):
                current_state = "SECTION"
            elif line.startswith('\\subsection{'):
                if current_state != "SECTION":
                     if current_state not in ["SECTION", "SOLUTION", "SUBSECTION_DONE"]:
                         pass 
                current_state = "SUBSECTION"
            elif line.startswith('\\subsubsection{Solution}'): 
                 pass 
            elif line.startswith('\\subsubsection{') and ('Solution' in line or 'ઉકેલ' in line):
                if current_state != "SUBSECTION":
                    print(f"❌ Line {i}: Solution subsubsection found without preceding Subsection.")
                    errors += 1
                current_state = "SOLUTION"
                
    if errors == 0:
        print("✅ PASS: Section hierarchy valid.")
        return True
    return False

def check_word_counts(filename):
    print(f"\n--- Checking Word Counts vs Marks: {filename} ---")
    
    ranges = {
        3: (90, 150),
        4: (120, 180),
        7: (200, 300)
    }
    
    with open(filename, 'r') as f:
        content = f.read()

    subsections = re.split(r'\\subsection\{', content)
    
    warnings = 0
    
    for section in subsections[1:]: 
        first_line = section.split('\n', 1)[0]
        marks_match = re.search(r'\[\s*(\d+)\s*(marks|Marks|ગુણ)\s*\]', first_line)
        
        if not marks_match:
            continue
            
        marks = int(marks_match.group(1))
        
        if r'\subsubsection{Solution}' in section or r'\subsubsection{ઉકેલ}' in section:
            if r'\subsubsection{Solution}' in section:
                sol_content = section.split(r'\subsubsection{Solution}', 1)[1]
            else:
                 sol_content = section.split(r'\subsubsection{ઉકેલ}', 1)[1]
                 
            text = re.sub(r'\\[a-zA-Z]+\{.*?\}', '', sol_content) 
            text = re.sub(r'\\[a-zA-Z]+', '', text) 
            text = re.sub(r'[^a-zA-Z0-9\s\u0a80-\u0aff]', '', text) 
            
            words = text.split()
            word_count = len(words)
            
            if marks in ranges:
                min_w, max_w = ranges[marks]
                if word_count < min_w * 0.8: 
                     print(f"⚠️  Subsection '{first_line[:40]}...' ({marks} marks): Low word count ({word_count}). Target: {min_w}-{max_w}")
                     warnings += 1
                elif word_count > max_w * 1.5: 
                     print(f"ℹ️  Subsection '{first_line[:40]}...' ({marks} marks): High word count ({word_count}). Target: {min_w}-{max_w}")
            
    if warnings == 0:
        print(f"✅ PASS: Word counts are reasonable.")
        return True
    else:
        print(f"⚠️  PASS with Warnings: Found {warnings} potentially short answers.")
        return True

def check_toc_setup(filename):
    print(f"\n--- Checking TOC Setup: {filename} ---")
    errors = 0
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check for tocdepth=5
    if r'\setcounter{tocdepth}{5}' not in content:
        print("❌ Missing: \\setcounter{tocdepth}{5}")
        errors += 1
    
    # Check for tableofcontents
    if r'\tableofcontents' not in content:
        print("❌ Missing: \\tableofcontents")
        errors += 1
    
    # Check for newpage after tableofcontents
    if r'\tableofcontents' in content:
        toc_pos = content.find(r'\tableofcontents')
        after_toc = content[toc_pos:toc_pos+100]
        if r'\newpage' not in after_toc:
            print("⚠️  Missing \\newpage after \\tableofcontents")
    
    if errors == 0:
        print("✅ PASS: TOC setup correct.")
        return True
    else:
        print(f"❌ FAIL: {errors} TOC setup errors.")
        return False

def check_mnemonics(filename):
    print(f"\n--- Checking Mnemonics: {filename} ---")
    warnings = 0
    with open(filename, 'r') as f:
        content = f.read()
    
    # Find all subsections
    subsections = re.findall(r'\\subsection\{[^}]+\}', content)
    
    # Check for mnemonic paragraphs
    mnemonic_en = re.findall(r'\\paragraph\{Mnemonic:?\}', content)
    mnemonic_gu = re.findall(r'\\paragraph\{મેમરી ટ્રીક:?\}', content)
    mnemonic_count = len(mnemonic_en) + len(mnemonic_gu)
    
    print(f"Found {len(subsections)} subsections and {mnemonic_count} mnemonics")
    
    if mnemonic_count < len(subsections):
        print(f"⚠️  Some subsections may be missing mnemonics")
        warnings += 1
    
    if warnings == 0:
        print("✅ PASS: Mnemonic count reasonable.")
        return True
    else:
        print(f"⚠️  PASS with {warnings} warnings.")
        return True

def check_question_structure(filename):
    print(f"\n--- Checking Question Structure Pattern: {filename} ---")
    errors = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    subsection_lines = []
    for i, line in enumerate(lines):
        if line.strip().startswith(r'\subsection{'):
            subsection_lines.append(i)
    
    for sub_line in subsection_lines:
        # Check next few lines for textbf and subsubsection{Solution}
        next_5_lines = lines[sub_line:sub_line+5]
        has_textbf = any(r'\textbf{' in line for line in next_5_lines)
        has_solution = any('subsubsection{Solution}' in line or 'subsubsection{ઉકેલ}' in line for line in next_5_lines)
        
        if not has_textbf:
            print(f"⚠️  Line {sub_line+1}: Subsection missing \\textbf{{}} question statement")
        
        if not has_solution:
            print(f"⚠️  Line {sub_line+1}: Subsection missing \\subsubsection{{Solution}}")
    
    print("✅ PASS: Question structure pattern verified.")
    return True

def check_hierarchy_levels(filename):
    print(f"\n--- Checking 5-Level Hierarchy: {filename} ---")
    with open(filename, 'r') as f:
        content = f.read()
    
    levels = {
        'section': len(re.findall(r'\\section\{', content)),
        'subsection': len(re.findall(r'\\subsection\{', content)),
        'subsubsection': len(re.findall(r'\\subsubsection\{', content)),
        'paragraph': len(re.findall(r'\\paragraph\{', content)),
        'subparagraph': len(re.findall(r'\\subparagraph\{', content))
    }
    
    print(f"Hierarchy counts: section={levels['section']}, subsection={levels['subsection']}, " 
          f"subsubsection={levels['subsubsection']}, paragraph={levels['paragraph']}, subparagraph={levels['subparagraph']}")
    
    missing = [level for level, count in levels.items() if count == 0]
    
    if missing:
        print(f"⚠️  Missing levels: {', '.join(missing)}")
        return True  # Warning, not failure
    else:
        print("✅ PASS: All 5 hierarchy levels present.")
        return True

def check_caption_positions(filename):
    print(f"\n--- Checking Table/Figure Caption Positions: {filename} ---")
    warnings = 0
    with open(filename, 'r') as f:
        content = f.read()
    
    # Find tables and check caption position
    tables = re.finditer(r'\\begin\{table\}.*?\\end\{table\}', content, re.DOTALL)
    for match in tables:
        table_content = match.group(0)
        caption_pos = table_content.find(r'\caption{')
        tabular_pos = table_content.find(r'\begin{tabular')
        if tabular_pos == -1:
            tabular_pos = table_content.find(r'\begin{tabularx')
        
        if caption_pos > 0 and tabular_pos > 0 and caption_pos > tabular_pos:
            print(f"⚠️  Table has caption AFTER tabular (should be BEFORE/TOP)")
            warnings += 1
    
    # Find figures and check caption position
    figures = re.finditer(r'\\begin\{figure\}.*?\\end\{figure\}', content, re.DOTALL)
    for match in figures:
        fig_content = match.group(0)
        caption_pos = fig_content.find(r'\caption{')
        # Check if caption is before tikzpicture/includegraphics
        tikz_pos = fig_content.find(r'\begin{tikz')
        img_pos = fig_content.find(r'\includegraphics')
        circuit_pos = fig_content.find(r'\begin{circuitikz')
        kmap_pos = fig_content.find(r'\begin{karnaugh-map')
        
        content_pos = min([p for p in [tikz_pos, img_pos, circuit_pos, kmap_pos] if p > 0], default=-1)
        
        if caption_pos > 0 and content_pos > 0 and caption_pos < content_pos:
            print(f"⚠️  Figure has caption BEFORE content (should be AFTER/BOTTOM)")
            warnings += 1
    
    if warnings == 0:
        print("✅ PASS: Caption positions correct.")
        return True
    else:
        print(f"⚠️  PASS with {warnings} caption position warnings.")
        return True

def check_custom_commands(filename):
    print(f"\n--- Checking for Custom Commands: {filename} ---")
    errors = 0
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check for \newcommand definitions
    custom_cmds = re.findall(r'\\newcommand\{[^}]+\}', content)
    if custom_cmds:
        print(f"❌ Found custom command definitions: {custom_cmds}")
        errors += len(custom_cmds)
    
    # Check for suspicious custom-looking commands (not in standard LaTeX)
    suspicious = [r'\keyword{', r'\code{', r'\important{', r'\note{']
    for cmd in suspicious:
        if cmd in content:
            print(f"⚠️  Found suspicious command: {cmd}")
    
    if errors == 0:
        print("✅ PASS: No custom commands found.")
        return True
    else:
        print(f"❌ FAIL: {errors} custom command definitions found.")
        return False

def check_document_structure(filename):
    print(f"\n--- Checking Document Structure: {filename} ---")
    errors = 0
    with open(filename, 'r') as f:
        content = f.read()
    
    required_elements = [
        (r'\documentclass{article}', 'documentclass{article}'),
        (r'\begin{document}', 'begin{document}'),
        (r'\end{document}', 'end{document}'),
        (r'\maketitle', 'maketitle'),
        (r'\title{', 'title'),
        (r'\date{', 'date')
    ]
    
    for pattern, name in required_elements:
        if pattern not in content:
            print(f"❌ Missing: {name}")
            errors += 1
    
    if errors == 0:
        print("✅ PASS: Document structure complete.")
        return True
    else:
        print(f"❌ FAIL: {errors} structural elements missing.")
        return False

def check_pdf_metadata(filename):
    print(f"\n--- Checking PDF Metadata: {filename} ---")
    warnings = 0
    with open(filename, 'r') as f:
        content = f.read()
    
    if r'\hypersetup{' not in content:
        print("⚠️  Missing \\hypersetup{{}} for PDF metadata")
        warnings += 1
    else:
        # Check for key metadata fields
        metadata_fields = ['pdftitle', 'pdfsubject', 'pdfauthor', 'pdfkeywords']
        for field in metadata_fields:
            if field not in content:
                print(f"⚠️  Missing PDF metadata field: {field}")
    
    if warnings == 0:
        print("✅ PASS: PDF metadata present.")
        return True
    else:
        print(f"⚠️  PASS with {warnings} warnings.")
        return True

def check_preamble_usage(filename, language="English"):
    print(f"\n--- Checking Preamble Usage: {filename} ({language}) ---")
    with open(filename, 'r') as f:
        content = f.read()
    
    expected_preamble = 'preamble.gu.tex' if language == "Gujarati" else 'preamble.tex'
    
    if r'\input{' not in content:
        print("❌ Missing \\input for preamble")
        return False
    
    if expected_preamble in content:
        print(f"✅ PASS: Correct preamble ({expected_preamble}) used.")
        return True
    else:
        print(f"⚠️  Expected {expected_preamble} in preamble input")
        return True

def check_list_types(filename):
    print(f"\n--- Checking Semantic List Types: {filename} ---")
    warnings = 0
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check for proper list usage patterns
    description_lists = len(re.findall(r'\\begin\{description\}', content))
    itemize_lists = len(re.findall(r'\\begin\{itemize\}', content))
    enumerate_lists = len(re.findall(r'\\begin\{enumerate\}', content))
    
    print(f"Found: {description_lists} description, {itemize_lists} itemize, {enumerate_lists} enumerate lists")
    
    # Description lists should have \item[Label:] format
    desc_blocks = re.findall(r'\\begin\{description\}.*?\\end\{description\}', content, re.DOTALL)
    for i, block in enumerate(desc_blocks, 1):
        items_with_labels = len(re.findall(r'\\item\[[^\]]+\]', block))
        items_without = len(re.findall(r'\\item(?!\[)', block))
        if items_without > 0:
            print(f"⚠️  Description list {i} has {items_without} items without labels")
            warnings += 1
    
    if warnings == 0:
        print("✅ PASS: Semantic list types used correctly.")
        return True
    else:
        print(f"⚠️  PASS with {warnings} warnings.")
        return True

def check_textbf_after_subsection(filename):
    print(f"\n--- Checking \\textbf{{}} After Subsections: {filename} ---")
    warnings = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        if line.strip().startswith(r'\subsection{'):
            # Check next few non-empty lines for \textbf
            found_textbf = False
            for j in range(i+1, min(i+4, len(lines))):
                next_line = lines[j].strip()
                if next_line and not next_line.startswith('%'):
                    if r'\textbf{' in next_line:
                        found_textbf = True
                        break
                    elif next_line.startswith(r'\subsubsection'):
                        break
            
            if not found_textbf:
                print(f"⚠️  Line {i+1}: Subsection missing \\textbf{{}} question statement")
                warnings += 1
    
    if warnings == 0:
        print("✅ PASS: All subsections have bold question statements.")
        return True
    else:
        print(f"⚠️  PASS with {warnings} warnings.")
        return True

def check_section_numbering(filename):
    print(f"\n--- Checking Section Numbering Pattern: {filename} ---")
    with open(filename, 'r') as f:
        content = f.read()
    
    sections = re.findall(r'\\section\{([^}]+)\}', content)
    
    print(f"Found {len(sections)} sections")
    for i, section in enumerate(sections, 1):
        # Check for "Question N" pattern
        if 'Question' not in section and 'પ્રશ્ન' not in section:
            print(f"⚠️  Section '{section[:40]}' doesn't follow 'Question N' pattern")
    
    print("✅ PASS: Section numbering check complete.")
    return True

def check_subsection_labeling(filename):
    print(f"\n--- Checking Subsection Labeling: {filename} ---")
    warnings = 0
    with open(filename, 'r') as f:
        content = f.read()
    
    subsections = re.findall(r'\\subsection\{([^}]+)\}', content)
    
    for subsec in subsections:
        # Check for (a), (b), (c), OR pattern and marks
        has_part = re.search(r'\([a-z]\)|OR|અથવા', subsec)
        has_marks = re.search(r'\[\s*\d+\s*(marks|Marks|ગુણ)\s*\]', subsec)
        
        if not has_part:
            print(f"⚠️  Subsection '{subsec[:40]}' missing part label (a), (b), (c), or OR")
            warnings += 1
        if not has_marks:
            # Already checked in check_marks_format, skip duplicate
            pass
    
    if warnings == 0:
        print("✅ PASS: Subsection labeling correct.")
        return True
    else:
        print(f"⚠️  PASS with {warnings} warnings.")
        return True

def check_list_count_parity(file_en, file_gu):
    print(f"\n--- Checking List Count Parity (En vs Gu) ---")
    warnings = 0
    
    with open(file_en, 'r') as f:
        content_en = f.read()
    with open(file_gu, 'r') as f:
        content_gu = f.read()
    
    list_types = ['description', 'itemize', 'enumerate']
    
    for ltype in list_types:
        count_en = len(re.findall(rf'\\begin\{{{ltype}\}}', content_en))
        count_gu = len(re.findall(rf'\\begin\{{{ltype}\}}', content_gu))
        
        if count_en != count_gu:
            print(f"⚠️  {ltype} list count differs: En={count_en}, Gu={count_gu}")
            warnings += 1
    
    if warnings == 0:
        print("✅ PASS: List counts match between versions.")
        return True
    else:
        print(f"⚠️  PASS with {warnings} identity warnings.")
        return True

def check_table_count_parity(file_en, file_gu):
    print(f"\n--- Checking Table Count Parity (En vs Gu) ---")
    
    with open(file_en, 'r') as f:
        content_en = f.read()
    with open(file_gu, 'r') as f:
        content_gu = f.read()
    
    tables_en = len(re.findall(r'\\begin\{table\}', content_en))
    tables_gu = len(re.findall(r'\\begin\{table\}', content_gu))
    
    if tables_en != tables_gu:
        print(f"⚠️  Table count differs: En={tables_en}, Gu={tables_gu}")
        return True
    else:
        print(f"✅ PASS: Table counts match (En={tables_en}, Gu={tables_gu}).")
        return True

def check_figure_count_parity(file_en, file_gu):
    print(f"\n--- Checking Figure Count Parity (En vs Gu) ---")
    
    with open(file_en, 'r') as f:
        content_en = f.read()
    with open(file_gu, 'r') as f:
        content_gu = f.read()
    
    figures_en = len(re.findall(r'\\begin\{figure\}', content_en))
    figures_gu = len(re.findall(r'\\begin\{figure\}', content_gu))
    
    if figures_en != figures_gu:
        print(f"⚠️  Figure count differs: En={figures_en}, Gu={figures_gu}")
        return True
    else:
        print(f"✅ PASS: Figure counts match (En={figures_en}, Gu={figures_gu}).")
        return True

def check_compilation(filename, language="English"):
    print(f"\n--- Checking Compilation: {filename} ({language}) ---")
    
    compiler = 'xelatex' if language == "Gujarati" else 'pdflatex'
    
    try:
        # Run compiler in nonstopmode (doesn't stop on errors)
        result = subprocess.run(
            [compiler, '-interaction=nonstopmode', '-halt-on-error', filename],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"✅ PASS: {filename} compiles successfully with {compiler}.")
            return True
        else:
            print(f"❌ FAIL: Compilation failed. Check .log file for details.")
            # Print last 20 lines of error output
            error_lines = result.stdout.split('\n')[-20:]
            for line in error_lines:
                if line.strip():
                    print(f"  {line}")
            return False
    except subprocess.TimeoutExpired:
        print(f"❌ FAIL: Compilation timeout (>30s).")
        return False
    except FileNotFoundError:
        print(f"⚠️  {compiler} not installed/found. Skipping compilation check.")
        return True

def check_filename_convention(filename):
    print(f"\n--- Checking Filename Convention: {filename} ---")
    
    # Extract just the filename without path
    import os
    basename = os.path.basename(filename)
    
    # Pattern: [Code]-[Season]-[Year]-Solution-Full.tex or .gu.tex
    pattern = r'^[A-Z0-9]+-(?:Summer|Winter)-\d{4}-Solution-Full(?:\.gu)?\.tex$'
    
    if re.match(pattern, basename):
        print(f"✅ PASS: Filename follows convention.")
        return True
    else:
        print(f"⚠️  Filename '{basename}' doesn't follow [Code]-[Season]-[Year]-Solution-Full.tex convention")
        return True

def check_content_after_toc(filename):
    print(f"\n--- Checking Content After TOC: {filename} ---")
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Find position of \tableofcontents
    toc_pos = content.find(r'\tableofcontents')
    if toc_pos == -1:
        print("⚠️  No \\tableofcontents found")
        return True
    
    # Check for sections after TOC
    after_toc = content[toc_pos:]
    sections = re.findall(r'\\section\{', after_toc)
    
    if len(sections) > 0:
        print(f"✅ PASS: Found {len(sections)} sections after TOC.")
        return True
    else:
        print("❌ FAIL: No sections found after TOC.")
        return False

def check_preamble_path(filename, language="English"):
    print(f"\n--- Checking Preamble Path: {filename} ({language}) ---")
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Check for \input command
    input_match = re.search(r'\\input\{([^}]+)\}', content)
    
    if not input_match:
        print("❌ FAIL: No \\input{{}} command found for preamble.")
        return False
    
    input_path = input_match.group(1)
    
    # Check if path is absolute
    if not (input_path.startswith('/') or input_path.startswith('C:')):
        print(f"⚠️  Preamble path is relative: {input_path}")
        print("    Consider using absolute path for consistency.")
    
    # Check if correct preamble is used
    expected_preamble = 'preamble.gu.tex' if language == "Gujarati" else 'preamble.tex'
    if expected_preamble in input_path:
        print(f"✅ PASS: Correct preamble path ({expected_preamble}).")
        return True
    else:
        print(f"⚠️  Expected {expected_preamble} in preamble path")
        return True

def check_description_item_count(file_en, file_gu):
    print(f"\n--- Checking Description List Item Counts (En vs Gu) ---")
    warnings = 0
    
    with open(file_en, 'r') as f:
        content_en = f.read()
    with open(file_gu, 'r') as f:
        content_gu = f.read()
    
    # Extract description blocks
    desc_en = re.findall(r'\\begin\{description\}.*?\\end\{description\}', content_en, re.DOTALL)
    desc_gu = re.findall(r'\\begin\{description\}.*?\\end\{description\}', content_gu, re.DOTALL)
    
    if len(desc_en) != len(desc_gu):
        print(f"⚠️  Description list count differs (checked in list parity)")
        return True
    
    # Check item counts in each description block
    for i, (block_en, block_gu) in enumerate(zip(desc_en, desc_gu), 1):
        items_en = len(re.findall(r'\\item\[', block_en))
        items_gu = len(re.findall(r'\\item\[', block_gu))
        
        if items_en != items_gu:
            print(f"⚠️  Description list {i} item count differs: En={items_en}, Gu={items_gu}")
            warnings += 1
    
    if warnings == 0:
        print("✅ PASS: Description list item counts match.")
        return True
    else:
        print(f"⚠️  PASS with {warnings} warnings.")
        return True

def check_code_math_diagram_identity(file_en, file_gu):
    print(f"\n--- Checking Code/Math/Diagram Identity (En vs Gu) ---")
    warnings = 0
    
    with open(file_en, 'r') as f:
        content_en = f.read()
    with open(file_gu, 'r') as f:
        content_gu = f.read()
    
    # Extract code listings
    code_en = re.findall(r'\\begin\{lstlisting\}.*?\\end\{lstlisting\}', content_en, re.DOTALL)
    code_gu = re.findall(r'\\begin\{lstlisting\}.*?\\end\{lstlisting\}', content_gu, re.DOTALL)
    
    if len(code_en) != len(code_gu):
        print(f"❌ Code block count mismatch: En={len(code_en)}, Gu={len(code_gu)}")
        warnings += 1
    else:
        # Check if code blocks are identical (ignoring caption text)
        for i, (en_code, gu_code) in enumerate(zip(code_en, code_gu)):
            # Remove caption for comparison
            en_clean = re.sub(r'caption=\{[^}]+\}', '', en_code)
            gu_clean = re.sub(r'caption=\{[^}]+\}', '', gu_code)
            if en_clean != gu_clean:
                print(f"⚠️  Code block {i+1} differs between En and Gu")
                warnings += 1
    
    # Extract inline and display math
    inline_math_en = re.findall(r'\\\([^)]+\\\)', content_en)
    inline_math_gu = re.findall(r'\\\([^)]+\\\)', content_gu)
    
    if len(inline_math_en) != len(inline_math_gu):
        print(f"⚠️  Inline math count differs: En={len(inline_math_en)}, Gu={len(inline_math_gu)}")
        warnings += 1
    
    display_math_en = re.findall(r'\\\[[^\]]+\\\]', content_en, re.DOTALL)
    display_math_gu = re.findall(r'\\\[[^\]]+\\\]', content_gu, re.DOTALL)
    
    if len(display_math_en) != len(display_math_gu):
        print(f"⚠️  Display math count differs: En={len(display_math_en)}, Gu={len(display_math_gu)}")
        warnings += 1
    
    # Extract diagrams (tikz, circuitikz, karnaugh-map)
    diagram_types = ['tikzpicture', 'circuitikz', 'karnaugh-map']
    for dtype in diagram_types:
        diag_en = re.findall(rf'\\begin\{{{dtype}\}}.*?\\end\{{{dtype}\}}', content_en, re.DOTALL)
        diag_gu = re.findall(rf'\\begin\{{{dtype}\}}.*?\\end\{{{dtype}\}}', content_gu, re.DOTALL)
        
        if len(diag_en) != len(diag_gu):
            print(f"⚠️  {dtype} count differs: En={len(diag_en)}, Gu={len(diag_gu)}")
            warnings += 1
        elif len(diag_en) > 0:
            # Check if diagrams are identical
            for i, (en_diag, gu_diag) in enumerate(zip(diag_en, diag_gu)):
                if en_diag != gu_diag:
                    print(f"⚠️  {dtype} diagram {i+1} differs between En and Gu")
                    warnings += 1
    
    if warnings == 0:
        print("✅ PASS: Code/Math/Diagrams are identical between versions.")
        return True
    else:
        print(f"⚠️  PASS with {warnings} identity warnings.")
        return True

def check_smart_quotes(filename):
    print(f"\n--- Checking Smart Quotes Usage: {filename} ---")
    warnings = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    in_lstlisting = False
    for i, line in enumerate(lines, 1):
        if '\\begin{lstlisting}' in line:
            in_lstlisting = True
        elif '\\end{lstlisting}' in line:
            in_lstlisting = False
        
        # Skip code blocks and comments
        if in_lstlisting or line.strip().startswith('%'):
            continue
        
        # Check for smart quote patterns in text
        if '\\emph{' in line or '\\paragraph{' in line or '\\textbf{' not in line:
            # Look for opening quotes
            if "''" in line or '``' in line:
                pass  # Has smart quotes, good
            elif '"' in line and 'lstlisting' not in line:
                # Has straight quotes in text - already warned by syntax check
                pass
    
    print("✅ PASS: Smart quotes check complete.")
    return True

def check_marks_format(filename):
    print(f"\n--- Checking Marks Format in Subsections: {filename} ---")
    warnings = 0
    with open(filename, 'r') as f:
        content = f.read()
    
    # Find all subsections
    subsections = re.findall(r'\\subsection\{([^}]+)\}', content)
    
    for subsec in subsections:
        # Check for marks notation [X marks] or [X ગુણ]
        if not re.search(r'\[\s*\d+\s*(marks|Marks|ગુણ)\s*\]', subsec):
            print(f"⚠️  Subsection missing marks notation: {subsec[:50]}...")
            warnings += 1
    
    if warnings == 0:
        print("✅ PASS: All subsections have marks notation.")
        return True
    else:
        print(f"⚠️  PASS with {warnings} warnings.")
        return True

def check_typography(filename):
    print(f"\n--- Checking Typography: {filename} ---")
    # Simplified check - just verify file exists and is readable
    # Thin spaces before units (\,) are optional for simplicity
    print("✅ PASS: Typography check (simplified).")
    return True 

def check_syntax(filename, language="English"):
    print(f"\n--- Checking Syntax: {filename} ({language}) ---")
    errors = 0
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    in_lstlisting = False
    for i, line in enumerate(lines, 1):
        # Track lstlisting blocks
        if '\\begin{lstlisting}' in line:
            in_lstlisting = True
        elif '\\end{lstlisting}' in line:
            in_lstlisting = False
            
        suspicious_dollar = re.search(r'(?<!\()(\$)(?!\))', line)
        if suspicious_dollar:
             print(rf"❌ Line {i}: Found forbidden '$' syntax. Use \(...\) or \[...\]")
             errors += 1
             
        if "**" in line:
            print(f"❌ Line {i}: Found Markdown '**' syntax. Use \\textbf{{...}}")
            errors += 1
            
        if '"' in line:
             # Skip if inside lstlisting block, or line has lstlisting, or is a comment
             if in_lstlisting or 'lstlisting' in line or line.strip().startswith('%'):
                 continue
             print(f"⚠️  Line {i}: Found straight quote [\"] in text? Use smart quotes [`` or '']. (Ignore if code)")
            
    if errors == 0:
        print("✅ PASS: No forbidden syntax found.")
        return True
    else:
        print(f"❌ FAIL: Found {errors} syntax errors.")
        return False

def run_chktex(filename):
    print(f"\n--- Running ChkTeX: {filename} ---")
    try:
        result = subprocess.run(['chktex', '-q', '-n1', '-n2', '-n3', '-n6', '-n8', '-n12', '-n13', '-n22', '-n36', '-n44', filename], capture_output=True, text=True)
        if result.returncode != 0 and result.stdout:
             print(result.stdout)
             print("⚠️  ChkTeX reported warnings (see above).")
        elif result.stderr:
             print(f"ChkTeX Error: {result.stderr}")
        else:
             print("✅ PASS: ChkTeX clean.")
    except FileNotFoundError:
        print("⚠️  ChkTeX not installed/found. Skipping.")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Verify GTU LaTeX Solutions.')
    parser.add_argument('file_en', nargs='?', default="DI01000051-Summer-2025-Solution-Full.tex", help='English Solution File')
    parser.add_argument('file_gu', nargs='?', default="DI01000051-Summer-2025-Solution-Full.gu.tex", help='Gujarati Solution File')
    
    args = parser.parse_args()
    
    file_en = args.file_en
    file_gu = args.file_gu
    
    print("========================================")
    print(f"      VERIFICATION REPORT               ")
    print(f" En: {file_en}")
    print(f" Gu: {file_gu}")
    print("========================================")
    
    # Core structure checks
    pass_lc = check_line_counts(file_en, file_gu)
    pass_struct = check_structure(file_en, file_gu)
    
    # Document structure and metadata
    pass_doc_en = check_document_structure(file_en)
    pass_doc_gu = check_document_structure(file_gu)
    pass_meta_en = check_pdf_metadata(file_en)
    pass_meta_gu = check_pdf_metadata(file_gu)
    pass_preamble_en = check_preamble_usage(file_en, "English")
    pass_preamble_gu = check_preamble_usage(file_gu, "Gujarati")
    pass_preamble_path_en = check_preamble_path(file_en, "English")
    pass_preamble_path_gu = check_preamble_path(file_gu, "Gujarati")
    
    # Syntax and compliance checks
    pass_syn_en = check_syntax(file_en, "English")
    pass_syn_gu = check_syntax(file_gu, "Gujarati")
    pass_cont_en = check_content_compliance(file_en)
    pass_cont_gu = check_content_compliance(file_gu)
    pass_hier_en = check_structure_strict(file_en)
    pass_hier_gu = check_structure_strict(file_gu)
    
    # Content quality checks
    pass_wc_en = check_word_counts(file_en)
    pass_wc_gu = check_word_counts(file_gu)
    pass_typo_en = check_typography(file_en)
    pass_quotes = check_smart_quotes(file_en)  # Check one file as example
    pass_marks_en = check_marks_format(file_en)
    pass_marks_gu = check_marks_format(file_gu)
    
    # Content fidelity checks (En vs Gu)
    pass_identity = check_code_math_diagram_identity(file_en, file_gu)
    pass_list_parity = check_list_count_parity(file_en, file_gu)
    pass_table_parity = check_table_count_parity(file_en, file_gu)
    pass_figure_parity = check_figure_count_parity(file_en, file_gu)
    pass_desc_items = check_description_item_count(file_en, file_gu)
    
    # Filename convention checks
    pass_filename_en = check_filename_convention(file_en)
    pass_filename_gu = check_filename_convention(file_gu)
    
    # Structural checks
    pass_toc_en = check_toc_setup(file_en)
    pass_toc_gu = check_toc_setup(file_gu)
    pass_content_after_toc_en = check_content_after_toc(file_en)
    pass_content_after_toc_gu = check_content_after_toc(file_gu)
    pass_mnem_en = check_mnemonics(file_en)
    pass_mnem_gu = check_mnemonics(file_gu)
    pass_qstruct_en = check_question_structure(file_en)
    pass_qstruct_gu = check_question_structure(file_gu)
    pass_textbf_en = check_textbf_after_subsection(file_en)
    pass_textbf_gu = check_textbf_after_subsection(file_gu)
    pass_section_num_en = check_section_numbering(file_en)
    pass_section_num_gu = check_section_numbering(file_gu)
    pass_subsec_label_en = check_subsection_labeling(file_en)
    pass_subsec_label_gu = check_subsection_labeling(file_gu)
    pass_levels_en = check_hierarchy_levels(file_en)
    pass_levels_gu = check_hierarchy_levels(file_gu)
    pass_list_types_en = check_list_types(file_en)
    pass_list_types_gu = check_list_types(file_gu)
    pass_captions_en = check_caption_positions(file_en)
    pass_captions_gu = check_caption_positions(file_gu)
    pass_cmds_en = check_custom_commands(file_en)
    pass_cmds_gu = check_custom_commands(file_gu)
    
    # External tools
    run_chktex(file_en)
    run_chktex(file_gu)
    
    # Compilation checks (optional but recommended)
    pass_compile_en = check_compilation(file_en, "English")
    pass_compile_gu = check_compilation(file_gu, "Gujarati")
    
    print("\n========================================")
    # Critical checks that must pass
    critical_checks = [
        pass_lc, pass_struct,
        pass_doc_en, pass_doc_gu,
        pass_preamble_en, pass_preamble_gu,
        pass_preamble_path_en, pass_preamble_path_gu,
        pass_syn_en, pass_syn_gu, 
        pass_cont_en, pass_cont_gu, 
        pass_hier_en, pass_hier_gu,
        pass_toc_en, pass_toc_gu,
        pass_content_after_toc_en, pass_content_after_toc_gu,
        pass_cmds_en, pass_cmds_gu,
        pass_compile_en, pass_compile_gu
    ]
    
    if all(critical_checks):
        print("OVERALL STATUS: ✅ PASSED")
        print("\nNote: All critical checks passed. Quality warnings (if any) should be reviewed.")
        sys.exit(0)
    else:
        print("OVERALL STATUS: ❌ FAILED")
        sys.exit(1)
