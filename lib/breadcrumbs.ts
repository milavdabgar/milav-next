
import { getContentBySlug } from '@/lib/mdx';
import { BreadcrumbItem } from '@/components/ui/breadcrumbs';

// Fallback map for common departments
const departmentMap: Record<string, string> = {
    '32-ict': 'Interest Communication Technology (ICT)',
    '11-ec': 'Electronics & Communication (EC)',
    '16-it': 'Information Technology (IT)',
    '00-general': 'General / All Departments'
};

export function getBreadcrumbs(basePath: string, slug: string[], locale?: string): BreadcrumbItem[] {
    const breadcrumbs: BreadcrumbItem[] = [];

    // Add Home
    // breadcrumbs.push({ label: 'Home', href: '/' });
    // Breadcrumbs component adds Home automatically

    // Handle base path (e.g. Resources -> Study Materials)
    // This part is static for now based on the section
    // Add 'Content' node as requested
    breadcrumbs.push({ label: 'Content', href: '#' });

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

        // Construct the directory path to check for _index
        const dirPathToCheck = currentDir === '' ? part : `${currentDir}/${part}`;

        let label = part;

        // 1. Check Metadata via _index.mdx
        try {
            const indexData = getContentBySlug(dirPathToCheck, '_index', locale === 'gu' ? 'gu' : undefined);

            if (indexData) {
                label = indexData.metadata.title;
            } else {
                // 2. Check Department Map Fallback
                if (departmentMap[part]) {
                    label = departmentMap[part];
                }
                // 3. Check if it is a file (leaf node)
                else if (index === slug.length - 1) {
                    const fileData = getContentBySlug(currentDir, part, locale === 'gu' ? 'gu' : undefined);
                    if (fileData) {
                        label = fileData.metadata.title;
                    } else {
                        // Fallback formatting
                        label = part.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
                    }
                } else {
                    // Fallback formatting
                    label = part.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
                }
            }
        } catch (e) {
            // Fallback
            if (departmentMap[part]) {
                label = departmentMap[part];
            } else {
                label = part.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ');
            }
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
