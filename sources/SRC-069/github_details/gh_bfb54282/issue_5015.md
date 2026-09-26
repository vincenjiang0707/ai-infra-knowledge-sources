# [Issue #5015] [Bug] sparse MLA SM120 hangs when a CUDA-graph-captured decode batch is padded (spec-decode q_len>1) on SM121/GB10

source: https://github.com/flashinfer-ai/flashinfer/issues/5015
state: closed | updated: 2026-09-19T14:58:32Z
labels: needs-triage

## 正文

### Summary

On SM121 (GB10), `FLASHINFER_MLA_SPARSE_SM120` hangs when a **full CUDA-graph replay** is handed a
speculative-decode batch whose row count was **padded up to a larger captured size**. The kernel never
returns: all GPUs sit at 96% utilization while the host worker threads are idle in
`poll_schedule_timeout`, so it is a device-side hang, not a CPU-side wait.

The same batch shape runs clean when that exact size is captured, and clean in `PIECEWISE` mode or
under `--enforce-eager`. The kernel math is not the problem; what the padded rows carry into the
captured graph is.

This is distinct from #3700 / PR #4732 (the sparse-MLA barrier race). We ship that fix and it does not
cover this. It may be related to #5001 (`test_sparse_mla_sm120` timing out in Spark CI, 488 timeout
nodes, first seen 2026-09-04) though the symptom shape differs: ours is a production CUDA-graph replay
hang with a precise trigger, not a unit-test timeout.

### Environment

| | |
|---|---|
| GPU | NVIDIA GB10, compute capability 12.1 (8x DGX Spark, TP8 over 200GbE RoCE) |
| FlashInfer | 0.6.18.dev20260819 (includes PR #4732) |
| vLLM | 0.1.dev20051+g487ecf187 (main, 2026-08-25) |
| torch / CUDA | 2.13.0+cu130 / 13.0 |
| Backend | `FLASHINFER_MLA_SPARSE_SM120`, `sparse_mla_force_mqa: true`, KV `fp8_ds_mla` |
| Model | GLM-5.3 native FP8 (`glm_moe_dsa`, kv_lora_rank 512, qk_rope_head_dim 64, index_topk 2048) |

### The trigger, precisely

With MTP `num_speculative_tokens=1`, each sequence contributes 2 query rows. vLLM's default capture
list (1, 2, 4, 8) produces full decode graphs at 2, 4 and 8 rows only. The first step in which a third
sequence joins is **6 rows, which pads into the captured 8-row graph, and that replay never returns.**

That also explains an otherwise confusing earlier table: `max_num_seqs 8` plain decode (8 rows, captured
exactly) is fine; MTP at 2 sequences (4 rows, captured exactly) is fine; MTP at 3 sequences (6 to 8) is
fatal.

### Bisection, one variable per boot

| k=1 graph setting | C3 (6 rows) | C4 (8 rows) |
|---|---|---|
| default capture sizes 1,2,4,8, FULL | **HANG** | not reached |
| `cudagraph_mode: PIECEWISE` (attention outside the graph) | ok | ok |
| `--enforce-eager` | ok | ok |
| capture sizes 1..8, FULL (6 captured exactly) | **ok**, 26.1 tok/s | ok, 32.9 tok/s |

And by speculative depth, all with graphs on: k=2 (q_len 3, batches 9 and 18) survives; k=3 (q_len 4)
survives. They survive only because their reachable row counts never land on a padded full graph.

Ruled out by measurement, each on its own boot: `--no-async-scheduling`, `disable_padded_drafter_batch`,
the V2 model runner, and PR #4732 itself.

### Failure signature

```
RPC call to sample_tokens timed out (300 s) -> EngineDeadError
num_running_reqs=3, kv_cache_usage ~0.85%, no preemption, spec tokens [-1]
all 8 ranks: GPU utilization 96%, worker threads idle in poll_schedule_timeout
```

### Config-only reproducer

No kernel-level harness needed. On SM121 with a sparse-MLA (DSA) checkpoint:

```bash
vllm serve <sparse-mla-model> \
  --attention-backend FLASHINFER_MLA_SPARSE_SM120 \
  --attention-config '{"sparse_mla_force_mqa": true}' \
  --kv-cache-dtype fp8_ds_mla \
  --speculative-config '{"method":"mtp","num_speculative_tokens":1}' \
  --max-num-seqs 4 --max-model-len 32768
# then drive THREE concurrent completion requests -> hang
# add --compilation-config '{"cudagraph_capture_sizes":[1,2,3,4,5,6,7,8]}' -> no hang
```

### Suspected cause

Whatever the padded rows carry into the captured graph: sparse indices / `seq_lens` for rows beyond
`num_actual_tokens`. A stale or `-1` entry there would produce exactly this signature, a kernel that
never returns with the device busy and the host idle. A defensive fix would either sanitize those rows
or make the kernel bounds-safe against them.

### Workaround for anyone hitting this

Capture every reachable batch size, `1..max_num_seqs*(k+1)`:

```
--compilation-config '{"cudagraph_capture_sizes":[1,2,...,max_num_seqs*(k+1)]}'
```

or use `cudagraph_mode: PIECEWISE`. Default capture sizes with k=1 are the trap. With every reachable
batch captured we now run MTP k=2 in production at 64K context and 6 sequences.

### Offer

Happy to run a candidate patch on 8x GB10 (SM121) and report back; this lane reproduces the hang
deterministically at three concurrent requests.


## 评论 (13)

### 200lz · 2026-09-08

The 6→8 differential is strong enough that I’d first remove vLLM from the loop. I can add a focused SM120 CUDA-graph repro that captures 8 rows and replays 6 real rows plus 2 padded rows, then vary the padded sparse indices / sequence metadata one field at a time. Once one field is sufficient to reproduce the non-return, I’d fix the validity contract at that owner rather than adding a generic thread-level early return inside the kernel, which could be unsafe around barriers. If useful, I’ll post the minimal metadata tuple before proposing the implementation.

### SBE247Emperor · 2026-09-09

@200lz yes, please. A standalone SM120 repro that takes vLLM out of the loop is the right next step, and I agree with the fix shape: establish and enforce the validity contract at the owner of the padded rows, not a generic thread-level early return inside the kernel. Anything that returns early near the barriers in this kernel family is exactly what #3700 / #4732 taught us to be careful with.

Posting the minimal metadata tuple first is welcome. If it helps, these are the parts of our configuration a focused repro should preserve so it is exercising the same path:

- `FLASHINFER_MLA_SPARSE_SM120` with `sparse_mla_force_mqa: true`, KV cache `fp8_ds_mla`
- DSA geometry: `kv_lora_rank 512`, `qk_rope_head_dim 64`, `index_topk 2048`
- spec-decode shape: `q_len 2` per sequence (MTP k=1), 3 real sequences = 6 real rows replayed through an 8-row capture, so 2 padded rows
- the padded rows are what vLLM leaves beyond `num_actual_tokens`: sparse indices and `seq_lens` for rows that were not written this step. My guess is a stale or `-1` entry there, but that is the hypothesis your one-field-at-a-time sweep would settle
- versions from the failing lane: FlashInfer 0.6.18.dev20260819 (includes #4732), vLLM main `487ecf187` (2026-08-25), torch 2.13.0+cu130, GB10 compute capability 12.1

One related data point since I filed this: on #5001, Champollion9012 reports the `test_sparse_mla_sm120` suite passing 488/488 in about fourteen seconds on discrete SM120 (RTX PRO 6000 Blackwell, cc 12.0), and notes the file gates on `is_sm12x_supported`, which admits both `is_sm120a` and `is_sm121a`. I cannot tell from here whether that means the same kernel behaves differently on SM121 or whether both Spark reports share a runner artifact, but it does suggest the padded-graph hang may be SM121-specific, so a repro that runs on both a discrete SM120 card and a GB10 would be more informative than either alone.

The offer stands: I can run your repro and any candidate patch on 8x GB10 (SM121, TP8) and report back. This lane reproduces the hang deterministically at three concurrent requests with default capture sizes, and stays clean with every reachable size captured, so it is a clear pass/fail oracle for whatever you propose.


### bkryu · 2026-09-09

Hi @SBE247Emperor, thanks for reporting this. #5048 I have a fix for a non-deterministic hang on DGX Spark, where the hang is caused by DGX Spark having a small number of SMs.

Can you see if #5048 fixes the issue?

### 200lz · 2026-09-09

Thanks @bkryu — #5048 is worth running on the reporter's GB10 lane, and I'd like it to be part of the same experiment.

I think there may be two independent hangs here, though. #5048 is in the swapAB *prefill* kernel and matches the intermittent `test_sparse_mla_sm120` timeout in #5001. #5015 is deterministic and sits on the decode step, and I can now reproduce it **without invoking FlashInfer at all**: at vLLM `487ecf187` the 6→8 FULL-graph replay (MTP k=1) pads a fourth request with `seq_len = 0`, the DSA indexer turns that into a per-token context length of `0 - 2 + 0 + 1 = -1` for its first row, and vLLM's own pre-#51538 `persistent_topk` (the top-k backend selected on SM12x) reads that as `uint32`, takes the multi-CTA radix path while its peer CTAs took the `max_seq_len <= RADIX_THRESHOLD` early exit, and spins forever in `wait_ge`. The FlashInfer decode is queued later on the same stream and never runs, which is why it presents as a sparse-MLA hang. On an RTX PRO 6000 (SM120) the standalone kernel with the padded row lengths `[..., -1, 0]` hangs deterministically with the pre-#51538 header and passes with the post-#51538 header on identical input; FlashInfer's decode, on both the 2026-08-19+#4732 tree and current main, passes a padded-row CUDA-graph matrix (all -1 / slot 0 / stale / length 0 / full width, 3000-replay soaks, compute-sanitizer clean).

vllm-project/vllm#51538 (commits 6–7, see vllm-project/vllm#51593) already fixed both the producer clamp and the kernel guard on 2026-08-15. `487ecf187` is on a fork lineage whose merge-base with vLLM main (`b908a21f`, 2026-08-12) predates that merge, so it has neither hunk.

I've prepared a one-command GB10 handoff that tests both independently: first the standalone vLLM top-k pre/post-#51538 differential (nvcc only, no model, no vLLM), then a FlashInfer-only padded CUDA-graph matrix against whatever FlashInfer build is installed, then (if `vllm` is importable) a metadata-level regression plus the #51538 hunks rebased onto `487ecf187`.

It would also be useful to run the original production repro with #5048 alone. My current expectation:

* #5048 + old vLLM: the 6→8 deterministic trigger still hangs;
* old FlashInfer + vLLM #51538 commits 6–7: it passes;
* both fixes: passes.

If #5048 alone removes the production trigger, the standalone top-k differential will tell us whether two bugs overlap on Spark.

@SBE247Emperor, the GB10 command is:

```bash
git clone --depth 1 -b issue5015-repro https://github.com/200lz/flashinfer fi5015 \
  && cd fi5015/repro_5015 && export PATH=/usr/local/cuda/bin:$PATH && bash gb10_handoff.sh
```

One GB10 is sufficient; no model is required for the first two steps. Expected: `topk_pre --poison` = HANG (killed at 90 s), `topk_post --poison` and the soaks = PASS, FlashInfer matrix = all PASS. Please attach the `results_*/` directory it creates. SM120 is my control; I won't call SM121 confirmed until your run comes back.


### 200lz · 2026-09-09

Status update while the GB10 run is pending:

* **Causal owner:** vLLM's DSA top-k path, not the FlashInfer decode kernel. Confirmed on SM120 (standalone pre-#51538 `persistent_topk` + padded row length `-1` = deterministic wedge; post-#51538 = pass on identical input; FlashInfer padded-row CUDA-graph matrix clean on both the reporter-era tree and main). **SM121 handoff pending** — I will not call SM121 confirmed until the GB10 results above come back.
* **Relation to #5048:** treated as an independent hang in the swapAB *prefill* kernel (#5001). Both fixes should be carried; the GB10 command tests them separately.
* **Upstream:** vLLM already carries the fix (vllm-project/vllm#51538, commits 6–7). I opened vllm-project/vllm#56003, a test-only PR that pins the padded spec-decode context-length invariant on the real indexer builder (fails with `-1` in row 6 if the clamps are removed); the kernel-side degenerate-length test is already in the open vllm-project/vllm#55122, so it was not duplicated.
* **Durable recommendation for the reporter's fork:** rebase onto a vLLM revision that contains #51538 (main ≥ `97388c44`, 2026-08-15); `repro_5015/patches/5015-vllm-51538-commits-6-7.patch` in the handoff bundle is the same two hunks rebased onto `487ecf187` for an interim test.


### SBE247Emperor · 2026-09-09

Thanks @bkryu, and thanks for the quick turnaround. Yes, we will test #5048 on the 8x GB10 lane
and report back.

One thing worth flagging first, so the result is not misread when it arrives. Since your comment,
@200lz has assembled strong evidence that there are two independent hangs on this hardware, and
that the one I filed here is not in the FlashInfer decode kernel:

* #5048 / #5001 is the swapAB **prefill** kernel, and intermittent.
* #5015 (this issue) is deterministic and sits on the **decode** step, and the owner appears to be
  vLLM's own `persistent_topk`. A padded decode slot carries `seq_len == 0`, the DSA indexer derives
  a per-token context length of `seq_len - max_decode_len + local_idx + 1` which is negative for the
  first row of that request, and the top-k kernel consumes it as `uint32`. The leader CTA then takes
  the cooperative radix path while its peers already took the `max_seq_len <= RADIX_THRESHOLD` early
  exit, and waits on an inter-CTA barrier that can never complete. The FlashInfer decode is queued
  later on the same stream and never runs, which is why it presents here.

vllm-project/vllm#51538 (merged 2026-08-15, `97388c44`) already carries both halves of that fix:
`318d623b4` clamps the producer, `f633bd67c` hardens the kernel. I checked our own lineage with the
compare API rather than taking it on trust: `487ecf187` diverged from main at `b908a21f`
(2026-08-13T05:57:59Z) and is 93 commits behind `97388c44`, so this lane has neither hunk. Note the
trap for anyone triaging from version strings: `487ecf187` is dated 2026-08-25, ten days *after* the
fix merged, so it looks like it should contain it.

So my expectation matches @200lz's: #5048 alone probably will not clear the trigger I reported here,
and that would not be evidence against #5048. We will run the two independently rather than
together, so the results stay separable and you get a clean answer on the prefill fix either way.

Timing, honestly: this lane is inside an endurance-qualification window that closes 2026-09-14, and
the first step of @200lz's repro deliberately wedges a kernel for 90 s, which would disturb that
measurement. We will run the full matrix in the maintenance window immediately after that date and
post the results. If a partial answer is useful sooner, I can bring #5048 forward on its own, since
testing it does not require the deliberate wedge. Say the word and I will prioritise it.

Apologies for aiming the original report at the wrong component. The SM121 confirmation is still
outstanding and we are the ones holding that hardware, so we will close that loop regardless of
which fix turns out to own it.


### SBE247Emperor · 2026-09-09

@200lz This is excellent work, thank you. I can independently confirm the lineage half of it from
the reporting side, and I have one correction and two additions.

**Confirmed.** Against `vllm-project/vllm` with the compare API: the merge base of `487ecf187` with
main is `b908a21f`, and relative to `97388c44` (the #51538 merge) `487ecf187` is ahead 142 /
behind 93. This lane therefore has neither `318d623b4` nor `f633bd67c`. Worth stating plainly for
anyone who finds this thread later: `487ecf187` is dated 2026-08-25, ten days after #51538 merged,
so the version string looks like it should already contain the fix. It does not. Comparing dates
will mislead you here; run `compare/97388c44...<your revision>` and read `status`.

**Correction.** The merge base is `b908a21f9a44` at 2026-08-13T05:57:59Z, not 2026-08-12. It does
not change your conclusion, only the record.

**Addition 1: the exposure is not limited to MTP k=1.** Our promoted production config is k=2, so
`max_decode_len` is 3 and the first padded row derives `0 - 3 + 0 + 1 = -2`. Still negative, still
underflows. Anyone on this fork lineage is exposed at any k, not only at the k=1 shape I originally
filed.

**Addition 2, which I think corroborates your root cause from production rather than from a
harness.** The only reason this lane is currently stable is a workaround we adopted empirically
without understanding why it worked: we require the CUDA-graph capture list to contain every integer
in `1..max_num_seqs*(k+1)` (1..18 at 6 seqs, k=2), enforced by an assert at serve time. With every
reachable decode batch captured there is no padding, therefore no `seq_len == 0` row, therefore no
underflow. Your explanation accounts for that exactly, and it also predicts the original failure:
with the stock `1,2,4,8` list, three concurrent requests pad 6 real rows into an 8-row capture and
the lane wedges deterministically. That is a fairly strong independent check on the mechanism, since
the workaround was derived from a bisection that never went near the top-k kernel.

**On the handoff.** The bundle reviewed cleanly here. I specifically appreciate that every wedging
step is bounded by `timeout -s KILL`, that steps 2 and 3 self-skip rather than half-running, and
that step 3 prints the patch command instead of applying it to the reader's checkout.

**Timing.** This lane is inside an endurance-qualification window that closes 2026-09-14, and step
1's deliberate 90 s wedge would disturb it, so I will run the full handoff in the maintenance window
immediately after that and attach the `results_*/` directory. It will be GB10 / SM121, cc 12.1,
FlashInfer 0.6.18.dev20260819, vLLM `487ecf187`, TP8, so it should be exactly the SM121 control you
are missing next to your SM120 results.

Independently of the repro, we are taking your durable recommendation and rebasing onto a revision
that contains #51538. Thank you for chasing this down to the actual owner. It also retires a
standing invariant on our side that we had been treating as a property of the hardware.


### bkryu · 2026-09-09

Thanks @SBE247Emperor and @200lz. I'd like to followup here.

As per @200lz's exoneration matrix, it seems like no FlashInfer fix is needed for the current issue. #5048 is merged but scoped to #5001. It seems like the deterministic decode hang is vLLM-owned. Am I understanding this correctly?

### SBE247Emperor · 2026-09-09

@bkryu Yes, that is right on all three points.

**#5015 needs no FlashInfer-side change.** The owner is vLLM's DSA top-k path. A padded decode slot
carries `seq_len == 0`, the indexer derives `seq_len - max_decode_len + local_idx + 1`, which is
negative for that request's first row (-1 at k=1, -2 at our promoted k=2), and `persistent_topk`
consumes it as `uint32`. The leader CTA then takes the cooperative radix path while its peers already
took the `max_seq_len <= RADIX_THRESHOLD` early exit, and waits on an inter-CTA barrier that can never
complete. The FlashInfer decode is queued later on the same stream and never runs, which is the only
reason this surfaced as a sparse-MLA hang. vllm-project/vllm#51538 (`97388c44`: `318d623b4` producer
clamp, `f633bd67c` kernel guard) already carries both halves; our fork lineage diverged two days
before it merged, which is ours to fix, and we are rebasing.

**#5048 is scoped to #5001** — swapAB prefill, intermittent — and is a separate defect from this one.

Two things before you close this out.

1. Could you leave #5015 open until roughly 2026-09-15? @200lz's matrix is an SM120 control and he has
   said he will not call SM121 confirmed until our GB10 run comes back. We are the only SM121 holder on
   the thread, and that run is in the maintenance window immediately after 2026-09-14 (the lane is in an
   endurance-qualification window until then, and step 1 of the repro deliberately wedges a kernel for
   90 s). If you would rather redirect and close now, that is fine as well — we will post the results on
   the closed thread and you can reopen if anything in them disagrees.
2. #5048 merged without an SM121 datapoint. We will build the merged FlashInfer (`b51a65a2`) and run the
   prefill case plus a soak on GB10 in the same window, reported separately from the vLLM #51538 hunks so
   each fix keeps a clean verdict. Since you note that #5001 manifests on Spark because of the low SM
   count, that datapoint seems worth having on the record.

### bkryu · 2026-09-10

Thanks @SBE247Emperor for confirming. I can keep this issue open for two more weeks. 

Please feel free to close it whenever you feel ready

### SBE247Emperor · 2026-09-14

@200lz @bkryu The promised GB10 / SM121 component validation is complete. The results support the vLLM padded-row top-k diagnosis; the separate FlashInfer decode matrix passed.

**[Raw component evidence, source pins and method](https://gist.github.com/SBE247Emperor/e55d0fdc26abc10523b1d396436f1faf)**. This includes all component logs, JUnit XML, structured results, image identities and the added prefill repetition script.

The model-free tests ran on **one GB10, cc 12.1**, during Ansible-managed maintenance of our TP8 lane, with PyTorch 2.13.0+cu130 / CUDA 13.0. We used the handoff components pinned at `210c64614bc8ab954a4fa2357fc6b10f28485238`, invoked separately in isolated containers rather than running the top-level shell script verbatim. The only standalone C++ harness adjustment was adding the missing `<unistd.h>` declaration for `_exit`; kernel headers, inputs, launch logic and checks were unchanged.

| Component | Observed result |
| --- | --- |
| Standalone top-k, clean pre/post controls | Both passed |
| Poisoned padding, k=1 | Pre-#51538 hung at the 20-second watchdog; post-fix passed |
| Poisoned padding, k=2 | Pre-fix hung with padded lengths `-2, -1, 0`; post-fix passed |
| Repeated top-k launches | Pre-fix clean and post-fix poisoned controls each passed 2,000 iterations |
| Native producer/top-k regression | Reporting image: exactly 3 expected failures and 2 passes; compiled v0.28.0 control: 5 passes; no skips |
| FlashInfer decode, reporting `0.6.18.dev20260819` | All 11 handoff cases passed |
| Decode graph repetitions | C/E/J each passed 3,000 replays; valid-row max absolute error approximately 6.95e-5 |

The native failures were the uniform-decode producer clamp, compiled `next_n` producer clamp, and the persistent-top-k negative-length wedge. Each deliberate wedge was followed by a successful fresh CUDA check. Padded decode outputs were finite, not necessarily zero; the contributor's valid-row correctness criterion passed.

**Separate #5048 prefill verdict:** exact merged revision `b51a65a27f49cf0b31061cf9e42bc09e51c71696` passed all six selected upstream forced-swapAB/MG/auto-routing cases at 64/128 heads. Both head counts also passed 3,000 synchronized forced-swapAB launches at 128 tokens/top-k 2,048, checking output and LSE against the upstream reference every 100 launches. The installed fixed header and actually loaded JIT library were SHA-256 attested. The source-built test image did not retain the incompatible nightly cubin package; no version-check bypass was used.

**Seven-day serving result, separate from those component checks:** the frozen workaround-based GLM-5.3 native-FP8 window recorded **3,364/3,364 successful authenticated content probes over 168 h 8 m 9 s**, from 2026-09-07 20:15:53 UTC through 2026-09-14 20:24:02 UTC. Geometry: eight GB10s, TP8, 65,536 context, six sequence slots, MTP k=2, capture sizes 1..18. No failed probes, gaps, transport/maintenance exclusions or incidents were recorded in that window. Probes sampled every three minutes (largest interval 185 seconds), checking the eight planets in order and `finish=stop`. This is sampled serving endurance, not continuous saturation. Later planned maintenance is excluded from those frozen totals; the gist contains component receipts, not the observer dataset.

**Limits:** the 3,000-replay/launch loops took seconds, not hours. We did not run a pre-#5048 prefill differential or qualify a combined patched eight-rank serving image. The native post-fix control is a newer compiled vLLM v0.28.0 image containing #51538, not an otherwise-identical two-hunk rebuild of our fork. Our production fork still lacks #51538 and retains the complete `1..18` capture workaround; k=2 alone is not protection. No rebase completion is claimed.

The original qualified lane is restored, authenticated generation passed, and the full doctor returned 50 PASS / 0 WARN / 0 FAIL. This closes the promised bounded hardware-validation loop, not the production-rebase work. Leaving issue closure to your review and the offered observation period. Credit to @200lz for isolating the owner and to @bkryu for the separate prefill fix and triage.


### 200lz · 2026-09-15

Thanks for completing the GB10 validation and documenting the controls and limitations.

Based on your reported results, I consider the pending SM121 component-validation step complete. The pre/post-#51538 top-k differential at both k=1 and k=2 corroborates the earlier SM120 diagnosis, while the separate FlashInfer decode matrix passes. No FlashInfer-side change is indicated for this deterministic trigger.

The #5048 prefill result remains separate. Likewise, the seven-day serving result validates the complete-capture workaround; the production rebase and combined patched eight-rank qualification remain outstanding.

I have linked your external validation in vllm-project/vllm#56003 for reviewers. From my side, the bounded investigation and hardware handoff are complete; issue closure can follow the agreed observation period. Thanks again for closing the SM121 evidence gap.


### SBE247Emperor · 2026-09-19

Closing this, as offered. Thanks @200lz and @bkryu for the triage and the hold.

**Summary for anyone who lands here from a search.** The hang is not a FlashInfer defect. A padded decode slot arrives with `seq_len == 0`, the indexer context length becomes `-1`, the top-k kernel reads that as `uint32` (~4e9), and the leader CTA then spins on an inter-CTA barrier whose peers have already early-exited. It is deterministic, it reproduces at both k=1 and k=2, and it was fixed upstream on 2026-08-15 by vllm-project/vllm#51538 (`97388c44`, the producer clamp plus the kernel guard). Our SM121 component validation is in the [evidence gist](https://gist.github.com/SBE247Emperor/e55d0fdc26abc10523b1d396436f1faf): the pre/post-#51538 top-k differential corroborates the diagnosis and the separate FlashInfer decode matrix passes.

**Until a deployment carries that vLLM fix**, the workaround is complete CUDA-graph capture (`cg_sizes 1..18` in our case), so no decode batch is padded. Our frozen seven-day window on that workaround recorded 3,364/3,364 successful content probes over 168 h 8 m, eight GB10s at TP8, MTP k=2.

**Deliberately out of scope here**, and not blocking this close:

- flashinfer#5048 is a different hang (swapAB prefill), merged as `b51a65a2` with no SM121 datapoint. If we produce one, it goes on that PR, not here.
- Our production rebase onto vLLM ≥ `97388c44` and the combined patched eight-rank qualification are our own outstanding work. If either surfaces something FlashInfer-side, we will open a new issue with fresh evidence rather than reopen this one.

Closing as resolved externally: no FlashInfer-side change indicated.

