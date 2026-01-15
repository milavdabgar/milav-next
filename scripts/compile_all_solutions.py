
import os
import glob
import subprocess

TARGET_DIR = "/Users/milav/Code/milav-next/content/resources/study-materials/11-ec/sem-2/4321103-eca/GTU Solutions Short"

def compile_all_solutions():
    # Find all solution .tex files
    tex_files = glob.glob(os.path.join(TARGET_DIR, "*-solution.tex")) + \
                glob.glob(os.path.join(TARGET_DIR, "*-solution.gu.tex"))
    
    print(f"Found {len(tex_files)} solution files to compile.")
    
    success_count = 0
    failed_files = []

    for tex_file in tex_files:
        filename = os.path.basename(tex_file)
        print(f"\nCompiling {filename}...")
        
        # Run xelatex from the TARGET_DIR so relative paths work
        # Output directly to TARGET_DIR (no separate build folder)
        cmd = [
            "xelatex",
            "-interaction=nonstopmode",
            filename
        ]
        
        try:
            result = subprocess.run(cmd, cwd=TARGET_DIR, capture_output=True, text=True)
            
            if result.returncode == 0:
                print(f"✅ Success: {filename}")
                success_count += 1
            else:
                print(f"❌ Failed: {filename}")
                failed_files.append(filename)
                # Print last few lines of log if available
                log_file = os.path.join(TARGET_DIR, filename.replace('.tex', '.log'))
                if os.path.exists(log_file):
                    print("  Last 10 lines of log:")
                    with open(log_file, 'r', errors='ignore') as f:
                        lines = f.readlines()
                        for line in lines[-10:]:
                            print("    " + line.strip())
                else:
                    print("  No log file generated.")
                    print("  Stderr:", result.stderr[:200])

        except Exception as e:
            print(f"❌ Exception compiling {filename}: {e}")
            failed_files.append(filename)

    print("\n" + "="*30)
    print(f"Compilation Summary: {success_count}/{len(tex_files)} passed.")
    if failed_files:
        print("Failed files:")
        for f in failed_files:
            print(f"  - {f}")
    print("="*30)

if __name__ == "__main__":
    compile_all_solutions()
