import { getContentBySlug } from '@/lib/mdx';
import { getBreadcrumbs } from '@/lib/breadcrumbs';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { SinglePageLayout } from '@/components/layouts';
import { ContentTemplate as PageTemplate } from '@/components/templates';
import Link from 'next/link';
import { Card, CardHeader, CardTitle, CardDescription } from '@/components/ui/card';
import fs from 'fs';
import path from 'path';

export default async function StudyMaterialsPage({
    searchParams,
}: {
    searchParams: Promise<{ lang?: string }>;
}) {
    const params = await searchParams;
    const locale = params.lang || 'en';
    const isGujarati = locale === 'gu';

    const page = getContentBySlug('resources/study-materials', '_index', locale === 'gu' ? 'gu' : undefined);

    if (!page) {
        notFound();
    }

    // Get departments manually by reading the directory or defining them
    // We'll read the directory to be dynamic
    const materialsPath = path.normalize(`${process.cwd()}/content/resources/study-materials`);
    const items = fs.readdirSync(materialsPath).filter(item => {
        const fullPath = path.normalize(`${materialsPath}/${item}`);
        return fs.statSync(fullPath).isDirectory() && !item.startsWith('.');
    });

    const departmentMap: Record<string, string> = {
        '32-ict': 'Interest Communication Technology (ICT)',
        '11-ec': 'Electronics & Communication (EC)',
        '16-it': 'Information Technology (IT)',
        '00-general': 'General / All Departments'
    };

    const departments = items.map(slug => ({
        slug,
        title: departmentMap[slug] || slug,
        description: isGujarati ? `${slug} વિભાગ માટે અભ્યાસ સામગ્રી` : `Study materials for ${departmentMap[slug] || slug}`
    }));

    const breadcrumbItems = getBreadcrumbs('resources/study-materials', [], locale);

    return (
        <SinglePageLayout>
            <PageTemplate
                title={page?.metadata.title || 'Study Materials'}
                description={page?.metadata.description}
                contentType="resource"
                breadcrumbs={breadcrumbItems}
            >
                <div className="prose dark:prose-invert max-w-none mb-8">
                    {page && <MDXRemote source={page.content} />}
                </div>

                <div className="grid gap-6 md:grid-cols-2">
                    {departments.map((dept) => (
                        <Link key={dept.slug} href={`/resources/study-materials/${dept.slug}${isGujarati ? '?lang=gu' : ''}`}>
                            <Card className="h-full hover:shadow-lg transition-shadow cursor-pointer">
                                <CardHeader>
                                    <CardTitle>{dept.title}</CardTitle>
                                    <CardDescription>{dept.description}</CardDescription>
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
    title: 'Study Materials - Milav Dabgar',
    description: 'Download study materials, notes, and papers for Diploma Engineering',
};
