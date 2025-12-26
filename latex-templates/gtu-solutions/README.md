# GTU Solutions LaTeX Standards & Best Practices

## 📚 Overview
This document defines professional LaTeX standards for GTU exam solutions and technical books. Following these guidelines ensures consistency, maintainability, and professional quality across 100+ solution documents.

---

## ✅ Current Professional Features

### 1. **Document Structure**
```latex
\documentclass{article}
\input{path/to/preamble.tex}
\input{path/to/english-boxes.tex}

\title{Subject Name (Code) - Exam Term Solution}
\date{Month Day, Year}

\begin{document}
\maketitle
% Content here
\end{document}
```

### 2. **PDF Metadata** ✓
- Author, subject, keywords automatically set
- Bookmarks enabled for navigation
- Proper hyperlinks (blue, clickable)

### 3. **Code Listings** ✓
- Natural page breaks (no wasted space)
- Syntax highlighting
- Line numbers
- Captions with automatic numbering
- Proper frames

### 4. **Global TikZ Styles** ✓
Use predefined styles for consistency:
```latex
\begin{tikzpicture}
  \node [gtu block] (name) {Text};
  \node [gtu class] (name) {Class};
  \node [gtu interface] (name) {Interface};
  \path [gtu arrow] (a) -- (b);
\end{tikzpicture}
```

### 5. **Color Scheme** ✓
- `headcolor` - Section headings (blue)
- `solutioncolor` - Solution boxes (green)
- `mnemoniccolor` - Mnemonic boxes (purple)
- `keycolor` - Key formulas (crimson)
- `codecolor` - Code elements (dark blue)

### 6. **Breakable Boxes** ✓
All tcolorbox environments can split across pages naturally.

---

## 📋 Professional Standards Checklist

### ✅ **IMPLEMENTED**
- [x] Consistent color scheme
- [x] Global TikZ styles
- [x] PDF metadata and bookmarks
- [x] Professional code listings with captions
- [x] Breakable boxes for long content
- [x] Proper hyperref configuration
- [x] Spacing variables
- [x] Author attribution

### 🔄 **RECOMMENDED FOR FUTURE** (Optional Enhancements)

#### Tables & Figures
**Current**: Using `\captionof` inside `center` environment
**Better**: Use proper `table` and `figure` environments

```latex
% Current (works, but not ideal)
\begin{center}
\captionof{table}{Title}
\begin{tabular}...
\end{tabular}
\end{center}

% Professional (for books)
\begin{table}[htbp]
\centering
\caption{Title}
\label{tab:mytable}
\begin{tabular}...
\end{tabular}
\end{table}
```

**Benefits**: Enables List of Tables, better positioning, cross-references

#### Cross-References
Add `\label{}` and use `\ref{}` for professional citations:
```latex
\caption{JVM Architecture}
\label{fig:jvm}

% Later in text:
As shown in Figure~\ref{fig:jvm}...
```

#### Semantic Commands
Use the provided `commands.tex` for consistency:
```latex
\question{1(a) [3 marks]}{Explain garbage collection}
\keyword{Garbage Collection}
\code{System.gc()}
\mnemonic{MSC: Mark-Sweep-Compact}
```

---

## 🎯 Usage Guidelines

### For GTU Solutions (Current Use)
**Keep it simple**: Current format is perfect for exam solutions
- Fast to write
- Clean output
- No unnecessary complexity

### For Books (Future Use)
**Add enhancements**:
1. Load `commands.tex` in preamble
2. Use `table` and `figure` environments
3. Add `\label{}` and `\ref{}`
4. Consider adding bibliography with `biblatex`
5. Use semantic commands for consistency

---

## 📝 Quick Reference

### Question Formatting
```latex
\section*{Question 1(a) [3 marks]}
\textbf{Question text here}
```

### Solution Box
```latex
\begin{solutionbox}
Content here...
\end{solutionbox}
```

### Mnemonic Box
```latex
\begin{mnemonicbox}
``Mnemonic text here''
\end{mnemonicbox}
```

### Code Listing
```latex
\begin{lstlisting}[language=Java,caption={Description}]
// Code here
\end{lstlisting}
```

### Tables
```latex
\begin{center}
\captionof{table}{Table Title}
\begin{tabular}{|l|l|}
\hline
Header 1 & Header 2 \\ \hline
Data 1 & Data 2 \\ \hline
\end{tabular}
\end{center}
```

### TikZ Diagrams
```latex
\begin{center}
\captionof{figure}{Diagram Title}
\begin{tikzpicture}
  \node [gtu block] (a) {Block A};
  \node [gtu block, right=1cm of a] (b) {Block B};
  \path [gtu arrow] (a) -- (b);
\end{tikzpicture}
\end{center}
```

---

## 🚀 Compilation

```bash
xelatex document.tex
xelatex document.tex  # Run twice for references
```

---

## 📖 Package Loading Order (Important!)

1. Geometry, basic packages
2. Graphics packages (tikz, pgfplots)
3. Table packages
4. **Hyperref (LAST)**
5. Cleveref (if used, after hyperref)

**Why**: Hyperref modifies many commands, so it should load last.

---

## ✨ Professional Tips

1. **Consistency**: Use the same structure across all documents
2. **Comments**: Add comments for complex TikZ diagrams
3. **Spacing**: Use `\gtuspacing` variable instead of hardcoded values
4. **Colors**: Use defined colors, don't define new ones inline
5. **Styles**: Use global TikZ styles, don't redefine locally
6. **Captions**: Always caption tables and figures
7. **Line breaks**: Let LaTeX handle them, don't force with `\\`
8. **Quotes**: Use `` `text' `` not `"text"`

---

## 🔧 Troubleshooting

### "Overfull hbox" warnings
- Usually from long code lines
- Already handled with `breaklines=true`
- Safe to ignore if output looks good

### "hypcap=true ignored" warnings
- Normal when using `\captionof`
- Doesn't affect output quality
- Can be safely ignored

### Compilation errors
1. Check for unmatched braces `{}`
2. Verify all environments are closed
3. Run `xelatex` twice for references
4. Check for special characters needing escaping

---

## 📚 For Book Production

When converting these solutions to a book:

1. **Add front matter**:
   ```latex
   \frontmatter
   \tableofcontents
   \listoffigures
   \listoftables
   ```

2. **Use chapters**:
   ```latex
   \chapter{Java Programming}
   \section{Garbage Collection}
   ```

3. **Add index**:
   ```latex
   \usepackage{makeidx}
   \makeindex
   % In text: \index{Garbage Collection}
   \printindex
   ```

4. **Bibliography**:
   ```latex
   \usepackage[style=numeric]{biblatex}
   \addbibresource{references.bib}
   \printbibliography
   ```

---

## 📄 File Structure

```
latex-templates/gtu-solutions/
├── preamble.tex          # Main configuration
├── english-boxes.tex     # Box environments
└── commands.tex          # Semantic commands (optional)

content/.../solution.tex  # Individual solution files
```

---

## ✅ Quality Checklist Before Publishing

- [ ] All code listings have captions
- [ ] All tables have captions
- [ ] All diagrams have captions
- [ ] No hardcoded spacing (use variables)
- [ ] Consistent TikZ styles used
- [ ] PDF compiles without errors
- [ ] Hyperlinks work correctly
- [ ] Bookmarks are properly structured
- [ ] Author and metadata are set
- [ ] No orphaned text or awkward breaks

---

**Version**: 1.0  
**Last Updated**: December 26, 2024  
**Maintained by**: Milav Dabgar
