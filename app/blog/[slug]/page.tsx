import { getContentBySlug, getAllContent } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Separator } from '@/components/ui/separator';
import { Calendar, Clock, ArrowLeft } from 'lucide-react';
import { formatDate } from '@/lib/utils';
import Link from 'next/link';

export default async function BlogPostPage({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ lang?: string }>;
}) {
  const { slug } = await params;
  const { lang } = await searchParams;
  const locale = lang === 'gu' ? 'gu' : undefined;
  
  const post = getContentBySlug('blog', slug, locale);

  if (!post) {
    notFound();
  }

  const isGujarati = locale === 'gu';

  return (
    <div className="container mx-auto px-4 py-8 max-w-4xl">
      {/* Back Button */}
      <Link href="/blog">
        <Button variant="ghost" size="sm" className="mb-6">
          <ArrowLeft className="mr-2 h-4 w-4" />
          {isGujarati ? 'બ્લોગ પર પાછા જાઓ' : 'Back to Blog'}
        </Button>
      </Link>

      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-4">
          <div className="flex-1">
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
          </div>
          <Button asChild variant="ghost" size="sm">
            <a href={`/blog/${slug}${isGujarati ? '' : '?lang=gu'}`}>
              {isGujarati ? 'English' : 'ગુજરાતી'}
            </a>
          </Button>
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

      {/* Content */}
      <article className="prose prose-neutral dark:prose-invert max-w-none">
        <MDXRemote source={post.content} />
      </article>

      <Separator className="my-8" />

      {/* Footer */}
      <div className="flex justify-between items-center">
        <Link href="/blog">
          <Button variant="outline">
            <ArrowLeft className="mr-2 h-4 w-4" />
            {isGujarati ? 'બધી પોસ્ટ્સ' : 'All Posts'}
          </Button>
        </Link>
      </div>
    </div>
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
  const { lang } = await searchParams;
  const locale = lang === 'gu' ? 'gu' : undefined;
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
