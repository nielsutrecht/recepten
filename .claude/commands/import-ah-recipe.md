# Import AH Allerhande Recipe

Import a recipe from ah.nl/allerhande into the project.

**Usage:** `/import-ah-recipe <url>`

## Steps

1. **Fetch the recipe data** using curl with a browser User-Agent (AH blocks headless requests but allows curl with a real UA):

```bash
curl -s "<url>" \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept: text/html" \
  --compressed
```

Then extract the `<script type="application/ld+json">` block whose `"@type"` is `"Recipe"` — it contains all structured recipe data.

2. **Parse the JSON-LD** to extract:
   - `name` → `title`
   - `recipeYield` → `servings` (integer)
   - `totalTime` (ISO 8601 duration like `PT30M`) → split into `prepTime` and `cookTime`. If only `totalTime` is given, use judgment: set `cookTime` to the majority of the time and `prepTime` to the remainder (minimum 5 min prep). If `prepTime`/`cookTime` are separate fields, use them directly.
   - `recipeIngredient` → `ingredients` array. Parse each string into `{ quantity, unit, name }`:
     - First token(s) = quantity (number, may include fractions like `½` → `0.5`)
     - Next token = unit (g, ml, el, tl, stuks, teentjes, etc.) — if none, use `"stuks"`
     - Remainder = name
   - `recipeInstructions` → ordered step texts for the `## Bereiding` section
   - `keywords` or `recipeCategory`/`recipeCuisine` → suggest tags (keep 2–4, lowercase Dutch)
   - `url` → `source`

3. **Determine the category directory** from the recipe type. Map to existing categories in `src/content/recipes/`:
   - pasta, soepen, vlees, vis, groente, bijgerechten, nagerechten, ontbijt
   - If unclear, ask the user which category to use.

4. **Derive the slug** from the AH URL path (the last segment, e.g. `pasta-all-amatriciana`).

5. **Create the file** at `src/content/recipes/<category>/<slug>.md` using this exact frontmatter format:

```markdown
---
title: "<title>"
pubDate: <today's date as YYYY-MM-DD>
servings: <number>
prepTime: <number>
cookTime: <number>        # omit if 0
tags: [<tag1>, <tag2>]
source: "<url>"
draft: false
ingredients:
  - { quantity: <n>, unit: "<unit>", name: "<name>" }
---

## Bereiding

1. <step 1>

2. <step 2>
...
```

   Leave out `ratings` — those get filled in after the family tries it.

6. **Run `npm run build`** to confirm the schema validates cleanly.

7. **Report** the created file path and a summary of what was imported. Note anything that needed a judgment call (e.g. time split, missing unit).
