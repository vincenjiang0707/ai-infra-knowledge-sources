source: https://github.com/vllm-project/guidellm/releases/tag/v0.5.3

# GuideLLM v0.5.3

## Overview

GuideLLM v0.5.3 is a very small patch focused on enabling mistral3 model tokenizers.

To get started, install with:

`pip install guidellm[recommended]==0.5.3`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.5.3`

## What's Changed

- Constant rate-type benchmarks now support the
`--rampup`

feature which ramps up the give rate linearly. - Added
`mistral-common`

as a optional dependency to enable loading mistral3 based tokenizers.- NOTE: Loading the mistral tokenizer also requires
`transformers>=5.0.0`

.

- NOTE: Loading the mistral tokenizer also requires

## Compatibility Notes

**Python**: 3.10–3.13**OS**: Linux, MacOS

## Changelog

### Bug fixes

### Features

- Add Mistral tokenizer as optional dependency by
[@sjmonson](https://github.com/sjmonson)in[#541](https://github.com/vllm-project/guidellm/pull/541) - Added rampup to constant rate type by
[@jaredoconnell](https://github.com/jaredoconnell)in[#549](https://github.com/vllm-project/guidellm/pull/549)

### Documentation

- Add documentation how to use with llama.cpp by
[@rgerganov](https://github.com/rgerganov)in[#536](https://github.com/vllm-project/guidellm/pull/536)

**Full Changelog**: `v0.5.2...v0.5.3`