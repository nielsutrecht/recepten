## Why

With 12+ recipes across 5 categories the home page is an unsorted wall — finding a specific recipe requires scanning every card. This change adds the last core PRD navigation features: client-side search and tag filtering on the home page, plus static category and tag pages for direct linking.

## What Changes

- Extract the recipe card markup into a shared `RecipeCard.astro` component reused across all listing pages
- Add static category pages at `/categorie/[category]/` — category badge on each card links here
- Add static tag pages at `/tag/[tag]/` — tag pills on each card link here
- Home page gains a text search input (substring match on title) and tag chip toggles (OR logic), all client-side with no page reload

## Capabilities

### New Capabilities

- `recipe-card-component`: Shared `RecipeCard.astro` component used by all recipe listing pages
- `category-pages`: Static pages listing all recipes in a given category
- `tag-pages`: Static pages listing all recipes with a given tag
- `home-search-filter`: Client-side text search and tag chip filter on the home page

### Modified Capabilities

- `recipe-card-grid`: Category badge and tag pills become navigation links (to category/tag pages respectively)
- `recipe-listing`: Home page listing gains search and tag filter controls above the card grid

## Impact

- `src/components/RecipeCard.astro` — new file
- `src/pages/index.astro` — adds search/filter UI and inline JS; uses RecipeCard component
- `src/pages/categorie/[category].astro` — new file
- `src/pages/tag/[tag].astro` — new file
- No schema changes, no new dependencies
