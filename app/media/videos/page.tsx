import { MDXRemote } from 'next-mdx-remote/rsc';
import { getContentBySlug, getAvailableLocales } from '@/lib/mdx';
import { SinglePageLayout } from '@/components/layouts';
import { SingleContentTemplate } from '@/components/templates';

export default async function VideosPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const params = await searchParams;
  const locale = params.lang || 'en';
  const content = await getContentBySlug('media', 'videos', locale);
  const availableLocales = await getAvailableLocales('media', 'videos');

  return (
    <SinglePageLayout
      backLink={{ href: '/media', label: 'Back to Media' }}
      locale={locale}
      availableLocales={availableLocales}
    >
      <SingleContentTemplate
        title={content.metadata.title}
        description={content.metadata.description}
      >
        <MDXRemote source={content.content} />
      </SingleContentTemplate>
    </SinglePageLayout>
  );
}

export const metadata = {
  title: 'Videos - Milav Dabgar',
  description: 'Curated video content',
};
