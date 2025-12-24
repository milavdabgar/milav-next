import { MDXRemote } from 'next-mdx-remote/rsc';
import { getContentBySlug, getAvailableLocales } from '@/lib/mdx';
import { Button } from '@/components/ui/button';
import Link from 'next/link';

export default async function VideosPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const params = await searchParams;
  const locale = params.lang || 'en';
  const content = await getContentBySlug('media', 'videos', locale);
  const availableLocales = await getAvailableLocales('media', 'videos');

  return (
    <div className="container mx-auto px-4 py-8 max-w-4xl">
      <div className="mb-6 flex items-center justify-between">
        <Link href="/media">
          <Button variant="ghost" size="sm">
            ← Back to Media
          </Button>
        </Link>
        <div className="flex gap-2">
          {availableLocales.map((loc) => (
            <Link key={loc} href={`?lang=${loc}`}>
              <Button variant={locale === loc ? 'default' : 'outline'} size="sm">
                {loc.toUpperCase()}
              </Button>
            </Link>
          ))}
        </div>
      </div>
      <article className="prose prose-neutral dark:prose-invert max-w-none">
        <MDXRemote source={content.content} />
      </article>
    </div>
  );
}

export const metadata = {
  title: 'Videos - Milav Dabgar',
  description: 'Curated video content',
};
