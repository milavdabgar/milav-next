
import { getAllContentRecursive } from '@/lib/mdx';
import { GridPageLayout } from '@/components/layouts';
import Link from 'next/link';
import { Badge } from '@/components/ui/badge';

export default async function TagsIndexPage({
    searchParams,
}: {
    searchParams: Promise<{ lang?: string }>;
}) {
    const { lang } = await searchParams;
    const locale = lang || 'en';
    const isGujarati = locale === 'gu';

    const allContent = getAllContentRecursive('', locale);

    // Extract unique tags and count frequencies
    const tagCounts: { [key: string]: number } = {};

    allContent.forEach(item => {
        if (item.metadata.tags) {
            item.metadata.tags.forEach(tag => {
                // Normalize tag if needed (trim, lowercase? probably keep original for now)
                tagCounts[tag] = (tagCounts[tag] || 0) + 1;
            });
        }
    });

    const sortedTags = Object.entries(tagCounts).sort((a, b) => {
        // Sort by count desc, then alpha asc
        if (b[1] !== a[1]) return b[1] - a[1];
        return a[0].localeCompare(b[0]);
    });

    const breadcrumbs = [
        { label: 'Home', href: '/' },
        { label: 'Tags', href: '/tags' },
    ];

    return (
        <GridPageLayout
            title={isGujarati ? "ટૅગ્સ" : "Tags"}
            description={isGujarati ? "બધા વિષયો અને ટૅગ્સનું અન્વેષણ કરો" : "Explore all topics and tags"}
            breadcrumbs={breadcrumbs}
            columns={{ default: 1 }}
        >
            <div className="bg-card w-full p-8 rounded-lg border shadow-sm col-span-full">
                <div className="flex flex-wrap gap-3 justify-center">
                    {sortedTags.map(([tag, count]) => (
                        <Link key={tag} href={`/tags/${tag}`}>
                            <Badge
                                variant="secondary"
                                className="text-base px-4 py-2 hover:bg-secondary/80 transition-colors cursor-pointer flex items-center gap-2"
                            >
                                #{tag}
                                <span className="bg-background/50 px-1.5 py-0.5 rounded-full text-xs min-w-[1.25rem] text-center">
                                    {count}
                                </span>
                            </Badge>
                        </Link>
                    ))}

                    {sortedTags.length === 0 && (
                        <p className="text-muted-foreground">No tags found.</p>
                    )}
                </div>
            </div>
        </GridPageLayout>
    );
}
