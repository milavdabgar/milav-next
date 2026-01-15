import os

ROOT_DIR = "content/resources/study-materials"

def find_solution_files():
    """Find all .tex and .gu.tex files in 'GTU Solutions Short' directories."""
    solution_files = []
    
    for root, dirs, files in os.walk(ROOT_DIR):
        if os.path.basename(root) == "GTU Solutions Short":
            for file in files:
                if (file.endswith(".tex") or file.endswith(".gu.tex")) and \
                   not file.startswith("preamble") and \
                   not file.startswith("commands") and \
                   not file.endswith("boxes.tex"):
                    solution_files.append(os.path.join(root, file))
    return solution_files

def main():
    files = find_solution_files()
    print(f"Total Solution Files Found: {len(files)}")
    
    success_pdf = 0
    missing_pdf = 0
    
    missing_files = []
    
    for f in files:
        if f.endswith(".tex"):
            pdf = f[:-4] + ".pdf"
        
        if os.path.exists(pdf):
            success_pdf += 1
        else:
            missing_pdf += 1
            missing_files.append(f)
            
    print(f"PDFs Generated: {success_pdf}")
    print(f"Missing PDFs:   {missing_pdf}")
    
    if missing_files:
        print("\nBroken Files (No PDF):")
        for mf in missing_files:
            print(f"- {os.path.basename(mf)}")

if __name__ == "__main__":
    main()
