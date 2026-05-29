## Context

Greenfield Astro project. The blog at `../blog` uses the same stack (Astro, TypeScript strict, content collections with glob loader) and serves as the reference implementation. The key difference: this site lives at a subpath (`/recepten`) on GitHub Pages, while the blog runs at a root domain. Subpath routing is Astro's `base` config option and requires care throughout.

## Goals / Non-Goals

**Goals:**
- Runnable `npm run dev` with hot reload
- `npm run build` produces a deployable `dist/`
- GitHub Actions deploys `dist/` to GitHub Pages on push to `main`
- Recipe content schema is defined and enforced at build time
- One sample recipe renders correctly end-to-end

**Non-Goals:**
- Visual design / styling (placeholder CSS only)
- Search, filtering, serving scaler (future changes)
- Category and tag index pages (future changes)
- RSS feed, print stylesheet, images

## Decisions

### Astro `base` config and internal links

**Decision:** Set `base: '/recepten'` in `astro.config.mjs`. Use `import.meta.env.BASE_URL` for all internal hrefs.

**Rationale:** Without `base`, all asset paths and links break under the `/recepten` subpath on GitHub Pages. Astro handles static asset paths automatically once `base` is set; only authored `<a href>` values need the prefix.

**Alternative considered:** Relative links. Rejected — fragile across different nesting depths.

---

### Content collection loader

**Decision:** Use Astro's `glob` loader (same pattern as `../blog`).

**Rationale:** `glob({ pattern: '**/*.md', base: './src/content/recipes' })` gives slugs of the form `<category>/<name>`, which maps naturally to the `/recepten/<category>/<name>` URL structure. No custom loader needed.

---

### Slug → URL mapping

**Decision:** Route file is `src/pages/recepten/[...slug].astro`. Slug from glob includes the category prefix (e.g., `soepen/tomatensoep`), so the full URL is `/recepten/soepen/tomatensoep`.

**Rationale:** Keeps category in the URL (good for SEO and navigation) without a separate `[category]` segment. The `...slug` spread handles arbitrary nesting.

---

### GitHub Actions deploy pattern

**Decision:** Two-job workflow: `build` (produces artifact) → `deploy` (uploads to Pages). Uses official actions: `actions/upload-pages-artifact@v3` + `actions/deploy-pages@v4`.

**Rationale:** This is Astro's documented GH Pages recipe. The two-job split allows the deploy job to run with minimal permissions (only `pages: write` + `id-token: write`).

**Prerequisite:** Repo → Settings → Pages → Source must be set to **GitHub Actions** (one-time manual step).

---

### Recipe Zod schema

**Decision:** Define `ratings` as a partial object (`z.object({ emma, annemijn }).partial().optional()`) and rating values as `z.enum(['😍','😊','😐','😒','🤢'])`.

**Rationale:** Not all recipes have been tried by both kids. Partial + optional allows zero, one, or two ratings without schema errors.

**Decision:** `ingredients` as `z.array(z.object({ quantity: z.number(), unit: z.string(), name: z.string() }))` — flat array, no nesting.

**Rationale:** Matches the PRD schema exactly. Flat array is easy to iterate in templates and easy to manipulate for the future serving scaler.

## Risks / Trade-offs

- **`base` path forgetting** → Any new page or link that omits `BASE_URL` will silently 404 on Pages but work locally. Mitigated by using a `Base.astro` layout that handles the `<base>` tag and by documenting the pattern.
- **`latest` version pinning** → `package.json` uses `"astro": "latest"` (matching blog). A breaking Astro release could break the build without a version bump. Acceptable for a personal project; easy to fix when it happens.
- **Manual Pages setting** → The deploy will silently do nothing until the repo Settings → Pages → Source is flipped to GitHub Actions. Documented in proposal and tasks.
