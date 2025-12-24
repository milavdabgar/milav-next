# Download Functionality Documentation

## Overview
This project now includes comprehensive content export functionality copied directly from the studio project, supporting 11 different formats with advanced features like syntax highlighting, math rendering, and diagram conversion.

## Supported Formats

### Text Formats
1. **Markdown (.md)** - Original markdown with frontmatter
2. **Plain Text (.txt)** - Clean text without formatting
3. **HTML (.html)** - Standalone HTML with embedded styles

### Document Formats
4. **PDF (Puppeteer)** - High-quality PDF with full rendering
5. **PDF (Chrome)** - Chrome headless fallback option
6. **PDF (Pandoc/XeLaTeX)** - Professional LaTeX-based PDF
7. **RTF (.rtf)** - Rich Text Format for word processors
8. **DOCX (.docx)** - Microsoft Word format
9. **ODT (.odt)** - OpenDocument Text (LibreOffice/OpenOffice)

### Academic & E-book Formats
10. **LaTeX (.tex)** - LaTeX typesetting format
11. **EPUB (.epub)** - E-book format for e-readers

## Dependencies Installed

### NPM Packages (Already Installed)
- `puppeteer` (^24.10.2) - PDF generation via browser automation
- `katex` (^0.16.22) - Math equation rendering
- `marked` (^12.0.2) - Markdown parsing
- `shiki` (^1.26.1) - Syntax highlighting with dual themes
- `gray-matter` (^4.0.3) - Frontmatter parsing

### System Requirements for Full Functionality

#### For PDF via Pandoc/XeLaTeX (Best Quality PDFs)
```bash
# macOS
brew install pandoc
brew install --cask mactex  # Full TeX distribution

# Or minimal TeX:
brew install basictex
sudo tlmgr update --self
sudo tlmgr install xelatex latex-bin
```

#### For DOCX, ODT, EPUB, LaTeX Conversion
```bash
# Pandoc is required (already installed above)
# Verify installation:
pandoc --version
```

## Features

### 1. Syntax Highlighting
- Uses Shiki for code blocks
- Dual theme support (light/dark)
- Supports 100+ languages

### 2. Math Rendering
- KaTeX for inline and display math
- LaTeX math syntax support
- High-quality mathematical typesetting

### 3. Diagram Support
- Mermaid diagrams converted to images
- SVG diagram embedding
- ASCII art preservation

### 4. Professional PDF Templates
- Custom LaTeX templates
- Professional formatting
- Table of contents generation
- Proper typography and margins

## Usage

### From Blog Posts
Click the "Download" button on any blog post and select your desired format:

```typescript
// The component automatically loads available formats
<BlogDownload title="Article Title" slug="article-slug" />
```

### API Usage
```typescript
// POST /api/download
{
  "slug": "blog-post-slug",
  "locale": "en",  // or "gu" for Gujarati
  "format": "pdf-pandoc",  // any supported format
  "options": {
    "title": "Custom Title",
    "author": "Author Name"
  }
}
```

## Format-Specific Notes

### PDF Formats

**PDF (Puppeteer)** - Default, Best for:
- Content with images
- Mermaid diagrams
- Web-style rendering
- Quick generation

**PDF (Pandoc/XeLaTeX)** - Best for:
- Academic papers
- Professional documents
- Mathematical content
- Print-quality output
- Requires: Pandoc + XeLaTeX installation

**PDF (Chrome)** - Fallback for:
- Systems without Puppeteer
- Lightweight environments
- Basic PDF needs

### Word Processor Formats

**DOCX** - Best for:
- Microsoft Word editing
- Corporate documents
- Maximum compatibility
- Requires: Pandoc

**ODT** - Best for:
- LibreOffice/OpenOffice
- Open-source workflows
- Cross-platform editing
- Requires: Pandoc

**RTF** - Best for:
- Universal compatibility
- Legacy systems
- Basic formatting needs

### E-book & Academic

**EPUB** - Best for:
- E-readers (Kindle, etc.)
- Mobile reading
- Reflowable content
- Requires: Pandoc

**LaTeX** - Best for:
- Academic publishing
- Further LaTeX customization
- Journal submissions

## Testing Checklist

- [x] Install dependencies (npm install)
- [ ] Test Markdown download
- [ ] Test HTML download
- [ ] Test Plain Text download
- [ ] Test PDF (Puppeteer) - Should work out of box
- [ ] Install Pandoc + XeLaTeX
- [ ] Test PDF (Pandoc/XeLaTeX)
- [ ] Test DOCX conversion
- [ ] Test ODT conversion
- [ ] Test EPUB generation
- [ ] Test LaTeX export
- [ ] Test with Gujarati content
- [ ] Test with code blocks
- [ ] Test with math equations
- [ ] Test with Mermaid diagrams

## Troubleshooting

### Puppeteer Issues
```bash
# If Puppeteer fails to install:
npm install puppeteer --legacy-peer-deps

# Or use system Chrome:
PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true npm install puppeteer
```

### Pandoc Issues
```bash
# Verify Pandoc is in PATH:
which pandoc
pandoc --version

# For XeLaTeX:
which xelatex
xelatex --version
```

### Memory Issues
Large documents with many diagrams may require:
```bash
export NODE_OPTIONS="--max-old-space-size=4096"
npm run dev
```

## Implementation Details

### ContentConverterV2 Class
- Location: `lib/content-converter-v2.ts`
- Size: ~2300 lines
- Source: Copied from studio project (tested and working)
- Features: Complete conversion pipeline with error handling

### Content Types Utilities
- `lib/content-types.ts` - Server-side detection
- `lib/content-types-client.ts` - Client-safe utilities
- Auto-detects Slidev presentations, markdown, etc.

### Download API Route
- Location: `app/api/download/route.ts`
- Methods:
  - `POST /api/download` - Convert and download content
  - `GET /api/download?action=supported-formats` - List formats

## Future Enhancements

Possible additions:
- [ ] PPTX (PowerPoint) generation
- [ ] Batch download multiple posts
- [ ] Custom PDF templates
- [ ] Watermark support
- [ ] Password-protected PDFs
- [ ] Archive (ZIP) of all formats

## Credits

This implementation is based on the working code from the studio project, which has been battle-tested with hundreds of downloads across multiple content types.
