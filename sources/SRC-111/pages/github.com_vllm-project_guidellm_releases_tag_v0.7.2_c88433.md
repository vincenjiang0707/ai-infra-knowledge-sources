source: https://github.com/vllm-project/guidellm/releases/tag/v0.7.2

# GuideLLM v0.7.2

[dbutenhof](https://github.com/dbutenhof)released this

·

[92 commits](https://github.com/vllm-project/guidellm/compare/v0.7.2...main)to main since this release
Immutable
release. Only release title and notes can be modified.

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