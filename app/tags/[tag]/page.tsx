
import { getAllContent } from '@/lib/mdx';
import { GridPageLayout } from '@/components/layouts';
import { ResourceCard } from '@/components/ui/resource-card';
import { notFound } from 'next/navigation';
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

    // Fetch all content
    const allPosts = getAllContent('blog');
    // For resources we'd need a similar helper or crawl everything. 
    // For now, let's start with blog posts as they are the primary tagged content.

    const filteredPosts = allPosts.filter(post =>
        post.metadata.tags && post.metadata.tags.includes(decodedTag)
    );

    if (filteredPosts.length === 0) {
        // Optionally return 404 or just empty state
        // notFound();
    }

    const breadcrumbs = [
        { label: 'Home', href: '/' },
        { label: 'Tags', href: '#' },
        { label: `#${decodedTag}`, href: `/tags/${tag}` }
    ];

    return (
        <GridPageLayout
            title={`#${decodedTag}`}
            description={isGujarati
                ? `"${decodedTag}" ટેગ સાથેના લેખો`
                : `Articles tagged with "${decodedTag}"`}
            columns={{ default: 1, md: 2, lg: 3 }}
            breadcrumbs={breadcrumbs}
        >
            {filteredPosts.map((post) => (
                <ResourceCard
                    key={post.slug}
                    title={post.metadata.title}
                    description={post.metadata.description || post.metadata.summary}
                    date={post.metadata.date ? new Date(post.metadata.date).toLocaleDateString() : undefined}
                    type="article"
                    tags={post.metadata.tags}
                    href={`/blog/${post.slug}${isGujarati ? '?lang=gu' : ''}`}
                />
            ))}

            {filteredPosts.length === 0 && (
                <div className="col-span-full text-center py-12 text-muted-foreground">
                    No content found for this tag.
                </div>
            )}
        </GridPageLayout>
    );
}
