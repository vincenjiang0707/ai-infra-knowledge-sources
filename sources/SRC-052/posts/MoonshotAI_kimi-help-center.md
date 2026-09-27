# MoonshotAI/kimi-help-center

source: https://github.com/MoonshotAI/kimi-help-center

# Kimi Help Center Docs

This repository stores the checked-in source content for the Kimi Help Center.
It contains locale-specific article trees and media assets, authored as
MDX-compatible Markdown.

## Repository Layout

```text
.
├── AGENTS.md
├── en-US/
└── zh-CN/
```

Content is organized by locale and category:

```text
<locale>/<category>/
├── _category.json
├── _category.png
├── article.md
└── images/<article>/...
```

Examples:

- `en-US/kimi-code/cli-getting-started.md`
- `en-US/kimi-code/images/cli-getting-started/screenshot-23.png`
- `zh-CN/deep-research/overview.md`

## What Belongs Here

- Public help center articles.
- Locale-specific category metadata and images.
- Article screenshots, illustrations, and other media assets.

## Authoring Rules

All authoring conventions for this repo live in [AGENTS.md](./AGENTS.md).

That includes:

- required front matter fields
- supported custom MDX components
- image placement conventions
- internal link conventions
- formatting constraints for MDX content

## Editing Guidance

- Keep articles MDX-compatible and simple.
- Do not add `import` statements in article files.
- Keep local assets under the matching category `images/` tree.
- Prefer updating existing slugs and routes carefully to avoid broken links.
- Follow the component and front matter rules in `AGENTS.md` before adding new
  content.

## Locales

- `en-US/` contains English help center content.
- `zh-CN/` contains Simplified Chinese help center content and is maintained
  manually, not by the machine translation helper.

## Setup Import Script

This repo includes a Node.js version of the help-center setup importer:

```bash
pnpm install
pnpm setup:docs:dry-run
```

To import into Postgres, provide the same DSN shape used by the API service:

```bash
DATABASE_URL="postgres://user:pass@localhost:5432/helpcenter?sslmode=disable" pnpm setup:docs
```

Local media can be uploaded to the CDN through Volcengine TOS, matching the
`landing-ui` upload path. Put credentials in an untracked `.env.local` file or
export them in your shell:

```bash
TOS_ACCESS_KEY_ID="..."
TOS_ACCESS_KEY_SECRET="..."
TOS_REGION="cn-beijing"
TOS_BUCKET="static-moonshot-cn"
CDN_PUBLIC_BASE="https://statics.kimi.ai"
CDN_PATH_PREFIX="kimi-helpcenter-doc/"
DATABASE_URL="postgres://user:pass@localhost:5432/helpcenter?sslmode=disable"
```

Then run:

```bash
pnpm exec node scripts/setup-docs.js \
  --upload-assets \
  .
```

Useful direct options:

- `node scripts/setup-docs.js --dry-run --locale zh-CN .`
- `node scripts/setup-docs.js --dsn "$DATABASE_URL" .`
- `node scripts/setup-docs.js --asset-url-prefix "https://static.example.com/help-docs" .`
- `node scripts/setup-docs.js --upload-assets --cdn-public-base "https://statics.kimi.ai" .`

## One-time Translation

The one-time translation helper has two maintained source locales:

- `en-US/` is the default source for overseas SEO-supported locales.
- `zh-CN/` is maintained manually for mainland China users and is the default
  source for `en-cn` / `en-CN`, the mainland China English locale.

`zh-CN/` is excluded as a machine translation target. Use `zh-SG/` for the
machine-translated overseas Simplified Chinese locale. Existing target files are
skipped unless `--overwrite` is passed.

```bash
TRANSLATION_API_KEY="..." pnpm translate:docs -- --target-locale ja-JP
```

Useful direct options:

- `node scripts/translate-docs.js --target-locale ja-JP --article en-US/agent/overview.md .`
- `node scripts/translate-docs.js --target-locale en-cn --article zh-CN/agent/overview.md .`
- `node scripts/translate-docs.js --all-seo-locales .`
- `node scripts/translate-docs.js --target-locale ja-JP --dry-run .`
- `node scripts/translate-docs.js --target-locale ja-JP --mock .`

The script uses an OpenAI-compatible `/chat/completions` API directly. Defaults
are aligned with Sagan's Weaver translation template:
`TRANSLATION_BASE_URL=https://openai.app.msh.team/v1`,
`TRANSLATION_MODEL=gpt-5.5`, `TRANSLATION_TEMPERATURE=0.6`, and
`TRANSLATION_THINKING=none`. Sagan's Weaver template sets `thinking: disabled`,
but Sagan skips the OpenAI thinking parameter for the `qianxun-openai` provider;
the direct script follows that behavior by default. Configure those environment
variables, or pass `--base-url`, `--api-key`, `--model`, `--temperature`, and
`--thinking` directly. `temperature` is omitted automatically for
`claude-opus-4-8`; use `--temperature none` to omit it explicitly. For full
runs, tune throughput with `TRANSLATION_CONCURRENCY` / `--concurrency` and
`TRANSLATION_MAX_RETRIES` / `--max-retries`; pass `--max-retries 0` to disable
request retries.

## GitLab CI

The pipeline validates docs first, then deploys to test automatically, then
offers a manual production deployment after test succeeds.

Create separate GitLab CI/CD variables so sensitive values can be masked and
hidden:

```bash
DATABASE_URL
TOS_ACCESS_KEY_ID
TOS_ACCESS_KEY_SECRET
TOS_REGION
TOS_BUCKET
CDN_PUBLIC_BASE
CDN_PATH_PREFIX
```

Use GitLab environment scopes to give test and production different values,
for example scope test values to `test` and production values to `production`.
`CDN_PATH_PREFIX` is optional; the script defaults to `kimi-helpcenter-doc/`.

