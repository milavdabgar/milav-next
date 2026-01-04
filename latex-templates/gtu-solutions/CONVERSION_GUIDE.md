# LaTeX to Markdown Conversion Guide

## ✅ Final Workflow

### 1. Write LaTeX with Standard Sectioning

```latex
\title{Subject Name (CODE) - Term Solution}
\author{Your Name}
\date{Date}

\begin{document}
\maketitle

\section{Question 1}

\subsection{Question 1(a) [3 marks]}
\textbf{Question text}

\subsubsection{Solution}
Content here...

\paragraph{Given Data:}
Details...

\paragraph{Step 1: Calculate}
More details...

\begin{quote}
\textbf{Mnemonic:} \emph{Memory aid text}
\end{quote}
```

### 2. Compile to PDF (Standard LaTeX)

```bash
xelatex sample_solution.tex
```

### 3. Convert to Markdown for Web

```bash
# For GitHub/web (with line wrapping)
pandoc sample_solution.tex \
  -o sample_solution.md \
  --to=gfm \
  --standalone \
  --shift-heading-level-by=1

# For Typora/editors (no hard line wrapping)
pandoc sample_solution.tex \
  -o sample_solution.md \
  --to=gfm \
  --wrap=none \
  --standalone \
  --shift-heading-level-by=1
```

**Note:** Use `--wrap=none` to prevent hard line breaks at 80 characters, which causes unnecessary line breaks in Typora and other markdown editors.

## 📊 Heading Mapping

| LaTeX | PDF | Markdown (GFM + shift) |
|-------|-----|------------------------|
| `\title{} + \maketitle` | Title page | YAML `title:` frontmatter |
| `\section{}` | Section | `## Heading` (H2) |
| `\subsection{}` | Subsection | `### Heading` (H3) |
| `\subsubsection{}` | Subsubsection | `#### Heading` (H4) |
| `\paragraph{}` | Paragraph heading | `##### Heading` (H5) |

## ✨ Conversion Results

### YAML Frontmatter
```yaml
---
author:
- Milav Dabgar
date: Month Day, Year
title: Subject Name (SUBJECT001) - Sample Term Solution
---
```

### Clean Hierarchy
```markdown
## Question 1                    (H2)

### Question 1(a) [3 marks]      (H3)

#### Solution                    (H4)

##### Given Data:                (H5)
##### Step 1: Calculate          (H5)

> **Mnemonic:** *Memory aid*     (blockquote with label)
```

### Perfect Tables
```markdown
| **Feature** | **Column 2** | **Column 3** |
|:---|:---|:---|
| Data | More data | Even more |
```

## 🎯 Best Practices

1. **Always use `\maketitle`** - Required for title export to YAML
2. **Standard LaTeX only** - Use `\section`, `\subsection`, `\subsubsection`, `\paragraph`
3. **Label mnemonics clearly** - Use `\textbf{Mnemonic:} \emph{text}` inside `\begin{quote}`
4. **Semantic commands OK** - `\keyword{}` → `**bold**`, `\code{}` → `` `code` ``
5. **Use `tabularx` + `booktabs`** - Converts to perfect GFM pipe tables
6. **Minimal colors** - Only `headcolor` for section titles (optional, for branding)
7. **H1 from CMS** - Your Next.js/Hugo controls H1 from frontmatter

## 🚀 For Production

```bash
# Batch conversion script
for file in *.tex; do
  pandoc "$file" \
    -o "${file%.tex}.md" \
    --to=gfm \
    --standalone \
    --shift-heading-level-by=1
done
```

## 📝 Notes

- ✅ No custom heading commands needed
- ✅ No duplicate title in `\section{}`
- ✅ Clean, semantic LaTeX
- ✅ Perfect web output
- ✅ Single source of truth
