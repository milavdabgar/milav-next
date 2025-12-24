import { getContentBySlug, getAvailableLocales } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { MDXRemote } from 'next-mdx-remote/rsc';
import { SinglePageLayout } from '@/components/layouts';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { Button } from '@/components/ui/button';
import { Mail, Github, Linkedin, Globe } from 'lucide-react';
import Link from 'next/link';

export default async function AboutPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const params = await searchParams;
  const locale = params.lang || 'en';
  
  const about = getContentBySlug('about', 'index', locale === 'gu' ? 'gu' : undefined);

  if (!about) {
    notFound();
  }

  const availableLocales = await getAvailableLocales('about', 'index');

  return (
    <SinglePageLayout
      title={about.metadata.title}
      description={about.metadata.description}
      locale={locale}
      availableLocales={availableLocales}
    >
      <MDXRemote source={about.content} />

      <Separator className="my-8" />

      {/* Contact Section */}
      <Card>
        <CardHeader>
          <CardTitle>{locale === 'gu' ? 'સંપર્ક કરો' : 'Get in Touch'}</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex flex-wrap gap-2">
            <Button asChild size="sm" variant="outline">
              <Link href="mailto:milav.dabgar@gmail.com">
                <Mail className="mr-2 h-4 w-4" />
                Email
              </Link>
            </Button>
            <Button asChild size="sm" variant="outline">
              <Link href="https://github.com/milavdabgar" target="_blank">
                <Github className="mr-2 h-4 w-4" />
                GitHub
              </Link>
            </Button>
            <Button asChild size="sm" variant="outline">
              <Link href="https://linkedin.com/in/milavdabgar" target="_blank">
                <Linkedin className="mr-2 h-4 w-4" />
                LinkedIn
              </Link>
            </Button>
            <Button asChild size="sm" variant="outline">
              <Link href="https://milav.in" target="_blank">
                <Globe className="mr-2 h-4 w-4" />
                Website
              </Link>
            </Button>
          </div>
        </CardContent>
      </Card>
    </SinglePageLayout>
  );
}

export const metadata = {
  title: 'About - Milav Dabgar',
  description: 'Learn more about Milav Dabgar',
};
