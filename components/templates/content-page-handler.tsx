import { getContentBySlug } from '@/lib/mdx';
import { getDirectoryContent } from '@/lib/directory-utils';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { SinglePageLayout, GridPageLayout } from '@/components/layouts';
import { ContentTemplate as PageTemplate } from '@/components/templates';
import { ResourceCard } from '@/components/ui/resource-card';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { Folder, FileText } from 'lucide-react';
import Link from 'next/link';
import path from 'path';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import { getBreadcrumbs } from '@/lib/breadcrumbs';
import { mdxComponents } from '@/components/mdx-components';
import { visit } from 'unist-util-visit';
import fs from 'fs';
import { formatDate } from '@/lib/utils';

// Custom rehype plugin to rewrite relative image paths
const rehypeRelativeImages = (options: { baseUrl: string }) => {
    return (tree: any) => {
        visit(tree, 'element', (node: any) => {
            if (node.tagName === 'img' && node.properties && node.properties.src) {
                const src = node.properties.src as string;
                if (src.startsWith('./')) {
                    // Replace ./ with the base URL
                    let baseUrl = options.baseUrl;
                    if (!baseUrl.endsWith('/')) baseUrl += '/';
                    node.properties.src = baseUrl + src.slice(2);
                }
            }
        });
    };
};

interface ContentPageHandlerProps {
    basePath: string;
    slug?: string[];
    locale: string;
    searchParams?: { [key: string]: string | string[] | undefined };
}

export async function ContentPageHandler({
    basePath,
    slug = [],
    locale,
    searchParams
}: ContentPageHandlerProps) {
    const isGujarati = locale === 'gu';
    const slugPath = slug.join('/');

    // Determine folder path for relative images (one level up from file)
    // If it's a folder listing, the base url is the folder itself.
    // If it's a file, it's the parent folder.

    // 1. Try to find if it matches a file directly (Article)
    // Check for slug.mdx or slug/index.mdx
    const fileContent = getContentBySlug(basePath, slugPath, isGujarati ? 'gu' : undefined);

    // Calculate Breadcrumbs
    const breadcrumbItems = getBreadcrumbs(basePath, slug, locale);

    if (fileContent) {
        // It's an article
        const parentFolder = slug.slice(0, -1).join('/');
        const relativeImageBaseUrl = `/${basePath}/${parentFolder}`;

        const fullPath = path.join(process.cwd(), 'content', basePath, slugPath);
        // We need to check if this specific path is a directory (implying index.mdx).
        let isBundle = false;
        try {
            if (fs.existsSync(fullPath) && fs.statSync(fullPath).isDirectory()) {
                isBundle = true;
            }
        } catch (e) { }

        const contentDir = isBundle ? slugPath : slug.slice(0, -1).join('/');
        const baseUrl = `/${basePath}/${contentDir}`;

        return (
            <SinglePageLayout>
                <PageTemplate
                    title={fileContent.metadata.title}
                    description={fileContent.metadata.description}
                    date={fileContent.metadata.date}
                    tags={fileContent.metadata.tags}
                    slug={slugPath}
                    contentType={basePath === 'blog' ? 'blog' : 'resource'}
                    breadcrumbs={breadcrumbItems}
                >
                    <MDXRemote
                        source={fileContent.content}
                        options={{
                            mdxOptions: {
                                remarkPlugins: [remarkMath, remarkGfm],
                                rehypePlugins: [
                                    rehypeKatex,
                                    [rehypeRelativeImages, { baseUrl }]
                                ],
                            }
                        }}
                        components={mdxComponents}
                    />
                </PageTemplate>
            </SinglePageLayout>
        );
    }

    // 2. If not a file/article, assume it's a directory (List View)
    // Note: getDirectoryContent expects 'folderPath' relative to 'content/'
    const directoryPath = slug.length > 0 ? `${basePath}/${slugPath}` : basePath;
    const { directories, files } = getDirectoryContent(directoryPath, isGujarati ? 'gu' : undefined);

    const mdxFiles = files.filter((f: any) => f.type === 'mdx');
    const staticFiles = files.filter((f: any) => f.type !== 'mdx');

    // Try to find _index file for metadata
    const indexContent = getContentBySlug(directoryPath, '_index', isGujarati ? 'gu' : undefined);

    // If nothing found at all, 404
    if (!indexContent && directories.length === 0 && files.length === 0) {
        notFound();
    }

    const title = indexContent?.metadata.title || (slug.length > 0 ? slug[slug.length - 1] : basePath);

    return (
        <GridPageLayout
            title={title}
            description={
                indexContent && (
                    <MDXRemote
                        source={indexContent.content}
                        options={{
                            mdxOptions: {
                                remarkPlugins: [remarkMath, remarkGfm],
                                rehypePlugins: [
                                    rehypeKatex,
                                    [rehypeRelativeImages, { baseUrl: `/${directoryPath}` }]
                                ],
                            }
                        }}
                        components={mdxComponents}
                    />
                )
            }
            columns={{ default: 1, md: 2, lg: 3 }}
            breadcrumbs={breadcrumbItems}
        >
            {/* Sub-directories (Folders) */}
            {directories.map((dir) => (
                <Link key={dir.slug} href={`/${[basePath, ...slug, dir.slug].filter(Boolean).join('/')}${isGujarati ? '?lang=gu' : ''}`}>
                    <ResourceCard
                        title={dir.title}
                        description={dir.description}
                        type="folder"
                        className="h-full"
                    />
                </Link>
            ))}

            {/* Articles (MDX Files) */}
            {(mdxFiles.length > 0 || directories.length > 0) && mdxFiles.length > 0 && (
                <>
                    {/* If we have mixed content (dirs + files), maybe separate them or just list them?
                          Resources page separated them. Let's separate if we have both. */}
                    {directories.length > 0 && <div className="col-span-full h-4" />}

                    {mdxFiles.map((file) => (
                        <Link key={file.slug} href={`/${[basePath, ...slug, file.slug].filter(Boolean).join('/')}${isGujarati ? '?lang=gu' : ''}`}>
                            <ResourceCard
                                title={file.title || file.slug}
                                description={file.description}
                                type="article"
                                date={file.date ? formatDate(file.date) : undefined}
                                className="h-full"
                            />
                        </Link>
                    ))}
                </>
            )}

            {/* Static Files */}
            {staticFiles.length > 0 && (
                <div className="col-span-full mt-12">
                    <h2 className="text-2xl font-bold mb-6">{isGujarati ? 'ફાઇલો' : 'Files'}</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {staticFiles.map((file) => {
                            const filePath = `${directoryPath}/${file.filename}`;
                            const fileUrl = `/api/file?path=${encodeURIComponent(filePath)}`;

                            return (
                                <Link key={file.filename} href={fileUrl} target="_blank" rel="noopener noreferrer">
                                    <Card className="h-full hover:bg-muted/50 transition-colors">
                                        <CardHeader className="flex flex-row items-center gap-4">
                                            <FileText className="h-8 w-8 text-red-500" />
                                            <div>
                                                <CardTitle className="text-lg truncate max-w-[200px]" title={file.title as string}>{file.title as string}</CardTitle>
                                                <CardDescription>{file.extension?.toUpperCase().replace('.', '') || 'FILE'}</CardDescription>
                                            </div>
                                        </CardHeader>
                                        <CardContent>
                                            <span className="text-sm font-medium text-blue-600 dark:text-blue-400">View File &rarr;</span>
                                        </CardContent>
                                    </Card>
                                </Link>
                            );
                        })}
                    </div>
                </div>
            )}

            {directories.length === 0 && mdxFiles.length === 0 && staticFiles.length === 0 && (
                <Card className="col-span-full p-12 text-center">
                    <p className="text-muted-foreground">
                        {isGujarati ? 'કોઈ સામગ્રી મળી નથી' : 'No content found'}
                    </p>
                </Card>
            )}
        </GridPageLayout>
    );
}
