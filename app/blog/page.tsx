import { getAllContent, getContentBySlug } from '@/lib/mdx';
import { getDirectoryContent } from '@/lib/directory-utils';
import { getBreadcrumbs } from '@/lib/breadcrumbs';
import Link from 'next/link';
import { GridPageLayout } from '@/components/layouts';
import { ResourceCard } from '@/components/ui/resource-card';
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { formatDate } from '@/lib/utils';
import { FileText } from 'lucide-react';

import { MDXRemote } from 'next-mdx-remote/rsc';
import { mdxComponents } from '@/components/mdx-components';

export default async function BlogPage({
  searchParams,
}: {
  searchParams: Promise<{ lang?: string }>;
}) {
  const params = await searchParams;
  const locale = params.lang || 'en';
  const isGujarati = locale === 'gu';

  const posts = getAllContent('blog');
  const indexContent = getContentBySlug('blog', '_index', isGujarati ? 'gu' : undefined);

  const { files: dirFiles } = getDirectoryContent('blog', locale === 'gu' ? 'gu' : undefined);
  const staticFiles = dirFiles.filter((f: any) => f.type !== 'mdx');

  const breadcrumbItems = getBreadcrumbs('blog', [], locale);

  const descriptionContent = indexContent?.content ? (
    <MDXRemote source={indexContent.content} components={mdxComponents} />
  ) : (
    indexContent?.metadata.description || (isGujarati
      ? 'ટ્યુટોરિયલ, ગાઇડ્સ અને ટેકનિકલ આર્ટિકલ્સ'
      : 'Tutorials, guides, and technical articles')
  );

  return (
    <GridPageLayout
      title={indexContent?.metadata.title || (isGujarati ? 'બ્લોગ' : 'Blog')}
      description={descriptionContent}
      columns={{ default: 1, md: 2, lg: 3 }}
      breadcrumbs={breadcrumbItems}
    >
      {posts.map((post) => (
        <ResourceCard
          key={post.slug}
          title={post.metadata.title}
          description={post.metadata.description || post.metadata.summary}
          date={post.metadata.date ? formatDate(post.metadata.date) : undefined}
          type="article"
          tags={post.metadata.tags}
          href={`/blog/${post.slug}${isGujarati ? '?lang=gu' : ''}`}
          className="h-full"
        />
      ))}

      {staticFiles.length > 0 && (
        <div className="col-span-full mt-12">
          <h2 className="text-2xl font-bold mb-6">Files</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {staticFiles.map((file: any) => {
              // Construct the path for the API
              // content/blog/filename.pdf -> /api/file?path=blog/filename.pdf
              // The 'slug' from getDirectoryContent for files is just filename without ext, or filename?
              // lib/directory-utils says: filename: file
              const filePath = `blog/${file.filename}`;
              const fileUrl = `/api/file?path=${encodeURIComponent(filePath)}`;

              return (
                <Link key={file.filename} href={fileUrl} target="_blank" rel="noopener noreferrer">
                  <Card className="h-full hover:bg-muted/50 transition-colors">
                    <CardHeader className="flex flex-row items-center gap-4">
                      <FileText className="h-8 w-8 text-red-500" />
                      <div>
                        <CardTitle className="text-lg truncate max-w-[200px]" title={file.title as string}>{file.title as string}</CardTitle>
                        <CardDescription>{file.extension?.toUpperCase().replace('.', '') || 'FILE'}</CardDescription>
                      </div>
                    </CardHeader>
                    <CardContent>
                      <span className="text-sm font-medium text-blue-600 dark:text-blue-400">View File &rarr;</span>
                    </CardContent>
                  </Card>
                </Link>
              );
            })}
          </div>
        </div>
      )}

      {posts.length === 0 && staticFiles.length === 0 && (
        <Card className="col-span-full p-12 text-center">
          <p className="text-muted-foreground">
            {isGujarati ? 'કોઈ બ્લોગ પોસ્ટ્સ મળી નથી' : 'No blog posts found'}
          </p>
        </Card>
      )}
    </GridPageLayout>
  );
}

export const metadata = {
  title: 'Blog - Milav Dabgar',
  description: 'Technical tutorials, guides, and articles on electronics, programming, and data science',
};
