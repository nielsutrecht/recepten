## ADDED Requirements

### Requirement: A dedicated kids-approved page exists at /kids/
The site SHALL have a static page at `/kids/` displaying all recipes that have been rated by at least one kid and have received no rejection ratings (😒 or 🤢) from either Emma or Annemijn.

#### Scenario: Approved recipe appears on kids page
- **WHEN** a recipe has `ratings.emma: "😍"` and no rating for Annemijn
- **THEN** it appears on `/kids/`

#### Scenario: Rejected recipe is excluded
- **WHEN** a recipe has `ratings.emma: "😍"` and `ratings.annemijn: "😒"`
- **THEN** it does NOT appear on `/kids/`

#### Scenario: Unrated recipe is excluded
- **WHEN** a recipe has no `ratings` field at all
- **THEN** it does NOT appear on `/kids/`

#### Scenario: Neutral rating is approved
- **WHEN** a recipe has `ratings.emma: "😐"` and `ratings.annemijn: "😐"`
- **THEN** it appears on `/kids/`

### Requirement: Kids page uses the standard card grid
The `/kids/` page SHALL display approved recipes using the shared `RecipeCard.astro` component in the same 2-column grid layout as other listing pages, sorted by pubDate descending.

#### Scenario: Kids page layout matches other listing pages
- **WHEN** the `/kids/` page is viewed
- **THEN** recipes are shown as cards in a 2-column grid

### Requirement: Kids page has a descriptive heading
The `/kids/` page SHALL have a heading that identifies it as showing kid-approved recipes, and display a recipe count.

#### Scenario: Heading and count visible
- **WHEN** the `/kids/` page is viewed
- **THEN** a heading and the number of approved recipes are visible
