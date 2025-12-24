import { getContentBySlug } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { Button } from '@/components/ui/button';
import { Mail, Github, Linkedin, Globe } from 'lucide-react';

export default async function AboutPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const { lang } = await searchParams;
  const locale = lang === 'gu' ? 'gu' : undefined;
  
  const about = getContentBySlug('about', 'index', locale);

  if (!about) {
    notFound();
  }

  const isGujarati = locale === 'gu';

  return (
    <div className="container mx-auto px-4 py-8 max-w-4xl">
      {/* Header */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-4">
          <h1 className="text-4xl font-bold tracking-tight">
            {about.metadata.title}
          </h1>
          <Button asChild variant="ghost" size="sm">
            <a href={`/about${isGujarati ? '' : '?lang=gu'}`}>
              {isGujarati ? 'English' : 'ગુજરાતી'}
            </a>
          </Button>
        </div>
        {about.metadata.description && (
          <p className="text-xl text-muted-foreground">
            {about.metadata.description}
          </p>
        )}
      </div>

      <Separator className="my-8" />

      {/* Main Content */}
      <article className="prose prose-neutral dark:prose-invert max-w-none mb-12">
        <MDXRemote source={about.content} />
      </article>

      {/* Connect Section */}
      <Card className="mt-8">
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Globe className="h-5 w-5" />
            {isGujarati ? 'જોડાઓ' : 'Connect'}
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex flex-wrap gap-3">
            <Button asChild variant="outline" size="sm">
              <a href="mailto:milav@example.com">
                <Mail className="mr-2 h-4 w-4" />
                Email
              </a>
            </Button>
            <Button asChild variant="outline" size="sm">
              <a href="https://github.com/milavdabgar" target="_blank" rel="noopener noreferrer">
                <Github className="mr-2 h-4 w-4" />
                GitHub
              </a>
            </Button>
            <Button asChild variant="outline" size="sm">
              <a href="https://linkedin.com/in/milavdabgar" target="_blank" rel="noopener noreferrer">
                <Linkedin className="mr-2 h-4 w-4" />
                LinkedIn
              </a>
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}

export async function generateMetadata({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const { lang } = await searchParams;
  const locale = lang === 'gu' ? 'gu' : undefined;
  const about = getContentBySlug('about', 'index', locale);

  if (!about) {
    return {
      title: 'About Not Found',
    };
  }

  return {
    title: about.metadata.title,
    description: about.metadata.description || about.metadata.summary,
  };
}
