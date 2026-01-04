---
title: "GTU LaTeX Solution Generator - Workflow"
description: "Complete workflow for generating bilingual GTU exam solutions"
date: 2026-01-04
---

# GTU LaTeX Solution Generator

**INPUT**: Question paper (markdown format)  
**OUTPUT**: English `.tex` + Gujarati `.gu.tex` (both with PDFs)

---

## PART 1: Reference & Context

### What You're Creating

Two LaTeX solution files with:

- **Identical structure** (same line counts, sectioning at same line numbers)
- **Identical technical content** (code, math, diagrams 100% same)
- **Different languages** (only descriptive text translated)

**Files**: `[Code]-[Season]-[Year]-Solution-Full.tex` and `.gu.tex`

### Reference Files (Study First)

```
/Users/milav/Code/milav-next/latex-templates/gtu-solutions/
├── sample_solution.tex       # English (332 lines) - YOUR SPECIFICATION
├── sample_solution.gu.tex    # Gujarati (332 lines) - Shows translation
├── preamble.tex              # English setup
└── preamble.gu.tex           # Gujarati setup
```

**These samples show ALL patterns - refer to them frequently.**
---

## PART 2: Specifications

### ⚠️ IMPORTANT: Use ONLY Sample Files as Reference

Before proceeding, understand this critical rule:

**The ONLY valid reference files are:**

- `/Users/milav/Code/milav-next/latex-templates/gtu-solutions/sample_solution.tex`
- `/Users/milav/Code/milav-next/latex-templates/gtu-solutions/sample_solution.gu.tex`

### Document Template

```latex
%% METADATA
%% subject-code: SUBJECT001
%% subject-name: Subject Name
%% semester: 1
%% examination: Summer-2025
%% date: 01-01-2025
%% description: Solution guide for [subject]
%% tags: study-material, solutions, gtu, [code]
%% END METADATA

\documentclass{article}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/preamble.tex}

\title{Subject Name (CODE) - Term Year Solution}
\date{Month Day, Year}

\hypersetup{
  pdftitle={Subject Name (CODE) - Term Year Solution},
  pdfsubject={GTU Exam Solution - Term-Year},
  pdfauthor={Milav Dabgar},
  pdfkeywords={study-material, solutions, gtu, code},
  pdfcreator={xelatex}
}

\begin{document}
\maketitle

\setcounter{tocdepth}{5}
\tableofcontents
\newpage

% Solutions here

\end{document}
```

### Critical Rules (MUST FOLLOW)

#### Math Notation

```latex
✅ \(inline\) and \[display\]
❌ $inline$ and $$display$$  % NEVER use $
```

#### Complete Hierarchy (All 5 Levels)

```latex
\section{Question 1}                      % Major Question/Section
\subsection{Question 1(a) [3 marks]}      % SubQuestion of Main Question
\textbf{Question statement}               % Question Statement, on separate line
\subsubsection{Solution}                  % Solution Heading
\paragraph{Key Topic of Solution}         % Paragraphs To Explain Solution
\subparagraph{Subtopic of solution}       % Subparagraphs (when needed)
\paragraph{Mnemonic:}                     % Mnemonic at end (required end)
```

#### Lists (Semantic)

```latex
\begin{description}          % For labeled items
    \item[Label:] Text
\end{description}

\begin{itemize}              % For bullets
    \item Text
\end{itemize}

\begin{enumerate}            % For numbered steps
    \item Text
\end{enumerate}
```

#### Tables, Figures, Code

```latex
% Table: caption TOP, use tabularx, [H]
\begin{table}[H]
\centering
\caption{Title}
\begin{tabularx}{\textwidth}{lXX}
\toprule
...
\bottomrule
\end{tabularx}
\end{table}

% Figure: caption BOTTOM, [H]
\begin{figure}[H]
\centering
% diagram code
\caption{Title}
\end{figure}

% Code: caption parameter, NO \paragraph before
\begin{lstlisting}[language=Java,caption={Title}]
// code here
\end{lstlisting}
```

#### Typography & Commands

- Text: Smart quotes `` ``double'' `` and `` `single' ``
- Code: Straight quotes `"string"` inside lstlisting
- Use: `\textbf{}`, `\texttt{}`, `\emph{}`
- NO custom commands: `\keyword{}`, `\code{}`, etc.

#### Comments (Identical in both files)

```latex
% ========================================
% QUESTION 1(a): Description (X marks)
% Demonstrates: features shown
% ========================================
```

### Word Count Targets

| Marks | Range   | Target |
|-------|---------|--------|
| 3     | 90-150  | 120    |
| 4     | 120-180 | 150    |
| 7     | 200-300 | 250    |

### Gujarati Translation

**Translate**: Descriptive text, explanations  
**Keep English**: Acronyms (HTML, CPU, BJT, LED)  
**Transliterate**: Technical terms (Java → જાવા)  
**Keep 100% Identical**: Code, Math, Diagrams, Comments

**Critical Fidelity**:

- Same line count (exactly)
- Same sectioning (at same line numbers)
- Same structure (identical elements)
- Use `preamble.gu.tex`, compile with `xelatex`

---

## PART 3: Workflow

### Step 1: Initialize

Create both files: `[Code]-[Season]-[Year]-Solution-Full.tex` and `.gu.tex`

Add to both:

1. Metadata block
2. `\documentclass{article}`
3. Preamble (`.tex` or `.gu.tex`)
4. Title, date, PDF metadata
5. `\begin{document}`, `\maketitle`
6. TOC: `\setcounter{tocdepth}{5}`, `\tableofcontents`, `\newpage`
7. **Don't add `\end{document}` yet**

### Step 2: Generate Q1 (Both Languages Simultaneously)

For each part (a, b, c, OR):

**Pattern**:

```latex
% Comment block
\section{Question 1}
\subsection{Question 1(a) [3 marks]}
\textbf{Question statement}

\subsubsection{Solution}
Introduction paragraph...

\paragraph{Given Data:}
\begin{itemize}
    \item Data
\end{itemize}

\paragraph{Key Concept:}
Explanation...

[Code OR Diagram OR Table OR Calculation]

\paragraph{Mnemonic:}
\emph{Memory trick}
```

**Ensure**: Gujarati has identical structure, comments, technical content

### Step 3: Verify Q1

**Compile**:

```bash
xelatex [file].tex
xelatex [file].gu.tex
```

**Verify**:

```bash
python content/resources/study-materials/00-general/sem-1/DI01000051-fe/verify_solutions.py \
  [english.tex] [gujarati.gu.tex]
```

**Required**: `✅ PASSED`

**If fails**: Fix all issues, recompile, re-verify

**DO NOT proceed to Q2 until Q1 passes**

### Step 4: Add Q2-Q5 Iteratively

For each question:

1. Generate both En & Gu simultaneously
2. Append to files
3. Compile both
4. Verify (must pass)
5. Fix if needed
6. Only then proceed to next

### Step 5: Finalize

1. Add `\end{document}` to both
2. Compile twice (for TOC):

   ```bash
   xelatex [file].tex
   xelatex [file].tex
   xelatex [file].gu.tex
   xelatex [file].gu.tex
   ```

3. Final verification (all 53 checks must pass)
4. Output: 2 complete PDFs

---

## PART 4: Verification

### verify_solutions.py (53 Checks)

**Location**: `content/resources/study-materials/00-general/sem-1/DI01000051-fe/verify_solutions.py`

**8 Categories**:

1. Core Structure (line counts, TOC)
2. Metadata (document structure, PDF, preambles)
3. Syntax (no `$`, `**`, straight quotes)
4. Quality (word counts, typography, mnemonics)
5. Fidelity (Code/Math/Diagrams identical, **sectioning alignment**)
6. Validation (TOC setup, patterns, 5 levels, lists)
7. Format (tabularx, [H], paragraph-only solutions)
8. Compilation (both files)

**26 Critical** (must pass) + **27 Warnings** (info)

### When to Verify

After: Q1, Q2, Q3, Q4, Q5, Finalization

### Common Issues & Fixes

**Line mismatch**: Check comments, blank lines  
**Sectioning misaligned**: Verify line numbers  
**Caption missing**: Add to tables/figures/listings  
**Code differs**: Ensure 100% identical  
**Forbidden syntax**: Use `\(...\)` not `$`  
**Structure violation**: Only `\paragraph`/`\subparagraph` in solutions

---

## Quick Checklists

### Per Question

- [ ] Comment block
- [ ] All 5 hierarchy levels
- [ ] Bold question statement
- [ ] Code/Diagram/Table
- [ ] Mnemonic paragraph
- [ ] Word count target
- [ ] Math uses `\(...\)`
- [ ] Semantic lists
- [ ] Gujarati identical structure
- [ ] Comments identical

### Per Verification

- [ ] Both compile
- [ ] `✅ PASSED` status
- [ ] Line counts match
- [ ] Sectioning aligned
- [ ] Both PDFs generated

---

## Success Criteria

**Complete when**:

1. Both files same line count
2. Sectioning at same line numbers
3. Technical content 100% identical
4. Word counts in range
5. `verify_solutions.py` shows `✅ PASSED`
6. Both PDFs compile (twice each)
7. All questions complete
8. TOC shows all 5 levels

**Deliverables**:

- `[Code]-[Season]-[Year]-Solution-Full.tex` (English)
- `[Code]-[Season]-[Year]-Solution-Full.gu.tex` (Gujarati)
- `[Code]-[Season]-[Year]-Solution-Full.pdf` (English)
- `[Code]-[Season]-[Year]-Solution-Full.gu.pdf` (Gujarati)

---

**Remember**: Reference `sample_solution.tex` constantly - it shows exact patterns for everything.

**⛔ NEVER reference other `.tex` files in the working directory - they are old attempts and do not meet quality standards!**
