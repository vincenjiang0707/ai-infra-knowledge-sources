source: https://github.com/vllm-project/guidellm/issues/529

**Is your feature request related to a problem? Please describe.**

Benchmarks that include incomplete requests (any benchmark using constraints other than max-requests) will have decreased successful request throughput metrics proportional to the percent of total requests that are incomplete and the length of time those requests ran for.

**Describe the solution you'd like**

Final console output should use `total`

requests for throughput metrics.

**Describe alternatives you've considered**

Another possible way of solving this is to discard throughput for sections that fall outside of the interquartile range and calculate the mean from the remaining samples. However, this can mask legitimate dips in throughput.

**Additional context**

This is related to the issue reported in [#514](https://github.com/vllm-project/guidellm/issues/514).

Is your feature request related to a problem? Please describe.Benchmarks that include incomplete requests (any benchmark using constraints other than max-requests) will have decreased successful request throughput metrics proportional to the percent of total requests that are incomplete and the length of time those requests ran for.

Describe the solution you'd likeFinal console output should use

`total`

requests for throughput metrics.Describe alternatives you've consideredAnother possible way of solving this is to discard throughput for sections that fall outside of the interquartile range and calculate the mean from the remaining samples. However, this can mask legitimate dips in throughput.

Additional contextThis is related to the issue reported in #514.