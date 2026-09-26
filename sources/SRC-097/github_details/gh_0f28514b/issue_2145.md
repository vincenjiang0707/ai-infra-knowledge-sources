# [Issue #2145] Support for Google Cloud Storage (GCS)

source: https://github.com/ai-dynamo/nixl/issues/2145
state: open | updated: 2026-09-01T03:26:32Z
labels: 

## 正文

Hi NIXL maintainers,

I'm trying to understand the current status of Google Cloud Storage (GCS) support with NIXL and would appreciate any guidance from the community.

Is there currently any native GCS integration/adaptation available or under development?
Has the existing OBJ plugin been tested or benchmarked with GCS using its S3-compatible API?
Are there any known limitations with using GCS through the existing S3-compatible interface?
Based on your experience, would there be any meaningful benefits to having a native GCS integration?

Any pointers to existing work, benchmarks, discussions, or recommendations would be very helpful.

Thanks!

## 评论 (3)

### lluki · 2026-08-31

Hi @guhan-eswaran 

I have benchmarked recently the object store plugin as SGLang K/V cache offloading backend. I found that it performs well, it usually saturates line rate or is at least comparable in performance with `s5cmd`. There are a few tunables that can help to achieve best performance, in particular setting `throughput_target_gbps` and `crtMinLimit` . But specifics depend on your network and transfer size etc.

We did not run it yet against GCS, so I cant comment on this yet. But I will run some benchmarks and consider implementing a GCS  specific backend.

### vvenkates27 · 2026-09-01

Hi @guhan-eswaran 
Thank you for the question. NIXL does not currently provide a native GCS plugin, although native GCS support is on our roadmap. In the meantime, we recommend evaluating GCS through its S3-compatible interface using the existing NIXL object storage plugin. While we have not yet formally validated or benchmarked this configuration with GCS, testing on other object storage backends has demonstrated near line-rate performance, and we are not currently aware of any limitations with this approach.

Our near-term focus is to evaluate GCS through the existing object storage plugin and compare it with native GCS APIs where appropriate. NIXLBench and AIPerf are suitable frameworks for measuring throughput, latency across different object sizes, and concurrent transfer performance. We welcome any benchmark results or implementation experience that can help inform future GCS support and optimization.
 

### guhan-eswaran · 2026-09-01

Thanks for confirming. I would like to contribute and already started with the compatibility checks and preliminary works.
