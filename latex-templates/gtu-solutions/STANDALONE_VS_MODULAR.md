# GTU LaTeX Solution Templates - Standalone vs Modular

Two versions available: **Modular** (with custom helpers) and **Standalone** (zero dependencies).

## 🎯 Standalone Version (Recommended for Simplicity)

**Files:** `sample_solution_standalone.tex` and `sample_solution_standalone.gu.tex`

### Features
- ✅ **ZERO external files** - Everything in one file
- ✅ **ZERO custom commands** - 100% standard LaTeX  
- ✅ **Minimal packages** - Only essential ones
- ✅ **Default styling** - Clean, professional LaTeX defaults
- ✅ **Perfect conversion** - Pandoc produces clean markdown
- ✅ **Self-contained** - Copy anywhere and compile

### Usage
```bash
# English
pdflatex sample_solution_standalone.tex

# Gujarati  
xelatex sample_solution_standalone.gu.tex

# Convert to markdown
pandoc sample_solution_standalone.tex -o output.md \
  --to=gfm --standalone --shift-heading-level-by=1
```

## 🔧 Modular Version (Advanced)

**Files:** `sample_solution.tex` and `sample_solution.gu.tex` + external files

### Features
- ✅ **Reusable** - Shared preamble and commands
- ✅ **Custom helpers** - `\keyword{}`, `\code{}` shortcuts
- ✅ **Branded styling** - Custom colors for headers
- ⚠️ **Requires 3 external files** per template

## 📊 Comparison

| Feature | Standalone | Modular |
|---------|-----------|---------|
| External files | 0 | 3 |
| Custom commands | 0 | 4 |
| File size | 221 lines | 262 + externals |
| Portability | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| Simplicity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

**Both produce identical markdown output!** Choose based on your needs.
