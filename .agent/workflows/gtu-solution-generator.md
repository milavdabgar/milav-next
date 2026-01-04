---
title: "GTU LaTeX Solution Generator"
date: 2026-01-04
---

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
% Use preamble.tex for English OR preamble.gu.tex for Gujarati
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

**Note**: Use `preamble.gu.tex` for Gujarati (includes font setup), `preamble.tex` for English.

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
5. `\subparagraph` → Minor nested details (optional, use sparingly)

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

% Code: caption BOTTOM (inside lstlisting)
\begin{lstlisting}[language=Java,caption={Find Maximum of Three Numbers}]
public class MaxOfThree {
    // code here
}
\end{lstlisting}
```

### 6. Typography

- **Text quotes**: `` ``double'' `` and `` `single' `` (smart quotes)
- **Code quotes**: `"string"` inside lstlisting (straight quotes)
- **Spacing**: `\,` for thin space in units (\(1.5\,k\Omega\))

## Content Requirements by Marks

| Marks       | Words   | Structure                                                    |
| ----------- | ------- | ------------------------------------------------------------ |
| **3 marks** | 90-150  | Explanation + Visual OR Code + Description list + Mnemonic   |
| **4 marks** | 120-180 | Explanation + Visual + Calculation OR Example + Description list + Mnemonic |
| **7 marks** | 200-300 | Detailed explanation + Table/Diagram + Code/Circuit + Description lists + Mnemonic |

## Gujarati Version

- Natural translation, keep technical terms in English
- Code/math/diagrams identical  
- Use `preamble.gu.tex` (includes Gujarati font setup)
- Same structure as English version

## Quality Check

- ✅ Standard LaTeX only, math: `\(...\)` and `\[...\]`
- ✅ Description lists for labeled items
- ✅ Word counts match marks (see table above)
- ✅ Smart quotes in text, straight in code

## Compilation

- **English**: `pdflatex sample_solution.tex`
- **Gujarati**: `xelatex sample_solution.gu.tex`
- **Markdown**: `pandoc file.tex -o file.md --to=gfm --wrap=none --standalone --shift-heading-level-by=1`
- **ChkTeX**: Only cosmetic TikZ warnings acceptable

**Copy patterns from `sample_solution.tex` - it shows everything.**
