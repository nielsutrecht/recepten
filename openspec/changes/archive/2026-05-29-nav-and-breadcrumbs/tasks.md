## 1. Header Navigation

- [x] 1.1 Add `breadcrumbs` prop to `Base.astro` interface: `Array<{label: string; href?: string}>`, optional
- [x] 1.2 Add nav links to header in `Base.astro`: "Voor de kids" → `${base}/kids/` and "Weekplanner" → `${base}/planner/`; style with flex layout (title left, nav right)
- [x] 1.3 Render breadcrumb trail in `Base.astro` between header and `<main>` when `breadcrumbs` prop is provided; separator `›`; last item plain text, others `<a>` links
- [x] 1.4 Add breadcrumb and nav CSS to `Base.astro`

## 2. Wire Breadcrumbs on Pages

- [x] 2.1 `src/pages/[...slug].astro` — pass `breadcrumbs={[{label:"Recepten",href:base},{label:category,href:`${base}/categorie/${category}/`},{label:data.title}]}`
- [x] 2.2 `src/pages/categorie/[category].astro` — pass `breadcrumbs={[{label:"Recepten",href:base},{label:category}]}`; remove `<a class="back-link">` element and its CSS
- [x] 2.3 `src/pages/tag/[tag].astro` — pass `breadcrumbs={[{label:"Recepten",href:base},{label:tag}]}`; remove `<a class="back-link">` element and its CSS
- [x] 2.4 `src/pages/kids.astro` — pass `breadcrumbs={[{label:"Recepten",href:base},{label:"voor de kids"}]}`; remove `<a class="back-link">` element and its CSS

## 3. Verify

- [x] 3.1 Run `npm run build` — confirm clean build
- [x] 3.2 Check header nav links appear on home, recipe, category, and tag pages
- [x] 3.3 Check breadcrumbs on recipe page show correct category link and title; confirm category link navigates correctly
- [x] 3.4 Check breadcrumbs on category, tag, and kids pages; confirm home link works
