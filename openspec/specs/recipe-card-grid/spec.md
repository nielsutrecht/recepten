## ADDED Requirements

### Requirement: Home page displays recipes as a 2-column card grid
The home page SHALL render recipes in a CSS Grid layout with 2 equal-width columns on screens wider than 480px, collapsing to a single column on narrower screens.

#### Scenario: Desktop grid layout
- **WHEN** the home page is viewed on a screen wider than 480px
- **THEN** recipes are displayed in 2 columns with equal card widths

#### Scenario: Mobile single-column layout
- **WHEN** the home page is viewed on a screen 480px wide or narrower
- **THEN** recipes are displayed in a single column

### Requirement: Each card is fully clickable and links to the recipe detail page
The entire card area SHALL be wrapped in an `<a>` element linking to the recipe's detail page — not just the title.

#### Scenario: Card click navigates to recipe
- **WHEN** a user clicks anywhere on a recipe card
- **THEN** they are navigated to `/recepten/<category>/<slug>/`

### Requirement: Each card displays category, total time, tags, and kid ratings
Each card SHALL show: recipe title (prominent), category (derived from file path), total time (prepTime + cookTime), tag pills (if any), and kid ratings (if present).

#### Scenario: Full-data card renders all sections
- **WHEN** a recipe has tags and ratings
- **THEN** the card shows title, category, time, all tags as pills, and each kid's name with their emoji

#### Scenario: Card without optional data renders gracefully
- **WHEN** a recipe has no tags and no ratings
- **THEN** the card shows title, category, and time; tag and rating sections are absent

#### Scenario: Category derived from file path
- **WHEN** a recipe file is at `src/content/recipes/pasta/lasagne.md`
- **THEN** the card displays "pasta" as the category label
