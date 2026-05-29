## Context

The header is a single link. With `/kids/` already live and `/planner/` coming, the site needs persistent navigation. Breadcrumbs also help with orientation on inner pages (recipe detail, category, tag).

## Goals / Non-Goals

**Goals:**
- All top-level destinations reachable from any page via the header
- Inner pages show a contextual breadcrumb trail
- Weekplanner link present now, even though the page doesn't exist yet

**Non-Goals:**
- Mobile hamburger menu (3 links fit comfortably inline)
- Active/highlighted nav state (low value on a simple site)
- Breadcrumb structured data (schema.org BreadcrumbList) — not needed for a private site

## Decisions

### Breadcrumbs as a Base.astro prop

**Decision:** `Base.astro` accepts an optional `breadcrumbs?: Array<{label: string; href?: string}>` prop. When present, it renders a `<nav class="breadcrumb">` between the header and main content. The last item (current page) has no `href`.

**Rationale:** Each page knows its own position in the hierarchy — category page knows `category`, recipe page knows `category` and `title`. Passing this data as a prop is explicit and type-safe. Auto-detecting from the URL is fragile (especially for the recipe `[...slug]` route which could be any depth).

**Alternative considered:** A separate `Breadcrumb.astro` component. Unnecessary — the markup is 5 lines and Base.astro already handles per-page customisation via props.

---

### Weekplanner as a dead link

**Decision:** Link to `${base}/planner/` in the header even though the page doesn't exist yet. Clicking it will 404 until the planner is built.

**Rationale:** The user explicitly wants all three nav items now. A 404 on a personal site is acceptable for a short period. Avoids a "disabled" link state that would need to be remembered and removed later.

---

### Header layout: title left, nav links right

**Decision:** `display: flex; justify-content: space-between` — site title on the left, nav links on the right.

**Rationale:** Standard pattern, minimal CSS, works at all viewport widths with 3 short labels. No hamburger needed.

## Risks / Trade-offs

- **Weekplanner 404** → Acceptable for a personal site; will be resolved when the planner is built.
- **Breadcrumb on recipe pages requires category extraction** → Already done via `recipe.id.split('/')[0]`; consistent with existing RecipeCard logic.
- **Back-link removal** → Category/tag/kids pages currently have a `← Alle recepten` back-link. Breadcrumbs provide equivalent (and richer) navigation so removal is safe.
