## ADDED Requirements

### Requirement: Recipe content collection is defined with a Zod schema
`src/content.config.ts` SHALL define a `recipes` collection using Astro's glob loader pointed at `./src/content/recipes`, with a Zod schema covering all PRD frontmatter fields.

#### Scenario: Valid recipe frontmatter passes validation
- **WHEN** a recipe `.md` file has all required fields with correct types
- **THEN** `npm run build` succeeds and the recipe is included in the collection

#### Scenario: Missing required field fails the build
- **WHEN** a recipe `.md` file is missing `title`, `pubDate`, `servings`, or `prepTime`
- **THEN** `npm run build` exits with a schema validation error

### Requirement: Required frontmatter fields are enforced
The schema SHALL require: `title` (string), `pubDate` (coerced date), `servings` (positive integer), `prepTime` (positive integer), `ingredients` (non-empty array of ingredient objects).

#### Scenario: All required fields present
- **WHEN** a recipe has title, pubDate, servings, prepTime, and at least one ingredient
- **THEN** the recipe is valid

### Requirement: Optional frontmatter fields have correct types
The schema SHALL accept optional fields: `cookTime` (positive integer), `tags` (string array, default `[]`), `source` (string), `ratings` (partial object with `emma` and `annemijn`), `draft` (boolean, default `false`).

#### Scenario: Recipe without optional fields is valid
- **WHEN** a recipe omits cookTime, tags, source, ratings, and draft
- **THEN** the recipe is valid and defaults apply (`tags: []`, `draft: false`)

### Requirement: Rating values are constrained to the approved emoji palette
Rating fields SHALL only accept values from the set `['😍', '😊', '😐', '😒', '🤢']`.

#### Scenario: Invalid rating emoji fails validation
- **WHEN** a recipe has `ratings.emma: '⭐'`
- **THEN** `npm run build` exits with a schema validation error

### Requirement: Ingredient objects have quantity, unit, and name
Each entry in the `ingredients` array SHALL be an object with `quantity` (positive number), `unit` (string), and `name` (string).

#### Scenario: Ingredient with all fields is valid
- **WHEN** an ingredient has `{ quantity: 500, unit: "g", name: "tomaten" }`
- **THEN** it passes schema validation

#### Scenario: Ingredient missing name fails validation
- **WHEN** an ingredient has `{ quantity: 1, unit: "el" }` with no `name`
- **THEN** `npm run build` exits with a schema validation error
