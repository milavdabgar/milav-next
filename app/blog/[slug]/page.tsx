import { getContentBySlug, getAllContent, getAvailableLocales } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { SinglePageLayout } from '@/components/layouts';
import { ContentTemplate } from '@/components/templates';
import { CodeBlock } from '@/components/ui/code-block';
import { Mermaid } from '@/components/ui/mermaid';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';

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
      <ContentTemplate
        title={post.metadata.title}
        description={post.metadata.description}
        date={post.metadata.date}
        readingTime={post.metadata.readingTime}
        tags={post.metadata.tags}
        author="Milav Dabgar"
        slug={slug}
        locale={locale}
        previousPost={previousPost ? { slug: previousPost.slug, title: previousPost.metadata.title } : undefined}
        nextPost={nextPost ? { slug: nextPost.slug, title: nextPost.metadata.title } : undefined}
        contentType="blog"
      >
        <MDXRemote
          source={post.content}
          options={{
            mdxOptions: {
              remarkPlugins: [remarkMath, remarkGfm],
              rehypePlugins: [rehypeKatex],
            }
          }}
          components={{
            code: ({ inline, className, children, ...props }: any) => {
              // Check if it's a code block (has className starting with language-) or inline
              const isCodeBlock = className && className.startsWith('language-');
              const language = className ? className.replace('language-', '') : '';

              if (language === 'mermaid') {
                return <Mermaid>{String(children)}</Mermaid>;
              }

              if (isCodeBlock) {
                return <CodeBlock className={className}>{String(children).replace(/\n$/, '')}</CodeBlock>;
              }

              // Inline code
              return <code className={className} {...props}>{children}</code>;
            }
          }}
        />
      </ContentTemplate>
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
