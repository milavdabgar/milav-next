import { getContentBySlug } from '@/lib/mdx';
import { notFound } from 'next/navigation';
import { Badge } from '@/components/ui/badge';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Separator } from '@/components/ui/separator';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';
import { ScrollArea } from '@/components/ui/scroll-area';
import { Avatar, AvatarFallback } from '@/components/ui/avatar';
import { Button } from '@/components/ui/button';
import { GraduationCap, Briefcase, Award, Code, Mail, Github, Linkedin } from 'lucide-react';

export default async function PortfolioPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const { lang } = await searchParams;
  const locale = lang === 'gu' ? 'gu' : undefined;
  
  const portfolio = getContentBySlug('portfolio', 'index', locale);

  if (!portfolio) {
    notFound();
  }

  const isGujarati = locale === 'gu';

  return (
    <div className="container mx-auto px-4 py-8 max-w-7xl">
      {/* Header Section */}
      <div className="mb-8">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-4">
            <Avatar className="h-20 w-20">
              <AvatarFallback className="text-2xl">MD</AvatarFallback>
            </Avatar>
            <div>
              <h1 className="text-4xl font-bold tracking-tight mb-2">
                {isGujarati ? 'મિલવ ડાબગર' : 'Milav Dabgar'}
              </h1>
              <p className="text-lg text-muted-foreground">
                {portfolio.metadata.description}
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <Badge variant="outline">{isGujarati ? 'ગુજરાતી' : 'English'}</Badge>
            <Button asChild variant="ghost" size="sm">
              <a href={`/portfolio${isGujarati ? '' : '?lang=gu'}`}>
                {isGujarati ? 'English' : 'ગુજરાતી'}
              </a>
            </Button>
          </div>
        </div>

        {/* Contact Buttons */}
        <div className="flex gap-2">
          <Button asChild size="sm" variant="outline">
            <a href="mailto:milav@example.com">
              <Mail className="mr-2 h-4 w-4" />
              Email
            </a>
          </Button>
          <Button asChild size="sm" variant="outline">
            <a href="https://github.com/milavdabgar" target="_blank" rel="noopener noreferrer">
              <Github className="mr-2 h-4 w-4" />
              GitHub
            </a>
          </Button>
          <Button asChild size="sm" variant="outline">
            <a href="https://linkedin.com/in/milavdabgar" target="_blank" rel="noopener noreferrer">
              <Linkedin className="mr-2 h-4 w-4" />
              LinkedIn
            </a>
          </Button>
        </div>
      </div>

      <Separator className="my-8" />

      {/* Main Content Tabs */}
      <Tabs defaultValue="overview" className="w-full">
        <TabsList className="grid w-full grid-cols-4 mb-8">
          <TabsTrigger value="overview">
            <GraduationCap className="mr-2 h-4 w-4" />
            {isGujarati ? 'ઝાંખી' : 'Overview'}
          </TabsTrigger>
          <TabsTrigger value="experience">
            <Briefcase className="mr-2 h-4 w-4" />
            {isGujarati ? 'અનુભવ' : 'Experience'}
          </TabsTrigger>
          <TabsTrigger value="certifications">
            <Award className="mr-2 h-4 w-4" />
            {isGujarati ? 'સર્ટિફિકેશન્સ' : 'Certifications'}
          </TabsTrigger>
          <TabsTrigger value="skills">
            <Code className="mr-2 h-4 w-4" />
            {isGujarati ? 'કૌશલ્યો' : 'Skills'}
          </TabsTrigger>
        </TabsList>

        {/* Overview Tab */}
        <TabsContent value="overview" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>{isGujarati ? 'શૈક્ષણિક લાયકાતો' : 'Academic Qualifications'}</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div className="border-l-4 border-primary pl-4">
                  <h3 className="font-semibold text-lg">
                    {isGujarati ? 'B.Sc. પ્રોગ્રામિંગ અને ડેટા સાયન્સ' : 'B.Sc. in Programming and Data Science'}
                  </h3>
                  <p className="text-muted-foreground">
                    {isGujarati ? 'IIT મદ્રાસ' : 'Indian Institute of Technology, Madras'} • {isGujarati ? 'પ્રગતિમાં' : 'In Progress'}
                  </p>
                  <p className="text-sm mt-2">
                    {isGujarati ? 'કમ્પ્યુટર સાયન્સ, ડેટા એનાલિસિસ, મશીન લર્નિંગ' : 'Computer Science, Data Analysis, Machine Learning'}
                  </p>
                </div>

                <div className="border-l-4 border-primary pl-4">
                  <h3 className="font-semibold text-lg">
                    {isGujarati ? 'M.E. કોમ્યુનિકેશન સિસ્ટમ્સ એન્જિનિયરિંગ' : 'M.E. in Communication Systems Engineering'}
                  </h3>
                  <p className="text-muted-foreground">
                    {isGujarati ? 'GTU' : 'Gujarat Technological University'} • 2013-2015
                  </p>
                  <p className="text-sm mt-2">
                    {isGujarati ? 'સિગ્નલ પ્રોસેસિંગ, એમ્બેડેડ સિસ્ટમ્સ, નેટવર્કિંગ' : 'Signal Processing, Embedded Systems, Networking'}
                  </p>
                </div>

                <div className="border-l-4 border-primary pl-4">
                  <h3 className="font-semibold text-lg">
                    {isGujarati ? 'B.E. ઇલેક્ટ્રોનિક્સ અને કોમ્યુનિકેશન' : 'B.E. in Electronics and Communication'}
                  </h3>
                  <p className="text-muted-foreground">
                    {isGujarati ? 'GTU' : 'Gujarat Technological University'} • 2009-2013
                  </p>
                  <p className="text-sm mt-2">
                    {isGujarati ? 'ઇલેક્ટ્રોનિક્સ, ડિજિટલ સિસ્ટમ્સ, કોમ્યુનિકેશન' : 'Electronics, Digital Systems, Communication'}
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>{isGujarati ? 'પ્રોજેક્ટ્સ અને રિસર્ચ' : 'Projects & Research'}</CardTitle>
            </CardHeader>
            <CardContent>
              <Accordion type="single" collapsible className="w-full">
                <AccordionItem value="fpga">
                  <AccordionTrigger>
                    {isGujarati ? 'FPGA ઇમેજ સ્ટેગેનોગ્રાફી' : 'FPGA Implementation of Image Steganography'}
                  </AccordionTrigger>
                  <AccordionContent>
                    <div className="space-y-2">
                      <Badge>M.E. Thesis</Badge>
                      <Badge variant="outline">2014-2015</Badge>
                      <p className="text-sm text-muted-foreground mt-2">
                        {isGujarati 
                          ? 'FPGA નો ઉપયોગ કરીને હાર્ડવેર-આધારિત સ્ટેગેનોગ્રાફી સિસ્ટમ વિકસાવી' 
                          : 'Developed hardware-based steganography system using FPGA with LSB technique for hiding data in digital images.'}
                      </p>
                    </div>
                  </AccordionContent>
                </AccordionItem>

                <AccordionItem value="iot">
                  <AccordionTrigger>
                    {isGujarati ? 'સ્માર્ટ હોમ ઓટોમેશન સિસ્ટમ' : 'Smart Home Automation System'}
                  </AccordionTrigger>
                  <AccordionContent>
                    <div className="space-y-2">
                      <Badge>IoT Project</Badge>
                      <Badge variant="outline">2020</Badge>
                      <p className="text-sm text-muted-foreground mt-2">
                        {isGujarati
                          ? 'ESP32 નો ઉપયોગ કરીને IoT-આધારિત હોમ ઓટોમેશન ડિઝાઇન અને અમલીકરણ'
                          : 'Designed and implemented IoT-based home automation using ESP32 with mobile app and voice control integration.'}
                      </p>
                    </div>
                  </AccordionContent>
                </AccordionItem>
              </Accordion>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Experience Tab */}
        <TabsContent value="experience" className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>{isGujarati ? 'ગવર્નમેન્ટ પોલિટેકનિક, પાલનપુર' : 'Government Polytechnic, Palanpur'}</CardTitle>
              <CardDescription>
                {isGujarati ? 'GES ક્લાસ II લેક્ચરર' : 'GES Class II Lecturer'} • {isGujarati ? 'ઓક્ટોબર 2016 – હાલ' : 'October 2016 – Present'}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div>
                  <h4 className="font-semibold mb-2">{isGujarati ? '🎓 અધ્યાપન' : '🎓 Teaching'}</h4>
                  <p className="text-sm text-muted-foreground">
                    {isGujarati 
                      ? 'પ્રોગ્રામિંગ ઇન C, માઇક્રોકન્ટ્રોલર્સ, એમ્બેડેડ સિસ્ટમ્સ, સર્કિટ ડિઝાઇન, કન્ઝ્યુમર ઇલેક્ટ્રોનિક્સ, ઇન્ડસ્ટ્રિયલ મેનેજમેન્ટ'
                      : 'Programming in C, Microcontrollers, Embedded Systems, Circuit Design, Consumer Electronics, Industrial Management'}
                  </p>
                </div>
                <Separator />
                <div>
                  <h4 className="font-semibold mb-2">{isGujarati ? '💼 એડમિનિસ્ટ્રેટિવ' : '💼 Administrative'}</h4>
                  <p className="text-sm text-muted-foreground">
                    {isGujarati
                      ? 'DTE-MIS કમિટી, કેમ્પસ નેટવર્ક એડમિનિસ્ટ્રેશન, KCG ફિનિશિંગ સ્કૂલ પ્રોગ્રામ, SSIP કમિટી'
                      : 'DTE-MIS Committee, Campus Network Administration, KCG Finishing School Programme, SSIP Committee'}
                  </p>
                </div>
                <Separator />
                <div>
                  <h4 className="font-semibold mb-2">{isGujarati ? '🔬 રિસર્ચ ગાઇડન્સ' : '🔬 Research Guidance'}</h4>
                  <p className="text-sm text-muted-foreground">
                    {isGujarati
                      ? 'ઇલેક્ટ્રોનિક્સ અને એમ્બેડેડ સિસ્ટમ્સમાં ઇનોવેટિવ સ્ટુડન્ટ પ્રોજેક્ટ્સનું સુપરવિઝન'
                      : 'Supervising innovative student projects in electronics and embedded systems'}
                  </p>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>{isGujarati ? 'TEXEG ઇન્ડિયા પ્રાઇવેટ લિમિટેડ' : 'TEXEG India Private Limited'}</CardTitle>
              <CardDescription>
                {isGujarati ? 'ઇલેક્ટ્રોનિક્સ એન્જિનિયર' : 'Electronics Engineer'} • {isGujarati ? 'જુલાઈ 2015 – ઓક્ટોબર 2016' : 'July 2015 – October 2016'}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <ul className="space-y-2 text-sm">
                <li>• {isGujarati ? 'R&D ટેસ્ટિંગ: ટેસ્ટ સેટઅપ ડિઝાઇન, ડેટા કલેક્શન, એનાલિસિસ અને રિપોર્ટિંગ' : 'R&D Testing: Test setup design, data collection, analysis and reporting'}</li>
                <li>• {isGujarati ? 'કન્ટ્રોલર ડિઝાઇન: MATLAB ટૂલબોક્સનો ઉપયોગ કરીને PID, PI, અને ફઝી લોજિક કન્ટ્રોલર્સ' : 'Controller Design: PID, PI, and Fuzzy logic controllers using MATLAB toolboxes'}</li>
                <li>• {isGujarati ? 'ફર્મવેર ડેવલપમેન્ટ: સિસ્ટમ ફર્મવેર ડિઝાઇન, ડેવલપમેન્ટ, ટેસ્ટિંગ અને ડિબગિંગ' : 'Firmware Development: System firmware design, development, testing and debugging'}</li>
                <li>• {isGujarati ? 'હાર્ડવેર સિસ્ટમ્સ: ઇલેક્ટ્રોનિક સિસ્ટમ્સની ડિઝાઇન, ડેવલપમેન્ટ અને ટ્રબલશૂટિંગ' : 'Hardware Systems: Design, development and troubleshooting of electronic systems'}</li>
              </ul>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Certifications Tab */}
        <TabsContent value="certifications" className="space-y-6">
          <ScrollArea className="h-[600px] rounded-md border p-4">
            <div className="space-y-4">
              <Card>
                <CardHeader>
                  <CardTitle>{isGujarati ? 'Coursera સ્પેશિલાઇઝેશન્સ' : 'Coursera Specializations'}</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="grid gap-3">
                    {[
                      { name: isGujarati ? 'એડવાન્સ્ડ મશીન લર્નિંગ' : 'Advanced Machine Learning', topics: 'Deep Learning, Computer Vision, NLP' },
                      { name: isGujarati ? 'મશીન લર્નિંગ' : 'Machine Learning', topics: 'Supervised Learning, Regression, Classification' },
                      { name: isGujarati ? 'ડીપ લર્નિંગ' : 'Deep Learning', topics: 'Neural Networks, CNN, RNN' },
                      { name: isGujarati ? 'રેકમેન્ડર સિસ્ટમ્સ' : 'Recommender Systems', topics: 'Collaborative Filtering, Matrix Factorization' },
                    ].map((cert, i) => (
                      <div key={i} className="flex items-start gap-3 p-3 rounded-lg border">
                        <Award className="h-5 w-5 text-primary mt-1" />
                        <div>
                          <h4 className="font-semibold">{cert.name}</h4>
                          <p className="text-sm text-muted-foreground">{cert.topics}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle>{isGujarati ? 'NPTEL સિદ્ધિઓ' : 'NPTEL Achievements'}</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="space-y-3">
                    <div className="flex items-center gap-2">
                      <Badge>🌟 {isGujarati ? 'ડિસિપ્લિન સ્ટાર 2020' : 'Discipline Star 2020'}</Badge>
                    </div>
                    <div className="flex items-center gap-2">
                      <Badge variant="secondary">📣 {isGujarati ? 'ઇવેન્જેલિસ્ટ 2020' : 'Evangelist 2020'}</Badge>
                    </div>
                    <div className="flex items-center gap-2">
                      <Badge variant="outline">💪 {isGujarati ? 'મોટિવેટેડ લર્નર 2020' : 'Motivated Learner 2020'}</Badge>
                    </div>
                    <div className="flex items-center gap-2">
                      <Badge variant="outline">🎯 {isGujarati ? 'બિલીવર 2020' : 'Believer 2020'}</Badge>
                    </div>
                  </div>
                </CardContent>
              </Card>

              <Card>
                <CardHeader>
                  <CardTitle>{isGujarati ? 'Udemy સર્ટિફિકેશન્સ' : 'Udemy Certifications'}</CardTitle>
                </CardHeader>
                <CardContent>
                  <ul className="space-y-2 text-sm">
                    <li>• CCNA Routing and Switching</li>
                    <li>• Machine Learning and Data Science</li>
                    <li>• Complete Python Masterclass</li>
                    <li>• Complete JavaScript Course</li>
                    <li>• MBA in 1 Course</li>
                  </ul>
                </CardContent>
              </Card>
            </div>
          </ScrollArea>
        </TabsContent>

        {/* Skills Tab */}
        <TabsContent value="skills" className="space-y-6">
          <div className="grid gap-6 md:grid-cols-2">
            <Card>
              <CardHeader>
                <CardTitle>{isGujarati ? 'પ્રોગ્રામિંગ ભાષાઓ' : 'Programming Languages'}</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  {['Python', 'C/C++', 'Java', 'JavaScript', 'TypeScript', 'R', 'MATLAB'].map((skill) => (
                    <Badge key={skill} variant="secondary">{skill}</Badge>
                  ))}
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>{isGujarati ? 'વેબ ટેકનોલોજીસ' : 'Web Technologies'}</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  {['Next.js', 'React', 'Node.js', 'HTML/CSS', 'Tailwind CSS'].map((skill) => (
                    <Badge key={skill} variant="secondary">{skill}</Badge>
                  ))}
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>{isGujarati ? 'ડેટા સાયન્સ' : 'Data Science'}</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  {['Pandas', 'NumPy', 'Scikit-learn', 'TensorFlow', 'Keras', 'PyTorch'].map((skill) => (
                    <Badge key={skill} variant="secondary">{skill}</Badge>
                  ))}
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>{isGujarati ? 'એમ્બેડેડ સિસ્ટમ્સ' : 'Embedded Systems'}</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  {['Arduino', 'Raspberry Pi', 'STM32', 'PIC', 'AVR', '8051'].map((skill) => (
                    <Badge key={skill} variant="secondary">{skill}</Badge>
                  ))}
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>{isGujarati ? 'ટૂલ્સ અને પ્લેટફોર્મ્સ' : 'Tools & Platforms'}</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  {['Git', 'Docker', 'VS Code', 'Proteus', 'KiCad', 'AWS'].map((skill) => (
                    <Badge key={skill} variant="secondary">{skill}</Badge>
                  ))}
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>{isGujarati ? 'ડેટાબેસિસ' : 'Databases'}</CardTitle>
              </CardHeader>
              <CardContent>
                <div className="flex flex-wrap gap-2">
                  {['MongoDB', 'MySQL', 'PostgreSQL'].map((skill) => (
                    <Badge key={skill} variant="secondary">{skill}</Badge>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>
        </TabsContent>
      </Tabs>
    </div>
  );
}

export async function generateMetadata({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const { lang } = await searchParams;
  const locale = lang === 'gu' ? 'gu' : undefined;
  const portfolio = getContentBySlug('portfolio', 'index', locale);

  if (!portfolio) {
    return {
      title: 'Portfolio Not Found',
    };
  }

  return {
    title: portfolio.metadata.title,
    description: portfolio.metadata.description || portfolio.metadata.summary,
  };
}
