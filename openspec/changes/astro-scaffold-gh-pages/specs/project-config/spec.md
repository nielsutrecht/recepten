## ADDED Requirements

### Requirement: Astro project is configured for GitHub Pages subpath deployment
The project SHALL have `astro.config.mjs` with `site: 'https://nielsutrecht.github.io'`, `base: '/recepten'`, and the `@astrojs/sitemap` integration enabled.

#### Scenario: Dev server runs at correct base path
- **WHEN** `npm run dev` is executed
- **THEN** the site is accessible at `http://localhost:4321/recepten/`

#### Scenario: Build output uses correct asset paths
- **WHEN** `npm run build` is executed
- **THEN** all asset URLs in `dist/` are prefixed with `/recepten/`

### Requirement: TypeScript is configured in strict mode
The project SHALL have `tsconfig.json` extending `astro/tsconfigs/strict` with `strictNullChecks: true`.

#### Scenario: TypeScript errors fail the build
- **WHEN** a `.astro` or `.ts` file contains a type error
- **THEN** `npm run build` exits with a non-zero status

### Requirement: Project scripts are defined
`package.json` SHALL define `dev`, `build`, and `preview` scripts as `astro dev`, `astro build`, and `astro preview` respectively.

#### Scenario: Standard commands are available
- **WHEN** a developer runs `npm run dev`, `npm run build`, or `npm run preview`
- **THEN** the corresponding Astro command executes
