import os
import glob
import subprocess
import multiprocessing
import time
from datetime import datetime

# Root directory to search for solutions
ROOT_DIR = "content/resources/study-materials"

def find_solution_files():
    """Find all .tex and .gu.tex files in 'GTU Solutions Short' directories."""
    solution_files = []
    print(f"Scanning {ROOT_DIR} for solution files...")
    
    for root, dirs, files in os.walk(ROOT_DIR):
        if os.path.basename(root) == "GTU Solutions Short":
            for file in files:
                if (file.endswith(".tex") or file.endswith(".gu.tex")) and \
                   not file.startswith("preamble") and \
                   not file.startswith("commands") and \
                   not file.endswith("boxes.tex"):
                    solution_files.append(os.path.join(root, file))
    
    return solution_files

def compile_file(filepath):
    """Compile a single solution file using xelatex."""
    directory = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    
    cmd = [
        "xelatex",
        "-interaction=nonstopmode",
        filename
    ]
    
    start_time = time.time()
    try:
        result = subprocess.run(cmd, cwd=directory, capture_output=True, text=True)
        duration = time.time() - start_time
        
        status = "PASS" if result.returncode == 0 else "FAIL"
        return {
            "file": filepath,
            "status": status,
            "duration": duration,
            "error": result.stderr if status == "FAIL" else None
        }
    except Exception as e:
        return {
            "file": filepath,
            "status": "ERROR",
            "duration": time.time() - start_time,
            "error": str(e)
        }

def main():
    files = find_solution_files()
    print(f"Found {len(files)} solution files.")
    
    if not files:
        print("No files found. Exiting.")
        return

    print("Starting compilation with multiprocessing...")
    
    # Use CPU count for number of processes
    cpu_count = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=cpu_count)
    
    results = []
    total = len(files)
    
    for i, res in enumerate(pool.imap_unordered(compile_file, files), 1):
        print(f"[{i}/{total}] {res['status']} - {os.path.basename(res['file'])} ({res['duration']:.2f}s)")
        results.append(res)
    
    pool.close()
    pool.join()
    
    # Generate Report
    generate_report(results)

def generate_report(results):
    passed = [r for r in results if r['status'] == "PASS"]
    failed = [r for r in results if r['status'] != "PASS"]
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_file = "compilation_report.md"
    
    with open(report_file, "w") as f:
        f.write(f"# Compilation Report - {timestamp}\n\n")
        f.write(f"**Total Files:** {len(results)}\n")
        f.write(f"**Passed:** {len(passed)}\n")
        f.write(f"**Failed:** {len(failed)}\n\n")
        
        if failed:
            f.write("## Failed Files\n")
            f.write("| File | Error Sample |\n")
            f.write("|------|--------------|\n")
            for res in failed:
                # Capture last 200 chars of error or stderr
                error_msg = (res['error'] or "Unknown Error").strip().replace("\n", " ")[:200]
                rel_path = os.path.relpath(res['file'], os.getcwd())
                f.write(f"| `{rel_path}` | {error_msg} |\n")
        
        f.write("\n## Success Log\n")
        for res in passed:
             rel_path = os.path.relpath(res['file'], os.getcwd())
             f.write(f"- {rel_path} ({res['duration']:.2f}s)\n")
             
    print(f"\nReport generated at {report_file}")
    print(f"Summary: {len(passed)} Passed, {len(failed)} Failed.")

if __name__ == "__main__":
    main()
