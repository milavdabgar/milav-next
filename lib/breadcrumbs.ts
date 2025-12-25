
import { getContentBySlug } from '@/lib/mdx';
import { BreadcrumbItem } from '@/components/ui/breadcrumbs';

export function getBreadcrumbs(basePath: string, slug: string[], locale?: string): BreadcrumbItem[] {
    const breadcrumbs: BreadcrumbItem[] = [];

    // Add Home
    // breadcrumbs.push({ label: 'Home', href: '/' });
    // Breadcrumbs component adds Home automatically

    // Handle base path (e.g. Resources -> Study Materials)
    // This part is static for now based on the section
    if (basePath.includes('resources')) {
        breadcrumbs.push({ label: 'Resources', href: '/resources' });
        if (basePath.includes('study-materials')) {
            breadcrumbs.push({ label: 'Study Materials', href: '/resources/study-materials' });
        }
    } else if (basePath.includes('blog')) {
        breadcrumbs.push({ label: 'Blog', href: '/blog' });
    }

    // Iterate through slug parts
    let currentPath = basePath.startsWith('resources') ? '/resources/study-materials' : '/blog';

    // We need to construct the full filesystem path to check for _index.mdx
    // Base dir relative to content
    // e.g. resources/study-materials
    let currentDir = basePath.replace(/^\/|\/$/g, '');

    slug.forEach((part, index) => {
        currentPath += `/${part}`;

        // Construct the path to the directory or file
        // For breadcrumbs, we want the title of the directory/file

        // If it's the last part and it's a file (not a dir), currentDir + part
        // If it's a directory, currentDir + part + _index

        // We try to fetch metadata for this segment.
        // We assume each segment corresponds to a directory unless it's the last one which might be a file.
        // However, in our structure, even leaf nodes might just be files.
        // But intermediate nodes are definitely directories.

        const segmentPath = `${currentDir}/${part}`;

        // Try to get index content for this segment (treating it as a directory)
        // We pass the full path up to this segment as the 'directory' argument for getContentBySlug
        // and '_index' as the slug.

        // Wait, getContentBySlug takes (directory, slug).
        // If we want title of `16-it` folder:
        // getContentBySlug('resources/study-materials/16-it', '_index', locale)

        // Construct the directory path to check for _index
        const dirPathToCheck = currentDir === '' ? part : `${currentDir}/${part}`;

        let label = part;

        // Only try to fetch metadata if we are not at the leaf node, 
        // OR if we are at the leaf node but we want to confirm its title (if passed from page, usually we have it).
        // Actually, let's just try to resolve it.

        // For intermediate steps (directories):
        try {
            const indexData = getContentBySlug(dirPathToCheck, '_index', locale === 'gu' ? 'gu' : undefined);
            if (indexData) {
                label = indexData.metadata.title;
            } else if (index === slug.length - 1) {
                // If it's the last item, it might be a file (not directory)
                // e.g. .../java (java.mdx)
                // getContentBySlug('resources/study-materials/...', 'java')
                const fileData = getContentBySlug(currentDir, part, locale === 'gu' ? 'gu' : undefined);
                if (fileData) {
                    label = fileData.metadata.title;
                } else {
                    // Fallback formatting
                    label = part.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
                }
            } else {
                // Fallback formatting for intermediate directories without _index (shouldn't happen often)
                label = part.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
            }
        } catch (e) {
            // Fallback
            label = part.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
        }

        breadcrumbs.push({
            label,
            href: currentPath
        });

        // Update currentDir for next iteration
        currentDir = `${currentDir}/${part}`;
    });

    return breadcrumbs;
}
