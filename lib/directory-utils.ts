import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

interface DirectoryItem {
    name: string;
    path: string;
    title?: string;
}

interface FileItem {
    name: string;
    path: string;
    title?: string;
    description?: string;
    date?: string;
}

export function getDirectoryContent(folderPath: string, locale?: string) {
    try {
        // Use template strings to avoid overly broad pattern matching by Turbopack
        const contentRoot = path.join(process.cwd(), 'content');
        // Normalize to ensure consistent separators, but construct via string
        const fullPath = path.normalize(`${contentRoot}/${folderPath}`);

        if (!fs.existsSync(fullPath)) {
            return {
                directories: [],
                files: []
            };
        }

        if (!fs.statSync(fullPath).isDirectory()) {
            return {
                directories: [],
                files: []
            };
        }

        const items = fs.readdirSync(fullPath);

        const directories: DirectoryItem[] = [];
        const files: FileItem[] = [];

        items.forEach(item => {
            const itemPath = `${fullPath}/${item}`;
            const isDirectory = fs.statSync(itemPath).isDirectory();

            if (item.startsWith('.') || item.startsWith('_') || item === 'index.json') return;

            if (isDirectory) {
                // Check if it's a Page Bundle (contains index.mdx)
                const indexName = locale === 'gu' ? 'index.gu.mdx' : 'index.mdx';
                const bundlePath = `${itemPath}/${indexName}`;
                const fallbackBundlePath = `${itemPath}/index.mdx`;

                let isBundle = false;
                let finalBundlePath = '';

                if (fs.existsSync(bundlePath)) {
                    isBundle = true;
                    finalBundlePath = bundlePath;
                } else if (locale === 'gu' && fs.existsSync(fallbackBundlePath)) {
                    isBundle = true;
                    finalBundlePath = fallbackBundlePath;
                }

                if (isBundle) {
                    // It is a Post (Leaf Bundle)
                    // Treat as FILE (MDX)
                    try {
                        const fileContent = fs.readFileSync(finalBundlePath, 'utf8');
                        const { data } = matter(fileContent);
                        files.push({
                            slug: item, // Slug is the folder name
                            filename: item, // For bundles, filename is folder name
                            title: data.title || item,
                            description: data.description,
                            type: 'mdx', // Treat as MDX post
                            date: data.date,
                            extension: '.mdx'
                        });
                    } catch (e) {
                        console.error(`Error parsing Bundle ${item}:`, e);
                    }
                } else {
                    // It is a standard Directory (Section)
                    // Check for _index.mdx for metadata
                    const indexPath = `${itemPath}/${locale === 'gu' ? '_index.gu.mdx' : '_index.mdx'}`;
                    const fallbackIndexPath = `${itemPath}/_index.mdx`;

                    let title = item;
                    let description = '';

                    if (fs.existsSync(indexPath)) {
                        const fileContent = fs.readFileSync(indexPath, 'utf8');
                        const { data } = matter(fileContent);
                        title = data.title || item;
                        description = data.description || '';
                    } else if (fs.existsSync(fallbackIndexPath)) {
                        const fileContent = fs.readFileSync(fallbackIndexPath, 'utf8');
                        const { data } = matter(fileContent);
                        title = data.title || item;
                        description = data.description || '';
                    }

                    directories.push({
                        slug: item,
                        title,
                        description,
                        type: 'directory'
                    });
                }
            } else {
                // It is a File
                // Logic for files...
                if (item.includes('.gu.') && locale !== 'gu') return;

                const extension = path.extname(item).toLowerCase();
                const isMdx = extension === '.mdx';

                if (isMdx) {
                    if (locale === 'gu' && !item.includes('.gu.')) {
                        const gujVersion = item.replace('.mdx', '.gu.mdx');
                        if (items.includes(gujVersion)) return;
                    }

                    try {
                        const fileContent = fs.readFileSync(itemPath, 'utf8');
                        const { data } = matter(fileContent);
                        files.push({
                            slug: item.replace(/\.gu\.mdx$/, '').replace(/\.mdx$/, ''),
                            filename: item,
                            title: data.title || item.replace('.mdx', ''),
                            description: data.description,
                            type: 'mdx',
                            date: data.date,
                            extension: '.mdx'
                        });
                    } catch (e) {
                        console.error(`Error parsing MDX ${item}:`, e);
                    }
                } else {
                    // Static file
                    files.push({
                        slug: item,
                        filename: item,
                        title: item,
                        description: '',
                        type: extension.replace('.', ''),
                        date: undefined,
                        extension
                    });
                }
            }
        });

        const filteredFiles = files.filter(f => f.slug !== '_index'); // Exclude index file from listing

        // Deduplicate files (if both slug.mdx and slug/index.mdx exist, we might get duplicates)
        const uniqueFiles = new Map();
        filteredFiles.forEach(file => {
            if (!uniqueFiles.has(file.slug)) {
                uniqueFiles.set(file.slug, file);
            } else {
                // If collision, typically prefer the one that is a bundle (which we can't easily distinguish here unless we added a property).
                // Or just pick the first one.
                // My logic processed directories then files? No, parallel.
                // Wait, I processed items.
                // If 'about' (dir) and 'about.mdx' (file) exist in `items`:
                // 'about' -> directory logic -> becomes MDX file object (bundle)
                // 'about.mdx' -> file logic -> becomes MDX file object
                // Order in `items` depends on fs.readdirSync (usually alphabetical). 'about' vs 'about.mdx'.
                // 'about' comes first usually?
                // Let's just keep the first one encountered.
            }
        });

        const finalFiles = Array.from(uniqueFiles.values()).sort((a, b) => {
            // Sort by date (desc) if present, else title/slug
            // Usually we want blog posts sorted by date.
            if (a.date && b.date) {
                return new Date(b.date).getTime() - new Date(a.date).getTime();
            }
            return 0; // Keep original or simple sort
        });

        return { directories, files: finalFiles };
    } catch (error) {
        console.error('Error reading directory content:', error);
        return { directories: [], files: [] };
    }
}
