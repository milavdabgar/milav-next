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
            const isMdx = item.endsWith('.mdx');
            const isLocaleFile = item.includes('.gu.');
            // Only include non-locale files or locale files if requested
            if (!isMdx) return false;
            if (locale === 'gu') return item.endsWith('.gu.mdx');
            return !item.includes('.gu.');
        }).map(file => {
            const filePath = path.normalize(`${fullPath}/${file}`);
            const fileContent = fs.readFileSync(filePath, 'utf8');
            const { data } = matter(fileContent);

            return {
                slug: file.replace(/\.gu\.mdx$/, '').replace(/\.mdx$/, ''),
                title: data.title,
                description: data.description,
                type: 'file',
                date: data.date
            };
        }).filter(f => f.slug !== '_index'); // Exclude index file from listing

        return { directories, files };
    } catch (error) {
        console.error('Error reading directory content:', error);
        return { directories: [], files: [] };
    }
}
