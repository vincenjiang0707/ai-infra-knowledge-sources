# [Issue #1482] Int8 pipeline parallelism

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/1482
state: closed | updated: 2026-02-21T20:27:26Z
labels: Medium Priority, High Risk

## 正文

I am trying to work with cuda streams for pipeline parallelism, i.e. executing different parts of a model at the same time on different gpus.
And with int4, float16, bfloat16 everything seems to work as expected.

However, with int8 there appears to be something blocking, and gpus execute sequentially.
As int4 works, I am wondering if anyone knows if there is some blocking operation in int8.

Thanks!

## 评论 (3)

### TimDettmers · 2025-02-28

For int4 you are also using bitsandbytes code or is this only for int8? There are some operations on bitsandbytes that forces the cuda device before c-calls because this sometimes introduced bugs. It might be that this is causing your problems.

This behavior was changed in 0.45. Can you check your bitsandbytes version and see if you still have this problem with the newer version?

### matthewdouglas · 2025-02-28

One further thing to note is that int8 has a host-device synchronization that is forced when decomposing the problem into separate int8 and fp16 matmuls. Using `threshold=0.0` should avoid that, and will be faster in general, at the potential cost of accuracy.

### TimDettmers · 2026-02-21

Closing this issue. The host-device synchronization in int8 mixed-precision decomposition (when `threshold > 0`) is the likely cause of the sequential execution you observed. As noted above, setting `threshold=0.0` avoids this sync point and should allow proper pipeline parallelism with CUDA streams. The device-forcing behavior was also changed in v0.45.

If you're still hitting this on the latest version, please reopen with updated details.
