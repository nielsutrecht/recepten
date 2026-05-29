## Why

The home page is a plain unstyled list and the recipe detail page has no way to adjust quantities — both make the site feel unfinished and limit its usefulness while actually cooking. These are the two highest-value features to build before adding more recipes.

## What Changes

- Replace the `<ul>` recipe list on the home page with a responsive 2-column card grid; each card shows category, total time, tag pills, and kid ratings
- Add a `[−] N [+]` serving scaler to recipe detail pages; ingredient quantities update in real time via vanilla JS using kitchen-sensible rounding

## Capabilities

### New Capabilities

- `recipe-card-grid`: Home page displays recipes as a 2-column card grid with category, time, tags, and kid ratings per card
- `serving-scaler`: Recipe detail page has a `[−] N [+]` control that scales ingredient quantities proportionally using kitchen-sensible rounding

### Modified Capabilities

- `recipe-listing`: Display format changes from plain list to card grid (new visual requirements for existing listing behaviour)
- `recipe-detail`: Servings display gains interactive scaler; ingredient quantities become dynamically updatable

## Impact

- `src/pages/index.astro` — rewritten to emit card grid markup with CSS
- `src/pages/[...slug].astro` — servings row gains scaler buttons; ingredients gain JS hook
- New inline `<script>` on the detail page (vanilla JS, no dependencies)
- No schema changes, no new dependencies
