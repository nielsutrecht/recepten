## Context

Three independent small features with no interdependencies. Ingredient categories are the most structurally significant because they touch the Zod schema and all 13 recipe files. Print and kids page are purely additive.

## Goals / Non-Goals

**Goals:**
- Ingredient `category` field available at build time for the shopping list (upcoming planner change)
- All 13 existing recipes categorized on day one so the shopping list is immediately useful
- Clean single-column printout of recipe pages with no UI chrome
- `/kids/` page showing rated-and-approved recipes

**Non-Goals:**
- Shopping list or week planner UI (separate change)
- Automatically syncing ingredient categories across recipe files on import (lookup table assists, human reviews)
- Per-category page counts or navigation

## Decisions

### Category as `z.string().optional()` vs `z.enum([...]).optional()`

**Decision:** `z.enum([...]).optional()` with the 9 defined values.

**Rationale:** Enum catches typos at build time — `"groente & fruit"` vs `"groente en fruit"` would silently pass with a string. The category list is small and stable. If a new category is ever needed, updating the Zod enum is a one-line change.

**Alternative considered:** `z.string().optional()` — more flexible but loses build-time safety.

---

### Recipe migration: all at once vs gradual

**Decision:** Categorize all 13 existing recipes in this change.

**Rationale:** With only 13 recipes the effort is small (~90 ingredients). If categories are left as `"overig"` until recipes are individually updated, the shopping list would be useless on first use. Front-loading the work pays off immediately.

---

### Kids approval rule

**Decision:** A recipe appears on `/kids/` if it has ≥1 rating AND no rating is 😒 or 🤢.

**Rationale:** Requiring both kids to have rated would exclude many good recipes Emma has tried but Annemijn hasn't yet (and vice versa). The rule "no rejections + at least tried by someone" is more permissive and fills the page faster as ratings accumulate.

---

### Print stylesheet: `Base.astro` vs separate file

**Decision:** `@media print` block inside `Base.astro`'s `<style>` tag.

**Rationale:** A single source of truth. All pages share `Base.astro`; any recipe page printed will get the same treatment. No separate file needed.

**What to hide:** `header`, `.filter-bar`, `.tag-chips`, `.servings-scaler button`, `.back-link`, `.card-ratings` on cards (irrelevant when printing a listing), `.no-results`.

**What to keep:** Title, metadata row, ingredient list, bereiding steps, kid ratings on recipe pages, notities.

## Risks / Trade-offs

- **New enum value needed later** → one-line Zod change + rebuild. Low risk.
- **Manual category assignment errors** → caught at build time if wrong enum value; wrong but valid assignments (e.g. sugar labelled as `"overig"`) only matter when shopping list is built. Acceptable.
- **Print styles need maintenance** → as new page types are added, print CSS may need updating. Low burden given site simplicity.
