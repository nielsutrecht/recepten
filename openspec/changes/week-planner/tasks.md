## 1. Page Scaffold and Data

- [x] 1.1 Create `src/pages/planner.astro` — query all non-draft recipes, serialise to client via `define:vars` (id, title, servings, prepTime, cookTime, tags, ingredients with category)
- [x] 1.2 Add `<Base>` layout with breadcrumb `Recepten / weekplanner` and page heading "Weekplanner"
- [x] 1.3 Render the static HTML structure: day grid container, `<dialog id="recipe-picker">`, shopping list section

## 2. State Management

- [x] 2.1 Implement `loadState()` / `saveState()` helpers using `localStorage` key `recepten-planner-v1`; wrap in try/catch for private-browsing safety
- [x] 2.2 Define state shape: `{ days: { ma, di, wo, do, vr, za, zo }, checkedItems: string[] }`; initialise from localStorage or defaults on page load

## 3. Week Grid

- [x] 3.1 Render seven day rows (Maandag–Zondag) from state: empty slot → "+ kies recept" button; assigned slot → recipe title + `[−] N [+]` + `[✕]`
- [x] 3.2 Wire `[+]` / `[−]` buttons: update `state.days[day].servings`, clamp to min 1, save, re-render shopping list
- [x] 3.3 Wire `[✕]` button: set `state.days[day] = null`, save, re-render row and shopping list
- [x] 3.4 Wire "+ kies recept" button: store `pendingDay`, reset picker search, call `dialog.showModal()`
- [x] 3.5 Wire "Plan wissen" button: reset all days to null, clear checkedItems, save, re-render everything

## 4. Recipe Picker Dialog

- [x] 4.1 Render recipe cards inside the dialog from `recipeData` — show title and time, clicking assigns to `pendingDay` with default servings 4, calls `dialog.close()`
- [x] 4.2 Wire picker search input: filter visible cards by title substring (case-insensitive) on input
- [x] 4.3 Close dialog on backdrop click: `dialog.addEventListener('click', e => { if (e.target === dialog) dialog.close() })`
- [x] 4.4 Reset search input to empty each time the dialog opens (in the showModal() call site)

## 5. Shopping List

- [x] 5.1 Implement `buildShoppingList(state, recipeData)`: scale ingredient quantities by `plannedServings / defaultServings`, group by category, sum identical name+unit pairs, collect recipe attribution
- [x] 5.2 Implement `roundKitchen(value)` (same algorithm as serving scaler: magnitude-based rounding with fraction symbols for < 1)
- [x] 5.3 Render shopping list grouped by category in supermarket order; each item shows: `<input type="checkbox"> <quantity> <unit> <name> (<recipes>)`; empty plan shows placeholder text
- [x] 5.4 Wire checkboxes: toggle item key (`name:unit`) in `state.checkedItems`, save to localStorage
- [x] 5.5 Restore checked state on render: check localStorage `checkedItems` and apply `checked` attribute to matching items

## 6. Styling

- [x] 6.1 Style day grid: day label left, content right; assigned slot shows recipe name in terracotta, serving controls inline; empty slot muted
- [x] 6.2 Style recipe picker dialog: full-width on mobile, max-width ~600px on desktop; search input at top; card grid below; close button in corner
- [x] 6.3 Style shopping list: category headings in small caps or muted style; checked items shown with strikethrough; attribution in muted smaller text

## 7. Verify

- [x] 7.1 Run `npm run build` — confirm clean build
- [x] 7.2 Assign recipes to several days, adjust servings, reload — confirm state persists
- [x] 7.3 Verify shopping list: quantities scale correctly, same-name+unit ingredients combine, categories in correct order
- [x] 7.4 Check off shopping items, reload — confirm checked state persists
- [x] 7.5 Click "Plan wissen" — confirm all slots clear and all checkboxes uncheck
