import { ContentPageHandler } from '@/components/templates/content-page-handler';

type Params = Promise<{ slug: string[]; lang?: string }>;

export default async function BlogDynamicPage({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string[] }>;
  searchParams: Promise<{ lang?: string }>;
}) {
  const { slug } = await params;
  const { lang } = await searchParams;
  const locale = lang || 'en';

  return <ContentPageHandler basePath="blog" slug={slug} locale={locale} searchParams={await searchParams} />;
}

export async function generateMetadata({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string[] }>;
  searchParams: Promise<{ lang?: string }>;
}) {
  const { slug } = await params;
  // We would ideally implementing metadata generation inside the handler or reuse helpers.
  // For now, let's keep it minimal or migrate metadata logic fully.
  // The handler renders the metadata for the page content, but Next.js metadata API is separate.
  // We should probably export a metadata generator helper or import one.

  // For now, falling back to minimal or no metadata generation here, relying on page content?
  // No, layout needs metadata. 
  // Let's implement basic metadata fetching reuse.

  return {
    title: `Blog: ${slug ? slug[slug.length - 1] : 'Details'}`,
    // Todo: properly fetch metadata
  };
}
