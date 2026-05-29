## Why

The site has no navigation beyond the home link — `/kids/` is unreachable without typing the URL, and there's no way to know the Weekplanner is coming. Pages also lack context about where you are in the site hierarchy.

## What Changes

- Extend the header with two nav links: **Voor de kids** (`/kids/`) and **Weekplanner** (`/planner/`, placeholder until built)
- Add optional `breadcrumbs` prop to `Base.astro`; render a trail below the header on inner pages
- Wire breadcrumbs on: recipe detail (`Recepten / category / title`), category pages (`Recepten / category`), tag pages (`Recepten / tag`), kids page (`Recepten / voor de kids`)
- Remove the existing `← Alle recepten` back-link from pages where breadcrumbs replace it

## Capabilities

### New Capabilities

- `site-nav`: Persistent header navigation with links to all top-level destinations
- `breadcrumbs`: Contextual trail showing the current page's position in the hierarchy

### Modified Capabilities

- `category-pages`: Back-link replaced by breadcrumb
- `tag-pages`: Back-link replaced by breadcrumb
- `kids-page`: Back-link replaced by breadcrumb

## Impact

- `src/layouts/Base.astro` — header gains nav; new breadcrumb slot below header
- `src/pages/[...slug].astro` — passes breadcrumbs prop
- `src/pages/categorie/[category].astro` — passes breadcrumbs, removes back-link
- `src/pages/tag/[tag].astro` — passes breadcrumbs, removes back-link
- `src/pages/kids.astro` — passes breadcrumbs, removes back-link
- No schema changes, no new dependencies
