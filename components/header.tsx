'use client';

import { Suspense } from 'react';
import Link from 'next/link';
import { usePathname, useSearchParams } from 'next/navigation';
import { Button } from '@/components/ui/button';
import { ThemeToggle } from '@/components/theme-toggle';
import { Search } from 'lucide-react';
import { cn } from '@/lib/utils';

const navigation = [
  { name: 'Home', href: '/' },
  { name: 'About', href: '/about' },
  { name: 'Portfolio', href: '/portfolio' },
  { name: 'Blog', href: '/blog' },
  { name: 'Projects', href: '/projects' },
  { name: 'Resources', href: '/resources' },
  { name: 'Media', href: '/media' },
];

function LanguageSwitcher() {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const currentLang = searchParams.get('lang') || 'en';

  return (
    <div className="flex gap-1">
      <Link href={`${pathname}?lang=en`}>
        <Button
          variant={currentLang === 'en' ? 'default' : 'ghost'}
          size="sm"
          className="h-9 px-3"
        >
          EN
        </Button>
      </Link>
      <Link href={`${pathname}?lang=gu`}>
        <Button
          variant={currentLang === 'gu' ? 'default' : 'ghost'}
          size="sm"
          className="h-9 px-3"
        >
          ગુ
        </Button>
      </Link>
    </div>
  );
}

export function Header() {
  const pathname = usePathname();

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <nav className="container mx-auto flex h-16 items-center px-4">
        <div className="mr-8">
          <Link href="/" className="flex items-center space-x-2">
            <span className="font-bold text-xl">Milav.in</span>
          </Link>
        </div>

        <div className="flex flex-1 items-center justify-between space-x-2 md:justify-end">
          <nav className="flex items-center space-x-6">
            {navigation.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className={cn(
                  'text-sm font-medium transition-colors hover:text-primary',
                  pathname === item.href
                    ? 'text-foreground'
                    : 'text-muted-foreground'
                )}
              >
                {item.name}
              </Link>
            ))}
          </nav>

          <div className="flex items-center gap-2 ml-4">
            <Button
              variant="ghost"
              size="icon"
              aria-label="Search"
            >
              <Search className="h-5 w-5" />
            </Button>

            <Suspense fallback={<div className="w-[88px] h-9" />}>
              <LanguageSwitcher />
            </Suspense>

            <ThemeToggle />
          </div>
        </div>
      </nav>
    </header>
  );
}
