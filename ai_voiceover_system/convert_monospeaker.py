import re
import sys
from pathlib import Path

def convert_to_monospeaker(file_path):
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File not found: {file_path}")
        return False

    content = path.read_text(encoding='utf-8')
    
    # Regex to match "Name: " prefix, optionally preceded by "[click] " and whitespace
    # Captures the prefix (indentation + [click]) in group 1 to preserve it
    pattern = r'([ \t]*(?:\[click\][ \t]*)?)(?:Dr\. James|Sarah):\s+'
    
    new_content = re.sub(pattern, r'\1', content)
    
    path.write_text(new_content, encoding='utf-8')
    print(f"Successfully converted {file_path}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_monospeaker.py <file_path>")
        sys.exit(1)
        
    convert_to_monospeaker(sys.argv[1])
