## Context

The site is fully static (Astro + GitHub Pages). The planner needs to be interactive and persistent without a backend. All recipe data is available at build time. `localStorage` provides persistence. The ingredient `category` field is already in the schema and populated on all 13 recipes.

## Goals / Non-Goals

**Goals:**
- Mon–Sun plan with one recipe per day, adjustable serving count
- Recipe picker via `<dialog>` with search
- Shopping list always visible, grouped by category, checkboxes persist
- Plan persists across page reloads; clears with a button

**Non-Goals:**
- Week navigation (previous/next week) — one persistent plan for now
- Multiple recipes per day
- Fuzzy ingredient name matching for combining
- Sharing or exporting the list

## Decisions

### Recipe data via `define:vars`

**Decision:** Serialise all non-draft recipes into the page at build time using Astro's `define:vars` directive. The client script receives a typed `recipeData` array containing id, title, servings, prepTime, cookTime, tags, and ingredients (with category).

**Rationale:** The site has no API. `define:vars` is Astro's canonical way to pass build-time data to client scripts. At 13 recipes the payload is small (~10KB unminified). Avoids a separate fetch or hydration framework.

**Alternative considered:** JSON in a `<script type="application/json">` tag. `define:vars` is cleaner and type-checked.

---

### HTML5 `<dialog>` for recipe picker

**Decision:** A single `<dialog id="recipe-picker">` element on the page, opened with `dialog.showModal()` and closed with `dialog.close()` or clicking outside the dialog.

**Rationale:** Native, accessible, no library. `showModal()` adds a backdrop and traps focus automatically. Supported in all modern browsers. Simpler than a custom overlay.

---

### State shape in localStorage

```json
{
  "days": {
    "ma": { "recipeId": "pasta/pasta-all-amatriciana", "servings": 4 },
    "di": null,
    "wo": null,
    "do": null,
    "vr": null,
    "za": null,
    "zo": null
  },
  "checkedItems": ["spaghetti:g", "guanciale blokjes:g"]
}
```

Key: `recepten-planner-v1`. State saved on every interaction.

---

### Shopping list: strict name+unit matching for combining

**Decision:** Sum quantities only when `name` AND `unit` are identical strings. Display separate lines otherwise.

**Rationale:** Fuzzy matching ("knoflook" vs "knoflook, fijngehakt") is error-prone and could combine items that shouldn't be combined. Strict matching is always correct — the worst case is two separate lines for the same ingredient, which is still useful. The user can mentally combine them.

---

### Quantity display in shopping list

**Decision:** Apply the same `roundKitchen()` rounding logic used by the serving scaler (magnitude-based, fractions for < 1).

**Rationale:** Consistency. A shopping list showing `166.7g` is as confusing as a recipe showing it. Reuse the same algorithm.

---

### Category ordering for shopping list

Supermarket-inspired order (fresh first, dry goods last):

1. groente en fruit
2. vlees en vis
3. zuivel en eieren
4. kaas
5. pasta en granen
6. conserven
7. sauzen en kruiden
8. bakken
9. overig

## Risks / Trade-offs

- **localStorage unavailable** (private browsing, blocked) → State resets on each load. Mitigated by a graceful try/catch; the planner still works, just doesn't persist.
- **`define:vars` payload size** → At current scale ~10KB. At 100 recipes, ~80KB. Acceptable for a long time; revisit if needed.
- **Strict name matching misses synonyms** → Two lines instead of one is the failure mode. Acceptable and obvious to the user.
