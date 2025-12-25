import { getContentBySlug } from '@/lib/mdx';
import { getBreadcrumbs } from '@/lib/breadcrumbs';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { GridPageLayout } from '@/components/layouts';
import { ResourceCard } from '@/components/ui/resource-card';
import Link from 'next/link';
import fs from 'fs';
import path from 'path';
import { mdxComponents } from '@/components/mdx-components';

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
        <GridPageLayout
            title={page?.metadata.title || 'Study Materials'}
            description={page?.metadata.description}
            columns={{ default: 1, md: 2 }}
            breadcrumbs={breadcrumbItems}
        >
            <div className="col-span-full max-w-none mb-8">
                {page && <MDXRemote source={page.content} options={{
                    mdxOptions: {
                        remarkPlugins: [],
                        rehypePlugins: [],
                    }
                }}
                    components={mdxComponents}
                />}
            </div>

            {departments.map((dept) => (
                <ResourceCard
                    key={dept.slug}
                    title={dept.title}
                    description={dept.description}
                    type="folder"
                    className="h-full"
                    href={`/resources/study-materials/${dept.slug}${isGujarati ? '?lang=gu' : ''}`}
                />
            ))}
        </GridPageLayout>
    );
}

export const metadata = {
    title: 'Study Materials - Milav Dabgar',
    description: 'Download study materials, notes, and papers for Diploma Engineering',
};
