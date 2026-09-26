source: https://docs.nvidia.com/dynamo/zh-CN/dev/knowledge-base/concepts/simulation/ai-simulate/sweeper/dynamo-integration
lastmod: 2026-09-24T19:58:16.636Z

# Dynamo Sweeper Integration

**Experimental.** The AISimulate CLI, adapter ABI, and replay contracts may change without a
standard deprecation period.

AISimulate’s Sweeper core does not depend on Dynamo. Dynamo owns its optional Planner and Router
sweep configuration providers and `DynamoReplayRunnerFactory`

.

## Install

AISimulate requires Python 3.11 through 3.13. The `ai-dynamo`

package remains installable on Python
3.10, but the AISimulate dependency and CLI are not installed there.

The supported prebuilt environment is the `dynamo-planner`

image. The image stages and installs the
published `aisimulate==0.12.0`

wheel alongside the Dynamo wheels. Dynamo’s Rust workspace
resolves `aisimulate-core==0.12.0`

from crates.io.

For Dynamo source development, install the published AISimulate wheel and build the matching Dynamo bindings:

On supported Python versions, `ai-dynamo`

declares the exact AISimulate release as a base
dependency. No `ai-dynamo[simulation]`

extra is required.

## Run the Unified CLI

Select the Dynamo stack explicitly to load the runner plus any configured Router and Planner adapters:

The `--stack`

option defaults to `engine`

. Without `--stack dynamo`

, top-level `router`

and
`planner`

sections have no matching adapter and fail configuration resolution.

The `ai-dynamo`

distribution registers:

## Use the Python SDK

Call the retained Sweeper Python API only when an application needs the legacy `SmartSearchConfig`

contract and explicit runner injection:

There is no compatibility CLI alias or `--enable-dynamo`

flag.

## Dynamo Providers

The `ai-dynamo`

distribution registers these entry points:

The public recommendation YAML places the adapter-owned domains at the top level:

The legacy `SmartSearchConfig.adapters`

mapping remains available only through the Python SDK.

The legacy flat Planner preset lists remain accepted for backward compatibility but emit a
`FutureWarning`

. They will be removed after the 1.5 release. Nest each list under its sub-item’s
`preset`

field.

Each Planner preset sub-item owns a complete knob set:

Named presets and custom mappings are validated against the complete sub-item. The provider fills family defaults for conditionally inactive predictor knobs before validation.

The Planner provider derives load-predictor parameters from all configured scaling intervals during
`generate_search_space`

. Enabled candidates materialize a concrete `PlannerConfig`

runtime hook.
The Router provider materializes either round-robin behavior without a hook or a concrete KV-router
hook.

## Replay Composition

`DynamoReplayRunnerFactory`

converts each serializable `ReplaySpec`

into an invocation of the
shared AISimulate Replayer. It resolves materialized Planner and Router hooks into Dynamo-owned
scaling and placement policies, while the Replayer continues to own traffic execution and report
generation.

The runner passes trace, fixed, or KV-load-derived closed-loop concurrency through
`ReplaySpec.concurrency`

. The public compiler maps `evaluation.sla`

into `ReplaySpec.goal.sla`

, and
`DynamoReplayRunnerFactory`

reads that lowered field as the replay goodput SLA. This SLA is
independent of the Planner’s scaling SLA. A `dynamo.router:placement_policy@1`

hook selects the
Dynamo placement policy. Without that hook, the Replayer uses its built-in round-robin policy.