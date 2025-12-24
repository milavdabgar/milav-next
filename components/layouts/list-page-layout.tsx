import { ReactNode } from 'react';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Separator } from '@/components/ui/separator';

interface ListPageLayoutProps {
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
  maxWidth?: 'sm' | 'md' | 'lg' | 'xl' | '2xl' | '4xl' | '6xl' | '7xl' | 'full';
}

const maxWidthClasses = {
  sm: 'max-w-screen-sm',
  md: 'max-w-screen-md',
  lg: 'max-w-screen-lg',
  xl: 'max-w-screen-xl',
  '2xl': 'max-w-screen-2xl',
  '4xl': 'max-w-4xl',
  '6xl': 'max-w-6xl',
  '7xl': 'max-w-7xl',
  full: 'max-w-full',
};

export function ListPageLayout({
  children,
  title,
  description,
  backLink,
  actions,
  locale = 'en',
  availableLocales = [],
  showLanguageSwitcher = false,
  maxWidth = '6xl',
}: ListPageLayoutProps) {
  return (
    <div className={`container mx-auto px-4 py-8 ${maxWidthClasses[maxWidth]}`}>
      {/* Header Section */}
      <div className="mb-8">
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

      {/* Content */}
      {children}
    </div>
  );
}
