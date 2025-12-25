import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

export function getDirectoryContent(folderPath: string, locale?: string) {
    try {
        const fullPath = path.normalize(`${process.cwd()}/content/${folderPath}`);

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

        const directories = items.filter(item => {
            const itemPath = path.normalize(`${fullPath}/${item}`);
            return fs.statSync(itemPath).isDirectory() && !item.startsWith('.');
        }).map(dir => {
            // Try to read _index.mdx inside the directory to get metadata
            const indexPath = path.normalize(`${fullPath}/${dir}/${locale === 'gu' ? '_index.gu.mdx' : '_index.mdx'}`);
            const fallbackIndexPath = path.normalize(`${fullPath}/${dir}/_index.mdx`);

            let title = dir;
            let description = '';

            if (fs.existsSync(indexPath)) {
                const fileContent = fs.readFileSync(indexPath, 'utf8');
                const { data } = matter(fileContent);
                title = data.title || dir;
                description = data.description || '';
            } else if (fs.existsSync(fallbackIndexPath)) {
                const fileContent = fs.readFileSync(fallbackIndexPath, 'utf8');
                const { data } = matter(fileContent);
                title = data.title || dir;
                description = data.description || '';
            }

            return {
                slug: dir,
                title,
                description,
                type: 'directory'
            };
        });

        const files = items.filter(item => {
            const isDirectory = fs.statSync(path.join(fullPath, item)).isDirectory();
            if (isDirectory) return false;
            if (item.startsWith('.')) return false;
            if (item.startsWith('_')) return false;
            if (item === 'index.json') return false; // generated index not needed in listing

            // If it's a locale file (e.g. .gu.mdx), only include if locale matches
            if (item.includes('.gu.')) {
                return locale === 'gu';
            }
            // If it's a base file (e.g. .mdx) and we are looking for 'gu', 
            // check if .gu.mdx exists? No, typical logic for others is loose.
            // For now, let's keep simple: include if not a hidden/system file
            return true;
        }).map(file => {
            const filePath = path.normalize(`${fullPath}/${file}`);
            const extension = path.extname(file).toLowerCase();
            const isMdx = extension === '.mdx';

            let title = file;
            let description = '';
            let date = undefined;
            let type = 'file';

            if (isMdx) {
                try {
                    const fileContent = fs.readFileSync(filePath, 'utf8');
                    const { data } = matter(fileContent);
                    title = data.title || file.replace('.mdx', '');
                    description = data.description;
                    date = data.date;
                    type = 'mdx';
                } catch (e) {
                    console.error(`Error parsing MDX ${file}:`, e);
                }
            } else {
                // For static files
                title = file;
                // Maybe readable format?
                type = extension.replace('.', '');
            }

            return {
                slug: file.replace(/\.gu\.mdx$/, '').replace(/\.mdx$/, ''), // For MDX, slug is without extension
                filename: file, // Keep original filename for static files
                title,
                description,
                type,
                date,
                extension
            };
        }).filter(f => f.slug !== '_index'); // Exclude index file from listing

        return { directories, files };
    } catch (error) {
        console.error('Error reading directory content:', error);
        return { directories: [], files: [] };
    }
}
