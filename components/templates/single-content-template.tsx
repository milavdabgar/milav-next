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
      
      {/* Content - automatically styled by globals.css */}
      <div>
        {children}
      </div>
    </article>
  );
}
