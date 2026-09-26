source: https://rocm.docs.amd.com/en/docs-7.2.4/reference/graph-safe-support.html

# Graph-safe support for ROCm libraries[#](https://rocm.docs.amd.com#graph-safe-support-for-rocm-libraries)

2026-02-19

1 min read time

HIP graph-safe libraries operate safely in HIP execution graphs.
[HIP graphs](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/how-to/hip_runtime_api/hipgraph.html#how-to-hip-graph) are an alternative way of executing tasks on a GPU
that can provide performance benefits over launching kernels using the standard
method via streams.

Functions and routines from graph-safe libraries shouldn’t result in issues like race conditions, deadlocks, or unintended dependencies.

The following table shows whether a ROCm library is graph-safe.

ROCm library |
Graph safe support |
|---|---|
❌ |
|
✅ |
|
⚠️ |
|
✅ |
|
✅ (see |
|
✅ |
|
⚠️ (experimental) |
|
✅ |
|
⚠️ (experimental) |
|
❌ |
|
❌ |
|
✅ |
|
❌ |
|
❌ |
|
✅ (see |
|
❌ |
|
✅ (see |
|
❌ |
|
❌ |
|
✅ |
|
✅ |
|
⚠️ (experimental) |
|
⚠️ (experimental) |
|
❌ |
|
❌ |
|
⚠️ |
|
✅ |

✅: full support

⚠️: partial support

❌: not supported