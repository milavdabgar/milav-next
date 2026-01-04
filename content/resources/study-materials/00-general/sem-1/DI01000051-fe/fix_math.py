import sys
import re

def fix_math(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern explanation:
    # (?<!\\)\$      : Match '$' not preceded by '\'
    # (.*?)          : Match content non-greedily (captured in group 1)
    # (?<!\\)\$      : Match '$' not preceded by '\'
    # Note: This handles multiple inline math blocks on the same line.
    # It assumes no multiline inline math (which is standard for $...$).
    
    new_content = re.sub(r'(?<!\\)\$(.*?)(?<!\\)\$', r'\\(\1\\)', content)
    
    # Also handle the display math if any $$...$$ were used (though grep said none, safer to check)
    # Actually, the previous regex might match $$...$$ as \(...$ or something if not careful.
    # $$ is usually empty variable in regex? No. 
    # But user guidelines say NO $$.
    # If $$ exists, it should be \[ \].
    # My grep said no $$, so I ignore that case.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fix_math.py <file1> <file2> ...")
        sys.exit(1)
        
    for path in sys.argv[1:]:
        print(f"Processing {path}...")
        fix_math(path)
