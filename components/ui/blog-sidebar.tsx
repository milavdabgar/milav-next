"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { cn } from "@/lib/utils";
import { FileText, Calendar, Tag, User } from "lucide-react";
import { ScrollArea } from "@/components/ui/scroll-area";

interface BlogPost {
  slug: string;
  title: string;
  date?: string;
}

interface BlogSidebarProps {
  posts: BlogPost[];
  className?: string;
}

export function BlogSidebar({ posts, className }: BlogSidebarProps) {
  const pathname = usePathname();

  return (
    <aside className={cn("hidden md:block border-r bg-muted/30", className)}>
      <div className="sticky top-16 h-[calc(100vh-4rem)]">
        <div className="p-4 border-b">
          <h2 className="font-semibold flex items-center gap-2">
            <FileText className="h-4 w-4" />
            Blog Posts
          </h2>
        </div>
        <ScrollArea className="h-[calc(100vh-8rem)]">
          <div className="p-2">
            {posts.map((post) => {
              const isActive = pathname.includes(post.slug);
              return (
                <Link
                  key={post.slug}
                  href={`/blog/${post.slug}`}
                  className={cn(
                    "block p-3 rounded-md text-sm transition-colors hover:bg-muted",
                    isActive
                      ? "bg-muted font-medium text-foreground"
                      : "text-muted-foreground"
                  )}
                >
                  <div className="line-clamp-2">{post.title}</div>
                  {post.date && (
                    <div className="text-xs text-muted-foreground mt-1 flex items-center gap-1">
                      <Calendar className="h-3 w-3" />
                      {new Date(post.date).toLocaleDateString()}
                    </div>
                  )}
                </Link>
              );
            })}
          </div>
        </ScrollArea>
      </div>
    </aside>
  );
}
