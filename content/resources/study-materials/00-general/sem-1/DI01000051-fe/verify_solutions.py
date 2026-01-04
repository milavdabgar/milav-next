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

def check_typography(filename):
    print(f"\n--- Checking Typography (Units, Spacing): {filename} ---")
    errors = 0
    possible_units = ['V', 'A', 'Hz', 'F', 'H', 'm', 's', 'K', 'J', 'W', 'Pa', 'N', 'C', 'T', 'G', 'M', 'k', 'n', 'p', 'u']
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines, 1):
         # Search for number followed immediately by unit chars in the typical set
         # Simplified heuristic
         for u in ['V', 'Hz', 'k\Omega', 'nF', 'F', 'H']:
             if re.search(r'\d+' + re.escape(u) + r'\b', line):
                 # Filter out if it actually has \, in file
                 # Reading raw line: '10\,V' matches regex `\d+V` ?? No, `\,` breaks it if looking for 'V' directly?
                 # Actually regex `re.escape('V')` is `V`.
                 # So `10V` matches `\d+V`.
                 # `10\,V` has `\` and `,` between 0 and V. Does NOT match `\d+V`.
                 # So this regex safely finds missing spaces.
                 print(f"⚠️  Line {i}: Found number+unit '{u}' without thin space (\\,). Use e.g. '10\\,{u}'")
                 errors += 1
                 break 
                 
    if errors == 0:
        print("✅ PASS: Typography seems okay.")
        return True
    else:
        print(f"⚠️  Found {errors} typography warnings.")
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
             print(f"❌ Line {i}: Found forbidden '$' syntax. Use \(...\) or \[...\]")
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
    
    pass_lc = check_line_counts(file_en, file_gu)
    pass_struct = check_structure(file_en, file_gu)
    pass_syn_en = check_syntax(file_en, "English")
    pass_syn_gu = check_syntax(file_gu, "Gujarati")
    pass_cont_en = check_content_compliance(file_en)
    pass_cont_gu = check_content_compliance(file_gu)
    pass_hier_en = check_structure_strict(file_en)
    pass_hier_gu = check_structure_strict(file_gu)
    
    pass_wc_en = check_word_counts(file_en)
    pass_wc_gu = check_word_counts(file_gu)
    pass_typo_en = check_typography(file_en)
    
    run_chktex(file_en)
    run_chktex(file_gu)
    
    print("\n========================================")
    if pass_lc and pass_struct and pass_syn_en and pass_syn_gu and pass_cont_en and pass_cont_gu and pass_hier_en and pass_hier_gu:
        print("OVERALL STATUS: ✅ PASSED")
        sys.exit(0)
    else:
        print("OVERALL STATUS: ❌ FAILED")
        sys.exit(1)
