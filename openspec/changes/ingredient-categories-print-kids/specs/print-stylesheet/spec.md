## ADDED Requirements

### Requirement: Recipe pages print as a clean single-column layout
When a recipe detail page is printed, the output SHALL show only the recipe content: title, metadata (time, servings, source), kid ratings, ingredient list, bereiding steps, and notities. All navigation and interactive UI elements SHALL be hidden.

#### Scenario: Navigation hidden on print
- **WHEN** a recipe page is printed
- **THEN** the site header and back link are not visible in the printout

#### Scenario: Filter and scaler UI hidden on print
- **WHEN** a recipe page is printed
- **THEN** the serving scaler +/− buttons and any filter chips are not visible

#### Scenario: Recipe content visible on print
- **WHEN** a recipe page is printed
- **THEN** the title, ingredient list, and bereiding steps are clearly visible

### Requirement: Print layout uses a single column with print-appropriate styling
The print stylesheet SHALL remove box shadows, card borders, and decorative backgrounds, and use a single-column layout regardless of screen width.

#### Scenario: No decorative styling in print
- **WHEN** a recipe page is printed
- **THEN** there are no coloured backgrounds, shadows, or rounded card borders in the output

### Requirement: Printed ingredient quantities reflect the current scaled values
Since ingredient quantities are updated in the DOM by the serving scaler, the print output SHALL show whatever quantities are currently displayed — allowing a user to scale first then print.

#### Scenario: Scaled quantities appear in print
- **WHEN** a user scales a recipe to 6 servings and then prints
- **THEN** the printed ingredient quantities reflect the 6-serving amounts
