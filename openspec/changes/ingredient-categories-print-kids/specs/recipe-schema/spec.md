## MODIFIED Requirements

### Requirement: Ingredient objects have quantity, unit, and name
Each entry in the `ingredients` array SHALL be an object with `quantity` (positive number), `unit` (string), `name` (string), and an optional `category` (one of the 9 defined ingredient category values).

#### Scenario: Ingredient with all fields is valid
- **WHEN** an ingredient has `{ quantity: 500, unit: "g", name: "tomaten", category: "groente en fruit" }`
- **THEN** it passes schema validation

#### Scenario: Ingredient without category is valid
- **WHEN** an ingredient has `{ quantity: 1, unit: "el", name: "olijfolie" }` with no `category`
- **THEN** it passes schema validation

#### Scenario: Ingredient missing name fails validation
- **WHEN** an ingredient has `{ quantity: 1, unit: "el" }` with no `name`
- **THEN** `npm run build` exits with a schema validation error

#### Scenario: Ingredient with invalid category fails validation
- **WHEN** an ingredient has `category: "dranken"` (not in the enum)
- **THEN** `npm run build` exits with a schema validation error
