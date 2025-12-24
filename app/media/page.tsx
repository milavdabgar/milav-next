import Link from 'next/link';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Music, Quote, Video } from 'lucide-react';

export default function MediaPage() {
  const mediaPages = [
    {
      title: 'Music Collection',
      titleGu: 'સંગીત સંગ્રહ',
      description: 'Curated playlists of Hindi and English music',
      descriptionGu: 'હિન્દી અને અંગ્રેજી સંગીતની પસંદ કરેલી પ્લેલિસ્ટ્સ',
      href: '/media/music',
      icon: Music,
    },
    {
      title: 'Quotes',
      titleGu: 'પ્રેરક વિચારો',
      description: 'Inspirational quotes and wisdom',
      descriptionGu: 'પ્રેરણાદાયક વિચારો અને જ્ઞાન',
      href: '/media/quotes',
      icon: Quote,
    },
    {
      title: 'Videos',
      titleGu: 'વિડિઓઝ',
      description: 'Curated video content',
      descriptionGu: 'પસંદ કરેલ વિડિયો સામગ્રી',
      href: '/media/videos',
      icon: Video,
    },
  ];

  return (
    <div className="container mx-auto px-4 py-8 max-w-6xl">
      <div className="mb-8">
        <h1 className="text-4xl font-bold tracking-tight mb-2">Media</h1>
        <p className="text-lg text-muted-foreground">
          Music, quotes, and videos collection
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        {mediaPages.map((page) => (
          <Link key={page.href} href={page.href}>
            <Card className="h-full hover:shadow-lg transition-shadow">
              <CardHeader>
                <page.icon className="h-12 w-12 mb-4 text-primary" />
                <CardTitle>{page.title}</CardTitle>
                <CardDescription>{page.description}</CardDescription>
              </CardHeader>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}

export const metadata = {
  title: 'Media - Milav Dabgar',
  description: 'Music, quotes, and videos collection',
};
