## ADDED Requirements

### Requirement: A static page exists for each tag
The site SHALL generate a page at `/tag/[tag]/` for every tag that appears on at least one non-draft recipe.

#### Scenario: Tag page is accessible
- **WHEN** at least one recipe has `tags: ["vegetarisch"]`
- **THEN** a page is rendered at `/recepten/tag/vegetarisch/`

### Requirement: Tag page lists all recipes with that tag
The tag page SHALL display all non-draft recipes carrying that tag using the shared card grid layout, sorted by pubDate descending.

#### Scenario: Tag page shows correct recipes
- **WHEN** the `/tag/vegetarisch/` page is viewed
- **THEN** only recipes tagged "vegetarisch" are shown

#### Scenario: Tag page sorted by date
- **WHEN** a tag has multiple recipes
- **THEN** they are displayed newest first

### Requirement: Tag page has a heading identifying the tag
The tag page SHALL display the tag name as a page heading.

#### Scenario: Tag heading displayed
- **WHEN** the `/tag/bbq/` page is viewed
- **THEN** the page heading reads "bbq" (or styled equivalent)
