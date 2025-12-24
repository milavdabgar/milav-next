import { ReactNode } from 'react';

interface SinglePageLayoutProps {
  children: ReactNode;
  title?: string;
  description?: string;
  actions?: ReactNode;
}

export function SinglePageLayout({
  children,
  title,
  description,
  actions,
}: SinglePageLayoutProps) {
  return (
    <div className="w-full px-4 sm:px-6 lg:px-8 py-8">
      {/* Header Section */}
      <div className="max-w-[1600px] mx-auto mb-8">
        {/* Actions Row */}
        {actions && (
          <div className="flex items-center justify-end mb-6">
            {actions}
          </div>
        )}

        {/* Title Section */}
        {title && (
          <div className="space-y-2">
            <h1 className="text-4xl font-bold tracking-tight">{title}</h1>
            {description && (
              <p className="text-lg text-muted-foreground">{description}</p>
            )}
          </div>
        )}
      </div>

      {/* Content - Full width with max-width handled by child components */}
      <div className="w-full">
        {children}
      </div>
    </div>
  );
}
