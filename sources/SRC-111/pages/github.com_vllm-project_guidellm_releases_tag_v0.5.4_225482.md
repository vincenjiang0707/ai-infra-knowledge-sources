source: https://github.com/vllm-project/guidellm/releases/tag/v0.5.4

# GuideLLM v0.5.4

## Overview

GuideLLM v0.5.4 is a hotfix patch recommended to all GuideLLM users.

To get started, install with:

`pip install guidellm[recommended]==0.5.4`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.5.4`

## What's Fixed

`--sample-requests`

should now function correctly- Bump
`transformers`

package in lockfile to support mistral model tokenizers - Update HTML report to pull its template from
`raw.githubusercontent.com`

rather than`blog.vllm.ai`

**Critical:**This issue would cause crashes when the HTML report was enabled


## Compatibility Notes

**Python**: 3.10–3.13**OS**: Linux, MacOS

## Changelog

### Bug fixes

- Fix the guidellm benchmark --sample-requests command line option by
[@sjmonson](https://github.com/sjmonson)in[#591](https://github.com/vllm-project/guidellm/pull/591) - Bump transformers version in lock by
[@sjmonson](https://github.com/sjmonson)in[#628](https://github.com/vllm-project/guidellm/pull/628) - Move html template source location to raw github by
[@sjmonson](https://github.com/sjmonson)in[#629](https://github.com/vllm-project/guidellm/pull/629)

**Full Changelog**: `v0.5.3...v0.5.4`