import { getContentBySlug } from '@/lib/mdx';
import { getDirectoryContent } from '@/lib/directory-utils';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { SinglePageLayout, GridPageLayout } from '@/components/layouts';
import { ContentTemplate as PageTemplate } from '@/components/templates';
import { CodeBlock } from '@/components/ui/code-block';
import { Mermaid } from '@/components/ui/mermaid';
import Link from 'next/link';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { Breadcrumbs } from "@/components/ui/breadcrumbs";
import { Folder, FileText } from 'lucide-react';
import fs from 'fs';
import path from 'path';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import { getBreadcrumbs } from '@/lib/breadcrumbs';

type Params = Promise<{ slug: string[]; lang?: string }>;

export default async function StudyMaterialDynamicPage({
    params,
    searchParams,
}: {
    params: Promise<{ slug: string[] }>;
    searchParams: Promise<{ lang?: string }>;
}) {
    const { slug } = await params;
    const searchParamsData = await searchParams;
    const locale = searchParamsData.lang || 'en';
    const isGujarati = locale === 'gu';

    const slugPath = slug.join('/');
    const folderPath = `resources/study-materials/${slug.slice(0, -1).join('/')}`;
    const fileName = slug[slug.length - 1];

    // 1. Try to find if it matches a file directly (e.g. subjects/maths)
    // Logic: Check if resources/study-materials/slug[0]/.../slug[n].mdx exists
    const fullFilePath = path.join('resources/study-materials', slugPath);
    const fileContent = getContentBySlug('resources/study-materials', slugPath, locale === 'gu' ? 'gu' : undefined);

    const breadcrumbItems = getBreadcrumbs('resources/study-materials', slug, locale);

    if (fileContent) {
        return (
            <SinglePageLayout>
                <PageTemplate
                    title={fileContent.metadata.title}
                    description={fileContent.metadata.description}
                    date={fileContent.metadata.date}
                    tags={fileContent.metadata.tags}
                    slug={slugPath}
                    contentType="resource"
                    breadcrumbs={breadcrumbItems}
                >
                    <div className="prose dark:prose-invert max-w-none">
                        <MDXRemote
                            source={fileContent.content}
                            options={{
                                mdxOptions: {
                                    remarkPlugins: [remarkMath, remarkGfm],
                                    rehypePlugins: [rehypeKatex],
                                }
                            }}
                            components={{
                                code: ({ inline, className, children, ...props }: any) => {
                                    const isCodeBlock = className && className.startsWith('language-');
                                    const language = className ? className.replace('language-', '') : '';

                                    if (language === 'mermaid') {
                                        return <Mermaid>{String(children)}</Mermaid>;
                                    }

                                    if (isCodeBlock) {
                                        return <CodeBlock className={className}>{String(children).replace(/\n$/, '')}</CodeBlock>;
                                    }

                                    return <code className={className} {...props}>{children}</code>;
                                }
                            }}
                        />
                    </div>
                </PageTemplate>
            </SinglePageLayout>
        );
    }

    // 2. If not a file, assumes it's a directory
    const directoryPath = `resources/study-materials/${slugPath}`;
    const { directories, files } = getDirectoryContent(directoryPath, locale === 'gu' ? 'gu' : undefined);

    const mdxFiles = files.filter((f: any) => f.type === 'mdx');
    const staticFiles = files.filter((f: any) => f.type !== 'mdx');

    // Try to find index file for this directory for metadata
    const indexContent = getContentBySlug(directoryPath, '_index', locale === 'gu' ? 'gu' : undefined);

    if (!indexContent && directories.length === 0 && files.length === 0) {
        notFound();
    }

    // Generate breadcrumbs
    // Breadcrumbs already generated above

    return (
        <GridPageLayout
            title={indexContent?.metadata.title || slug[slug.length - 1]}
            description={indexContent?.metadata.description}
            columns={{ default: 1, md: 2 }}
            breadcrumbs={breadcrumbItems}
        >
            {indexContent && (
                <div className="col-span-full prose dark:prose-invert max-w-none mb-8">
                    <MDXRemote
                        source={indexContent.content}
                        options={{
                            mdxOptions: {
                                remarkPlugins: [remarkMath, remarkGfm],
                                rehypePlugins: [rehypeKatex],
                            }
                        }}
                        components={{
                            code: ({ inline, className, children, ...props }: any) => {
                                const isCodeBlock = className && className.startsWith('language-');
                                const language = className ? className.replace('language-', '') : '';

                                if (language === 'mermaid') {
                                    return <Mermaid>{String(children)}</Mermaid>;
                                }

                                if (isCodeBlock) {
                                    return <CodeBlock className={className}>{String(children).replace(/\n$/, '')}</CodeBlock>;
                                }

                                return <code className={className} {...props}>{children}</code>;
                            }
                        }}
                    />
                </div>
            )}

            {directories.map((dir) => (
                <Link key={dir.slug} href={`/resources/study-materials/${slugPath}/${dir.slug}${isGujarati ? '?lang=gu' : ''}`}>
                    <Card className="h-full hover:bg-muted/50 transition-colors">
                        <CardHeader className="flex flex-row items-center gap-4">
                            <Folder className="h-8 w-8 text-blue-500" />
                            <div>
                                <CardTitle className="text-lg">{dir.title}</CardTitle>
                                <CardDescription>{dir.description}</CardDescription>
                            </div>
                        </CardHeader>
                    </Card>
                </Link>
            ))}

            {/* Articles Section */}
            {mdxFiles.length > 0 && (
                <div className="col-span-full mt-8">
                    <h2 className="text-2xl font-bold mb-4">Articles</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {mdxFiles.map((file) => (
                            <Link key={file.slug} href={`/resources/study-materials/${slugPath}/${file.slug}${isGujarati ? '?lang=gu' : ''}`}>
                                <Card className="h-full hover:bg-muted/50 transition-colors">
                                    <CardHeader className="flex flex-row items-center gap-4">
                                        <FileText className="h-8 w-8 text-green-500" />
                                        <div>
                                            <CardTitle className="text-lg">{file.title || file.slug}</CardTitle>
                                            <CardDescription>{file.description}</CardDescription>
                                        </div>
                                    </CardHeader>
                                </Card>
                            </Link>
                        ))}
                    </div>
                </div>
            )}

            {/* Static Files Section */}
            {staticFiles.length > 0 && (
                <div className="col-span-full mt-8">
                    <h2 className="text-2xl font-bold mb-4">Files</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {staticFiles.map((file) => {
                            // Construct the path for the API
                            // resource/study-materials/maths/book.pdf
                            const filePath = `resources/study-materials/${slugPath}/${file.filename}`;
                            const fileUrl = `/api/file?path=${encodeURIComponent(filePath)}`;

                            return (
                                <Link key={file.filename} href={fileUrl} target="_blank" rel="noopener noreferrer">
                                    <Card className="h-full hover:bg-muted/50 transition-colors">
                                        <CardHeader className="flex flex-row items-center gap-4">
                                            <FileText className="h-8 w-8 text-red-500" />
                                            <div>
                                                <CardTitle className="text-lg truncate max-w-[200px]" title={file.title}>{file.title}</CardTitle>
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
        </GridPageLayout>
    );
}

// Generate static params if needed, but for infinite depth dynamic routes 
// we might rely on dynamic rendering or generate a sensible depth
