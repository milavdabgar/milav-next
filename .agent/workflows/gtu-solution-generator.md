---
title: "GTU LaTeX Solution Generator"
date: 2026-01-04
---

**INPUT**: Question paper (markdown format)  
**OUTPUT**: Complete LaTeX solution files (English `.tex` + Gujarati `.gu.tex`)

# Workflow Steps (Simultaneous Generation Approach)

**Goal**: ensure high fidelity between English and Gujarati versions by generating them together for each question.

## 1. Initialization

- Create `[Code]-[Season]-[Year]-Solution-Full.tex` and `.gu.tex`.
- Add Preamble (`preamble.tex` for English, `preamble.gu.tex` for Gujarati).
- Add Title, Date, PDF Metadata.
- Add `\begin{document}`, `\maketitle`, table of contents setup, and `\newpage`.
- **Do not** add `\end{document}` yet.

## 2. Strict Q1 Verification (The Foundation)

1. **Generate Q1 (En & Gu)**:
   - Generate full LaTeX content for **Question 1** (all parts: a, b, c, OR) for **BOTH** English and Gujarati in a **single step**.
   - **Crucial**: Ensure Gujarati structure (paragraphs, lists, diagrams) matches English exactly.
   - **Compliance**: Use `\(...\)` for math, end with `Mnemonic`.
   
2. **Compile & Verify**:
   - Compile both Q1 files using `pdflatex` (En) and `xelatex` (Gu).
   - **Thorough Check**: 
     - Does it follow all "Critical LaTeX Conventions"?
     - Are math delimiters `\(...\)` used?
     - Is the Gujarati content fully translated but structurally identical?
     - Are diagrams identical?

3. **Run Verification Script**: Execute `verify_solutions.py [en-file] [gu-file]`
   - **CRITICAL**: ALL checks must pass before proceeding to Q2. Fix any errors:
     - ✅ **Line counts match exactly** (same number of lines in both files)
     - ✅ **Sectioning alignment** (all `\section`, `\subsection`, `\subsubsection`, `\paragraph`, `\subparagraph` at same line numbers)
     - ✅ **Caption presence** (all tables, figures, listings have captions)
     - ✅ **Code/Math/Diagram identity** (100% identical between En and Gu)
     - ✅ **Structure hierarchy** (Section → Subsection → Subsubsection{Solution} → Paragraph)
     - ✅ **Compilation success** (both PDFs generated without errors)
     - ✅ **Content fidelity** (identical paragraph/list/table/figure counts)
     - ✅ **Syntax compliance** (no `$`, `**`, straight quotes in text)
   
4. **Iterate**:
   - If ANY issue is found in verification, fix it **immediately** before proceeding.
   - Recompile and re-verify after fixes.
   - **DO NOT** move to Q2 until verification shows `✅ PASSED`.

## 3. Iterative Append (Q2 to Q5)

Once Q1 verification passes, proceed with Q2, then Q3, up to Q5.

For each subsequent Question (Qx):

1. **Generate En & Gu Simultaneously**: Produce the LaTeX code for Qx (all parts: a, b, c, OR) for both languages at the same time.
2. **Append**: Add the content to the respective main files.
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
     - TOC structure remains consistent
   - **If verification fails**: Fix issues immediately, recompile, and re-verify before continuing.
5. **Only after ✅ PASS**: Proceed to next question.

## 4. Finalization

- Append `\end{document}` to both files.
- **Final Compilation**:
  - English: `pdflatex` (Run twice for TOC update).
  - Gujarati: `xelatex` (Run twice for TOC update).
- **Final Verification**: Execute `verify_solutions.py [en-file] [gu-file]`
  - **ALL 53 checks must pass**:
    - Core structure (line counts, TOC hierarchy)
    - Document metadata and preambles
    - Syntax compliance (no `$`, `**`, straight quotes)
    - Content fidelity (code/math/diagrams identical)
    - Structural validation (sectioning alignment, solution structure)
    - Format standards (table format, figure placement, caption presence)
    - Compilation success
    - Word count vs marks allocation
    - Typography and formatting standards
  - **Status must be**: `✅ PASSED`
  - **If any check fails**: Fix issues, recompile, re-verify until all pass.
- **Output**: Two complete, verified PDF files ready for distribution.

---

# Verification Script Usage

**Location**: `content/resources/study-materials/00-general/sem-1/DI01000051-fe/verify_solutions.py`

**Command**:
```bash
python verify_solutions.py [english-file.tex] [gujarati-file.gu.tex]
```

**When to Use**:

- After generating Q1 (before proceeding to Q2)
- After adding each subsequent question (Q2, Q3, Q4, Q5)
- Before final submission

**What It Checks** (53 comprehensive checks across 8 categories):

1. **Core Structure**: Line counts match, TOC hierarchy identical
2. **Document Metadata**: Complete structure, PDF metadata, correct preambles with absolute paths
3. **Syntax Compliance**: No `$`, `**`, straight quotes in text; proper hierarchy; no deprecated commands
4. **Content Quality**: Word counts match marks allocation, proper typography, mnemonics present
5. **Content Fidelity**: Code/Math/Diagrams 100% identical, list/table/figure parity, **sectioning alignment at same line numbers**
6. **Structural Validation**: TOC setup, question patterns, bold statements, section numbering, all 5 hierarchy levels, semantic lists, caption positions
7. **Format Standards**: Tables use `tabularx`, figures use `[H]`, **solutions use only `\paragraph`/`\subparagraph`**
8. **Compilation**: Both files compile successfully

**Critical vs Warning Checks**:

- **26 Critical checks**: Must pass for `✅ PASSED` status
- **27 Warning checks**: Informational, don't fail verification

**If verification fails**: 

1. Review error messages (script shows exactly what failed)
2. Fix ALL identified issues
3. Recompile both files
4. Re-run verification
5. DO NOT proceed until `✅ PASSED`

---

# Reference / Specification

## Reference Files (These ARE the Specification)

Study `sample_solution.tex` and `sample_solution.gu.tex` in:

```
/Users/milav/Code/milav-next/latex-templates/gtu-solutions/
```

They show exact patterns for all question types.

## File Name, Location & Structure

**Filename**: `[Code]-[Season]-[Year]-Solution-Full.tex` (e.g., `4341101-Summer-2024-Solution-Full.tex`)  
**Location**: Same folder as question paper

```latex
\documentclass{article}
% Use preamble.tex for English OR preamble.gu.tex for Gujarati
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/preamble.tex}

\title{Subject Name (CODE) - Term Year Solution}
\date{Month Day, Year}

% PDF Metadata (copy from sample)
\hypersetup{...}

\begin{document}
\maketitle

% Table of Contents (REQUIRED)
\setcounter{tocdepth}{5}
\tableofcontents
\newpage

% Solutions here
\end{document}
```

**Note**: 

- Use `preamble.gu.tex` for Gujarati (includes font setup), `preamble.tex` for English
- TOC with depth=5 shows all 5 hierarchy levels
- Always include `\newpage` after TOC

## Critical LaTeX Conventions

### 1. Math Notation (LaTeX Standard)

```latex
\(inline math\)          % NOT $...$
\[display math\]         % NOT $$...$$
```

### 2. Question and Answer Structure

**Critical Pattern** (MUST follow exactly):

```latex
\section{Question 1}                           % H1: Main question number

\subsection{Question 1(a) [3 marks]}          % H2: Sub-question with marks
\textbf{Question statement here.}              % Question text in bold, separate line

\subsubsection{Solution}                       % H3: Solution heading

% Solution content using:
\paragraph{Given Data:}                        % H4: For subsections
\paragraph{Step 1:}                            % H4: For steps
\paragraph{Key Points:}                        % H4: For description lists

\subparagraph{Additional Detail:}             % H5: For nested detail (rarely used)

\paragraph{Mnemonic:}                          % H4: Always end with mnemonic
```

**Complete Hierarchy**:

1. `\section` → Main question number
2. `\subsection` → Sub-question with marks
3. `\subsubsection` → Solution heading
4. `\paragraph` → Major subsections
5. `\subparagraph` → Minor nested details (use multiple times throughout for additional context)

**Example**:

```latex
\subsection{Question 1(a) [3 marks]}
\textbf{Write a Java program to find the maximum of three numbers.}

\subsubsection{Solution}
To find the \textbf{maximum} of three numbers...

\paragraph{Key Points:}
\begin{description}
    \item[Logic:] Compare values...
\end{description}

\subparagraph{Optimization Note:}
For production code, use built-in Math.max() method.
```

### 3. Semantic Lists

```latex
% Description for labeled items (Key Points, Results, Parameters)
\begin{description}
    \item[Label:] Text...
\end{description}

% Itemize for bullets (Given Data)
\begin{itemize}
    \item Text...
\end{itemize}

% Enumerate for steps
\begin{enumerate}
    \item Text...
\end{enumerate}
```

### 4. Standard Commands Only

```latex
\textbf{bold}    % NO custom \keyword{}
\texttt{code}    % NO custom \code{}
\emph{emphasis}  % For semantic emphasis
```

### 5. Tables, Figures, and Code

```latex
% Table: caption TOP
\begin{table}[H]
\centering
\caption{Title}
\begin{tabularx}{\textwidth}{lXX}
\toprule
...
\bottomrule
\end{tabularx}
\end{table}

% Figure: caption BOTTOM
\begin{figure}[H]
\centering
...circuit/diagram...
\caption{Title}
\end{figure}

% Code: NO paragraph heading before listing (caption is sufficient)
% WRONG: \paragraph{Java Program:}\begin{lstlisting}...
% CORRECT:
\begin{lstlisting}[language=Java,caption={Find Maximum of Three Numbers}]
public class MaxOfThree {
    // code here
}
\end{lstlisting}
```

**Important**: Never add `\paragraph` headings before code listings - the `caption` parameter provides the heading. Adding both causes overlap issues.

### 6. Typography

- **Text quotes**: `` ``double'' `` and `` `single' `` (smart quotes)
- **Code quotes**: `"string"` inside lstlisting (straight quotes)

## Content Requirements by Marks

| Marks       | Words   | Structure                                                    |
| ----------- | ------- | ------------------------------------------------------------ |
| **3 marks** | 90-150  | Explanation AND/OR Description list + (Diagrams AND/OR Tables) OR Code Listing + Mnemonic   |
| **4 marks** | 120-180 | Explanation AND/OR Description list + (Diagrams AND/OR Tables) OR Code Listing OR Calculation + Mnemonic |
| **7 marks** | 200-300 | Detailed explanation AND/OR Description list + (Diagrams AND/OR Tables) OR Code Listing OR Calculation + Mnemonic  |


## Gujarati Version

**Follow `sample_solution.gu.tex` conventions exactly:**

### Translation Rules

1. **Natural translation**: Not word-by-word, but meaning-preserving Gujarati
2. **Technical terms**: Keep English acronyms (HTML, CSS, JavaScript, BJT, FET, MOSFET, IC, SCR, PIV)
3. **Transliteration**: Use natural Gujarati for common technical terms:
   - Java → જાવા
   - Transistors → ટ્રાન્ઝિસ્ટર્સ
   - Diodes → ડાયોડ્સ
   - Capacitor → કેપેસિટર
   - Resistor → રેઝિસ્ટર

### Preservation Rules

4. **Code blocks**: Keep 100% identical (no translation in `\begin{lstlisting}...\end{lstlisting}`)
5. **Math expressions**: Keep 100% identical (all `\(...\)` and `\[...\]` unchanged)
6. **Diagrams**: Keep 100% identical (all TikZ/CircuiTikZ/karnaugh-map code unchanged)
7. **Translate only**: Regular text paragraphs, descriptions, explanations, list items

### Structure Requirements (Content Fidelity)

8. **Same hierarchy**: Identical sectioning levels at identical positions
9. **Same elements**: Same number of paragraphs, subparagraphs, lists, tables, figures
10. **Same patterns**: If English has 3 subparagraphs in Q1(a), Gujarati must have 3 subparagraphs in Q1(a)
11. **Same flow**: Introduction → Explanation → Visual → Analysis → Mnemonic (exactly matching English)

### Technical Requirements

- Use `preamble.gu.tex` (includes Gujarati font setup with Noto Sans Gujarati)
- Compile with `xelatex` (NOT `pdflatex`)
- Run twice to populate table of contents
- **Verification**: Use `verify_solutions.py` to ensure perfect content fidelity (see Verification Script Usage section)

## Quality Checklist

**Before submitting**: Run `verify_solutions.py` (must show `✅ PASSED`)

**Key manual checks** (also verified by script):

- Math: `\(...\)` and `\[...\]` only (NO `$`)
- Lists: Use semantic types (description/itemize/enumerate)
- Word counts: 3 marks→90-150, 4 marks→120-180, 7 marks→200-300
- Code: Use `caption` parameter (NO `\paragraph` before listings)
- Structure: All 5 hierarchy levels present
- Mnemonics: End every question with `\paragraph{Mnemonic:}`
- Compilation: Both files compile twice without errors

## Packages Available

- **karnaugh-map**: For K-map diagrams (already in preambles)
- **circuitikz**: For circuit diagrams
- **tikz**: For custom diagrams
- **listings**: Code syntax highlighting (configured with proper spacing)
- See preambles for complete list

## Compilation

- **English**: `pdflatex sample_solution.tex` (run twice for TOC)
- **Gujarati**: `xelatex sample_solution.gu.tex` (run twice for TOC)
- **Markdown**: `pandoc file.tex -o file.md --to=gfm --wrap=none --standalone --shift-heading-level-by=1`
- **ChkTeX**: Only cosmetic TikZ warnings acceptable

**Critical**: Compile twice to populate table of contents correctly.

**Copy patterns from `sample_solution.tex` - it shows everything.**
