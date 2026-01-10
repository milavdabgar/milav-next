# Slidev Complete Guide

## Table of Contents
1. [Overview & Features](#overview--features)
2. [Syntax Guide](#syntax-guide)
3. [Advanced Syntax Features](#advanced-syntax-features)
4. [Layouts](#layouts)
5. [Components](#components)
6. [Animations](#animations)
7. [Built-in Components](#built-in-components)
8. [Built-in Layouts](#built-in-layouts)
9. [Advanced Features](#advanced-features)
10. [Configuration](#configuration)
11. [Export & Hosting](#export--hosting)

---

## Overview & Features

Slidev is a developer-focused presentation tool that uses Markdown to create interactive slides.

### Key Features
- **Presentation Creation**: Markdown-based slide creation with developer-focused tools
- **Customization**: Themes, addons, configurable highlighter, Vue/Vite plugins, UnoCSS integration
- **Interactive Elements**: Monaco code editor, code running/editing, drawing tools, click animations
- **Advanced Functionality**: Remote slide access, recording, side editor, global context, slide hooks
- **Development Workflow**: VS Code extension, CLI tools, code snippet imports, canvas control
- **Export & Sharing**: PDF export, hosting capabilities, remote asset bundling
- **Diagram Support**: LaTeX, Mermaid, PlantUML integration
- **Icon Support**: Built-in icon libraries

*Note: Each feature can be used independently and is optional.*

---

## Syntax Guide

### Slide Structure
- Slides are written in "Slidev Markdown" format
- Slides separated by `---` on a new line
- Default entry file: `./slides.md`

### Frontmatter Configuration
Optional YAML configuration blocks:
- **Headmatter**: First block configures entire presentation
- **Slide-specific**: Configure individual slides

```md
---
theme: seriph
title: Welcome to Slidev
---

# Slide 1

---
layout: center
background: /background-1.png
class: text-white
---

# Slide 2
```

### Code Blocks
- Markdown-flavored code blocks with Shiki syntax highlighting
- Supports line numbers, max height, line highlighting
- Monaco Editor integration available

### Additional Syntax Features
- **Notes**: Add presenter notes at slide end
- **LaTeX**: Mathematical expressions and formulas
- **Diagrams**: Mermaid and PlantUML support
- **Scoped CSS**: Slide-specific styling
- **Slide Importing**: Import slides from other files
- **MDC Syntax**: Markdown Component syntax

### Presenter Notes with Click Markers
Add progressive highlighting to presenter notes:

```md
---
layout: default
---

# My Slide Content

<!--
Content before any clicks

[click] This will be highlighted after the first click

This content is also highlighted after first click

- [click] This list item highlights on second click
- Regular list item

[click:4] This content appears on the 4th click (skipping click 3)

Final notes content
-->
```

#### Click Marker Features
- **Progressive Highlighting**: Notes highlight based on slide clicks
- **Auto-scrolling**: Automatically scrolls to current marker
- **Skip Clicks**: Use `[click:{n}]` to skip to specific click numbers
- **Synchronization**: Keeps presenter notes in sync with slide progress
- Available since Slidev v0.48.0

---

## Advanced Syntax Features

### Advanced Code Block Features

#### Line Highlighting
```md
```ts {2,4-6}
function add(a: number, b: number) {
  return a + b  // highlighted
}
console.log('not highlighted')
console.log('highlighted')  // highlighted
console.log('highlighted')  // highlighted
```
```

#### Line Numbers Configuration

##### Global Line Numbers
Enable line numbers for all code blocks:
```yaml
---
# In headmatter (applies to entire presentation)
lineNumbers: true
---
```

##### Per-Block Line Numbers
Enable for specific code blocks:
```md
```ts {lines:true}
// Shows line numbers for this block only
function example() {
  return 'hello'
}
```
```

##### Custom Starting Line Numbers
```md
```ts {lines:true,startLine:5}
// Line numbers start from 5
function example() {
  return 'world'
}
```

```ts {6,7}{lines:true,startLine:5}
// Combined with line highlighting
function add(
  a: Ref<number> | number,  // Line 6
  b: Ref<number> | number   // Line 7
) {
  return computed(() => unref(a) + unref(b))
}
```
```

#### Max Height and Scrolling

##### Fixed Height with Scrolling
```md
```ts {maxHeight:'100px'}
// Creates scrollable code block
function longFunction() {
  const line1 = 'This is a very long function'
  const line2 = 'With many lines of code'
  const line3 = 'That would exceed slide height'
  const line4 = 'So we enable scrolling'
  const line5 = 'Users can scroll to see more'
  // ... many more lines
  return 'result'
}
```
```

##### Max Height with Line Highlighting
```md
```ts {2|3|7|12}{maxHeight:'120px'}
function add(
  a: Ref<number> | number,    // Highlighted on first click
  b: Ref<number> | number     // Highlighted on second click
) {
  console.log('Adding numbers')
  const result = computed(() => {
    return unref(a) + unref(b)  // Highlighted on third click
  })
  
  // More code lines...
  console.log('Calculation complete')
  return result                 // Highlighted on fourth click
}
```
```

##### Combining All Options
```md
```typescript {2,4-6}{lines:true,startLine:10,maxHeight:'150px'}
// All features combined: highlighting, line numbers, height limit
function complexExample(
  param1: string,        // Line 11, highlighted
  param2: number
) {                      // Lines 14-16, highlighted
  const processing = 'Complex logic here'
  const moreLogic = 'Even more processing'
  
  // Many more lines that will require scrolling...
  return { param1, param2, processing }
}
```
```

#### Code Groups (Tabbed Code)
```md
:::code-group

```js [config.js]
export default {
  theme: 'seriph'
}
```

```ts [config.ts]
export default {
  theme: 'seriph'
} as const
```

:::
```

### Code Snippet Importing
Import code from external files:

```md
<!-- Import entire file -->
<<< @/snippets/example.js

<!-- Import with line highlighting -->
<<< @/snippets/example.js{2,4-6}

<!-- Import specific lines -->
<<< @/snippets/example.js#region-name
```

### Twoslash TypeScript Integration
Show TypeScript hover information and errors:

```md
```ts twoslash
interface User {
  name: string
}

const user: User = {
  name: 'John'
//    ^?
}
```
```

### Shiki Magic Move
Animated code transitions between slides:

```md
```ts {*|1|2-5}
function fibonacci(n: number): number {
  if (n <= 1) return n
  return fibonacci(n - 1) + fibonacci(n - 2)
}
```
```

### Advanced Frontmatter Options

#### Comprehensive Slide Configuration
```yaml
---
layout: center
background: '/bg-image.jpg'
backgroundSize: cover
class: 'text-white'
transition: slide-left
clicks: 5
zoom: 0.8
download: true
hideInToc: true
routeAlias: /custom-route
info: |
  ## Slide Notes
  This slide demonstrates advanced features
  - Custom routing
  - Background control
  - Zoom settings
---
```

#### Global Presentation Configuration
```yaml
---
# Headmatter (first slide)
theme: seriph
title: 'My Presentation'
author: 'Your Name' 
highlighter: shiki
lineNumbers: true
downloads: true
export:
  format: pdf
  timeout: 30000
monaco: dev
drawings:
  enabled: true
  persist: false
remoteAssets: true
---
```

---

## Layouts

Layouts are Vue components that wrap slide content and define structural presentation.

### Layout Usage
Specify in slide frontmatter:
```md
---
layout: quote
---

A quote from someone
```

### Layout Loading Order
1. Default built-in layouts
2. Theme-provided layouts
3. Addon-provided layouts
4. Custom layouts in `layouts/` directory

### Default Behavior
- First slide: `cover` layout
- Subsequent slides: `default` layout

### Custom Layouts
Create custom layouts in the `layouts/` directory as Vue components.

---

## Components

Components allow you to use Vue components directly in slides.

### Using Components
Components are automatically available without manual importing:

```md
# My Slide

<MyComponent :count="4"/>
```

### Component Sources
1. **Built-in components** (provided by Slidev)
2. **Theme and addon components**
3. **Custom components** in `components/` directory

### Creating Custom Components
Create Vue files in the `components/` directory:

```
your-slidev/
  ├── slides.md
  └── components/
      └── MyComponent.vue
```

---

## Animations

Slidev provides powerful animation capabilities for dynamic presentations.

### Click Animations

#### Basic Click Controls
Use `<v-click>` component or `v-click` directive:

```html
<v-click>This appears on click</v-click>
<div v-click>This too</div>
<div v-click.hide>This hides after click</div>
```

#### Advanced Click Positioning
```html
<!-- Appear at specific click number -->
<v-click at="3">Appears on 3rd click</v-click>

<!-- Relative positioning -->
<v-click at="+2">Appears 2 clicks after previous</v-click>

<!-- Hide after specific click -->
<v-click at="[2, 4]">Visible from click 2 to 4</v-click>
```

#### Click Lists and Groups
```html
<!-- Animate list items sequentially -->
<v-clicks>
  <li>First item</li>
  <li>Second item</li>
  <li>Third item</li>
</v-clicks>

<!-- Control animation timing -->
<v-clicks :every="2">
  <div>Appears every 2 clicks</div>
  <div>This too</div>
</v-clicks>

<!-- With custom starting point -->
<v-clicks at="3">
  <p>Starts from click 3</p>
  <p>Then this appears</p>
</v-clicks>
```

#### After Animations
```html
<!-- Show after previous element -->
<div v-click>First element</div>
<div v-after>Shows after first</div>

<!-- Chain multiple v-after elements -->
<div v-click>Click to start</div>
<div v-after>Second</div>
<div v-after>Third</div>
<div v-after>Fourth</div>
```

### Motion Effects
Powered by @vueuse/motion with `v-motion` directive:

#### Basic Motion
```html
<div
  v-motion
  :initial="{ x: -80 }"
  :enter="{ x: 0 }"
  :click-1="{ y: 30 }"
>
  Animated Element
</div>
```

#### Advanced Motion States
```html
<div
  v-motion
  :initial="{ x: -80, opacity: 0 }"
  :enter="{ x: 0, opacity: 1, transition: { duration: 1000 } }"
  :hovered="{ scale: 1.2 }"
  :focused="{ scale: 1.1 }"
  :click-1="{ y: -30, rotate: 45 }"
  :leave="{ x: 80, opacity: 0 }"
>
  Complex Animation
</div>
```

#### Motion with Custom Timing
```html
<div
  v-motion
  :initial="{ scale: 0 }"
  :enter="{ 
    scale: 1,
    transition: {
      type: 'spring',
      stiffness: 300,
      damping: 20
    }
  }"
>
  Spring Animation
</div>
```

#### Motion Variants
```html
<div
  v-motion
  :variants="{
    initial: { opacity: 0, y: 100 },
    visible: { opacity: 1, y: 0 },
    hovered: { scale: 1.1 }
  }"
  :initial="'initial'"
  :enter="'visible'"
  :hovered="'hovered'"
>
  Variant-based Animation
</div>
```

### Slide Transitions

#### Basic Transitions
Configure in frontmatter:

```yaml
---
transition: slide-left
clicks: 10  # Total clicks before next slide
---
```

#### Directional Transitions
```yaml
---
# Different forward and backward transitions
transition: slide-left | slide-right
---
```

#### Built-in Transitions
- **`fade`**: Fade in/out effect
- **`slide-left/right/up/down`**: Slide from specified direction
- **`view-transition`**: Modern View Transition API
- **`zoom`**: Zoom in/out effect
- **`flip`**: 3D flip animation

#### Custom Transition Classes
```yaml
---
transition: my-custom-transition
---
```

```css
.my-custom-transition-enter-active,
.my-custom-transition-leave-active {
  transition: all 0.3s ease;
}
.my-custom-transition-enter-from {
  opacity: 0;
  transform: translateX(-100%);
}
.my-custom-transition-leave-to {
  opacity: 0;
  transform: translateX(100%);
}
```

#### Per-Slide Transition Control
```yaml
---
# Disable transition for this slide
transition: false
---

---
# Override global transition
transition: fade
---
```

---

## Built-in Components

### Arrow Components

#### Arrow
Draws arrows between coordinates:
```html
<Arrow x1="10" y1="20" x2="100" y2="200" />

<!-- With styling options -->
<Arrow 
  x1="10" y1="20" x2="100" y2="200" 
  width="3" 
  color="red" 
  two-way 
/>
```

#### VDragArrow
Draggable version of Arrow:
```html
<VDragArrow x1="10" y1="20" x2="100" y2="200" />
```

### Text Components

#### AutoFitText
Auto-adjusts text font size:
```html
<AutoFitText :max="200" :min="100" modelValue="Some text"/>

<!-- With custom content -->
<AutoFitText :max="150" :min="50">
  Dynamic sized text that fits the container
</AutoFitText>
```

### Theme Components

#### LightOrDark
Theme-conditional content:
```html
<LightOrDark>
  <template #dark>Dark mode content</template>
  <template #light>Light mode content</template>
</LightOrDark>
```

#### VSwitch
Toggle between two states:
```html
<VSwitch>
  <template #1>First state content</template>
  <template #2>Second state content</template>
</VSwitch>

<!-- With custom trigger -->
<VSwitch :names="['Code', 'Result']">
  <template #Code>
    ```js
    console.log('Hello World')
    ```
  </template>
  <template #Result>
    Hello World
  </template>
</VSwitch>
```

### Navigation Components

#### Link
Navigate to specific slides:
```html
<Link to="42">Go to slide 42</Link>

<!-- With custom title -->
<Link to="intro" title="Back to Introduction">Go Back</Link>

<!-- External links -->
<Link to="https://slidev.dev" external>Slidev Website</Link>
```

### Conditional Rendering

#### RenderWhen
Conditional rendering based on context:
```html
<!-- Single context -->
<RenderWhen context="main">Only in main view</RenderWhen>

<!-- Multiple contexts -->
<RenderWhen context="presenter,print">
  Visible in presenter and print modes
</RenderWhen>

<!-- Available contexts: main, presenter, print, slide -->
<RenderWhen context="slide">Only in slide view</RenderWhen>
```

### Media Components

#### Youtube
Embed YouTube videos:
```html
<Youtube id="luoMHjh-XcQ" />

<!-- With custom dimensions -->
<Youtube id="luoMHjh-XcQ" width="800" height="450" />
```

#### SlidevVideo
Enhanced video player:
```html
<SlidevVideo controls autoplay autoreset poster="/poster.jpg">
  <source src="/video.mp4" type="video/mp4">
  <source src="/video.webm" type="video/webm">
</SlidevVideo>

<!-- With custom controls -->
<SlidevVideo 
  :controls="true"
  :autoplay="false"
  :muted="true"
  :loop="true"
  timestamp="30"
>
  <source src="/demo.mp4" type="video/mp4">
</SlidevVideo>
```

### Social Media

#### Tweet
Embed tweets:
```html
<Tweet id="1390115482657726468" />

<!-- With conversation -->
<Tweet id="1390115482657726468" conversation />

<!-- Custom scale -->
<Tweet id="1390115482657726468" scale="0.8" />
```

### Transform Components

#### Transform
Scale and transform elements:
```html
<Transform :scale="0.8">
  <div>Scaled down content</div>
</Transform>

<!-- Multiple transformations -->
<Transform :scale="1.5" :rotate="45" :translate-x="100">
  <p>Transformed content</p>
</Transform>

<!-- Responsive transforms -->
<Transform 
  :scale="{ xs: 0.5, sm: 0.7, md: 1.0 }"
  origin="top-left"
>
  <div>Responsive scaling</div>
</Transform>
```

### Utility Components

#### SlideCurrentNo & SlidesTotal
Display slide numbers:
```html
<div class="absolute bottom-4 right-4">
  <SlideCurrentNo /> / <SlidesTotal />
</div>

<!-- Custom formatting -->
<div>
  Slide <SlideCurrentNo format="roman" /> of <SlidesTotal />
</div>
```

#### Toc
Table of contents:
```html
<Toc />

<!-- With custom options -->
<Toc 
  :columns="2" 
  :max-depth="2"
  :mode="'onlySiblings'"
/>

<!-- Custom styling -->
<Toc class="my-toc">
  <template #title="{ title }">
    🎯 {{ title }}
  </template>
</Toc>
```

#### PoweredBySlidev
Branding component:
```html
<PoweredBySlidev />

<!-- Custom positioning -->
<PoweredBySlidev class="absolute bottom-2 right-2 opacity-50" />
```

### Interactive Components

#### Rough Notation
Add hand-drawn annotations:
```html
<RoughNotation type="underline" color="red">
  Important text
</RoughNotation>

<!-- Multiple annotation types -->
<RoughNotation type="box" :stroke-width="3" color="blue">
  Boxed content
</RoughNotation>

<RoughNotation type="highlight" color="yellow">
  Highlighted text
</RoughNotation>

<!-- Animated annotations -->
<RoughNotation 
  type="circle" 
  :animate="true" 
  :duration="2000"
  v-click
>
  Click to animate
</RoughNotation>
```

---

## Built-in Layouts

### Basic Layouts
- **`center`**: Content centered on screen
- **`cover`**: Title page layout
- **`default`**: Basic content layout
- **`end`**: Final presentation page
- **`full`**: Full screen content
- **`none`**: No styling

### Content Layouts
- **`fact`**: Prominent fact/data display
- **`quote`**: Quotation display
- **`statement`**: Main affirmation display
- **`intro`**: Presentation introduction
- **`section`**: Section divider

### Image Layouts

#### image-left
```yaml
---
layout: image-left
image: /path/to/image
class: my-cool-content-on-the-right
---
```

#### image-right
Similar to `image-left` but image on right side.

#### image
```yaml
---
layout: image
image: /path/to/image
backgroundSize: contain
---
```

### Column Layouts

#### two-cols
```md
---
layout: two-cols
---
# Left Column
Content here

::right::
# Right Column
Content here
```

#### two-cols-header
Header section with two-column content below.

### Web Integration
- **`iframe-left`**: Embed webpage on left
- **`iframe-right`**: Embed webpage on right

---

## Advanced Features

### Development Tools

#### Monaco Editor Integration
Enable in-slide code editing with full IDE features:

```yaml
---
# Global configuration
monaco: true  # or 'dev' for development only
---
```

```html
<!-- Monaco editor block -->
```ts {monaco}
function fibonacci(n: number): number {
  if (n <= 1) return n
  return fibonacci(n - 1) + fibonacci(n - 2)
}

console.log(fibonacci(10))
```
```

#### Code Runners
Execute code directly in presentations:

```html
```js {monaco-run}
// This code can be executed
const result = 2 + 2
console.log(`Result: ${result}`)
```
```

#### Drawing Tools
Enable slide annotations and drawing:

```yaml
---
# Enable drawing globally
drawings:
  enabled: true
  persist: false  # Don't save drawings
  presenterOnly: true  # Only in presenter mode
---
```

### Global Layers
Persistent elements across all slides:

```html
<!-- In components/global/Bottom.vue -->
<template>
  <div class="absolute bottom-0 left-0 right-0 p-4">
    <div class="text-sm opacity-50">
      My Presentation - {{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}
    </div>
  </div>
</template>
```

### Slide Hooks
Lifecycle events for advanced slide control:

```js
// In setup/main.ts
import { onSlideEnter, onSlideLeave } from '@slidev/client'

onSlideEnter((ctx) => {
  console.log('Entering slide:', ctx.no)
  // Custom logic when entering slide
})

onSlideLeave((ctx) => {
  console.log('Leaving slide:', ctx.no)
  // Cleanup or save state
})
```

### Remote Control
Access presentations from different devices:

```bash
# Start with remote access
slidev --remote

# Access from other devices at:
# http://localhost:3030/presenter (presenter view)
# http://localhost:3030 (audience view)
```

### Recording Presentations
Built-in recording capabilities:

```yaml
---
# Enable recording features
record: true
---
```

```html
<!-- Recording controls -->
<div v-if="$slidev.nav.record">
  <button @click="$slidev.nav.record.start()">Start Recording</button>
  <button @click="$slidev.nav.record.stop()">Stop Recording</button>
</div>
```

---

## Configuration

### Slidev Config File
Create `slidev.config.ts` for advanced configuration:

```ts
import { defineConfig } from '@slidev/cli'

export default defineConfig({
  // Presentation metadata
  title: 'My Presentation',
  author: 'Your Name',
  
  // Appearance
  theme: 'seriph',
  highlighter: 'shiki',
  lineNumbers: true,
  
  // Features
  monaco: 'dev',
  download: true,
  drawings: {
    enabled: true,
    persist: false
  },
  
  // Export settings
  export: {
    format: 'pdf',
    timeout: 30000,
    dark: false,
    withClicks: true
  },
  
  // Remote access
  remote: true,
  remoteAssets: true,
  
  // Build optimization
  routerMode: 'hash',
  contextMenu: true,
  
  // Custom CSS
  css: 'uno',
  
  // Vite configuration
  vite: {
    server: {
      port: 3030
    }
  }
})
```

### Environment Variables
Configure via environment:

```bash
# Development
SLIDEV_THEME=seriph
SLIDEV_HIGHLIGHTER=shiki
SLIDEV_MONACO=true

# Production
SLIDEV_EXPORT_FORMAT=pdf
SLIDEV_BASE_URL=/presentations/
```

### Package.json Scripts
Recommended development scripts:

```json
{
  "scripts": {
    "dev": "slidev",
    "build": "slidev build",
    "export": "slidev export",
    "deploy": "slidev build --base /my-slides/",
    "preview": "slidev build && slidev --host 0.0.0.0"
  }
}
```

### Advanced Styling
Custom CSS and UnoCSS configuration:

```css
/* style.css */
.my-custom-slide {
  background: linear-gradient(45deg, #667eea, #764ba2);
}

.code-highlight {
  background: rgba(255, 255, 0, 0.2);
  padding: 2px 4px;
  border-radius: 4px;
}
```

```ts
// uno.config.ts
import { defineConfig } from 'unocss'

export default defineConfig({
  shortcuts: [
    ['btn', 'px-4 py-2 rounded bg-blue-500 text-white hover:bg-blue-600'],
    ['slide-title', 'text-4xl font-bold mb-8']
  ],
  theme: {
    colors: {
      primary: '#667eea',
      secondary: '#764ba2'
    }
  }
})
```

---

## Export & Hosting

### PDF Export
Generate PDF presentations:

```bash
# Basic export
slidev export

# With custom options
slidev export --format pdf --output my-slides.pdf

# Export with clicks
slidev export --with-clicks

# Dark mode export
slidev export --dark
```

### Static Site Generation
Build for hosting:

```bash
# Build static files
slidev build

# Build with custom base URL
slidev build --base /presentations/

# Build for GitHub Pages
slidev build --base /repo-name/
```

### Hosting Platforms

#### Netlify
```toml
# netlify.toml
[build]
  command = "npm run build"
  publish = "dist"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
```

#### Vercel
```json
{
  "builds": [
    {
      "src": "package.json",
      "use": "@vercel/static-build",
      "config": {
        "buildCommand": "slidev build"
      }
    }
  ]
}
```

#### GitHub Pages
```yaml
# .github/workflows/deploy.yml
name: Deploy Slides
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run build
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./dist
```

### Remote Assets
Bundle remote assets for offline use:

```yaml
---
# Enable remote asset bundling
remoteAssets: true
---
```

```html
<!-- These will be bundled -->
<img src="https://example.com/image.jpg" />
<iframe src="https://example.com/embed" />
```

### Performance Optimization

#### Lazy Loading
```html
<!-- Images with lazy loading -->
<img v-lazy="'/images/large-image.jpg'" />

<!-- Components with lazy loading -->
<LazyWrapper>
  <ExpensiveComponent />
</LazyWrapper>
```

#### Code Splitting
```ts
// Lazy load heavy components
const HeavyChart = defineAsyncComponent(() => import('./HeavyChart.vue'))
```

---

## Quick Reference

### Essential Frontmatter Options
```yaml
---
layout: default
background: /bg.png
class: text-center
transition: slide-left
clicks: 5
theme: seriph
---
```

### Common Component Patterns
```html
<!-- Click animations -->
<v-click>Appear on click</v-click>
<div v-click="2">Appear on 2nd click</div>

<!-- Motion -->
<div v-motion :initial="{x: -80}" :enter="{x: 0}">
  Slide in from left
</div>

<!-- Navigation -->
<Link to="5">Jump to slide 5</Link>

<!-- Conditional content -->
<RenderWhen context="presenter">
  Only visible in presenter mode
</RenderWhen>
```

### File Structure
```
your-slidev/
  ├── slides.md          # Main presentation
  ├── components/        # Custom components
  ├── layouts/          # Custom layouts  
  ├── public/           # Static assets
  └── package.json      # Dependencies
```

---

*This guide covers the essential Slidev features for creating interactive, developer-friendly presentations. For advanced usage and latest updates, refer to the official Slidev documentation.*