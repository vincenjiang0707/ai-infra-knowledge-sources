# [Issue #3809] [Track]: Mooncake Store Configuration and Environment Convergence

source: https://github.com/kvcache-ai/Mooncake/issues/3809
state: open | updated: 2026-09-23T17:03:27Z
labels: 

## 正文

Mooncake Store currently reads configuration from environment variables, config files, and CLI flags through several different paths. Environment-variable names, parsing, validation, and business logic are often mixed together, which makes behavior difficult to review and new settings easy to implement inconsistently.

This issue tracks staged convergence of those paths. Master-specific design remains aligned with #2694.

## Overall status

**Last updated:** 2026-09-24

| Phase | Status | Current position |
| --- | --- | --- |
| Phase 1: Environment convergence | Implementation coverage submitted; merge and final audit pending | The remaining eligible Store reads are covered by the owner-scoped PRs below, ending with #4256. Six Phase 1 PRs are still open, so this phase is **not yet complete on `main`**. |
| Phase 2: Structured configuration | Internal ownership pilots under review | #4275, #4297, and #4301 move three Master bootstrap settings into component-owned configs. They retain the existing flat YAML/JSON keys and CLI flags; **no public grouped schema has been approved or introduced**. |
| Phase 3: CLI convergence | Not started Store-wide | The pilots centralize explicit CLI overrides for their own settings, but do not establish a general CLI model or change the wider CLI contract. |

The next Phase 1 gate is to merge the six open owner PRs and repeat the production-read inventory against the resulting `main`: every remaining direct environment read must have an explicit owner and lifecycle classification or be recorded as an intentional exception. Submitted PR coverage is not the same as satisfying the completion criteria below.

## Goals

- Keep environment-variable definitions in one grouped catalog, named after the actual environment variables.
- Keep generic value parsing separate from environment-variable definitions.
- Group settings by the component configuration that owns their meaning, not merely by the file or helper where `getenv` currently appears.
- Read startup-only settings once through an explicit config loader such as `FromEnvironment()` during component initialization, then pass the resolved config to business logic.
- Classify each read as startup-only, intentionally late-read, or delegated to an external library before migrating it.
- Preserve existing variable names, defaults, empty/invalid-value behavior, alias order, diagnostics, and source precedence during convergence. Any deliberate safety fix must be identified and tested separately from behavior preservation.
- Cover each migrated config with focused tests.

## Current scope and review rules

The following rules govern the environment-convergence PRs. Earlier merged pilots may predate part of this layout and should be included in the final audit.

1. Define environment variables in `mooncake-common`, grouped by owning configuration. Use the existing `MC_DEFINE_ENV_VAR` macro so the C++ name and environment-variable string stay identical.
2. Reuse the common typed parsing layer. `EnvironmentVariable<T>` selects the shared parser for `T`; keep a definition string-typed and use a custom parser only when needed to preserve an existing acceptance surface or diagnostic behavior, and document the exception next to the definition or loader.
3. Extract the config type from the business component. Keep environment loading and config-specific validation under `mooncake-store/src/config`; choose a private or public header according to the actual API boundary.
4. Keep the dependency direction `business component -> config`. A config implementation must not depend on the business component that consumes it.
5. Make runtime components consume the resolved config instead of reading the process environment directly. Operational error handling that depends on live component state remains with the component.
6. Prefer semantic config field types, such as `std::chrono` durations, and perform environment-unit conversion explicitly in the loader.
7. Keep each PR limited to one coherent config owner and avoid unrelated behavior or API changes.

Where applicable, behavior-preservation tests should cover unset, explicitly empty, valid, invalid, boundary/overflow, whitespace/trailing-character, alias precedence, and diagnostic behavior. Tests that modify the process environment must restore the previous value rather than assuming it was unset.

The following are not authorized by the environment-only phase: changing public environment-variable names or defaults; changing config-file, environment, or CLI precedence; adding hot reload; redesigning the public structured config format; or mechanically migrating test-/benchmark-only variables without a production owner.

## Progress

These are delivery statuses, **not** an overall completion percentage. #3408 and #3823 cover the same owner; #3957 is a supporting layout alignment.

| Work | Status | PRs |
| --- | --- | --- |
| Earlier owner migrations and layout alignment | Merged | #3408, #3823, #3525, #3763, #3773, #3781, #3785, #3804, #3840 |
| Transfer, storage, client, memory, NoF/SPDK, HA, and connector owners added since the previous update | Merged | #3850, #3853, #3871, #3872, #3900, #3948, #3949, #3956, #3957, #3966, #3967, #3976, #3982, #3983, #4012, #4036, #4098, #4119, #4146, #4165, #4166 |
| NoF worker pool, QoS, debug, shared-memory SPDK registration, and client checksum owners | Open | #4170, #4171, #4203, #4204, #4245 |
| Remaining eligible Store environment reads and exception inventory | Open; Phase 1 closing PR | #4256 |
| Master configuration ownership pilots | Open; Phase 2 internal work | #4275 (metrics), #4297 (embedded HTTP), #4301 (pod identity) |

The old #3850/#3853 CI-blocker note is resolved: both PRs have merged. #4256 covers DFS enablement, Master metadata, Store cluster identity, and NVMe KV executor settings without duplicating the five other open owner PRs. It identifies external accelerator contracts, Master bootstrap/Kubernetes paths, and test/failpoint/stub-only controls as remaining direct-read categories to classify during the final audit.

## Remaining work and phase boundaries

1. Land #4170, #4171, #4203, #4204, #4245, and #4256, handling integration conflicts only if they actually arise. Then audit `main` against the Phase 1 completion criteria, including owner boundaries, first-use/late-read behavior, diagnostics, and focused tests. Do not declare Phase 1 complete merely because the PRs were opened.
2. Continue Phase 2 as small, reviewable configuration-owner migrations. The current Master pilots use existing flat file keys and explicit CLI flags. #4275 and #4297 separately validate effective ports before narrowing them; #4301 is a behavior-preserving string configuration refactor. A public grouped schema, unknown-key policy, migration strategy, and compatibility contract require separate review under #2694 before new keys are exposed.
3. Begin Store-wide Phase 3 CLI convergence only after the source-resolution and compatibility design is agreed. The existing pilots do not, by themselves, settle global CLI precedence or diagnostics.

Late reads are exceptions, not a general hot-reload mechanism. They may remain when existing behavior intentionally observes the environment at the point of use, for example a debug/test failpoint or an external-library contract. Each exception should be explicit and tested rather than hidden among startup-only reads.

## Later-phase design checklist

### Structured configuration

- Inventory existing config-file readers, keys, validation, and precedence.
- Feed structured input into component-owned typed configs instead of creating a second runtime model.
- Centralize source-independent normalization and validation where existing behavior permits it.
- Preserve existing file keys and compatibility behavior during migration.
- Test defaults, valid/invalid values, aliases, and source precedence.

### CLI convergence

- Inventory current CLI flags, explicit-set detection, and override behavior.
- Map CLI inputs into the same component configs instead of maintaining a separate runtime model.
- Centralize precedence and diagnostics without changing the existing order until compatibility coverage and an approved design justify it.
- Remove duplicate parsing and validation only after compatibility coverage is in place.

## Phase 1 completion criteria

The environment phase is complete when every production Store environment read has an explicit owner and lifecycle classification, and is either:

1. a startup-only setting defined in the grouped catalog, resolved by its owning config loader, and consumed without a direct environment read in the business component; or
2. documented as an intentional late-read or external-library exception.

Each migrated path must preserve existing behavior and have focused tests. A migration should not add a new wrapper, parser, or public API unless the existing shared abstraction cannot express the required behavior. Completion of the environment phase does not imply that config-file or CLI convergence is complete.

## Related work

- #459 proposed a general Mooncake config module. It is useful prior art, but was closed after inactivity and did not track this staged Store migration.
- #2694 is the focused RFC for Master configuration refactoring and remains authoritative for Master-specific design.
- #1538 is an older cross-component proposal; the owner-scoped Store PRs in this tracker cover the remaining Store work instead of treating it as a prerequisite.

### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/).


## 评论 (1)

### github-actions[bot] · 2026-09-01

Thanks for opening this issue, @bitborne!

| Field | Value |
|-------|-------|
| **Issue** | #3809 |
| **GitHub user ID** | `177341921` |
| **Reporter** | @bitborne |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
