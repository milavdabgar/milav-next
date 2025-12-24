import { getContentBySlug, getAllContent, getAvailableLocales } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { SinglePageLayout } from '@/components/layouts';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { Calendar } from 'lucide-react';
import { formatDate } from '@/lib/utils';

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
      {/* Post Header */}
      <div className="mb-8 -mt-4">
        <h1 className="text-4xl font-bold tracking-tight mb-4">
          {post.metadata.title}
        </h1>
        {post.metadata.description && (
          <p className="text-xl text-muted-foreground mb-4">
            {post.metadata.description}
          </p>
        )}
        <div className="flex flex-wrap items-center gap-4 text-sm text-muted-foreground">
          {post.metadata.date && (
            <div className="flex items-center">
              <Calendar className="mr-2 h-4 w-4" />
              {formatDate(post.metadata.date)}
            </div>
          )}
        </div>

        {post.metadata.tags && post.metadata.tags.length > 0 && (
          <div className="flex flex-wrap gap-2 mt-4">
            {post.metadata.tags.map((tag: string) => (
              <Badge key={tag} variant="secondary">
                {tag}
              </Badge>
            ))}
          </div>
        )}
      </div>

      <Separator className="my-8" />

      
      {/* Article Content */}
      <MDXRemote source={post.content} />
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
