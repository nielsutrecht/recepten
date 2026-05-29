## ADDED Requirements

### Requirement: Header contains navigation links to all top-level destinations
The site header SHALL contain links to: the home page (site title), `/kids/`, and `/planner/`. These links SHALL be visible on every page.

#### Scenario: Nav links present on home page
- **WHEN** the home page is viewed
- **THEN** the header contains links to "Voor de kids" and "Weekplanner"

#### Scenario: Nav links present on recipe page
- **WHEN** a recipe detail page is viewed
- **THEN** the header contains links to "Voor de kids" and "Weekplanner"

#### Scenario: Nav links present on category page
- **WHEN** a category page is viewed
- **THEN** the header contains links to "Voor de kids" and "Weekplanner"

### Requirement: Site title in header links to home
The site title ("Recepten") in the header SHALL remain a link to the home page (`/`).

#### Scenario: Site title links home
- **WHEN** a user clicks the site title in the header
- **THEN** they are navigated to the home page
