source: https://github.com/vllm-project/guidellm/releases/tag/v0.5.2

# GuideLLM v0.5.2

## Overview

GuideLLM v0.5.2 continues to fix bugs and reintroduce features dropped in v0.4.0.

To get started, install with:

`pip install guidellm[recommended]==0.5.2`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.5.2`

## What's Changed

- Support for passing an API key has been reintroduced. API keys can be set with the argument
`--backend-kwargs '{"api_key": "KEY"}'`

. - Console output now uses the "total" requests category rather then just "successful". See
[#529](https://github.com/vllm-project/guidellm/issues/529)for more details.

## What's Fixed

- Fixed a deadlock that could occur on benchmark start which could significantly delay the first request send.
- Fixed formatting of image and video URLs. The previous version worked with vLLM but was not OpenAI-API compliant.

## Compatibility Notes

**Python**: 3.10–3.13**OS**: Linux, MacOS

## Changelog

### Bug fixes

- Make image_url/video_url send dictionaries by
[@Vinno97](https://github.com/Vinno97)in[#525](https://github.com/vllm-project/guidellm/pull/525) - Fix strategy initialization deadlock by
[@sjmonson](https://github.com/sjmonson)in[#528](https://github.com/vllm-project/guidellm/pull/528)

### Features

- Use total requests for throughput calculation by
[@sjmonson](https://github.com/sjmonson)in[#530](https://github.com/vllm-project/guidellm/pull/530) - Added option to log errors from backends by
[@jaredoconnell](https://github.com/jaredoconnell)in[#534](https://github.com/vllm-project/guidellm/pull/534) - OpenAI API-Key Support by
[@jaredoconnell](https://github.com/jaredoconnell)in[#535](https://github.com/vllm-project/guidellm/pull/535)

### Documentation

- Fix some outdated docs examples by
[@sjmonson](https://github.com/sjmonson)in[#531](https://github.com/vllm-project/guidellm/pull/531) - docs: update link for vllm simulator by
[@maryamtahhan](https://github.com/maryamtahhan)in[#532](https://github.com/vllm-project/guidellm/pull/532)

## New Contributors

**Full Changelog**: `v0.5.1...v0.5.2`