import { ReactNode } from 'react';
import { Separator } from '@/components/ui/separator';

interface SingleContentTemplateProps {
  title: string;
  description?: string;
  children: ReactNode;
  showSeparator?: boolean;
}

export function SingleContentTemplate({
  title,
  description,
  children,
  showSeparator = true,
}: SingleContentTemplateProps) {
  return (
    <article className="space-y-8">
      {/* Header */}
      <header className="space-y-3">
        <h1 className="text-4xl font-bold tracking-tight lg:text-5xl">
          {title}
        </h1>
        
        {description && (
          <p className="text-xl text-muted-foreground">
            {description}
          </p>
        )}
      </header>
      
      {showSeparator && <Separator />}
      
      {/* Content with enhanced prose styling */}
      <div className="prose prose-neutral dark:prose-invert prose-lg max-w-none
        prose-headings:scroll-m-20 prose-headings:font-semibold
        prose-h1:text-4xl prose-h1:font-extrabold prose-h1:tracking-tight
        prose-h2:text-3xl prose-h2:border-b prose-h2:pb-2
        prose-h3:text-2xl
        prose-p:leading-7
        prose-a:text-primary prose-a:font-medium prose-a:no-underline hover:prose-a:underline
        prose-blockquote:border-l-4 prose-blockquote:border-primary prose-blockquote:bg-muted/50 prose-blockquote:py-2 prose-blockquote:not-italic
        prose-code:bg-muted prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded prose-code:font-mono prose-code:text-sm prose-code:before:content-none prose-code:after:content-none
        prose-pre:bg-black prose-pre:border
        prose-img:rounded-lg prose-img:border
        prose-strong:font-bold prose-strong:text-foreground
        prose-table:border-collapse
        prose-th:border prose-th:border-border prose-th:bg-muted prose-th:px-4 prose-th:py-3 prose-th:text-left prose-th:font-bold
        prose-td:border prose-td:border-border prose-td:px-4 prose-td:py-3
        prose-ul:list-disc prose-ul:marker:text-primary
        prose-ol:list-decimal prose-ol:marker:text-primary prose-ol:marker:font-semibold
        prose-li:my-2
      ">
        {children}
      </div>
    </article>
  );
}
