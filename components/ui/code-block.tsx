"use client";

import React, { useEffect, useState } from 'react';
import { codeToHtml, BundledLanguage, BundledTheme } from 'shiki';
import { useTheme } from 'next-themes';
import { Button } from './button';
import { Copy, Check } from 'lucide-react';

interface CodeBlockProps {
  children: string;
  className?: string;
  inline?: boolean;
}

export function CodeBlock({ children, className = '', inline }: CodeBlockProps) {
  const [highlightedCode, setHighlightedCode] = useState<string>('');
  const [copied, setCopied] = useState(false);
  const { theme } = useTheme();

  // Extract language from className (format: language-xxx)
  const language = className.replace(/language-/, '') || 'text';

  // If inline code, render as simple code tag
  if (inline) {
    return <code className={className}>{children}</code>;
  }

  useEffect(() => {
    const highlightCode = async () => {
      try {
        // Handle special cases that Shiki doesn't support
        const unsupportedLanguages = ['goat', 'ascii', 'diagram', 'text', 'plain'];

        if (unsupportedLanguages.includes(language.toLowerCase())) {
          const escapedCode = children
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');

          setHighlightedCode(`<pre class="plain-text"><code>${escapedCode}</code></pre>`);
          return;
        }

        const lightTheme: BundledTheme = 'catppuccin-latte';
        const darkTheme: BundledTheme = 'one-dark-pro';

        // Handle language aliases
        let actualLanguage = language;
        if (language === 'yml') actualLanguage = 'yaml';
        if (language === 'js') actualLanguage = 'javascript';
        if (language === 'ts') actualLanguage = 'typescript';

        const html = await codeToHtml(children, {
          lang: actualLanguage as BundledLanguage,
          themes: {
            light: lightTheme,
            dark: darkTheme
          },
          defaultColor: false
        });

        setHighlightedCode(html);
      } catch (error) {
        console.error('Error highlighting code:', error);
        const escapedCode = children
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;');
        setHighlightedCode(`<pre class="plain-text"><code>${escapedCode}</code></pre>`);
      }
    };

    highlightCode();
  }, [children, language, theme]);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(children);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (error) {
      console.error('Failed to copy code:', error);
    }
  };

  const getDisplayLanguage = (lang: string) => {
    const languageMap: Record<string, string> = {
      'js': 'JavaScript',
      'ts': 'TypeScript',
      'py': 'Python',
      'python': 'Python',
      'java': 'Java',
      'cpp': 'C++',
      'c': 'C',
      'rust': 'Rust',
      'go': 'Go',
      'bash': 'Bash',
      'sh': 'Shell',
      'yaml': 'YAML',
      'yml': 'YAML',
      'json': 'JSON',
      'html': 'HTML',
      'css': 'CSS',
      'sql': 'SQL',
      'text': 'Plain Text',
      'plain': 'Plain Text'
    };
    return languageMap[lang.toLowerCase()] || lang;
  };

  return (
    <div className="relative group my-6">
      <div className="flex justify-between items-center bg-muted/50 border border-b-0 border-border rounded-t-lg px-4 py-2 text-sm">
        <span className="text-muted-foreground font-mono text-xs">
          {getDisplayLanguage(language)}
        </span>
        <Button
          variant="ghost"
          size="sm"
          onClick={handleCopy}
          className="h-6 w-6 p-0 hover:bg-muted/80"
        >
          {copied ? (
            <Check className="h-3 w-3 text-green-500" />
          ) : (
            <Copy className="h-3 w-3" />
          )}
        </Button>
      </div>
      <div
        className="[&>pre]:!mt-0 [&>pre]:!rounded-t-none"
        dangerouslySetInnerHTML={{ __html: highlightedCode }}
      />
    </div>
  );
}
