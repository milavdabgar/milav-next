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

### 3. Iterative Append (Q2 to Q5)

- For each subsequent Question (Q2, Q3, Q4, Q5):
  1. **Generate En & Gu Simultaneously**: Produce LaTeX code for the entire question block.
  2. **Append**: Add to respective files.
  3. **Quick Check**: Ensure no `$` usage and structure matches reference.

### 4. Finalization

- Add `\end{document}`.
- **Final Compilation**: Run `pdflatex`/`xelatex` twice.
- **Verification**: Check TOC, line counts, and math fidelity.

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
3. **NO Translation**: Code blocks, Math expressions, TikZ/CircuitTikZ commands.
4. **Fidelity**: Maintain exact same paragraph/list count as English.
