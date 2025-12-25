import { getAllContent } from '@/lib/mdx';
import { getBreadcrumbs } from '@/lib/breadcrumbs';
import Link from 'next/link';
import { GridPageLayout } from '@/components/layouts';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Calendar, Clock, Tag } from 'lucide-react';
import { formatDate } from '@/lib/utils';

export default async function BlogPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const params = await searchParams;
  const locale = params.lang || 'en';
  const isGujarati = locale === 'gu';

  const posts = getAllContent('blog');

  const breadcrumbItems = getBreadcrumbs('blog', [], locale);

  return (
    <GridPageLayout
      title={isGujarati ? 'બ્લોગ' : 'Blog'}
      description={isGujarati
        ? 'ટ્યુટોરિયલ, ગાઇડ્સ અને ટેકનિકલ આર્ટિકલ્સ'
        : 'Tutorials, guides, and technical articles'}
      columns={{ default: 1, md: 2, lg: 3 }}
      breadcrumbs={breadcrumbItems}
    >
      {posts.map((post) => (
        <Link key={post.slug} href={`/blog/${post.slug}${isGujarati ? '?lang=gu' : ''}`}>
          <Card className="h-full hover:shadow-lg transition-shadow">
            <CardHeader>
              <CardTitle className="line-clamp-2">
                {post.metadata.title}
              </CardTitle>
              <CardDescription className="line-clamp-3">
                {post.metadata.description || post.metadata.summary}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {post.metadata.date && (
                  <div className="flex items-center text-sm text-muted-foreground">
                    <Calendar className="mr-2 h-4 w-4" />
                    {formatDate(post.metadata.date)}
                  </div>
                )}
                {post.metadata.tags && post.metadata.tags.length > 0 && (
                  <div className="flex flex-wrap gap-1">
                    {post.metadata.tags.slice(0, 3).map((tag: string) => (
                      <Badge key={tag} variant="secondary" className="text-xs">
                        {tag}
                      </Badge>
                    ))}
                    {post.metadata.tags.length > 3 && (
                      <Badge variant="outline" className="text-xs">
                        +{post.metadata.tags.length - 3}
                      </Badge>
                    )}
                  </div>
                )}
              </div>
            </CardContent>
          </Card>
        </Link>
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
