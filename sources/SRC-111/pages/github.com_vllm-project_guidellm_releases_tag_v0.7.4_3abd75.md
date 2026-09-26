source: https://github.com/vllm-project/guidellm/releases/tag/v0.7.4

[sjmonson](https://github.com/sjmonson)released this

·

[82 commits](https://github.com/vllm-project/guidellm/compare/v0.7.4...main)to main since this release
Immutable
release. Only release title and notes can be modified.

## Overview

GuideLLM v0.7.4 is a minor release which backports many bugfixes including a change to how token metrics interact with warmup/cooldown. This change will cause differences in which requests are sampled for latency metrics and will bound token event to only the tokens that occur outside warmup/cooldown.

To get started, install with:

`pip install guidellm[recommended]==0.7.4`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.7.4`

## What's Fixed

- Change to the methodology around tracking token latency and throughput events. See
[#1078](https://github.com/vllm-project/guidellm/issues/1078)for full details of the problem.

## What's Changed

### Bug fixes

- Bound token events by when they occur in
[#1079](https://github.com/vllm-project/guidellm/pull/1079) - fix(openai): validate non-streaming tool calls before yielding in
[#1099](https://github.com/vllm-project/guidellm/pull/1099) - fix(openai): surface nested Responses streaming errors in
[#1107](https://github.com/vllm-project/guidellm/pull/1107) - fix(openai): accept SSE DONE markers without a space in
[#1106](https://github.com/vllm-project/guidellm/pull/1106) - fix: serialize audio translation filename in
[#1096](https://github.com/vllm-project/guidellm/pull/1096) - Pull pending requests into a worker only when a consumer is waiting in
[#1042](https://github.com/vllm-project/guidellm/pull/1042) - fix: use spawn multiprocessing context on macOS in
[#1026](https://github.com/vllm-project/guidellm/pull/1026) - Fix encoded audio sample frame metrics in
[#987](https://github.com/vllm-project/guidellm/pull/987) - Fix non-streaming audio response parsing in
[#981](https://github.com/vllm-project/guidellm/pull/981) - Fix multipart filenames for audio uploads in
[#990](https://github.com/vllm-project/guidellm/pull/990)

### CI environment

- [GitHub Actions]: Bump docker/setup-qemu-action from 4.2.0 to 4.3.0 in
[#1129](https://github.com/vllm-project/guidellm/pull/1129) - [GitHub Actions]: Bump redhat-actions/buildah-build from 3.0.2 to 3.1.0 in
[#1062](https://github.com/vllm-project/guidellm/pull/1062) - [GitHub Actions]: Bump redhat-actions/buildah-build from 2.13 to 3 in
[#1036](https://github.com/vllm-project/guidellm/pull/1036) - [GitHub Actions]: Bump redhat-actions/push-to-registry from 2.8 to 3 in
[#1037](https://github.com/vllm-project/guidellm/pull/1037) - fix: keep GHCR latest/stable as multi-arch manifests in
[#1018](https://github.com/vllm-project/guidellm/pull/1018)

### Dependency updates

- build(deps): Bump transformers from 5.5.0 to 5.10.1 in
[#1076](https://github.com/vllm-project/guidellm/pull/1076) - Bump h2 from 4.3.0 to 4.4.1 in
[#1011](https://github.com/vllm-project/guidellm/pull/1011) - Bump aiohttp from 3.14.1 to 3.14.3 in
[#995](https://github.com/vllm-project/guidellm/pull/995)

**Full Changelog**: `v0.7.3...v0.7.4`