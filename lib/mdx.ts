
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
  tags?: string[];
  [key: string]: any;
}

export interface ContentItem {
  slug: string;
  metadata: ContentMetadata;
  content: string;
  filePath: string;
}

export function getContentBySlug(
  folder: string,
  slug: string,
  locale?: string
): ContentItem | null {
  try {
    const contentPath = path.join(contentDirectory, folder);

    // Potential file paths to check
    // 1. folder/slug.locale.mdx (Localized Leaf)
    // 2. folder/slug.mdx (Default Leaf)
    // 3. folder/slug/index.locale.mdx (Localized Bundle)
    // 4. folder/slug/index.mdx (Default Bundle)

    let possiblePaths: string[] = [];

    if (locale) {
      possiblePaths.push(path.join(contentPath, `${slug}.${locale}.mdx`));
    }
    possiblePaths.push(path.join(contentPath, `${slug}.mdx`));

    if (locale) {
      possiblePaths.push(path.join(contentPath, slug, `index.${locale}.mdx`));
    }
    possiblePaths.push(path.join(contentPath, slug, 'index.mdx'));

    // Find the first path that exists
    const fullPath = possiblePaths.find((p) => fs.existsSync(p));

    if (!fullPath) {
      return null;
    }

    const fileContents = fs.readFileSync(fullPath, 'utf8');
    const { data, content } = matter(fileContents);

    return {
      slug,
      metadata: data as ContentMetadata,
      content,
      filePath: fullPath,
    };
  } catch (error) {
    console.error(`Error reading content: ${folder}/${slug}`, error);
    return null;
  }
}

export function getAllContent(folder: string, locale?: string): ContentItem[] {
  try {
    const contentPath = path.join(contentDirectory, folder);

    if (!fs.existsSync(contentPath)) {
      return [];
    }

    const entries = fs.readdirSync(contentPath, { withFileTypes: true });

    // Identify potential slugs
    const slugs = new Set<string>();

    for (const entry of entries) {
      if (entry.isFile() && entry.name.endsWith('.mdx')) {
        // Leaf file
        const name = entry.name;
        if (name.startsWith('_index')) continue; // Skip section indices in list
        if (name.includes('.gu.')) {
          // It's a localized file.
          // If we are listing for 'en', we usually ignore it unless we want to include 'gu' posts in 'en' list?
          // Usually 'getAllContent' is for a specific locale list or all?
          // The previous logic filtered `!file.includes('.gu.')` indiscriminately.
          // Let's assume we collect slugs based on the main file, and `getContentBySlug` handles locale fallback.
          // So for list calculation, we valid check if base slug exists.
          // But actually, we just need the slug.
          const slug = name.replace(/\.gu\.mdx$/, '').replace(/\.mdx$/, '');
          slugs.add(slug);
        } else {
          const slug = name.replace(/\.mdx$/, '');
          slugs.add(slug);
        }
      } else if (entry.isDirectory()) {
        // Page bundle
        // Check if it has index.mdx or index.gu.mdx
        const hasIndex = fs.existsSync(path.join(contentPath, entry.name, 'index.mdx'));
        const hasGuIndex = fs.existsSync(path.join(contentPath, entry.name, 'index.gu.mdx'));

        if (hasIndex || hasGuIndex) {
          slugs.add(entry.name);
        }
      }
    }

    const allContent = Array.from(slugs)
      .map((slug) => getContentBySlug(folder, slug, locale))
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

// Recursive function to get all MDX files
export function getAllContentRecursive(folder: string = '', locale?: string): ContentItem[] {
  const items: ContentItem[] = [];
  const absolutePath = path.join(contentDirectory, folder);

  if (!fs.existsSync(absolutePath)) return [];

  const entries = fs.readdirSync(absolutePath, { withFileTypes: true });

  for (const entry of entries) {
    const relativePath = path.join(folder, entry.name);

    if (entry.isDirectory()) {
      items.push(...getAllContentRecursive(relativePath, locale));
    } else if (entry.isFile() && entry.name.endsWith('.mdx') && !entry.name.includes('.gu.')) {
      // We found an MDX file
      // Determine slug (relative path to content root, minus extension)
      // But getContentBySlug expects (folder, slug)

      // For recursively found files, strict (folder, slug) separation is tricky 
      // because getContentBySlug builds path as content/folder/slug.mdx
      // So we can pass 'folder' as the directory path relative to content, and 'slug' as filename without extension.

      const fileDirectory = folder;
      const slug = entry.name.replace(/\.mdx$/, '');

      // Skip _index.mdx if we only want "pages" or arguably include them. 
      // Usually tags are on leaf nodes or important section pages. Let's include everything.

      const content = getContentBySlug(fileDirectory, slug, locale);
      if (content) {
        // Adjust slug to be the full relative path from content root if needed for linking. 
        // However, getContentBySlug returns just the filename slug.
        // For global search/tags, we likely need the full path to link correctly.
        // Let's attach a 'fullSlug' or similar if needed, or rebuild the slug.

        // Construct a clickable URI-friendly slug
        const uriSlug = path.join(fileDirectory, slug).replace(/\\/g, '/'); // ensure forward slashes

        // We overwrite slug to be the full path so links work like /blog/slug or /resources/path/to/slug
        // But wait, /blog/slug is a specific route. /resources/path/to/slug is another.
        // We need to know which top-level section it belongs to for the Link href.

        // Let's store the full relative text path as the slug for now? 
        // Standard getAllContent just returns filename as slug for blog.
        // But for nested resources, simple filename isn't unique or sufficient.

        items.push({
          ...content,
          slug: uriSlug // Override slug with full relative path
        });
      }
    }
  }

  return items;
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
