source: https://github.com/vllm-project/guidellm/releases/tag/v0.6.0

# GuideLLM v0.6.0

[dbutenhof](https://github.com/dbutenhof)released this

·

[400 commits](https://github.com/vllm-project/guidellm/compare/v0.6.0...main)to main since this release
Immutable
release. Only release title and notes can be modified.

## Overview

GuideLLM v0.6.0 is a feature release adding multi-turn, Responses API, GeoSpatial model support, and in-process vLLM Python backend along with bug fixes.

To get started, install with:

`pip install guidellm[recommended]==0.6.0`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.6.0`

## Compatibility Notes

**Python**: 3.10–3.13**OS**: Linux, MacOS

## What's New:

- Added basic Responses API support: tool calling support will be added later
- Added multi-turn support for both datasets and synthetic data
- Added vLLM Python (in-process) backend
- Added TerraTorch GeoSpacial model support

## What's Fixed:

- Allow disabling vLLM-specific body options in HTTP backend
- Fix
`--sample-requests`

to limit sampling in output - Fix HTML references in html report
- Fixed container image HOME permissions for OpenShift

## Change Log

### Features

- Instant ttft oversaturation by
[@ushaket](https://github.com/ushaket)in[#607](https://github.com/vllm-project/guidellm/pull/607) - vLLM Python Backend by
[@jaredoconnell](https://github.com/jaredoconnell)in[#596](https://github.com/vllm-project/guidellm/pull/596) - Multiturn Benchmarking by
[@sjmonson](https://github.com/sjmonson)in[#590](https://github.com/vllm-project/guidellm/pull/590) - Add turn and conversation trackers to the request by
[@sjmonson](https://github.com/sjmonson)in[#649](https://github.com/vllm-project/guidellm/pull/649) - Basic Responses API Support by
[@jaredoconnell](https://github.com/jaredoconnell)in[#655](https://github.com/vllm-project/guidellm/pull/655) - Add support for TerraTorch Geospatial models served via the vLLM /pooling endpoint by
[@mgazz](https://github.com/mgazz)in[#610](https://github.com/vllm-project/guidellm/pull/610)

### Internal refactoring & cleanup

- Fix and improve the mock server by
[@jaredoconnell](https://github.com/jaredoconnell)in[#640](https://github.com/vllm-project/guidellm/pull/640) - Import utils from sub-submodules by
[@sjmonson](https://github.com/sjmonson)in[#644](https://github.com/vllm-project/guidellm/pull/644) - Move request formatting to backend by
[@sjmonson](https://github.com/sjmonson)in[#478](https://github.com/vllm-project/guidellm/pull/478) - Drop median from throughput metrics in console by
[@sjmonson](https://github.com/sjmonson)in[#617](https://github.com/vllm-project/guidellm/pull/617) - Fix HTML on main and disable by default by
[@sjmonson](https://github.com/sjmonson)in[#638](https://github.com/vllm-project/guidellm/pull/638) - Drop vLLM extras group by
[@sjmonson](https://github.com/sjmonson)in[#635](https://github.com/vllm-project/guidellm/pull/635) - Improve environment variables warning and validation cleanup by
[@sjmonson](https://github.com/sjmonson)in[#654](https://github.com/vllm-project/guidellm/pull/654) - Pass mp context to strategy by
[@sjmonson](https://github.com/sjmonson)in[#651](https://github.com/vllm-project/guidellm/pull/651) - Cleanup
**init**by[@sjmonson](https://github.com/sjmonson)in[#647](https://github.com/vllm-project/guidellm/pull/647)

### Fixes

- fix(cli): validate --output-path against --output-dir by
[@aiwantaozi](https://github.com/aiwantaozi)in[#561](https://github.com/vllm-project/guidellm/pull/561) - Fix the guidellm benchmark --sample-requests command line option by
[@natoscott](https://github.com/natoscott)in[#591](https://github.com/vllm-project/guidellm/pull/591) - Drop various depricated settings and remove the default OpenAI request timeout by
[@sjmonson](https://github.com/sjmonson)in[#589](https://github.com/vllm-project/guidellm/pull/589) - Fix /v1/chat/completions formatting by
[@sjmonson](https://github.com/sjmonson)in[#595](https://github.com/vllm-project/guidellm/pull/595) - Containerfile: ensure that HOME can be used by any user ID by
[@kpouget](https://github.com/kpouget)in[#601](https://github.com/vllm-project/guidellm/pull/601) - Fix JSON serialization for binary request payloads via base64 bytes config by
[@ushaket](https://github.com/ushaket)in[#612](https://github.com/vllm-project/guidellm/pull/612) - Move html template source location to raw github by
[@sjmonson](https://github.com/sjmonson)in[#629](https://github.com/vllm-project/guidellm/pull/629) - Fix file extension not being sent to output handler by
[@jaredoconnell](https://github.com/jaredoconnell)in[#639](https://github.com/vllm-project/guidellm/pull/639) - Check if deserialization path is vaild safely by
[@sjmonson](https://github.com/sjmonson)in[#659](https://github.com/vllm-project/guidellm/pull/659) - Support removing keys from HTTP request bodies by
[@sjmonson](https://github.com/sjmonson)in[#661](https://github.com/vllm-project/guidellm/pull/661) - Replace line iter with bytes to lines wrapper by
[@sjmonson](https://github.com/sjmonson)in[#663](https://github.com/vllm-project/guidellm/pull/663) - Revert back to iterating over lines by
[@sjmonson](https://github.com/sjmonson)in[#680](https://github.com/vllm-project/guidellm/pull/680)

### CI environment

- Fix multiple main CI failures by
[@sjmonson](https://github.com/sjmonson)in[#578](https://github.com/vllm-project/guidellm/pull/578) - Replace exisiting issue templates with form versions by
[@sjmonson](https://github.com/sjmonson)in[#586](https://github.com/vllm-project/guidellm/pull/586) - Add merge policies by
[@sjmonson](https://github.com/sjmonson)in[#630](https://github.com/vllm-project/guidellm/pull/630) - Run format job in CI by
[@sjmonson](https://github.com/sjmonson)in[#625](https://github.com/vllm-project/guidellm/pull/625) - Drop RC jobs and nightly PyPi publish by
[@sjmonson](https://github.com/sjmonson)in[#632](https://github.com/vllm-project/guidellm/pull/632) - Mark requeue test as xfail due to uvloop bug by
[@sjmonson](https://github.com/sjmonson)in[#652](https://github.com/vllm-project/guidellm/pull/652) - Lock all GitHub Actions to SHA by
[@dbutenhof](https://github.com/dbutenhof)in[#666](https://github.com/vllm-project/guidellm/pull/666) - Identify action versions by
[@dbutenhof](https://github.com/dbutenhof)in[#679](https://github.com/vllm-project/guidellm/pull/679) - Remove "uv" ecosystem from yaml by
[@dbutenhof](https://github.com/dbutenhof)in[#681](https://github.com/vllm-project/guidellm/pull/681)

### Documentation

- Add multimodal benchmarking usage docs by
[@markurtz](https://github.com/markurtz)in[#568](https://github.com/vllm-project/guidellm/pull/568) - Add data parameter to benchmark command in README by
[@S1ro1](https://github.com/S1ro1)in[#616](https://github.com/vllm-project/guidellm/pull/616) - Add detail in benchmark profile documentation by
[@dbutenhof](https://github.com/dbutenhof)in[#619](https://github.com/vllm-project/guidellm/pull/619) - docs: add documentation for passing sampling parameters via --backend-kwargs by
[@cemigo114](https://github.com/cemigo114)in[#626](https://github.com/vllm-project/guidellm/pull/626) - docs: Fixing a broken link of docs/guides/outputs.md. by
[@theodor2311](https://github.com/theodor2311)in[#642](https://github.com/vllm-project/guidellm/pull/642)

### Dependency updates

- Fixup pylock after dependabot PRs by
[@sjmonson](https://github.com/sjmonson)in[#553](https://github.com/vllm-project/guidellm/pull/553) - Fix for Dependabot action by
[@sjmonson](https://github.com/sjmonson)in[#554](https://github.com/vllm-project/guidellm/pull/554) - Drop pylock by
[@sjmonson](https://github.com/sjmonson)in[#555](https://github.com/vllm-project/guidellm/pull/555) - Bump virtualenv from 20.35.4 to 20.36.1 by
[@dependabot](https://github.com/dependabot)[bot] in[#544](https://github.com/vllm-project/guidellm/pull/544) - Bump urllib3 from 2.5.0 to 2.6.3 by
[@dependabot](https://github.com/dependabot)[bot] in[#545](https://github.com/vllm-project/guidellm/pull/545) - Bump aiohttp from 3.13.2 to 3.13.3 by
[@dependabot](https://github.com/dependabot)[bot] in[#547](https://github.com/vllm-project/guidellm/pull/547) - Bump protobuf from 6.33.1 to 6.33.5 by
[@dependabot](https://github.com/dependabot)[bot] in[#580](https://github.com/vllm-project/guidellm/pull/580) - Bump pillow from 12.0.0 to 12.1.1 by
[@dependabot](https://github.com/dependabot)[bot] in[#593](https://github.com/vllm-project/guidellm/pull/593) - Bump torchcodec (and torch) by
[@sjmonson](https://github.com/sjmonson)in[#614](https://github.com/vllm-project/guidellm/pull/614) - Bump transformers version in lock by
[@sjmonson](https://github.com/sjmonson)in[#628](https://github.com/vllm-project/guidellm/pull/628) - Bump orjson from 3.11.4 to 3.11.6 by
[@dependabot](https://github.com/dependabot)[bot] in[#631](https://github.com/vllm-project/guidellm/pull/631) - Bump ujson from 5.11.0 to 5.12.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#643](https://github.com/vllm-project/guidellm/pull/643) - Require datasets 4.1.0 by
[@dbutenhof](https://github.com/dbutenhof)in[#650](https://github.com/vllm-project/guidellm/pull/650) - Bump requests from 2.32.5 to 2.33.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#657](https://github.com/vllm-project/guidellm/pull/657)

## New Contributors

[@aiwantaozi](https://github.com/aiwantaozi)made their first contribution in[#561](https://github.com/vllm-project/guidellm/pull/561)[@kpouget](https://github.com/kpouget)made their first contribution in[#601](https://github.com/vllm-project/guidellm/pull/601)[@ushaket](https://github.com/ushaket)made their first contribution in[#612](https://github.com/vllm-project/guidellm/pull/612)[@S1ro1](https://github.com/S1ro1)made their first contribution in[#616](https://github.com/vllm-project/guidellm/pull/616)[@dbutenhof](https://github.com/dbutenhof)made their first contribution in[#619](https://github.com/vllm-project/guidellm/pull/619)[@cemigo114](https://github.com/cemigo114)made their first contribution in[#626](https://github.com/vllm-project/guidellm/pull/626)[@theodor2311](https://github.com/theodor2311)made their first contribution in[#642](https://github.com/vllm-project/guidellm/pull/642)[@mgazz](https://github.com/mgazz)made their first contribution in[#610](https://github.com/vllm-project/guidellm/pull/610)

**Full Changelog**: `v0.5.3...v0.6.0`