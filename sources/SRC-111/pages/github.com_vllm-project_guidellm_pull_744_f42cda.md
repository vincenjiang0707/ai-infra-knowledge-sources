source: https://github.com/vllm-project/guidellm/pull/744

# Fix blank HTML report by serving UI assets from GitHub Pages - #744

[jaredoconnell](https://github.com/jaredoconnell)merged 1 commit into

[jaredoconnell](https://github.com/jaredoconnell) merged 1 commit into

[jaredoconnell](https://github.com/jaredoconnell)merged 1 commit into

## Conversation

|
Thanks for the contribution! Please fix the CI failure above then I think this is good to go. I didn't realize the vLLM project was still publishing to their |

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Thanks for the fix. Please reformat the file as indicated by the CI failure, and rebase. Once that passes this will be ready to merge.

…hubusercontent The generated HTML benchmark report loads its JS bundle from `raw.githubusercontent.com`, which serves files as `text/plain` with `X-Content-Type-Options: nosniff`. Browsers therefore refuse to execute the scripts (and the webpack runtime's `publicPath` makes dynamically imported chunks fail the same way), so opening the report shows a blank page even though the benchmark data is embedded in the HTML. The same `gh-pages` branch is already published via GitHub Pages at `[https://vllm-project.github.io/guidellm/`], which serves the identical files with the correct `application/javascript` MIME type. Point the report source and the UI build `ASSET_PREFIX` at the Pages URL instead. This regressed in[, which moved hosting off the (now retired) `blog.vllm.ai` Pages site to the raw.githubusercontent URL. Generated-by: Claude Code (claude-opus-4-7) Signed-off-by: sund4y <sund4y1123@gmail.com>]23e9af7

[regrow1123](https://github.com/regrow1123)

[force-pushed](https://github.com/vllm-project/guidellm/compare/b5d93843095b05f9d993bb78b9af62d429769743..dd92b133973eaa3bd78a8cd6f19839c8050ad13d)the fix/html-report-asset-host-github-pages branch from

[to](https://github.com/vllm-project/guidellm/commit/b5d93843095b05f9d993bb78b9af62d429769743)

`b5d9384`


`dd92b13`

[Compare](https://github.com/vllm-project/guidellm/compare/b5d93843095b05f9d993bb78b9af62d429769743..dd92b133973eaa3bd78a8cd6f19839c8050ad13d)

May 26, 2026 22:20

|
Thanks both! Fixed the
|

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

The generated HTML benchmark report renders as a blank page when opened in a browser, even though the benchmark data is embedded in the file. The report's JS bundle is loaded from

`raw.githubusercontent.com`

, which serves every file as`Content-Type: text/plain`

with`X-Content-Type-Options: nosniff`

. Browsers refuse to execute scripts under those headers, so the UI never mounts. The webpack runtime's baked-in`publicPath`

also points at`raw.githubusercontent.com`

, so dynamically-imported chunks fail the same way.The exact same

`gh-pages`

branch is already published via GitHub Pages at`https://vllm-project.github.io/guidellm/`

, which serves the identical files with the correct`application/javascript`

MIME type and no`nosniff`

block. This PR points the report source and the UI build`ASSET_PREFIX`

at the Pages URL instead of the raw URL.This regressed in

23e9af7("Move html template source location to raw github"), which moved hosting off the now-retired`blog.vllm.ai`

Pages site (it now 301-redirects to a Vercel-hosted blog) onto the raw.githubusercontent URL.## Details

`src/guidellm/settings.py`

: report`source`

→`vllm-project.github.io`

`src/ui/.env.production`

,`.env.staging`

,`.env.development`

:`ASSET_PREFIX`

→`vllm-project.github.io`

`tests/unit/test_settings.py`

: update expected`BASE_URL`

prefixHost swap only; paths/versions are unchanged. All four target URLs (

`ui/v0.5.4/index.html`

,`ui/latest`

,`ui/dev`

,`ui/release/latest`

) were verified to return`200`

with`content-type: application/javascript`

on the Pages host.## Test Plan

`pytest tests/unit/test_settings.py`

— passes (10/10).`text/plain`

+`nosniff`

); after repointing assets to the Pages host the report renders fully (charts + statistics tables).`application/javascript`

MIME for both the bootstrap chunks and the dynamically-loaded chunks (`d55cc8df.*`

,`652.*`

) on the Pages host.## Related Issues

## Use of AI

🤖 Generated with Claude Code