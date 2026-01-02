import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { getAllContent } from '@/lib/mdx';
import { CalendarIcon, ArrowRightIcon, Github, Linkedin, Mail, Twitter, Youtube, Instagram } from 'lucide-react';

export default async function Home() {
  // Fetch recent content
  const blogs = getAllContent('blog').map(item => ({ ...item, type: 'blog' }));
  const projects = getAllContent('projects').map(item => ({ ...item, type: 'projects' }));
  const resources = getAllContent('resources').map(item => ({ ...item, type: 'resources' }));

  // Combine and sort by date
  const allContent = [...blogs, ...projects, ...resources]
    .sort((a, b) => {
      const dateA = new Date(a.metadata.date || 0).getTime();
      const dateB = new Date(b.metadata.date || 0).getTime();
      return dateB - dateA;
    })
    .slice(0, 6);

  return (
    <div className="flex flex-col min-h-screen">
      {/* Hero Section */}
      {/* Hero Section */}
      {/* Hero Section */}
      <section className="relative w-full min-h-[500px] flex items-center justify-center text-center overflow-hidden bg-background">
        {/* Subtle Background Pattern */}
        <div className="absolute inset-0 z-0 bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] [background-size:16px_16px] dark:bg-[radial-gradient(#1f2937_1px,transparent_1px)] opacity-50" />

        {/* Content */}
        <div className="relative z-10 container mx-auto px-4 flex flex-col items-center animate-in fade-in zoom-in duration-700 slide-in-from-bottom-4">

          {/* Avatar */}
          <div className="mb-8 p-1 rounded-full ring-2 ring-border/50 bg-background/50 backdrop-blur-sm shadow-xl">
            <div className="relative w-32 h-32 md:w-40 md:h-40 rounded-full overflow-hidden border-2 border-background shadow-sm">
              <img
                src="/avatar.jpg"
                alt="Milav Dabgar"
                className="object-cover w-full h-full"
              />
            </div>
          </div>

          <h1 className="text-4xl md:text-6xl font-bold tracking-tight mb-4 bg-clip-text text-transparent bg-gradient-to-r from-primary to-primary/60 dark:to-primary/40 pb-1">
            Milav Dabgar
          </h1>

          <p className="text-xl md:text-2xl font-medium text-muted-foreground mb-8 max-w-2xl">
            Lecturer in Electronics and Communication Engineering
          </p>

          {/* Social Links */}
          <div className="flex gap-4 items-center">
            <SocialLink href="https://linkedin.com/in/milavdabgar" icon="linkedin" />
            <SocialLink href="https://github.com/milavdabgar" icon="github" />
            <SocialLink href="https://instagram.com/milav.dabgar" icon="instagram" />
            <SocialLink href="https://youtube.com/@milav.dabgar" icon="youtube" />
            <SocialLink href="mailto:milav.dabgar@gmail.com" icon="mail" />
          </div>

          {/* Tagline */}
          <div className="mt-12 px-6 py-2 rounded-full bg-muted/30 border border-border/40 backdrop-blur-sm">
            <p className="text-sm md:text-base font-medium text-muted-foreground tracking-wide">
              On a Continuous Journey of Digital Exploration...
            </p>
          </div>
        </div>
      </section>

      {/* Recent Content Section */}
      <section className="container mx-auto px-4 py-16">
        <h2 className="text-3xl font-bold mb-8">Recent</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {allContent.map((item) => (
            <Link key={item.slug} href={`/${item.type}/${item.slug}`}>
              <Card className="h-full hover:shadow-lg transition-shadow duration-300 flex flex-col">
                <CardHeader>
                  <CardTitle className="line-clamp-2">{item.metadata.title}</CardTitle>
                  <CardDescription className="flex items-center gap-2 mt-2">
                    <CalendarIcon className="w-4 h-4" />
                    {item.metadata.date ? new Date(item.metadata.date).toLocaleDateString('en-GB', {
                      day: 'numeric',
                      month: 'long',
                      year: 'numeric'
                    }) : 'No date'}
                  </CardDescription>
                </CardHeader>
                <CardContent className="flex-grow">
                  {/* Tags */}
                  {item.metadata.tags && (
                    <div className="flex flex-wrap gap-2 mb-4">
                      {item.metadata.tags.slice(0, 3).map(tag => (
                        <Badge key={tag} variant="secondary" className="text-xs">
                          {tag}
                        </Badge>
                      ))}
                    </div>
                  )}
                  <p className="text-muted-foreground line-clamp-3 text-sm">
                    {item.metadata.description || item.metadata.summary || "No description available."}
                  </p>
                </CardContent>
                {item.metadata.readingTime && (
                  <CardFooter className="text-xs text-muted-foreground pt-0 mt-auto">
                    {item.metadata.usedTime || item.metadata.readingTime}
                  </CardFooter>
                )}
              </Card>
            </Link>
          ))}
        </div>

        <div className="flex justify-center mt-12">
          <Button asChild variant="outline" size="lg">
            <Link href="/blog">
              View Archive <ArrowRightIcon className="ml-2 w-4 h-4" />
            </Link>
          </Button>
        </div>
      </section>
    </div>
  );
}

function SocialLink({ href, icon }: { href: string; icon: string }) {
  return (
    <a
      href={href}
      target="_blank"
      rel="noopener noreferrer"
      className="p-2 rounded-full hover:bg-muted transition-all duration-300 border border-transparent hover:border-border"
    >
      <Icon name={icon} className="w-5 h-5 text-muted-foreground hover:text-foreground" />
    </a>
  );
}

function Icon({ name, className }: { name: string; className?: string }) {
  const icons: { [key: string]: React.ComponentType<{ className?: string }> } = {
    github: Github,
    linkedin: Linkedin,
    mail: Mail,
    twitter: Twitter,
    youtube: Youtube,
    instagram: Instagram
  };

  const LucideIcon = icons[name];
  return LucideIcon ? <LucideIcon className={className} /> : null;
}
