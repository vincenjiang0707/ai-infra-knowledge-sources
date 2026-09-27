# [Issue #4323] [Bug]: TCP transport stages device memory with synchronous cudaMemcpy on the legacy stream, so a read waits behind the peer's queued GPU work

source: https://github.com/kvcache-ai/Mooncake/issues/4323
state: open | updated: 2026-09-25T02:59:39Z
labels: 

## 正文

### Bug Report

The TCP transport's CUDA staging copies run on the legacy default stream. So a transfer of device memory waits for every kernel the process already has queued on that device, and the thread doing the copy sits in `cudaMemcpy` the whole time. I hit this in [M*](https://github.com/mstar-project/mstar), where streamed tokens were reaching the client two at a time.

**Where.** `mooncake-transfer-engine/src/transport/tcp_transport/tcp_transport_session_impl.h` uses a plain `cudaMemcpy(..., cudaMemcpyDefault)` in all four directions:

- `ServerSession::writeBody` (main L261)
- `ServerSession::readBody` (main L351)
- `ClientSession::readBody` (main L812)
- `ClientSession::writeBody` (main L876)

It's the same in 0.3.13.post1, v0.3.14-rc1 and main. The `USE_MACA` build already goes through `copyTcpCudaMemory` (a non-blocking stream, `cudaMemcpyAsync`, then a sync of that stream). The CUDA build doesn't.

PyTorch and most inference engines run their compute on the legacy stream, and a serving process usually has its next step queued by the time a peer reads its last output. So an 8-byte read waits for that whole step. On a host without an RDMA NIC, `protocol="rdma"` falls back to this transport (the engine logs `Using TCP transport`), so single-host setups hit it without ever asking for TCP.

**Repro.** Two processes on one H100, each with its own `TransferEngine` (P2PHANDSHAKE). R reads S's device buffer into its own device buffer with `batch_transfer_sync_read`. One side first queues a fixed batch of bf16 matmuls (about 77 ms of GPU work), and the read starts 5 ms later. Meanwhile the busy side times one small pinned D2H copy of its own, on a separate non-blocking stream.

| 8 B read | 0.3.13.post1 | 0.3.14-rc1 | busy side's own copy |
|---|---|---|---|
| nothing queued | 0.16 ms | 0.13 ms | - |
| S (serving) busy, legacy stream | 37.45 ms | 36.54 ms | 32-33 ms |
| S busy, non-blocking stream | 0.20 ms | 0.24 ms | 0.10 ms |
| R (reading) busy, legacy stream | 38.71 ms | 38.22 ms | 33 ms |
| R busy, non-blocking stream | 0.78 ms | 0.52 ms | 0.10 ms |

64 KiB reads look the same (37.71 / 0.33 / 38.49 / 0.28 ms for the four busy rows). With the busy side's work on a non-blocking stream the reads drop back under a millisecond, so this is ordering on the legacy stream, not the GPU being busy. The data was correct in every run.

Two things I can't explain yet. The busy side's own copy is on a non-blocking stream and still blocks for about 33 ms while the transport's `cudaMemcpy` is waiting. And a 4 MiB read took 41.64 ms with S busy on a non-blocking stream (7.08 ms with nothing queued), while R busy on a non-blocking stream gave 6.47 ms. So at larger sizes something besides stream ordering makes the serving side wait.

To check the fix direction, I used an `LD_PRELOAD` shim that reroutes small (<= 4 KiB) `cudaMemcpy` calls of kind D2H or Default to `cudaMemcpyAsync` on a private non-blocking stream, followed by `cudaStreamSynchronize` of that stream. With it, the S-busy read went to 2.30 ms, the R-busy read to 0.27 ms, and the busy side's own copy to 0.10 ms.

In M* this showed up as 18.9% of client inter-token gaps under 1 ms at concurrency 1, against 0.0% over M*'s shared-memory transport. Bagel chat at concurrency 16 ran 10.0-10.3 req/s over this path and 16.0-16.5 req/s over shared memory (same build, same session). M* can avoid it on a single host by using shared memory, but anyone who picks the transfer engine on a host without an RDMA NIC still hits it.

**Suggested fix.** Do what the MACA branch does, but keep the stream around instead of creating one per copy: one non-blocking stream per device, and `cudaMemcpyAsync(..., stream)` plus `cudaStreamSynchronize(stream)` in place of each `cudaMemcpy`. Pinning the staging buffer (it's reused since #3562) would also let the copy engine DMA it directly. I haven't checked whether that fixes the 4 MiB case.

One behavior change to be aware of: today the legacy-stream copy also waits for kernels still writing the buffer, so a caller that exposes a buffer before its writes finish gets correct data by accident. After the change it wouldn't. M* publishes a pointer only after the producing step's CUDA event has completed, so this is fine for us, but it may be worth documenting.

Related: #3446 (the TCP transport RFC, which touches the same staging code), and #2843 and #3562 (staging cost, not ordering). I haven't tested hosts with an RDMA NIC, where the RDMA transport moves device memory without these copies.

**Environment.** H100 80GB HBM3, driver 595.71.05, CUDA 12.9 runtime (PyTorch 2.12.1+cu129), Python 3.12, `mooncake-transfer-engine` 0.3.13.post1 and 0.3.14rc1 wheels, single host, no RDMA NIC.

### Before submitting...

- [x] Ensure you searched for relevant issues and read the documentation


## 评论 (6)

### github-actions[bot] · 2026-09-24

Thanks for opening this issue, @Gaurav-Shah05!

| Field | Value |
|-------|-------|
| **Issue** | #4323 |
| **GitHub user ID** | `73552538` |
| **Reporter** | @Gaurav-Shah05 |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### he-yufeng · 2026-09-25

Picking this up. The fix mirrors the existing `USE_MACA` path: give every GPU build the non-blocking-stream copy and route all four staging sites through it, instead of the CUDA build sitting in a legacy-stream `cudaMemcpy`.

One note on the neighbor: #4233 pipelines CUDA staging but deliberately keeps `cudaStreamDefault` (legacy-stream semantics) for its session stream, so the stall you measured survives it. This fix is complementary; whichever lands second rebases.


### Gaurav-Shah05 · 2026-09-25

Edit: just saw #4324, which is the same change, so the numbers below should apply to it too. Happy to run it through the same repro.

Thanks for picking this up! I tried the same approach locally (all four staging sites through `copyTcpCudaMemory`, with one cached non-blocking stream per io thread per device instead of one per copy), and wanted to share what I found before you get too far. It fixes the stall, but it regresses one case, so I didn't open a PR.

Same `mc_w2w` repro as in the issue, medians of 7, two runs per build:

| read | main | legacy stream swapped for a non-blocking one |
|---|---|---|
| 8 B, R busy on legacy stream | 38.4-39.2 ms | 0.36-0.37 ms |
| 8 B, S busy on legacy stream | 38.6-39.4 ms | 1.71-1.86 ms |
| busy side's own copy meanwhile | 33-35 ms | 0.06-0.10 ms |
| 4 MiB, R busy on legacy stream | 38.3-38.6 ms | 4.9-5.2 ms |
| **8 B, S busy on a non-blocking stream** | **0.35-0.36 ms** | **1.71-1.78 ms** |
| 4 MiB, S busy (either stream) | 37.7-45.5 ms | 43.6-45.5 ms |

The last-but-one row is the regression. A process that already runs its compute on a non-blocking stream was fine before, and now the serving side's D2H takes about 1.4 ms longer. My guess is the async D2H into the pageable staging buffer: it waits for the kernel that's running (each queued matmul is ~3.5 ms, so ~1.75 ms on average). That would also explain why S-busy reads stay at ~1.7 ms instead of dropping to idle. I haven't tested pinning yet, so that's just a guess. #4233 moves staging to pinned buffers, so the stream change on top of it might fix both. The 4 MiB S-busy wait doesn't move with either version, so something else is going on there.

I also wrote a test that might be useful: `tcp_cuda_staging_test.cpp` gates the legacy stream with a `cudaLaunchHostFunc` that blocks until released, then does a TCP WRITE and READ of device memory. On main both time out after 15 s; with the change it passes 5/5. It doesn't depend on timing, and it skips without a GPU.

Happy to work with you on this: I can push the branch and the test somewhere you can pull from, or rerun the repro on whatever you put up (with or without #4233). Let me know what's most useful.

### he-yufeng · 2026-09-25

Thanks for running this down, the regression row is real and I think your mechanism is the right one. `cudaMemcpyAsync` against pageable staging degrades: the driver stages it through an internal path that can wait behind an in-flight kernel, so the serving side's D2H picks up roughly half a queued matmul. The legacy-stream synchronous copy didn't hit that case because it never synchronized with your non-blocking compute stream in the first place.

How I weigh the trade: what main does to the legacy-stream case is an unbounded stall behind the peer's entire queued GPU work (your 38 ms is just the queue you happened to have), while the regression is a bounded ~1.4 ms in a case that pinned staging should close entirely. So the stream change is still the right default, but the residual is worth closing rather than hand-waving.

On composition: #4233's pinned buffers are exactly what makes the async copy fully async. #4324 keeps pageable staging on purpose to stay orthogonal, so whichever of the two lands second owns the re-measure. If you have a #4233 tree handy, the most useful single datapoint is your mc_w2w matrix on #4324 + #4233 together, especially the 8 B S-busy-on-non-blocking row.

And yes please to the test: a `cudaLaunchHostFunc`-gated legacy-stream repro that skips without a GPU is exactly the shape this repo's CI can run. If you push `tcp_cuda_staging_test.cpp` somewhere I can pull from, I'll integrate it into #4324 with you credited in the commit; alternatively attach it here and I'll adapt it.

### Gaurav-Shah05 · 2026-09-25

Thanks, agreed on the trade. An unbounded stall behind the peer's whole queue is worse than a bounded ~1.4 ms that pinned staging should close.

Here's the test. It adds one case to the existing `tests/tcp_cuda_staging_test.cpp`, so no CMake change: the target is already there from #3562. The diff applies cleanly to current main and on top of #4324.

How it works: `LegacyStreamGate` puts a `cudaLaunchHostFunc` on `cudaStreamLegacy` that blocks until released, so the legacy stream stays busy as long as the test wants, with no kernel and no nvcc. Then a TCP WRITE and READ of device memory have to complete while it's blocked, which goes through all four staging sites. `runOne` already bounds each transfer at 15 s, and the gate's destructor releases the stream, so a failure can't hang CI. It skips without a GPU.

On my side, on main both transfers come back TIMEOUT and the test fails (30.7 s total); with the stream change it passes 5/5. I haven't run it on your branch yet, but it should pass there too, since the per-copy stream isn't the legacy one.

<details>
<summary><code>tcp_cuda_staging_test.cpp</code>: add <code>StagingDoesNotWaitForTheLegacyStream</code> (git apply)</summary>

```diff
diff --git a/mooncake-transfer-engine/tests/tcp_cuda_staging_test.cpp b/mooncake-transfer-engine/tests/tcp_cuda_staging_test.cpp
index b4e674a7..b898b913 100644
--- a/mooncake-transfer-engine/tests/tcp_cuda_staging_test.cpp
+++ b/mooncake-transfer-engine/tests/tcp_cuda_staging_test.cpp
@@ -17,6 +17,7 @@
 #include <chrono>
 #include <cstdlib>
 #include <cstring>
+#include <future>
 #include <memory>
 #include <optional>
 #include <string>
@@ -71,6 +72,34 @@ class DeviceBuffer {
     void* data_ = nullptr;
 };
 
+// a host function blocked until release(), not a long kernel: this file builds
+// without nvcc, and the legacy stream stays busy however long the copy takes
+class LegacyStreamGate {
+   public:
+    ~LegacyStreamGate() {
+        release();
+        cudaStreamSynchronize(cudaStreamLegacy);
+    }
+
+    cudaError_t close() {
+        return cudaLaunchHostFunc(cudaStreamLegacy, &wait, this);
+    }
+
+    void release() {
+        if (!released_) open_.set_value();
+        released_ = true;
+    }
+
+   private:
+    static void wait(void* gate) {
+        static_cast<LegacyStreamGate*>(gate)->opened_.wait();
+    }
+
+    std::promise<void> open_;
+    std::future<void> opened_ = open_.get_future();
+    bool released_ = false;
+};
+
 TransferStatusEnum runOne(TransferEngine* engine,
                           const TransferRequest& request) {
     auto batch_id = engine->allocateBatchID(1);
@@ -183,4 +212,58 @@ TEST(TcpCudaStagingTest, ReusesStagingAcrossChunksAndRequests) {
     engine.reset();
 }
 
+TEST(TcpCudaStagingTest, StagingDoesNotWaitForTheLegacyStream) {
+    int device_count = 0;
+    cudaError_t cuda_status = cudaGetDeviceCount(&device_count);
+    if (cuda_status != cudaSuccess || device_count == 0) {
+        GTEST_SKIP() << "CUDA device unavailable";
+    }
+    ASSERT_EQ(cudaSetDevice(0), cudaSuccess);
+
+    constexpr size_t kTransferSize = 64 * 1024;
+    constexpr size_t kBufferSize = 2 * kTransferSize;
+
+    DeviceBuffer device_buffer;
+    ASSERT_EQ(cudaMalloc(device_buffer.out(), kBufferSize), cudaSuccess);
+
+    auto engine = std::make_unique<TransferEngine>(false);
+    const std::string server_name = "127.0.0.2:17932";
+    const auto hostname_port = parseHostNameWithPort(server_name);
+    ASSERT_EQ(engine->init(P2PHANDSHAKE, server_name,
+                           hostname_port.first.c_str(), hostname_port.second),
+              0);
+    ASSERT_NE(engine->installTransport("tcp", nullptr), nullptr);
+    ASSERT_EQ(
+        engine->registerLocalMemory(device_buffer.get(), kBufferSize, "cuda:0"),
+        0);
+
+    const auto segment_id = engine->openSegment(engine->getLocalIpAndPort());
+    const auto segment_desc =
+        engine->getMetadata()->getSegmentDescByID(segment_id);
+    ASSERT_NE(segment_desc, nullptr);
+    ASSERT_FALSE(segment_desc->buffers.empty());
+    const uint64_t remote_base = segment_desc->buffers[0].addr;
+
+    LegacyStreamGate gate;
+    ASSERT_EQ(gate.close(), cudaSuccess);
+
+    TransferRequest write;
+    write.opcode = TransferRequest::WRITE;
+    write.length = kTransferSize;
+    write.source = device_buffer.get();
+    write.target_id = segment_id;
+    write.target_offset = remote_base + kTransferSize;
+    EXPECT_EQ(runOne(engine.get(), write), TransferStatusEnum::COMPLETED)
+        << "a WRITE of device memory waited for the legacy default stream";
+
+    TransferRequest read = write;
+    read.opcode = TransferRequest::READ;
+    EXPECT_EQ(runOne(engine.get(), read), TransferStatusEnum::COMPLETED)
+        << "a READ of device memory waited for the legacy default stream";
+
+    gate.release();
+    EXPECT_EQ(engine->unregisterLocalMemory(device_buffer.get()), 0);
+    engine.reset();
+}
+
 }  // namespace
```

</details>


### he-yufeng · 2026-09-26

Integrated into #4324 as f5b6889f8 with you credited in the commit message. Reviewed the gate mechanics before landing it: the launch blocks the legacy stream until release, the destructor releases and syncs so a failure can't hang CI, and the double-release guard covers the explicit-release path. One disclosure for reviewers: I can't compile the CUDA test target on this machine (no toolkit/GPU), so its verification is your two runs (main times out both transfers, patched build passes 5/5) plus GPU CI.
