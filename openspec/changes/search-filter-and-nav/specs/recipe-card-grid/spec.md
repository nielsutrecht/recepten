## MODIFIED Requirements

### Requirement: Each card displays category, total time, tags, and kid ratings
Each card SHALL show: recipe title (prominent, as a link to the detail page), category (derived from file path, as a link to the category page), total time (prepTime + cookTime), tag pills (each a link to the tag page), and kid ratings (if present).

#### Scenario: Full-data card renders all sections
- **WHEN** a recipe has tags and ratings
- **THEN** the card shows title link, category link, time, tag links, and each kid's name with their emoji

#### Scenario: Card without optional data renders gracefully
- **WHEN** a recipe has no tags and no ratings
- **THEN** the card shows title link, category link, and time; tag and rating sections are absent

#### Scenario: Category derived from file path and links to category page
- **WHEN** a recipe file is at `src/content/recipes/pasta/lasagne.md`
- **THEN** the card displays "pasta" linking to `/recepten/categorie/pasta/`

#### Scenario: Tag pill links to tag page
- **WHEN** a recipe has tag "vegetarisch"
- **THEN** the tag pill links to `/recepten/tag/vegetarisch/`
