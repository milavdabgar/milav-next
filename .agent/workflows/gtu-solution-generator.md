---
title: "GTU LaTeX Solution Generator"
date: 2026-01-04
---

# Generate GTU Exam Solutions in LaTeX

**INPUT**: Question paper (markdown format)  
**OUTPUT**: Complete LaTeX solution files (English `.tex` + Gujarati `.gu.tex`)

## Reference Files (These ARE the Specification)

Study `sample_solution.tex` and `sample_solution.gu.tex` in:
```
/Users/milav/Code/milav-next/latex-templates/gtu-solutions/
```

They show exact patterns for all question types.

## File Structure

```latex
\documentclass{article}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/preamble.tex}

\title{Subject Name (CODE) - Term Year Solution}
\date{Month Day, Year}

% PDF Metadata (copy from sample)
\hypersetup{...}

\begin{document}
\maketitle
% Solutions here
\end{document}
```

## Critical LaTeX Conventions

### 1. Math Notation (LaTeX Standard)
```latex
\(inline math\)          % NOT $...$
\[display math\]         % NOT $$...$$
```

### 2. Sectioning Hierarchy
```latex
\section{Question 1}                  % H1
\subsection{Question 1(a) [3 marks]} % H2
\subsubsection{Solution}             % H3
\paragraph{Step 1:}                  % H4
\paragraph{Mnemonic:}                % H4
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

### 5. Tables and Figures
```latex
% Table: caption TOP
\begin{table}[H]
\centering
\caption{Title}
\begin{tabularx}{\textwidth}{lXX}
...
\end{tabularx}
\end{table}

% Figure: caption BOTTOM
\begin{figure}[H]
\centering
...circuit/diagram...
\caption{Title}
\end{figure}
```

## Gujarati Version

- Natural translation, keep technical terms in English
- Code/math/diagrams identical
- Same structure, use fontspec + Noto Sans Gujarati

## Quality Check

- ✅ Standard LaTeX only, math: `\(...\)` and `\[...\]`
- ✅ Description lists for labeled items
- ✅ Compiles: `pdflatex` (en) / `xelatex` (gu)

**Copy patterns from `sample_solution.tex` - it shows everything.**
