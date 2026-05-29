## MODIFIED Requirements

### Requirement: Each recipe entry shows title and basic metadata
Each card SHALL show at minimum: the recipe title, category (derived from file path), total time (prepTime + cookTime if available), tag pills (if any), and kid ratings (if any). The entire card SHALL be a clickable link to the detail page.

#### Scenario: Recipe entry links to detail page
- **WHEN** a recipe is listed on the home page
- **THEN** clicking anywhere on the card navigates to `/recepten/<category>/<slug>/`

#### Scenario: Time display
- **WHEN** a recipe has `prepTime: 15` and `cookTime: 30`
- **THEN** the card shows a combined time of 45 min

#### Scenario: Time display without cookTime
- **WHEN** a recipe has only `prepTime: 20` and no `cookTime`
- **THEN** the card shows 20 min

#### Scenario: Tags displayed as pills
- **WHEN** a recipe has `tags: ["vegetarisch", "snel"]`
- **THEN** both tags appear as styled pill elements on the card

#### Scenario: Kid ratings displayed on card
- **WHEN** a recipe has ratings for one or both kids
- **THEN** the card shows each rated kid's name and emoji
