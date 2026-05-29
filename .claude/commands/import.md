# Import Recipe

Import a recipe from any website into the project.

**Usage:** `/import-ah-recipe <url>`

## Steps

### 1. Fetch the page

```bash
curl -s "<url>" \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Accept: text/html" \
  --compressed
```

### 2. Extract recipe data — try in order

**A) JSON-LD (preferred)** — extract `<script type="application/ld+json">` blocks whose `"@type"` is `"Recipe"`. Most major recipe sites (AH Allerhande, etc.) include this. Parse with Python:

```python
import re, json
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL):
    try:
        d = json.loads(m)
        if d.get('@type') == 'Recipe': # found it
    except: pass
```

From JSON-LD extract:
- `name` → title
- `recipeYield` → servings (integer)
- `totalTime` / `prepTime` / `cookTime` (ISO 8601, e.g. `PT30M` = 30 min)
- `recipeIngredient` → ingredient strings
- `recipeInstructions` → step texts
- `keywords` / `recipeCategory` / `recipeCuisine` → tags

**B) Microdata** — if no JSON-LD, look for `itemtype="https://schema.org/Recipe"` in the HTML and extract `itemprop` values for the same fields.

**C) WordPress Recipe Maker (WPRM)** — very common on food blogs. Look for `wprm-recipe` class names:
- `.wprm-recipe-ingredient` elements → ingredients
- `.wprm-recipe-instruction-text` elements → steps
- `.wprm-recipe-servings` → servings
- `.wprm-recipe-prep-time`, `.wprm-recipe-cook-time` → times

**D) HTML heuristic** — last resort. Strip HTML tags and extract:
- Find the ingredient block: look for a list near the word "Ingrediënten" / "Ingredients"
- Find the preparation block: look for content near "Bereiding" / "Instructies" / "Directions"
- Extract step-by-step text from `<ol>`, `<li>`, or `<p>` tags in that region

If any method finds partial data, use it and apply judgment for missing fields.

### 3. Parse ingredient strings into structured objects

Each ingredient string → `{ quantity, unit, name }`:
- First token(s) = quantity (number; convert fractions: `½`→`0.5`, `¼`→`0.25`, `¾`→`0.75`)
- Next token = unit (`g`, `ml`, `el`, `tl`, `kg`, `l`, `stuks`, `teentjes`, `plakjes`, `blaadjes`, `eetlepels`→`el`, `theelepels`→`tl`, etc.)
- If no recognisable unit follows the quantity, use `"stuks"`
- Remainder = name

### 4. Determine timing

- If `prepTime` and `cookTime` are separate → use directly
- If only `totalTime` → use judgment based on the steps: assign `cookTime` to the longest oven/stovetop step, minimum `prepTime: 5`
- If time is mostly passive (chilling, marinating, rising) → count only active time; omit `cookTime` if there's no real heat step

### 5. Determine the category directory

Map to existing categories in `src/content/recipes/`:
- `pasta`, `soepen`, `vlees`, `vis`, `groente`, `bijgerechten`, `nagerechten`, `ontbijt`

If unclear, ask the user.

### 6. Derive the slug

Use the last path segment of the URL (strip query strings and trailing slashes). Drop marketing suffixes like `-advertorial`, `-sponsored`.

### 7. Create the file

`src/content/recipes/<category>/<slug>.md`:

```markdown
---
title: "<title>"
pubDate: <today's date as YYYY-MM-DD>
servings: <number>
prepTime: <number>
cookTime: <number>        # omit if no active cooking
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

Leave out `ratings` — filled in after the family tries it.

### 8. Verify and report

Run `npm run build` to confirm the schema validates cleanly.

Report:
- File path created
- Extraction method used (JSON-LD / microdata / WPRM / HTML heuristic)
- Any judgment calls (time split, missing units, inferred fields)
- Anything that couldn't be extracted and was left out or guessed
