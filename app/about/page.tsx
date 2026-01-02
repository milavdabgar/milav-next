import { getContentBySlug, getAvailableLocales } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { SinglePageLayout } from '@/components/layouts';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Separator } from '@/components/ui/separator';
import { Button } from '@/components/ui/button';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Mail, Github, Linkedin, Globe, GraduationCap, Briefcase, Code, Target } from 'lucide-react';
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
    <SinglePageLayout>
      <div className="space-y-8 -mt-4">
        {/* Hero Section */}
        <Card className="border-2">
          <CardHeader>
            <div className="flex items-center gap-4">
              <div className="h-16 w-16 rounded-full bg-primary/10 flex items-center justify-center">
                <span className="text-2xl font-bold text-primary">MD</span>
              </div>
              <div>
                <CardTitle className="text-3xl">{about.metadata.title}</CardTitle>
                <CardDescription className="text-base mt-2">{about.metadata.description}</CardDescription>
              </div>
            </div>
          </CardHeader>
        </Card>

        {/* Tabs Section */}
        <Tabs defaultValue="overview" className="w-full">
          <TabsList className="grid w-full grid-cols-4">
            <TabsTrigger value="overview">
              <Target className="h-4 w-4 mr-2" />
              Overview
            </TabsTrigger>
            <TabsTrigger value="content">
              <Code className="h-4 w-4 mr-2" />
              Content
            </TabsTrigger>
            <TabsTrigger value="background">
              <GraduationCap className="h-4 w-4 mr-2" />
              Background
            </TabsTrigger>
            <TabsTrigger value="connect">
              <Mail className="h-4 w-4 mr-2" />
              Connect
            </TabsTrigger>
          </TabsList>

          <TabsContent value="overview" className="space-y-4 mt-6">
            <Card>
              <CardHeader>
                <CardTitle>Purpose & Vision</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <p className="text-muted-foreground">
                  PlanetMilav is my digital garden where I share knowledge and experiences I find valuable. 
                  The site serves as both a personal reference and a resource for others interested in electronics, 
                  embedded systems, programming, and data science.
                </p>
                <div className="space-y-2">
                  <p className="font-medium">Goals:</p>
                  <ul className="list-disc list-inside space-y-1 text-muted-foreground">
                    <li>Document solutions to technical problems I&apos;ve encountered</li>
                    <li>Share educational resources with students and fellow enthusiasts</li>
                    <li>Track my learning journey across various technical domains</li>
                    <li>Connect with like-minded individuals in the tech community</li>
                  </ul>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="content" className="space-y-4 mt-6">
            <Card>
              <CardHeader>
                <CardTitle>Content Focus</CardTitle>
                <CardDescription>
                  As a Lecturer in Electronics and Communication at Government Polytechnic, Palanpur, 
                  much of the study material shared here is at the Diploma level. However, I also cover 
                  more advanced topics that reflect my personal interests and ongoing education.
                </CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid gap-4 md:grid-cols-2">
                  <Card className="border-2">
                    <CardHeader>
                      <Badge variant="outline" className="w-fit">Electronics</Badge>
                      <CardDescription className="mt-2">
                        Circuit design, PCB layout, component selection
                      </CardDescription>
                    </CardHeader>
                  </Card>
                  <Card className="border-2">
                    <CardHeader>
                      <Badge variant="outline" className="w-fit">Embedded Systems</Badge>
                      <CardDescription className="mt-2">
                        Microcontrollers, firmware, real-time systems
                      </CardDescription>
                    </CardHeader>
                  </Card>
                  <Card className="border-2">
                    <CardHeader>
                      <Badge variant="outline" className="w-fit">Programming</Badge>
                      <CardDescription className="mt-2">
                        C/C++, Python, R, and other languages
                      </CardDescription>
                    </CardHeader>
                  </Card>
                  <Card className="border-2">
                    <CardHeader>
                      <Badge variant="outline" className="w-fit">Data Science</Badge>
                      <CardDescription className="mt-2">
                        Machine learning, computer vision, data analysis
                      </CardDescription>
                    </CardHeader>
                  </Card>
                  <Card className="border-2">
                    <CardHeader>
                      <Badge variant="outline" className="w-fit">IoT</Badge>
                      <CardDescription className="mt-2">
                        Sensors, wireless protocols, cloud integration
                      </CardDescription>
                    </CardHeader>
                  </Card>
                  <Card className="border-2">
                    <CardHeader>
                      <Badge variant="outline" className="w-fit">Academic Resources</Badge>
                      <CardDescription className="mt-2">
                        Course materials, project guides, references
                      </CardDescription>
                    </CardHeader>
                  </Card>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="background" className="space-y-4 mt-6">
            <Card>
              <CardHeader>
                <CardTitle>About the Author</CardTitle>
                <CardDescription>
                  I&apos;m Milav Dabgar, an Electronics and Communication Engineering professional with 
                  experience in both academia and industry.
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-6">
                <div className="space-y-4">
                  <div className="flex gap-3">
                    <Briefcase className="h-5 w-5 mt-1 text-primary" />
                    <div>
                      <p className="font-medium">Current Role</p>
                      <p className="text-sm text-muted-foreground">
                        GES Class II Lecturer at Government Polytechnic, Palanpur
                      </p>
                    </div>
                  </div>
                  
                  <div className="flex gap-3">
                    <Briefcase className="h-5 w-5 mt-1 text-muted-foreground" />
                    <div>
                      <p className="font-medium">Previous Experience</p>
                      <p className="text-sm text-muted-foreground">
                        Electronics Engineer at TEXEG India Private Limited
                      </p>
                    </div>
                  </div>

                  <Separator />
                  
                  <div className="flex gap-3">
                    <GraduationCap className="h-5 w-5 mt-1 text-primary" />
                    <div className="space-y-2">
                      <p className="font-medium">Education</p>
                      <ul className="text-sm text-muted-foreground space-y-1">
                        <li>• M.E. in Communication Systems Engineering from L.D College of Engineering</li>
                        <li>• B.E. in Electronics and Communication Engineering</li>
                        <li>• Currently pursuing B.Sc. in Programming and Data Science from IIT Madras</li>
                      </ul>
                    </div>
                  </div>

                  <Separator />
                  
                  <p className="text-sm text-muted-foreground italic">
                    I&apos;m passionate about continuous learning and applying technology to solve real-world problems. 
                    When I&apos;m not teaching or working on technical projects, I enjoy music and practicing yoga.
                  </p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="connect" className="space-y-4 mt-6">
            <Card>
              <CardHeader>
                <CardTitle>Get in Touch</CardTitle>
                <CardDescription>
                  Feel free to reach out for technical discussions, collaborations, or student guidance.
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="grid gap-3 sm:grid-cols-2">
                  <Button asChild variant="outline" className="justify-start">
                    <Link href="mailto:milav.dabgar@gmail.com">
                      <Mail className="mr-2 h-4 w-4" />
                      milav.dabgar@gmail.com
                    </Link>
                  </Button>
                  <Button asChild variant="outline" className="justify-start">
                    <Link href="https://github.com/milavdabgar" target="_blank">
                      <Github className="mr-2 h-4 w-4" />
                      GitHub
                    </Link>
                  </Button>
                  <Button asChild variant="outline" className="justify-start">
                    <Link href="https://linkedin.com/in/milavdabgar" target="_blank">
                      <Linkedin className="mr-2 h-4 w-4" />
                      LinkedIn
                    </Link>
                  </Button>
                  <Button asChild variant="outline" className="justify-start">
                    <Link href="https://milav.in" target="_blank">
                      <Globe className="mr-2 h-4 w-4" />
                      Website
                    </Link>
                  </Button>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </SinglePageLayout>
  );
}

export const metadata = {
  title: 'About - Milav Dabgar',
  description: 'Learn more about Milav Dabgar',
};
