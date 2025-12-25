import { getAllContent, getContentBySlug } from '@/lib/mdx';
import { getBreadcrumbs } from '@/lib/breadcrumbs';
import Link from 'next/link';
import { GridPageLayout } from '@/components/layouts';
import { ResourceCard } from '@/components/ui/resource-card';
import { Card } from '@/components/ui/card';
import { formatDate } from '@/lib/utils';

import { MDXRemote } from 'next-mdx-remote/rsc';
import { mdxComponents } from '@/components/mdx-components';

export default async function BlogPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const params = await searchParams;
  const locale = params.lang || 'en';
  const isGujarati = locale === 'gu';

  const posts = getAllContent('blog');
  const indexContent = getContentBySlug('blog', '_index', isGujarati ? 'gu' : undefined);

  const breadcrumbItems = getBreadcrumbs('blog', [], locale);

  const descriptionContent = indexContent?.content ? (
    <MDXRemote source={indexContent.content} components={mdxComponents} />
  ) : (
    indexContent?.metadata.description || (isGujarati
      ? 'ટ્યુટોરિયલ, ગાઇડ્સ અને ટેકનિકલ આર્ટિકલ્સ'
      : 'Tutorials, guides, and technical articles')
  );

  return (
    <GridPageLayout
      title={indexContent?.metadata.title || (isGujarati ? 'બ્લોગ' : 'Blog')}
      description={descriptionContent}
      columns={{ default: 1, md: 2, lg: 3 }}
      breadcrumbs={breadcrumbItems}
    >
      {posts.map((post) => (
        <ResourceCard
          key={post.slug}
          title={post.metadata.title}
          description={post.metadata.description || post.metadata.summary}
          date={post.metadata.date ? formatDate(post.metadata.date) : undefined}
          type="article"
          tags={post.metadata.tags}
          href={`/blog/${post.slug}${isGujarati ? '?lang=gu' : ''}`}
          className="h-full"
        />
      ))}

      {posts.length === 0 && (
        <Card className="col-span-full p-12 text-center">
          <p className="text-muted-foreground">
            {isGujarati ? 'કોઈ બ્લોગ પોસ્ટ્સ મળી નથી' : 'No blog posts found'}
          </p>
        </Card>
      )}
    </GridPageLayout>
  );
}

export const metadata = {
  title: 'Blog - Milav Dabgar',
  description: 'Technical tutorials, guides, and articles on electronics, programming, and data science',
};
