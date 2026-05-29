## ADDED Requirements

### Requirement: Ingredient objects have an optional category field
Each ingredient object SHALL accept an optional `category` field constrained to the enum: `"groente en fruit"`, `"vlees en vis"`, `"zuivel en eieren"`, `"kaas"`, `"pasta en granen"`, `"sauzen en kruiden"`, `"conserven"`, `"bakken"`, `"overig"`.

#### Scenario: Ingredient with valid category passes validation
- **WHEN** an ingredient has `{ quantity: 500, unit: "g", name: "tomaten", category: "groente en fruit" }`
- **THEN** it passes schema validation

#### Scenario: Ingredient without category passes validation
- **WHEN** an ingredient has `{ quantity: 500, unit: "g", name: "tomaten" }` with no `category`
- **THEN** it passes schema validation

#### Scenario: Ingredient with invalid category fails validation
- **WHEN** an ingredient has `{ quantity: 1, unit: "el", name: "olie", category: "dranken" }`
- **THEN** `npm run build` exits with a schema validation error

### Requirement: All existing recipes have ingredient categories assigned
All 13 recipe files SHALL have a `category` value on every ingredient.

#### Scenario: Categorized recipe builds cleanly
- **WHEN** all ingredients in a recipe have a valid `category`
- **THEN** `npm run build` succeeds

### Requirement: The /import command assigns categories automatically
The `/import` command SHALL include a lookup table mapping common Dutch ingredient name substrings to categories. Unrecognised ingredients default to `"overig"`.

#### Scenario: Known ingredient gets correct category
- **WHEN** importing a recipe containing `"knoflook"`
- **THEN** the ingredient is assigned `category: "groente en fruit"`

#### Scenario: Unknown ingredient gets overig
- **WHEN** importing a recipe containing an ingredient not in the lookup table
- **THEN** the ingredient is assigned `category: "overig"`
