# [Issue #3033] [QST] [CuTeDSL] Alignment dropped by partition_S.

source: https://github.com/NVIDIA/cutlass/issues/3033
state: open | updated: 2026-09-24T14:38:01Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

**What is your question?**

Here is the [code](https://gist.github.com/brian030128/9a910962eecef5825df14d62629e133e) of my vectorized transposed kernel, it fails to compile with the error:

```
cutlass.base_dsl.common.DSLRuntimeError: DSLRuntimeError: 🧊🧊🧊 ICE IR Verification Failed 🧊🧊🧊
  Caused exception: Verification failed:
error: "cute.copy("("/home/brain_l/flashtree/base/cutedsl_kernel/src/transpose.py":41:4): 'cute.copy' op '!cute_nvgpu.atom.universal_copy<f32, 128 b>' ptr alignment does not meet requirement
 note: "cute.copy("("/home/brain_l/flashtree/base/cutedsl_kernel/src/transpose.py":41:4): see current operation: "cute.copy"(%arg3, %149, %161) : (!cute.tiled_copy<!cute_nvgpu.atom.universal_copy<f32, 128 b>, layout_copy_tv = <"((8,32),4):((128,1),32)">, tiler_mn = <"[32:1;32:1]">>, !cute.memref<f32, gmem, "((4,1),(1,1)):((1,0),(0,0))">, !cute.memref<f32, smem, align<16>, "((4,1),(1,1)):((1,0),(0,0))">) -> ()
```

I tried to print the iterator with `cute.printf(g2s_thr_src.iterator)`, it shows align to 4 bytes. But the raw ptr value is aligned to 16 bytes. My guess is the alignment is not propogated correctly and is dropped by partition_S, how should I do this correctly?
```
raw_ptr(0x00007fbeac604c00: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604c10: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604c20: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604c30: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604c40: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604c50: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604c60: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604c70: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604d00: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604d10: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604d20: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604d30: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604d40: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604d50: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604d60: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604d70: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604e00: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604e10: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604e20: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604e30: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604e40: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604e50: f32, gmem, align<4>)
raw_ptr(0x00007fbeac604e60: f32, gmem, align<4>)
```

## 评论 (4)

### github-actions[bot] · 2026-03-16

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-06-14

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### 0z5a · 2026-09-24

Hi,  I can investigate this.

I'd like to narrow down whether `partition_S` is actually dropping statically provable alignment information, versus the source tensor not carrying enough alignment information for the partitioned iterator to preserve it safely.

I'll check:

* alignment metadata before and after `partition_S`;
* layouts/offsets where 16-byte alignment is statically guaranteed versus cases where it is not;
* whether the lost information prevents legal 128-bit vectorized copies;
* generated IR/PTX for the vectorized and fallback paths;
* regression cases ensuring we do not propagate stronger alignment when the partition offset can break it.

If this turns out to be an alignment-propagation issue in CuTe DSL, I'll send a focused fix plus positive and negative regression tests.


### 0z5a · 2026-09-24

Draft #3668 documents row-stride alignment proofs and a checked 32-bit fallback for offset views. All 13 regression cases pass on RTX 5090 with CuTeDSL 4.8; memcheck is clean, and PTX/SASS confirms the 128-bit and scalar paths.

