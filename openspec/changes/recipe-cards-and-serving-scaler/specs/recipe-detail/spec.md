## MODIFIED Requirements

### Requirement: Recipe detail page renders all frontmatter metadata
The detail page SHALL display: title, pubDate (formatted as Dutch date), servings count (as an interactive scaler control), prepTime, cookTime (if present), tags (if any), source (if present), and kids ratings (if present).

#### Scenario: Full metadata recipe renders completely
- **WHEN** a recipe has all optional fields populated
- **THEN** all fields are visible on the rendered page

#### Scenario: Partial metadata recipe renders gracefully
- **WHEN** a recipe has only required fields
- **THEN** the page renders without errors and optional sections are simply absent

#### Scenario: Servings displayed as interactive control
- **WHEN** a recipe detail page loads
- **THEN** the servings count is displayed as a `[−] N [+]` scaler rather than plain text

## ADDED Requirements

### Requirement: Ingredients are rendered as a dynamically scalable list
The detail page SHALL render each ingredient as `<quantity> <unit> <name>` with the quantity in a `data-quantity` attribute. Quantity display values SHALL update in real time when the serving scaler changes.

#### Scenario: Ingredient quantity is accessible via data attribute
- **WHEN** an ingredient has `{ quantity: 500, unit: "g", name: "tomaten" }`
- **THEN** the rendered HTML contains `data-quantity="500"` on the quantity element

#### Scenario: Displayed quantity updates on scaler change
- **WHEN** the user changes the serving count via the scaler
- **THEN** all ingredient quantity display values update without a page reload
