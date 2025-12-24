import { getContentBySlug, getAllContent, getAvailableLocales } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { SinglePageLayout } from '@/components/layouts';
import { BlogPostTemplate } from '@/components/templates';

export default async function BlogPostPage({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ lang?: string }>;
}) {
  const { slug } = await params;
  const searchParamsData = await searchParams;
  const locale = searchParamsData.lang || 'en';
  
  const post = getContentBySlug('blog', slug, locale === 'gu' ? 'gu' : undefined);

  if (!post) {
    notFound();
  }

  const availableLocales = await getAvailableLocales('blog', slug);

  return (
    <SinglePageLayout
      backLink={{ href: '/blog', label: 'Back to Blog' }}
      locale={locale}
      availableLocales={availableLocales}
    >
      <BlogPostTemplate
        title={post.metadata.title}
        description={post.metadata.description}
        date={post.metadata.date}
        tags={post.metadata.tags}
        author="Milav Dabgar"
      >
        <MDXRemote source={post.content} />
      </BlogPostTemplate>
    </SinglePageLayout>
  );
}

export async function generateStaticParams() {
  const posts = getAllContent('blog');
  return posts.map((post) => ({
    slug: post.slug,
  }));
}

export async function generateMetadata({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ lang?: string }>;
}) {
  const { slug } = await params;
  const searchParamsData = await searchParams;
  const locale = searchParamsData.lang === 'gu' ? 'gu' : undefined;
  const post = getContentBySlug('blog', slug, locale);

  if (!post) {
    return {
      title: 'Post Not Found',
    };
  }

  return {
    title: post.metadata.title,
    description: post.metadata.description || post.metadata.summary,
  };
}
