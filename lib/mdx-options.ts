import rehypePrettyCode from 'rehype-pretty-code';
import type { Options } from 'rehype-pretty-code';

export const rehypePrettyCodeOptions: Options = {
  theme: {
    dark: 'one-dark-pro',
    light: 'github-light',
  },
  keepBackground: false,
  onVisitLine(node: any) {
    // Prevent lines from collapsing in `display: grid` mode, and allow empty
    // lines to be copy/pasted
    if (node.children.length === 0) {
      node.children = [{ type: 'text', value: ' ' }];
    }
  },
  onVisitHighlightedLine(node: any) {
    node.properties.className?.push('highlighted');
  },
  onVisitHighlightedChars(node: any) {
    node.properties.className = ['word'];
  },
};

export const mdxOptions = {
  rehypePlugins: [[rehypePrettyCode, rehypePrettyCodeOptions]],
};
