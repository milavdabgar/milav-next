
import * as React from "react"
import Link from "next/link"
import Image from "next/image"
import { cn } from "@/lib/utils"
import { CodeBlock } from "@/components/ui/code-block"
import { Mermaid } from "@/components/ui/mermaid"

// Table components
const Table = ({ className, ...props }: React.HTMLAttributes<HTMLTableElement>) => (
    <div className="my-6 w-full overflow-y-auto">
        <table className={cn("w-full caption-bottom text-sm", className)} {...props} />
    </div>
)

const TableHeader = ({ className, ...props }: React.HTMLAttributes<HTMLTableSectionElement>) => (
    <thead className={cn("[&_tr]:border-b", className)} {...props} />
)

const TableBody = ({ className, ...props }: React.HTMLAttributes<HTMLTableSectionElement>) => (
    <tbody className={cn("[&_tr:last-child]:border-0", className)} {...props} />
)

const TableRow = ({ className, ...props }: React.HTMLAttributes<HTMLTableRowElement>) => (
    <tr className={cn("border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted", className)} {...props} />
)

const TableHead = ({ className, ...props }: React.ThHTMLAttributes<HTMLTableCellElement>) => (
    <th className={cn("h-12 px-4 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0", className)} {...props} />
)

const TableCell = ({ className, ...props }: React.TdHTMLAttributes<HTMLTableCellElement>) => (
    <td className={cn("p-4 align-middle [&:has([role=checkbox])]:pr-0", className)} {...props} />
)

// Typography components mapping to standard HTML elements but with enforced styling if needed.
// However, Tailwind Typography (prose) usually handles h1-h6, p, ul, ol well.
// We only need to override if we want special behavior or if prose is not catching them.
// Let's provide explicit overrides to guarantee consistency regardless of Prose configuration.

const H1 = ({ className, ...props }: React.HTMLAttributes<HTMLHeadingElement>) => (
    <h1 className={cn("scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl mb-8 mt-10", className)} {...props} />
)

const H2 = ({ className, ...props }: React.HTMLAttributes<HTMLHeadingElement>) => (
    <h2 className={cn("scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight first:mt-0 mb-6 mt-10", className)} {...props} />
)

const H3 = ({ className, ...props }: React.HTMLAttributes<HTMLHeadingElement>) => (
    <h3 className={cn("scroll-m-20 text-2xl font-semibold tracking-tight mb-4 mt-8", className)} {...props} />
)

const H4 = ({ className, ...props }: React.HTMLAttributes<HTMLHeadingElement>) => (
    <h4 className={cn("scroll-m-20 text-xl font-semibold tracking-tight mb-4 mt-6", className)} {...props} />
)

const P = ({ className, ...props }: React.HTMLAttributes<HTMLParagraphElement>) => (
    <p className={cn("leading-7 [&:not(:first-child)]:mt-6 mb-6", className)} {...props} />
)

const UL = ({ className, ...props }: React.HTMLAttributes<HTMLUListElement>) => (
    <ul className={cn("my-6 ml-6 list-disc [&>li]:mt-2", className)} {...props} />
)

const OL = ({ className, ...props }: React.HTMLAttributes<HTMLOListElement>) => (
    <ol className={cn("my-6 ml-6 list-decimal [&>li]:mt-2", className)} {...props} />
)

const Blockquote = ({ className, ...props }: React.HTMLAttributes<HTMLQuoteElement>) => (
    <blockquote className={cn("mt-6 border-l-2 pl-6 italic", className)} {...props} />
)

const CustomLink = ({ className, href, ...props }: React.AnchorHTMLAttributes<HTMLAnchorElement>) => {
    const isInternal = href && (href.startsWith("/") || href.startsWith("#"))
    const isAnchor = href && href.startsWith("#")

    if (isInternal) {
        return (
            <Link
                href={href}
                className={cn("font-medium text-primary underline underline-offset-4", className)}
                {...props}
            />
        )
    }

    return (
        <a
            href={href}
            target="_blank"
            rel="noopener noreferrer"
            className={cn("font-medium text-primary underline underline-offset-4", className)}
            {...props}
        />
    )
}

const Pre = ({ className, ...props }: React.HTMLAttributes<HTMLPreElement>) => (
    <pre className={cn("mb-4 mt-6 overflow-x-auto rounded-lg border bg-black py-4", className)} {...props} />
)

const Code = ({ className, children, ...props }: React.HTMLAttributes<HTMLElement>) => {
    const isCodeBlock = className && className.startsWith('language-');
    const language = className ? className.replace('language-', '') : '';

    if (language === 'mermaid') {
        return <Mermaid>{String(children)}</Mermaid>;
    }

    if (isCodeBlock) {
        return <CodeBlock className={className}>{String(children).replace(/\n$/, '')}</CodeBlock>;
    }

    return (
        <code className={cn("relative rounded bg-muted px-[0.3rem] py-[0.2rem] font-mono text-sm font-semibold", className)} {...props}>
            {children}
        </code>
    );
}

export const mdxComponents = {
    h1: H1,
    h2: H2,
    h3: H3,
    h4: H4,
    p: P,
    ul: UL,
    ol: OL,
    blockquote: Blockquote,
    a: CustomLink,
    pre: Pre,
    code: Code,
    table: Table,
    thead: TableHeader,
    tbody: TableBody,
    tr: TableRow,
    th: TableHead,
    td: TableCell,
    Image,
}
