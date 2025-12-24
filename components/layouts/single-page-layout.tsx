import { ReactNode } from 'react';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Separator } from '@/components/ui/separator';

interface SinglePageLayoutProps {
  children: ReactNode;
  title?: string;
  description?: string;
  backLink?: {
    href: string;
    label: string;
  };
  actions?: ReactNode;
  locale?: string;
  availableLocales?: string[];
  showLanguageSwitcher?: boolean;
}

export function SinglePageLayout({
  children,
  title,
  description,
  backLink,
  actions,
  locale = 'en',
  availableLocales = [],
  showLanguageSwitcher = true,
}: SinglePageLayoutProps) {
  return (
    <div className="container mx-auto px-4 py-8 max-w-4xl">
      {/* Header Section */}
      <div className="mb-8">
        {/* Navigation Row */}
        <div className="flex items-center justify-between mb-6">
          {backLink ? (
            <Link href={backLink.href}>
              <Button variant="ghost" size="sm">
                ← {backLink.label}
              </Button>
            </Link>
          ) : (
            <div />
          )}
          
          <div className="flex items-center gap-2">
            {actions}
            {showLanguageSwitcher && availableLocales.length > 0 && (
              <>
                <Separator orientation="vertical" className="h-6" />
                <div className="flex gap-2">
                  {availableLocales.map((loc) => (
                    <Link key={loc} href={`?lang=${loc}`}>
                      <Button 
                        variant={locale === loc ? 'default' : 'outline'} 
                        size="sm"
                      >
                        {loc.toUpperCase()}
                      </Button>
                    </Link>
                  ))}
                </div>
              </>
            )}
          </div>
        </div>

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

      {/* Content */}
      {children}
    </div>
  );
}
