
import { ContentPageHandler } from '@/components/templates/content-page-handler';

export default async function ContentPage({
    searchParams,
}: {
    searchParams: Promise<{ lang?: string }>;
}) {
    const { lang } = await searchParams;
    const locale = lang || 'en';

    // basePath="" means we are listing the root content directory
    return <ContentPageHandler basePath="" slug={[]} locale={locale} searchParams={await searchParams} />;
}

export const metadata = {
    title: 'Content - Milav Dabgar',
    description: 'Explore blogs, resources, and study materials',
};
