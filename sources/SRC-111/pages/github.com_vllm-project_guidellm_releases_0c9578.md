source: https://github.com/vllm-project/guidellm/releases

# Releases: vllm-project/guidellm

## Release list

## GuideLLM v0.7.4

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

## GuideLLM v0.7.3

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

## GuideLLM v0.7.2

## Overview

GuideLLM v0.7.2 completes the v0.7.0 CLI transition, adds synthetic image and video data generation, adds support for generating graph images using `--output kind=plot,path=<file>`

, and resolves some dependency vulnerabilities.

To get started, install with:

`pip install guidellm[recommended]==0.7.2`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.7.2`

## What's Fixed

- Fixed a bug where
`console`

output from`guidellm benchmark from-file`

(now`guidellm export`

) was crashing. - Fixed a minor bug in the
`safe_add`

utility function. - Fixed the HTML report format by locking the referenced assets to a published version.
- Fixed a crash in generating the CSV report format when using the backend
`api_key`

parameter. - Fixed a redundant console refresh in the progress components.
- Restored the ability to configure a default directory for report outputs, with the GUIDELLM_DEFAULT_RESULTS_DIR environment variable.
- Improved the CLI help text for the benchmark command group.
- Updating our
`transformers`

dependency to 5.5.0 resolves a Critical and several High severity security vulnerabilities.

## What's Changed

- In 0.7.0 the
`guidellm run`

command was completely overhauled, but this introduced bugs and inconsistenies in the`guidellm benchmark from-file`

(now`guidellm export`

) and`guidellm preprocess dataset`

commands. This release overhauls those commands to match the new`guidellm run`

command. See the updated[v0.7.0 Migration Guide](https://vllm-project.github.io/guidellm/0.7.2/guides/v0.7.0_migration_guide)for more details. - Added support for synthetic image and video data generation.
- Added support for generating graph images using
`--output kind=plot,path=<file>`

. The image type is inferred from the file extension, including SVG, PNG, and PDF. - Added support for early exit from multi-strategy benchmarks when errors occur. (For example, when running a constant profile with multiple increasing rates, the benchmark will exit when the first rate fails rather than continuing to run higher rates which are likely to fail as well.). For example,
`--constraint kind=max_errors,count=1,stopping_scope=all`

will exit the benchmark when the first error occurs. - With the addition of the "plot" output type, we've enhanced the
`guidellm run`

and`guidellm benchmark from-file`

(now`guidellm export`

) commands to allow generating multiple output files of the same kind. For example,`--output kind=plot,path=plots/plot.svg --output kind=plot,path=plots/plot.png`

will generate two output files, one as SVG and one as PNG. - Improved error messaging for command options using the new registry kind model: e.g.,
`--output`

will now show the available kinds. - Renamed the
`guidellm benchmark from-file`

command to`guidellm export`

to better reflect its purpose.

## Changelog

### Features

- feat: synthetic image and video data generation for VLM benchmarking by
[@zakariaelh](https://github.com/zakariaelh)in[#732](https://github.com/vllm-project/guidellm/pull/732) - Feat/cross rate early exit by
[@ushaket](https://github.com/ushaket)in[#605](https://github.com/vllm-project/guidellm/pull/605) - feat: Add graph plotting support for benchmarks by
[@Prasannajaga](https://github.com/Prasannajaga)in[#923](https://github.com/vllm-project/guidellm/pull/923) - Modernize benchmark from-file by
[@dbutenhof](https://github.com/dbutenhof)in[#927](https://github.com/vllm-project/guidellm/pull/927) - Handle repeated
`--output`

specifications consistently across run and from-file by[@Pragadeesh122](https://github.com/Pragadeesh122)in[#936](https://github.com/vllm-project/guidellm/pull/936) - Update
`guidellm preprocess dataset`

syntax to 0.7.x CLI style by[@dbutenhof](https://github.com/dbutenhof)in[#943](https://github.com/vllm-project/guidellm/pull/943) - Added more useful error messages for kind inputs by
[@jaredoconnell](https://github.com/jaredoconnell)in[#949](https://github.com/vllm-project/guidellm/pull/949) - Renamed
`guidellm benchmark from-file`

to`guidellm export`

by[@jaredoconnell](https://github.com/jaredoconnell)in[#960](https://github.com/vllm-project/guidellm/pull/960)

### Bug fixes

- Fix safe_add sign handling for the first value by
[@harivilasp](https://github.com/harivilasp)in[#900](https://github.com/vllm-project/guidellm/pull/900) - Bump UI target to latest by
[@sjmonson](https://github.com/sjmonson)in[#901](https://github.com/vllm-project/guidellm/pull/901) - Fix explicit fill-value overwrite detection in arg parser by
[@harivilasp](https://github.com/harivilasp)in[#897](https://github.com/vllm-project/guidellm/pull/897) - Correct the CSV report format by
[@dbutenhof](https://github.com/dbutenhof)in[#912](https://github.com/vllm-project/guidellm/pull/912) - Disable redundant auto-refresh in console progress components by
[@whygyc](https://github.com/whygyc)in[#914](https://github.com/vllm-project/guidellm/pull/914) - Add a setting to configure the default working dir by
[@sjmonson](https://github.com/sjmonson)in[#916](https://github.com/vllm-project/guidellm/pull/916) - Fix misleading CLI help text for benchmark command group by
[@bennyturns](https://github.com/bennyturns)in[#938](https://github.com/vllm-project/guidellm/pull/938)

### Documentation

- Cleanup docs/guides by
[@SkiHatDuckie](https://github.com/SkiHatDuckie)in[#885](https://github.com/vllm-project/guidellm/pull/885) - docs(developing): add a proper Logging guide (
[#881](https://github.com/vllm-project/guidellm/issues/881)) by[@Anai-Guo](https://github.com/Anai-Guo)in[#898](https://github.com/vllm-project/guidellm/pull/898) - Add example: benchmarking with local tokenizer and custom JSONL dataset by
[@miglis](https://github.com/miglis)in[#915](https://github.com/vllm-project/guidellm/pull/915)

### Internal refactoring and cleanup

- Minor logging cleanup by
[@dbutenhof](https://github.com/dbutenhof)in[#902](https://github.com/vllm-project/guidellm/pull/902)

### CI environment

- Added integration tests for constraint overrides by
[@jaredoconnell](https://github.com/jaredoconnell)in[#887](https://github.com/vllm-project/guidellm/pull/887) - Allow TODO and HACK comments by
[@sjmonson](https://github.com/sjmonson)in[#910](https://github.com/vllm-project/guidellm/pull/910) - Move tox runner setting back into tests env by
[@sjmonson](https://github.com/sjmonson)in[#908](https://github.com/vllm-project/guidellm/pull/908) - Fix typo in pyproject.toml comment by
[@arijitroy003](https://github.com/arijitroy003)in[#950](https://github.com/vllm-project/guidellm/pull/950)

### Dependency updates

- [GitHub Actions]: Bump docker/setup-buildx-action from 4.1.0 to 4.2.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#882](https://github.com/vllm-project/guidellm/pull/882) - [GitHub Actions]: Bump actions/cache from 6.0.0 to 6.1.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#883](https://github.com/vllm-project/guidellm/pull/883) - [GitHub Actions]: Bump docker/setup-qemu-action from 4.1.0 to 4.2.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#884](https://github.com/vllm-project/guidellm/pull/884) - Bump development dependencies by
[@sjmonson](https://github.com/sjmonson)in[#894](https://github.com/vllm-project/guidellm/pull/894) - Bump transformers from 5.3.0 to 5.5.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#928](https://github.com/vllm-project/guidellm/pull/928) - Bump pillow from 12.2.0 to 12.3.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#942](https://github.com/vllm-project/guidellm/pull/942) - Bump setuptools from 80.9.0 to 83.0.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#954](https://github.com/vllm-project/guidellm/pull/954) - [GitHub Actions]: Bump actions/setup-python from 6.3.0 to 7.0.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#957](https://github.com/vllm-project/guidellm/pull/957)

## New Contributors

[@zakariaelh](https://github.com/zakariaelh)made their first contribution in[#732](https://github.com/vllm-project/guidellm/pull/732)[@harivilasp](https://github.com/harivilasp)made their first contribution in[#900](https://github.com/vllm-project/guidellm/pull/900)[@whygyc](https://github.com/whygyc)made their first contribution in[#914](https://github.com/vllm-project/guidellm/pull/914)[@Prasannajaga](https://github.com/Prasannajaga)made their first contribution in[#923](https://github.com/vllm-project/guidellm/pull/923)[@miglis](https://github.com/miglis)made their first contribution in[#915](https://github.com/vllm-project/guidellm/pull/915)[@Pragadeesh122](https://github.com/Pragadeesh122)made their first contribution in[#936](https://github.com/vllm-project/guidellm/pull/936)[@bennyturns](https://github.com/bennyturns)made their first contribution in[#938](https://github.com/vllm-project/guidellm/pull/938)[@arijitroy003](https://github.com/arijitroy003)made their first contribution in[#950](https://github.com/vllm-project/guidellm/pull/950)

**Full Changelog**: `v0.7.1...v0.7.2`

## GuideLLM v0.7.1

## Overview

GuideLLM v0.7.1 introduces some minor fixes for the v0.7.0 CLI changes plus finishing touches on tool-call and multi-turn.

To get started, install with:

`pip install guidellm[recommended]==0.7.1`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.7.1`

## What's Fixed

- When using a
`--config`

file, profile`rate`

/`streams`

parameters were not being passed to the benchmark. This is now fixed. - The
`--override`

option now supports overriding sub-benchmark (per-strategy) constraints. For example,`--constraint kind=max_duration,seconds=30 --override constraint[0].seconds 10,20`

will apply a 10 second constraint to the first strategy, and a 20 second constraint to the second strategy. - Improved support for server tool calls. Turns can now be designated as turns where you expect the server to run a tool call, and turns where you do not expect the server to run a tool call.
- Improvements to realism of client-side tool calls. Client side tool calls now span 2 turns. The first turn is the client asking the server to request a tool call, and the second turn is the client sending the mocked tool call output to the server, and the server responding to that.
- Dataset requeue delay is now exposed in the dataset API as column
`requeue_delay`

(which can be remapped as usual). Requeue delay (sometimes called "think time") is the delay between the end of one turn and the start of the next turn. For synthetic text datasets, you can specify statistical delay spreads using:`delay`

: average requeue delay in seconds.`delay_stdev`

: standard deviation of requeue delay in seconds`delay_min`

: minimum requeue delay in seconds`delay_max`

: maximum requeue delay in seconds


## What's Changed

- Add auto queue rule + misc PR description fixes by
[@sjmonson](https://github.com/sjmonson)in[#872](https://github.com/vllm-project/guidellm/pull/872) - Trace File Refactor by
[@SkiHatDuckie](https://github.com/SkiHatDuckie)in[#829](https://github.com/vllm-project/guidellm/pull/829) - Loosen torchcodec requirement by
[@sjmonson](https://github.com/sjmonson)in[#874](https://github.com/vllm-project/guidellm/pull/874) - Fix for being unable to specify "benchmarks" in a config by
[@sjmonson](https://github.com/sjmonson)in[#875](https://github.com/vllm-project/guidellm/pull/875) - Fix tool call turn sequence and add improved support for server tool calls by
[@jaredoconnell](https://github.com/jaredoconnell)in[#839](https://github.com/vllm-project/guidellm/pull/839) - Support for per sub-benchmark constraints by
[@sjmonson](https://github.com/sjmonson)in[#877](https://github.com/vllm-project/guidellm/pull/877) - Update documentation for
`--override`

by[@dbutenhof](https://github.com/dbutenhof)in[#880](https://github.com/vllm-project/guidellm/pull/880) - Expose requeue delay from datasets (
[#871](https://github.com/vllm-project/guidellm/pull/871)Cont.) by[@SkiHatDuckie](https://github.com/SkiHatDuckie)in[#876](https://github.com/vllm-project/guidellm/pull/876)

**Full Changelog**: `v0.7.0...v0.7.1`

## GuideLLM v0.7.0

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
[#787](https://github.com/vllm-project/guidellm/issues/787)) by[@Anai-Guo](https://github.com/Anai-Guo)in[#796](https://github.com/vllm-project/guidellm/pull/796) - fix(openai): surface streaming SSE error payloads as request failures...

[Read more](https://github.com/vllm-project/guidellm/releases/tag/v0.7.0)

## GuideLLM v0.6.1

## Overview

GuideLLM v0.6.1 is a hotfix patch to support RHAI 3.5 container build.

To get started, install with:

`pip install guidellm[recommended]==0.6.1`

Or from source with:

`pip install 'guidellm[recommended] @ git+https://github.com/vllm-project/guidellm.git'@v0.6.1`

## What's Fixed

- Bump torch version to 2.11
- Bump torchcodec version to 0.11

## Compatibility Notes

**Python**: 3.10–3.13**OS**: Linux, MacOS

## What's Changed

- Upgrade 0.6 torch dependencies by
[@dbutenhof](https://github.com/dbutenhof)in[#837](https://github.com/vllm-project/guidellm/pull/837)

**Full Changelog**: `v0.6.0...v0.6.1`

## GuideLLM v0.6.0

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

## GuideLLM v0.5.4

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

## GuideLLM v0.5.3

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

## GuideLLM v0.5.2

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