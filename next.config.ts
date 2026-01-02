import type { NextConfig } from "next";
import createMDX from '@next/mdx';

const nextConfig: NextConfig = {
  // Enable standalone output for Docker deployments
  output: 'standalone',
  pageExtensions: ['js', 'jsx', 'md', 'mdx', 'ts', 'tsx'],
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**',
      },
    ],
  },
  async rewrites() {
    return [
      {
        source: '/resources/study-materials/:path*',
        has: [
          {
            type: 'query',
            key: 'path', // This is just to ensure we don't conflict with existing pages if somehow query params matched, but basic regex matching on extension is safer or order matters.
            // Actually next.js rewrites don't support regex on source clearly like that in simple format.
            // Better to use a reliable source pattern.
          }
        ],
        destination: '/should-not-match-this-way'
      },
      // We want to catch image extensions. Next.js doesn't support regex in `source` directly in the simple way? 
      // It supports `:path*`. We can rely on the API to handle non-images if we route everything? No, we need to route pages to pages.
      // So we must distinguish.
      // We can use `source: '/resources/study-materials/:path*.jpg'` etc.
      {
        source: '/resources/study-materials/:path*.jpg',
        destination: '/api/content-image?path=resources/study-materials/:path*.jpg',
      },
      {
        source: '/resources/study-materials/:path*.jpeg',
        destination: '/api/content-image?path=resources/study-materials/:path*.jpeg',
      },
      {
        source: '/resources/study-materials/:path*.png',
        destination: '/api/content-image?path=resources/study-materials/:path*.png',
      },
      {
        source: '/resources/study-materials/:path*.gif',
        destination: '/api/content-image?path=resources/study-materials/:path*.gif',
      },
      {
        source: '/resources/study-materials/:path*.svg',
        destination: '/api/content-image?path=resources/study-materials/:path*.svg',
      },
      {
        source: '/resources/study-materials/:path*.pdf',
        destination: '/api/content-image?path=resources/study-materials/:path*.pdf',
      }
    ];
  },
};

const withMDX = createMDX({
  // Add markdown plugins here, as desired
  options: {
    remarkPlugins: [],
    rehypePlugins: [],
  },
});

export default withMDX(nextConfig);
