---
description: Convert MDX solution to native LaTeX
---

# MDX to LaTeX Solution Conversion

## Reference Templates

**IMPORTANT**: Study these example files to understand LaTeX conventions:

- English: `/Users/milav/Code/milav-next/latex-templates/gtu-solutions/example-solution.tex`
- Gujarati: `/Users/milav/Code/milav-next/latex-templates/gtu-solutions/example-solution.gu.tex`

## Workflow

### 1. Setup

Create `.tex` file in same directory as MDX source:

- English: `{subject-code}-{term}-solution.tex`
- Gujarati: `{subject-code}-{term}-solution.gu.tex`

### 2. Document Structure

```latex
\documentclass{article}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/preamble.tex}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/english-boxes.tex}  % or gujarati-boxes.tex
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/commands.tex}

\title{Subject Name (Code) - Term Year Solution}
\date{Month Day, Year}

\begin{document}
\maketitle

% Convert all questions here

\end{document}
```

### 3. Convert Content

- As the Solutions are Large files, and you might face '**Maximum Output Token Limit'**, to avoid this write in moderate chunks of around 500-600 lines.  You can write each file in around **two shots**, in one shot Write **Q1 a, Q1b, Q1c till Q3C**. in second shot you may cover **Q3a OR, Q3 b OR, Q3 c OR upto end Q5c OR**. 
- **Follow example templates** for all formatting patterns
- **STRICT Content Fidelity**:
  - **DO NOT** create, expand, or streamline text.
  - **DO NOT** summarize or omit details.
  - Migrate the **EXACT** text content from MDX to LaTeX.
  - The only exception is diagrams (see below).

#### converting MDX elements:

- Headings → `\questionmarks{}{}{}`
- Tables → `\tabulary` with caption at top
- Code blocks → `\lstlisting`
- Mnemonics → `\mnemonicbox`

#### Diagrams (The Exception to Fidelity)

MDX diagrams (ASCII/Mermaid) are limited. In LaTeX:

- **Be Creative**: Replace simple text diagrams with professional TikZ diagrams.
- **Improve Quality**: Use correct shapes, arrows, and layouts that better represent the concept.
- **Consistency**: Use the **SAME** enhanced TikZ diagram structure for both English and Gujarati versions (translate labels for Gujarati).
- Use `gtu` styles (`gtu block`, `gtu arrow`, `gtu state`, etc.).

### 4. Key Conventions (from examples)

- Use `\keyword{Term}` for highlighted terms
- Use `\code{inline}` for inline code (NOT `\texttt{}`)
- Tables: caption at TOP, figures: caption at BOTTOM
- TikZ: Use predefined `gtu block`, `gtu arrow`, `gtu state` styles
- Multi-line TikZ nodes: add `align=center` option
- Code: Use straight quotes `"` inside listings

### 5. Gujarati-Specific

- Use `gujarati-boxes.tex` instead of `english-boxes.tex`
- Translate all explanatory text to Gujarati
- Keep code, mnemonics, and technical terms in English
- Same structure and formatting as English version

### 6. Compile

```bash
cd /path/to/solution/directory
xelatex -interaction=nonstopmode {filename}.tex
xelatex -interaction=nonstopmode {filename}.tex  # Second run for references
rm -f *.aux *.log *.out
```