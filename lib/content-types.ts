// src/lib/content-types.ts

import fs from 'fs';
import path from 'path';

// Import and re-export types and client-safe functions
import type { ContentType } from './content-types-client';
import { isBrowserViewable, requiresDownload, getMimeType, detectContentTypeFromExtension } from './content-types-client';

export type { ContentType };
export { isBrowserViewable, requiresDownload, getMimeType, detectContentTypeFromExtension };

/**
 * Detect the content type based on file extension and content analysis (server-side only)
 */
export function detectContentType(filePath: string): ContentType {
  if (!fs.existsSync(filePath)) {
    return 'markdown';
  }

  const extension = path.extname(filePath).toLowerCase();
  
  // Handle obvious cases first
  if (extension === '.pdf') return 'pdf';
  if (extension === '.docx') return 'docx';
  if (extension === '.pptx') return 'pptx';
  if (extension === '.xlsx') return 'xlsx';
  if (['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.bmp', '.ico'].includes(extension)) return 'image';
  if (['.txt', '.csv', '.json', '.xml'].includes(extension)) return 'text';
  if (extension === '.html' || extension === '.htm') {
    const content = fs.readFileSync(filePath, 'utf8');
    if (content.includes('reveal.js') || content.includes('Reveal.initialize')) {
      return 'reveal';
    }
    return 'html';
  }
  
  // For markdown files, check content for Slidev indicators
  if (extension === '.md') {
    try {
      const content = fs.readFileSync(filePath, 'utf8');
      
      // Check for Slidev frontmatter indicators
      const frontmatterMatch = content.match(/^---\s*\n([\s\S]*?)\n---/);
      if (frontmatterMatch) {
        const frontmatter = frontmatterMatch[1];
        
        // Look for Slidev-specific frontmatter fields
        if (frontmatter.includes('theme:') || 
            frontmatter.includes('background:') ||
            frontmatter.includes('highlighter:') ||
            frontmatter.includes('transition:') ||
            frontmatter.includes('slidev:') ||
            frontmatter.includes('class: text-center') ||
            frontmatter.includes('drawings:') ||
            frontmatter.includes('mdc:')) {
          return 'slidev';
        }
      }
      
      // Also check for Slidev layout indicators in content
      if (content.includes('layout:') && 
          (content.includes('---\nlayout:') || content.includes('layout: default') || 
           content.includes('layout: two-cols') || content.includes('layout: center'))) {
        return 'slidev';
      }
      
      // Check for Slidev-specific slide separators with layout or other Slidev indicators
      if (content.includes('\n---\n') && frontmatterMatch) {
        // Only consider it Slidev if slide separators are combined with Slidev-specific patterns
        const slideSeparators = (content.match(/\n---\n/g) || []).length;
        if (slideSeparators > 1) {
          // Look for Slidev-specific patterns after slide separators
          const hasLayoutAfterSeparator = /\n---\n[^]*?^layout:\s*/m.test(content);
          const hasSlidevDirectives = content.includes('v-click') || 
                                     content.includes('::v-click') ||
                                     content.includes('<v-') ||
                                     content.includes('slidev');
          
          // Only classify as Slidev if we have clear Slidev indicators
          if (hasLayoutAfterSeparator || hasSlidevDirectives) {
            return 'slidev';
          }
        }
      }
      
    } catch (error) {
      console.warn(`Error reading file for content type detection: ${filePath}`, error);
    }
  }
  
  // Fallback for any other file type
  if (extension && extension !== '.md') {
    return 'other';
  }
  
  return 'markdown';
}

/**
 * Check if a file is a Slidev presentation based on its path pattern
 */
export function isSlidevPath(filePath: string): boolean {
  const pathSegments = filePath.split(path.sep);
  return pathSegments.some(segment => 
    segment.toLowerCase().includes('slidev') || 
    segment.toLowerCase().includes('slides')
  );
}

/**
 * Get content type with additional context information (server-side only)
 */
export function getContentTypeInfo(filePath: string) {
  const contentType = detectContentType(filePath);
  const isSlidevByPath = isSlidevPath(filePath);
  
  return {
    type: contentType,
    isSlidevByPath,
    extension: path.extname(filePath).toLowerCase(),
    filename: path.basename(filePath),
    isSlidePresentation: contentType === 'slidev' || contentType === 'reveal',
    isBrowserViewable: isBrowserViewable(contentType),
    requiresDownload: requiresDownload(contentType)
  };
}
