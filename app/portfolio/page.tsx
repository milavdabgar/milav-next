import { getContentBySlug } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { Avatar, AvatarFallback } from '@/components/ui/avatar';
import { Button } from '@/components/ui/button';
import { Mail, Github, Linkedin } from 'lucide-react';
import { MDXRemote } from 'next-mdx-remote/rsc';
import remarkMath from 'remark-math';
import remarkGfm from 'remark-gfm';
import rehypeKatex from 'rehype-katex';
import { mdxComponents } from '@/components/mdx-components';

export default async function PortfolioPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const { lang } = await searchParams;
  const locale = lang === 'gu' ? 'gu' : undefined;

  const portfolio = getContentBySlug('portfolio', 'index', locale);

  if (!portfolio) {
    notFound();
  }

  const isGujarati = locale === 'gu';

  return (
    <div className="container mx-auto px-4 py-8 max-w-4xl">
      {/* Header Section */}
      <div className="mb-12 text-center md:text-left">
        <div className="flex flex-col md:flex-row items-center justify-between mb-6 gap-6">
          <div className="flex flex-col md:flex-row items-center gap-6">
            <Avatar className="h-24 w-24 md:h-32 md:w-32 border-4 border-background shadow-xl">
              <AvatarFallback className="text-4xl">MD</AvatarFallback>
            </Avatar>
            <div className="text-center md:text-left">
              <h1 className="text-4xl md:text-5xl font-bold tracking-tight mb-3">
                {isGujarati ? 'મિલવ ડાબગર' : 'Milav Dabgar'}
              </h1>
              <p className="text-xl text-muted-foreground">
                {portfolio.metadata.description}
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <Badge variant="outline" className="text-base px-3 py-1">{isGujarati ? 'ગુજરાતી' : 'English'}</Badge>
            <Button asChild variant="ghost" size="sm">
              <a href={`/portfolio${isGujarati ? '' : '?lang=gu'}`}>
                {isGujarati ? 'English' : 'ગુજરાતી'}
              </a>
            </Button>
          </div>
        </div>

        {/* Contact Buttons */}
        <div className="flex flex-wrap justify-center md:justify-start gap-3">
          <Button asChild variant="outline">
            <a href="mailto:milav.dabgar@gmail.com">
              <Mail className="mr-2 h-4 w-4" />
              Email
            </a>
          </Button>
          <Button asChild variant="outline">
            <a href="https://github.com/milavdabgar" target="_blank" rel="noopener noreferrer">
              <Github className="mr-2 h-4 w-4" />
              GitHub
            </a>
          </Button>
          <Button asChild variant="outline">
            <a href="https://linkedin.com/in/milavdabgar" target="_blank" rel="noopener noreferrer">
              <Linkedin className="mr-2 h-4 w-4" />
              LinkedIn
            </a>
          </Button>
        </div>
      </div>

      <Separator className="my-8" />

      {/* Main Content Rendered from MDX */}
      <div className="prose prose-zinc dark:prose-invert max-w-none prose-headings:scroll-m-20 prose-headings:font-semibold prose-a:text-primary prose-img:rounded-lg">
        <MDXRemote
          source={portfolio.content}
          options={{
            mdxOptions: {
              remarkPlugins: [remarkMath, remarkGfm],
              rehypePlugins: [rehypeKatex],
            }
          }}
          components={mdxComponents}
        />
      </div>
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
  const portfolio = getContentBySlug('portfolio', 'index', locale);

  if (!portfolio) {
    return {
      title: 'Portfolio Not Found',
    };
  }

  return {
    title: portfolio.metadata.title,
    description: portfolio.metadata.description || portfolio.metadata.summary,
  };
}
