
import os
import re
import glob

# Constants
SEARCH_ROOT = "/Users/milav/Code/milav-next/content/resources/study-materials"
TARGET_DIR_NAME = "GTU Solutions Short"
FIGURES_REL_PATH = "figures/tex-diagrams/tex"

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def generate_tags(question_context, caption_text, subject_code):
    tags = [subject_code]
    
    ignore_words = {
        'explain', 'describe', 'briefly', 'calculate', 'write', 'short', 'note', 'diagram', 'circuit', 'figure', 'draw', 'what', 'with', 'necessary', 'neat', 'sketch', 'define', 'give', 
        'the', 'and', 'for', 'are', 'is', 'that', 'this', 'to', 'of', 'in', 'on', 'at', 'by', 'from', 'an', 'a', 'or', 'be', 'as', 'it', 'its',
        'સમજાવો', 'વિગતવાર', 'લખો', 'વર્ણવો', 'આપો', 'કરો', 'અને', 'ની', 'ના', 'માં', 'માટે', 'ટૂંકનોંધ', 'તફાવત', 'વ્યાખ્યા', 'ઉદાહરણ', 'આકૃતિ', 'દોરો', 'સાથે', 'જણાવો'
    }
    
    def extract_words(text):
        if not text: return []
        # Remove common punctuation first to avoid "word."
        for char in ".,;:!?()[]{}":
            text = text.replace(char, " ")
        words = text.split()
        # Clean words
        clean = []
        for w in words:
            w_clean = w.strip().lower()
            if w_clean.startswith('\\'): # Ignore LaTeX commands
                continue
            if len(w_clean) >= 3:
                clean.append(w_clean)
        return clean

    keywords = extract_words(question_context)
    
    filtered_keywords = [w for w in keywords if w not in ignore_words]
    # Deduplicate and limit
    filtered_keywords = list(set(filtered_keywords))[:5]
    tags.extend(filtered_keywords)
    
    if caption_text:
        caption_keywords = extract_words(caption_text)
        tags.extend([w for w in caption_keywords if w not in ignore_words and w not in tags])
        
    return ", ".join(tags)

def extract_diagrams_from_file(file_path):
    print(f"Processing: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(file_path)
    basename = os.path.splitext(filename)[0] # e.g., 4321103-summer-2023-solution
    
    # Extract subject code from filename (assuming format: CODE-TERM-YEAR-...)
    parts = basename.split('-')
    subject_code = parts[0] if parts else "unknown"

    # Directory for extracted diagrams
    parent_dir = os.path.dirname(file_path)
    figures_dir = os.path.join(parent_dir, FIGURES_REL_PATH)
    ensure_directory(figures_dir)

    # Patterns
    # Find question context: \questionmarks{Q}{Sub}{Marks} followed by bold text usually
    # We will iterate line by line or split by questions to maintain context?
    # Actually, simplistic regex replacement might be risky if nested. 
    # But tikzpictures are usually top-level in the solutionbox.
    
    # Let's iterate and identify sections.
    
    lines = content.split('\n')
    new_lines = []
    
    current_q = "unknown"
    current_sub = ""
    
    # Regexes
    q_pattern = re.compile(r'\\questionmarks\{(\w+)\}\{(\w+)\}\{.*?\}')
    # Use flags for multiline matching if needed, but we go line by line for context tracking
    # However, diagrams span multiple lines.
    
    # Better approach: State machine loop
    i = 0
    diagram_count = 0
    
    # Buffer for checking next question context
    # We'll just regex search all start indices of tikzpicture/circuitikz
    # But we need context.
    
    # Let's do a pass to map line numbers to Question numbers
    line_contexts = {}
    last_context = ("unknown", "unknown", "") # Q, Sub, Text
    
    q_re = re.compile(r'\\questionmarks\{(\w+)\}\{(\w+)\}')
    # Text usually follows immediately.
    
    for idx, line in enumerate(lines):
        m = q_re.search(line)
        if m:
            last_context = (m.group(1), m.group(2), "")
            # Try to grab the question text in the next few lines
            # Limit lookahead
            q_text = ""
            for offset in range(1, 5):
                if idx + offset < len(lines):
                    next_l = lines[idx+offset].strip()
                    if next_l.startswith(r'\textbf{'):
                        q_text = next_l.replace(r'\textbf{', '').replace('}', '')
                        break
            last_context = (last_context[0], last_context[1], q_text)
            
        line_contexts[idx] = last_context

    # Now find diagrams and replace
    result_content = ""
    i = 0
    
    # pattern for environment start
    env_start = re.compile(r'\\begin\{(tikzpicture|circuitikz)\}')
    env_end = re.compile(r'\\end\{(tikzpicture|circuitikz)\}')
    
    while i < len(lines):
        line = lines[i]
        m_start = env_start.search(line)
        
        if m_start:
            # Found start of diagram
            env_type = m_start.group(1)
            start_line_idx = i
            
            # Find end
            diagram_lines = []
            nesting = 0
            found_end = False
            
            # Capture content including current line from the match position?
            # Tikz usually starts on own line or inside center.
            # We assume standard formatting: \begin{...} on its own line usually
            
            # Simple line-based extraction (assuming \begin and \end are on valid separate lines or easy to handle)
            # If \begin is inline, this might break. Assuming standard formatting as per guidelines.
            
            # Check if \end is on the same line
            if env_end.search(line) and line.count(f'\\begin{{{env_type}}}') == line.count(f'\\end{{{env_type}}}'):
                 # One liner or fully contained
                 diagram_lines.append(line)
                 i += 1
                 # Process this diagram
                 extract = True
            else:
                 # Multiline
                 for j in range(i, len(lines)):
                     l = lines[j]
                     # Count opens and closes to handle nesting if any (unlikely for tikz usually, but good practice)
                     nesting += l.count(f'\\begin{{{env_type}}}')
                     nesting -= l.count(f'\\end{{{env_type}}}')
                     diagram_lines.append(l)
                     if nesting == 0:
                         i = j + 1
                         found_end = True
                         break
            
            if not found_end and len(diagram_lines) > 1:
                # Fallback if EOF reached without closure
                print(f"Warning: Unclosed {env_type} at line {start_line_idx}")
                new_lines.append(line) # Don't extract
                i += 1
                continue
                
            # Process extraction
            ctx_q, ctx_sub, ctx_text = line_contexts.get(start_line_idx, ("unknown", "unknown", ""))
            
            # Unique ID
            suffix_char = ctx_sub if ctx_sub else "x"
            # handle sub being number or char
            
            # Check if multiple diagrams in same Q
            # Using a global counter for the file or per Q?
            # Let's use QNumber-Sub-Index
            
            diag_index = 1
            # Check collision with existing keys or simple sequence
            # We assume linear processing
            
            # Construct filename
            # 4321103-summer-2023-solution-q1a.tex
            # If multiple, q1a-1.tex
            
            # We need to detect if we already used this q code
            # Simple way: just append an index if we see it again? 
            # Or always append index if > 1?
            # User example: q1a.tex. So if only one, no index.
            
            # Since we are processing sequentially, we need to track counts per Q-Sub
            # Implementation detail: Use a tracker dict
            
            token = f"q{ctx_q}{ctx_sub}"
            if not hasattr(extract_diagrams_from_file, "q_counters"):
                extract_diagrams_from_file.q_counters = {}
            
            # Reset counters for each file
            # Oh, function is called per file.
            pass

        else:
            new_lines.append(line)
            i += 1
            
    # Wait, the while loop approach is better but I need to integrate correctly.
    # Let's rewrite the loop structure properly.

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    filename = os.path.basename(file_path)
    basename = os.path.splitext(filename)[0].replace('.gu', '') # Handle .gu.tex
    is_gujarati = '.gu.tex' in file_path
    
    parts = basename.split('-')
    subject_code = parts[0] if parts else "unknown"
    
    parent_dir = os.path.dirname(file_path)
    figures_dir = os.path.join(parent_dir, FIGURES_REL_PATH)
    rel_path_to_figures = FIGURES_REL_PATH # Relative for input
    
    # Adjust relative path for input command
    # File is at .../GTU Solutions Short/X.tex
    # Figures at .../GTU Solutions Short/figures/tex-diagrams/tex/
    # So Input should be {figures/tex-diagrams/tex/filename}
    
    ensure_directory(figures_dir)
    
    # Context extraction
    q_counters = {} # Key: "q1a", Value: count
    
    new_lines = []
    i = 0
    
    # Context trackers
    current_q = "0"
    current_sub = "0"
    current_text = ""
    current_subheading = ""
    
    q_re = re.compile(r'\\questionmarks\{(\w+)\}\{(\w+)\}')
    # Alternative format: \questionmarks{1(a)}{3}{text} or \questionmarks{2 [OR] (a)}{3}{...}
    q_re_alt = re.compile(r'\\questionmarks\{([^}]+)\}\{(\d+)\}\{')
    env_start = re.compile(r'\\begin\{(tikzpicture|circuitikz)\}')
    env_end = re.compile(r'\\end\{(tikzpicture|circuitikz)\}')
    solutionbox_start = re.compile(r'\\begin\{solutionbox\}')
    
    while i < len(lines):
        line = lines[i]
        
        # Update context - try both formats
        m_q = q_re.search(line)
        m_q_alt = q_re_alt.search(line)
        if m_q:
            current_q = m_q.group(1)
            current_sub = m_q.group(2)
            # Try to find text in next lines
            current_text = ""
            for offset in range(1, 10): # Search a bit further
                if i + offset < len(lines):
                    next_l = lines[i+offset].strip()
                    if next_l.startswith(r'\textbf{'):
                        current_text = next_l.replace(r'\textbf{', '').replace('}', '')
                        break
            # Reset subheading when new question starts
            current_subheading = ""
        elif m_q_alt:
            # Parse format like "1(a)" or "2 [OR] (a)" or "2(c)(I)"
            q_str = m_q_alt.group(1).strip()
            # Extract question number and sub-part
            # Pattern: digit(s) possibly followed by (letter/roman) or [OR] (letter)
            q_parts = re.match(r'(\d+)\s*(?:\[OR\]\s*)?\(([^)]+)\)(?:\(([^)]+)\))?', q_str)
            if q_parts:
                current_q = q_parts.group(1)
                current_sub = q_parts.group(2)
                if q_parts.group(3):  # e.g., 2(c)(I)
                    current_sub += q_parts.group(3)
            else:
                # Fallback: use full string cleaned
                current_q = re.sub(r'[^\w]', '', q_str)
                current_sub = ""
            current_text = ""
            current_subheading = ""
        
        if solutionbox_start.search(line):
            # Reset subheading at start of solutionbox? 
            # Usually subheading is inside.
            pass
            
        # Track bold text as subheading (heuristic)
        if line.strip().startswith(r'\textbf{') and not m_q:
             # Cleanup
             clean_sub = line.strip().replace(r'\textbf{', '').replace('}', '').replace(':', '')
             # Ignore if it looks like a question prompt (already captured in current_text)
             if clean_sub != current_text:
                 current_subheading = clean_sub

        # Check for diagram
        m_start = env_start.search(line)
        if m_start:
            env_type = m_start.group(1)
            
            # Extract block
            diagram_code = []
            nesting = 0
            found_end = False
            
            j = i
            while j < len(lines):
                l = lines[j]
                current_nesting = l.count(f'\\begin{{{env_type}}}') - l.count(f'\\end{{{env_type}}}')
                nesting += current_nesting
                diagram_code.append(l)
                
                if nesting == 0:
                    found_end = True
                    i = j + 1
                    break
                j += 1
            
            if not found_end:
                 # Failed to find end, keep original
                 new_lines.append(line)
                 i += 1
                 continue
                 
            # Logic for naming
            q_key = f"q{current_q}{current_sub}"
            q_counters[q_key] = q_counters.get(q_key, 0) + 1
            
            layout_suffix = ""
            if q_counters[q_key] > 1:
                layout_suffix = f"-{q_counters[q_key]}"
            
            # Check for Gujarati suffix
            lang_suffix = ".gu" if is_gujarati else ""
            
            # basname is like "4321103-summer-2023-solution"
            # We want "4321103-summer-2023-solution-q1a.tex"
            # Currently logic was: f"{basename}-solution-{q_key}..." -> duplicates solution
            
            diag_filename = f"{basename}-{q_key}{layout_suffix}{lang_suffix}.tex"
            full_diag_path = os.path.join(figures_dir, diag_filename)
            
            # Generate Logic for Tags
            # Pass combined text of Question + Subheading
            context_text = f"{current_text} {current_subheading}"
            tags = generate_tags(context_text, "", subject_code)
            
            # Write diagram file (for reusable library)
            header = f"% Tags: {tags}\n"
            with open(full_diag_path, 'w', encoding='utf-8') as f_diag:
                f_diag.write(header + "".join(diagram_code))
            
            print(f"  Extracted: {diag_filename}")
            
            # KEEP original inline TikZ code - don't replace with includefigure
            # This preserves working solutions while building diagram library
            new_lines.extend(diagram_code)
            
        else:
            new_lines.append(line)
            i += 1
            
    # DON'T modify the main file - keep original inline TikZ code
    # The extracted diagrams serve as a reusable library that can be
    # improved independently and integrated later if needed
        
def main():
    # Find all "GTU Solutions Short" directories
    print("Searching for solution directories...")
    # Use glob for recursive search?
    # root/**/GTU Solutions Short
    
    # User requested to NOT process all folders at once.
    # Let's target a specific one for testing as per request.
    # Target: content/resources/study-materials/11-ec/sem-2/4321103-eca/GTU Solutions Short
    
    target_path = "/Users/milav/Code/milav-next/content/resources/study-materials/11-ec/sem-2/4321102-de/GTU Solutions Short"
    
    if os.path.exists(target_path):
        targets = [target_path]
    else:
        print(f"Target path not found: {target_path}")
        return

    # targets = []
    # for root, dirs, files in os.walk(SEARCH_ROOT):
    #     if TARGET_DIR_NAME in dirs:
    #         targets.append(os.path.join(root, TARGET_DIR_NAME))
            
    print(f"Found {len(targets)} target directories.")
    
    for target in targets:
        print(f"Processing directory: {target}")
        # Find all .tex files (exclude exclusions)
        tex_files = glob.glob(os.path.join(target, "*.tex"))
        for tf in tex_files:
            if "preamble" in tf or "commands" in tf or "english-boxes" in tf:
                continue
            if not "solution" in tf: # Safety filter
                continue
                
            process_file(tf)

if __name__ == "__main__":
    main()
