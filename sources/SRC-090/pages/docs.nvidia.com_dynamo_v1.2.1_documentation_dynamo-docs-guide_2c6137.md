source: https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide
lastmod: 2026-09-24T19:58:16.636Z

# How to Build and Publish Dynamo Docs

This document describes the architecture, workflows, and maintenance procedures for the
NVIDIA Dynamo documentation website powered by [Fern](https://buildwithfern.com/).

The documentation website is published at [https://docs.nvidia.com/dynamo](https://docs.nvidia.com/dynamo). CI handles publishing, including hosting, CDN, and versioned URL routing.

The `docs-website`

branch is **CI-managed and must never be edited by
hand**. All documentation authoring happens on `main`

(or a feature
branch based on `main`

). The sync workflow copies changes to
`docs-website`

automatically.

## Table of Contents

[Branch Architecture](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#branch-architecture)[Directory Layout](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#directory-layout)[Configuration Files](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#configuration-files)[GitHub Workflows](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#github-workflows)[Content Authoring](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#content-authoring)[Callout Conversion](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#callout-conversion)[Running Locally](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#running-locally)[Version Management](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#version-management)[How Publishing Works](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#how-publishing-works)[Common Tasks](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#common-tasks)[Claude Code Skills](https://docs.nvidia.com/dynamo/v1.2.1/documentation/dynamo-docs-guide#claude-code-skills)

## Claude Code Skills

A single Claude Code skill automates common docs tasks. Invoke it as a slash
command in Claude Code (e.g., `/dynamo-docs`

) — the skill walks through
the full workflow: creating, editing, or removing the markdown file, updating
the navigation in `docs/index.yml`

, and running `fern check`

to validate.

## Branch Architecture

The documentation system uses a **dual-branch model**:

Authors edit pages on `main`

. A GitHub Actions workflow automatically syncs
changes to the `docs-website`

branch and publishes them to Fern. The
`docs-website`

branch is never edited by hand — it is entirely managed by CI.

### Why two branches?

The `docs-website`

branch accumulates versioned snapshots over time (e.g.
`pages-v0.8.0/`

, `pages-v0.8.1/`

). Keeping these on a separate branch avoids
bloating the `main`

branch with frozen copies of old documentation.

## Directory Layout

### On `main`


### On `docs-website`


The `docs-website`

branch has a different layout optimized for Fern’s directory
conventions, plus versioned snapshots:

Each `pages-vX.Y.Z/`

directory is an immutable copy of `pages/`

taken at
release time. The corresponding `versions/vX.Y.Z.yml`

file is a copy of
`dev.yml`

with all `../pages/`

paths rewritten to `../pages-vX.Y.Z/`

.

The sync workflow copies content from `main`

’s `docs/`

into `fern/pages/`

and
transforms navigation paths in `index.yml`

→ `versions/dev.yml`

accordingly.

## Configuration Files

`fern/fern.config.json`


**organization**: The Fern organization that owns the docs site.**version**: Pins the Fern CLI version used for generation.

`fern/docs.yml`


This is the main Fern site configuration. Key sections:

**Important:** On `main`

, `docs.yml`

only lists the `dev`

version. On
`docs-website`

, it contains the **full versions array** (dev + all releases).
The sync workflow preserves the versions array from `docs-website`

when copying
`docs.yml`

from `main`

.

`docs/index.yml`


Defines the navigation tree — the sidebar structure of the docs site. Each entry maps a page title to a markdown file path:

Paths are relative to the `docs/`

directory. Sections can be nested. Pages can
be marked as `hidden: true`

to make them accessible by URL but invisible in the
sidebar.

During sync to `docs-website`

, the workflow copies `index.yml`

to
`fern/versions/dev.yml`

and transforms paths (e.g., `getting-started/X`

→
`../pages/getting-started/X`

) to match the docs-website directory layout.

## GitHub Workflows

### Fern Docs Workflow (`fern-docs.yml`

)

**Location:** `.github/workflows/fern-docs.yml`


This single consolidated workflow handles linting, syncing, versioning, and publishing. It runs three jobs depending on the trigger:

#### Job 1: Lint (PRs)

**Triggers:** Pull requests that modify `docs/**`

files.

**Steps:**

`fern check`

— validates Fern configuration syntax`fern docs broken-links`

— checks for broken internal links

**Purpose:** Catches broken docs before they merge.

#### Job 2: Sync dev (push to `main`

)

**Triggers:** Push to `main`

that modifies `docs/**`

files, or manual
`workflow_dispatch`

(with no tag specified).

**Steps:**

- Checks out both
`main`

and`docs-website`

branches side-by-side - Copies content from
`main`

’s`docs/`

→`docs-website`

’s`fern/pages/`

- Copies
`docs/index.yml`

→`fern/versions/dev.yml`

and transforms paths for the docs-website layout using`yq`

- Syncs assets from
`docs/assets/`

and Digest posts from`docs/digest/`

- Copies Fern config files from
`fern/`

→ docs-website’s`fern/`

(`fern.config.json`

,`components/`

,`main.css`

,`convert_callouts.py`

) - Runs
`convert_callouts.py`

to transform GitHub-style callouts to Fern format - Updates
`docs.yml`

from`main`

**while preserving the versions array**from`docs-website`

(uses`yq`

to save/restore the versions list) - Commits and pushes to
`docs-website`

- Publishes to Fern via
`fern generate --docs`


#### Job 3: Version Release (tags)

**Triggers:** New Git tags matching `vX.Y.Z`

(e.g., `v0.9.0`

, `v1.0.0`

), or
manual `workflow_dispatch`

with a tag specified.

**Steps:**

- Validates tag format (must be exactly
`vX.Y.Z`

, no suffixes like`-rc1`

) - Checks that the version doesn’t already exist (no duplicate snapshots)
- Creates
`fern/pages-vX.Y.Z/`

by copying`fern/pages/`

- Rewrites GitHub links in the snapshot:
`github.com/ai-dynamo/dynamo/tree/v1.2.1`

→`tree/vX.Y.Z`

`github.com/ai-dynamo/dynamo/blob/v1.2.1`

→`blob/vX.Y.Z`


- Runs
`convert_callouts.py`

on the snapshot - Creates
`fern/versions/vX.Y.Z.yml`

from`dev.yml`

with paths updated to`../pages-vX.Y.Z/`

- Updates
`fern/docs.yml`

:- Inserts new version right after the “dev” entry
- Sets the product’s default
`path`

to the new version - Updates the “Latest” display-name to
`"Latest (vX.Y.Z)"`


- Commits and pushes to
`docs-website`

- Publishes to Fern via
`fern generate --docs`


**Anti-recursion note:** Pushes made with `GITHUB_TOKEN`

do not trigger other
workflows (GitHub’s built-in guard). This is why the publish step is inline in
each job rather than in a separate workflow.

### Docs Link Check Workflow (`docs-link-check.yml`

)

**Location:** `.github/workflows/docs-link-check.yml`


**Triggers:** Push to `main`

and pull requests.

Runs two independent link-checking jobs:

## Content Authoring

### Writing docs on `main`


- Edit or add markdown files in
`docs/`

. - If adding a new page, add an entry in
`docs/index.yml`

to make it appear in the sidebar navigation. - Use standard GitHub-flavored markdown. Callouts (admonitions) should use
GitHub’s native syntax — they are automatically converted during sync:
- Open a PR. The lint jobs (
`fern check`

,`fern docs broken-links`

, lychee, broken-links-check) run automatically. - Once merged to
`main`

, the sync-dev workflow publishes changes within minutes.

### Assets and images

Place images in `docs/assets/`

and reference them with relative paths from your
markdown files:

### Custom components

React components in `fern/components/`

can be used in markdown via MDX. The
`CustomFooter.tsx`

renders the NVIDIA footer with legal links and branding.

## Callout Conversion

The `fern/convert_callouts.py`

script bridges the gap between GitHub-flavored
markdown and Fern’s admonition format. This lets authors use GitHub’s native
callout syntax on `main`

while Fern gets its required component format.

### Mapping

### Usage

The conversion happens automatically during the sync-dev and release-version workflows. Authors never need to run it manually.

## Running Locally

You can preview the documentation site on your machine using the
[Fern CLI](https://buildwithfern.com/learn/cli-api/overview). This is useful
for verifying layout, navigation, and content before opening a PR.

### Prerequisites

Install the Fern CLI globally via npm:

### Validate configuration

Run `fern check`

from the repo root to validate that `fern/docs.yml`

,
`fern/fern.config.json`

, and the navigation files are syntactically correct:

### Check for broken links

Use `fern docs broken-links`

to scan all pages for internal links that don’t
resolve:

This is the same check that runs in CI on every pull request.

### Start a local preview server

Run `fern docs dev`

to build the site and serve it locally with hot-reload:

The local server lets you see exactly how pages will look on the live site, including navigation, version dropdowns, and custom styling.

## Version Management

### How versions work

The Fern site supports a version dropdown in the UI. Each version is defined by:

**A navigation file**(`fern/versions/vX.Y.Z.yml`

) — sidebar structure pointing to version-specific pages (on the`docs-website`

branch).**A pages directory**(`fern/pages-vX.Y.Z/`

) — frozen snapshot of the markdown content at release time (on the`docs-website`

branch).**An entry in**— tells Fern about the version’s display name, slug, and config path.`fern/docs.yml`


### Version types

### URL structure

**Latest (default):**`docs.nvidia.com/dynamo/`

**Specific version:**`docs.nvidia.com/dynamo/v0.8.1/`

**Dev:**`docs.nvidia.com/dynamo/dev/`


### Creating a new version

Simply push a semver tag:

The `release-version`

job in `fern-docs.yml`

handles everything else
automatically.

## How Publishing Works

### Secrets

## Common Tasks

### Update existing documentation

- Edit files in
`docs/`

on a feature branch. - If adding a new page, add its entry in
`docs/index.yml`

. - Open a PR — linting runs automatically.
- Merge — sync + publish happens automatically.

### Add a new top-level section

- Create a directory under
`docs/`

(e.g.,`docs/new-section/`

). - Add markdown files for each page.
- Add a new
`- section:`

block in`docs/index.yml`

with the desired hierarchy.

### Release versioned documentation

That’s it. The workflow snapshots the current dev docs, creates the version config, and publishes.

### Manually trigger a sync or release

Go to **Actions → Fern Docs → Run workflow**:

- Leave
**tag**empty to trigger a dev sync. - Enter a tag (e.g.,
`v0.9.0`

) to trigger a version release.

### Debug a failed publish

- Check the
**Actions**tab for the failed`Fern Docs`

workflow run. - Common issues:
**Broken links:**Fix the links flagged by`fern docs broken-links`

.**Invalid YAML:**Check`fern/docs.yml`

or`docs/index.yml`

syntax.**Expired**Rotate the token in repo secrets.`FERN_TOKEN`

:**Duplicate version:**The tag was already released; check`docs-website`

for existing`fern/pages-vX.Y.Z/`

directory.