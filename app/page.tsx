import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';

export default function Home() {
  return (
    <div className="container mx-auto px-4 py-16">
      {/* Hero Section */}
      <section className="text-center py-20">
        <h1 className="text-5xl font-bold tracking-tight mb-6">
          Hi, I'm <span className="text-primary">Milav Dabgar</span>
        </h1>
        <p className="text-xl text-muted-foreground max-w-2xl mx-auto mb-8">
          Educator, Engineer, and Tech Enthusiast. I teach, learn, and build innovative
          solutions in electronics, embedded systems, and software development.
        </p>
        <div className="flex gap-4 justify-center">
          <Button asChild size="lg">
            <Link href="/portfolio">View Portfolio</Link>
          </Button>
          <Button asChild variant="outline" size="lg">
            <Link href="/blog">Read Blog</Link>
          </Button>
        </div>
      </section>

      {/* Quick Links */}
      <section className="py-16">
        <h2 className="text-3xl font-bold mb-8 text-center">What I Do</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <Card>
            <CardHeader>
              <CardTitle>Teaching</CardTitle>
              <CardDescription>
                Government Polytechnic, Palanpur
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground">
                Lecturer in Electronics & Communication, specializing in Programming,
                Microcontrollers, and Embedded Systems.
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Learning</CardTitle>
              <CardDescription>
                Continuous Professional Development
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground">
                Pursuing B.Sc. in Programming and Data Science from IIT Madras.
                Multiple certifications from Coursera, NPTEL, and Udemy.
              </p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Building</CardTitle>
              <CardDescription>
                Innovation & Development
              </CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-sm text-muted-foreground">
                Creating solutions with Next.js, React, Python, and embedded systems.
                Focus on education technology and IoT projects.
              </p>
            </CardContent>
          </Card>
        </div>
      </section>

      {/* Skills Section */}
      <section className="py-16">
        <h2 className="text-3xl font-bold mb-8 text-center">Tech Stack</h2>
        <div className="flex flex-wrap gap-2 justify-center max-w-3xl mx-auto">
          {[
            'Next.js', 'React', 'TypeScript', 'Python', 'C/C++',
            'Embedded Systems', 'IoT', 'Machine Learning', 'Data Science',
            'Arduino', 'Raspberry Pi', 'STM32', 'Tailwind CSS', 'Node.js'
          ].map((skill) => (
            <Badge key={skill} variant="secondary">
              {skill}
            </Badge>
          ))}
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-16 text-center">
        <Card className="max-w-2xl mx-auto">
          <CardHeader>
            <CardTitle className="text-2xl">Let's Connect</CardTitle>
            <CardDescription>
              Interested in collaboration or have questions?
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex gap-4 justify-center">
              <Button asChild>
                <a href="mailto:milav@example.com">Get in Touch</a>
              </Button>
              <Button asChild variant="outline">
                <a href="https://github.com/milavdabgar" target="_blank" rel="noopener noreferrer">
                  GitHub
                </a>
              </Button>
              <Button asChild variant="outline">
                <a href="https://linkedin.com/in/milavdabgar" target="_blank" rel="noopener noreferrer">
                  LinkedIn
                </a>
              </Button>
            </div>
          </CardContent>
        </Card>
      </section>
    </div>
  );
}

