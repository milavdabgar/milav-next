import { ContentPageHandler } from '@/components/templates/content-page-handler';

export default async function UniversalContentPage({
    params,
    searchParams,
}: {
    params: Promise<{ slug: string[] }>;
    searchParams: Promise<{ lang?: string }>;
}) {
    const { slug } = await params;
    const { lang } = await searchParams;
    const locale = lang || 'en';

    // We pass an empty basePath because the 'slug' array captured by [...slug]
    // contains the full path from the root.
    // E.g. /categories/tech -> slug: ['categories', 'tech']
    // ContentPageHandler with basePath="" will look in content/categories/tech
    return <ContentPageHandler basePath="" slug={slug} locale={locale} searchParams={await searchParams} />;
}

// Generate dynamic metadata if needed, or let ContentPageHandler handle the content.
// Since ContentPageHandler renders the page, metadata export here might need 
// to duplicate logic to be accurate, but Next.js needs a generateMetadata function here.
// For now, simple fallback or we can extract metadata logic later.
export async function generateMetadata({
    params,
    searchParams,
}: {
    params: Promise<{ slug: string[] }>;
    searchParams: Promise<{ lang?: string }>;
}) {
    const { slug } = await params;
    const { lang } = await searchParams;
    const title = slug[slug.length - 1];

    // Capitalize first letter for a basic title
    const formattedTitle = title.charAt(0).toUpperCase() + title.slice(1);

    return {
        title: `${formattedTitle} - Milav Dabgar`,
    };
}
