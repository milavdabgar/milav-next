import os
import glob

TARGET_DIR = "/Users/milav/Code/milav-next/content/resources/study-materials/11-ec/sem-2/4321103-eca/GTU Solutions Short"
REL_PATH = "figures/tex-diagrams/pdf/"
ABS_PATH = os.path.join(TARGET_DIR, REL_PATH)

def scan_and_fix():
    # Only main solution files, not the extracted diagrams
    # Pattern: *-solution.tex or *-solution.gu.tex
    files = glob.glob(os.path.join(TARGET_DIR, "*-solution*.tex"))
    
    print(f"Checking {len(files)} files...")
    
    for file_path in files:
        # Skip if it's in the figures directory (glob shouldn't find them there since we didn't use recursive, but good to be safe)
        if "figures/" in file_path:
            continue
            
        print(f"Processing {os.path.basename(file_path)}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        print(f"Processing {os.path.basename(file_path)}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # FORCE RELATIVE PATHS
        if ABS_PATH in content:
            new_content = content.replace(ABS_PATH, REL_PATH)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("  Fixed paths: Reverted to relative.")
        elif REL_PATH in content and ABS_PATH not in content:
            print("  Already has relative paths.")
        else:
            print("  No diagram paths found.")

if __name__ == "__main__":
    scan_and_fix()
