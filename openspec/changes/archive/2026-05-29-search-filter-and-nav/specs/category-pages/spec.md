## ADDED Requirements

### Requirement: A static page exists for each recipe category
The site SHALL generate a page at `/categorie/[category]/` for every category that has at least one non-draft recipe. Categories are derived from recipe file paths (`src/content/recipes/<category>/`).

#### Scenario: Category page is accessible
- **WHEN** recipes exist in `src/content/recipes/pasta/`
- **THEN** a page is rendered at `/recepten/categorie/pasta/`

#### Scenario: Empty categories are not generated
- **WHEN** a category directory exists but contains only draft recipes
- **THEN** no category page is generated for it

### Requirement: Category page lists all recipes in that category
The category page SHALL display all non-draft recipes in the category using the shared card grid layout, sorted by pubDate descending.

#### Scenario: Category page shows correct recipes
- **WHEN** the `/categorie/pasta/` page is viewed
- **THEN** only pasta recipes are shown, no recipes from other categories

#### Scenario: Category page sorted by date
- **WHEN** a category has multiple recipes
- **THEN** they are displayed newest first

### Requirement: Category page has a heading identifying the category
The category page SHALL display the category name as a page heading.

#### Scenario: Category heading displayed
- **WHEN** the `/categorie/pasta/` page is viewed
- **THEN** the page heading reads "pasta" (or capitalised equivalent)
