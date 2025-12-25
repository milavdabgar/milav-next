import { getContentBySlug } from '@/lib/mdx';
import { getBreadcrumbs } from '@/lib/breadcrumbs';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { GridPageLayout } from '@/components/layouts';
import { ResourceCard } from '@/components/ui/resource-card';
import Link from 'next/link';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import { cn } from '@/lib/utils';

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

    const breadcrumbItems = getBreadcrumbs('resources', [], locale);

    return (
        <GridPageLayout
            title={page.metadata.title}
            description={page.metadata.description}
            columns={{ default: 1, md: 2 }}
            breadcrumbs={breadcrumbItems}
        >
            <div className="col-span-full prose dark:prose-invert max-w-none mb-8">
                <MDXRemote
                    source={page.content}
                    options={{
                        mdxOptions: {
                            remarkPlugins: [remarkMath, remarkGfm],
                            rehypePlugins: [rehypeKatex],
                        }
                    }}
                    components={{
                        table: ({ className, ...props }: React.HTMLAttributes<HTMLTableElement>) => (
                            <div className="my-6 w-full overflow-y-auto">
                                <table className={cn("w-full caption-bottom text-sm", className)} {...props} />
                            </div>
                        ),
                        thead: ({ className, ...props }: React.HTMLAttributes<HTMLTableSectionElement>) => (
                            <thead className={cn("[&_tr]:border-b", className)} {...props} />
                        ),
                        tbody: ({ className, ...props }: React.HTMLAttributes<HTMLTableSectionElement>) => (
                            <tbody className={cn("[&_tr:last-child]:border-0", className)} {...props} />
                        ),
                        tr: ({ className, ...props }: React.HTMLAttributes<HTMLTableRowElement>) => (
                            <tr className={cn("border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted", className)} {...props} />
                        ),
                        th: ({ className, ...props }: React.ThHTMLAttributes<HTMLTableCellElement>) => (
                            <th className={cn("h-12 px-4 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0", className)} {...props} />
                        ),
                        td: ({ className, ...props }: React.TdHTMLAttributes<HTMLTableCellElement>) => (
                            <td className={cn("p-4 align-middle [&:has([role=checkbox])]:pr-0", className)} {...props} />
                        ),
                    }}
                />
            </div>

            {sections.map((section) => (
                <ResourceCard
                    key={section.slug}
                    title={section.title}
                    description={section.description}
                    type="folder"
                    className="h-full"
                    href={`/resources/${section.slug}${isGujarati ? '?lang=gu' : ''}`}
                />
            ))}
        </GridPageLayout>
    );
}

export const metadata = {
    title: 'Resources - Milav Dabgar',
    description: 'Educational resources, study materials, and tools',
};
