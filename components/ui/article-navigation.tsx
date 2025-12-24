"use client";

import Link from "next/link";
import { ChevronLeft, ChevronRight } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";

interface ArticleNavigationProps {
  previousPost?: {
    slug: string;
    title: string;
  };
  nextPost?: {
    slug: string;
    title: string;
  };
  locale?: string;
}

export function ArticleNavigation({
  previousPost,
  nextPost,
  locale = "en",
}: ArticleNavigationProps) {
  if (!previousPost && !nextPost) return null;

  const langParam = locale === "gu" ? "?lang=gu" : "";

  return (
    <div className="mt-12 pt-8 border-t">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Previous Post */}
        {previousPost ? (
          <Card className="hover:bg-muted/50 transition-colors">
            <CardContent className="p-4">
              <Link
                href={`/blog/${previousPost.slug}${langParam}`}
                className="group flex items-center gap-3"
              >
                <ChevronLeft className="h-5 w-5 text-muted-foreground group-hover:text-foreground transition-colors" />
                <div className="flex-1 min-w-0">
                  <div className="text-xs text-muted-foreground mb-1">
                    Previous
                  </div>
                  <div className="text-sm font-medium group-hover:text-primary transition-colors line-clamp-2">
                    {previousPost.title}
                  </div>
                </div>
              </Link>
            </CardContent>
          </Card>
        ) : (
          <div />
        )}

        {/* Next Post */}
        {nextPost && (
          <Card className="hover:bg-muted/50 transition-colors">
            <CardContent className="p-4">
              <Link
                href={`/blog/${nextPost.slug}${langParam}`}
                className="group flex items-center gap-3 text-right"
              >
                <div className="flex-1 min-w-0">
                  <div className="text-xs text-muted-foreground mb-1">
                    Next
                  </div>
                  <div className="text-sm font-medium group-hover:text-primary transition-colors line-clamp-2">
                    {nextPost.title}
                  </div>
                </div>
                <ChevronRight className="h-5 w-5 text-muted-foreground group-hover:text-foreground transition-colors" />
              </Link>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}
