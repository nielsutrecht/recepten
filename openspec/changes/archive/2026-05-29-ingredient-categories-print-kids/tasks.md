## 1. Ingredient Category Schema

- [x] 1.1 Add `ingredientCategory` enum to `src/content.config.ts` with 9 values: `groente en fruit`, `vlees en vis`, `zuivel en eieren`, `kaas`, `pasta en granen`, `sauzen en kruiden`, `conserven`, `bakken`, `overig`
- [x] 1.2 Add optional `category: ingredientCategory` field to the ingredient object schema

## 2. Categorize Existing Recipes

- [x] 2.1 Add `category` to every ingredient in `bijgerechten/carolina-barbecue-rub.md`
- [x] 2.2 Add `category` to every ingredient in `bijgerechten/coleslaw.md`
- [x] 2.3 Add `category` to every ingredient in `bijgerechten/frambozencoulis.md`
- [x] 2.4 Add `category` to every ingredient in `bijgerechten/hoe-maak-je-barbecuesaus.md`
- [x] 2.5 Add `category` to every ingredient in `bijgerechten/perfecte-aardappelpuree.md`
- [x] 2.6 Add `category` to every ingredient in `nagerechten/chocolademousse-zonder-ei.md`
- [x] 2.7 Add `category` to every ingredient in `nagerechten/panna-cotta-classica.md`
- [x] 2.8 Add `category` to every ingredient in `nagerechten/tiramisu-met-likeur.md`
- [x] 2.9 Add `category` to every ingredient in `pasta/lasagne-met-kipgehakt-spinazie-en-courgette.md`
- [x] 2.10 Add `category` to every ingredient in `pasta/pasta-all-amatriciana.md`
- [x] 2.11 Add `category` to every ingredient in `soepen/tomatensoep.md`
- [x] 2.12 Add `category` to every ingredient in `vlees/kruidige-gehakttaart.md`

## 3. Update /import Command

- [x] 3.1 Add a category lookup table to `.claude/commands/import.md` mapping common Dutch ingredient name substrings to their category (e.g. `"knoflook"` → `"groente en fruit"`, `"melk"` → `"zuivel en eieren"`)
- [x] 3.2 Update the ingredient parsing step to auto-assign `category` from the lookup table, defaulting to `"overig"`

## 4. Print Stylesheet

- [x] 4.1 Add `@media print` block to `src/layouts/Base.astro` hiding: `header`, `.filter-bar`, `.servings-scaler button`, `.back-link`, `.no-results`, `#tag-chips`
- [x] 4.2 Add print rules for single-column layout, no box-shadows, no card borders, readable font size

## 5. Kids Page

- [x] 5.1 Create `src/pages/kids.astro` — filter recipes to those with ≥1 rating and no 😒/🤢 rating from either kid; sort by pubDate desc
- [x] 5.2 Render heading ("Voor de kids"), recipe count, and card grid using `RecipeCard.astro`

## 6. Verify

- [x] 6.1 Run `npm run build` — confirm clean build with no schema errors
- [x] 6.2 Check that `/kids/` page renders (should show tomatensoep)
- [x] 6.3 Open a recipe page and use browser print preview — confirm nav/scaler hidden, ingredients and steps visible
