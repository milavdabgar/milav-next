---
title: "GTU Solution Workflow (Optimized)"
date: 2025-05-01
description: "Imperative guidelines for generating GTU LaTeX solutions"
tags: ["gtu", "latex", "tikz", "workflow"]
---
**ROLE**: You are an expert academic content generator for Gujarat Technological University (GTU).
**OBJECTIVE**: Convert inputs into high-quality, exam-oriented LaTeX solutions.

I've Tagged a GTU Question paper (As Markdown file) for one of the subjects of Diploma in EC/ICT/IT Engineering. I want you to create a comprehensive paper solution of the attached/tagged Question paper in the same folder.

- Each Question Paper Contains Questions in Both English and Gujarati alongwith marks, and optionally Blooms Taxonomy Levels (R/U/A). Along with this it also contains metadata like:
  - SEMESTER: e.g. 1
  - EXAMINATION: e.g. Summer-2025
  - Date: e.g. 12-06-2025 (dd-mm-yyyy)
  - Subject Code:  e.g. DI01000051
  - Subject Name: e.g. Fundamentals of Electronics

## GUIDELINES FOR SOLUTION CREATION

### 1. File Organization

- Create complete paper solution in a single file name: `[subject-code]-[season]-[year]-solution.tex`. e.g. filename - `DI01000051-Summer-2025-Solution.tex`
  - English Solution Filename Example : DI01000051-Summer-2025-Solution.tex
  - Gujarati Solution Filename Example : DI01000051-Summer-2025-Solution.gu.tex
- First create the complete English version, then create the Gujarati version
- Add YAML Front Matter to the file, as per below example

### 3. Content Requirements and Priority Order

1. **FIRST PRIORITY**: Use **tables** for comparisons and lists (always try this first)
2. **SECOND PRIORITY**: Include a **simple diagram** using mermaid/goat/ASCII/SVG if it helps explain concepts.
3. **THIRD PRIORITY**: For coding questions, write the **simplest, shortest code** possible
4. **FOURTH PRIORITY**: Use bullet points with **bold keywords** only if needed and within word limits

- **Reduced word count** for very weak students - strictly follow these limits:
  - 3-mark questions: 60-75 words
  - 4-mark questions: 75-90 words
  - 7-mark questions: 125-150 words

### 4. Solution Structural Elements

1. Keep diagrams and tables **simple and easy to understand** - they should be the primary method to explain concepts
2. Use **proper latex syntax** for all formatting
3. Each bullet point (if used) should have **bold keywords** that help students memorize key terms
4. Create memorable **mnemonics** to help students recall the answer
5. Create code as **minimal and simple** as possible, as weak students struggle with coding
6. For diagrams:
   - Use mermaid, SVG, GOAT-ASCII or ASCII art that's compatible with pandoc and Hugo

### 5. Gujarati Translation Guidelines

- Use natural, conversational Gujarati while adapting content culturally (not word-for-word translation)
- Keep technical terms in English (programming terms, keywords, etc.)
- Include all diagrams, tables, and visual elements in the Gujarati version identical to the English version
- Ensure both English and Gujarati versions present the same level of detail and content
- **Diagrams**: COPY exact TikZ code but **translate the labels** inside the nodes.
- Make sure that you use gujarati glyphs and transliterate properly and not just give overuse english. use english only when it makes sense. acceptable and not acceptable ways are:

```markdown
Not at all accepted:
- HTTP requests handle કરે
- Load balancing અને caching
- Security features provide કરે

accepted statements:
- HTTP રિક્વેસ્ટ્સ હૅન્ડલ  કરે
- લોડ બેલેસિંગ એન્ડ કેશિંગ
- સિક્યોરિટી ફીચર્સ પ્રોવાઈડ કરે
```

## 1. CONFIGURATION & PATHS

**ALWAYS** use these absolute paths for imports:

- **Preamble**: `/Users/milav/Code/milav-next/latex-templates/gtu-solutions/preamble.tex`
- **Commands**: `/Users/milav/Code/milav-next/latex-templates/gtu-solutions/commands.tex`
- **English Boxes**: `/Users/milav/Code/milav-next/latex-templates/gtu-solutions/english-boxes.tex`
- **Gujarati Boxes**: `/Users/milav/Code/milav-next/latex-templates/gtu-solutions/gujarati-boxes.tex`

## 2. CRITICAL RULES (NON-NEGOTIABLE)

### ⛔️ WHAT NOT TO DO

- **NO Mermaid/ASCII**: ALL diagrams must be native **TikZ** or **CircuitikZ**.
- **NO `\texttt`**: Use `\code{}` for inline code.
- **NO Generic Formatting**: Formatting must use the semantic commands below (`\solutionbox`, `\keyword`).

### ✅ STRICT REQUIREMENTS

- **Filenames**: `[Code]-[Season]-[Year]-Solution.tex` (e.g., `4341101-Summer-2024-Solution.tex`).
- **Location**: Same Folder as the Question Paper.
- **Word Counts (Strict Ranges)**:
  - **3 Marks**: 90-115 words
  - **4 Marks**: 115-135 words
  - **7 Marks**: 190-225 words
- **Diagrams**: Every solution needs a diagram or table. Use `gtu block`, `gtu arrow`, `gtu state` TikZ styles.

## 3. THE "ONE TRUTH" TEMPLATE

Follow this structure **EXACTLY**.

```latex
\documentclass{article}
% IMPORTS
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/preamble.tex}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/english-boxes.tex} % OR gujarati-boxes.tex
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/commands.tex}

\title{Subject Name (Code) - Season Year Solution}
\date{Date}

\begin{document}
\maketitle

% QUESTION FORMAT: \questionmarks{Number}{Marks}{Text}
\questionmarks{1(a)}{3}{Explain the difference between compiler and interpreter.}

% SOLUTION BOX
\begin{solutionbox}
    Direct, point-wise explanation starts here. Use full sentences.

    % KEYWORDS
    \begin{itemize}
        \item \keyword{Compiler}: Translates entire code at once.
        \item \keyword{Interpreter}: Translates line by line.
    \end{itemize}

    % TABLE (Preferred for Comparisons)
    \begin{center}
        \captionof{table}{Comparison Table}
        \begin{tabulary}{\linewidth}{|L|L|}
            \hline
            \textbf{Compiler} & \textbf{Interpreter} \\ \hline
            Faster execution & Slower execution \\ \hline
        \end{tabulary}
    \end{center}

    % DIAGRAM (TikZ ONLY)
    \begin{center}
        \begin{tikzpicture}[node distance=1.5cm, auto]
            \node [gtu block] (src) {Source Code};
            \node [gtu block, right=of src] (comp) {Compiler};
            \node [gtu block, right=of comp] (mach) {Machine Code};
            \path [gtu arrow] (src) -- (comp);
            \path [gtu arrow] (comp) -- (mach);
        \end{tikzpicture}
        \captionof{figure}{Compilation Process}
    \end{center}
    
    % CODE SNIPPET (If applicable)
    % Use straight quotes inside!
    \begin{lstlisting}[language=C, caption={Simple Example}]
    #include <stdio.h>
    void main() {
        printf("Hello"); // Straight quotes
    }Create complete paper solution in a single file name: `[subject-code]-[season]-[year]-solution.tex`. e.g. filename - `DI01000051-Summer-2025-Solution.tex`
    \end{lstlisting}
\end{solutionbox}

% MNEMONIC (Optional)
\begin{mnemonicbox}
    \mnemonic{FAST: Faster All-at-once Source Translation}
\end{mnemonicbox}

\end{document}
```

In Each new chat I'll also attach Syllabus of the subject for which we are preparing paper solution, refer this to get the context so that you prepare solutions that adhere to the syllabus.

And final Reminder, This paper solution is for weak students who struggle with exams. So, make sure to not exceed the word limit and keep the content simple and easy to understand.
