## Why

Three small quality-of-life improvements that lay groundwork for the upcoming week planner: ingredient categories enable shopping list grouping, the print stylesheet makes recipes usable on paper, and the kids page surfaces approved recipes instantly.

## What Changes

- Add optional `category` field to ingredient schema (9-value enum); update all 13 existing recipes with correct categories; update `/import` command with a lookup table for common Dutch ingredient names
- Add `@media print` stylesheet to `Base.astro` that produces a clean single-column printout of recipe pages
- Add static `/kids/` page listing recipes where at least one kid is rated and neither has given 😒 or 🤢

## Capabilities

### New Capabilities

- `ingredient-category-schema`: Zod schema extended with optional `category` enum on each ingredient object
- `print-stylesheet`: CSS print rules producing a clean recipe printout
- `kids-page`: Static `/kids/` page filtered to kid-approved recipes

### Modified Capabilities

- `recipe-schema`: Ingredient objects gain an optional `category` field — existing recipes without it remain valid (defaults to `"overig"` at runtime)

## Impact

- `src/content.config.ts` — adds `category` to ingredient schema
- All 13 recipe `.md` files — add `category` to each ingredient
- `src/layouts/Base.astro` — add `@media print` block
- `src/pages/kids.astro` — new file
- `.claude/commands/import.md` — add category lookup table
- No breaking changes: `category` is optional; existing recipes without it build cleanly
