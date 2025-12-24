"use client";

import { useEffect, useState } from "react";
import { cn } from "@/lib/utils";
import { List, X } from "lucide-react";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Sheet, SheetContent, SheetHeader, SheetTitle, SheetTrigger } from "@/components/ui/sheet";

interface TocItem {
  id: string;
  text: string;
  level: number;
}

interface ResponsiveTocProps {
  className?: string;
}

export function ResponsiveToc({ className }: ResponsiveTocProps) {
  const [toc, setToc] = useState<TocItem[]>([]);
  const [activeId, setActiveId] = useState<string>("");
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    // Find all headings in the article
    const article = document.querySelector("article");
    if (!article) return;

    const headings = article.querySelectorAll("h2, h3, h4");
    const tocItems: TocItem[] = [];

    headings.forEach((heading, index) => {
      const level = parseInt(heading.tagName.substring(1));
      const text = heading.textContent || "";
      
      // Create ID if it doesn't exist
      let id = heading.id;
      if (!id) {
        id = `heading-${index}`;
        heading.id = id;
      }

      tocItems.push({ id, text, level });
    });

    setToc(tocItems);

    // Set up intersection observer for active heading
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id);
          }
        });
      },
      { rootMargin: "-80px 0px -80% 0px" }
    );

    headings.forEach((heading) => observer.observe(heading));

    return () => {
      headings.forEach((heading) => observer.unobserve(heading));
    };
  }, []);

  const scrollToHeading = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      const offset = 80;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - offset;
      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth",
      });
      setIsOpen(false); // Close mobile menu after click
    }
  };

  if (toc.length === 0) return null;

  const TocContent = () => (
    <nav className="space-y-1">
      {toc.map((item) => (
        <button
          key={item.id}
          onClick={() => scrollToHeading(item.id)}
          className={cn(
            "block w-full text-left py-2 px-3 text-sm transition-colors hover:text-foreground rounded-md",
            item.level === 2 && "pl-3",
            item.level === 3 && "pl-6",
            item.level === 4 && "pl-9",
            activeId === item.id
              ? "font-medium text-foreground bg-muted"
              : "text-muted-foreground hover:bg-muted/50"
          )}
        >
          {item.text}
        </button>
      ))}
    </nav>
  );

  return (
    <>
      {/* Desktop TOC - Always visible on large screens */}
      <aside className={cn("hidden lg:block", className)}>
        <div className="sticky top-24 space-y-4">
          <div className="text-sm font-semibold px-3 mb-4">On This Page</div>
          <ScrollArea className="h-[calc(100vh-12rem)]">
            <TocContent />
          </ScrollArea>
        </div>
      </aside>

      {/* Mobile TOC - Sheet that slides in */}
      <Sheet open={isOpen} onOpenChange={setIsOpen}>
        <SheetTrigger asChild className="lg:hidden fixed bottom-6 right-6 z-50">
          <Button size="icon" className="rounded-full shadow-lg h-14 w-14">
            <List className="h-6 w-6" />
          </Button>
        </SheetTrigger>
        <SheetContent side="right" className="w-80">
          <SheetHeader>
            <SheetTitle>Table of Contents</SheetTitle>
          </SheetHeader>
          <ScrollArea className="h-[calc(100vh-8rem)] mt-6">
            <TocContent />
          </ScrollArea>
        </SheetContent>
      </Sheet>
    </>
  );
}
