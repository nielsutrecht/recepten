## ADDED Requirements

### Requirement: Planner page exists at /planner/ with a Mon–Sun day grid
The site SHALL have a static page at `/planner/` displaying seven day rows (Maandag through Zondag). Each row shows either an assigned recipe or an empty slot.

#### Scenario: Planner page is accessible
- **WHEN** a user navigates to `/recepten/planner/`
- **THEN** the page renders with seven day rows

### Requirement: Empty slots show a recipe assignment button
An unassigned day slot SHALL display a "+ kies recept" button. Clicking it opens the recipe picker for that day.

#### Scenario: Empty slot renders assignment button
- **WHEN** a day has no recipe assigned
- **THEN** the slot shows a "+ kies recept" button

#### Scenario: Clicking assignment button opens picker
- **WHEN** a user clicks "+ kies recept" on an empty day
- **THEN** the recipe picker dialog opens

### Requirement: Assigned slots show recipe name, serving scaler, and remove button
A day with a recipe assigned SHALL display the recipe title, a `[−] N [+]` serving scaler (default 4), and a `[✕]` remove button.

#### Scenario: Assigned slot renders correctly
- **WHEN** a recipe is assigned to a day with servings set to 4
- **THEN** the row shows the recipe title, "− 4 +" controls, and an ✕ button

#### Scenario: Serving count updates on button press
- **WHEN** a user taps `[+]` on an assigned slot
- **THEN** the serving count increments by 1 (minimum 1)

#### Scenario: Remove button clears the slot
- **WHEN** a user clicks `[✕]` on an assigned slot
- **THEN** the day becomes empty and the "+ kies recept" button reappears

### Requirement: Plan state persists across page reloads
The assigned recipes and serving counts SHALL be saved to `localStorage` under the key `recepten-planner-v1` and restored on page load.

#### Scenario: Plan survives page reload
- **WHEN** a user assigns a recipe and reloads the page
- **THEN** the assignment is still present

### Requirement: A "Plan wissen" button clears all assignments
A "Plan wissen" button SHALL clear all day assignments and reset the shopping list checkboxes.

#### Scenario: Plan wissen clears everything
- **WHEN** a user clicks "Plan wissen"
- **THEN** all seven day slots become empty
