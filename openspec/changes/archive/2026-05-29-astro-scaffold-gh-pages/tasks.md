## 1. Project Foundation

- [x] 1.1 Create `package.json` with astro, @astrojs/sitemap dependencies and dev/build/preview scripts
- [x] 1.2 Create `astro.config.mjs` with `site`, `base: '/recepten'`, and sitemap integration
- [x] 1.3 Create `tsconfig.json` extending `astro/tsconfigs/strict` with `strictNullChecks: true`
- [x] 1.4 Create `.gitignore` (node_modules, dist, .astro)
- [x] 1.5 Run `npm install` to generate `package-lock.json`

## 2. GitHub Actions Deploy Workflow

- [x] 2.1 Create `.github/workflows/deploy.yml` with build job (checkout, setup-node@v4 with Node 20 + npm cache, npm ci, npm run build, upload-pages-artifact)
- [x] 2.2 Add deploy job (depends on build, uses deploy-pages@v4, environment: github-pages)
- [x] 2.3 Set workflow permissions: `contents: read` on build, `pages: write` + `id-token: write` on deploy
- [x] 2.4 Add concurrency group `"pages"` with `cancel-in-progress: false`

## 3. Content Schema

- [x] 3.1 Create `src/content.config.ts` with `recipes` collection using glob loader at `./src/content/recipes`
- [x] 3.2 Define Zod schema: required fields (`title`, `pubDate`, `servings`, `prepTime`, `ingredients`)
- [x] 3.3 Add optional fields to schema (`cookTime`, `tags`, `source`, `ratings`, `draft`) with correct defaults
- [x] 3.4 Define `ratingEmoji` enum and `ratings` as a partial optional object

## 4. Base Layout and Pages

- [x] 4.1 Create `src/layouts/Base.astro` with `<html>`, `<head>` (charset, viewport, title slot), `<body>` with `<slot>`; use `import.meta.env.BASE_URL` for any internal links
- [x] 4.2 Create `src/pages/index.astro` — query all non-draft recipes sorted by pubDate desc, render a list with title link and total time
- [x] 4.3 Create `src/pages/recepten/[...slug].astro` — `getStaticPaths` from non-draft recipes; render title, metadata, ingredients list (with `data-quantity` attributes), and Markdown body

## 5. Sample Recipe

- [x] 5.1 Create `src/content/recipes/soepen/` directory
- [x] 5.2 Create `src/content/recipes/soepen/tomatensoep.md` with valid frontmatter (title, pubDate, servings, prepTime, cookTime, tags, ratings for Emma and Annemijn, ingredients) and a short `## Bereiding` section

## 6. Verify End-to-End

- [x] 6.1 Run `npm run dev` and confirm the home page loads at `localhost:4321/recepten/` showing tomatensoep
- [x] 6.2 Click through to the recipe detail page and confirm all metadata, ingredients, and body render correctly
- [x] 6.3 Run `npm run build` and confirm it exits cleanly with no type or schema errors
- [x] 6.4 Push to `main`, then in GitHub repo Settings → Pages → set Source to **GitHub Actions**, and confirm the Actions workflow completes and the site is live at `https://nielsutrecht.github.io/recepten/`
