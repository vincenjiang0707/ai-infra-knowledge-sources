source: https://github.com/vllm-project/guidellm/issues/564

**Is your feature request related to a problem? Please describe.**

The sweep "throughput" phase isn't calibrated to the actual capabilities; it can oversaturate or undersaturate.

**Describe the solution you'd like**

More intelligently discover the maximum throughput capabilities of the system under test to set a reasonable upper limit.

**Describe alternatives you've considered**

PR [#552](https://github.com/vllm-project/guidellm/pull/552)

**Additional context**

Is your feature request related to a problem? Please describe.The sweep "throughput" phase isn't calibrated to the actual capabilities; it can oversaturate or undersaturate.

Describe the solution you'd likeMore intelligently discover the maximum throughput capabilities of the system under test to set a reasonable upper limit.

Describe alternatives you've consideredPR #552

Additional context