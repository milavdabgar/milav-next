import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    fs: {
      allow: [
        // Allow serving files from the parent directories
        '..',
        '../..',
        // Allow Monaco Editor files
        '../../node_modules/monaco-editor',
        '../../node_modules/@unocss'
      ]
    }
  },
  build: {
    sourcemap: false
  },
  // Suppress source map warnings
  logLevel: 'warn'
})