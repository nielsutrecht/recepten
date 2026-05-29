## 1. Extract RecipeCard Component

- [x] 1.1 Create `src/components/RecipeCard.astro` accepting `recipe` and `base` props
- [x] 1.2 Move card markup from `index.astro` into the component; add `data-title`, `data-tags`, `data-category` attributes to the card `<div>`
- [x] 1.3 Change outer card element from `<a>` to `<div class="recipe-card">`; make title a `<a class="card-title-link">` linking to the detail page
- [x] 1.4 Make category badge an `<a>` linking to `/categorie/<category>/`
- [x] 1.5 Make each tag pill an `<a>` linking to `/tag/<tag>/`
- [x] 1.6 Update `index.astro` to import and use `RecipeCard.astro`; verify cards still render correctly

## 2. Category Pages

- [x] 2.1 Create `src/pages/categorie/[category].astro` with `getStaticPaths()` deriving all categories from non-draft recipe IDs
- [x] 2.2 Filter to only generate pages for categories with ≥1 recipe; sort recipes by pubDate descending
- [x] 2.3 Render page with heading (capitalised category name), recipe count, and card grid using `RecipeCard.astro`

## 3. Tag Pages

- [x] 3.1 Create `src/pages/tag/[tag].astro` with `getStaticPaths()` deriving all unique tags from non-draft recipes
- [x] 3.2 Filter recipes to those carrying the tag; sort by pubDate descending
- [x] 3.3 Render page with heading (tag name), recipe count, and card grid using `RecipeCard.astro`

## 4. Home Page Search and Tag Filter

- [x] 4.1 Add search input above the card grid in `index.astro` with placeholder "Zoek een recept…"
- [x] 4.2 Derive all unique tags at build time; render tag chip toggles as `<button>` elements with `data-tag` attributes
- [x] 4.3 Add inline `<script>` implementing text search: on input, hide cards where `data-title` does not include the query (lowercase)
- [x] 4.4 Extend script with tag filter: maintain a `Set` of active tags; on chip click toggle membership, update chip active style, hide cards where no `data-tag` intersects active set
- [x] 4.5 Combine filters: a card is visible when it matches the text search AND satisfies the tag filter (OR across selected tags)
- [x] 4.6 Style search input and tag chips to match the site's warm minimal aesthetic; active chip uses terracotta fill

## 5. Verify

- [x] 5.1 Run `npm run build` — confirm clean build, check page count increased for categories and tags
- [x] 5.2 Run `npm run dev`; confirm home page search filters cards live as you type
- [x] 5.3 Confirm tag chips toggle and filter correctly with OR logic; confirm search + tags combine
- [x] 5.4 Click a category badge — confirm it navigates to the correct category page showing only that category's recipes
- [x] 5.5 Click a tag pill — confirm it navigates to the correct tag page showing only that tag's recipes
