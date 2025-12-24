"use client";

import { useState, useEffect } from "react";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Download, FileText, Printer, Copy, Check, Globe, Code } from "lucide-react";
import { useToast } from "@/hooks/use-toast";
import { usePathname, useSearchParams } from "next/navigation";

interface BlogDownloadProps {
  title: string;
  slug?: string;
}

interface DownloadFormat {
  id: string;
  name: string;
  description: string;
  extension: string;
  category: string;
}

export function BlogDownload({ title, slug }: BlogDownloadProps) {
  const [copied, setCopied] = useState(false);
  const [isDownloading, setIsDownloading] = useState(false);
  const [formats, setFormats] = useState<DownloadFormat[]>([]);
  const { toast } = useToast();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const locale = searchParams.get('lang') || 'en';

  useEffect(() => {
    // Load supported formats
    fetch('/api/download?action=supported-formats')
      .then(res => res.json())
      .then(data => setFormats(data.formats || []))
      .catch(err => console.error('Failed to load formats:', err));
  }, []);

  const handleDownload = async (formatId: string) => {
    if (!slug) {
      // Fallback to simple download
      handleSimpleDownload(formatId);
      return;
    }

    setIsDownloading(true);

    try {
      const response = await fetch('/api/download', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          slug,
          locale,
          format: formatId,
          title,
        }),
      });

      if (!response.ok) {
        throw new Error('Download failed');
      }

      const blob = await response.blob();
      const format = formats.find(f => f.id === formatId);
      const filename = `${title.replace(/[^a-z0-9]/gi, "-").toLowerCase()}.${format?.extension || 'txt'}`;

      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = filename;
      a.click();
      URL.revokeObjectURL(url);

      toast({
        title: "Download Complete",
        description: `${format?.name || formatId} file downloaded successfully`,
      });
    } catch (error) {
      console.error('Download error:', error);
      toast({
        variant: "destructive",
        title: "Download Failed",
        description: "Could not download the file. Please try again.",
      });
    } finally {
      setIsDownloading(false);
    }
  };

  const handleSimpleDownload = (format: string) => {
    const article = document.querySelector("article");
    if (!article) return;

    let content: string;
    let mimeType: string;
    let extension: string;

    switch (format) {
      case 'md':
        content = `# ${title}\n\n${article.innerText}`;
        mimeType = "text/markdown";
        extension = "md";
        break;
      case 'html':
        content = `<!DOCTYPE html>
<html><head><meta charset="UTF-8"><title>${title}</title></head>
<body><h1>${title}</h1>${article.innerHTML}</body></html>`;
        mimeType = "text/html";
        extension = "html";
        break;
      case 'json':
        content = JSON.stringify({ title, content: article.innerText }, null, 2);
        mimeType = "application/json";
        extension = "json";
        break;
      default:
        content = article.innerText;
        mimeType = "text/plain";
        extension = "txt";
    }

    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `${title.replace(/[^a-z0-9]/gi, "-").toLowerCase()}.${extension}`;
    a.click();
    URL.revokeObjectURL(url);

    toast({
      title: "Download Complete",
      description: `File downloaded successfully`,
    });
  };

  const handlePrint = () => {
    window.print();
    toast({
      title: "Print",
      description: "Opening print dialog...",
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

  const getIcon = (formatId: string) => {
    switch (formatId) {
      case 'html': return Globe;
      case 'json': return Code;
      default: return FileText;
    }
  };

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="sm" disabled={isDownloading}>
          <Download className="h-4 w-4 mr-2" />
          {isDownloading ? "Downloading..." : "Download"}
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-56">
        <DropdownMenuLabel>Export Formats</DropdownMenuLabel>
        <DropdownMenuSeparator />
        
        {formats.map((format) => {
          const Icon = getIcon(format.id);
          return (
            <DropdownMenuItem key={format.id} onClick={() => handleDownload(format.id)}>
              <Icon className="h-4 w-4 mr-2" />
              <div className="flex flex-col">
                <span>{format.name}</span>
                <span className="text-xs text-muted-foreground">{format.description}</span>
              </div>
            </DropdownMenuItem>
          );
        })}
        
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
