## ADDED Requirements

### Requirement: A recipe picker dialog opens when selecting a recipe for a day
Clicking "+ kies recept" SHALL open an HTML5 `<dialog>` element containing a search input and a scrollable grid of recipe cards. Clicking a card assigns that recipe to the day and closes the dialog.

#### Scenario: Dialog opens on slot click
- **WHEN** a user clicks "+ kies recept"
- **THEN** the recipe picker dialog is visible and focused

#### Scenario: Selecting a recipe closes the dialog and assigns the recipe
- **WHEN** a user clicks a recipe card in the picker
- **THEN** the dialog closes and the recipe is assigned to the day with default servings (4)

#### Scenario: Dialog closes without selection on backdrop click
- **WHEN** a user clicks outside the dialog (on the backdrop)
- **THEN** the dialog closes and the day assignment is unchanged

### Requirement: Recipe picker has a search input that filters displayed cards
The dialog SHALL contain a text input. As the user types, only cards whose title matches the query (case-insensitive substring) are shown.

#### Scenario: Search filters cards
- **WHEN** a user types "pasta" in the picker search input
- **THEN** only recipes with "pasta" in their title remain visible

#### Scenario: Clearing search restores all cards
- **WHEN** a user clears the picker search input
- **THEN** all recipe cards are visible again

### Requirement: Picker search resets when the dialog opens
Each time the dialog is opened, the search input SHALL be cleared and all recipes shown.

#### Scenario: Search clears on reopen
- **WHEN** a user opens the picker, searches, closes without selecting, then opens again
- **THEN** the search input is empty and all recipes are visible
