## Context

The home page currently renders a static card grid with no way to filter. Category and tag labels appear on cards but aren't clickable. With 12+ recipes this is already causing friction; the problem compounds as more recipes are added.

The card grid markup is currently inlined in `index.astro`. Category and tag pages need the same markup, so extraction into a shared component is a prerequisite for all other work in this change.

## Goals / Non-Goals

**Goals:**
- Shared `RecipeCard.astro` component eliminates duplication
- Category and tag pages are statically generated — no JS required for navigation
- Home page search and tag filter work client-side with no page reload
- Category badge and tag pills on cards become navigation links

**Non-Goals:**
- Combined search + category/tag filter across pages (search only on home page)
- AND logic for tag chips (OR is sufficient at current recipe count)
- Persistent filter state in URL or localStorage
- Pagination (not needed at current scale)

## Decisions

### Shared RecipeCard component

**Decision:** Extract card markup and CSS into `src/components/RecipeCard.astro`. Accept `recipe`, `base` as props.

**Rationale:** Three pages (home, category, tag) render identical cards. Inlining the markup in each would create three copies to keep in sync. Component extraction is the standard Astro pattern.

---

### Static category and tag pages

**Decision:** `src/pages/categorie/[category].astro` and `src/pages/tag/[tag].astro` using `getStaticPaths()` — Astro generates one page per category/tag at build time.

**Rationale:** The site is fully static. Server-side filtering at request time isn't available. Static generation is the correct Astro approach and produces fast, cacheable pages.

**Category derivation:** `[...new Set(recipes.map(r => r.id.split('/')[0]))]` — extracted from recipe IDs at build time, no separate config needed.

**Tag derivation:** `[...new Set(recipes.flatMap(r => r.data.tags))]` — all unique tags across all recipes.

---

### Category badge and tag pills become links

**Decision:** Category badge links to `/categorie/<category>/`; each tag pill links to `/tag/<tag>/`. Both open as normal `<a>` navigations (full page load).

**Rationale:** Agreed in exploration. Static pages, not in-page filters. The whole card being a link conflicts with having clickable children — this requires the child links to `stopPropagation` or wrapping differently.

**Implementation:** Change the outer card from `<a>` wrapping the whole card to a `<div>` with a dedicated title link. This avoids nested interactive elements. The title remains the primary tap target; category and tag become secondary links.

---

### Client-side search and tag filter

**Decision:** `data-title`, `data-tags`, `data-category` attributes on each card `<div>`. Inline `<script>` on `index.astro` handles input events and shows/hides cards.

**Rationale:** All recipe data is available at build time. Serialising into `data-*` attributes is the simplest approach — no JSON blob needed, no extra HTTP requests. The script is ~40 lines and has zero dependencies.

**Tag OR logic:** If tags `[bbq, italiaans]` are selected, show cards matching EITHER tag. Implemented as: `selectedTags.length === 0 || selectedTags.some(t => cardTags.includes(t))`.

**Search + tag interaction:** Both filters apply simultaneously (AND between search and tag filters). A recipe must match the text search AND at least one selected tag.

---

### Card layout change: div + title link instead of wrapping `<a>`

**Decision:** The card outer element becomes `<div class="recipe-card">` with a `<a class="card-title-link">` around the title. Category and tag are `<a>` elements.

**Rationale:** HTML does not allow interactive elements (links, buttons) nested inside `<a>`. The previous whole-card-as-link approach must change once category and tags become links. Moving the primary link to the title is a minor UX change — the title is still prominent and large enough to tap.

## Risks / Trade-offs

- **Card tap target shrinks** — previously the entire card was tappable; now only the title is a link to the recipe. Mitigated by making the title large and by ensuring category/tag links give users alternative navigation.
- **Tag name collisions in URLs** — tags like "hoofdgerecht" appear on many recipes; the URL `/tag/hoofdgerecht/` is clean. Tags with spaces or special characters would need slugification — current tags are all lowercase single words so this isn't an issue yet.
- **Category page becomes stale** — if a category has 0 recipes after a deletion, its page is still generated. Mitigated by filtering at `getStaticPaths` time to only generate pages for categories with ≥1 recipe.
