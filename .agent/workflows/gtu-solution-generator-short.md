---
title: "GTU LaTeX Solution Generator (Short)"
description: "Condensed workflow for generating English and Gujarati LaTeX solutions."
date: 2026-01-04
---

**INPUT**: Question paper (markdown format)  
**OUTPUT**: Complete LaTeX solution files (English `.tex` + Gujarati `.gu.tex`)

## Workflow Steps (Simultaneous Generation Approach)

### 1. Initialization

- Create `[Code]-[Season]-[Year]-Solution-Full.tex` and `.gu.tex`.
- Use `preamble.tex` (English) and `preamble.gu.tex` (Gujarati).
- Add Title, Date, PDF Metadata, Main TOC setup (`tocdepth=5`), and `\newpage`.

### 2. Strict Q1 Verification (The Foundation)

1. **Generate Q1 (En & Gu)**: Generate full LaTeX content for **Question 1** (all parts) for **BOTH** languages in a single step.
2. **Compile & Verify**: Run `pdflatex` (En) and `xelatex` (Gu).
   - **Check**: Math `\(...\)`, diagrams, and identical structure. Fix ANY errors immediately.
3. **Run Verification Script**: Execute `verify_solutions.py [en-file] [gu-file]`
   - **CRITICAL**: ALL checks must pass before proceeding. Fix any errors:
     - ✅ **Line counts match exactly** (same number of lines in both files)
     - ✅ **Sectioning alignment** (all `\section`, `\subsection`, `\subsubsection`, `\paragraph`, `\subparagraph` at same line numbers)
     - ✅ **Caption presence** (all tables, figures, listings have captions)
     - ✅ **Code/Math/Diagram identity** (100% identical between En and Gu)
     - ✅ **Structure hierarchy** (Section → Subsection → Subsubsection{Solution} → Paragraph)
     - ✅ **Compilation success** (both PDFs generated without errors)
   - **DO NOT** proceed to Q2 until verification passes completely.

### 3. Iterative Append (Q2 to Q5)

- For each subsequent Question (Q2, Q3, Q4, Q5):
  1. **Generate En & Gu Simultaneously**: Produce LaTeX code for the entire question block.
  2. **Append**: Add to respective files.
  3. **Compile**: Run `pdflatex` (En) and `xelatex` (Gu) to check for compilation errors.
  4. **Run Verification Script**: Execute `verify_solutions.py [en-file] [gu-file]`
     - **MANDATORY**: Fix ALL issues identified by the script before proceeding.
     - **Key checks**:
       - Line count parity (En and Gu must have identical line counts)
       - Sectioning command alignment (must be at same line numbers)
       - Caption presence and positions (tables top, figures bottom)
       - Math/Code/Diagram fidelity (100% identical)
       - No forbidden syntax (`$`, `**`, straight quotes in text)
       - Solution structure (only `\paragraph` and `\subparagraph` inside solutions)
     - **If verification fails**: Fix issues immediately, recompile, and re-verify before continuing.
  5. **Only after ✅ PASS**: Proceed to next question.

### 4. Finalization

- Add `\end{document}`.
- **Final Compilation**: Run `pdflatex`/`xelatex` twice (for TOC update).
- **Final Verification**: Execute `verify_solutions.py [en-file] [gu-file]`
  - **ALL 53 checks must pass**:
    - Core structure (line counts, TOC hierarchy)
    - Document metadata and preambles
    - Syntax compliance (no `$`, `**`, straight quotes)
    - Content fidelity (code/math/diagrams identical)
    - Structural validation (sectioning alignment, solution structure)
    - Format standards (table format, figure placement, caption presence)
    - Compilation success
  - **Status must be**: `✅ PASSED`
- **Output**: Two complete PDF files ready for distribution.

## Reference Specifications

**Strictly follow the patterns in these files for all LaTeX syntax:**

- **English**: `latex-templates/gtu-solutions/sample_solution.tex`
- **Gujarati**: `latex-templates/gtu-solutions/sample_solution.gu.tex`

**Critical Rules:**

1. **Math**: ALWAYS use `\( ... \)` and `\[ ... \]`. NEVER use `$`.
2. **Structure**: `\section` -> `\subsection` -> `\subsubsection{Solution}` -> `\paragraph{...}` -> `\subparagraph`.
3. **Mnemonics**: EVERY question must end with a `\paragraph{Mnemonic:}`.
4. **Code**: Use `lstlisting` with `caption`. NO `\paragraph` before code.
5. **Lists**: Use `description` for labeled items, `enumerate` for steps.

## Gujarati Translation Rules

1. **Transliterate Technical Terms**: Java -> જાવા, Resistor -> રેઝિસ્ટર.
2. **Keep English**: Acronyms (HTML, CPU, BJT, LED).
3. **NO Translation**: Code blocks, Math expressions, TikZ/CircuiTikz commands, **comment blocks**.
4. **Fidelity**: Maintain exact same paragraph/list count as English.
5. **Comments**: Maintain exact same comments as English source code - **including section separator comments**.
6. **Line Count**: Gujarati file MUST have exactly the same number of lines as English file.

## Verification Script Usage

**Location**: `content/resources/study-materials/00-general/sem-1/DI01000051-fe/verify_solutions.py`

**Command**:
```bash
python verify_solutions.py [english-file.tex] [gujarati-file.gu.tex]
```

**When to Use**:
- After generating Q1 (before proceeding to Q2)
- After adding each subsequent question (Q2, Q3, Q4, Q5)
- Before final submission

**Critical Checks** (must all pass):
- Line counts match exactly
- All sectioning commands at same line numbers (42 total: `\section`, `\subsection`, `\subsubsection`, `\paragraph`, `\subparagraph`)
- All tables/figures/listings have captions
- Code/Math/Diagram 100% identical between files
- No forbidden syntax (`$`, `**`, straight quotes in text)
- Correct preamble paths (absolute paths required)
- Solution structure follows paragraph-only hierarchy
- Both files compile successfully

**If verification fails**: Fix ALL identified issues, recompile, re-verify. DO NOT proceed until `✅ PASSED`.
