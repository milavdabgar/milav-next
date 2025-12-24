"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Download, FileText, Printer, Copy, Check } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

interface BlogDownloadProps {
  title: string;
  content?: string;
}

export function BlogDownload({ title, content }: BlogDownloadProps) {
  const [copied, setCopied] = useState(false);
  const { toast } = useToast();

  const handlePrint = () => {
    window.print();
    toast({
      title: "Print",
      description: "Opening print dialog...",
    });
  };

  const handleDownloadMarkdown = () => {
    const article = document.querySelector("article");
    if (!article) return;

    const mdContent = content || article.innerText;
    const blob = new Blob([mdContent], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${title.replace(/[^a-z0-9]/gi, "-").toLowerCase()}.md`;
    a.click();
    URL.revokeObjectURL(url);

    toast({
      title: "Download Complete",
      description: "Markdown file downloaded successfully",
    });
  };

  const handleDownloadText = () => {
    const article = document.querySelector("article");
    if (!article) return;

    const textContent = article.innerText;
    const blob = new Blob([textContent], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${title.replace(/[^a-z0-9]/gi, "-").toLowerCase()}.txt`;
    a.click();
    URL.revokeObjectURL(url);

    toast({
      title: "Download Complete",
      description: "Text file downloaded successfully",
    });
  };

  const handleCopyToClipboard = async () => {
    const article = document.querySelector("article");
    if (!article) return;

    try {
      await navigator.clipboard.writeText(article.innerText);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
      
      toast({
        title: "Copied!",
        description: "Article content copied to clipboard",
      });
    } catch (err) {
      toast({
        variant: "destructive",
        title: "Error",
        description: "Failed to copy to clipboard",
      });
    }
  };

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="sm">
          <Download className="h-4 w-4 mr-2" />
          Download
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-48">
        <DropdownMenuLabel>Export Options</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuItem onClick={handleDownloadMarkdown}>
          <FileText className="h-4 w-4 mr-2" />
          Download as Markdown
        </DropdownMenuItem>
        <DropdownMenuItem onClick={handleDownloadText}>
          <FileText className="h-4 w-4 mr-2" />
          Download as Text
        </DropdownMenuItem>
        <DropdownMenuSeparator />
        <DropdownMenuItem onClick={handlePrint}>
          <Printer className="h-4 w-4 mr-2" />
          Print Article
        </DropdownMenuItem>
        <DropdownMenuItem onClick={handleCopyToClipboard}>
          {copied ? (
            <Check className="h-4 w-4 mr-2" />
          ) : (
            <Copy className="h-4 w-4 mr-2" />
          )}
          {copied ? "Copied!" : "Copy to Clipboard"}
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
}
