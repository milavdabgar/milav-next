---
title: "GTU Solution Generation"
date: 2026-01-03
---

# GTU LaTeX Solution Generator

**GOAL**: Generate comprehensive GTU exam solutions for perfect scores.

## FILE SETUP

**Filename**: `[Code]-[Season]-[Year]-Solution.tex` (e.g., `4341101-Summer-2024-Solution.tex`)  
**Location**: Same folder as question paper

**Required imports** (absolute paths):

```latex
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/preamble.tex}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/commands.tex}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/english-boxes.tex}
% For Gujarati: english-boxes.tex → gujarati-boxes.tex
```

## CRITICAL RULES

### Typography

- **Text**: Use smart quotes: `` ``double'' `` and `` `single' ``
- **Code**: Use straight quotes: `"string"`
- **Inline code**: `\code{text}` NEVER `\texttt{text}`

### Structure

- **Tables**: Caption at TOP, use `\tabulary{\linewidth}{|L|L|}`
- **Figures**: Caption at BOTTOM
- **Diagrams**: TikZ only, use `gtu block`, `gtu state`, `gtu arrow`, `gtu decision` styles

## SOLUTION TEMPLATE

```latex
\questionmarks{1(a)}{3}{Question text}

\begin{solutionbox}
Clear explanation (1-2 paragraphs).

% Table for comparisons
\begin{center}
\captionof{table}{Title}
\begin{tabulary}{\linewidth}{|L|L|}
\hline
\textbf{Col1} & \textbf{Col2} \\ \hline
Data & Data \\ \hline
\end{tabulary}
\end{center}

% OR Diagram
\begin{center}
\begin{tikzpicture}[node distance=1.5cm, auto]
    \node [gtu state] (n1) {Node};
    \node [gtu state, right=of n1] (n2) {Node};
    \path [gtu arrow] (n1) -- (n2);
\end{tikzpicture}
\captionof{figure}{Title}
\end{center}

% OR Code
\begin{lstlisting}[language=Java,caption={Title}]
System.out.println("Straight quotes");
\end{lstlisting}

% Key points (if needed)
\begin{itemize}
    \item \keyword{Term}: Brief explanation
\end{itemize}
\end{solutionbox}

\begin{mnemonicbox}
\mnemonic{ABC: Simple Memory Aid}
\end{mnemonicbox}
```

## CONTENT PRIORITY

Each answer MUST include (in order):

1. **Definition/Explanation** - Direct answer
2. **Visual** - Table (for comparisons) OR TikZ diagram
3. **Example** - Code (if programming) OR practical case
4. **Keywords** - Bullet points with `\keyword{}`
5. **Mnemonic** - Memory aid

## WORD TARGETS

- 3 marks: 90-150 words + visual
- 4 marks: 120-180 words + visual  
- 7 marks: 200-300 words + visual + code

**Prioritize completeness over word count.**

## GUJARATI VERSION

- Natural spoken Gujarati, not word-by-word translation
- Keep technical terms in English
- Identical diagrams, tables, code
- Separate file: `[Code]-[Season]-[Year]-Solution.gu.tex`

## QUALITY CHECKLIST

- [ ] Smart quotes in text, straight in code
- [ ] `\code{}` for inline code (no `\texttt{}`)
- [ ] Table captions TOP, figure captions BOTTOM
- [ ] TikZ uses `gtu` styles
- [ ] Every question has mnemonic
- [ ] All visuals clear and labeled

---

**Execute**: Generate complete solution file following template exactly.
