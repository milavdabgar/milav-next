
import { getAllContentRecursive } from '@/lib/mdx';
import { GridPageLayout } from '@/components/layouts';
import { ResourceCard } from '@/components/ui/resource-card';
import { getBreadcrumbs } from '@/lib/breadcrumbs';

export default async function TagPage({
    params,
    searchParams,
}: {
    params: Promise<{ tag: string }>;
    searchParams: Promise<{ lang?: string }>;
}) {
    const { tag } = await params;
    const { lang } = await searchParams;
    const locale = lang || 'en';
    const isGujarati = locale === 'gu';

    const decodedTag = decodeURIComponent(tag);

    // Fetch all content recursively from root content directory
    const allContent = getAllContentRecursive('', locale);

    const filteredPosts = allContent.filter(post =>
        post.metadata.tags && post.metadata.tags.includes(decodedTag)
    );

    const breadcrumbs = [
        { label: 'Home', href: '/' },
        { label: 'Tags', href: '/tags' },
        { label: `#${decodedTag}`, href: `/tags/${tag}` }
    ];

    return (
        <GridPageLayout
            title={`#${decodedTag}`}
            description={isGujarati
                ? `"${decodedTag}" ટેગ સાથેના લેખો`
                : `Content tagged with "${decodedTag}"`}
            columns={{ default: 1, md: 2, lg: 3 }}
            breadcrumbs={breadcrumbs}
        >
            {filteredPosts.map((post) => {
                // Determine correct href based on folder structure
                let href = '';
                if (post.slug.startsWith('blog/')) {
                    href = `/${post.slug}${isGujarati ? '?lang=gu' : ''}`;
                } else if (post.slug.startsWith('resources/')) {
                    href = `/${post.slug}${isGujarati ? '?lang=gu' : ''}`;
                } else {
                    // Fallback for logic consistency, though practically it's one of the above usually
                    href = `/resources/${post.slug}${isGujarati ? '?lang=gu' : ''}`;
                }

                // Determine type
                // This is a rough heuristic. If it has children it's a folder, but here we are listing MDX files.
                // MDX files are "articles" or "files" generally. 
                // _index.mdx represents a section/folder.
                const isSection = post.slug.endsWith('_index') || post.slug.endsWith('/_index');
                const type = isSection ? 'folder' : 'article';

                return (
                    <ResourceCard
                        key={post.slug}
                        title={post.metadata.title}
                        description={post.metadata.description || post.metadata.summary}
                        date={post.metadata.date ? new Date(post.metadata.date).toLocaleDateString() : undefined}
                        type={type}
                        tags={post.metadata.tags}
                        href={href}
                    />
                );
            })}

            {filteredPosts.length === 0 && (
                <div className="col-span-full text-center py-12 text-muted-foreground">
                    No content found for this tag.
                </div>
            )}
        </GridPageLayout>
    );
}
