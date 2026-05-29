## Context

The home page is currently a plain `<ul>` with title and time — functional but bare. The recipe detail page shows a static servings count with no way to scale. Both pages have all the data needed; this change is purely about presentation and interactivity.

The `data-quantity` attributes are already in place on ingredient spans from the scaffold change, so the scaler can be wired up without touching the schema or layout structure.

## Goals / Non-Goals

**Goals:**
- Home page becomes a browsable 2-column card grid
- Each card shows category, time, tags, kid ratings at a glance
- Serving scaler on detail page scales all ingredient quantities live
- Kitchen-sensible number rounding (not raw decimals)

**Non-Goals:**
- Search or tag filtering (separate change)
- Persistent scaler state across page loads (overkill for a personal cookbook)
- Images on cards (out of scope v1)
- CSS animations or transitions

## Decisions

### Card grid: CSS Grid, not flexbox

**Decision:** `display: grid; grid-template-columns: repeat(2, 1fr)` with a single media query to collapse to 1 column below ~480px.

**Rationale:** Grid gives equal-height rows and clean 2-column alignment without float hacks. Flexbox with `flex-wrap` would work but produces uneven card heights in the last row. CSS Grid is well-supported and matches the no-framework constraint.

---

### Whole card is a link

**Decision:** Wrap the entire card in an `<a>` tag styled as a block, rather than a title-only link.

**Rationale:** Larger tap target, especially on mobile where this is used at the kitchen counter. Avoids interactive elements nested inside links by keeping the card content purely presentational.

---

### Category derived from slug at build time

**Decision:** Extract category as `recipe.id.split('/')[0]` in the Astro template — no new frontmatter field.

**Rationale:** The category is already encoded in the file path (and therefore the id). Adding a redundant `category` frontmatter field would create a sync problem. The split is trivial and deterministic.

---

### Serving scaler: inline `<script>` on detail page

**Decision:** A single `<script>` tag at the bottom of `[...slug].astro`, emitting a self-contained IIFE. No external file, no build step, no framework.

**Rationale:** The scaler only runs on recipe pages and has zero dependencies. A separate JS file would require Astro's asset pipeline and adds complexity for ~30 lines of code. Inline script is simpler and consistent with the PRD's "vanilla JS" requirement.

**State:** In-memory only. Servings reset to default on page reload — no `localStorage`. Acceptable for a personal cookbook.

---

### Rounding algorithm

**Decision:** Magnitude-based rounding with fraction symbols for sub-1 values:

| Result range | Round to | Display example |
|---|---|---|
| < 1 | nearest 0.25 | ¼, ½, ¾ (or decimal if not clean) |
| 1 – 5 | nearest 0.5 | 1, 1.5, 2 |
| 5 – 20 | nearest 1 | 6, 13 |
| 20 – 100 | nearest 5 | 25, 75 |
| ≥ 100 | nearest 10 | 200, 850 |

Fraction map: `{ 0.25: '¼', 0.5: '½', 0.75: '¾', 0.33: '⅓', 0.67: '⅔' }` — only exact matches get symbols, others show as decimals rounded to 1 place.

**Rationale:** Raw decimal output (`166.7 g`) is confusing in a kitchen. This mirrors how cookbook authors round quantities when scaling recipes.

## Risks / Trade-offs

- **Whole-card `<a>` with nested interactive elements** → The scaler `[−]` / `[+]` buttons are on the detail page, not on cards, so no nesting conflict.
- **Inline script and Astro's CSP** → No CSP headers are set (static GH Pages), so inline scripts are fine.
- **Rounding edge cases** → Very large scaling factors (e.g. 1→20 servings) may produce odd numbers. Acceptable — the scaler is for typical kitchen adjustments (halve/double), not catering.
