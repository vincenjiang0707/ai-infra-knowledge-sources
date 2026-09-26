source: https://github.com/vllm-project/guidellm/pull/552

# cpu - sweep saturation detection - #552

Open

[maryamtahhan](https://github.com/maryamtahhan)wants to merge 6 commits into

Open

[maryamtahhan](https://github.com/maryamtahhan) wants to merge 6 commits into

[maryamtahhan](https://github.com/maryamtahhan)wants to merge 6 commits into

## Conversation

[maryamtahhan](https://github.com/maryamtahhan)

[force-pushed](https://github.com/vllm-project/guidellm/compare/94577825ed742a7c1ef36b1b4130937caa6d3162..e8ccf7704b15371b5fbd74cd4fda1604ca51c750)the cpu-sweep-saturation branch from

[to](https://github.com/vllm-project/guidellm/commit/94577825ed742a7c1ef36b1b4130937caa6d3162)

`9457782`


`e8ccf77`

[Compare](https://github.com/vllm-project/guidellm/compare/94577825ed742a7c1ef36b1b4130937caa6d3162..e8ccf7704b15371b5fbd74cd4fda1604ca51c750)

January 23, 2026 10:08

Contributor
Author

Contributor
Author

Contributor
Author

Contributor

|
You can do this by running: |

Contributor

|
This pull request has merge conflicts that must be resolved before it can be |

CPU deployments saturate at much lower concurrency rates than GPU deployments (e.g., 8 vs 512), causing sweep tests to continue measuring beyond saturation. This creates misleading performance graphs with "knee bend" artifacts and wasted benchmark time. This commit adds three configurable parameters to handle saturation: 1. exclude_throughput_target (default: false) - Stops constant-rate tests before reaching throughput level - Prevents generating tests at rates the system cannot sustain - Eliminates "elbow" artifacts in graphs 2. exclude_throughput_result (default: false) - Excludes throughput benchmark from saved results - Removes anomalous burst-capacity data points that create visual artifacts (TTFT spikes from ~70ms to 244ms, inter-token latency anomalies) in performance graphs 3. saturation_threshold (default: 0.98) - Automatically stops sweep when achieved rate < target × threshold - Detects saturation (e.g., system achieves 2.63 req/s when targeting 2.68 req/s = 98% efficiency) - Saves time by skipping unnecessary over-saturated tests Parameters are configurable via CLI flags (--exclude-throughput-target) or environment variables (GUIDELLM__EXCLUDE_THROUGHPUT_TARGET). Defaults remain GPU-friendly (all disabled). CPU deployments should enable both exclusion flags and tune saturation threshold as needed. Signed-off-by: Maryam Tahhan <mtahhan@redhat.com> Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>

Add important note explaining why max_concurrency should not be set when running sweep profile tests. When max_concurrency is artificially limited, the throughput test underestimates server capacity, causing constant-rate tests to run at rates far below actual capacity. This prevents proper saturation detection and can produce misleading results where TTFT decreases instead of increases. Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

Expand the "How It Works" section to provide: - Clear explanation of test execution order - Detailed rationale for each parameter (why + effect) - Explanation of how all three parameters work together - Real-world example of throughput test outliers (23+ sec TTFT) This helps users understand why all three parameters are recommended for CPU deployments and how they complement each other to produce clean, efficient benchmarks. Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

[maryamtahhan](https://github.com/maryamtahhan)

[force-pushed](https://github.com/vllm-project/guidellm/compare/eab3e3869746b31cfbbb2f14532a3dedb6a9b15d..49900f8fe4573e564b9511112f8849d1a6dbc9c3)the cpu-sweep-saturation branch from

[to](https://github.com/vllm-project/guidellm/commit/eab3e3869746b31cfbbb2f14532a3dedb6a9b15d)

`eab3e38`


`49900f8`

[Compare](https://github.com/vllm-project/guidellm/compare/eab3e3869746b31cfbbb2f14532a3dedb6a9b15d..49900f8fe4573e564b9511112f8849d1a6dbc9c3)

April 21, 2026 10:06

### This branch has not been deployed

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)Add this suggestion to a batch that can be applied as a single commit.This suggestion is invalid because no changes were made to the code.Suggestions cannot be applied while the pull request is closed.Suggestions cannot be applied while viewing a subset of changes.Only one suggestion per line can be applied in a batch.Add this suggestion to a batch that can be applied as a single commit.Applying suggestions on deleted lines is not supported.You must change the existing code in this line in order to create a valid suggestion.Outdated suggestions cannot be applied.This suggestion has been applied or marked resolved.Suggestions cannot be applied from pending reviews.Suggestions cannot be applied on multi-line comments.Suggestions cannot be applied while the pull request is queued to merge.Suggestion cannot be applied right now. Please check back later.

## Summary

This PR adds configurable saturation detection and optimisation parameters for testing CPU-based deployments/SUTs (vllm-cpu) with the sweep profile. CPU deployments saturate at much lower concurrency rates than GPU deployments (e.g., 16 concurrent requests vs 512), causing sweep tests to continue measuring beyond saturation and producing misleading "knee bend" artifacts in performance graphs. The new parameters allow users to detect saturation early, stop tests efficiently, and exclude anomalous throughput measurements from results.

## Details

## Test Plan

Verified with vLLM-CPU deployment


Test saturation detection works correctly:** Test that defaults work for GPU deployments**

** Verify environment variable configuration **

** Run unit tests**

Run pre-commit checks## Related Issues

N/A

## Use of AI

`## WRITTEN BY AI ##`

)