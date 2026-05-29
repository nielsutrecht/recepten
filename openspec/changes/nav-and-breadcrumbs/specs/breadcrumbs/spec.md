## ADDED Requirements

### Requirement: Inner pages display a breadcrumb trail below the header
Pages other than the home page SHALL display a breadcrumb trail showing the page's position in the site hierarchy. The trail appears between the header and the main page content.

#### Scenario: Breadcrumb on recipe page
- **WHEN** a recipe detail page is viewed
- **THEN** the breadcrumb reads "Recepten / [category] / [recipe title]" where "Recepten" links to home and "[category]" links to the category page

#### Scenario: Breadcrumb on category page
- **WHEN** a category page is viewed
- **THEN** the breadcrumb reads "Recepten / [category]" where "Recepten" links to home

#### Scenario: Breadcrumb on tag page
- **WHEN** a tag page is viewed
- **THEN** the breadcrumb reads "Recepten / [tag]" where "Recepten" links to home

#### Scenario: Breadcrumb on kids page
- **WHEN** the `/kids/` page is viewed
- **THEN** the breadcrumb reads "Recepten / voor de kids" where "Recepten" links to home

#### Scenario: Home page has no breadcrumb
- **WHEN** the home page is viewed
- **THEN** no breadcrumb trail is displayed

### Requirement: Current page segment is not a link
The last segment of the breadcrumb trail (the current page) SHALL be plain text, not a link.

#### Scenario: Last crumb is not clickable
- **WHEN** a breadcrumb trail is displayed
- **THEN** the final segment has no href and is styled as plain text
