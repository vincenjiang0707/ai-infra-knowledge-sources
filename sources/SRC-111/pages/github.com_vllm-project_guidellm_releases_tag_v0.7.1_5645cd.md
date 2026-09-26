source: https://github.com/vllm-project/guidellm/releases/tag/v0.7.1

# GuideLLM v0.7.1

[dbutenhof](https://github.com/dbutenhof)released this

·

[123 commits](https://github.com/vllm-project/guidellm/compare/v0.7.1...main)to main since this release
Immutable
release. Only release title and notes can be modified.

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