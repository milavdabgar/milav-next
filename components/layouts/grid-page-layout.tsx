import { ReactNode } from 'react';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Separator } from '@/components/ui/separator';

interface GridPageLayoutProps {
  children: ReactNode;
  title: string;
  description?: string;
  backLink?: {
    href: string;
    label: string;
  };
  actions?: ReactNode;
  locale?: string;
  availableLocales?: string[];
  showLanguageSwitcher?: boolean;
  columns?: {
    default?: number;
    sm?: number;
    md?: number;
    lg?: number;
    xl?: number;
  };
  breadcrumbs?: ReactNode;
}

export function GridPageLayout({
  children,
  title,
  description,
  backLink,
  actions,
  breadcrumbs,
  locale = 'en',
  availableLocales = [],
  showLanguageSwitcher = false,
  columns = { default: 1, md: 2, lg: 3 },
}: GridPageLayoutProps) {
  // Build grid classes
  const gridClasses = [
    'grid',
    'gap-6',
    columns.default && `grid-cols-${columns.default}`,
    columns.sm && `sm:grid-cols-${columns.sm}`,
    columns.md && `md:grid-cols-${columns.md}`,
    columns.lg && `lg:grid-cols-${columns.lg}`,
    columns.xl && `xl:grid-cols-${columns.xl}`,
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <div className="container mx-auto px-4 py-8 max-w-7xl">
      {/* Header Section */}
      <div className="mb-8">
        {/* Breadcrumbs */}
        {breadcrumbs && (
          <div className="mb-4">
            {breadcrumbs}
          </div>
        )}

        {/* Navigation Row */}
        {(backLink || actions || (showLanguageSwitcher && availableLocales.length > 0)) && (
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
        )}

        {/* Title Section */}
        <div className="space-y-2">
          <h1 className="text-4xl font-bold tracking-tight">{title}</h1>
          {description && (
            <p className="text-lg text-muted-foreground">{description}</p>
          )}
        </div>
      </div>

      {/* Grid Content */}
      <div className={gridClasses}>{children}</div>
    </div>
  );
}
