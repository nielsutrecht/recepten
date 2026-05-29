## ADDED Requirements

### Requirement: Recipe detail page has a serving scaler control
The recipe detail page SHALL display a `[−] N [+]` control next to the servings count. The default value is the recipe's `servings` frontmatter field. The minimum value is 1.

#### Scenario: Scaler renders with default servings
- **WHEN** a recipe detail page loads
- **THEN** the scaler shows the recipe's default servings value between two buttons

#### Scenario: Servings cannot go below 1
- **WHEN** the user taps `[−]` while servings is 1
- **THEN** servings stays at 1 and no quantity update occurs

### Requirement: Ingredient quantities update in real time when servings change
When the serving count changes, all ingredient quantities on the page SHALL update immediately without a page reload, scaled proportionally from the original recipe quantities.

#### Scenario: Scaling up doubles quantities
- **WHEN** default servings is 4 and user taps `[+]` once (to 5)
- **THEN** each ingredient quantity is multiplied by 5/4

#### Scenario: Scaling down halves quantities
- **WHEN** default servings is 4 and user taps `[−]` twice (to 2)
- **THEN** each ingredient quantity is multiplied by 2/4

#### Scenario: Quantities scale from original values
- **WHEN** the user scales up then back down to the original servings
- **THEN** all quantities return to their original values exactly

### Requirement: Scaled quantities are rounded to kitchen-sensible values
Displayed quantities SHALL be rounded according to their magnitude and shown as fractions for sub-1 values where applicable.

#### Scenario: Large quantity rounds to nearest 10
- **WHEN** a scaled quantity is 166.7
- **THEN** it is displayed as 170

#### Scenario: Medium quantity rounds to nearest 5
- **WHEN** a scaled quantity is 62.5
- **THEN** it is displayed as 65

#### Scenario: Small quantity rounds to nearest 1
- **WHEN** a scaled quantity is 7.3
- **THEN** it is displayed as 7

#### Scenario: Tiny quantity rounds to nearest 0.5
- **WHEN** a scaled quantity is 1.3
- **THEN** it is displayed as 1.5

#### Scenario: Sub-1 quantity displays as fraction
- **WHEN** a scaled quantity is 0.5
- **THEN** it is displayed as ½

#### Scenario: Sub-1 quantity displays as fraction for quarter
- **WHEN** a scaled quantity is 0.25
- **THEN** it is displayed as ¼
