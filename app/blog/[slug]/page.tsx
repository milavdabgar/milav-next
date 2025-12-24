import { getContentBySlug, getAllContent, getAvailableLocales } from '@/lib/mdx';
import { mdxOptions } from '@/lib/mdx-options';
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

  // Get all posts for navigation
  const allPosts = getAllContent('blog', locale === 'gu' ? 'gu' : undefined);
  const currentIndex = allPosts.findIndex(p => p.slug === slug);
  const previousPost = currentIndex > 0 ? allPosts[currentIndex - 1] : undefined;
  const nextPost = currentIndex < allPosts.length - 1 ? allPosts[currentIndex + 1] : undefined;

  return (
    <SinglePageLayout>
      <BlogPostTemplate
        title={post.metadata.title}
        description={post.metadata.description}
        date={post.metadata.date}
        tags={post.metadata.tags}
        author="Milav Dabgar"
        slug={slug}
        locale={locale}
        previousPost={previousPost ? { slug: previousPost.slug, title: previousPost.metadata.title } : undefined}
        nextPost={nextPost ? { slug: nextPost.slug, title: nextPost.metadata.title } : undefined}
      >
        <MDXRemote source={post.content} options={mdxOptions} />
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
