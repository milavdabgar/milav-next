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
- **Spacing**: `\,` for thin space in units (\(1.5\,k\Omega\))

## Content Requirements by Marks

| Marks       | Words   | Structure                                                    |
| ----------- | ------- | ------------------------------------------------------------ |
| **3 marks** | 90-150  | Explanation + Visual OR Code + Description list + Mnemonic   |
| **4 marks** | 120-180 | Explanation + Visual + Calculation OR Example + Description list + Mnemonic |
| **7 marks** | 200-300 | Detailed explanation + Table where appropriate |


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

**Verification**: 

1. Compare TOC entries: English and Gujarati should have identical number of entries at each level
2. Line count check: Both `.tex` files should have similar line counts (±10% variation is acceptable due to Gujarati text width)
3. Structure match: Same number of `\section`, `\subsection`, `\subsubsection`, `\paragraph`, `\subparagraph` commands in both files

## Quality Checklist

Before submitting, verify:

- ✅ **Math notation**: `\(...\)` for inline, `\[...\]` for display (NO `$` or `$$`)
- ✅ **Semantic lists**: Description lists for labeled items, itemize for bullets, enumerate for numbered
- ✅ **Word counts**: Match marks allocation (3→90-150, 4→120-180, 7→200-300 words)
- ✅ **Typography**: Smart quotes in text (`` ``double'' ``), straight quotes in code
- ✅ **TOC**: Included with `\setcounter{tocdepth}{5}` and `\newpage` after
- ✅ **Code listings**: NO `\paragraph{}` headings before them (use caption parameter only)
- ✅ **Content fidelity**: English and Gujarati have identical structure
- ✅ **All 5 levels**: Each solution demonstrates complete hierarchy
- ✅ **Mnemonics**: Every question ends with `\paragraph{Mnemonic:}` or `\paragraph{મેમરી ટ્રીક:}`
- ✅ **Compilation**: Both versions compile without errors (run twice for TOC)

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
