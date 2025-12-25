
import { GridPageLayout } from '@/components/layouts';
import Link from 'next/link';
import { Card, CardHeader, CardTitle, CardDescription } from '@/components/ui/card';
import { BookOpen, FileText } from 'lucide-react';

export default async function ContentPage({
    searchParams,
}: {
    searchParams: Promise<{ lang?: string }>;
}) {
    const params = await searchParams;
    const locale = params.lang || 'en';
    const isGujarati = locale === 'gu';

    const items = [
        {
            title: isGujarati ? 'બ્લોગ' : 'Blog',
            description: isGujarati
                ? 'ટ્યુટોરિયલ, ગાઇડ્સ અને ટેકનિકલ આર્ટિકલ્સ'
                : 'Tutorials, guides, and technical articles',
            href: '/blog',
            icon: <BookOpen className="h-8 w-8 text-blue-500" />
        },
        {
            title: isGujarati ? 'સંસાધનો' : 'Resources',
            description: isGujarati
                ? 'GTU ડિપ્લોમા અભ્યાસક્રમ માટે નોંધો, પેપર્સ અને પુસ્તકો'
                : 'Study materials, notes, and papers for Diploma Engineering',
            href: '/resources',
            icon: <FileText className="h-8 w-8 text-green-500" />
        }
    ];

    return (
        <GridPageLayout
            title={isGujarati ? 'સામગ્રી' : 'Content'}
            description={isGujarati ? 'અમારી તમામ સામગ્રી અને સંસાધનોનું અન્વેષણ કરો' : 'Explore all our content and resources'}
            columns={{ default: 1, md: 2 }}
            breadcrumbs={[{ label: 'Content', href: '#' }]}
        >
            {items.map((item) => (
                <Link key={item.href} href={isGujarati ? `${item.href}?lang=gu` : item.href}>
                    <Card className="h-full hover:shadow-lg transition-shadow cursor-pointer">
                        <CardHeader className="flex flex-row items-center gap-4">
                            {item.icon}
                            <div>
                                <CardTitle>{item.title}</CardTitle>
                                <CardDescription>{item.description}</CardDescription>
                            </div>
                        </CardHeader>
                    </Card>
                </Link>
            ))}
        </GridPageLayout>
    );
}

export const metadata = {
    title: 'Content - Milav Dabgar',
    description: 'Explore blogs, resources, and study materials',
};
