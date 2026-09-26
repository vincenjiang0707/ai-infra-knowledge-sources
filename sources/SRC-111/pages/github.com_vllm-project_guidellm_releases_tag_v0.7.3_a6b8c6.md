source: https://github.com/vllm-project/guidellm/releases/tag/v0.7.3

# GuideLLM v0.7.3

[dbutenhof](https://github.com/dbutenhof)released this

·

[82 commits](https://github.com/vllm-project/guidellm/compare/v0.7.3...main)to main since this release
Immutable
release. Only release title and notes can be modified.

## Overview

GuideLLM v0.7.3 is a minor release to resolve a dependency vulnerability but adds a few minor improvements.

To get started, install with:

`pip install guidellm[recommended]==0.7.3`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.7.3`

## What's Fixed

- Our
`transformers`

dependency was locked by transitive dependencies to <5.0 in RHAI downstream, resulting in CRITICAL/HIGH CVEs. This release resolves the transitive dependency (through`huggingface_hub`

) by updating to click 8.4. - The
`--output kind=plot`

command is now documented, and has been updated to use`GUIDELLM_DEFAULT_RESULTS_DIR`

. - A minor improvement reports unusable LLM responses more gracefully.

## What's Changed

### Features

- bug(openai): support structured chat content metadata for OpenAI backend endpoint by
[@Prasannajaga](https://github.com/Prasannajaga)in[#947](https://github.com/vllm-project/guidellm/pull/947)

### Bug fixes

- Fix worker status for unusable terminal backend responses by
[@ushaket](https://github.com/ushaket)in[#615](https://github.com/vllm-project/guidellm/pull/615) - Make plot path behave like others by
[@dbutenhof](https://github.com/dbutenhof)in[#974](https://github.com/vllm-project/guidellm/pull/974)

### Documentation

- docs: document the plot output kind by
[@Pragadeesh122](https://github.com/Pragadeesh122)in[#971](https://github.com/vllm-project/guidellm/pull/971)

### CI environment

- Add py.typed marker for PEP 561 compliance by
[@arijitroy003](https://github.com/arijitroy003)in[#951](https://github.com/vllm-project/guidellm/pull/951) - Prevent .env files from tainting tests by
[@jaredoconnell](https://github.com/jaredoconnell)in[#970](https://github.com/vllm-project/guidellm/pull/970)

### Dependency updates

- [GitHub Actions]: Bump actions/checkout from 7.0.0 to 7.0.1 by
[@dependabot](https://github.com/dependabot)[bot] in[#956](https://github.com/vllm-project/guidellm/pull/956) - Bump urllib3 from 2.6.3 to 2.7.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#962](https://github.com/vllm-project/guidellm/pull/962) - [GitHub Actions]: Bump redhat-actions/podman-login from 1.7 to 2.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#977](https://github.com/vllm-project/guidellm/pull/977) - Update click to 8.4 by
[@dbutenhof](https://github.com/dbutenhof)in[#978](https://github.com/vllm-project/guidellm/pull/978)

**Full Changelog**: `v0.7.2...v0.7.3`