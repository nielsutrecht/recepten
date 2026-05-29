## Why

Planning dinners for the week is currently done mentally or on paper. With 13+ recipes and ingredient categories already in the schema, the site has everything needed to generate a shopping list automatically — this feature makes the cookbook actively useful for weekly meal prep.

## What Changes

- Add a `/planner/` page with a Mon–Sun week grid where each day can have one recipe assigned with a custom serving count
- Add an HTML5 `<dialog>` recipe picker (search + card grid) for selecting recipes per day
- Add a shopping list below the grid: ingredients grouped by category, quantities scaled and summed across recipes, with checkboxes
- All state (plan + checked items) persists in `localStorage`; a "Plan wissen" button resets the plan

## Capabilities

### New Capabilities

- `week-planner-grid`: Mon–Sun grid with assignable recipe slots and per-slot serving scaler
- `recipe-picker-dialog`: HTML5 dialog with search and card grid for selecting a recipe
- `shopping-list`: Ingredient list derived from the plan, grouped by category, with persistent checkboxes

### Modified Capabilities

## Impact

- `src/pages/planner.astro` — new file; all recipe data serialised at build time via `define:vars`
- No schema changes, no new dependencies
- The "Weekplanner" nav link in the header already points to `/planner/`
