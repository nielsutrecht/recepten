## ADDED Requirements

### Requirement: Push to main triggers a GitHub Pages deployment
The repository SHALL have a GitHub Actions workflow at `.github/workflows/deploy.yml` that builds the site and deploys it to GitHub Pages whenever a commit is pushed to `main`.

#### Scenario: Successful push deploys the site
- **WHEN** a commit is pushed to the `main` branch
- **THEN** the Actions workflow runs, builds the site, and deploys `dist/` to GitHub Pages

#### Scenario: Manual trigger is available
- **WHEN** a developer triggers the workflow manually via the Actions UI (`workflow_dispatch`)
- **THEN** the build and deploy steps execute

### Requirement: Workflow uses correct permissions
The workflow SHALL set `permissions: pages: write` and `id-token: write` on the deploy job, and `contents: read` on the build job.

#### Scenario: Deployment succeeds without extra permissions
- **WHEN** the deploy job runs
- **THEN** it authenticates with GitHub Pages using OIDC (no PAT required)

### Requirement: Concurrent deployments are prevented
The workflow SHALL use a concurrency group named `"pages"` with `cancel-in-progress: false` so that in-flight deployments are not cancelled by rapid pushes.

#### Scenario: Second push queues rather than cancels
- **WHEN** two commits are pushed in quick succession
- **THEN** the second deploy waits for the first to finish rather than cancelling it

### Requirement: Node.js version is pinned
The build job SHALL use Node.js 20 with npm caching enabled.

#### Scenario: Build uses cached dependencies
- **WHEN** `package-lock.json` has not changed between runs
- **THEN** `npm ci` restores from cache and the install step completes quickly
