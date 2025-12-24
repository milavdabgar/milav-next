// src/lib/content-types-client.ts
// Client-side content type utilities (no fs dependencies)

export type ContentType = 'markdown' | 'slidev' | 'pdf' | 'html' | 'reveal' | 'docx' | 'pptx' | 'xlsx' | 'image' | 'text' | 'other';

/**
 * Check if a file should be viewable in browser
 */
export function isBrowserViewable(contentType: ContentType): boolean {
  return ['pdf', 'html', 'image', 'text', 'markdown', 'slidev', 'reveal'].includes(contentType);
}

/**
 * Check if a file should be downloaded instead of viewed
 */
export function requiresDownload(contentType: ContentType): boolean {
  return ['docx', 'pptx', 'xlsx', 'other'].includes(contentType);
}

/**
 * Get MIME type for a content type
 */
export function getMimeType(contentType: ContentType, extension?: string): string {
  const mimeMap: Record<ContentType, string> = {
    'pdf': 'application/pdf',
    'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
    'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'html': 'text/html',
    'markdown': 'text/markdown',
    'slidev': 'text/markdown',
    'reveal': 'text/html',
    'image': 'image/*',
    'text': 'text/plain',
    'other': 'application/octet-stream'
  };
  
  // For images, try to be more specific
  if (contentType === 'image' && extension) {
    const imgMimeMap: Record<string, string> = {
      '.jpg': 'image/jpeg',
      '.jpeg': 'image/jpeg',
      '.png': 'image/png',
      '.gif': 'image/gif',
      '.svg': 'image/svg+xml',
      '.webp': 'image/webp',
      '.bmp': 'image/bmp',
      '.ico': 'image/x-icon'
    };
    return imgMimeMap[extension.toLowerCase()] || 'image/*';
  }
  
  return mimeMap[contentType] || 'application/octet-stream';
}

/**
 * Detect content type based on file extension only (client-safe)
 */
export function detectContentTypeFromExtension(extension: string): ContentType {
  const ext = extension.toLowerCase();
  
  if (ext === '.pdf') return 'pdf';
  if (ext === '.docx') return 'docx';
  if (ext === '.pptx') return 'pptx';
  if (ext === '.xlsx') return 'xlsx';
  if (['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.bmp', '.ico'].includes(ext)) return 'image';
  if (['.txt', '.csv', '.json', '.xml'].includes(ext)) return 'text';
  if (ext === '.html' || ext === '.htm') return 'html';
  if (ext === '.md') return 'markdown';
  
  return 'other';
}