## ADDED Requirements

### Requirement: Recipe card markup is defined in a shared component
A `RecipeCard.astro` component SHALL exist at `src/components/RecipeCard.astro` and accept a recipe entry and base URL as props. All recipe listing pages (home, category, tag) SHALL use this component rather than inlining card markup.

#### Scenario: Component used on home page
- **WHEN** the home page renders recipe cards
- **THEN** each card is rendered via `RecipeCard.astro`

#### Scenario: Component used on category page
- **WHEN** a category page renders recipe cards
- **THEN** each card is rendered via `RecipeCard.astro`

#### Scenario: Component used on tag page
- **WHEN** a tag page renders recipe cards
- **THEN** each card is rendered via `RecipeCard.astro`

### Requirement: Card exposes data attributes for client-side filtering
Each rendered card SHALL have `data-title`, `data-tags`, and `data-category` attributes containing the recipe's title (lowercase), comma-separated tags, and category respectively.

#### Scenario: Data attributes present on rendered card
- **WHEN** a recipe card is rendered for a recipe with title "Tomatensoep", tags ["soep", "vegetarisch"], category "soepen"
- **THEN** the card element has `data-title="tomatensoep"`, `data-tags="soep,vegetarisch"`, `data-category="soepen"`
