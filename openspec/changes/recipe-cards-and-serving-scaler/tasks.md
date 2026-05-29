## 1. Recipe Card Grid

- [x] 1.1 Rewrite `src/pages/index.astro` to extract category from `recipe.id.split('/')[0]`
- [x] 1.2 Replace `<ul>` with a `<div class="recipe-grid">` containing `<a class="recipe-card">` elements
- [x] 1.3 Each card renders: category label + time (top row), title (main), tag pills (if any), kid ratings (if any)
- [x] 1.4 Add CSS Grid styles: 2-column layout, single-column below 480px, equal card heights, card hover state

## 2. Serving Scaler — Markup

- [x] 2.1 In `src/pages/[...slug].astro`, replace the plain servings `<span>` with a scaler control: `<button>−</button> <span id="servings-count">N</span> <button>+</button>`
- [x] 2.2 Add `data-default-servings={data.servings}` to the ingredients container element

## 3. Serving Scaler — JavaScript

- [x] 3.1 Add inline `<script>` to `[...slug].astro` with a `roundKitchen(value)` function implementing the magnitude-based rounding table (nearest 10 / 5 / 1 / 0.5 / 0.25 with fraction symbols for < 1)
- [x] 3.2 Implement fraction display map: `{ 0.25: '¼', 0.5: '½', 0.75: '¾', 0.33: '⅓', 0.67: '⅔' }`
- [x] 3.3 Wire `[+]` and `[−]` buttons: read `data-default-servings`, clamp minimum to 1, update the servings display
- [x] 3.4 On servings change, iterate all `[data-quantity]` elements: compute `original * (current / default)`, apply `roundKitchen()`, update `textContent`

## 4. Verify

- [x] 4.1 Run `npm run build` — confirm clean build
- [x] 4.2 Run `npm run dev`, check home page: cards render in 2-column grid, collapse to 1 column on narrow viewport
- [x] 4.3 Open a recipe detail page: scaler shows default servings, `[+]` increases count and updates all quantities, `[−]` decreases (min 1)
- [x] 4.4 Verify rounding: scale tomatensoep 4→2 — `800g` → `400g`, `0.5 tl` → `¼ tl`, `2 el` → `1 el`
