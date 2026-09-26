# [Issue #2105] Refactor common result metadata processing into a shared helper

source: https://github.com/SemiAnalysisAI/InferenceX/issues/2105
state: open | updated: 2026-07-06T19:50:39Z
labels: 

## 正文

## Problem

`utils/process_result.py` and `utils/agentic/aggregation/process_agentic_result.py` independently parse and validate common benchmark metadata. PR #2100 adds heterogeneous prefill/decode hardware metadata to both paths, which highlights the maintenance cost and risk of the two implementations drifting.

## Goal

Move shared environment parsing, topology validation, and common result fields behind one reusable implementation consumed by both regular and agentic result processors.

## Acceptance criteria

- Regular and agentic result processors use the same code for common metadata and multinode topology fields.
- Optional `PREFILL_HARDWARE` / `DECODE_HARDWARE` handling is implemented once, with both-or-neither validation.
- Existing homogeneous, heterogeneous, single-node, and multinode result schemas remain compatible.
- Shared table-driven tests cover the common behavior; processor-specific tests focus on integration and metric output.

## 评论 (1)

### cquil11 · 2026-07-06

Suggested implementation:

1. Add a pure helper module such as `utils/result_metadata.py`. Have it accept a `Mapping[str, str]` rather than reading `os.environ` directly.
2. Introduce `build_common_result_fields(env, scenario_type=...)` for shared fields such as runner hardware, model, framework, precision, speculative decoding, disaggregation, and scenario type.
3. Introduce `build_topology_fields(env)` returning both serialized topology fields and derived values (`num_gpus`, effective TP/EP, and DP attention). This function should own single-node versus multinode parsing, prefill/decode worker fields, and paired optional hardware validation.
4. Keep metric-specific work in the current processors: `process_result.py` handles serving latency/throughput conversion, while `process_agentic_result.py` handles request/server metric nesting.
5. Move the topology cases into table-driven tests against the shared helper: single-node, homogeneous multinode, heterogeneous multinode, prefill-only hardware, and decode-only hardware. Leave one integration smoke test in each processor to verify that shared metadata reaches its final JSON.

A small immutable dataclass (for example, `TopologyMetadata`) would make the derived values explicit and prevent the processors from recomputing counts differently. The dataclass can expose `as_result_fields()` so output naming also lives in one place.
