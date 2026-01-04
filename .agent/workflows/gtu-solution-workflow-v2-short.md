---
title: "GTU LaTeX Solution Generator - Quick Workflow v2"
description: "Condensed workflow with logical sequence for LLM execution"
date: 2026-01-04
version: 2.0
---

# GTU Solution Generator - Quick Guide

**INPUT**: Question paper (markdown)  
**OUTPUT**: English `.tex` + Gujarati `.gu.tex` (both with PDFs)

---

## 1. UNDERSTAND: What to Generate

### Reference Files (Study These First)

```
/Users/milav/Code/milav-next/latex-templates/gtu-solutions/
├── sample_solution.tex       # Shows ALL patterns
├── sample_solution.gu.tex    # Shows translation
├── preamble.tex              # English setup
└── preamble.gu.tex           # Gujarati setup
```

### Critical Rules (MUST FOLLOW)

**Math**: `\(...\)` and `\[...\]` ONLY (NEVER `$`)

**Hierarchy** (All 5 levels required):

```latex
\section{Question 1}                      % H1
\subsection{Question 1(a) [3 marks]}     % H2
\textbf{Question statement}              % Bold (separate line)
\subsubsection{Solution}                  % H3
\paragraph{Given Data:}                   % H4
\subparagraph{Detail:}                    % H5 (when needed)
\paragraph{Mnemonic:}                     % H4 (required ending)
```

**Tables**: Use `tabularx`, caption TOP, `[H]` placement
**Figures**: Caption BOTTOM, `[H]` placement
**Code**: Use `caption` parameter (NO `\paragraph` before)
**Lists**: description (labeled), itemize (bullets), enumerate (numbers)

**Word Counts**: 3 marks→120, 4 marks→150, 7 marks→250

### Gujarati Rules

**Translate**: Descriptive text, explanations  
**Keep English**: Acronyms (HTML, CPU, BJT, LED)  
**Keep Identical**: Code, Math, Diagrams, Comments  
**Must Match**: Same line count, same sectioning at same line numbers

---

## 2. EXECUTE: Workflow Steps

### Step 1: Initialize Both Files

Create `[Code]-[Season]-[Year]-Solution-Full.tex` and `.gu.tex`

Add to both:

- Metadata block
- `\documentclass{article}`
- Preamble input (`.tex` or `.gu.tex`)
- Title, date, PDF metadata
- `\begin{document}`, `\maketitle`
- TOC: `\setcounter{tocdepth}{5}`, `\tableofcontents`, `\newpage`
- **Don't add `\end{document}` yet**

### Step 2: Generate Q1 (Both Languages Simultaneously)

For each part (a, b, c, OR):

1. Comment block describing question
2. Section/subsection structure
3. Bold question statement
4. Solution with complete hierarchy
5. Code/Diagram/Table/Calculation
6. Mnemonic paragraph

**Ensure**: Gujarati has identical structure, comments, technical content

### Step 3: Verify Q1

**Compile**:

```bash
pdflatex [file].tex
xelatex [file].gu.tex
```

**Verify**:

```bash
python verify_solutions.py [english.tex] [gujarati.gu.tex]
```

**Required**: `✅ PASSED`

**If fails**: Fix issues, recompile, re-verify

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
2. Compile twice (for TOC): `pdflatex` twice, `xelatex` twice
3. Final verification (must pass all 53 checks)
4. Output: 2 PDFs ready

---

## 3. VERIFY: Check Quality

### Verification Script

**Location**: `content/resources/study-materials/00-general/sem-1/DI01000051-fe/verify_solutions.py`

**Command**: `python verify_solutions.py [en.tex] [gu.tex]`

**When**: After Q1, after each Q2-Q5, after finalization

### 53 Checks (8 Categories)

1. **Core Structure**: Line counts, TOC hierarchy
2. **Metadata**: Document structure, PDF metadata, preambles
3. **Syntax**: No `$`, `**`, straight quotes; proper hierarchy
4. **Quality**: Word counts, typography, mnemonics
5. **Fidelity**: Code/Math/Diagrams identical, **sectioning alignment**
6. **Validation**: TOC setup, patterns, all 5 levels, semantic lists
7. **Format**: `tabularx`, `[H]`, `\paragraph`/`\subparagraph` only
8. **Compilation**: Both files compile

**26 Critical** (must pass) + **27 Warnings** (informational)

### Common Fixes

**Line mismatch**: Check comments, blank lines  
**Sectioning misalignment**: Verify line numbers match  
**Caption missing**: Add to tables/figures/listings  
**Code differs**: Ensure 100% identical  
**Forbidden syntax**: Use `\(...\)` not `$`, smart quotes not straight  
**Structure violation**: Only `\paragraph`/`\subparagraph` inside solutions

---

## Quick Checklist

### Per Question

- [ ] Comment block
- [ ] All 5 hierarchy levels used
- [ ] Bold question statement
- [ ] Code/Diagram/Table included
- [ ] Mnemonic paragraph
- [ ] Word count target met
- [ ] Math uses `\(...\)` only
- [ ] Semantic lists
- [ ] Gujarati identical structure
- [ ] Comments identical

### Per Verification

- [ ] Both compile successfully
- [ ] `verify_solutions.py` shows `✅ PASSED`
- [ ] Line counts match
- [ ] Sectioning aligned
- [ ] Both PDFs generated

---

## Success = ✅ PASSED + 2 PDFs

**When done right**:

- Both files same line count
- All sectioning at same lines
- Technical content 100% identical
- Word counts in range
- Both PDFs compile (twice each)
- Verification shows `✅ PASSED`
- All 5 questions complete
