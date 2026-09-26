# [Issue #2864] [RFC]: TENT Operator CLI and Sanitized Diagnostic Bundle

source: https://github.com/kvcache-ai/Mooncake/issues/2864
state: open | updated: 2026-09-16T04:53:38Z
labels: RFC

## 正文

## Summary

This RFC proposes a single TENT operator CLI, tentatively named `tent`, and a versioned sanitized diagnostic bundle format.

The goal is to let an operator answer the following questions without reading TENT source code or manually correlating many logs:

- What CPU/GPU/NPU/NIC topology did TENT discover?
- Which transports, devices, policies, QP pools, SL/TC values, and runtime features are enabled?
- Are the local configuration and remote peer compatible?
- Why did TENT select a Direct or Staged path, a particular backend/rail, or a fallback?
- Is a failure caused by configuration, metadata, connectivity, runtime queue pressure, receiver credit, staging, or transport execution?
- What evidence can be attached to a GitHub issue without exposing credentials, rkeys, raw addresses, or other sensitive deployment data?

The first implementation milestone is read-only. It must not hot-reload configuration, quarantine a rail, trigger failover, change QoS policy, or upload diagnostics automatically.

The CLI should reuse existing functionality rather than create parallel implementations:

- `show-link` and NIC discovery from #2820;
- `tebench` for performance testing;
- existing TENT config, topology, metadata, peer probe, metrics, and tracing collectors;
- effective-policy explain from #2856/#2857;
- Execution Plan explain from #2863 when available.

## Motivation

The TENT roadmap in #1058 explicitly lists an isolated transfer/diagnostics CLI as a community-contributable production-readiness item. TENT has accumulated many useful mechanisms, but their operational interfaces remain fragmented.

Examples:

- #2820 provides `show_link`, including local NIC discovery, NUMA affinity, link speed, and a readable/JSON topology matrix.
- `tebench` exercises real transfers and already contains multiple benchmark modes.
- TENT exposes metrics and a basic health endpoint.
- `probePeerAliveByID()` can test control-plane liveness.
- #2821 adds causal latency stage metrics.
- #2845 adds a QoS benchmark/metrics baseline.
- #2856/#2857 add effective QoS policy resolution and explain output.
- #2863 proposes first-class Backend Capabilities and Execution Plan explainability.

These are useful data sources, but users still need different binaries, configuration knowledge, log patterns, and manual interpretation. A failed cross-node run often requires separately checking:

- local NIC enumeration and GID selection;
- remote metadata and endpoint names;
- transport enablement and build flags;
- policy matching and device masks;
- QP pool, SL, and TC settings;
- Direct versus Staged routing;
- peer/control connectivity;
- queue, staging, or receiver-side pressure;
- the exact Mooncake build and sanitized configuration.

This increases support cost and makes bug reports difficult to reproduce. The CLI should provide a common diagnostic model and explain what it observed, what it inferred, and what it could not verify.

## Goals

1. Provide one discoverable `tent` command with stable subcommands.
2. Reuse existing collectors, probes, and benchmarks.
3. Separate offline checks from live/remote checks.
4. Produce both human-readable text and versioned machine-readable JSON.
5. Define consistent check severity, evidence, remediation, and exit-code semantics.
6. Redact sensitive values by default.
7. Generate a bounded diagnostic bundle suitable for offline support and GitHub issues.
8. Keep all v1 operations read-only and explicitly bounded.
9. Work with partial builds where some transports/platforms are unavailable.
10. Provide a stable integration point for future TENT health, Execution Plan, and QoS diagnostics.

## Non-goals

- A configuration hot-reload or remote administration service.
- Automatic rail quarantine, failover, or remediation.
- A second topology discovery implementation.
- A new benchmark engine that competes with `tebench`.
- Dumping all environment variables, process memory, rkeys, or raw transport handles.
- Automatically uploading a diagnostic bundle.
- A cluster-wide scheduler or monitoring platform.
- Replacing Prometheus, tracing, NCCL RAS, or vendor fabric tools.
- Guaranteeing that a successful control-plane probe proves the data path is healthy.
- Requiring every optional backend to be installed for the base CLI to build.

## Proposed command surface

The exact spelling can be adjusted during review, but the command responsibilities should remain distinct.

### `tent version`

Print:

- Mooncake/TENT version and Git commit;
- build type and enabled platform/transport features;
- CLI diagnostic schema versions;
- compiler, CUDA/ROCm/CANN, and relevant runtime versions where available.

### `tent show-topology`

Display the local topology known to TENT:

- CPU NUMA nodes;
- GPU/NPU/device identifiers;
- NIC name, type, NUMA node, link state, speed, port, and selected GID;
- memory locations;
- GPU/NPU-to-NIC affinity;
- NVLink/MNNVL or other supported local links;
- unavailable or partially discovered devices with reasons.

This command should call the same topology/prober code used by TENT, not parse a second set of sysfs files independently.

### `tent check-config`

Validate an effective configuration without starting transfer traffic.

Checks should include:

- parse/type/range validation;
- unknown keys and deprecated aliases;
- build-time availability of enabled transports;
- policy references to valid transports and devices;
- QP pool, SL, TC, and rail-topology consistency;
- conflicting allow/deny lists;
- impossible Direct/Staged combinations;
- QoS Contract validation when configured;
- fields that require restart rather than future hot reload;
- source/provenance of effective values when available.

The output must distinguish:

- `PASS`: verified and valid;
- `WARN`: valid but suspicious or unverifiable;
- `FAIL`: invalid or unsafe;
- `SKIP`: collector/feature unavailable in this build.

### `tent show-link`

Reuse #2820's `show_link` implementation and output model. The existing binary may remain as a compatibility wrapper or alias.

In later milestones, an optional remote target may add:

- local-to-remote NIC mapping;
- selected GID/port and the reason;
- control-plane reachability;
- expected Direct/Staged candidate paths;
- unavailable mappings and specific rejection reasons.

### `tent test-run`

Perform a small, bounded connectivity test using registered scratch memory.

It should report separately:

- metadata resolution;
- control-plane probe;
- remote descriptor compatibility;
- selected policy and Execution Plan;
- transport/rail/QP pool/SL/TC;
- submit, completion, and data-integrity result;
- stage timing when Staged;
- structured failure origin and recommended next check.

Safety requirements:

- no arbitrary raw remote address supplied by the user;
- bounded default buffer size, request count, duration, and concurrency;
- explicit opt-in for any larger test;
- no long-running server exposed on a public interface by default;
- clear distinction between a control probe and a real data-path test.

### `tent show-plan`

Consume #2863's planner or legacy decision adapter and explain:

- effective intent and matched policy;
- Direct/Staged physical path;
- Primary/Fallback/Degraded role;
- backend, device/rail, QP pool, SL/TC;
- resource charge vector;
- cost/health inputs and freshness;
- accepted and rejected candidates with reasons.

Before #2863 is implemented, this subcommand may be absent or limited to the current selector decision. The CLI RFC must not define a second Execution Plan model.

### `tent status`

Query a local running TENT instance through a bounded local interface in a later milestone. Candidate fields:

- instance/config generation and uptime;
- registered segment/buffer counts without raw addresses;
- peer/control state;
- queue depth and inflight work;
- staging occupancy;
- receiver-credit state;
- rail/QP/backend status;
- last-progress timestamp and recent categorized errors.

The local query interface should default to a Unix socket or localhost and must not block transfer progress. This command is observation-only; health-policy automation belongs to a separate RFC.

### `tent collect-diagnostics`

Collect a bounded snapshot from available commands and data sources.

Suggested contents:

- `manifest.json` with bundle/schema version and checksums;
- version/build information;
- sanitized effective configuration and provenance;
- topology and link information;
- policy/QoS validation;
- plan explain for a supplied target/request shape, if requested;
- bounded status/metrics snapshot;
- bounded recent categorized errors;
- results of explicitly requested probes/tests;
- collector errors and skipped sections.

The bundle is created locally and is never uploaded automatically.

### `tent bench`

This is an optional convenience frontend to `tebench`, not a new benchmark implementation. It should preserve access to the underlying tebench command line and output schema. More complex benchmark changes should continue to land in tebench first.

## Diagnostic data model

All subcommands should build a normalized diagnostic result before rendering text or JSON.

```cpp
enum class CheckOutcome {
    PASS,
    WARN,
    FAIL,
    SKIP,
};

struct DiagnosticEvidence {
    std::string source;
    std::string field;
    SanitizedValue observed;
};

struct DiagnosticCheck {
    std::string id;
    CheckOutcome outcome;
    std::string summary;
    std::vector<DiagnosticEvidence> evidence;
    std::vector<std::string> remediation;
};

struct DiagnosticSnapshot {
    uint32_t schema_version;
    BuildInfo build;
    std::vector<DiagnosticSection> sections;
    std::vector<DiagnosticCheck> checks;
    RedactionMetadata redaction;
};
```

Collector failures should be represented in the result instead of aborting the entire bundle, unless a required command input is invalid.

## JSON compatibility

Machine-readable output is a public operational contract.

Rules:

- top-level `schema_version` is required;
- additive optional fields are allowed within the same major version;
- fields must not silently change unit or meaning;
- units belong in names or typed objects (`latency_us`, `bandwidth_bps`);
- timestamps specify clock/domain and format;
- enums use stable lowercase strings;
- unavailable data is omitted or explicitly marked unavailable, not replaced with zero;
- text output may evolve, but JSON compatibility requires review and tests;
- all collectors record their own status so partial results are unambiguous.

Example:

```json
{
  "schema_version": 1,
  "command": "check-config",
  "build": {
    "commit": "<git-sha>",
    "tent": true,
    "cuda": true,
    "rdma": true
  },
  "checks": [
    {
      "id": "policy.device.exists",
      "outcome": "pass",
      "summary": "all configured policy devices were discovered"
    },
    {
      "id": "rdma.gid.reachability",
      "outcome": "warn",
      "summary": "remote reachability was not tested",
      "remediation": ["run tent test-run --target <peer>"]
    }
  ],
  "redaction": {
    "mode": "default",
    "fields_redacted": 7
  }
}
```

## Redaction and security

Diagnostics frequently contain deployment-sensitive information. Redaction must happen at collection/model boundaries, not as a final regex over serialized JSON.

### Always excluded by default

- rkeys and lkeys;
- raw CUDA IPC/Fabric handles;
- credentials, tokens, passwords, certificates, and private keys;
- arbitrary process environment dumps;
- raw memory addresses;
- payload data;
- unbounded logs;
- cloud instance credentials or metadata-service responses.

### Redaction modes

Suggested modes:

```text
default -> safe for ordinary support; preserve enough topology to diagnose
strict  -> pseudonymize hosts, IPs, device serials, paths, tenant/policy names
none    -> explicit local-only opt-in with a warning; secrets remain excluded
```

Strict mode can use a random per-bundle salt so the same host/device remains correlatable inside one bundle without being correlatable across bundles.

### Bundle handling

- output files should be created with restrictive permissions;
- archive size and per-section size must be bounded;
- collection timeout must be bounded;
- symlinks and arbitrary file inclusion are forbidden;
- the manifest records redaction mode and omitted sections;
- the tool must not upload or transmit the bundle without a separate explicit user action outside this RFC.

### Remote testing

`test-run` and remote `show-link` must use existing authenticated/authorized control paths where available. The CLI must not introduce an unauthenticated arbitrary-memory test server. A standalone validation server, if needed later, requires an explicit security design and is out of v1 scope.

## Offline and live modes

Commands fall into two groups.

### Offline/local discovery

- `version`
- `show-topology`
- `check-config`
- local `show-link`

These should work without a running TENT instance or metadata service when possible.

### Live/remote diagnosis

- remote `show-link`
- `test-run`
- `show-plan` with remote metadata
- `status`
- live sections of `collect-diagnostics`

These must report partial/unavailable state clearly when the peer or metadata service cannot be reached.

## Exit codes

Suggested stable exit codes:

```text
0  command completed and no FAIL checks were produced
1  command completed and at least one diagnostic check failed
2  invalid command line or invalid input
3  required collector/service unavailable or command timed out
4  internal tool error or incompatible diagnostic schema
```

Warnings alone return zero unless `--strict` is specified. JSON output must still be emitted for diagnostic failures whenever possible.

## Architecture

```text
CLI frontend
    |
    +-- topology/config/link/plan/status/test collectors
    |
    v
DiagnosticSnapshot + DiagnosticCheck
    |
    +-- readable renderer
    +-- JSON renderer
    +-- bundle writer
```

Collectors should be reusable libraries rather than logic embedded directly in `main()`. Existing commands such as `show_link` can call the same collector/rendering library.

Optional collectors must be isolated by build feature. A CPU-only build should still provide config/topology checks and report GPU/RDMA collectors as unavailable rather than failing to build the CLI.

## Compatibility and rollout

- Existing `show_link` behavior remains available during migration.
- Existing tebench remains the benchmark implementation and may remain a separate binary.
- No current environment variable or config key changes meaning.
- The CLI is additive and does not initialize transports unless a command explicitly requires it.
- Read-only commands must avoid creating GPU contexts where discovery can be completed without one.
- Commands that initialize a real engine must say so in help and output.
- JSON schemas and exit codes require compatibility tests.

## Proposed PR sequence

### PR1: Diagnostic core and schema

- Add `DiagnosticSnapshot`, checks, evidence, renderers, redaction primitives, and schema tests.
- Add `tent version`.
- No transport initialization or remote calls.

### PR2: Topology and existing show-link integration

- Add `tent show-topology` and `tent show-link` using existing collectors.
- Preserve `show_link` as a wrapper/alias if maintainers prefer.
- Add fake topology and real Linux discovery tests.

### PR3: Config validation

- Add `tent check-config`.
- Reuse TENT config parsing, policy validation, QoS Contract validation, and effective-config provenance where available.
- Add invalid/mismatched configuration fixtures.

### PR4: Bounded connectivity test

- Add `tent test-run` using scratch registered buffers.
- Separate control probe, metadata resolution, data-path completion, and integrity results.
- Add explicit time/size/concurrency limits.

### PR5: Plan explain

- Add `tent show-plan` by consuming #2863.
- Do not define a second plan schema.

### PR6: Live status and diagnostic bundle

- Add a bounded local status query interface.
- Add `tent status` and `tent collect-diagnostics`.
- Add strict/default redaction and archive safety tests.

### Later work

- `tent bench` convenience integration with tebench;
- additional vendor/backend collectors;
- switch/NIC per-priority counter integration;
- health event monitoring after a separate health-state RFC;
- connector-specific diagnostic sections.

## Validation plan

### Unit and schema tests

- JSON golden tests and forward-compatible additive fields;
- stable exit-code behavior;
- PASS/WARN/FAIL/SKIP aggregation;
- unavailable optional collector behavior;
- default/strict redaction;
- secret/rkey/address non-disclosure tests;
- path traversal, symlink, permission, timeout, and size-limit tests;
- deterministic config checks and remediation text;
- text and JSON renderers representing the same facts.

### Differential tests

- `tent show-link` matches the existing #2820 collector output;
- `tent check-config` accepts configurations accepted by the runtime and rejects known-invalid configurations before runtime initialization;
- `tent show-plan` matches #2863 explain output;
- `tent bench` forwards to tebench without changing benchmark semantics.

### Real-cluster validation

On the existing H20/RoCE nodes, cover:

- healthy two-node RDMA and TCP paths;
- multiple NUMA domains and NICs;
- an unreachable or wrong GID/port;
- a disabled/down NIC;
- policy referring to a missing device;
- local/remote transport capability mismatch;
- Direct GPU↔GPU transfer;
- forced Staged transfer;
- peer process stopped or killed;
- runtime queue and receiver-credit enabled/disabled where available;
- default and strict diagnostic bundles inspected for secrets.

For every failure, the CLI should identify the furthest verified stage and avoid claiming later stages passed. For example, a successful control probe must not be reported as successful RDMA data connectivity.

### Overhead

- offline commands add no data-path overhead;
- status collection must not block transfer progress;
- any live monitoring interval is bounded and configurable;
- diagnostic collection must complete or time out without leaking threads, QPs, registered memory, or temporary files.

## Expected benefits and claims boundary

This RFC should provide:

- reproducible and more complete issue reports;
- faster diagnosis of GID, port, remote QP, NUMA, rail topology, policy, and capability problems;
- a common explain surface for Execution Plan and QoS decisions;
- stable JSON for automation and CI qualification;
- a secure default path for sharing diagnostics;
- less duplicate diagnostic logic across examples and ad-hoc scripts.

It does not claim to fix a failing path automatically or improve transfer performance. Any future remediation or automatic health policy requires separate design and validation.

## Relationship to existing work

- #1058: directly implements the TENT CLI/diagnostics and documentation roadmap item.
- #2820: reuse local NIC/topology `show-link`; do not duplicate its discovery code.
- #2821 and #1850: consume causal metrics/traces; do not replace tracing.
- #2845 and tebench: reuse benchmark and QoS metric formats.
- #2856/#2857: consume effective QoS policy validation/explain.
- #2849: report receiver-credit/backpressure state when available; do not define another credit protocol.
- #2863: consume Backend Capability and Execution Plan explain.
- #1808: reuse the dedicated peer liveness probe while clearly separating it from data-path validation.
- #1984/#2438: report rail/failover state when available; automatic health control remains outside this RFC.
- #2713: Classic TE metrics may be an optional collector, but this RFC is TENT-first.

## Open questions

1. Is `tent` the preferred binary name, or should the initial commands live under an existing Mooncake CLI namespace?
2. Should `show_link` become a compatibility wrapper around `tent show-link`, or remain independently installed?
3. Which commands must be available in the first accepted milestone: `show-topology`, `check-config`, and `show-link`, or should `test-run` also be included?
4. Should the live status interface use a Unix socket, localhost TCP, or an existing ControlService method?
5. Which fields may remain stable in JSON v1, and which should be placed under explicitly experimental sections?
6. What should default redaction preserve for topology diagnosis: private IP prefixes, GID prefixes, device names, and policy names?
7. Should `collect-diagnostics` create a directory, JSON file, or compressed archive by default?
8. Should `bench` remain visibly separate from tebench until the rest of the CLI stabilizes?

### Before submitting a new issue...

- [x] Searched existing issues and PRs for TENT CLI, doctor, diagnostics, topology, config checking, connectivity testing, and diagnostic bundles.
- [x] Read #1058 and reviewed existing show-link, tebench, tracing, metrics, policy explain, peer probe, and Execution Plan work.


## 评论 (7)

### github-actions[bot] · 2026-07-12

Thanks for opening this issue, @catyans!

| Field | Value |
|-------|-------|
| **Issue** | #2864 |
| **GitHub user ID** | `18214026` |
| **Reporter** | @catyans |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### catyans · 2026-07-12

Real topology-source feasibility experiment on 2026-07-13 using the current `show_link` implementation from merge head `159712b7`.

Environment: Lingjun H20 `lingjun-099`, Linux 5.10.134, 2 x Xeon Platinum 8575C / 192 vCPUs / 2 NUMA nodes, 8 x H20-3e, driver 580.105.08, five mlx5 HCAs. Built with GCC 13.3, `BUILD_EXAMPLES=ON`, `USE_TENT=ON`, `USE_CUDA=OFF`. Command: `show_link --discover_only --json`.

Results:
- 30 invocations: 701.87 ms total, **23.4 ms/invocation**; output was valid JSON (~1.0 KiB) with `local_nics` and `topology`;
- one of those 30 invocations observed `mlx5_bond_0` as temporarily unavailable and returned only 4 NICs;
- an immediate follow-up campaign returned the full 5 NICs in **100/100** runs; overall full discovery was **129/130**, with one transient partial snapshot;
- the current discover-only JSON left GID/port/speed/NUMA fields unknown for the listed NIC records, while the topology section still provided CPU-to-NIC grouping.

Conclusion: the underlying topology collection is fast enough for an operator command and already exposes useful structured data, but the transient 4/5 result shows why the RFC needs explicit `complete/degraded`, per-probe errors, timestamp/generation and retry guidance. A partial snapshot must not look authoritative. This also confirms that `show-topology` should combine multiple probes rather than simply wrap the current JSON.

### alogfans · 2026-07-17

We believe these peripheral components are a priority at this stage.

### catyans · 2026-07-21

Thanks — just to confirm, do you mean these operator and diagnostic components are a priority at the current stage? If so, I will start with a small read-only PR containing the diagnostic schema, JSON renderer, and tent version, without transport initialization or runtime control changes.

### catyans · 2026-07-31

I will take the priority feedback as support for the smallest read-only implementation slice: diagnostic schema, JSON rendering, and version reporting only, without transport initialization, runtime mutation, or control commands. I will link the implementation PR here once that focused slice is ready.

### 0z5a · 2026-09-16

Hi @catyans , I'd like to take PR1 (Diagnostic core and schema): `DiagnosticSnapshot` / checks and evidence, text + JSON renderers, redaction primitives, schema tests, and `tent version`, keeping it offline-only with no transport initialization or remote calls.

I'll keep unresolved RFC choices (such as the final CLI naming and broader redaction policy) minimally coupled so they can be adjusted during review.


### 0z5a · 2026-09-16

PR1 implementation is now available in #4154. It adds the diagnostic schema/core model, text and JSON renderers, redaction primitives, schema and redaction tests, and the offline-only `tent version` command. The CLI does not link or initialize transports, metadata clients, device runtimes, or remote connections.
