## ADDED Requirements

### Requirement: Each recipe has a detail page at a stable URL
The site SHALL generate a page for each non-draft recipe at `/recepten/<category>/<slug>/`, derived from the file path `src/content/recipes/<category>/<slug>.md`.

#### Scenario: Recipe page is accessible
- **WHEN** a recipe file exists at `src/content/recipes/soepen/tomatensoep.md`
- **THEN** a page is rendered at `/recepten/soepen/tomatensoep/`

#### Scenario: Draft recipes are not published
- **WHEN** a recipe has `draft: true` in frontmatter
- **THEN** no page is generated for it and it is excluded from all listings

### Requirement: Recipe detail page renders all frontmatter metadata
The detail page SHALL display: title, pubDate (formatted as Dutch date), servings count, prepTime, cookTime (if present), tags (if any), source (if present), and kids ratings (if present).

#### Scenario: Full metadata recipe renders completely
- **WHEN** a recipe has all optional fields populated
- **THEN** all fields are visible on the rendered page

#### Scenario: Partial metadata recipe renders gracefully
- **WHEN** a recipe has only required fields
- **THEN** the page renders without errors and optional sections are simply absent

### Requirement: Ingredients are rendered as a list with quantity and unit
The detail page SHALL render each ingredient as `<quantity> <unit> <name>` with the quantity in a `data-quantity` attribute for future serving scaler support.

#### Scenario: Ingredient quantity is accessible via data attribute
- **WHEN** an ingredient has `{ quantity: 500, unit: "g", name: "tomaten" }`
- **THEN** the rendered HTML contains `data-quantity="500"` on the quantity element

### Requirement: Recipe body is rendered below ingredients
The Markdown body (starting with `## Bereiding`) SHALL be rendered as HTML below the ingredients list.

#### Scenario: Method steps render as HTML
- **WHEN** a recipe body contains `## Bereiding` followed by numbered steps
- **THEN** the page renders a heading and the steps as HTML

### Requirement: Kids ratings are displayed as a name–emoji pair
If `ratings` is present, the page SHALL display each rated child's name alongside their emoji.

#### Scenario: Both kids rated
- **WHEN** ratings has both `emma` and `annemijn`
- **THEN** both are displayed as "Emma 😍" / "Annemijn 😐" style pairs
