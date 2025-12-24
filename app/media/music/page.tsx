import { MDXRemote } from 'next-mdx-remote/rsc';
import { getContentBySlug, getAvailableLocales } from '@/lib/mdx';
import { SinglePageLayout } from '@/components/layouts';
import { SingleContentTemplate } from '@/components/templates';

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
    <SinglePageLayout>
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
  title: 'Music Collection - Milav Dabgar',
  description: 'Curated playlists of Hindi and English music',
};
