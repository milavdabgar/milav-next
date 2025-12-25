import { ReactNode } from 'react';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { Calendar, Clock } from 'lucide-react';
import { formatDate } from '@/lib/utils';
import { ResponsiveToc } from '@/components/ui/responsive-toc';
import { BlogDownload } from '@/components/ui/blog-download';
import { ArticleNavigation } from '@/components/ui/article-navigation';
import { Breadcrumbs } from '@/components/ui/breadcrumbs';

interface ContentTemplateProps {
  title: string;
  description?: string;
  date?: string;
  readingTime?: string;
  tags?: string[];
  author?: string;
  slug?: string;
  locale?: string;
  previousPost?: { slug: string; title: string };
  nextPost?: { slug: string; title: string };
  children: ReactNode;
  contentType?: 'blog' | 'resource';
}

export function ContentTemplate({
  title,
  description,
  date,
  readingTime,
  tags,
  author,
  slug,
  locale,
  previousPost,
  nextPost,
  children,
  contentType = 'blog',
}: ContentTemplateProps) {
  const breadcrumbItems = contentType === 'blog'
    ? [
      { label: 'Blog', href: '/blog' },
      { label: title, href: `/blog/${slug}` },
    ]
    : [
      { label: 'Resources', href: '/resources' },
      // We might want to improve this for deeply nested resources later
      { label: title, href: '#' },
    ];

  return (
    <div className="flex gap-6 max-w-[1600px] mx-auto">
      {/* Main Content Area - Flexible width */}
      <article className="flex-1 min-w-0 space-y-6 pb-12">
        {/* Breadcrumbs */}
        <Breadcrumbs items={breadcrumbItems} />

        {/* Article Header */}
        <header className="space-y-4">
          <div className="flex items-start justify-between gap-4 flex-wrap">
            <h1 className="text-3xl md:text-4xl lg:text-5xl font-bold tracking-tight flex-1 min-w-0">
              {title}
            </h1>
            <BlogDownload title={title} slug={slug} />
          </div>

          {description && (
            <p className="text-lg md:text-xl text-muted-foreground leading-relaxed">
              {description}
            </p>
          )}

          {/* Metadata */}
          <div className="flex flex-wrap items-center gap-4 text-sm text-muted-foreground">
            {date && (
              <div className="flex items-center gap-2">
                <Calendar className="h-4 w-4" />
                <time dateTime={date}>{formatDate(date)}</time>
              </div>
            )}

            {readingTime && (
              <div className="flex items-center gap-2">
                <Clock className="h-4 w-4" />
                <span>{readingTime}</span>
              </div>
            )}

            {author && (
              <div className="flex items-center gap-2">
                <span>By {author}</span>
              </div>
            )}
          </div>

          {/* Tags */}
          {tags && tags.length > 0 && (
            <div className="flex flex-wrap gap-2 pt-2">
              {tags.map((tag: string) => (
                <Badge key={tag} variant="secondary">
                  {tag}
                </Badge>
              ))}
            </div>
          )}
        </header>

        <Separator />

        {/* Article Content - automatically styled by globals.css */}
        <div className="prose-content">
          {children}
        </div>

        {/* Previous/Next Navigation */}
        <ArticleNavigation
          previousPost={previousPost}
          nextPost={nextPost}
          locale={locale}
        />
      </article>

      {/* Right Sidebar - TOC (Desktop only, mobile uses floating button) */}
      <ResponsiveToc className="w-64 flex-shrink-0" locale={locale} />
    </div>
  );
}
