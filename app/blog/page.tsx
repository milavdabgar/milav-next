import { ContentPageHandler } from '@/components/templates/content-page-handler';

export default async function BlogPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const { lang } = await searchParams;
  const locale = lang || 'en';

  return <ContentPageHandler basePath="blog" slug={[]} locale={locale} searchParams={await searchParams} />;
}

export const metadata = {
  title: 'Blog - Milav Dabgar',
  description: 'Technical tutorials, guides, and articles on electronics, programming, and data science',
};
