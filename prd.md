# PRD: Recepten — Personal Recipe Site

## Context

A private recipe site to store and browse family cooking recipes. Feels like a personal digital cookbook: clean, fast, easy to add to, and practical to use while actually cooking (serving scaler, readable on a phone). Mirrors the Astro-based blog at `../blog` in tech stack but gets a fresh visual design and recipe-specific features.

## Project Identity

| Property | Value |
|----------|-------|
| Repo | `nielsutrecht/recepten` (private) |
| URL | `https://nielsutrecht.github.io/recepten` |
| Language (code) | English |
| Language (content) | Dutch |
| Deployment | GitHub Actions → GitHub Pages |

> Note: GitHub Pages from a private repo is still publicly accessible by URL — the repo source is hidden, the published site is not. This is acceptable.

---

## Tech Stack

- **Astro** (latest) — static site generator
- **TypeScript + Zod** — content schema validation
- **Markdown** — recipe bodies; structured ingredient data in YAML frontmatter
- **`@astrojs/sitemap`** — auto-generated sitemap
- **No CSS framework** — custom CSS, clean & minimal aesthetic
- **Vanilla JS** — serving scaler, search filter, week planner (no build-time JS framework)

Astro config sets `base: '/recepten'` for correct GitHub Pages subpath routing.

---

## Content Structure

### Directory layout

```
src/content/recipes/
  soepen/
  pasta/
  vlees/
  vis/
  groente/
  bijgerechten/
  nagerechten/
  ontbijt/
```

Category directories are the primary axis. Tags handle cross-cutting concerns (`snel`, `vegetarisch`, `kindvriendelijk`, etc.).

### Frontmatter schema

```yaml
---
title: "Tomatensoep"
pubDate: 2026-05-29           # ISO date — used for "recently added" sorting
servings: 4                   # default serving count for the scaler
prepTime: 15                  # minutes
cookTime: 30                  # minutes (optional)
tags: ["soep", "vegetarisch", "snel"]
source: "https://..."         # optional — URL only; omit for own recipes
ratings:
  emma: "😍"
  annemijn: "😐"
draft: false
ingredients:
  - { quantity: 500, unit: "g", name: "tomaten", category: "groente en fruit" }
  - { quantity: 1, unit: "el", name: "olijfolie", category: "sauzen en kruiden" }
  - { quantity: 2, unit: "teentjes", name: "knoflook", category: "groente en fruit" }
  - { quantity: 0.5, unit: "tl", name: "zout", category: "sauzen en kruiden" }
---
```

**Rating emoji palette:** 😍 geliefd · 😊 lekker · 😐 oké · 😒 niet zo lekker · 🤢 vies

**All quantities are metric** (g, ml, el, tl, dl, kg, l, etc.). **All tags lowercase.**

**Ingredient categories** (used for shopping list grouping):
`groente en fruit` · `vlees en vis` · `zuivel en eieren` · `kaas` · `pasta en granen` · `sauzen en kruiden` · `conserven` · `bakken` · `overig`

`category` is optional on each ingredient — defaults to `"overig"` if omitted.

### Recipe body convention

- `## Bereiding` heading introduces the method steps (free Markdown)
- Ingredients live entirely in frontmatter (enables client-side scaling)
- Optional `## Notities` heading for tips/variations

---

## Pages & Routes

| Route | Description |
|-------|-------------|
| `/` | Home: search bar + tag filter chips; all recipe cards, filtered client-side |
| `/recepten/[...slug]/` | Individual recipe page |
| `/categorie/[category]/` | All recipes in a category |
| `/tag/[tag]/` | All recipes with a tag |
| `/kids/` | Recipes approved by both kids (neither rated 😒 or 🤢) |
| `/planner/` | Week planner + shopping list |

---

## Key Features

### 1. Serving Scaler

On each recipe page, a `+` / `−` control adjusts the serving count. Ingredient quantities recompute proportionally in real time. Ingredients rendered with `data-quantity` attributes; small inline `<script>` rewrites displayed values. No external JS library.

### 2. Per-Kid Ratings

Displayed as a small panel on the recipe page:

```
Emma      😍
Annemijn  😐
```

Rendered from frontmatter; no interaction required.

### 3. Client-Side Search & Filter

Home page:
- Text input filters recipe cards by title (substring match)
- Tag chips toggle on/off (derived from all tags at build time)
- Cards update without page reload — all data serialised into the page at build time

### 4. Recipe Cards

Each card shows: title (links to recipe), category (links to category page), prep+cook time, tag pills (link to tag pages), kids ratings.

### 5. Kids-Approved Page

`/kids/` — a dedicated page listing recipes where neither Emma nor Annemijn has given a 😒 or 🤢 rating, and at least one kid has rated the recipe. Same card grid as home page. Recipes not yet tried by the kids are excluded.

### 6. Print Stylesheet

A `@media print` CSS block that hides navigation, search, filter chips, and serving scaler buttons. Renders a clean single-column layout with the ingredient list and preparation steps readable on paper.

### 7. Week Planner

`/planner/` — a client-side week planner (Mon–Sun) stored in `localStorage`. Each day can have one recipe assigned with a custom serving count (default 4). State persists between visits.

```
Maandag    Lasagne          ×4  [wis]
Dinsdag    —                    [+ kies]
Woensdag   Tomatensoep      ×6  [wis]
...
```

Clicking `[+ kies]` opens a recipe picker with the same search/filter as the home page.

### 8. Shopping List

Derived from the week planner. Generated on demand from all planned recipes and their serving-scaled ingredient quantities.

- Ingredients grouped by category (see schema)
- Items with identical name + unit across multiple recipes are combined (quantities summed)
- Each item shows which recipe(s) it comes from
- Checkboxes to tick off items while shopping — checked state persists in `localStorage`

```
Groente en fruit
☐ 400g verse spinazie     (Lasagne)
☐ 2 rode uien             (Lasagne, Amatriciana)

Pasta en granen
☐ 250g lasagnebladen      (Lasagne)
☐ 300g spaghetti          (Amatriciana)
```

---

## Design

**Aesthetic:** Clean & minimal — lots of white space, clear typography, content-first.

**Palette:** Warm off-white background (`#faf9f7`), dark text, single accent color (terracotta `#b85c38`).

**Typography:** System font stack. No jQuery, no Bootstrap.

**Mobile:** Recipe pages comfortable on a phone on the kitchen counter — base font ≥17px, generous line-height, serving scaler buttons large enough to tap.

---

## GitHub Actions Workflow

`.github/workflows/deploy.yml` — triggers on push to `main`, builds with `npm run build`, deploys `dist/` via `actions/deploy-pages`. GitHub Pages source set to **GitHub Actions** in repo settings.

---

## Out of Scope

- Comments or visitor ratings
- Hero images per recipe
- RSS feed
- User accounts / auth
- Multi-user / shared planners
