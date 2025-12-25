
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { Folder, FileText, BookOpen } from 'lucide-react';
import { cn } from '@/lib/utils';
import { ReactNode } from 'react';

interface ResourceCardProps {
    title: string;
    description?: string;
    type: 'folder' | 'article' | 'file';
    href?: string;
    icon?: ReactNode;
    className?: string;
    date?: string;
    tags?: string[];
    readingTime?: string;
}

export function ResourceCard({
    title,
    description,
    type,
    icon,
    className,
    date,
    tags,
    readingTime,
}: ResourceCardProps) {

    // Determine default icon and color based on type
    let DefaultIcon = Folder;
    let iconColorClass = "text-blue-500";

    switch (type) {
        case 'folder':
            DefaultIcon = Folder;
            iconColorClass = "text-blue-500";
            break;
        case 'article':
            DefaultIcon = BookOpen;
            iconColorClass = "text-green-500";
            break;
        case 'file':
            DefaultIcon = FileText;
            iconColorClass = "text-red-500";
            break;
    }

    return (
        <Card className={cn("h-full hover:shadow-lg transition-all duration-200 hover:bg-muted/30 group", className)}>
            <CardHeader className="flex flex-row items-start gap-4 space-y-0 pb-3">
                <div className={cn("mt-1 shrink-0 p-2 rounded-lg bg-background/50 group-hover:bg-background/80 transition-colors", iconColorClass)}>
                    {icon || <DefaultIcon className="h-6 w-6" />}
                </div>
                <div className="space-y-1 min-w-0 flex-1">
                    <CardTitle className="text-lg leading-tight line-clamp-2 group-hover:text-primary transition-colors">
                        {title}
                    </CardTitle>
                    {description && (
                        <CardDescription className="line-clamp-2 text-sm">
                            {description}
                        </CardDescription>
                    )}
                </div>
            </CardHeader>

            {(date || tags || readingTime) && (
                <CardContent className="pt-0">
                    <div className="flex flex-wrap items-center gap-x-4 gap-y-2 text-xs text-muted-foreground mt-2">
                        {date && (
                            <span>{date}</span>
                        )}
                        {readingTime && (
                            <span>{readingTime}</span>
                        )}
                        {tags && tags.length > 0 && (
                            <div className="flex gap-1 flex-wrap">
                                {tags.slice(0, 3).map(tag => (
                                    <span key={tag} className="inline-flex px-1.5 py-0.5 rounded-full bg-secondary/50 text-secondary-foreground">
                                        #{tag}
                                    </span>
                                ))}
                                {tags.length > 3 && (
                                    <span className="inline-flex px-1.5 py-0.5 rounded-full bg-secondary/50 text-secondary-foreground">+{tags.length - 3}</span>
                                )}
                            </div>
                        )}
                    </div>
                </CardContent>
            )}
        </Card>
    );
}
