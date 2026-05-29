## ADDED Requirements

### Requirement: Home page has a text search input that filters cards by title
The home page SHALL display a text input above the card grid. As the user types, cards whose title does not contain the query (case-insensitive substring match) are hidden. No page reload occurs.

#### Scenario: Matching cards remain visible
- **WHEN** the user types "pasta" in the search input
- **THEN** only cards whose title contains "pasta" (case-insensitive) remain visible

#### Scenario: Non-matching cards are hidden
- **WHEN** the user types "pasta" in the search input
- **THEN** cards whose title does not contain "pasta" are hidden

#### Scenario: Clearing the input restores all cards
- **WHEN** the user clears the search input
- **THEN** all cards become visible again (subject to active tag filters)

### Requirement: Home page has tag chip toggles that filter cards by tag
The home page SHALL display a chip for every unique tag across all recipes. Clicking a chip toggles it on/off. Cards that do not carry at least one active tag are hidden (OR logic). No page reload occurs.

#### Scenario: No tags selected shows all cards
- **WHEN** no tag chips are active
- **THEN** all recipes are visible (subject to text search)

#### Scenario: One tag selected filters to matching cards
- **WHEN** the user activates the "vegetarisch" chip
- **THEN** only cards tagged "vegetarisch" remain visible

#### Scenario: Multiple tags selected uses OR logic
- **WHEN** the user activates both "bbq" and "italiaans" chips
- **THEN** cards tagged "bbq" OR "italiaans" (or both) are visible

#### Scenario: Active chip is visually distinct
- **WHEN** a tag chip is toggled on
- **THEN** it has a visually distinct style (e.g. filled background) compared to inactive chips

### Requirement: Search and tag filters combine with AND logic
Both filters apply simultaneously — a recipe must match the text search AND satisfy the tag filter.

#### Scenario: Combined search and tag filter
- **WHEN** the user types "la" and activates "italiaans"
- **THEN** only cards whose title contains "la" AND are tagged "italiaans" are visible
