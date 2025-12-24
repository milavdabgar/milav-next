import { getContentBySlug } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { Badge } from '@/components/ui/badge';
import { Card } from '@/components/ui/card';
import { Separator } from '@/components/ui/separator';
import { MDXRemote } from 'next-mdx-remote/rsc';

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

  return (
    <div className="container mx-auto px-4 py-8 max-w-5xl">
      <div className="mb-8">
        <div className="flex items-center gap-2 mb-4">
          <Badge variant="outline">{locale === 'gu' ? 'ગુજરાતી' : 'English'}</Badge>
          <a 
            href={`/portfolio${locale === 'gu' ? '' : '?lang=gu'}`}
            className="text-sm text-muted-foreground hover:text-foreground"
          >
            {locale === 'gu' ? 'Switch to English' : 'ગુજરાતીમાં વાંચો'}
          </a>
        </div>
        
        <h1 className="text-4xl font-bold tracking-tight mb-2">
          {portfolio.metadata.title}
        </h1>
        
        {portfolio.metadata.description && (
          <p className="text-xl text-muted-foreground">
            {portfolio.metadata.description}
          </p>
        )}
      </div>

      <Separator className="my-8" />

      <article className="prose prose-neutral dark:prose-invert max-w-none">
        <MDXRemote source={portfolio.content} />
      </article>
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
