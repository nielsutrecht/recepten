# Recepten

Personal recipe site for Niels. Static site built with Astro, deployed to GitHub Pages.

**URL:** https://nielsutrecht.github.io/recepten

## Development

```bash
npm run dev      # local dev server at localhost:4321/recepten/
npm run build    # build to dist/
npm run preview  # preview built output
```

Push to `main` triggers GitHub Actions → builds → deploys to GitHub Pages.

## Adding recipes

Recipes live in `src/content/recipes/<category>/slug.md`. Use the `/import` skill in Claude Code to import a recipe from a URL directly into the project.

Manually created recipes follow the same frontmatter schema defined in `src/content.config.ts`.

## Scripts

### `scripts/parse_cookbook.py`

Parses a PDF cookbook (converted to text via `pdftotext`) into individual recipe markdown files in `input/`.

**Step 1** — convert the PDF to text:

```bash
pdftotext ~/Downloads/cookbook.pdf ~/Downloads/cookbook.txt
```

**Step 2** — run the parser:

```bash
python3 scripts/parse_cookbook.py ~/Downloads/cookbook.txt
# output goes to input/ by default

# or specify a custom output directory:
python3 scripts/parse_cookbook.py ~/Downloads/cookbook.txt ~/Downloads/my-recipes/
```

Each output file contains the recipe title, nutrition info (calories/protein/carbs/fat), section (breakfast/lunch/dinner/snack), ingredients, notes, and instructions. These files can then be reviewed and imported individually using the `/import` skill.

The script was written for "The Ultimate High Protein Chef Cookbook" by Panacea Palm but should work for any PDF cookbook that uses a similar `pdftotext` output structure.
