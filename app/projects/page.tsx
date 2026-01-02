import { getContentBySlug, getAvailableLocales } from '@/lib/mdx';
import { SinglePageLayout } from '@/components/layouts';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Separator } from '@/components/ui/separator';
import { Button } from '@/components/ui/button';
import { ExternalLink, FileText, Users, Lightbulb, BookOpen } from 'lucide-react';
import Link from 'next/link';

export default async function ProjectsPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const params = await searchParams;
  const locale = params.lang || 'en';
  const content = await getContentBySlug('projects', 'index', locale);
  const availableLocales = await getAvailableLocales('projects', 'index');

  const featuredProjects = [
    {
      title: 'FPGA Implementation of Image Steganography',
      category: 'Research',
      description: 'Hardware implementation of the YASS algorithm resistant to steganalysis attacks',
      status: 'Completed & Published',
      badge: 'success',
    },
    {
      title: 'Wireless Data Acquisition System',
      category: 'Industrial',
      description: 'Multi-device monitoring system using Modbus protocol with wireless connectivity',
      status: 'Completed',
      badge: 'success',
    },
    {
      title: 'Edge ML for Embedded Devices',
      category: 'Research',
      description: 'Implementing machine learning algorithms on resource-constrained microcontrollers',
      status: 'In Progress',
      badge: 'default',
    },
    {
      title: 'Smart Agriculture Monitoring',
      category: 'IoT',
      description: 'Sensor network and monitoring system for agricultural applications',
      status: 'In Progress',
      badge: 'default',
    },
  ];

  const publications = [
    {
      title: 'FPGA Based Implementation of Image Steganography',
      venue: 'International Journal of Computer Applications',
      year: '2015',
      url: 'https://www.ijcaonline.org/archives/volume120/number9/21259-4125',
    },
    {
      title: 'Embedded Systems Approach to Industrial Automation',
      venue: 'Conference Proceedings, IEEE',
      year: '2016',
      url: null,
    },
  ];

  const studentProjects = [
    {
      title: 'Smart Traffic Management System',
      tech: 'Arduino, Sensors, ML',
      team: 'Patel K., Shah R., Joshi M.',
      year: '2023',
    },
    {
      title: 'IoT-based Health Monitoring',
      tech: 'ESP32, Web App, Cloud',
      team: 'Mehta S., Desai J.',
      year: '2022',
    },
    {
      title: 'Automated Irrigation Controller',
      tech: 'Microcontroller, Sensors',
      team: 'Prajapati A., Modi K.',
      year: '2021',
    },
    {
      title: 'Solar Power Monitoring System',
      tech: 'STM32, IoT, Data Analytics',
      team: 'Sharma P., Vyas H.',
      year: '2020',
    },
  ];

  const resources = [
    { icon: FileText, title: 'Project Templates', desc: 'Starting frameworks and code bases' },
    { icon: BookOpen, title: 'Design Documents', desc: 'Sample documentation structure' },
    { icon: Lightbulb, title: 'Development Guidelines', desc: 'Best practices for embedded and IoT projects' },
    { icon: FileText, title: 'Troubleshooting Guides', desc: 'Common issues and their solutions' },
  ];

  return (
    <SinglePageLayout>
      <div className="space-y-8 -mt-4">
        {/* Hero Section */}
        <Card className="border-2">
          <CardHeader>
            <CardTitle className="text-3xl">Projects</CardTitle>
            <CardDescription className="text-base">
              Explore technical projects spanning embedded systems, data science, IoT, and electronics engineering.
              This section showcases various research and implementation projects I&apos;ve worked on personally, 
              guided students through, or collaborated on with industry partners.
            </CardDescription>
          </CardHeader>
        </Card>

        {/* Tabs Section */}
        <Tabs defaultValue="featured" className="w-full">
          <TabsList className="grid w-full grid-cols-4">
            <TabsTrigger value="featured">
              <Lightbulb className="h-4 w-4 mr-2" />
              Featured
            </TabsTrigger>
            <TabsTrigger value="publications">
              <FileText className="h-4 w-4 mr-2" />
              Publications
            </TabsTrigger>
            <TabsTrigger value="student">
              <Users className="h-4 w-4 mr-2" />
              Student Projects
            </TabsTrigger>
            <TabsTrigger value="resources">
              <BookOpen className="h-4 w-4 mr-2" />
              Resources
            </TabsTrigger>
          </TabsList>

          <TabsContent value="featured" className="mt-6">
            <div className="grid gap-4 md:grid-cols-2">
              {featuredProjects.map((project, idx) => (
                <Card key={idx} className="border-2 hover:shadow-lg transition-shadow">
                  <CardHeader>
                    <div className="flex items-start justify-between">
                      <Badge variant="outline">{project.category}</Badge>
                      <Badge variant={project.badge === 'success' ? 'default' : 'secondary'}>
                        {project.status}
                      </Badge>
                    </div>
                    <CardTitle className="mt-4">{project.title}</CardTitle>
                    <CardDescription>{project.description}</CardDescription>
                  </CardHeader>
                </Card>
              ))}
            </div>
          </TabsContent>

          <TabsContent value="publications" className="mt-6">
            <Card>
              <CardHeader>
                <CardTitle>Research Publications</CardTitle>
                <CardDescription>
                  My academic work has been published in peer-reviewed journals and conferences
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-4">
                {publications.map((pub, idx) => (
                  <Card key={idx} className="border-2">
                    <CardHeader>
                      <div className="flex items-start justify-between">
                        <div className="space-y-2 flex-1">
                          <CardTitle className="text-lg">{pub.title}</CardTitle>
                          <CardDescription>
                            {pub.venue} ({pub.year})
                          </CardDescription>
                        </div>
                        {pub.url && (
                          <Button asChild size="sm" variant="outline">
                            <Link href={pub.url} target="_blank">
                              <ExternalLink className="h-4 w-4" />
                            </Link>
                          </Button>
                        )}
                      </div>
                    </CardHeader>
                  </Card>
                ))}
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="student" className="mt-6">
            <Card>
              <CardHeader>
                <CardTitle>Student Projects</CardTitle>
                <CardDescription>
                  I&apos;ve guided numerous student projects that demonstrate creative solutions to real-world challenges
                </CardDescription>
              </CardHeader>
              <CardContent className="space-y-3">
                {studentProjects.map((project, idx) => (
                  <Card key={idx} className="border-2">
                    <CardHeader>
                      <div className="flex items-start justify-between">
                        <div className="space-y-2 flex-1">
                          <CardTitle className="text-base">{project.title}</CardTitle>
                          <div className="flex flex-wrap gap-2">
                            <Badge variant="outline">{project.tech}</Badge>
                            <Badge variant="secondary">{project.year}</Badge>
                          </div>
                          <CardDescription className="text-sm">
                            Team: {project.team}
                          </CardDescription>
                        </div>
                      </div>
                    </CardHeader>
                  </Card>
                ))}
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="resources" className="mt-6">
            <div className="grid gap-4 md:grid-cols-2">
              {resources.map((resource, idx) => (
                <Card key={idx} className="border-2 hover:shadow-lg transition-shadow">
                  <CardHeader>
                    <resource.icon className="h-8 w-8 mb-2 text-primary" />
                    <CardTitle className="text-lg">{resource.title}</CardTitle>
                    <CardDescription>{resource.desc}</CardDescription>
                  </CardHeader>
                </Card>
              ))}
            </div>
            <Separator className="my-6" />
            <Card>
              <CardContent className="pt-6 text-center">
                <p className="text-sm text-muted-foreground italic">
                  Looking to collaborate on a project or need guidance for implementation?{' '}
                  <Link href="mailto:milav.dabgar@gmail.com" className="text-primary hover:underline">
                    Contact me
                  </Link>{' '}
                  to discuss possibilities.
                </p>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </SinglePageLayout>
  );
}

export const metadata = {
  title: 'Projects - Milav Dabgar',
  description: 'Research work, technical implementations, and student-led innovations',
};
