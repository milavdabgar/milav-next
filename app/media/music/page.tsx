import { MDXRemote } from 'next-mdx-remote/rsc';
import { getContentBySlug, getAvailableLocales } from '@/lib/mdx';
import { SinglePageLayout } from '@/components/layouts';

export default async function MusicPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const params = await searchParams;
  const locale = params.lang || 'en';
  const content = await getContentBySlug('media', 'music', locale);
  const availableLocales = await getAvailableLocales('media', 'music');

  return (
    <SinglePageLayout
      backLink={{ href: '/media', label: 'Back to Media' }}
      locale={locale}
      availableLocales={availableLocales}
    >
      <MDXRemote source={content.content} />
    </SinglePageLayout>
  );
}

export const metadata = {
  title: 'Music Collection - Milav Dabgar',
  description: 'Curated playlists of Hindi and English music',
};
