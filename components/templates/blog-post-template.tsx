import { ReactNode } from 'react';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { Calendar, Clock } from 'lucide-react';
import { formatDate } from '@/lib/utils';
import { TableOfContents } from '@/components/ui/table-of-contents';
import { BlogDownload } from '@/components/ui/blog-download';

interface BlogPostTemplateProps {
  title: string;
  description?: string;
  date?: string;
  readingTime?: string;
  tags?: string[];
  author?: string;
  children: ReactNode;
}

export function BlogPostTemplate({
  title,
  description,
  date,
  readingTime,
  tags,
  author,
  children,
}: BlogPostTemplateProps) {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-[1fr_250px] gap-8">
      <article className="space-y-8 min-w-0">
        {/* Article Header */}
        <header className="space-y-4">
          <div className="flex items-start justify-between gap-4">
            <h1 className="text-4xl font-bold tracking-tight lg:text-5xl flex-1">
              {title}
            </h1>
            <BlogDownload title={title} />
          </div>
          
          {description && (
            <p className="text-xl text-muted-foreground leading-relaxed">
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
        <div>
          {children}
        </div>
      </article>
      
      {/* Sidebar with TOC */}
      <aside className="hidden lg:block">
        <div className="sticky top-24 space-y-4">
          <TableOfContents />
        </div>
      </aside>
    </div>
  );
}
