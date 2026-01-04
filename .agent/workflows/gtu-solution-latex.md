---
title: "GTU LaTeX Solution Generator"
date: 2026-01-04
---

**INPUT**: Question paper (markdown format like `sample_paper.md`)  
**OUTPUT**: Complete LaTeX solution files in same folder (English `.tex` + Gujarati `.gu.tex`)

## Example-Driven Approach

**Study these reference files** - they demonstrate ALL conventions:

```
/Users/milav/Code/milav-next/latex-templates/gtu-solutions/
├── sample_paper.md              # Input format example
├── sample_solution.tex          # English output - YOUR SPEC
├── sample_solution.gu.tex       # Gujarati output - YOUR SPEC
└── preamble.tex                 # Shared configuration (only dependency)
```

**Your task**: Given a question paper like `sample_paper.md`, produce solutions following the EXACT structure, formatting, and conventions shown in `sample_solution.tex` and `sample_solution.gu.tex`.

**The sample solutions ARE the specification** - they show everything you need:

- Standard LaTeX only - NO custom commands
- Semantic markup with proper list environments
- LaTeX-native math notation (NOT markdown style)
- Tables with caption at TOP (Q1c)
- Figures with caption at BOTTOM (Q1c OR)
- Code with lstlisting (Q1a)
- CircuiTikZ circuits (Q1c OR)
- TikZ diagrams (Q1c OR)

## File Structure

```latex
\documentclass{article}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/preamble.tex}

\title{Subject Name (CODE) - Term Year Solution}
\date{Month Day, Year}

% PDF Metadata
\hypersetup{
  pdftitle={Subject Name (CODE) - Term Year Solution},
  pdfsubject={GTU Exam Solution - Term-Year},
  pdfauthor={Milav Dabgar},
  pdfkeywords={study-material, solutions, gtu, subject-code},
  pdfcreator={XeLaTeX}
}

\begin{document}
\maketitle
```

## Conventions (MUST Follow)

### 1. Mathematics Notation (LaTeX Standard - NOT Markdown)

**REQUIRED**: Use LaTeX-native math notation, NOT markdown style.

```latex
% CORRECT - LaTeX Standard
Inline math: \(x + y = z\)
Display math: \[f(x) = \frac{1}{2\pi}\]

% WRONG - Never use these
Inline: $x + y$        % This is TeX, not LaTeX2e
Display: $$...$$       % Deprecated TeX notation
```

**Why**: LaTeX2e standard for proper semantics. Pandoc converts `\(...\)` to GFM `` $`...`$ `` automatically.

### 2. Semantic Markup (Use Proper List Environments)

**Description Lists** for labeled items (term-definition pairs):

```latex
% CORRECT - Semantic
\begin{description}
    \item[Transistors:] Used for amplification...
    \item[Diodes:] Allow current in one direction...
\end{description}

% WRONG - Non-semantic
\begin{itemize}
    \item \textbf{Transistors}: Used for...  % Misuse of itemize
\end{itemize}
```

**When to use each**:

- `description`: Labeled items (Key Points, Results, Parameters)
- `itemize`: Unlabeled bullet lists (Given Data)
- `enumerate`: Numbered sequences (steps, procedures)

### 3. Sectioning Hierarchy (Standard LaTeX)

```latex
\section{Question 1}                    % H1 - Question number
\subsection{Question 1(a) [3 marks]}    % H2 - Sub-question
\subsubsection{Solution}                 % H3 - Solution header
\paragraph{Java Program:}                % H4 - Content sections
\paragraph{Structure Examples
```

**See `sample_solution.tex` for complete patterns**:

1. **Q1(a) [3 marks]**: Programming question
   - Explanation paragraph with `\textbf{}` and `\emph{}`
   - Code with `lstlisting` environment
   - Output in `verbatim`
   - Description list for Key Points
   - Mnemonic as paragraph section

2. **Q1(b) [4 marks]**: Calculation question
   - Given Data as itemize list with inline math `\(...\)`
   - Step-by-step calculation with display math `\[...\]`
   - Results as description list
   - Mnemonic with formula notation

3. **Q1(c) [7 marks]**: Comparison/Theory question
   - Explanation paragraph
   - Table with `tabularx` for comparisons
   - Two description lists for detailed components
   - Key distinction paragraph
   - Mnemonic

4. **Q1(c OR) [7 marks]**: Circuit/Diagram question
   - Explanation paragraph
   - Circuit with CircuiTikZ
   - Working principle as description list (3 items)
   - Waveforms with TikZ
   - Key Parameters as description list
   - Applications paragraph
   - Mnemonic

## Gujarati Version Rules

**Follow `sample_solution.gu.tex` conventions**:

1. **Natural translation**: Not word-by-word, but meaning-preserving
2. **Keep technical terms in English**: "Transistors", "BJT", "FET", "Diodes"
3. **Keep all code identical**: No translation in lstlisting blocks
4. **Keep all math identical**: Same formulas, same notation
5. **Keep diagrams identical**: TikZ/CircuiTikZ code unchanged
6. **Translate text only**: Explanations, labels, descriptions
7. **Use inline font setup**: fontspec + polyglossia + Noto Sans Gujarati
8. **Same structure**: All sectioning, lists, formatting identical

| Marks | Words | Structure |
|-------|-------|-----------|
| **3 marks** | 90-150 | Explanation + Visual OR Code + Description list + Mnemonic |
| **4 marks** | 120-180 | Explanation + Visual + Calculation OR Example + Description list + Mnemonic |
| **7 marks** | 200-300 | Detailed explanation + Table/Diagram + Code/Circuit + Description lists + Mnemonic |

### 6. Mnemonic Sections (Paragraph + Emphasis)

```latex
% CORRECT - Semantic structure
\paragraph{Mnemonic:}
\emph{MAX: Compare in pairs, update Maximum At eXamination}

% For formulas in mnemonics:
\paragraph{Mnemonic:}
\emph{RC-Formula:} \(f_c = \frac{1}{2\pi RC}\), \(V_{out} = 0.707 \times V_{in}\) at \(f_c\)
```

### 7. Typography

- **Text quotes**: `` ``double'' `` and `` `single' `` (smart quotes)
- **Code quotes**: `"string"` inside lstlisting (straight quotes)
- **Spacing**: `\,` for thin space in units (\(1.5\,k\Omega\))

### 8. Tables and Figures

```latex
% Tables: Caption at TOP
\begin{table}[H]
\centering
\caption{Table Title}
\begin{tabularx}{\textwidth}{lXX}
\toprule
...
\bottomrule
\end{tabularx}
\end{table}

% Figures: Caption at BOTTOM
\begin{figure}[H]
\centering
\begin{tikzpicture}
...
\end{tikzpicture}
\caption{Figure Title}
\end{figure(a)}{3}{Question text from paper}

\begin{solutionbox}
% Solution content - see examples for structure
\end{solutionbox}

\begin{mnemonicbox}
```

**Before submitting, verify against `sample_solution.tex`**:

### Structure

- ✅ Uses only standard LaTeX commands (no `\keyword{}`, `\code{}`, `\questionmarks{}`)
- ✅ Standard sectioning: `\section{}` → `\subsection{}` → `\subsubsection{}` → `\paragraph{}`
- ✅ Description lists for all labeled items
- ✅ Mnemonics as `\paragraph{Mnemonic:}` sections
- ✅ Only one dependency: `preamble.tex`

### Mathematics

- ✅ Inline math uses `\(...\)` NOT `$...$`
- ✅ Display math uses `\[...\]` NOT `$$...$$`
- ✅ All formulas use proper LaTeX notation
- ✅ Spacing in units: `\,` for thin space

### Content

- ✅ Word counts match marks (3→90-150, 4→120-180, 7→200-300)
- ✅ All questions have visuals (tables/diagrams/code)
- ✅ Description lists for Key Points, Results, Parameters
- ✅ Smart quotes in text (`` ``...'' ``), straight in code
- ✅ Every question has mnemonic section

### Compilation

- ✅ English: `pdflatex sample_solution.tex` compiles
- ✅ Gujarati: `xelatex sample_solution.gu.tex` compiles
- ✅ ChkTeX shows only cosmetic warnings (TikZ trailing spaces acceptable)
- ✅ Markdown: `pandoc file.tex -o file.md --to=gfm --wrap=none --standalone --shift-heading-level-by=1`

## Markdown Conversion (Optional)

To generate GFM markdown files:

```bash
pandoc sample_solution.tex -o sample_solution.md --to=gfm --wrap=none --standalone --shift-heading-level-by=1
pandoc sample_solution.gu.tex -o sample_solution.gu.md --to=gfm --wrap=none --standalone --shift-heading-level-by=1
```

**Output format**:

- Inline math: `` $`x + y`$ `` (GFM with backticks)
- Display math: ` ``` math` block
- Tables: Proper GFM tables
- Description lists: Term-definition structure preserved

## Execution Steps

1. **Study Examples**: Read `sample_solution.tex` lines 1-257 completely
2. **Understand Patterns**: Note mark-based structures (3/4/7 marks)
3. **Parse Input**: Extract questions from markdown paper
4. **Generate Solutions**: Match structure to mark allocation
5. **Add Visuals**: Tables (comparisons), TikZ (diagrams), lstlisting (code)
6. **Semantic Markup**: Use description lists for labeled content
7. **Math Notation**: Use `\(...\)` and `\[...\]` only
8. **Write Gujarati**: Translate text, keep technical terms/code/math
9. **Compile Both**: Test pdflatex and xelatex
10. **Verify**: Check all items in quality checklist

---

**Golden Rule**: The examples ARE the specification. When in doubt, copy the exact

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
