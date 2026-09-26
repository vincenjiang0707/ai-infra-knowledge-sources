# [Issue #2233] RFC: native GPUNetIO PUT and completion through the common GPU Device API

source: https://github.com/ai-dynamo/nixl/issues/2233
state: open | updated: 2026-09-09T16:07:54Z
labels: 

## 正文

## Proposal

Follow-up to #2232's Device API item: implement native GPUNetIO PUT and
completion polling behind the existing NIXL GPU memory-view API.

The initial opt-in scope is deliberately bounded: THREAD execution, ordinary
registered VRAM on the engine GPU, one remote peer, and one accepted/unretired
PUT per shared data QP. The application kernel submits the WRITE directly;
there is no host posting or CPU-proxy fallback. Native mode owns its CQ and
does not start the legacy data-progress kernel.

Submission returns IN_PROG; a nonblocking ticket-based query reports completion
and caches terminal status. Errors latch the lane. Local views pin MRs, and
unretired view dependencies are retained until QP teardown. Callers must preserve
payload and registration lifetime and use cold preparation/release operations.
Sender completion is not an application receiver-ready signal.

## Interface questions

1. Is engine-scoped execution-mode reporting plus tagged public memory-view
   wrappers the appropriate integration point alongside #2111/#2147 and the
   CPU-proxy work?
2. Is reserving four bytes of the existing 64-byte device status acceptable,
   subject to proving the UCX request fits the remaining 60 bytes?
3. How should the plugin ABI extension be versioned? The local prototype uses
   ABI 2 and requires rebuilding core, plugins and CUDA consumers together.
4. Is this single-flight PUT/completion milestone a useful first review unit,
   with atomics, cooperative execution, multiple peers and receiver signaling
   deferred?

## Prototype and evidence

A local stacked implementation exists on upstream revision 8585eee0 plus
#2052/#2174/#2175/#2178 foundations and #2196's allocator. It uses the legacy
DOCA 3.1 completion helper from #2222. A linked Draft PR will expose the code
for discussion, not request merge approval or imply design acceptance.

Two independent H20 endpoint pairs passed normal-path tests: 4 KiB/64 KiB/1 MiB,
8193 distinct-slot wrap PUTs, payload/guard validation, cached completion,
busy and invalid-argument rejection. Host wrapper tests and legacy READ/WRITE
regression also passed. No performance claim is made.

Still unverified: hardware fault injection, the UCX/dual-backend matrix,
concurrent submitters, additional cross-engine/null-placeholder cases and
native-path tracing. The complete acceptance matrix is not claimed finished.

Please advise on the interface/ABI and review split before this prototype is
promoted beyond draft. Existing host-mode fixes and performance PRs are separate.


## 评论 (1)

### foraxe · 2026-09-09

Prototype for the design discussion: #2234 (Draft). Normal-path validation, dependencies, ABI changes and unverified cases are listed in the PR; this is not a request for merge approval.
