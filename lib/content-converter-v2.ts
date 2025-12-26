/**
 * Enhanced Content Converter v2 - Based on working pdf-converter.js
 * Supports multiple output formats with robust Mermaid and math rendering
 */

import fs from 'fs';
import path from 'path';
import { marked } from 'marked';
import matter from 'gray-matter';
import { exec } from 'child_process';
import { promisify } from 'util';
import { codeToHtml, BundledLanguage } from 'shiki';

const execAsync = promisify(exec);

// Import Puppeteer for PDF generation
interface PuppeteerBrowser {
    newPage: () => Promise<{
        setViewport: (options: { width: number; height: number; deviceScaleFactor: number }) => Promise<void>;
        evaluateOnNewDocument: (fn: () => void) => Promise<void>;
        setContent: (html: string, options?: { waitUntil?: string; timeout?: number }) => Promise<void>;
        evaluateHandle: (script: string) => Promise<unknown>;
        evaluate: (fn: () => Promise<void>) => Promise<void>;
        pdf: (options: Record<string, unknown>) => Promise<Buffer>;
    }>;
    close: () => Promise<void>;
}

interface PuppeteerInstance {
    launch: (options?: Record<string, unknown>) => Promise<PuppeteerBrowser>;
}

let puppeteer: PuppeteerInstance | null = null;
interface ChromiumInstance {
    executablePath: (path: string) => Promise<string>;
    args: string[];
    defaultViewport: Record<string, unknown>;
}

let chromium: ChromiumInstance | null = null;
try {
    puppeteer = require('puppeteer');
    // For production environments, also try chromium
    try {
        // @ts-ignore - Optional dependency for production
        chromium = eval("require('@sparticuz/chromium-min')");
    } catch {
        // Chromium package is optional
    }
} catch {
    console.log('Puppeteer not available, PDF generation will use Chrome headless fallback');
}

// Import KaTeX for math rendering
interface KatexInstance {
    renderToString: (math: string, options?: {
        displayMode?: boolean;
        throwOnError?: boolean;
        strict?: boolean;
    }) => string;
}

let katex: KatexInstance | null = null;
try {
    katex = require('katex');
} catch {
    console.log('KaTeX not available, math rendering will be limited');
}

interface ConversionOptions {
    title?: string;
    author?: string;
    language?: string;
    includeStyles?: boolean;
    contentPath?: string;  // Path to the content file for resolving relative paths
    pdfEngine?: 'puppeteer' | 'chrome';  // Choose PDF generation engine
    pdfOptions?: {
        format?: 'A4' | 'Letter';
        margin?: {
            top?: string;
            right?: string;
            bottom?: string;
            left?: string;
        };
        waitForNetwork?: boolean;  // Wait for network requests to complete
        timeout?: number;          // Timeout for PDF generation
    };
}

export class ContentConverterV2 {
    private tempDir: string;

    constructor() {
        this.tempDir = path.resolve(process.cwd(), 'tmp');
        this.ensureDirectoryExists(this.tempDir);
    }

    private async processCodeBlocks(content: string): Promise<string> {
        // Enhanced code block processing with Shiki syntax highlighting
        const codeBlockRegex = /```(\w+)?\n([\s\S]*?)```/g;

        const processCodeBlock = async (match: string, language: string = '', code: string): Promise<string> => {
            try {
                // Skip Mermaid diagrams - they will be processed separately
                if (language && language.toLowerCase() === 'mermaid') {
                    return match; // Return original Mermaid block unchanged
                }

                // Handle special cases that Shiki doesn't support
                const unsupportedLanguages = ['goat', 'ascii', 'diagram', 'text', 'plain', 'assembly', 'asm', 'x86', 'arm', 'nasm', 'masm'];

                if (!language || unsupportedLanguages.includes(language.toLowerCase())) {
                    // For ASCII diagrams and plain text, render without syntax highlighting
                    const escapedCode = code
                        .replace(/&/g, '&amp;')
                        .replace(/</g, '&lt;')
                        .replace(/>/g, '&gt;');

                    const cssClass = language === 'goat' ? 'goat-diagram' : 'plain-text';
                    return `<pre class="${cssClass}"><code>${escapedCode}</code></pre>`;
                }

                // Handle language aliases
                let actualLanguage = language;
                if (language === 'yml') {
                    actualLanguage = 'yaml';
                }

                // Generate syntax highlighted HTML with dual theme support
                const html = await codeToHtml(code, {
                    lang: actualLanguage as BundledLanguage,
                    themes: {
                        light: 'catppuccin-latte',
                        dark: 'one-dark-pro'
                    },
                    defaultColor: false
                });

                return html;
            } catch (error) {
                if (process.env.NODE_ENV !== 'test') {
                    console.error('Error highlighting code for language:', language, error);
                }
                // Fallback to plain text with basic HTML escaping
                const escapedCode = code
                    .replace(/&/g, '&amp;')
                    .replace(/</g, '&lt;')
                    .replace(/>/g, '&gt;');
                return `<pre class="plain-text"><code>${escapedCode}</code></pre>`;
            }
        };

        // Process all code blocks
        const matches = Array.from(content.matchAll(codeBlockRegex));
        let processedContent = content;

        // Process in reverse order to maintain string positions
        for (let i = matches.length - 1; i >= 0; i--) {
            const match = matches[i];
            const [fullMatch, language, code] = match;
            const startIndex = match.index!;
            const endIndex = startIndex + fullMatch.length;

            const highlightedCode = await processCodeBlock(fullMatch, language, code);

            processedContent = processedContent.slice(0, startIndex) +
                highlightedCode +
                processedContent.slice(endIndex);
        }

        return processedContent;
    }

    /**
     * Convert Slidev content to various formats
     * Note: For full Slidev presentations, use the native Slidev build process
     * This method provides basic conversion for export/download functionality
     */
    async convertSlidev(slidevContent: string, format: string, options: ConversionOptions = {}): Promise<Buffer | string> {
        // Parse Slidev content manually (simplified version)
        const presentation = this.parseSlidevContentBasic(slidevContent);

        switch (format) {
            case 'md':
                return slidevContent;

            case 'html':
                return await this.convertSlidevToHtml(presentation, options);

            case 'pdf':
                return await this.convertSlidevToPdf(presentation, options);

            case 'pptx':
                return await this.convertSlidevToPptx(presentation, options);

            case 'txt':
                return this.convertSlidevToPlainText(presentation, options);

            default:
                // For other formats, convert to plain markdown first
                const markdownContent = this.convertSlidevToMarkdown(presentation);
                const { data: frontmatter, content } = matter(markdownContent);
                return await this.convert(markdownContent, format, options);
        }
    }

    /**
     * Basic Slidev content parser (simplified version for export functionality)
     */
    private parseSlidevContentBasic(content: string) {
        const { data: frontmatter, content: body } = matter(content);

        // Split slides by --- separator
        const slides = body.split('\n---\n').map((slideContent, index) => {
            // Extract layout from slide content if present
            const layoutMatch = slideContent.match(/^layout:\s*(.+)$/m);
            const layout = layoutMatch ? layoutMatch[1] : 'default';

            // Remove layout line from content
            const cleanContent = slideContent.replace(/^layout:\s*.+$/m, '').trim();

            return {
                content: cleanContent,
                layout,
                index
            };
        });

        return {
            frontmatter,
            slides,
            totalSlides: slides.length
        };
    }

    /**
     * Convert Slidev presentation to HTML
     */
    private async convertSlidevToHtml(presentation: any, options: ConversionOptions): Promise<string> {
        const slides = presentation.slides.map((slide: any, index: number) => {
            return `
                <section class="slide slide-${index + 1}" data-layout="${slide.layout || 'default'}">
                    <div class="slide-content">
                        ${marked(slide.content)}
                    </div>
                    <div class="slide-footer">
                        <span class="slide-number">${index + 1} / ${presentation.totalSlides}</span>
                    </div>
                </section>
            `;
        }).join('\n');

        const title = presentation.title || options.title || 'Slidev Presentation';
        const theme = presentation.theme || 'default';

        return `
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>${title}</title>
                <style>
                    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; padding: 0; }
                    .slide { width: 100vw; height: 100vh; padding: 2rem; box-sizing: border-box; display: flex; flex-direction: column; page-break-after: always; }
                    .slide-content { flex: 1; overflow-y: auto; }
                    .slide-footer { padding: 1rem 0; text-align: right; font-size: 0.875rem; color: #666; }
                    .slide[data-layout="center"] .slide-content { display: flex; align-items: center; justify-content: center; text-align: center; }
                    .slide[data-layout="cover"] { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
                    .slide[data-layout="two-cols"] .slide-content { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
                    h1 { font-size: 2.5rem; margin: 0 0 1rem 0; }
                    h2 { font-size: 2rem; margin: 0 0 1rem 0; }
                    h3 { font-size: 1.5rem; margin: 0 0 0.75rem 0; }
                    @media print {
                        .slide { page-break-after: always; }
                    }
                </style>
            </head>
            <body>
                ${slides}
            </body>
            </html>
        `;
    }

    /**
     * Convert Slidev presentation to PDF
     */
    private async convertSlidevToPdf(presentation: any, options: ConversionOptions): Promise<Buffer> {
        const html = await this.convertSlidevToHtml(presentation, options);

        // Use Puppeteer to generate PDF with slide-friendly settings
        if (puppeteer) {
            const browser = await puppeteer.launch({
                headless: true,
                args: ['--no-sandbox', '--disable-setuid-sandbox']
            });

            try {
                const page = await browser.newPage();
                await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });
                await page.setContent(html, { waitUntil: 'networkidle0', timeout: 30000 });

                return await page.pdf({
                    format: 'A4',
                    landscape: true,
                    printBackground: true,
                    margin: { top: '0', right: '0', bottom: '0', left: '0' }
                });
            } finally {
                await browser.close();
            }
        } else {
            throw new Error('PDF generation requires Puppeteer for Slidev presentations');
        }
    }

    /**
     * Convert Slidev presentation to PowerPoint (basic version)
     */
    private async convertSlidevToPptx(presentation: any, options: ConversionOptions): Promise<Buffer> {
        // Convert to markdown first, then use existing PPTX conversion
        const markdownContent = this.convertSlidevToMarkdown(presentation);
        const { data: frontmatter, content } = matter(markdownContent);
        return await this.convertToPptx(content, frontmatter, options);
    }

    /**
     * Convert Slidev presentation to plain text
     */
    private convertSlidevToPlainText(presentation: any, options: ConversionOptions): string {
        const title = presentation.title || 'Slidev Presentation';
        const slides = presentation.slides.map((slide: any, index: number) => {
            const content = slide.content
                .replace(/#+\s/g, '') // Remove markdown headers
                .replace(/\*\*(.*?)\*\*/g, '$1') // Remove bold
                .replace(/\*(.*?)\*/g, '$1') // Remove italic
                .replace(/`(.*?)`/g, '$1') // Remove code
                .replace(/\n+/g, '\n') // Normalize newlines
                .trim();

            return `SLIDE ${index + 1}:\n${content}\n${'='.repeat(50)}`;
        }).join('\n\n');

        return `${title}\n${'='.repeat(title.length)}\n\n${slides}`;
    }

    /**
     * Convert Slidev presentation to plain markdown
     */
    private convertSlidevToMarkdown(presentation: any): string {
        const frontmatterString = Object.keys(presentation.frontmatter).length > 0
            ? `---\n${Object.entries(presentation.frontmatter).map(([key, value]) => `${key}: ${value}`).join('\n')}\n---\n\n`
            : '';

        const slidesMarkdown = presentation.slides.map((slide: any) => slide.content).join('\n\n---\n\n');

        return frontmatterString + slidesMarkdown;
    }

    async convert(markdownContent: string, format: string, options: ConversionOptions = {}): Promise<Buffer | string> {
        const { data: frontmatter, content } = matter(markdownContent);

        switch (format) {
            case 'md':
                return markdownContent;

            case 'html':
                return await this.convertToHtml(content, frontmatter, options);

            case 'pdf':
            case 'pdf-puppeteer':
                // Use Puppeteer for high-quality PDF with full rendering
                return await this.convertToPdfPuppeteer(content, frontmatter, options);

            case 'pdf-pandoc':
                // Use pandoc with XeLaTeX for PDF generation
                return await this.convertToPdfPandoc(content, frontmatter, options);

            case 'txt':
                return this.convertToPlainText(content, frontmatter, options);

            case 'rtf':
                return this.convertToRtf(content, frontmatter, options);

            case 'docx':
                return await this.convertToDocx(content, frontmatter, options);

            case 'odt':
                return await this.convertToOdt(content, frontmatter, options);

            case 'epub':
                return await this.convertToEpub(content, frontmatter, options);

            case 'pptx':
                return await this.convertToPptx(content, frontmatter, options);

            case 'latex':
            case 'tex':
                return await this.convertToLatex(content, frontmatter, options);

            case 'pdf-latex-color':
                return await this.convertToPdfLatexPython(content, frontmatter, options);


            default:
                throw new Error(`Unsupported format: ${format}`);
        }
    }

    private async convertToHtml(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): Promise<string> {
        // Process code blocks with syntax highlighting first
        let processedContent = await this.processCodeBlocks(content);

        // Process math expressions (before markdown)
        processedContent = this.processMathExpressions(processedContent);

        // Convert markdown to HTML (excluding code blocks that are already processed)
        let htmlContent = await marked(processedContent);

        // Process Mermaid diagrams
        htmlContent = this.processMermaidDiagrams(htmlContent);

        // Process SVG images for PDF compatibility
        htmlContent = await this.processSvgImages(htmlContent, options);

        // Generate the complete HTML
        const title = String(options.title || frontmatter.title || 'Document');
        const author = String(options.author || frontmatter.author || 'Unknown');

        return this.generateHtmlTemplate(htmlContent, title, author, options);
    }

    private async convertToPdfChrome(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): Promise<Buffer> {
        // First convert to HTML
        const htmlContent = await this.convertToHtml(content, frontmatter, options);

        // Save HTML to temporary file
        const tempHtmlPath = path.join(this.tempDir, `temp-${Date.now()}.html`);
        fs.writeFileSync(tempHtmlPath, htmlContent);

        try {
            // Use Chrome headless to convert to PDF
            const outputPath = path.join(this.tempDir, `output-${Date.now()}.pdf`);

            const chromeArgs = [
                '--headless',
                '--disable-gpu',
                '--disable-software-rasterizer',
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-extensions',
                '--disable-plugins',
                '--disable-images',
                '--run-all-compositor-stages-before-draw',
                '--disable-background-timer-throttling',
                '--disable-renderer-backgrounding',
                '--disable-backgrounding-occluded-windows',
                '--disable-features=TranslateUI,VizDisplayCompositor',
                `--print-to-pdf=${outputPath}`,
                '--print-to-pdf-no-header',
                '--virtual-time-budget=10000'
            ];

            // Use the system chromium binary if available, otherwise try Chrome paths
            let chromePath = '/usr/bin/chromium-browser'; // Alpine Linux path
            if (!require('fs').existsSync(chromePath)) {
                chromePath = '/Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome'; // macOS path
            }

            const command = `${chromePath} ${chromeArgs.join(' ')} "${tempHtmlPath}"`;

            await execAsync(command);

            // Wait a bit for file to be written
            await new Promise(resolve => setTimeout(resolve, 2000));

            if (!fs.existsSync(outputPath)) {
                throw new Error('PDF generation failed - output file not created');
            }

            const pdfBuffer = fs.readFileSync(outputPath);

            // Clean up temporary files
            fs.unlinkSync(tempHtmlPath);
            fs.unlinkSync(outputPath);

            return pdfBuffer;
        } catch (error) {
            // Clean up temp HTML file
            if (fs.existsSync(tempHtmlPath)) {
                fs.unlinkSync(tempHtmlPath);
            }
            throw error;
        }
    }

    private async convertToPdfPuppeteer(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): Promise<Buffer> {
        let puppeteerInstance = puppeteer;
        if (!puppeteerInstance) {
            try {
                puppeteerInstance = require('puppeteer');
            } catch {
                console.log('Puppeteer not available, falling back to Chrome headless');
                return this.convertToPdfChrome(content, frontmatter, options);
            }
        }

        // First convert to HTML
        const htmlContent = await this.convertToHtml(content, frontmatter, options);

        let browser;
        try {
            const isProduction = process.env.NODE_ENV === 'production';

            // Configure browser launch options
            const launchOptions: Record<string, unknown> = {
                headless: true,
                args: [
                    '--no-sandbox',
                    '--disable-setuid-sandbox',
                    '--disable-dev-shm-usage',
                    '--disable-web-security',
                    '--font-render-hinting=none',
                    '--disable-features=VizDisplayCompositor',
                    '--run-all-compositor-stages-before-draw',
                    '--disable-background-timer-throttling',
                    '--disable-renderer-backgrounding',
                    '--disable-backgrounding-occluded-windows'
                ]
            };

            // Use system Chromium in production (Docker) or chromium package if available
            if (isProduction) {
                // Check if we have PUPPETEER_EXECUTABLE_PATH set (Docker environment)
                if (process.env.PUPPETEER_EXECUTABLE_PATH) {
                    launchOptions.executablePath = process.env.PUPPETEER_EXECUTABLE_PATH;
                } else if (chromium) {
                    // Fallback to chromium package if available
                    try {
                        launchOptions.executablePath = await chromium.executablePath('/opt/nodejs/node_modules/@sparticuz/chromium-min/bin');
                        const chromiumArgs: string[] = Array.isArray(chromium.args) ? chromium.args.filter((arg): arg is string => typeof arg === 'string') : [];
                        const currentArgs = Array.isArray(launchOptions.args) ? launchOptions.args : [];
                        launchOptions.args = [...currentArgs, ...chromiumArgs];
                        launchOptions.defaultViewport = chromium.defaultViewport;
                    } catch (error) {
                        console.warn('Failed to get chromium executable path:', error);
                    }
                }
            }

            browser = await puppeteerInstance!.launch(launchOptions);
            const page = await browser.newPage();

            // Set viewport for consistent rendering
            await page.setViewport({
                width: 1200,
                height: 800,
                deviceScaleFactor: 1
            });

            // Configure page for better rendering
            await page.evaluateOnNewDocument(() => {
                // Disable animations for consistent rendering
                const style = document.createElement('style');
                style.textContent = `
                    *, *::before, *::after {
                        animation-duration: 0s !important;
                        animation-delay: 0s !important;
                        transition-duration: 0s !important;
                        transition-delay: 0s !important;
                    }
                `;
                document.head.appendChild(style);
            });

            // Set content and wait for resources
            await page.setContent(htmlContent, {
                waitUntil: options.pdfOptions?.waitForNetwork ? 'networkidle0' : 'load',
                timeout: options.pdfOptions?.timeout || 30000
            });

            // Wait for fonts to load with extended timeout
            await page.evaluateHandle('document.fonts.ready');

            // Additional wait for Google Fonts and custom fonts
            await page.evaluate(() => {
                return new Promise<void>((resolve) => {
                    const checkFonts = () => {
                        if (document.fonts.status === 'loaded' || document.fonts.size > 0) {
                            resolve();
                        } else {
                            setTimeout(checkFonts, 100);
                        }
                    };
                    checkFonts();
                });
            });

            // Wait for Mermaid diagrams to render
            try {
                await page.evaluate(() => {
                    return new Promise<void>((resolve) => {
                        const diagrams = document.querySelectorAll('.mermaid-diagram');
                        if (diagrams.length === 0) {
                            resolve();
                            return;
                        }

                        // Check if Mermaid is available
                        if (typeof (window as unknown as { mermaid?: unknown }).mermaid !== 'undefined') {
                            (window as unknown as {
                                mermaid: {
                                    initialize: (config: Record<string, unknown>) => void;
                                    render: (id: string, code: string, callback: (svg: string) => void) => void;
                                };
                            }).mermaid.initialize({
                                startOnLoad: false,
                                theme: 'default',
                                flowchart: {
                                    useMaxWidth: true,
                                    htmlLabels: true
                                },
                                securityLevel: 'loose'
                            });

                            let rendered = 0;
                            const total = diagrams.length;

                            diagrams.forEach((diagram: Element, index: number) => {
                                const codeEl = diagram.querySelector('.mermaid-code');
                                const renderEl = diagram.querySelector('.mermaid-render');
                                if (codeEl && renderEl && codeEl.textContent) {
                                    try {
                                        (window as unknown as {
                                            mermaid: {
                                                render: (id: string, code: string, callback: (svg: string) => void) => void;
                                            };
                                        }).mermaid.render(`diagram-${index}`, codeEl.textContent, (svgCode: string) => {
                                            renderEl.innerHTML = svgCode;
                                            rendered++;
                                            if (rendered === total) {
                                                setTimeout(() => resolve(), 500);
                                            }
                                        });
                                    } catch {
                                        rendered++;
                                        if (rendered === total) {
                                            setTimeout(() => resolve(), 500);
                                        }
                                    }
                                } else {
                                    rendered++;
                                    if (rendered === total) {
                                        setTimeout(() => resolve(), 500);
                                    }
                                }
                            });

                            // Timeout fallback
                            setTimeout(() => resolve(), 5000);
                        } else {
                            // No Mermaid, continue
                            resolve();
                        }
                    });
                });
            } catch (error) {
                console.log('Mermaid rendering skipped:', error);
            }

            // Additional wait for any remaining rendering
            await new Promise(resolve => setTimeout(resolve, 1000));

            // Configure PDF options with optimized settings for CV/Resume
            const pdfOptions: Record<string, unknown> = {
                format: options.pdfOptions?.format || 'A4',
                printBackground: true,
                margin: options.pdfOptions?.margin || {
                    top: '0.75in',
                    right: '0.75in',
                    bottom: '0.75in',
                    left: '0.75in'
                },
                preferCSSPageSize: true,
                // Ensure embedded images and SVGs are properly rendered
                omitBackground: false,
                tagged: false,
                scale: 1.0,
                landscape: false,
                // Additional quality settings for better PDF output
                quality: 100,
                timeout: 60000,
                // Ensure fonts are embedded properly
                generateTaggedPDF: false
            };

            // Generate PDF
            const pdfBuffer = await page.pdf(pdfOptions);

            return Buffer.from(pdfBuffer);

        } catch (error: unknown) {
            console.error('Puppeteer PDF generation error:', error);
            const errorMessage = error instanceof Error ? error.message : String(error);
            throw new Error(`PDF generation failed: ${errorMessage}`);
        } finally {
            if (browser) {
                await browser.close();
            }
        }
    }

    private convertToPlainText(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): string {
        // Strip markdown formatting and return plain text
        const text = content
            .replace(/!\[.*?\]\(.*?\)/g, '') // Remove images
            .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1') // Convert links to just text
            .replace(/```[\s\S]*?```/g, '') // Remove code blocks first
            .replace(/\*\*(.*?)\*\*/g, '$1') // Remove bold
            .replace(/\*(.*?)\*/g, '$1') // Remove italic
            .replace(/`([^`]+)`/g, '$1') // Remove inline code
            .replace(/#{1,6}\s*/g, '') // Remove headers
            .replace(/^\s*[-*+]\s+/gm, '• ') // Convert bullet lists
            .replace(/^\s*\d+\.\s+/gm, '') // Remove numbered lists
            .replace(/^\s*>\s*/gm, '') // Remove blockquotes
            .replace(/\$\$[\s\S]*?\$\$/g, '[Math Expression]') // Replace display math
            .replace(/\$([^$\n]+)\$/g, '[Math: $1]') // Replace inline math
            .replace(/\n{3,}/g, '\n\n') // Normalize newlines
            .trim();

        const title = options.title || frontmatter.title || 'Document';
        const author = options.author || frontmatter.author || '';
        const date = frontmatter.date ? new Date(frontmatter.date as string).toLocaleDateString() : '';

        let header = title;
        if (author) header += `\nBy: ${author}`;
        if (date) header += `\nDate: ${date}`;
        header += '\n' + '='.repeat(String(title).length) + '\n\n';

        return header + text;
    }

    private convertToRtf(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): string {
        // Convert markdown to RTF (Rich Text Format)
        const rtf = this.markdownToRtf(content);

        const title = options.title || frontmatter.title || 'Document';
        const author = options.author || frontmatter.author || '';

        return `{\\rtf1\\ansi\\deff0 {\\fonttbl {\\f0 Times New Roman;}}
{\\info{\\title ${title}}{\\author ${author}}}
\\f0\\fs24
{\\b\\fs32 ${title}\\par}
{\\i ${author}\\par}
\\par
${rtf}
}`;
    }

    private markdownToRtf(markdown: string): string {
        // Basic markdown to RTF conversion
        return markdown
            .replace(/^# (.*?)$/gm, '{\\b\\fs28 $1\\par}')
            .replace(/^## (.*?)$/gm, '{\\b\\fs24 $1\\par}')
            .replace(/^### (.*?)$/gm, '{\\b\\fs20 $1\\par}')
            .replace(/\*\*(.*?)\*\*/g, '{\\b $1}')
            .replace(/\*(.*?)\*/g, '{\\i $1}')
            .replace(/`([^`]+)`/g, '{\\f1 $1}')
            .replace(/```[\s\S]*?```/g, '{\\f1 $1\\par}')
            .replace(/^\* (.*?)$/gm, '\\bullet $1\\par')
            .replace(/\$\$[\s\S]*?\$\$/g, '[Math Expression]\\par')
            .replace(/\$([^$\n]+)\$/g, '[Math: $1]')
            .replace(/\n/g, '\\par\n');
    }

    private async convertToPdfLatexPython(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): Promise<Buffer> {
        // Need contentPath to run the script
        if (!options.contentPath) {
            console.warn('contentPath not provided for LateX Python conversion, falling back to standard Pandoc');
            return this.convertToPdfPandoc(content, frontmatter, options);
        }

        const filePath = path.resolve(options.contentPath);
        const fileName = path.basename(filePath);

        // Check if file matches pattern
        const isSolution = /.*-solution(\.gu)?\.mdx$/.test(fileName);

        if (!isSolution) {
            console.log('File does not match solution pattern, falling back to standard Pandoc');
            return this.convertToPdfPandoc(content, frontmatter, options);
        }

        // Path to python script (resolved relative to project root)
        const scriptPath = path.resolve(process.cwd(), 'scripts/convert_mdx_to_pdf.py');

        // Run script
        try {
            // We run python3 on the file. The script expects the file path.
            // Note: The script outputs the PDF in the same directory as the input file.
            const cmd = `python3 "${scriptPath}" "${filePath}"`; // Default is keep_aux=False, no-pdf=False

            console.log(`Executing Python conversion: ${cmd}`);
            await execAsync(cmd);

            // Determine output PDF name based on script logic
            const stem = path.basename(filePath, '.mdx');
            let pdfName = '';

            // Logic matches convert_mdx_to_pdf.py:
            // if stem.endswith('.gu') -> base_stem-pandoc.gu.pdf
            // else -> stem-pandoc.pdf

            if (stem.endsWith('.gu')) {
                pdfName = `${stem.slice(0, -3)}-pandoc.gu.pdf`;
            } else {
                pdfName = `${stem}-pandoc.pdf`;
            }

            const pdfPath = path.join(path.dirname(filePath), pdfName);

            if (fs.existsSync(pdfPath)) {
                const pdfBuffer = fs.readFileSync(pdfPath);

                // Clean up the generated PDF and TeX files to avoid cluttering the source directory
                fs.unlinkSync(pdfPath);

                // Delete the intermediate .tex file as well
                const texName = pdfName.replace('.pdf', '.tex');
                const texPath = path.join(path.dirname(filePath), texName);
                if (fs.existsSync(texPath)) {
                    fs.unlinkSync(texPath);
                }

                return pdfBuffer;
            } else {
                throw new Error(`PDF generated by Python script not found at ${pdfPath}`);
            }

        } catch (error) {
            console.error('Python LaTeX conversion failed:', error);
            // Fallback to Pandoc if Python fails? Or throw?
            // User likely prefers explicit failure if they asked for this format.
            throw error;
        }
    }

    private async convertToDocx(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): Promise<Buffer> {
        // Use pandoc to convert markdown to docx
        const tempMdPath = path.join(this.tempDir, `temp-${Date.now()}.md`);
        const tempDocxPath = path.join(this.tempDir, `temp-${Date.now()}.docx`);

        try {
            // Convert Mermaid diagrams to images first
            let processedContent = await this.convertMermaidToImages(content);

            // Process SVG images for Pandoc compatibility
            processedContent = await this.processSvgForPandoc(processedContent, options);

            // Create frontmatter content
            const title = options.title || frontmatter.title || 'Document';
            const author = options.author || frontmatter.author || '';
            const date = frontmatter.date ? new Date(frontmatter.date as string).toLocaleDateString() : '';

            const markdownWithMeta = `---
title: "${title}"
author: "${author}"
date: "${date}"
---

${processedContent}`;

            fs.writeFileSync(tempMdPath, markdownWithMeta);

            // Convert using pandoc
            const pandocCommand = `pandoc "${tempMdPath}" -o "${tempDocxPath}" --from markdown --to docx`;
            await execAsync(pandocCommand);

            if (!fs.existsSync(tempDocxPath)) {
                throw new Error('DOCX generation failed - output file not created');
            }

            const docxBuffer = fs.readFileSync(tempDocxPath);

            // Clean up temporary files
            fs.unlinkSync(tempMdPath);
            fs.unlinkSync(tempDocxPath);

            return docxBuffer;
        } catch (error) {
            // Clean up temp files
            if (fs.existsSync(tempMdPath)) {
                fs.unlinkSync(tempMdPath);
            }
            if (fs.existsSync(tempDocxPath)) {
                fs.unlinkSync(tempDocxPath);
            }
            throw new Error(`DOCX conversion failed: ${error instanceof Error ? error.message : String(error)}`);
        }
    }

    private async convertToEpub(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): Promise<Buffer> {
        // Generate temporary markdown file
        const tempMdPath = path.join(this.tempDir, `temp-${Date.now()}.md`);
        const tempEpubPath = path.join(this.tempDir, `output-${Date.now()}.epub`);

        // Process SVG images for Pandoc compatibility
        const processedContent = await this.processSvgForPandoc(content, options);

        // Create complete markdown with frontmatter
        const title = options.title || frontmatter.title || 'Document';
        const author = options.author || frontmatter.author || 'Unknown Author';
        const date = frontmatter.date || new Date().toISOString().split('T')[0];

        const fullMarkdown = `---
title: "${title}"
author: "${author}"
date: ${date}
lang: ${options.language || 'en'}
---

${processedContent}`;

        try {
            fs.writeFileSync(tempMdPath, fullMarkdown);

            // Use pandoc to convert to EPUB with custom styling
            const pandocCommand = [
                'pandoc',
                `"${tempMdPath}"`,
                '-o', `"${tempEpubPath}"`,
                '--toc',
                '--toc-depth=3',
                '--epub-chapter-level=2'
            ].join(' ');

            await execAsync(pandocCommand);

            // Read the generated EPUB file
            const epubBuffer = fs.readFileSync(tempEpubPath);

            // Clean up temporary files
            fs.unlinkSync(tempMdPath);
            fs.unlinkSync(tempEpubPath);

            return epubBuffer;
        } catch (error) {
            // Clean up temporary files in case of error
            if (fs.existsSync(tempMdPath)) {
                fs.unlinkSync(tempMdPath);
            }
            if (fs.existsSync(tempEpubPath)) {
                fs.unlinkSync(tempEpubPath);
            }
            throw error;
        }
    }

    private async convertToLatex(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): Promise<string> {
        // Generate temporary markdown file
        const tempMdPath = path.join(this.tempDir, `temp-${Date.now()}.md`);
        const tempTexPath = path.join(this.tempDir, `output-${Date.now()}.tex`);

        // Process SVG images for Pandoc compatibility
        const processedContent = await this.processSvgForPandoc(content, options);

        // Create complete markdown with frontmatter
        const title = options.title || frontmatter.title || 'Document';
        const author = options.author || frontmatter.author || 'Unknown Author';
        const date = frontmatter.date || new Date().toISOString().split('T')[0];

        const fullMarkdown = `---
title: "${title}"
author: "${author}"
date: ${date}
---

${processedContent}`;

        try {
            fs.writeFileSync(tempMdPath, fullMarkdown);

            // Use pandoc to convert to LaTeX
            const pandocCommand = [
                'pandoc',
                `"${tempMdPath}"`,
                '-o', `"${tempTexPath}"`,
                '--standalone',
                '--variable=geometry:margin=1in',
                '--variable=fontsize=11pt',
                '--variable=documentclass=article'
            ].join(' ');

            await execAsync(pandocCommand);

            // Read the generated LaTeX file
            const latexContent = fs.readFileSync(tempTexPath, 'utf8');

            // Clean up temporary files
            fs.unlinkSync(tempMdPath);
            fs.unlinkSync(tempTexPath);

            return latexContent;
        } catch (error) {
            // Clean up temporary files in case of error
            if (fs.existsSync(tempMdPath)) {
                fs.unlinkSync(tempMdPath);
            }
            if (fs.existsSync(tempTexPath)) {
                fs.unlinkSync(tempTexPath);
            }
            throw error;
        }
    }

    private async convertToPdfPandoc(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): Promise<Buffer> {
        // Generate temporary markdown file
        const tempMdPath = path.join(this.tempDir, `temp-${Date.now()}.md`);
        const tempPdfPath = path.join(this.tempDir, `output-${Date.now()}.pdf`);
        const tempTexPath = path.join(this.tempDir, `template-${Date.now()}.tex`);

        try {
            // Convert Mermaid diagrams to images first
            let processedContent = await this.convertMermaidToImages(content);

            // Process SVG images for Pandoc compatibility
            processedContent = await this.processSvgForPandoc(processedContent, options);

            // Create complete markdown with frontmatter
            const title = String(options.title || frontmatter.title || 'Document');
            const author = String(options.author || frontmatter.author || 'Unknown Author');
            const date = frontmatter.date && typeof frontmatter.date === 'string' ? frontmatter.date : new Date().toISOString().split('T')[0];

            const fullMarkdown = `---
title: "${title}"
author: "${author}"
date: ${date}
geometry: margin=1in
fontsize: 11pt
documentclass: article
---

${processedContent}`;

            fs.writeFileSync(tempMdPath, fullMarkdown);

            // Use Pandoc with default template (reliable for complex tables)
            const pandocCommand = [
                'pandoc',
                `"${tempMdPath}"`,
                '-o', `"${tempPdfPath}"`,
                '--pdf-engine=xelatex',
                '--standalone',
                '--toc',
                '--variable=colorlinks:true',
                '--variable=linkcolor:blue',
                '--variable=urlcolor:blue',
                '--variable=toccolor:blue',
                '--variable=fontsize:11pt',
                '--variable=geometry:margin=1in',
                '--shift-heading-level-by=-1'
            ].join(' ');

            // Increase maxBuffer to handle large SVG conversion output (especially for documents with many images)
            await execAsync(pandocCommand, { maxBuffer: 10 * 1024 * 1024 }); // 10MB buffer

            if (!fs.existsSync(tempPdfPath)) {
                throw new Error('PDF generation failed - output file not created');
            }

            // Read the generated PDF file
            const pdfBuffer = fs.readFileSync(tempPdfPath);

            // Clean up temporary files
            fs.unlinkSync(tempMdPath);
            if (fs.existsSync(tempTexPath)) {
                fs.unlinkSync(tempTexPath);
            }
            fs.unlinkSync(tempPdfPath);

            return pdfBuffer;
        } catch (error) {
            // Clean up temporary files in case of error
            if (fs.existsSync(tempMdPath)) {
                fs.unlinkSync(tempMdPath);
            }
            if (fs.existsSync(tempTexPath)) {
                fs.unlinkSync(tempTexPath);
            }
            if (fs.existsSync(tempPdfPath)) {
                fs.unlinkSync(tempPdfPath);
            }
            throw new Error(`PDF conversion failed: ${error instanceof Error ? error.message : String(error)}`);
        }
    }

    private async convertToOdt(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): Promise<Buffer> {
        // Generate temporary markdown file
        const tempMdPath = path.join(this.tempDir, `temp-${Date.now()}.md`);
        const tempOdtPath = path.join(this.tempDir, `output-${Date.now()}.odt`);

        try {
            // Convert Mermaid diagrams to images first
            let processedContent = await this.convertMermaidToImages(content);

            // Process SVG images for Pandoc compatibility
            processedContent = await this.processSvgForPandoc(processedContent, options);

            // Create complete markdown with frontmatter
            const title = options.title || frontmatter.title || 'Document';
            const author = options.author || frontmatter.author || 'Unknown Author';
            const date = frontmatter.date && typeof frontmatter.date === 'string' ? frontmatter.date : new Date().toISOString().split('T')[0];

            const fullMarkdown = `---
title: "${title}"
author: "${author}"
date: ${date}
lang: ${options.language || 'en'}
---

${processedContent}`;

            fs.writeFileSync(tempMdPath, fullMarkdown);

            // Use pandoc to convert to ODT (OpenDocument Text)
            const pandocCommand = [
                'pandoc',
                `"${tempMdPath}"`,
                '-o', `"${tempOdtPath}"`,
                '--standalone',
                '--toc',
                '--toc-depth=3'
            ].join(' ');

            await execAsync(pandocCommand);

            if (!fs.existsSync(tempOdtPath)) {
                throw new Error('ODT generation failed - output file not created');
            }

            // Read the generated ODT file
            const odtBuffer = fs.readFileSync(tempOdtPath);

            // Clean up temporary files
            fs.unlinkSync(tempMdPath);
            fs.unlinkSync(tempOdtPath);

            return odtBuffer;
        } catch (error) {
            // Clean up temporary files in case of error
            if (fs.existsSync(tempMdPath)) {
                fs.unlinkSync(tempMdPath);
            }
            if (fs.existsSync(tempOdtPath)) {
                fs.unlinkSync(tempOdtPath);
            }
            throw new Error(`ODT conversion failed: ${error instanceof Error ? error.message : String(error)}`);
        }
    }

    private async convertToPptx(content: string, frontmatter: Record<string, unknown>, options: ConversionOptions): Promise<Buffer> {
        // Generate temporary markdown file
        const tempMdPath = path.join(this.tempDir, `temp-${Date.now()}.md`);
        const tempPptxPath = path.join(this.tempDir, `output-${Date.now()}.pptx`);

        try {
            // Convert Mermaid diagrams to images first
            let processedContent = await this.convertMermaidToImages(content);

            // Process SVG images for Pandoc compatibility
            processedContent = await this.processSvgForPandoc(processedContent, options);

            // Create complete markdown with frontmatter optimized for presentation
            const title = options.title || frontmatter.title || 'Presentation';
            const author = options.author || frontmatter.author || 'Unknown Author';
            const date = frontmatter.date && typeof frontmatter.date === 'string' ? frontmatter.date : new Date().toISOString().split('T')[0];

            // Process content to be more presentation-friendly
            let presentationContent = processedContent;

            // Convert main headings (# and ##) to slide breaks
            presentationContent = presentationContent.replace(/^# /gm, '\n---\n\n# ');
            presentationContent = presentationContent.replace(/^## /gm, '\n---\n\n## ');

            const fullMarkdown = `---
title: "${title}"
author: "${author}"
date: ${date}
---

# ${title}

**${author}**

${date}

---

${presentationContent}`;

            fs.writeFileSync(tempMdPath, fullMarkdown);

            // Use pandoc to convert to PPTX with presentation-specific options
            const pandocCommand = [
                'pandoc',
                `"${tempMdPath}"`,
                '-o', `"${tempPptxPath}"`,
                '--standalone',
                '-t', 'pptx',
                '--slide-level=2'  // Use level 2 headings as slides
            ].join(' ');

            await execAsync(pandocCommand);

            if (!fs.existsSync(tempPptxPath)) {
                throw new Error('PPTX generation failed - output file not created');
            }

            // Read the generated PPTX file
            const pptxBuffer = fs.readFileSync(tempPptxPath);

            // Clean up temporary files
            fs.unlinkSync(tempMdPath);
            fs.unlinkSync(tempPptxPath);

            return pptxBuffer;
        } catch (error) {
            // Clean up temporary files in case of error
            if (fs.existsSync(tempMdPath)) {
                fs.unlinkSync(tempMdPath);
            }
            if (fs.existsSync(tempPptxPath)) {
                fs.unlinkSync(tempPptxPath);
            }
            throw new Error(`PPTX conversion failed: ${error instanceof Error ? error.message : String(error)}`);
        }
    }

    private processMathExpressions(content: string): string {
        if (!katex) return content;

        // Process display math ($$...$$)
        content = content.replace(/\$\$([^$]+)\$\$/g, (match, math) => {
            try {
                const rendered = katex.renderToString(math.trim(), {
                    displayMode: true,
                    throwOnError: false,
                    strict: false
                });
                return `<div class="math-display">${rendered}</div>`;
            } catch (error) {
                console.warn('Math rendering error:', error);
                return `<div class="math-display">${math}</div>`;
            }
        });

        // Process inline math ($...$)
        content = content.replace(/\$([^$\n]+)\$/g, (match, math) => {
            try {
                const rendered = katex.renderToString(math.trim(), {
                    displayMode: false,
                    throwOnError: false,
                    strict: false
                });
                return `<span class="math-inline">${rendered}</span>`;
            } catch (error) {
                console.warn('Math rendering error:', error);
                return `<span class="math-inline">${math}</span>`;
            }
        });

        return content;
    }

    private processMermaidDiagrams(html: string): string {
        let diagramCounter = 0;

        // Process mermaid code blocks - handle both already converted and original markdown
        // First handle any remaining markdown mermaid blocks that weren't processed by marked
        html = html.replace(/```mermaid\n([\s\S]*?)```/g, (match, code) => {
            diagramCounter++;
            const cleanCode = code.trim();

            return `<div class="mermaid-diagram" data-diagram-id="${diagramCounter}">
<pre class="mermaid-code">${cleanCode}</pre>
<div class="mermaid-render" id="mermaid-${diagramCounter}"></div>
</div>`;
        });

        // Then handle any that were converted by marked to HTML code blocks
        html = html.replace(/<pre><code class="language-mermaid">([\s\S]*?)<\/code><\/pre>/g, (match, code) => {
            diagramCounter++;
            const cleanCode = code.trim()
                .replace(/&lt;/g, '<')
                .replace(/&gt;/g, '>')
                .replace(/&amp;/g, '&')
                .replace(/&quot;/g, '"');

            return `<div class="mermaid-diagram" data-diagram-id="${diagramCounter}">
<pre class="mermaid-code">${cleanCode}</pre>
<div class="mermaid-render" id="mermaid-${diagramCounter}"></div>
</div>`;
        });

        return html;
    }

    /**
     * Process SVG images to ensure they embed properly in PDFs
     * Converts SVG file references to base64 data URLs
     */
    private async processSvgImages(html: string, options: ConversionOptions = {}): Promise<string> {
        // Find all img tags with SVG sources
        const imgRegex = /<img([^>]*?)src=["']([^"']*\.svg)["']([^>]*?)>/gi;
        const matches = Array.from(html.matchAll(imgRegex));

        if (matches.length === 0) {
            return html;
        }

        let processedHtml = html;

        // Process each SVG image
        for (const match of matches) {
            const [fullMatch, beforeSrc, svgPath, afterSrc] = match;

            try {
                let svgContent: string | null = null;

                // First try to get SVG content from API or filesystem
                if (svgPath.startsWith('/api/content-images/')) {
                    // SVG is served through API - fetch it
                    svgContent = await this.fetchSvgFromApi(svgPath);
                } else if (svgPath.startsWith('/')) {
                    // Absolute path - try API first, then filesystem
                    const apiPath = `/api/content-images${svgPath}`;
                    svgContent = await this.fetchSvgFromApi(apiPath);
                    if (!svgContent) {
                        const resolvedPath = this.resolveSvgPath(svgPath);
                        if (fs.existsSync(resolvedPath)) {
                            svgContent = fs.readFileSync(resolvedPath, 'utf8');
                        }
                    }
                } else {
                    // Relative path - resolve using content path context
                    const resolvedApiPath = this.resolveRelativeSvgPath(svgPath, options.contentPath);
                    if (resolvedApiPath) {
                        svgContent = await this.fetchSvgFromApi(resolvedApiPath);
                    }

                    // Fallback to filesystem resolution
                    if (!svgContent) {
                        const resolvedPath = this.resolveSvgPath(svgPath);
                        if (fs.existsSync(resolvedPath)) {
                            svgContent = fs.readFileSync(resolvedPath, 'utf8');
                        }
                    }
                }

                if (svgContent) {
                    // Convert to base64 data URL
                    const base64Data = Buffer.from(svgContent).toString('base64');
                    const dataUrl = `data:image/svg+xml;base64,${base64Data}`;

                    // Replace the image src with the data URL
                    const newImg = `<img${beforeSrc}src="${dataUrl}"${afterSrc}>`;
                    processedHtml = processedHtml.replace(fullMatch, newImg);

                    console.log(`Converted SVG to base64: ${svgPath}`);
                } else {
                    console.warn(`SVG file not found: ${svgPath}`);
                    // Keep the original but add error handling
                    const errorImg = `<img${beforeSrc}src="${svgPath}" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"${afterSrc}><div style="display:none; color:red; font-size:12px; border:1px solid #ccc; padding:10px; background:#f9f9f9;">[SVG Image Not Found: ${svgPath}]</div>`;
                    processedHtml = processedHtml.replace(fullMatch, errorImg);
                }
            } catch (error) {
                console.error(`Error processing SVG ${svgPath}:`, error);
                // Keep original image with error fallback
                const errorImg = `<img${beforeSrc}src="${svgPath}" onerror="this.style.display='none'; this.nextElementSibling.style.display='block';"${afterSrc}><div style="display:none; color:red; font-size:12px; border:1px solid #ccc; padding:10px; background:#f9f9f9;">[SVG Processing Error: ${svgPath}]</div>`;
                processedHtml = processedHtml.replace(fullMatch, errorImg);
            }
        }

        return processedHtml;
    }

    /**
     * Process SVG images in markdown content for Pandoc formats
     * Converts relative SVG paths to absolute file paths for Pandoc processing
     */
    private async processSvgForPandoc(content: string, options: ConversionOptions = {}): Promise<string> {
        // Find all markdown image references with SVG sources
        const imgRegex = /!\[([^\]]*)\]\(([^)]*\.svg)(?:\s+"([^"]*)")?\)/g;
        const matches = Array.from(content.matchAll(imgRegex));

        if (matches.length === 0) {
            return content;
        }

        let processedContent = content;

        // Process each SVG image
        for (const match of matches) {
            const [fullMatch, altText, svgPath] = match;

            try {
                let absolutePath: string | null = null;

                // 1. If absolute path, check existence
                if (path.isAbsolute(svgPath)) {
                    if (fs.existsSync(svgPath)) {
                        absolutePath = svgPath;
                    }
                }
                // 2. Resolve relative to contentPath (most likely scenario)
                else if (options.contentPath) {
                    const contentDir = path.dirname(options.contentPath);
                    const resolved = path.resolve(contentDir, svgPath);
                    if (fs.existsSync(resolved)) {
                        absolutePath = resolved;
                    } else {
                        // Try looking in public dir if not found in content dir
                        const publicPath = path.resolve(process.cwd(), 'public', svgPath.replace(/^\//, ''));
                        if (fs.existsSync(publicPath)) {
                            absolutePath = publicPath;
                        }
                    }
                }
                // 3. Fallback: try resolving from cwd or common folders
                else {
                    const possiblePaths = [
                        path.resolve(process.cwd(), 'public', svgPath.replace(/^\//, '')),
                        path.resolve(process.cwd(), 'content', svgPath)
                    ];
                    for (const p of possiblePaths) {
                        if (fs.existsSync(p)) {
                            absolutePath = p;
                            break;
                        }
                    }
                }

                if (absolutePath) {
                    // Replace with absolute path for Pandoc
                    // Keep markdown syntax: ![alt](/abs/path/to.svg)
                    const replacement = `![${altText || ''}](${absolutePath})`;
                    processedContent = processedContent.replace(fullMatch, replacement);

                    console.log(`Resolved SVG for Pandoc: ${svgPath} -> ${absolutePath}`);
                } else {
                    console.warn(`SVG file not found for Pandoc: ${svgPath}`);
                    // Replace with text indicating missing image
                    processedContent = processedContent.replace(fullMatch, `[Image not found: ${svgPath}]`);
                }
            } catch (error) {
                console.error(`Error processing SVG for Pandoc ${svgPath}:`, error);
                processedContent = processedContent.replace(fullMatch, `[SVG Error: ${svgPath}]`);
            }
        }

        return processedContent;
    }

    /**
     * Resolve relative SVG paths to API endpoints using content path context
     */
    private resolveRelativeSvgPath(svgPath: string, contentPath?: string): string | null {
        // Handle absolute paths - return them as is
        if (path.isAbsolute(svgPath)) {
            return svgPath;
        }

        if (!contentPath) {
            // Try to resolve without content path
            const possiblePaths = [
                path.resolve(process.cwd(), 'content', svgPath),
                path.resolve(process.cwd(), 'public', svgPath)
            ];

            for (const possiblePath of possiblePaths) {
                try {
                    if (fs.existsSync(possiblePath)) {
                        return possiblePath;
                    }
                } catch {
                    // Continue to next path
                }
            }
            return null;
        }

        // Extract the directory part of the content path
        const contentDir = path.dirname(contentPath);

        // Try multiple resolution strategies
        const possiblePaths = [
            path.resolve(contentDir, svgPath),
            path.resolve(process.cwd(), 'content', svgPath),
            path.resolve(process.cwd(), 'public', svgPath)
        ];

        for (const possiblePath of possiblePaths) {
            try {
                if (fs.existsSync(possiblePath)) {
                    // Construct the API path
                    const apiPath = `/api/content-images/${contentDir}/${svgPath}`;
                    if (process.env.NODE_ENV !== 'test') {
                        console.log(`Resolving relative SVG path: ${svgPath} -> ${apiPath}`);
                    }
                    return apiPath;
                }
            } catch {
                // Continue to next path
            }
        }

        return null;
    }

    /**
     * Fetch SVG content from API endpoint
     */
    private async fetchSvgFromApi(apiPath: string): Promise<string | null> {
        try {
            // Construct the full URL for the API call
            const baseUrl = process.env.NEXT_PUBLIC_BASE_URL || 'http://localhost:3000';
            const fullUrl = `${baseUrl}${apiPath}`;

            if (process.env.NODE_ENV !== 'test') {
                console.log(`Fetching SVG from API: ${fullUrl}`);
            }

            // Try to use fetch - handle both browser and Node.js environments
            let fetchFunction: typeof fetch;
            try {
                // Use built-in fetch (available in Next.js/Node 18+)
                fetchFunction = fetch;
                if (typeof fetchFunction === 'undefined') {
                    console.warn('fetch not available, skipping API call');
                    return null;
                }
            } catch {
                // Fallback for environments without fetch
                console.warn('fetch not available, skipping API call');
                return null;
            }

            const response = await fetchFunction(fullUrl, {
                method: 'GET',
                headers: {
                    'Accept': 'image/svg+xml,text/plain,*/*'
                }
            });
            if (response.ok) {
                const svgContent = await response.text();
                return svgContent;
            } else {
                if (process.env.NODE_ENV !== 'test') {
                    console.error(`Failed to fetch SVG from API: ${response.status} ${response.statusText}`);
                }
                return null;
            }
        } catch (error) {
            if (process.env.NODE_ENV !== 'test') {
                console.error(`Error fetching SVG from API ${apiPath}:`, error);
            }
            return null;
        }
    }

    /**
     * Resolve SVG file path relative to content directory
     */
    private resolveSvgPath(svgPath: string): string {
        // Handle null/undefined input
        if (!svgPath) {
            return svgPath;
        }

        // If it's already an absolute path, use it
        if (path.isAbsolute(svgPath)) {
            return svgPath;
        }

        // Try different base directories
        const possiblePaths = [
            // Relative to public directory
            path.resolve(process.cwd(), 'public', svgPath),
            // Check if it's in the content directory structure
            path.resolve(process.cwd(), `content/resources/${svgPath}`),
            // Relative to content directory
            path.resolve(process.cwd(), 'content', svgPath),
        ];

        // Find the first path that exists
        for (const possiblePath of possiblePaths) {
            try {
                if (fs.existsSync(possiblePath)) {
                    return possiblePath;
                }
            } catch {
                // Continue to next path on filesystem errors
                continue;
            }
        }

        // Default fallback
        return svgPath;
    }

    private escapeHtml(text: string): string {
        return text
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#x27;');
    }

    private generateHtmlTemplate(content: string, title: string, author: string, options: ConversionOptions): string {
        const currentDate = new Date().toLocaleDateString('en-GB');
        const escapedTitle = this.escapeHtml(title);
        const escapedAuthor = this.escapeHtml(author);

        return `<!DOCTYPE html>
<html lang="${options.language || 'en'}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="${escapedAuthor}">
    <title>${escapedTitle}</title>
    
    <!-- KaTeX CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
    <!-- Mermaid -->
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.6.1/dist/mermaid.min.js"></script>
    <!-- Font imports -->
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Sans+Gujarati:wght@300;400;500;600;700&display=swap');
        
        @page {
            size: ${options.pdfOptions?.format || 'A4'};
            margin: ${options.pdfOptions?.margin?.top || '2cm'} ${options.pdfOptions?.margin?.right || '2cm'} ${options.pdfOptions?.margin?.bottom || '2cm'} ${options.pdfOptions?.margin?.left || '2cm'};
        }
        
        * {
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            line-height: 1.6;
            color: #1a202c;
            font-size: 11pt;
            max-width: none;
            margin: 0;
            padding: 0;
            background: white;
        }
        
        .container {
            max-width: 100%;
            margin: 0 auto;
            padding: 20px;
        }
        
        h1 {
            color: #2d3748;
            border-bottom: 3px solid #3182ce;
            padding-bottom: 10px;
            font-size: 20pt;
            margin-top: 0;
            margin-bottom: 30px;
            page-break-after: avoid;
        }
        
        h2 {
            color: #2c5282;
            background: linear-gradient(to right, #e2e8f0, transparent);
            padding: 10px 15px;
            border-left: 4px solid #3182ce;
            margin-top: 30px;
            margin-bottom: 20px;
            font-size: 14pt;
            page-break-after: avoid;
        }
        
        h3 {
            color: #4a5568;
            font-size: 12pt;
            margin-top: 25px;
            margin-bottom: 15px;
            page-break-after: avoid;
        }
        
        h4, h5, h6 {
            color: #718096;
            margin-top: 20px;
            margin-bottom: 10px;
            page-break-after: avoid;
        }
        
        p {
            margin-bottom: 15px;
            text-align: justify;
            orphans: 3;
            widows: 3;
            text-indent: 0;
        }
        
        .poem-content, .canvas-text.poem, pre.poem {
            white-space: pre-wrap !important;
            text-indent: 0 !important;
            margin-left: 0 !important;
            padding: 0 !important;
            text-align: left !important;
            font-family: 'Georgia', serif !important;
            font-style: italic !important;
            border: none !important;
            background: transparent !important;
            line-height: 1.8 !important;
            word-wrap: break-word !important;
        }
        
        .table-wrapper {
            overflow-x: auto;
            margin: 20px 0;
            page-break-inside: avoid;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 10pt;
        }
        
        th, td {
            border: 1px solid #cbd5e0;
            padding: 8px 12px;
            text-align: left;
            vertical-align: top;
        }
        
        th {
            background-color: #3182ce;
            color: white;
            font-weight: 600;
        }
        
        tr:nth-child(even) {
            background-color: #f7fafc;
        }
        
        pre {
            background-color: #f7fafc;
            padding: 15px;
            border-radius: 6px;
            border-left: 4px solid #3182ce;
            overflow-x: auto;
            font-size: 9pt;
            margin: 15px 0;
            page-break-inside: avoid;
        }
        
        code {
            background-color: #edf2f7;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            font-size: 9pt;
        }
        
        pre code {
            background: none;
            padding: 0;
        }
        
        blockquote {
            border-left: 4px solid #3182ce;
            margin: 15px 0;
            padding: 10px 20px;
            background-color: #edf2f7;
            font-style: italic;
            page-break-inside: avoid;
        }
        
        strong, b {
            color: #2d3748;
            font-weight: 600;
        }
        
        ul, ol {
            margin: 15px 0;
            padding-left: 30px;
        }
        
        li {
            margin-bottom: 8px;
        }
        
        .header-info {
            text-align: center;
            color: #718096;
            font-size: 9pt;
            margin-bottom: 30px;
            padding-bottom: 15px;
            border-bottom: 1px solid #e2e8f0;
        }
        
        /* Math styling */
        .math-inline {
            font-family: 'Computer Modern', 'Times New Roman', serif;
            font-style: italic;
            background-color: #f0f8ff;
            padding: 2px 4px;
            border-radius: 3px;
        }
        
        .math-display {
            font-family: 'Computer Modern', 'Times New Roman', serif;
            font-style: italic;
            background-color: #f0f8ff;
            padding: 10px;
            margin: 15px 0;
            border-radius: 6px;
            text-align: center;
            border-left: 4px solid #4299e1;
        }
        
        .katex {
            font-size: 1.1em;
        }
        
        .katex-display {
            margin: 15px 0;
            text-align: center;
        }
        
        /* Mermaid diagram styling */
        .mermaid-diagram {
            margin: 20px 0;
            page-break-inside: avoid;
            text-align: center;
        }
        
        .mermaid-render {
            background-color: #f8fafc;
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
            min-height: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            overflow: hidden;
        }
        
        .mermaid-render svg {
            max-width: 100%;
            max-height: 400px;
            height: auto;
            width: auto;
        }
        
        .mermaid-code {
            display: none;
            background-color: #f7fafc;
            padding: 10px;
            border-radius: 4px;
            font-family: monospace;
            font-size: 9pt;
            white-space: pre-wrap;
            margin-top: 10px;
        }
        
        .mermaid-fallback {
            background-color: #fff5f5;
            border: 1px solid #fed7d7;
            border-radius: 6px;
            padding: 15px;
            margin: 15px 0;
        }
        
        .mermaid-fallback::before {
            content: "Mermaid Diagram:";
            font-weight: bold;
            color: #c53030;
            display: block;
            margin-bottom: 10px;
        }
        
        .page-break {
            page-break-before: always;
        }
        
        @media print {
            body {
                font-size: 10pt;
            }
            
            h1 { font-size: 18pt; }
            h2 { font-size: 13pt; }
            h3 { font-size: 11pt; }
            
            .no-print {
                display: none;
            }
            
            /* Show rendered diagrams in print, hide code */
            .mermaid-code {
                display: none !important;
            }
            
            .mermaid-render {
                display: block !important;
                padding: 10px !important;
                page-break-inside: avoid;
            }
            
            /* Ensure SVG diagrams are visible and properly sized for print */
            .mermaid-render svg {
                max-width: 90% !important;
                max-height: 300px !important;
                height: auto !important;
                width: auto !important;
                display: block !important;
                margin: 0 auto !important;
            }
            
            /* Scale down oversized diagrams */
            .mermaid-diagram {
                margin: 10px 0 !important;
                page-break-inside: avoid;
            }
        }
        
        /* Shiki syntax highlighting styles for export */
        pre.shiki {
            background-color: #f8fafc !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 6px !important;
            padding: 15px !important;
            overflow-x: auto;
            margin: 15px 0;
            page-break-inside: avoid;
            font-size: 9pt;
            line-height: 1.4;
        }
        
        pre.shiki code {
            background: none !important;
            padding: 0 !important;
            border-radius: 0 !important;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace !important;
            font-size: inherit !important;
        }
        
        /* Shiki theme support - defaults to light theme for print/export */
        .shiki,
        .shiki span {
            color: var(--shiki-light) !important;
            background-color: var(--shiki-light-bg) !important;
        }
        
        /* Special handling for unsupported languages */
        pre.plain-text,
        pre.goat-diagram {
            background-color: #f7fafc !important;
            border: 1px solid #e2e8f0 !important;
            border-radius: 6px !important;
            padding: 15px !important;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace !important;
            font-size: 9pt !important;
            line-height: 1.4 !important;
            overflow-x: auto;
            margin: 15px 0;
            page-break-inside: avoid;
        }
        
        pre.goat-diagram {
            border-left: 4px solid #38b2ac !important;
            background-color: #e6fffa !important;
        }
        
        /* Override default pre/code styles for syntax highlighted blocks */
        pre:has(.shiki),
        pre.shiki {
            background-color: transparent !important;
            border: none !important;
            padding: 0 !important;
            border-left: none !important;
        }
        
        @media print {
            pre.shiki,
            pre.plain-text,
            pre.goat-diagram {
                background-color: #f8f9fa !important;
                border: 1px solid #dee2e6 !important;
                font-size: 8pt !important;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header-info">
            <strong>${escapedTitle}</strong><br>
            By: ${escapedAuthor}<br>
            Generated on ${currentDate} | Content Converter System
        </div>
        
        <div class="content">
            ${content}
        </div>
    </div>
    
    <script>
        // Initialize Mermaid with better error handling
        mermaid.initialize({ 
            startOnLoad: false,
            theme: 'default',
            themeVariables: {
                primaryColor: '#3182ce',
                primaryTextColor: '#1a202c',
                primaryBorderColor: '#2c5282',
                lineColor: '#4a5568',
                secondaryColor: '#e2e8f0',
                tertiaryColor: '#f7fafc'
            },
            fontFamily: 'Inter, sans-serif',
            fontSize: 12,
            flowchart: {
                useMaxWidth: true,
                htmlLabels: true,
                nodeSpacing: 30,
                rankSpacing: 40
            },
            sequence: {
                useMaxWidth: true,
                width: 150
            },
            gantt: {
                useMaxWidth: true
            }
        });
        
        // Render Mermaid diagrams with better error handling
        document.addEventListener('DOMContentLoaded', function() {
            console.log('DOM loaded, starting Mermaid rendering...');
            
            const diagrams = document.querySelectorAll('.mermaid-diagram');
            console.log('Found', diagrams.length, 'Mermaid diagrams');
            
            let renderedCount = 0;
            
            diagrams.forEach((diagram, index) => {
                const codeElement = diagram.querySelector('.mermaid-code');
                const renderDiv = diagram.querySelector('.mermaid-render');
                
                if (!codeElement || !renderDiv) {
                    console.log('Missing elements for diagram', index);
                    return;
                }
                
                const code = codeElement.textContent.trim();
                const renderId = 'mermaid-svg-' + (index + 1);
                
                console.log('Rendering diagram', index + 1, 'with code:', code.substring(0, 50) + '...');
                
                try {
                    mermaid.render(renderId, code).then(result => {
                        console.log('Successfully rendered diagram', index + 1);
                        renderDiv.innerHTML = result.svg;
                        diagram.classList.add('rendered');
                        renderedCount++;
                        
                        if (renderedCount === diagrams.length) {
                            document.body.classList.add('mermaid-ready');
                            console.log('All Mermaid diagrams rendered');
                        }
                    }).catch(error => {
                        console.error('Mermaid rendering error for diagram', index + 1, ':', error);
                        renderDiv.innerHTML = '<p style="color: #c53030; font-style: italic;">Diagram rendering failed</p>';
                        codeElement.style.display = 'block';
                        renderedCount++;
                        
                        if (renderedCount === diagrams.length) {
                            document.body.classList.add('mermaid-ready');
                        }
                    });
                } catch (error) {
                    console.error('Mermaid setup error for diagram', index + 1, ':', error);
                    renderDiv.innerHTML = '<p style="color: #c53030; font-style: italic;">Diagram setup failed</p>';
                    codeElement.style.display = 'block';
                    renderedCount++;
                    
                    if (renderedCount === diagrams.length) {
                        document.body.classList.add('mermaid-ready');
                    }
                }
            });
            
            if (diagrams.length === 0) {
                document.body.classList.add('mermaid-ready');
                console.log('No Mermaid diagrams found, marking as ready');
            }
        });
    </script>
</body>
</html>`;
    }

    private async convertMermaidToImages(content: string): Promise<string> {
        // Convert Mermaid diagrams to PNG images for formats that don't support interactive diagrams
        const mermaidRegex = /```mermaid\n([\s\S]*?)```/g;

        let processedContent = content;
        const matches = Array.from(content.matchAll(mermaidRegex));

        // Process in reverse order to maintain string positions
        for (let i = matches.length - 1; i >= 0; i--) {
            const match = matches[i];
            const [fullMatch, diagramCode] = match;
            const startIndex = match.index!;
            const endIndex = startIndex + fullMatch.length;

            try {
                // Generate a unique filename for this diagram
                const diagramId = `mermaid-${Date.now()}-${i}`;
                const mermaidFile = path.join(this.tempDir, `${diagramId}.mmd`);
                const pngPath = path.join(this.tempDir, `${diagramId}.png`);

                // Write the Mermaid code to a file
                fs.writeFileSync(mermaidFile, diagramCode.trim());

                try {
                    // Use mermaid CLI to generate PNG (better compatibility in documents)
                    await execAsync(`npx @mermaid-js/mermaid-cli -i "${mermaidFile}" -o "${pngPath}" -t neutral -b white --width 800 --height 600`);

                    // Check if PNG was created successfully
                    if (fs.existsSync(pngPath)) {
                        // Replace the Mermaid code block with an image reference
                        const imageMarkdown = `![Mermaid Diagram](${pngPath})`;
                        processedContent = processedContent.slice(0, startIndex) +
                            imageMarkdown +
                            processedContent.slice(endIndex);
                        console.log(`✅ Converted Mermaid diagram ${i + 1} to PNG`);
                    } else {
                        throw new Error('PNG file was not created');
                    }
                } catch (cliError) {
                    console.warn(`Failed to convert Mermaid diagram ${i + 1} to PNG:`, cliError);
                    // Fallback to descriptive text
                    const diagramType = diagramCode.trim().split('\n')[0] || 'diagram';
                    const textFallback = `[Mermaid ${diagramType} - Image conversion not available]`;
                    processedContent = processedContent.slice(0, startIndex) +
                        textFallback +
                        processedContent.slice(endIndex);
                }

                // Clean up temporary mermaid file
                if (fs.existsSync(mermaidFile)) {
                    fs.unlinkSync(mermaidFile);
                }

            } catch (error) {
                console.warn(`Error processing Mermaid diagram ${i + 1}:`, error);
                // Replace with simple text fallback
                const textFallback = `[Mermaid Diagram]`;
                processedContent = processedContent.slice(0, startIndex) +
                    textFallback +
                    processedContent.slice(endIndex);
            }
        }

        return processedContent;
    }

    private ensureDirectoryExists(dirPath: string): void {
        if (!fs.existsSync(dirPath)) {
            fs.mkdirSync(dirPath, { recursive: true });
        }
    }
}
