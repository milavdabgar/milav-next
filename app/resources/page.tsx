import { getContentBySlug } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { SinglePageLayout } from '@/components/layouts';
import { SingleContentTemplate as PageTemplate } from '@/components/templates';
import Link from 'next/link';
import { Card, CardHeader, CardTitle, CardDescription } from '@/components/ui/card';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

export default async function ResourcesPage({
    searchParams,
}: {
    searchParams: Promise<{ lang?: string }>;
}) {
    const params = await searchParams;
    const locale = params.lang || 'en';
    const isGujarati = locale === 'gu';

    const page = getContentBySlug('resources', '_index', locale === 'gu' ? 'gu' : undefined);

    if (!page) {
        notFound();
    }

    // Define available resource sections manually for now or fetch dynamically 
    // if we add more top-level sections
    const sections = [
        {
            slug: 'study-materials',
            title: isGujarati ? 'અભ્યાસ ડાઉનલોડ્સ' : 'Study Materials',
            description: isGujarati
                ? 'GTU ડિપ્લોમા અભ્યાસક્રમ માટે નોંધો, પેપર્સ અને પુસ્તકો'
                : 'Notes, papers, and books for GTU Diploma curriculum',
        },
        // Add more sections as they are migrated
    ];

    return (
        <SinglePageLayout>
            <PageTemplate
                title={page.metadata.title}
                description={page.metadata.description}
            >
                <div className="prose dark:prose-invert max-w-none mb-8">
                    <MDXRemote
                        source={page.content}
                        options={{
                            mdxOptions: {
                                remarkPlugins: [remarkMath],
                                rehypePlugins: [rehypeKatex],
                            }
                        }}
                    />
                </div>

                <div className="grid gap-6 md:grid-cols-2">
                    {sections.map((section) => (
                        <Link key={section.slug} href={`/resources/${section.slug}${isGujarati ? '?lang=gu' : ''}`}>
                            <Card className="h-full hover:shadow-lg transition-shadow cursor-pointer">
                                <CardHeader>
                                    <CardTitle>{section.title}</CardTitle>
                                    <CardDescription>{section.description}</CardDescription>
                                </CardHeader>
                            </Card>
                        </Link>
                    ))}
                </div>
            </PageTemplate>
        </SinglePageLayout>
    );
}

export const metadata = {
    title: 'Resources - Milav Dabgar',
    description: 'Educational resources, study materials, and tools',
};
