---
title: "GTU LaTeX Solution Generator - Workflow Long"
description: "Complete workflow with logical sequence for LLM execution"
date: 2026-01-04
---

# GTU LaTeX Solution Generator - Detailed Guide

**INPUT**: Question paper (markdown format)  
**OUTPUT**: Complete LaTeX solution files (English `.tex` + Gujarati `.gu.tex`)

---

## PART 1: Reference & Context

### What You're Creating

Two complete LaTeX solution files for GTU exam papers:

- **English version**: `[Code]-[Season]-[Year]-Solution-Full.tex`
- **Gujarati version**: `[Code]-[Season]-[Year]-Solution-Full.gu.tex`

Both files must have:

- **Identical structure** (same line counts, same sectioning at same line numbers)
- **Identical technical content** (code, math, diagrams 100% same)
- **Different languages** (only descriptive text translated)

### Reference Files (Your Specification)

**Study these files carefully - they show EXACTLY what to generate:**

```
/Users/milav/Code/milav-next/latex-templates/gtu-solutions/
├── sample_solution.tex       # English reference (332 lines)
├── sample_solution.gu.tex    # Gujarati reference (332 lines)
├── preamble.tex              # English preamble
└── preamble.gu.tex           # Gujarati preamble
```

**These files demonstrate all patterns you need to follow.**

---

## PART 2: Complete Specifications

### Document Structure Template

```latex
%% METADATA (Required at top)
%% subject-code: SUBJECT001
%% subject-name: Subject Name
%% semester: 1
%% examination: Summer-2025
%% date: 01-01-2025
%% description: Solution guide for [subject]
%% summary: Complete solutions with detailed explanations
%% tags: study-material, solutions, gtu, [code]
%% END METADATA

\documentclass{article}
\input{/Users/milav/Code/milav-next/latex-templates/gtu-solutions/preamble.tex}

\title{Subject Name (CODE) - Term Year Solution}
\date{Month Day, Year}

% PDF Metadata
\hypersetup{
  pdftitle={Subject Name (CODE) - Term Year Solution},
  pdfsubject={GTU Exam Solution - Term-Year},
  pdfauthor={Milav Dabgar},
  pdfkeywords={study-material, solutions, gtu, code},
  pdfcreator={xelatex}  % or XeLaTeX for Gujarati
}

\begin{document}
\maketitle

% Table of Contents (REQUIRED)
\setcounter{tocdepth}{5}
\tableofcontents
\newpage

% ========================================
% Solutions start here
% ========================================

\section{Question 1}

\subsection{Question 1(a) [3 marks]}
\textbf{Question statement here.}

\subsubsection{Solution}
Solution content here...

\paragraph{Mnemonic:}
\emph{Memory trick here...}

% ... more questions ...

\end{document}
```

### Critical LaTeX Conventions (MUST FOLLOW)

#### 1. Math Notation

```latex
✅ CORRECT:
\(inline math\)          
\[display math\]         

❌ WRONG:
$inline$                 % NEVER use $
$$display$$              % NEVER use $$
```

#### 2. Complete Hierarchy (All 5 Levels Required)

```latex
\section{Question 1}                           % H1: Main question

\subsection{Question 1(a) [3 marks]}          % H2: Sub-question + marks
\textbf{Write a Java program...}              % Bold question (separate line)

\subsubsection{Solution}                       % H3: Solution heading

\paragraph{Given Data:}                        % H4: Major subsections
\begin{itemize}
    \item Data here
\end{itemize}

\paragraph{Step 1: Initialize Variables}       % H4: Steps
Code or explanation here...

\subparagraph{Optimization Note:}             % H5: Nested details
Additional context when needed...

\paragraph{Mnemonic:}                          % H4: Required ending
\emph{Memory trick here...}
```

#### 3. Semantic Lists

```latex
% Description lists: for labeled items
\paragraph{Key Points:}
\begin{description}
    \item[Label:] Explanation...
    \item[Another:] More detail...
\end{description}

% Itemize: for bullet points
\paragraph{Given Data:}
\begin{itemize}
    \item Point one
    \item Point two
\end{itemize}

% Enumerate: for numbered steps
\paragraph{Algorithm Steps:}
\begin{enumerate}
    \item First step
    \item Second step
\end{enumerate}
```

#### 4. Tables (Caption at TOP)

```latex
\begin{table}[H]
\centering
\caption{Comparison of BJT and FET}
\begin{tabularx}{\textwidth}{lXX}
\toprule
\textbf{Parameter} & \textbf{BJT} & \textbf{FET} \\
\midrule
Type & Current-controlled & Voltage-controlled \\
Input Impedance & Low & High \\
\bottomrule
\end{tabularx}
\end{table}
```

**CRITICAL**: 

- Use `\begin{tabularx}{\textwidth}{lXX}` (NOT `tabular`)
- Use `[H]` placement
- Caption BEFORE tabularx

#### 5. Figures (Caption at BOTTOM)

```latex
\begin{figure}[H]
\centering
\begin{circuitikz}
    % Circuit/diagram code here
\end{circuitikz}
\caption{Half-Wave Rectifier Circuit}
\end{figure}
```

**CRITICAL**: 

- Use `[H]` placement
- Caption AFTER diagram

#### 6. Code Listings (NO paragraph before)

```latex
❌ WRONG:
\paragraph{Java Program:}
\begin{lstlisting}[language=Java,caption={...}]
code here
\end{lstlisting}

✅ CORRECT:
\begin{lstlisting}[language=Java,caption={Find Maximum of Three Numbers}]
public class MaxOfThree {
    public static void main(String[] args) {
        int a = 25, b = 40, c = 15;
        int max = a;
        
        if (b > max) {
            max = b;
        }
        if (c > max) {
            max = c;
        }
        
        System.out.println("Maximum: " + max);
    }
}
\end{lstlisting}
```

**CRITICAL**: The `caption` parameter provides the heading. Never add `\paragraph` before code.

#### 7. Typography

- **Text**: Use smart quotes: `` ``double'' `` and `` `single' ``
- **Code**: Use straight quotes: `"string"` inside lstlisting
- **Emphasis**: Use `\textbf{bold}`, `\texttt{code}`, `\emph{emphasis}`
- **NO custom commands**: Don't create `\keyword{}`, `\code{}`, etc.

#### 8. Comments (Must be identical in both files)

```latex
% ========================================
% QUESTION 1(a): Programming Code (3 marks)
% Demonstrates: lstlisting for code, straight quotes in code, ~100 words
% ========================================
```

### Content Requirements by Marks

| Marks       | Word Count | Structure Required |
|-------------|------------|--------------------|
| **3 marks** | 90-150     | Explanation + (Code OR Diagram OR Table) + Mnemonic |
| **4 marks** | 120-180    | Detailed explanation + (Code OR Diagram OR Calculation) + Mnemonic |
| **7 marks** | 200-300    | Comprehensive explanation + (Code OR Diagram OR Calculation) + Mnemonic |

**Target word counts** (aim for middle of range):

- 3 marks → 120 words
- 4 marks → 150 words  
- 7 marks → 250 words

### Gujarati Translation Rules

#### Translation Strategy

1. **Translate**: Descriptive text, explanations, list items
2. **Keep English**: Acronyms (HTML, CSS, JavaScript, BJT, FET, MOSFET, IC, SCR, PIV)
3. **Transliterate**: Common technical terms (Java → જાવા, Resistor → રેઝિસ્ટર)

#### Preservation Rules (100% Identical)

4. **Code blocks**: NO translation in `\begin{lstlisting}...\end{lstlisting}`
5. **Math expressions**: NO translation in `\(...\)` and `\[...\]`
6. **Diagrams**: NO translation in TikZ/CircuiTikZ/karnaugh-map code
7. **Comments**: Keep exact same comments including section separators

#### Structure Rules (Perfect Fidelity)

8. **Same line count**: Gujarati MUST have exactly same number of lines as English
9. **Same sectioning**: All `\section`, `\subsection`, `\subsubsection`, `\paragraph`, `\subparagraph` at same line numbers
10. **Same elements**: Identical count of paragraphs, lists, tables, figures
11. **Same flow**: Maintain exact same sequence and structure

#### Technical Setup

- Use `\input{.../preamble.gu.tex}` (includes Gujarati font setup)
- Compile with `xelatex` (NOT `xelatex`)
- PDF metadata: Add `(Gujarati)` to title, add `gujarati` to keywords

---

## PART 3: Workflow Execution

### Step 1: Initialization

Create both files simultaneously:

**English file**: `[Code]-[Season]-[Year]-Solution-Full.tex`
**Gujarati file**: `[Code]-[Season]-[Year]-Solution-Full.gu.tex`

Add to both:

1. Metadata block (see template above)
2. `\documentclass{article}`
3. Preamble input (`.tex` for English, `.gu.tex` for Gujarati)
4. Title, date, PDF metadata
5. `\begin{document}`, `\maketitle`
6. TOC setup: `\setcounter{tocdepth}{5}`, `\tableofcontents`, `\newpage`
7. **DO NOT add `\end{document}` yet**

### Step 2: Generate Question 1 (Foundation)

**Generate both English and Gujarati Q1 simultaneously in ONE step.**

For Question 1 with parts (a), (b), (c), (OR):

1. **Start with section comment block**:

```latex
% ========================================
% QUESTION 1(a): [Brief description] ([X] marks)
% Demonstrates: [key features shown]
% ========================================
```

2. **Add section and subsection**:

```latex
\section{Question 1}

\subsection{Question 1(a) [3 marks]}
\textbf{[Question statement]}
```

3. **Add solution with complete hierarchy**:

```latex
\subsubsection{Solution}
[Introduction paragraph explaining approach]

\paragraph{Given Data:}
\begin{itemize}
    \item [data point]
\end{itemize}

\paragraph{[Key concept]:}
[Explanation...]

[Code OR Diagram OR Table OR Calculation]

\paragraph{Mnemonic:}
\emph{[Memory trick]}
```

4. **Repeat for all parts** (b, c, OR if applicable)

5. **Ensure Gujarati version**:
   - Same structure exactly
   - Comments identical (including English technical terms)
   - Code/Math/Diagrams 100% identical
   - Only descriptive text translated

### Step 3: Compile & Verify Q1

**Compile both files**:

```bash
xelatex [Code]-[Season]-[Year]-Solution-Full.tex
xelatex [Code]-[Season]-[Year]-Solution-Full.gu.tex
```

**Run verification script**:

```bash
python content/resources/study-materials/00-general/sem-1/DI01000051-fe/verify_solutions.py \
  [english-file.tex] [gujarati-file.gu.tex]
```

**CRITICAL**: Must see `✅ PASSED` before proceeding to Q2.

**If verification fails**:

1. Read error messages carefully
2. Fix ALL identified issues
3. Recompile both files
4. Re-run verification
5. Repeat until `✅ PASSED`

**Key checks verified**:

- ✅ Line counts match exactly
- ✅ All sectioning commands at same line numbers
- ✅ All tables/figures/listings have captions
- ✅ Code/Math/Diagrams 100% identical
- ✅ No `$`, `**`, straight quotes in text
- ✅ Solution structure uses only `\paragraph`/`\subparagraph`
- ✅ Both files compile successfully

**DO NOT proceed to Q2 until Q1 verification passes.**

### Step 4: Iterative Append (Q2, Q3, Q4, Q5)

For each remaining question:

1. **Generate both En & Gu simultaneously** (entire question with all parts)
2. **Append to respective files**
3. **Compile both files** (check for errors)
4. **Run verification script**
5. **Fix any issues immediately**
6. **Re-verify until `✅ PASSED`**
7. **Only then proceed to next question**

**Pattern for each question**:

- Add section comment block
- Add `\section{Question X}`
- Add subsections for each part
- Follow same hierarchy as Q1
- Maintain word count targets
- End each part with mnemonic

### Step 5: Finalization

1. **Add to both files**: `\end{document}`

2. **Final compilation** (run TWICE for TOC):

```bash
xelatex [file].tex
xelatex [file].tex
xelatex [file].gu.tex
xelatex [file].gu.tex
```

3. **Final verification**:

```bash
python verify_solutions.py [english-file.tex] [gujarati-file.gu.tex]
```

**Must achieve**:

- `✅ PASSED` status
- All 53 checks passing
- Both PDFs generated successfully
- TOC shows all 5 hierarchy levels

4. **Output**: Two complete, verified PDF files ready for distribution

---

## PART 4: Verification Details

### What verify_solutions.py Checks (53 checks)

**8 Categories of checks**:

1. **Core Structure**: Line counts match, TOC hierarchy identical
2. **Document Metadata**: Complete structure, PDF metadata, correct preambles with absolute paths
3. **Syntax Compliance**: No `$`, `**`, straight quotes; proper hierarchy; no deprecated commands
4. **Content Quality**: Word counts match marks, proper typography, mnemonics present
5. **Content Fidelity**: Code/Math/Diagrams 100% identical, list/table/figure parity, **sectioning alignment**
6. **Structural Validation**: TOC setup, question patterns, section numbering, all 5 levels, semantic lists
7. **Format Standards**: Tables use `tabularx`, figures use `[H]`, **solutions use only `\paragraph`/`\subparagraph`**
8. **Compilation**: Both files compile successfully

**Critical checks** (26 checks - must pass):

- Line counts, sectioning alignment, compilation, syntax, structure hierarchy, preambles, TOC, content compliance, custom commands, caption presence, solution structure

**Warning checks** (27 checks - informational):

- Word counts, typography, marks format, mnemonics, caption positions, filename conventions, etc.

### When to Verify

**Mandatory verification points**:

1. After generating Q1 (before Q2)
2. After adding Q2 (before Q3)
3. After adding Q3 (before Q4)
4. After adding Q4 (before Q5)
5. After adding Q5 (before finalization)
6. After finalization (final check)

### Troubleshooting Verification Failures

**Common issues and fixes**:

1. **Line count mismatch**: 
   - Check for missing/extra comments
   - Ensure comment blocks identical in both files
   - Check for extra blank lines

2. **Sectioning alignment mismatch**:
   - Verify all `\section`, `\subsection`, etc. at same line numbers
   - Check comment blocks have same number of lines
   - Ensure no missing sections

3. **Caption missing**:
   - Add `\caption{}` to all tables
   - Add `\caption{}` to all figures
   - Add `caption={}` parameter to all `\begin{lstlisting}`

4. **Code/Math/Diagram differences**:
   - Ensure 100% identical (including comments)
   - No translation in technical content
   - Check for typos or missing characters

5. **Forbidden syntax**:
   - Replace `$...$` with `\(...\)`
   - Replace `$$...$$` with `\[...\]`
   - Remove `**bold**` (use `\textbf{}`)
   - Replace straight quotes in text with smart quotes

6. **Solution structure violation**:
   - Inside `\subsubsection{Solution}...\paragraph{Mnemonic}`, use ONLY `\paragraph` and `\subparagraph`
   - Do NOT use `\section`, `\subsection`, or `\subsubsection` inside solutions

---

## Quick Reference Card

### Generation Checklist (For Each Question)

- [ ] Comment block with question description
- [ ] `\section{Question X}`
- [ ] `\subsection{Question X(y) [Z marks]}`
- [ ] `\textbf{Question statement}` (separate line)
- [ ] `\subsubsection{Solution}`
- [ ] Introduction paragraph
- [ ] `\paragraph{}` sections as needed
- [ ] `\subparagraph{}` for nested details (if needed)
- [ ] Code OR Diagram OR Table OR Calculation
- [ ] `\paragraph{Mnemonic:}` with `\emph{}` content
- [ ] Word count meets target (120/150/250)
- [ ] All math uses `\(...\)` or `\[...\]`
- [ ] All lists are semantic (description/itemize/enumerate)
- [ ] No `\paragraph` before code listings
- [ ] Gujarati version identical structure
- [ ] Comments identical in both files

### Verification Checklist

- [ ] `xelatex` compiles English successfully
- [ ] `xelatex` compiles Gujarati successfully
- [ ] `verify_solutions.py` shows `✅ PASSED`
- [ ] Line counts match exactly
- [ ] All sectioning aligned at same line numbers
- [ ] Both PDFs generated
- [ ] TOC shows all 5 levels
- [ ] No error messages in verification output

---

## Success Criteria

**You have successfully completed the task when**:

1. Both `.tex` files exist with same line count
2. Both PDFs compile successfully (run twice each)
3. `verify_solutions.py` shows `✅ PASSED` status
4. All 5 questions (Q1-Q5) are complete with all parts
5. Every question part has all required elements
6. Word counts are within acceptable ranges
7. Technical content is 100% identical between versions
8. Gujarati translations are natural and accurate
9. No compilation errors or warnings (except cosmetic TikZ)
10. Files follow all conventions from reference samples

**Final deliverables**:

- `[Code]-[Season]-[Year]-Solution-Full.tex` (English)
- `[Code]-[Season]-[Year]-Solution-Full.gu.tex` (Gujarati)
- `[Code]-[Season]-[Year]-Solution-Full.pdf` (English)
- `[Code]-[Season]-[Year]-Solution-Full.gu.pdf` (Gujarati)
