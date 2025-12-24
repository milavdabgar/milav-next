import { MDXRemote } from 'next-mdx-remote/rsc';
import { getContentBySlug, getAvailableLocales } from '@/lib/mdx';
import { SinglePageLayout } from '@/components/layouts';

export default async function ProjectsPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const params = await searchParams;
  const locale = params.lang || 'en';
  const content = await getContentBySlug('projects', 'index', locale);
  const availableLocales = await getAvailableLocales('projects', 'index');

  return (
    <SinglePageLayout
      locale={locale}
      availableLocales={availableLocales}
    >
      <MDXRemote source={content.content} />
    </SinglePageLayout>
  );
}

export const metadata = {
  title: 'Projects - Milav Dabgar',
  description: 'Research work, technical implementations, and student-led innovations',
};
