import { getAllContent } from '@/lib/mdx';
import Link from 'next/link';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { Calendar, Clock, Tag } from 'lucide-react';
import { formatDate } from '@/lib/utils';

export default async function BlogPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const { lang } = await searchParams;
  const isGujarati = lang === 'gu';
  
  const posts = getAllContent('blog');

  return (
    <div className="container mx-auto px-4 py-8 max-w-6xl">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-4">
          <div>
            <h1 className="text-4xl font-bold tracking-tight mb-2">
              {isGujarati ? 'બ્લોગ' : 'Blog'}
            </h1>
            <p className="text-lg text-muted-foreground">
              {isGujarati 
                ? 'ટ્યુટોરિયલ, ગાઇડ્સ અને ટેકનિકલ આર્ટિકલ્સ' 
                : 'Tutorials, guides, and technical articles'}
            </p>
          </div>
          <Button asChild variant="ghost" size="sm">
            <a href={`/blog${isGujarati ? '' : '?lang=gu'}`}>
              {isGujarati ? 'English' : 'ગુજરાતી'}
            </a>
          </Button>
        </div>
      </div>

      {/* Blog Posts Grid */}
      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
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
      </div>

      {posts.length === 0 && (
        <Card className="p-12 text-center">
          <p className="text-muted-foreground">
            {isGujarati ? 'કોઈ બ્લોગ પોસ્ટ્સ મળી નથી' : 'No blog posts found'}
          </p>
        </Card>
      )}
    </div>
  );
}

export const metadata = {
  title: 'Blog - Milav Dabgar',
  description: 'Technical tutorials, guides, and articles on electronics, programming, and data science',
};
