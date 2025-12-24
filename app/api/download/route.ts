import { NextRequest, NextResponse } from 'next/server';
import { getContentBySlug } from '@/lib/mdx';
import path from 'path';
import fs from 'fs';

export async function POST(request: NextRequest) {
  try {
    const { slug, locale, format, title } = await request.json();

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

    // Get the content
    const post = getContentBySlug('blog', slug, locale === 'gu' ? 'gu' : undefined);
    
    if (!post) {
      return NextResponse.json(
        { error: 'Content not found' },
        { status: 404 }
      );
    }

    const baseFilename = title || slug;
    let result: string | Buffer;
    let contentType: string;
    let filename: string;

    switch (format) {
      case 'md':
        result = `---
title: ${post.metadata.title}
description: ${post.metadata.description || ''}
date: ${post.metadata.date || ''}
tags: ${post.metadata.tags?.join(', ') || ''}
---

# ${post.metadata.title}

${post.content}`;
        contentType = 'text/markdown';
        filename = `${baseFilename.replace(/[^a-z0-9]/gi, '-').toLowerCase()}.md`;
        break;

      case 'txt':
        // Strip markdown formatting for plain text
        result = `${post.metadata.title}\n\n${post.metadata.description || ''}\n\n${post.content}`;
        contentType = 'text/plain';
        filename = `${baseFilename.replace(/[^a-z0-9]/gi, '-').toLowerCase()}.txt`;
        break;

      case 'html':
        result = `<!DOCTYPE html>
<html lang="${locale || 'en'}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${post.metadata.title}</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      max-width: 800px;
      margin: 0 auto;
      padding: 2rem;
      line-height: 1.6;
      color: #333;
    }
    h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
    h2 { font-size: 2rem; margin-top: 2rem; border-bottom: 2px solid #eee; padding-bottom: 0.5rem; }
    h3 { font-size: 1.5rem; margin-top: 1.5rem; }
    pre { background: #f5f5f5; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; }
    code { background: #f5f5f5; padding: 0.2rem 0.4rem; border-radius: 0.25rem; font-size: 0.9em; }
    blockquote { border-left: 4px solid #ddd; margin-left: 0; padding-left: 1rem; color: #666; }
    a { color: #0066cc; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .metadata { color: #666; font-size: 0.9rem; margin-bottom: 2rem; }
    @media print {
      body { padding: 0; }
    }
  </style>
</head>
<body>
  <article>
    <h1>${post.metadata.title}</h1>
    ${post.metadata.description ? `<p class="description">${post.metadata.description}</p>` : ''}
    <div class="metadata">
      ${post.metadata.date ? `<time>${new Date(post.metadata.date).toLocaleDateString()}</time>` : ''}
      ${post.metadata.tags ? ` · ${post.metadata.tags.join(', ')}` : ''}
    </div>
    <div class="content">
      ${post.content}
    </div>
  </article>
</body>
</html>`;
        contentType = 'text/html';
        filename = `${baseFilename.replace(/[^a-z0-9]/gi, '-').toLowerCase()}.html`;
        break;

      case 'json':
        result = JSON.stringify({
          title: post.metadata.title,
          description: post.metadata.description,
          date: post.metadata.date,
          tags: post.metadata.tags,
          content: post.content,
          metadata: post.metadata
        }, null, 2);
        contentType = 'application/json';
        filename = `${baseFilename.replace(/[^a-z0-9]/gi, '-').toLowerCase()}.json`;
        break;

      default:
        return NextResponse.json(
          { error: 'Unsupported format' },
          { status: 400 }
        );
    }

    const response = new NextResponse(result);
    response.headers.set('Content-Type', contentType);
    response.headers.set('Content-Disposition', `attachment; filename="${filename}"`);
    
    return response;

  } catch (error) {
    console.error('Download error:', error);
    return NextResponse.json(
      { 
        error: 'Failed to generate download', 
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
            description: 'Original markdown format with frontmatter',
            extension: 'md',
            category: 'text'
          },
          {
            id: 'html',
            name: 'HTML',
            description: 'Standalone HTML file ready to view',
            extension: 'html',
            category: 'web'
          },
          {
            id: 'txt',
            name: 'Plain Text',
            description: 'Simple plain text without formatting',
            extension: 'txt',
            category: 'text'
          },
          {
            id: 'json',
            name: 'JSON',
            description: 'Structured data with metadata',
            extension: 'json',
            category: 'data'
          }
        ]
      });
    }

    return NextResponse.json(
      { error: 'Invalid action' },
      { status: 400 }
    );

  } catch (error) {
    console.error('Download API error:', error);
    return NextResponse.json(
      { error: 'Internal server error' },
      { status: 500 }
    );
  }
}
