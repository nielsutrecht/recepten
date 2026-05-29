## MODIFIED Requirements

### Requirement: Each recipe entry shows title and basic metadata
Each card SHALL show at minimum: the recipe title (as a link to the detail page), category (as a link to the category page), total time (prepTime + cookTime if available), tag pills (each linking to the tag page), and kid ratings (if any).

#### Scenario: Recipe entry title links to detail page
- **WHEN** a recipe is listed on the home page
- **THEN** clicking the recipe title navigates to `/recepten/<category>/<slug>/`

#### Scenario: Time display
- **WHEN** a recipe has `prepTime: 15` and `cookTime: 30`
- **THEN** the card shows a combined time of 45 min

#### Scenario: Time display without cookTime
- **WHEN** a recipe has only `prepTime: 20` and no `cookTime`
- **THEN** the card shows 20 min

#### Scenario: Tags displayed as linked pills
- **WHEN** a recipe has `tags: ["vegetarisch", "snel"]`
- **THEN** both tags appear as pill links to their respective tag pages

#### Scenario: Kid ratings displayed on card
- **WHEN** a recipe has ratings for one or both kids
- **THEN** the card shows each rated kid's name and emoji

## ADDED Requirements

### Requirement: Home page displays search input and tag chips above the card grid
The home page listing SHALL be preceded by a text search input and a row of tag chip toggles, enabling client-side filtering without a page reload.

#### Scenario: Search input visible above grid
- **WHEN** the home page loads
- **THEN** a text search input is visible above the recipe card grid

#### Scenario: Tag chips visible above grid
- **WHEN** the home page loads
- **THEN** a chip for every unique tag is visible above the recipe card grid
