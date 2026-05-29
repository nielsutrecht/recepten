# Recepten

Personal recipe site for Niels. Static site built with Astro, deployed to GitHub Pages via GitHub Actions.

- **Repo:** `nielsutrecht/recepten` (private)
- **URL:** `https://nielsutrecht.github.io/recepten`
- **PRD:** `prd.md`
- **Reference:** similar stack at `../blog`

## Code conventions

- Code and identifiers in **English**; all site content in **Dutch**
- TypeScript strict mode; Zod for all content schema validation
- No CSS frameworks — custom CSS only
- No JS frameworks — vanilla JS for client-side interactions (serving scaler, search filter)

## Content

Recipes live in `src/content/recipes/<category>/slug.md`.

Each recipe must have all required frontmatter fields as defined in `src/content.config.ts`:
- `title`, `pubDate`, `servings`, `prepTime` (required)
- `cookTime`, `tags`, `source`, `ratings`, `draft` (optional)
- `ingredients` array: `{ quantity: number, unit: string, name: string }[]`

All quantities **metric**. Recipe body uses `## Bereiding` for method steps.

Kids rating emojis: 😍 😊 😐 😒 🤢 (for Emma and Annemijn).

### Recipe import rules

When importing recipes from external sources:

- **Strip all commentary** — ingredient names must be clean (e.g. `"ui, fijngesnipperd"` not `"ui, fijngesnipperd, want anders..."`); steps must contain only the action, not tips, explanations, or caveats
- **Steps in Dutch** — translate if the source is in another language; write in plain instructional Dutch
- **Clear and concise steps** — one action per step; move tips and variations to a `## Notities` section if worth keeping, otherwise discard them
- **`source` must be a URL** — omit `source` entirely for own recipes

## Commands

```bash
npm run dev      # local dev server at localhost:4321/recepten/
npm run build    # build to dist/
npm run preview  # preview built output
```

## Deployment

Push to `main` triggers GitHub Actions → builds → deploys to GitHub Pages. Workflow at `.github/workflows/deploy.yml`.

Astro config uses `base: '/recepten'` — all internal links must use Astro's `<a href={base + '/path'}>` or the `BASE_URL` variable.
