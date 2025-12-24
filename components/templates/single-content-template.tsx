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
      <div className="prose prose-neutral dark:prose-invert max-w-none
        prose-headings:scroll-m-20 prose-headings:font-semibold prose-headings:tracking-tight
        prose-h2:text-3xl prose-h2:border-b prose-h2:pb-3 prose-h2:mt-12 prose-h2:mb-6
        prose-h3:text-2xl prose-h3:mt-10 prose-h3:mb-4
        prose-h4:text-xl prose-h4:mt-8 prose-h4:mb-3
        prose-p:leading-7 prose-p:text-base prose-p:mb-6
        prose-a:text-primary prose-a:font-medium prose-a:underline prose-a:underline-offset-4 hover:prose-a:text-primary/80 prose-a:decoration-primary/30 hover:prose-a:decoration-primary
        prose-blockquote:border-l-4 prose-blockquote:border-primary prose-blockquote:bg-muted/50 prose-blockquote:py-4 prose-blockquote:px-6 prose-blockquote:rounded-r-lg prose-blockquote:not-italic prose-blockquote:my-6
        prose-code:bg-muted prose-code:px-1.5 prose-code:py-0.5 prose-code:rounded prose-code:font-mono prose-code:text-sm prose-code:font-semibold prose-code:before:content-none prose-code:after:content-none
        prose-pre:bg-zinc-950 dark:prose-pre:bg-zinc-900 prose-pre:border prose-pre:border-zinc-800 prose-pre:rounded-lg prose-pre:p-4 prose-pre:overflow-x-auto prose-pre:my-6
        prose-img:rounded-xl prose-img:border prose-img:shadow-md prose-img:my-8
        prose-strong:font-bold prose-strong:text-foreground
        prose-em:italic
        prose-ul:my-6 prose-ul:list-disc prose-ul:pl-6 prose-ul:space-y-2 prose-ul:marker:text-primary
        prose-ol:my-6 prose-ol:list-decimal prose-ol:pl-6 prose-ol:space-y-2 prose-ol:marker:text-primary prose-ol:marker:font-semibold
        prose-li:leading-7
        prose-table:w-full prose-table:border-collapse prose-table:my-8 prose-table:overflow-hidden prose-table:rounded-lg prose-table:border prose-table:border-border
        prose-thead:bg-muted
        prose-th:border prose-th:border-border prose-th:bg-muted/80 prose-th:px-4 prose-th:py-3 prose-th:text-left prose-th:font-bold prose-th:text-sm
        prose-td:border prose-td:border-border prose-td:px-4 prose-td:py-3 prose-td:text-sm
        prose-tr:border-b prose-tr:border-border last:prose-tr:border-b-0 prose-tr:hover:bg-muted/50 prose-tr:transition-colors
        prose-hr:my-12 prose-hr:border-border
      ">
        {children}
      </div>
    </article>
  );
}
