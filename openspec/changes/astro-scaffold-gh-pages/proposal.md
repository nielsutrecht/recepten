## Why

The recipe site exists only as a PRD and CLAUDE.md — there is no runnable Astro project yet. This change creates the full project foundation so development can begin and the site can be seen live on GitHub Pages from day one.

## What Changes

- Initialize the Astro project (package.json, astro.config.mjs, tsconfig.json)
- Add GitHub Actions workflow that builds and deploys to GitHub Pages on push to `main`
- Define the Zod content schema for recipes (all PRD frontmatter fields)
- Create a base layout, home page, and recipe detail page
- Add one sample recipe (tomatensoep) to verify end-to-end rendering

## Capabilities

### New Capabilities

- `project-config`: Astro project configuration — package.json, astro.config.mjs with `base: '/recepten'`, tsconfig
- `deploy-pipeline`: GitHub Actions workflow for building and deploying to GitHub Pages
- `recipe-schema`: Zod content collection schema validating all recipe frontmatter fields
- `recipe-detail`: Individual recipe page rendering title, metadata, ingredients, and method body
- `recipe-listing`: Home page listing all non-draft recipes with title and basic metadata

### Modified Capabilities

## Impact

- Creates the entire `src/` directory structure and all root config files
- Adds `.github/workflows/deploy.yml`
- Requires one manual step in GitHub repo settings: set Pages source to **GitHub Actions**
- No existing code is modified (greenfield)
