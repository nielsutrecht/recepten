## ADDED Requirements

### Requirement: Shopping list is always visible below the week grid
The shopping list SHALL be displayed below the day grid at all times, even when no recipes are planned. When the plan is empty it shows a placeholder message.

#### Scenario: Empty plan shows placeholder
- **WHEN** no recipes are assigned to any day
- **THEN** the shopping list shows a message indicating no recipes are planned

#### Scenario: Shopping list updates when plan changes
- **WHEN** a user assigns or removes a recipe
- **THEN** the shopping list updates immediately without a page reload

### Requirement: Ingredients are scaled by the planned serving count
Each ingredient's quantity in the shopping list SHALL be scaled by `plannedServings / recipeDefaultServings`.

#### Scenario: Ingredients scale with serving count
- **WHEN** tomatensoep (default 4 servings) is planned with 8 servings
- **THEN** each ingredient quantity is doubled in the shopping list

### Requirement: Ingredients from multiple recipes are combined when name and unit match exactly
When two or more planned recipes share an ingredient with identical `name` AND `unit`, their quantities SHALL be summed into a single line.

#### Scenario: Same ingredient from two recipes is combined
- **WHEN** two planned recipes both require `knoflook` in `teentjes`
- **THEN** the shopping list shows one line with the summed quantity

#### Scenario: Same ingredient with different units is not combined
- **WHEN** one recipe requires `100 g knoflook` and another requires `2 teentjes knoflook`
- **THEN** the shopping list shows two separate lines

### Requirement: Shopping list is grouped by ingredient category in supermarket order
Ingredients SHALL be grouped under category headings in the following order: groente en fruit, vlees en vis, zuivel en eieren, kaas, pasta en granen, conserven, sauzen en kruiden, bakken, overig.

#### Scenario: Categories appear in correct order
- **WHEN** a plan includes recipes with ingredients in multiple categories
- **THEN** "groente en fruit" appears before "pasta en granen" before "bakken"

### Requirement: Each shopping list item has a persistent checkbox
Each ingredient line SHALL have a checkbox. Checked state persists in `localStorage` and survives page reloads. Clicking "Plan wissen" unchecks all items.

#### Scenario: Checked item survives reload
- **WHEN** a user checks an ingredient and reloads the page
- **THEN** the ingredient remains checked

#### Scenario: Plan wissen unchecks all items
- **WHEN** a user clicks "Plan wissen"
- **THEN** all checkboxes are unchecked

### Requirement: Each shopping list line shows recipe attribution
Each ingredient line SHALL show which recipe(s) it comes from, in parentheses.

#### Scenario: Single-recipe attribution shown
- **WHEN** an ingredient comes from one recipe
- **THEN** the line shows "(Tomatensoep)" after the ingredient

#### Scenario: Multi-recipe attribution shown
- **WHEN** an ingredient comes from two recipes after combining
- **THEN** the line shows "(Tomatensoep, Lasagne)" after the ingredient
