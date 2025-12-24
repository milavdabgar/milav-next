import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

const contentDirectory = path.join(process.cwd(), 'content');

export interface ContentMetadata {
  title: string;
  description?: string;
  summary?: string;
  date?: string;
  showDate?: boolean;
  showAuthor?: boolean;
  showReadingTime?: boolean;
  showEdit?: boolean;
  [key: string]: any;
}

export interface ContentItem {
  slug: string;
  metadata: ContentMetadata;
  content: string;
}

export function getContentBySlug(
  folder: string,
  slug: string,
  locale?: string
): ContentItem | null {
  try {
    const fileName = locale ? `${slug}.${locale}.mdx` : `${slug}.mdx`;
    const fallbackFileName = `${slug}.mdx`;
    
    const contentPath = path.join(contentDirectory, folder);
    
    // Try locale-specific file first, then fall back to default
    let fullPath = path.join(contentPath, fileName);
    if (!fs.existsSync(fullPath) && locale) {
      fullPath = path.join(contentPath, fallbackFileName);
    }
    
    if (!fs.existsSync(fullPath)) {
      return null;
    }

    const fileContents = fs.readFileSync(fullPath, 'utf8');
    const { data, content } = matter(fileContents);

    return {
      slug,
      metadata: data as ContentMetadata,
      content,
    };
  } catch (error) {
    console.error(`Error reading content: ${folder}/${slug}`, error);
    return null;
  }
}

export function getAllContent(folder: string): ContentItem[] {
  try {
    const contentPath = path.join(contentDirectory, folder);
    
    if (!fs.existsSync(contentPath)) {
      return [];
    }

    const files = fs.readdirSync(contentPath);
    const mdxFiles = files.filter((file) => 
      file.endsWith('.mdx') && !file.includes('.gu.')
    );

    const allContent = mdxFiles
      .map((file) => {
        const slug = file.replace(/\.mdx$/, '');
        return getContentBySlug(folder, slug);
      })
      .filter((item): item is ContentItem => item !== null);

    return allContent.sort((a, b) => {
      if (a.metadata.date && b.metadata.date) {
        return new Date(b.metadata.date).getTime() - new Date(a.metadata.date).getTime();
      }
      return 0;
    });
  } catch (error) {
    console.error(`Error reading content folder: ${folder}`, error);
    return [];
  }
}

export function getAvailableLocales(folder: string, slug: string): string[] {
  try {
    const contentPath = path.join(contentDirectory, folder);
    const files = fs.readdirSync(contentPath);
    
    const locales = ['en']; // Default English
    
    // Check for Gujarati version
    if (files.includes(`${slug}.gu.mdx`)) {
      locales.push('gu');
    }
    
    return locales;
  } catch (error) {
    return ['en'];
  }
}
