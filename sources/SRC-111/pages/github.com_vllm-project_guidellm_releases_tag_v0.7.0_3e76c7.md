source: https://github.com/vllm-project/guidellm/releases/tag/v0.7.0

# GuideLLM v0.7.0

[dbutenhof](https://github.com/dbutenhof)released this

·

[131 commits](https://github.com/vllm-project/guidellm/compare/v0.7.0...main)to main since this release
Immutable
release. Only release title and notes can be modified.

## Overview

GuideLLM v0.7.0 improves how you configure and run benchmarks, adds production-realistic trace replay, and expands support for modern LLM workloads: reasoning models, tool calling, embeddings, and Mooncake traces.

To get started, install with:

`pip install guidellm\[recommended\]==0.7.0`

Or from source with:

`pip install 'guidellm\[recommended\] @ git+[https://github.com/vllm-project/guidellm.git'@v0.7.0](https://github.com/vllm-project/guidellm.git'@v0.7.0)`

## What's New

- Support for server-side conversation history in /v1/responses API
- Support for client and server side tool calling using /v1/chat/completions and /v1/responses APIs
- Websocket backend (openai_websocket) for realtime audio transcription
- vLLM Python backend (vllm_python) for running inference in the same process as GuideLLM using vLLM's python API (AsyncLLMEngine), without an HTTP server.
- Synthetic tool calling support in chat/completions and responses APIs
- Mooncake LLM trace replay
- Given a data file with timestamps and
`prompt_tokens`

/`output_tokens`

synthetic data parameters, you can replay a recorded session. Mooncake provides KV cache replay using token cache block hash values which are used to compute tokens that replay a conversation with equivalent cache sensitivity, without recording or using the original data.

- Given a data file with timestamps and
- Support for testing OpenAI embeddings API
- Support for building ARM64 container images

### Major CLI refactoring

- Constraints (
`--max-requests`

,`--max-duration`

,`--max-errors`

, etc.) are now treated as first class objects using the consistent syntax`--constraint kind=<name>,<OPTIONS>...`

, such as`--constraint kind=max_requests,count=1000`

or`--constraint kind=over_saturation,mode=enforce,moe_threshold=3.0`

- The
`--data`

handling was overloaded, often with no clear way to determine what sort of data was to be loaded – for example, a huggingface dataset vs a local file. Error messages are often unclear, because the engine searched through a list of possibilities with no way to know which was expected to succeed. Now “data” is clearly typed, like`--data kind=huggingface,source=<name>`

or`--data kind=json_file,path=<path>`

- Specification of profiles and backends are now clearly typed, with clearly connected parameters, like
`--backend kind=openai_http,target=<url>,streaming=true`

and`--profile async ‘{“rate”:[10,20]}’`

- The syntax is designed to allow pre-loading layered “config” files like the previous
`--scenario <file>`

, also allowing overrides to the scenario/global values. This will enable the long-requested feature of being able to override constraints for each benchmark (“strategy”) scheduled under a profile. For example,`--profile kind=async,rate=10`

schedules one asynchronous strategy with rate 10, but specifying multiple rates requires using inline JSON to specify a list. Instead, you can define the rates with`–profile kind=async --override profile.rate=10,20`

you can run two rates.

## CLI Migration Guide

Read on GitHub at [v0.7.0 Migration Guide](https://vllm-project.github.io/guidellm/0.7.0/guides/v0.7.0_migration_guide/)

## What's Fixed

- Several fixes for the HTML report output rendering. (Future plans include making the HTML report format completely self-contained to eliminate many problems.)
- Improved handling of audio file format – preserve original format if possible, and when transcoding is necessary default to WAV rather than MP3
- Improved reporting of TTFT, especially when reasoning models first generate “non-output” thinking tokens
- Several fixes in dataset column mapping, including fast failure when there are no mappable columns

## Known Limitations

- Tool call responses are currently added to the following user turn. The following release will separate them into dedicated response turns.

## Changelog

### Features

- Process tool call requests for chat completions API by
[@jaredoconnell](https://github.com/jaredoconnell)in[#687](https://github.com/vllm-project/guidellm/pull/687) - Apply tool calling stats to the responses API by
[@jaredoconnell](https://github.com/jaredoconnell)in[#692](https://github.com/vllm-project/guidellm/pull/692) - Support server-side conversation history on responses API by
[@jaredoconnell](https://github.com/jaredoconnell)in[#697](https://github.com/vllm-project/guidellm/pull/697) - feat: Add embeddings endpoint support (MVP) by
[@maryamtahhan](https://github.com/maryamtahhan)in[#710](https://github.com/vllm-project/guidellm/pull/710) - [v0.7 CLI Refactor] Rework BackendArgs to be the authoritative config location by
[@sjmonson](https://github.com/sjmonson)in[#723](https://github.com/vllm-project/guidellm/pull/723) - [FEAT] Add replay from trace strategy by
[@VincentG1234](https://github.com/VincentG1234)in[#620](https://github.com/vllm-project/guidellm/pull/620) - Multi-turn tool call chat completions conversations by
[@jaredoconnell](https://github.com/jaredoconnell)in[#712](https://github.com/vllm-project/guidellm/pull/712) - Add multi-arch (x86, arm) container image support by
[@maryamtahhan](https://github.com/maryamtahhan)in[#720](https://github.com/vllm-project/guidellm/pull/720) - [v0.7 CLI Refactor] Rework Data Deserialization Config by
[@sjmonson](https://github.com/sjmonson)in[#733](https://github.com/vllm-project/guidellm/pull/733) - Feat/multi turn tools responses by
[@jaredoconnell](https://github.com/jaredoconnell)in[#739](https://github.com/vllm-project/guidellm/pull/739) - [v0.7 CLI Refactor] Finish up data rework by
[@sjmonson](https://github.com/sjmonson)in[#754](https://github.com/vllm-project/guidellm/pull/754) - CLI profile refactor by
[@dbutenhof](https://github.com/dbutenhof)in[#753](https://github.com/vllm-project/guidellm/pull/753) - Add lazy-loading for extras packages by
[@sjmonson](https://github.com/sjmonson)in[#641](https://github.com/vllm-project/guidellm/pull/641) - Constraints refactor by
[@jaredoconnell](https://github.com/jaredoconnell)in[#786](https://github.com/vllm-project/guidellm/pull/786) - Add Mooncake trace format support by
[@SkiHatDuckie](https://github.com/SkiHatDuckie)in[#777](https://github.com/vllm-project/guidellm/pull/777) - Infer audio encoding format from source instead of defaulting to MP3 by
[@jaredoconnell](https://github.com/jaredoconnell)in[#794](https://github.com/vllm-project/guidellm/pull/794) - [v0.7 CLI Refactor] New internal top-level args / CLI by
[@sjmonson](https://github.com/sjmonson)in[#789](https://github.com/vllm-project/guidellm/pull/789) - Simplify constraint parameter names by
[@dbutenhof](https://github.com/dbutenhof)in[#799](https://github.com/vllm-project/guidellm/pull/799) - Realtime transcription endpoint by
[@ushaket](https://github.com/ushaket)in[#713](https://github.com/vllm-project/guidellm/pull/713) - Revert Pydantic Registry parameters back to single value fields by
[@sjmonson](https://github.com/sjmonson)in[#826](https://github.com/vllm-project/guidellm/pull/826) - Restore startup logs and fix config environment variable support by
[@sjmonson](https://github.com/sjmonson)in[#825](https://github.com/vllm-project/guidellm/pull/825) - Improve Pydantic commenting by
[@dbutenhof](https://github.com/dbutenhof)in[#818](https://github.com/vllm-project/guidellm/pull/818) - Rename "config" CLI command to "env" by
[@jaredoconnell](https://github.com/jaredoconnell)in[#849](https://github.com/vllm-project/guidellm/pull/849) - Added registry setup for metrics, with accompanying CLI option by
[@jaredoconnell](https://github.com/jaredoconnell)in[#863](https://github.com/vllm-project/guidellm/pull/863) - Add
`--label`

argument by[@sjmonson](https://github.com/sjmonson)in[#846](https://github.com/vllm-project/guidellm/pull/846)

### Internal refactoring and cleanup

- Add AGENTS.md by
[@sjmonson](https://github.com/sjmonson)in[#714](https://github.com/vllm-project/guidellm/pull/714) - Refactor CSV tests by
[@jaredoconnell](https://github.com/jaredoconnell)in[#715](https://github.com/vllm-project/guidellm/pull/715) - Replace various key=value string parsers with a single utility by
[@sjmonson](https://github.com/sjmonson)in[#569](https://github.com/vllm-project/guidellm/pull/569) - Refactor CLI into nested structure by
[@sjmonson](https://github.com/sjmonson)in[#717](https://github.com/vllm-project/guidellm/pull/717) - Add instructions against common AI poor code quality habits by
[@jaredoconnell](https://github.com/jaredoconnell)in[#718](https://github.com/vllm-project/guidellm/pull/718) - Build ProfileArgs in BenchmarkGenerativeTextArgs by
[@dbutenhof](https://github.com/dbutenhof)in[#774](https://github.com/vllm-project/guidellm/pull/774) - [v0.7 CLI Refactor] Misc Cleanup by
[@sjmonson](https://github.com/sjmonson)in[#788](https://github.com/vllm-project/guidellm/pull/788) - Disable reloading parent schemas by default by
[@sjmonson](https://github.com/sjmonson)in[#805](https://github.com/vllm-project/guidellm/pull/805) - Switch BenchmarksArgs to BenchmarkScernario in output by
[@sjmonson](https://github.com/sjmonson)in[#816](https://github.com/vllm-project/guidellm/pull/816) - Remove "rate" as an alias for profile parameters by
[@dbutenhof](https://github.com/dbutenhof)in[#836](https://github.com/vllm-project/guidellm/pull/836) - Conversation extraction script for debugging by
[@jaredoconnell](https://github.com/jaredoconnell)in[#848](https://github.com/vllm-project/guidellm/pull/848)

### Bug fixes

- Add a health check for the worker processes by
[@jaredoconnell](https://github.com/jaredoconnell)in[#686](https://github.com/vllm-project/guidellm/pull/686) - Fix long import times due to processing all pydantic subclasses by
[@jaredoconnell](https://github.com/jaredoconnell)in[#689](https://github.com/vllm-project/guidellm/pull/689) - Fix custom column mapping by
[@sjmonson](https://github.com/sjmonson)in[#711](https://github.com/vllm-project/guidellm/pull/711) - Fix CSV column misalignment across multiple benchmarks by
[@leehyeoklee](https://github.com/leehyeoklee)in[#707](https://github.com/vllm-project/guidellm/pull/707) - Checks for no valid requests in processed dataset by
[@jaredoconnell](https://github.com/jaredoconnell)in[#709](https://github.com/vllm-project/guidellm/pull/709) - Fix TypeError when streaming delta has tool_calls=null by
[@rgerganov](https://github.com/rgerganov)in[#752](https://github.com/vllm-project/guidellm/pull/752) - Fix blank HTML report by serving UI assets from GitHub Pages by
[@regrow1123](https://github.com/regrow1123)in[#744](https://github.com/vllm-project/guidellm/pull/744) - Fix TTFT measurement for reasoning-capable models by
[@soyr-redhat](https://github.com/soyr-redhat)in[#742](https://github.com/vllm-project/guidellm/pull/742) - Make synthetic_text output_tokens optional and improve CLI errors by
[@rgerganov](https://github.com/rgerganov)in[#759](https://github.com/vllm-project/guidellm/pull/759) - Time to first output token and related fixes by
[@jaredoconnell](https://github.com/jaredoconnell)in[#760](https://github.com/vllm-project/guidellm/pull/760) - Enable multiprocessing support for trace replay strategy by
[@VincentG1234](https://github.com/VincentG1234)in[#745](https://github.com/vllm-project/guidellm/pull/745) - Fix unpicklable lambda collate_fn in TorchDataLoader for Python 3.14 by
[@rgerganov](https://github.com/rgerganov)in[#782](https://github.com/vllm-project/guidellm/pull/782) - Fix report serialization for nested paths by
[@sjh9714](https://github.com/sjh9714)in[#783](https://github.com/vllm-project/guidellm/pull/783) - fix(data): fail fast when no mappable columns are found (
[#787](https://github.com/vllm-project/guidellm/issues/787)) by[@Anai-Guo](https://github.com/Anai-Guo)in[#796](https://github.com/vllm-project/guidellm/pull/796) - fix(openai): surface streaming SSE error payloads as request failures (
[#743](https://github.com/vllm-project/guidellm/issues/743)) by[@Anai-Guo](https://github.com/Anai-Guo)in[#795](https://github.com/vllm-project/guidellm/pull/795) - fix(openai): recognize reasoning_content key for TTFT calculation by
[@rgerganov](https://github.com/rgerganov)in[#835](https://github.com/vllm-project/guidellm/pull/835) - Fix: Exclude computed fields during pydantic MP serialization by
[@SkiHatDuckie](https://github.com/SkiHatDuckie)in[#845](https://github.com/vllm-project/guidellm/pull/845) - Fix
`preprocess dataset`

by[@dbutenhof](https://github.com/dbutenhof)in[#842](https://github.com/vllm-project/guidellm/pull/842) - Fix: Add relative_timestamp column to output in Mooncake deserializer by
[@SkiHatDuckie](https://github.com/SkiHatDuckie)in[#855](https://github.com/vllm-project/guidellm/pull/855) - Misc v0.7.0 Fixes by
[@sjmonson](https://github.com/sjmonson)in[#843](https://github.com/vllm-project/guidellm/pull/843)

### CI environment

- Drop UI CI jobs by
[@sjmonson](https://github.com/sjmonson)in[#694](https://github.com/vllm-project/guidellm/pull/694) - Redrop nightly PyPi build by
[@sjmonson](https://github.com/sjmonson)in[#695](https://github.com/vllm-project/guidellm/pull/695) - [GitHub Actions]: Bump actions/cache from 5.0.4 to 5.0.5 by
[@dependabot](https://github.com/dependabot)[bot] in[#698](https://github.com/vllm-project/guidellm/pull/698) - [GitHub Actions]: Bump actions/upload-artifact from 7.0.0 to 7.0.1 by
[@dependabot](https://github.com/dependabot)[bot] in[#699](https://github.com/vllm-project/guidellm/pull/699) - Rename tox envs by
[@sjmonson](https://github.com/sjmonson)in[#701](https://github.com/vllm-project/guidellm/pull/701) - ci(mergify): upgrade configuration to current format by
[@mergify](https://github.com/mergify)[bot] in[#685](https://github.com/vllm-project/guidellm/pull/685) - Made E2E test theoretically run better in CI by
[@jaredoconnell](https://github.com/jaredoconnell)in[#738](https://github.com/vllm-project/guidellm/pull/738) - Run a useful set of tox environments by default by
[@sjmonson](https://github.com/sjmonson)in[#748](https://github.com/vllm-project/guidellm/pull/748) - Ensure system env vars don't taint tests by
[@jaredoconnell](https://github.com/jaredoconnell)in[#751](https://github.com/vllm-project/guidellm/pull/751) - feat: add automated docs deployment workflow by
[@1195343015](https://github.com/1195343015)in[#747](https://github.com/vllm-project/guidellm/pull/747) - Add a rebase + merge based merge queue by
[@sjmonson](https://github.com/sjmonson)in[#756](https://github.com/vllm-project/guidellm/pull/756) - fix mergify queue settings by
[@sjmonson](https://github.com/sjmonson)in[#757](https://github.com/vllm-project/guidellm/pull/757) - fix: fix docs deploy trigger and minor doc issues by
[@1195343015](https://github.com/1195343015)in[#758](https://github.com/vllm-project/guidellm/pull/758) - [GitHub Actions]: Bump docker/setup-qemu-action from 3.2.0 to 4.1.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#749](https://github.com/vllm-project/guidellm/pull/749) - Implement a Squash Commit PR Workflow by
[@sjmonson](https://github.com/sjmonson)in[#763](https://github.com/vllm-project/guidellm/pull/763) - Fix update-description job by
[@sjmonson](https://github.com/sjmonson)in[#766](https://github.com/vllm-project/guidellm/pull/766) - [GitHub Actions]: Bump docker/setup-buildx-action from 4.0.0 to 4.1.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#750](https://github.com/vllm-project/guidellm/pull/750) - [GitHub Actions]: Bump snok/container-retention-policy from 3.0.1 to 3.1.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#772](https://github.com/vllm-project/guidellm/pull/772) - [GitHub Actions]: Bump actions/checkout from 6.0.2 to 6.0.3 by
[@dependabot](https://github.com/dependabot)[bot] in[#773](https://github.com/vllm-project/guidellm/pull/773) - Force linux LF line endings by
[@dbutenhof](https://github.com/dbutenhof)in[#798](https://github.com/vllm-project/guidellm/pull/798) - Add a HuggingFace cache step to tox-run by
[@sjmonson](https://github.com/sjmonson)in[#806](https://github.com/vllm-project/guidellm/pull/806) - [GitHub Actions]: Bump actions/checkout from 6.0.3 to 7.0.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#815](https://github.com/vllm-project/guidellm/pull/815) - Update container build by
[@dbutenhof](https://github.com/dbutenhof)in[#819](https://github.com/vllm-project/guidellm/pull/819) - test: register
`slow`

pytest marker to silence PytestUnknownMarkWarning ([#840](https://github.com/vllm-project/guidellm/issues/840)) by[@Anai-Guo](https://github.com/Anai-Guo)in[#841](https://github.com/vllm-project/guidellm/pull/841) - Migrate docs build to nightly and fix error by
[@sjmonson](https://github.com/sjmonson)in[#859](https://github.com/vllm-project/guidellm/pull/859) - [GitHub Actions]: Bump actions/setup-python from 6.2.0 to 6.3.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#858](https://github.com/vllm-project/guidellm/pull/858) - [GitHub Actions]: Bump actions/cache from 5.0.5 to 6.0.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#857](https://github.com/vllm-project/guidellm/pull/857)

### Documentation

- Add documentation section regarding AI assistance by
[@dbutenhof](https://github.com/dbutenhof)in[#721](https://github.com/vllm-project/guidellm/pull/721) - Update README.md by
[@SkiHatDuckie](https://github.com/SkiHatDuckie)in[#792](https://github.com/vllm-project/guidellm/pull/792) - Documentation refactoring by
[@dbutenhof](https://github.com/dbutenhof)in[#814](https://github.com/vllm-project/guidellm/pull/814) - Add troubleshooting guide by
[@jaredoconnell](https://github.com/jaredoconnell)in[#860](https://github.com/vllm-project/guidellm/pull/860) - Fix up doc linkages by
[@dbutenhof](https://github.com/dbutenhof)in[#870](https://github.com/vllm-project/guidellm/pull/870)

### Dependency updates

- Bump aiohttp from 3.13.3 to 3.13.4 by
[@dependabot](https://github.com/dependabot)[bot] in[#682](https://github.com/vllm-project/guidellm/pull/682) - Bump pillow from 12.1.1 to 12.2.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#693](https://github.com/vllm-project/guidellm/pull/693) - Bump python-dotenv from 1.2.1 to 1.2.2 by
[@dependabot](https://github.com/dependabot)[bot] in[#702](https://github.com/vllm-project/guidellm/pull/702) - Bump lxml from 6.0.2 to 6.1.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#703](https://github.com/vllm-project/guidellm/pull/703) - Bump urllib3 from 2.6.3 to 2.7.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#727](https://github.com/vllm-project/guidellm/pull/727) - Bump ujson from 5.12.0 to 5.12.1 by
[@dependabot](https://github.com/dependabot)[bot] in[#730](https://github.com/vllm-project/guidellm/pull/730) - Bump idna from 3.11 to 3.15 by
[@dependabot](https://github.com/dependabot)[bot] in[#734](https://github.com/vllm-project/guidellm/pull/734) - Bump aiohttp from 3.13.4 to 3.14.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#771](https://github.com/vllm-project/guidellm/pull/771) - Bump pyarrow from 22.0.0 to 23.0.1 by
[@dependabot](https://github.com/dependabot)[bot] in[#780](https://github.com/vllm-project/guidellm/pull/780) - Bump aiohttp from 3.14.0 to 3.14.1 by
[@dependabot](https://github.com/dependabot)[bot] in[#801](https://github.com/vllm-project/guidellm/pull/801) - Bump ujson from 5.12.0 to 5.13.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#822](https://github.com/vllm-project/guidellm/pull/822) - Bump pydantic-settings from 2.12.0 to 2.14.2 by
[@dependabot](https://github.com/dependabot)[bot] in[#823](https://github.com/vllm-project/guidellm/pull/823) - Bump msgpack from 1.1.2 to 1.2.1 by
[@dependabot](https://github.com/dependabot)[bot] in[#824](https://github.com/vllm-project/guidellm/pull/824)

## New Contributors

[@mergify](https://github.com/mergify)[bot] made their first contribution in[#685](https://github.com/vllm-project/guidellm/pull/685)[@leehyeoklee](https://github.com/leehyeoklee)made their first contribution in[#707](https://github.com/vllm-project/guidellm/pull/707)[@VincentG1234](https://github.com/VincentG1234)made their first contribution in[#620](https://github.com/vllm-project/guidellm/pull/620)[@regrow1123](https://github.com/regrow1123)made their first contribution in[#744](https://github.com/vllm-project/guidellm/pull/744)[@1195343015](https://github.com/1195343015)made their first contribution in[#747](https://github.com/vllm-project/guidellm/pull/747)[@soyr-redhat](https://github.com/soyr-redhat)made their first contribution in[#742](https://github.com/vllm-project/guidellm/pull/742)[@sjh9714](https://github.com/sjh9714)made their first contribution in[#783](https://github.com/vllm-project/guidellm/pull/783)[@SkiHatDuckie](https://github.com/SkiHatDuckie)made their first contribution in[#777](https://github.com/vllm-project/guidellm/pull/777)[@Anai-Guo](https://github.com/Anai-Guo)made their first contribution in[#796](https://github.com/vllm-project/guidellm/pull/796)

**Full Changelog**: `v0.6.0...v0.7.0`