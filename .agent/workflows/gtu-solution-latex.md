---
title: "GTU LaTeX Solution Generator"
date: 2026-01-03
---

# Generate GTU Exam Solutions in LaTeX

**INPUT**: Question paper (markdown format like `sample_paper.md`)  
**OUTPUT**: Complete LaTeX solution files in same folder (English `.tex` + Gujarati `.gu.tex`)

## Example-Driven Approach

**Study these reference files** - they demonstrate ALL conventions:

```
/Users/milav/Code/milav-next/latex-templates/gtu-solutions/
├── sample_paper.md              # Input format example
├── sample_solution.tex          # English output example
├── sample_solution.gu.tex       # Gujarati output example
├── latex-conventions.tex        # Style guide with examples
└── latex-conventions.gu.tex     # Gujarati style guide
```

**Your task**: Given a question paper like `sample_paper.md`, produce solutions following the EXACT structure, formatting, and conventions shown in `sample_solution.tex` and `sample_solution.gu.tex`.

## File Structure

```latex
\documentclass{article}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/preamble.tex}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/commands.tex}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/english-boxes.tex}
% For Gujarati: use gujarati-boxes.tex instead

\title{Subject Name (CODE) - Term Year Solution}
\date{Month Day, Year}

\begin{document}
\maketitle

% Solutions here - follow sample_solution.tex format exactly

\end{document}
```

## Critical Rules (Study Examples for Details)

### Content Requirements by Marks

| Marks | Words | Structure |
|-------|-------|-----------|
| **3 marks** | 90-150 | Definition + Visual OR Code + Key points + Mnemonic |
| **4 marks** | 120-180 | Explanation + Visual + Calculation OR Example + Key points + Mnemonic |
| **7 marks** | 200-300 | Detailed explanation + Table/Diagram + Code/Circuit + Key points + Mnemonic |

**See `sample_solution.tex` lines 15-60 (3 marks), 62-105 (4 marks), 107-148 (7 marks) for examples.**

### Typography (Examples in latex-conventions.tex)

- **Smart quotes in text**: `` ``double'' `` and `` `single' ``
- **Straight quotes in code**: `"string"` inside lstlisting
- **Inline code**: `\code{text}` NOT `\texttt{text}`

### Structure (Examples in sample_solution.tex)

- **Tables**: `\captionof{table}` at TOP, use `\tabulary{\linewidth}{|L|L|}`
- **Figures**: `\captionof{figure}` at BOTTOM
- **Circuits**: Use CircuiTikZ (see sample_solution.tex lines 161-183)
- **Diagrams**: Use TikZ with inline styles like `circle, draw, fill=blue!10` (see latex-conventions.tex lines 84-93)

### Question Format

```latex
\questionmarks{1(a)}{3}{Question text from paper}

\begin{solutionbox}
% Solution content - see examples for structure
\end{solutionbox}

\begin{mnemonicbox}
\mnemonic{Simple Memory Aid}
\end{mnemonicbox}
```

## Content Guidelines

**FOLLOW THE EXAMPLES** for:
- How to structure explanations (see sample_solution.tex Q1a, Q1b, Q1c)
- When to use tables vs diagrams (Q1c uses table, Q1c OR uses circuit diagram)
- How to format mathematics (Q1b shows step-by-step with \[ \])
- How to present code (Q1a shows lstlisting with output)
- Bullet point usage (all questions show \keyword{} usage)
- Mnemonic style (concise, memorable acronyms)

## Gujarati Version

**Follow `sample_solution.gu.tex` exactly**:
- Natural Gujarati translation (not word-by-word)
- Keep technical terms in English (e.g., "Transistors", "BJT", "FET")
- Keep all code, equations, diagrams identical
- Translate only explanatory text and labels

## Quality Checklist

Compare your output with `sample_solution.tex`:
- ✅ Every question has \questionmarks, \solutionbox, \mnemonicbox
- ✅ Word counts match mark allocation (3→90-150, 4→120-180, 7→200-300)
- ✅ All visuals present (tables for comparisons, diagrams for concepts, code for programming)
- ✅ Smart quotes in text, straight quotes in code
- ✅ \keyword{} used for important terms
- ✅ \code{} used for inline code elements
- ✅ File compiles without errors using xelatex

## Execution

1. **Study Examples**: Read `sample_solution.tex` completely to understand patterns
2. **Parse Input**: Extract questions from markdown paper
3. **Generate Solutions**: For each question, follow the structure pattern from examples matching the mark value
4. **Add Visuals**: Tables for comparisons, TikZ/CircuiTikZ for diagrams, lstlisting for code
5. **Write Both Files**: English `.tex` and Gujarati `.gu.tex` with identical structure
6. **Verify**: Check against quality checklist above

---

**Remember**: The examples ARE the specification. When in doubt, copy the pattern from `sample_solution.tex`.
