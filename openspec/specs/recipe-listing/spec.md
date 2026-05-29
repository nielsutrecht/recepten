## ADDED Requirements

### Requirement: Home page lists all published recipes
The home page at `/` SHALL display a list of all non-draft recipes, each linking to its detail page.

#### Scenario: Published recipe appears on home page
- **WHEN** a recipe has `draft: false` (or omitted)
- **THEN** it appears in the home page listing

#### Scenario: Draft recipe is excluded from home page
- **WHEN** a recipe has `draft: true`
- **THEN** it does not appear in the home page listing

### Requirement: Each recipe entry shows title and basic metadata
Each listing entry SHALL show at minimum: the recipe title (as a link to the detail page) and the total time (prepTime + cookTime if available).

#### Scenario: Recipe entry links to detail page
- **WHEN** a recipe is listed on the home page
- **THEN** clicking its title navigates to `/recepten/<category>/<slug>/`

#### Scenario: Time display
- **WHEN** a recipe has `prepTime: 15` and `cookTime: 30`
- **THEN** the listing shows a combined time of 45 min

#### Scenario: Time display without cookTime
- **WHEN** a recipe has only `prepTime: 20` and no `cookTime`
- **THEN** the listing shows 20 min

### Requirement: Recipes are sorted by publication date descending
The home page listing SHALL display recipes with the most recently added (`pubDate`) first.

#### Scenario: Newer recipe appears before older
- **WHEN** two recipes exist with different `pubDate` values
- **THEN** the newer one appears earlier in the list
