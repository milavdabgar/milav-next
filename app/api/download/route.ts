import { NextRequest, NextResponse } from 'next/server';
import { ContentConverterV2 } from '@/lib/content-converter-v2';
import { detectContentType } from '@/lib/content-types';
import { getContentBySlug } from '@/lib/mdx';
import fs from 'fs';
import path from 'path';

export async function POST(request: NextRequest) {
  try {
    const { slug, locale, format, options = {} } = await request.json();

    if (!slug) {
      return NextResponse.json(
        { error: 'Slug is required' },
        { status: 400 }
      );
    }

    if (!format) {
      return NextResponse.json(
        { error: 'Format is required' },
        { status: 400 }
      );
    }

    const converter = new ContentConverterV2();
    
    // Get content from MDX
    const post = getContentBySlug('blog', slug, locale === 'gu' ? 'gu' : undefined);
    
    if (!post) {
      return NextResponse.json(
        { error: 'Blog post not found' },
        { status: 404 }
      );
    }

    // Construct full markdown content with frontmatter
    const frontmatter = `---
title: "${post.metadata.title}"
description: "${post.metadata.description || ''}"
date: ${post.metadata.date || ''}
tags: ${post.metadata.tags ? post.metadata.tags.join(', ') : ''}
author: Milav Dabgar
---

`;
    
    const markdownContent = frontmatter + post.content;

    // Add enhanced options for conversion
    const enhancedOptions = {
      ...options,
      title: post.metadata.title,
      author: 'Milav Dabgar',
      contentPath: `blog/${slug}.md`
    };
    
    // Convert content based on format
    const result = await converter.convert(markdownContent, format, enhancedOptions);
    
    // Get the appropriate filename and content type
    const baseFilename = slug;
    const { filename, contentType } = getFileDetails(baseFilename, format);
    
    // Create response
    const response = new NextResponse(result as BodyInit);
    response.headers.set('Content-Type', contentType);
    response.headers.set('Content-Disposition', `attachment; filename="${filename}"`);
    
    return response;

  } catch (error) {
    console.error('Download conversion error:', error);
    return NextResponse.json(
      { 
        error: 'Failed to convert content', 
        details: error instanceof Error ? error.message : String(error)
      },
      { status: 500 }
    );
  }
}

export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url);
    const action = searchParams.get('action');

    if (action === 'supported-formats') {
      return NextResponse.json({
        formats: [
          {
            id: 'md',
            name: 'Markdown',
            description: 'Original markdown format',
            extension: 'md',
            category: 'text'
          },
          {
            id: 'html',
            name: 'HTML',
            description: 'Web-ready HTML with Mermaid diagrams and math',
            extension: 'html',
            category: 'web'
          },
          {
            id: 'pdf',
            name: 'PDF (Puppeteer)',
            description: 'High-quality PDF with diagrams and math support',
            extension: 'pdf',
            category: 'document'
          },
          {
            id: 'pdf-pandoc',
            name: 'PDF (Pandoc/XeLaTeX)',
            description: 'Professional PDF using Pandoc with XeLaTeX engine',
            extension: 'pdf',
            category: 'document'
          },
          {
            id: 'txt',
            name: 'Plain Text',
            description: 'Clean plain text format',
            extension: 'txt',
            category: 'text'
          },
          {
            id: 'rtf',
            name: 'Rich Text Format',
            description: 'RTF format for word processors',
            extension: 'rtf',
            category: 'document'
          },
          {
            id: 'docx',
            name: 'Word Document',
            description: 'Microsoft Word DOCX format',
            extension: 'docx',
            category: 'document'
          },
          {
            id: 'odt',
            name: 'OpenDocument Text',
            description: 'LibreOffice/OpenOffice text document format',
            extension: 'odt',
            category: 'document'
          },
          {
            id: 'epub',
            name: 'EPUB',
            description: 'Electronic book format for e-readers',
            extension: 'epub',
            category: 'ebook'
          },
          {
            id: 'latex',
            name: 'LaTeX',
            description: 'LaTeX typesetting format for academic documents',
            extension: 'tex',
            category: 'document'
          }
        ]
      });
    }

    return NextResponse.json({ error: 'Invalid action' }, { status: 400 });

  } catch (error) {
    console.error('API error:', error);
    return NextResponse.json(
      { 
        error: 'API request failed', 
        details: error instanceof Error ? error.message : String(error)
      },
      { status: 500 }
    );
  }
}

function getFileDetails(baseFilename: string, format: string) {
  const formatMap: Record<string, { extension: string; contentType: string; isBuffer: boolean }> = {
    'md': { 
      extension: 'md', 
      contentType: 'text/markdown', 
      isBuffer: false 
    },
    'html': { 
      extension: 'html', 
      contentType: 'text/html', 
      isBuffer: false 
    },
    'pdf': { 
      extension: 'pdf', 
      contentType: 'application/pdf', 
      isBuffer: true 
    },
    'pdf-pandoc': { 
      extension: 'pdf', 
      contentType: 'application/pdf', 
      isBuffer: true 
    },
    'txt': { 
      extension: 'txt', 
      contentType: 'text/plain', 
      isBuffer: false 
    },
    'rtf': { 
      extension: 'rtf', 
      contentType: 'application/rtf', 
      isBuffer: false 
    },
    'docx': { 
      extension: 'docx', 
      contentType: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 
      isBuffer: true 
    },
    'odt': { 
      extension: 'odt', 
      contentType: 'application/vnd.oasis.opendocument.text', 
      isBuffer: true 
    },
    'epub': { 
      extension: 'epub', 
      contentType: 'application/epub+zip', 
      isBuffer: true 
    },
    'latex': { 
      extension: 'tex', 
      contentType: 'application/x-latex', 
      isBuffer: false 
    }
  };

  const details = formatMap[format] || formatMap['html'];
  return {
    filename: `${baseFilename}.${details.extension}`,
    contentType: details.contentType,
    isBuffer: details.isBuffer
  };
}
