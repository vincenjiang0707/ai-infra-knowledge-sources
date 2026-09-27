# [Issue #4815] [RFC][Refactor] Turn Server Bench into a Case-Driven KV Data-Plane Test Tool

source: https://github.com/LMCache/LMCache/issues/4815
state: open | updated: 2026-09-17T16:57:30Z
labels: 

## 正文

> [!NOTE]
> **Design Update — September 18, 2026**
>
> This revision replaces the earlier, broader `KVLayoutProfile -> WorkerPlan ->
> MockWorker` proposal with the smaller design that has now been implemented and
> reviewed through Steps 1-4 and is being completed in Step 5 (#5165).
>
> The goal is unchanged: make ServerBench a deterministic KV data-plane test
> tool backed by a real LMCache Server. The updated design avoids introducing a
> general worker-planning framework before PP, DCP, or multi-server cases need it.

## Summary

`lmcache bench server` should validate LMCache registration, lookup, transfer,
and data integrity without loading a model or inference engine.

The design separates three concerns:

- `BenchCase` defines request order and correctness checks.
- A legacy shape spec or YAML `ModelLayout` creates synthetic, rank-local KV
  tensors.
- LMCache's production `TransferContext`, format detection, grouping, platform
  code, and Server protocol perform the actual data-plane work.

This is a synthetic cache benchmark, not a replacement for vLLM/SGLang E2E
tests.

## Why

The original ServerBench path mixed CLI parsing, tensor allocation, transfer
protocol details, and cold/warm test logic. That made it difficult to add a new
layout and easy for benchmark-only implementations to drift from production
LMCache behavior.

The refactor gives us:

- deterministic cold STORE -> warm RETRIEVE correctness tests;
- both LMCache-driven and engine-driven baseline coverage;
- configurable hybrid-model cache layouts without model weights;
- reuse of production transfer and KV-grouping code;
- a small place to test layout and protocol edge cases before full engine E2E.

## Current architecture

```text
CLI
├── legacy --kvcache-shape-spec
└── --model-layout <yaml>
          |
          v
rank-local tensors and registration metadata
          |
          v
ServerBenchClient + TransferContext
          |
          v
BenchCase
  LOOKUP -> STORE -> visibility -> LOOKUP -> RETRIEVE -> checksum
          |
          v
real LMCache Server
```

Responsibilities are intentionally narrow:

| Component | Responsibility |
|---|---|
| `BenchCase` | Defines requests, operation order, expected results, and checks |
| `ServerBenchClient` | Owns sessions, synthetic rank contexts, LOOKUP, transfer submission, checksums, and cleanup |
| `TransferContext` | Implements LMCache-driven or engine-driven registration and transfer behavior |
| `ModelLayout` | Describes model layers, TP size, allocation, and layout mode |
| `ModelCache` | Keeps allocated owners, tensor views, block-ID mapping, and KV group metadata alive |

The target remains a real LMCache Server. ServerBench mocks only the tensors and
metadata that would normally be supplied by an inference engine.

## Layout inputs

### Legacy physical shape

`--kvcache-shape-spec` remains the compatibility path for the existing
single-layout baseline. It is not translated into the YAML model schema and
should not be extended into a model-layout language.

### YAML model layout

Step 5 adds `--model-layout` for model-aware synthetic layouts:

```yaml
model:
  layer_definitions:
    state: {kind: kda, num_heads: 96}
    attention: {kind: mla}
  layer_types: [state, state, attention]
parallel: {tp_size: 2}
allocation: {num_blocks: 3}
```

The resolution path is:

```text
YAML
  -> ModelLayout
  -> TP-local layer definitions
  -> ComponentSpec
  -> semantic TensorSpec groups
  -> pool / offset / stride / block-domain placement
  -> allocated tensor views
  -> ModelCache
  -> TransferContext.register()
  -> existing BenchCase
```

`ComponentSpec` is the boundary between model terminology and storage
terminology. It records each cache component's row width and dtype, logical
tokens and physical slots per block, sliding-window or recurrent-state
semantics, and TP ownership.

The resulting `TensorSpec` objects describe rank-local tensor geometry,
Engine Groups, and storage placement. `allocate_layout()` creates the backing
owners and typed views, then reuses LMCache's format detection,
`group_layers_by_identity()`, and `KVLayerGroupsManager`.

## Layout modes

### `basic`

`basic` is the default, engine-independent implementation. It currently models
MHA/GQA/MQA, KDA, MLA, and DSV4 layers. Each tensor owns a separate pool, making
the layout easy to inspect while still exercising TP ownership, sliding windows,
recurrent states, grouping, registration, and transfer.

### `vllm`

`vllm` emulates selected concrete vLLM cache layouts, including their page
sizing, alignment, padding, grouping, and pool sharing. Because these details
are ABI-sensitive, support is deliberately explicit rather than generic.

Step 5 supports:

- DSV4 attention with `fp8_ds_mla`;
- KDA + MLA with `bfloat16` for the Kimi K3 layout.

Unsupported combinations are rejected. This mode reproduces tensor geometry
for LMCache validation; it does not launch vLLM or run inference.

## Design rules

1. `BenchCase` owns test flow and assertions; layout code does not.
2. Layout resolution produces rank-local tensor specs before allocation.
3. Model semantics are configured; physical KV format is detected from the
   allocated tensors.
4. Engine Groups define logical block-ID domains. Physical KV groups are
   derived with LMCache's production grouping code.
5. Transfer and platform mechanisms stay in `TransferContext` and platform
   implementations, not in model-layout code.
6. The legacy shape path and the YAML model-layout path stay explicit and
   independent.
7. Engine-specific emulation must reject unsupported ABI combinations rather
   than silently approximate them.
8. Every path ultimately runs a `BenchCase` against a real LMCache Server.

## Current scope

The existing legacy baseline covers CPU/GPU modes and LMCache-driven or
engine-driven transfer where supported.

The Step 5 YAML model-layout path currently has narrower runtime support:

- synthetic TP ranks only;
- GPU LMCache-driven transfer;
- separate object groups;
- no PP, DCP, multi-server placement, or remote worker orchestration;
- no Hugging Face `config.json` ingestion;
- no generic vLLM, SGLang, or model-inference compatibility claim.

These limits are deliberate. A `WorkerPlan` or `MockWorker` abstraction should
be introduced only when a concrete multi-worker topology requires it.

## Correctness requirements

The benchmark must preserve these invariants:

- cold LOOKUP misses and warm LOOKUP hits the expected block range;
- STORE data becomes visible before the warm pass begins;
- RETRIEVE restores the exact bytes written by every synthetic rank;
- CUDA tensors are copied to CPU before NumPy checksum conversion;
- registration and transfer use production LMCache grouping and context code;
- all sessions, locks, tensor views, owners, and transfer contexts are released.

The STORE visibility check is bounded and observes LOOKUP/prefetch state; it is
not an arbitrary sleep and does not redefine the framework's STORE completion
contract.

## Roadmap

- [x] **Step 1 — Extract data models** (#4820)
- [x] **Step 2 — Extract `ServerBenchClient`** (#4829)
- [x] **Step 3 — Extract the cold/warm flow into `BenchCase`** (#4883)
- [x] **Step 4 — Reuse production `TransferContext`** (#4948)
- [ ] **Step 5 — Add configurable synthetic model layouts** (#5165)
  - add typed YAML `ModelLayout` configuration;
  - resolve TP-local component and tensor specs;
  - provide engine-independent `basic` layout generation;
  - emulate the selected DSV4 and Kimi K3 vLLM layouts;
  - allocate/register `ModelCache` and run the existing benchmark flow.

Possible follow-ups should be driven by concrete test cases:

- separate runtime ownership further if it simplifies the client;
- add PP/DCP/multi-server planning when those cases are implemented;
- add more engine layouts only with a pinned ABI and validation target;
- add partial-hit, cancellation, failure, and session-isolation cases.

## Non-goals

This RFC does not make ServerBench responsible for:

- model execution, attention correctness, or model accuracy;
- TTFT, TPOT, or serving throughput measurement;
- loading model weights;
- engine-side KV eviction policy;
- importing the full vLLM/SGLang runtime;
- a YAML DSL for benchmark control flow;
- speculative topology abstractions without an exercised use case.

Real-engine E2E tests remain necessary. ServerBench provides a smaller,
deterministic layer for validating LMCache's KV data plane below them.


## 评论 (5)

### maobaolong · 2026-09-02

@riversky0014 I found there is another aspect to improve the server_bench, i'm not quite sure whether we can reusethe lmcache/v1/multiprocess/transfer_context/worker_transfer.py to separate lmcache_driven and engine_driven logic into individual files.

The core idea behind ServerBench is to simulate VLLMs along with LMCache, include vllm, lmcache_mp_connector, and vllm_mp_adapter. The goal is to reuse their existing abstract layering rather than spreading logical concepts flat across the Server bench command, the helper, or the runtime you've refactored on the backend.

### riversky0014 · 2026-09-02

Thanks, this make sense. ServerBench should only mock the engine side, such as rank-local KV tensors, topology, and request flow.
For registration and transfer, reusing `TransferContext` and the existing platform abstraction looks much better than maintaining seperate CPU/GPU and  lmcache-driven/engine-driven branched in ServerBench.

I'll design the mock flow around a KV layout description and parallel topology to build rank-local tensors, then follow the Connector/Adapter structure and reuse infrastructure such as `TransferContext`. This should keep ServerBench as close as possible to the real engine integration flow

### rishabhsinha17 · 2026-09-07

@riversky0014 @maobaolong on designing the mock flow around a KV layout description, the physical half of that description may already exist in #4592. It adds a declarative KVLayoutDescriptor per EngineKVFormat member, an axis vocabulary plus an ordering that shape, stride, and contiguity facts derive from, with an exhaustive round trip test pinning the descriptor set to the enum so the two cannot drift. All 17 current members are covered.

The natural place for it in this design is between TensorGroupProfile and SyntheticTensorSpec. If resolve_worker_plans derives each rank's tensor shapes and strides from the descriptor of the intended format instead of hand written per format recipes, the bijection guarantees the mock allocation lands on that format under real detection. A new format then costs a descriptor entry rather than new mock code, and your DSA example, MLA plus indexer tensor groups in one engine group, becomes expressible before any engine integration exists. Today's #5002 is exactly that kind of layout tripping a layer count assumption, so expressing it without an engine has immediate value.

Happy to co-design and implement that piece on top of the TransferContext reuse. I am reviewing #4948 with this in mind.

### riversky0014 · 2026-09-08

@rishabhsinha17 thanks, this fits what I had in mind. After #4592 merged, I'll put `KVLayoutDescriptor` directly on `TensorGroupProfile`, and have `resolve_worker_plans()` fill each rank's dimensions based on topology to produce `SyntheticTensorSpec`, this will be more elegant.

I'm also considering renaming `KVLayoutProfile` to `KVCacheProfile`, since it covers layers membership, engine groups and logical cache semantics, while `KVLayoutDescriptor` describes the physical structure. That should make the distinction clearer.

Happy to work through the detials together, and thanks for reviewing #4948 ~

### rishabhsinha17 · 2026-09-10

@riversky0014 agreed on `KVCacheProfile`, the profile describes the cache itself, layer membership and engine groups, and the physical side already has its name in the descriptor. No need to wait on #4592 either, I can start the `KVLayoutDescriptor` on `TensorGroupProfile` wiring on top of your branch now. I would keep the descriptor import local to the bench until #4592 merges, so this piece does not serialize behind that review queue. Happy to work through the details.

