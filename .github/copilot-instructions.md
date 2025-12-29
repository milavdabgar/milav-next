# Copilot Instructions for milav-next

## Project Overview
- **Type:** Personal portfolio & blog
- **Stack:** Next.js 15 (App Router), TypeScript, Tailwind CSS v4, shadcn/ui, MDX, React 19
- **Content:** Bilingual (English/Gujarati) with MDX-based content in `/content`.
- **UI:** Custom components in `/components` (see `ui/`, `layouts/`, `templates/`, `mdx/`).

## Key Architectural Patterns
- **App Router:** All routing is under `/app`. Dynamic routes use `[...slug]` and `[tag]`.
- **MDX Content:** Content is loaded from `/content` using utilities in `lib/mdx.ts`. Supports localization via file naming (e.g., `about.gu.mdx`).
- **Layouts:** Use layout components from `components/layouts/` and `components/templates/` for page structure. Most pages use `GridPageLayout` or `ContentTemplate`.
- **UI Components:** All reusable UI is in `components/ui/`. Use these for consistent design (e.g., `Button`, `Breadcrumbs`, `Card`).
- **Theming:** Theme context is provided via `lib/contexts/theme-context` and used in `app/layout.tsx`.
- **SEO:** Metadata is set in `app/layout.tsx` and per-page as needed.

## Developer Workflows
- **Install:** `npm install`
- **Dev server:** `npm run dev` (or `pnpm dev`, `bun dev`)
- **Build:** `npm run build`
- **Lint:** `npm run lint`
- **Content:** Add MDX files to `/content`. Use frontmatter for metadata.
- **Components:** Add new UI to `components/ui/`. Prefer composition over inheritance.

## Project Conventions
- **MDX:** Use React components in MDX. See `components/mdx-components.tsx` for mapped elements (e.g., custom `Table`, `CodeBlock`, `Mermaid`).
- **Breadcrumbs:** Use `Breadcrumbs` from `components/ui/breadcrumbs.tsx` for navigation. Pass `items` prop as array of `{label, href}`.
- **Localization:** For Gujarati, use `.gu.mdx` suffix. Fallback to default if not found.
- **Content API:** API routes in `app/api/` (e.g., `content-image/route.ts`) serve files from `/content` securely.
- **Styling:** Use Tailwind utility classes. Avoid inline styles.
- **Imports:** Use `@/` alias for root imports (see `tsconfig.json`).

## Integration Points
- **Fonts:** Uses `next/font` for Geist Sans/Mono.
- **Mermaid:** Diagrams via `Mermaid` component in MDX.
- **Carousel:** Use `CarouselGallery` for image galleries in MDX.

## Examples
- **Add a blog post:** Place `my-post.mdx` in `/content/blog/` with frontmatter. Use `<Mermaid />` or `<CarouselGallery />` as needed.
- **Add a new UI component:** Create in `components/ui/`, export, and use in MDX via `components/mdx-components.tsx`.

## References
- See `README.md` for setup basics.
- See `lib/mdx.ts` for content loading logic.
- See `components/mdx-components.tsx` for MDX element mapping.
- See `components/layouts/` and `components/templates/` for page structure patterns.

---
For questions or unclear conventions, check the referenced files or ask for clarification.
