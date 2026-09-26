source: https://github.com/vllm-project/guidellm/pull/710

# feat: Add embeddings endpoint support (MVP) - #710

[sjmonson](https://github.com/sjmonson)merged 7 commits into

## Conversation

[maryamtahhan](https://github.com/maryamtahhan)

[force-pushed](https://github.com/vllm-project/guidellm/compare/10339cb4a99a1a041355b425db80434490a928df..52d15577394ff9ce7315372caa91537c3b9811ff)the embeddings-mvp-from-scratch branch 3 times, most recently from

[to](https://github.com/vllm-project/guidellm/commit/10339cb4a99a1a041355b425db80434490a928df)

`10339cb`


`52d1557`

[Compare](https://github.com/vllm-project/guidellm/compare/10339cb4a99a1a041355b425db80434490a928df..52d15577394ff9ce7315372caa91537c3b9811ff)

April 29, 2026 11:26


[dbutenhof](https://github.com/dbutenhof)added

[community contribution](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3A%22community%20contribution%22)

[feature](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Afeature)

Apr 29, 2026


**requested changes**

[sjmonson](https://github.com/sjmonson)Apr 29, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Overall a much better design. See nits below.

[src/guidellm/data/schemas.py](https://github.com/vllm-project/guidellm/pull/710/files#diff-70cdc853c05c11fbc8c7a03ff185af9a094fc68fdc0924853f75153972dc1370)Outdated

[src/guidellm/data/schemas.py](https://github.com/vllm-project/guidellm/pull/710/files#diff-70cdc853c05c11fbc8c7a03ff185af9a094fc68fdc0924853f75153972dc1370)Outdated

[src/guidellm/data/schemas.py](https://github.com/vllm-project/guidellm/pull/710/files#diff-70cdc853c05c11fbc8c7a03ff185af9a094fc68fdc0924853f75153972dc1370)Outdated

[src/guidellm/utils/random.py](https://github.com/vllm-project/guidellm/pull/710/files#diff-ee5c5fcbdd1d3951c1616c31f2e582e11bfc08548c662b604f9f12758262433c)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/710/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/benchmark/outputs/console.py](https://github.com/vllm-project/guidellm/pull/710/files#diff-f321b63a8b5258670d851eda893190e71d8f7366f4371ce7be43c1a2ccef1bf0)Outdated

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/710/files#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

[docs/guides/embeddings.md](https://github.com/vllm-project/guidellm/pull/710/files#diff-6c7a5d04118bad44a4b01f7de9f63343b8ec1726d53b625eacd13e335234486f)Outdated

[docs/guides/embeddings.md](https://github.com/vllm-project/guidellm/pull/710/files#diff-6c7a5d04118bad44a4b01f7de9f63343b8ec1726d53b625eacd13e335234486f)Outdated

[docs/guides/embeddings.md](https://github.com/vllm-project/guidellm/pull/710/files#diff-6c7a5d04118bad44a4b01f7de9f63343b8ec1726d53b625eacd13e335234486f)Outdated

[maryamtahhan](https://github.com/maryamtahhan)added a commit to maryamtahhan/guidellm that referenced this pull request

Apr 30, 2026

Fix root causes instead of working around them: - Make output_tokens optional (int | None) in SyntheticTextDatasetConfig - Fix RunningMetricStats to skip None values (TTFT/ITL/TPOT now None for non-streaming) - Revert console.py workarounds (streaming metrics show -- automatically when None) - Revert PreprocessDatasetConfig changes (unrelated) - Revert random.py changes (not needed with optional output_tokens) Code cleanup: - Remove encoding_format/dimensions kwargs from handler (can't be set via backend) - Remove embeddings from LEGACY_API_ALIASES (moving away from legacy format) Documentation fixes: - Fix --request-format embeddings → /v1/embeddings - Fix --backend-extra → --backend-kwargs with correct syntax - Fix rate syntax: --rate 1 5 10 20 → --rate 1,5,10,20 Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

Adds minimal embeddings support following the pooling pattern (~113 line handler). Core Implementation: - EmbeddingsRequestHandler for /v1/embeddings endpoint - Formats requests with single text or list of texts - Returns GenerationResponse (reuses existing infrastructure) - Registered /v1/embeddings in DEFAULT_API_PATHS - Added embeddings alias to LEGACY_API_ALIASES Synthetic Data Support: - Allow output_tokens=0 in SyntheticTextDatasetConfig - Fix config parser to accept single key=value pairs (e.g., "prompt_tokens=64") - Fix IntegerRangeSampler to support 0 tokens and prevent invalid ranges Embeddings-Aware Console Output: - Auto-detect embeddings mode (zero output tokens) - Hide text metrics table (words/characters) for embeddings - Hide streaming metrics (TTFT/ITL/TPOT) for embeddings - Focus output on relevant metrics: latency, tokens/sec, throughput Tests & Documentation: - 13 comprehensive unit tests for EmbeddingsRequestHandler - Complete embeddings benchmarking guide in docs/guides/embeddings.md - Examples for all benchmark profiles and configuration options Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

Fix root causes instead of working around them: - Make output_tokens optional (int | None) in SyntheticTextDatasetConfig - Fix RunningMetricStats to skip None values (TTFT/ITL/TPOT now None for non-streaming) - Revert console.py workarounds (streaming metrics show -- automatically when None) - Revert PreprocessDatasetConfig changes (unrelated) - Revert random.py changes (not needed with optional output_tokens) Code cleanup: - Remove encoding_format/dimensions kwargs from handler (can't be set via backend) - Remove embeddings from LEGACY_API_ALIASES (moving away from legacy format) Documentation fixes: - Fix --request-format embeddings → /v1/embeddings - Fix --backend-extra → --backend-kwargs with correct syntax - Fix rate syntax: --rate 1 5 10 20 → --rate 1,5,10,20 Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

These kwargs were removed from the handler as they can't be set via the current backend kwargs mechanism (per PR[vllm-project#710]review). Tests now: 11 passing (was 13, removed 2) Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

[maryamtahhan](https://github.com/maryamtahhan)

[force-pushed](https://github.com/vllm-project/guidellm/compare/a112c576b14703cf0cc74538fb4613cc6ea099ca..19356b36b1038c30f85608c9c37360baa958481a)the embeddings-mvp-from-scratch branch from

[to](https://github.com/vllm-project/guidellm/commit/a112c576b14703cf0cc74538fb4613cc6ea099ca)

`a112c57`


`19356b3`

[Compare](https://github.com/vllm-project/guidellm/compare/a112c576b14703cf0cc74538fb4613cc6ea099ca..19356b36b1038c30f85608c9c37360baa958481a)

April 30, 2026 12:12


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Apr 30, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good to me. Sam will also re-review this.

[src/guidellm/backends/openai/request_handlers.py](https://github.com/vllm-project/guidellm/pull/710/files/19356b36b1038c30f85608c9c37360baa958481a#diff-60cfc62dcd68426ebab8f6d637eba19d6423ac6fe297be59efdfb943b9f0d79f)Outdated

Embeddings don't generate output, so output_metrics should have all None values (not text_tokens=0). By omitting the output_metrics parameter, it defaults to UsageMetrics() with all None values, which is more semantically accurate: - None means 'not applicable' - 0 means 'zero tokens generated' Addresses PR[vllm-project#710]review comment from[@jaredoconnell]. Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 1, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I think this looks OK, although I made a comment on some documentation that could be "tweaked" for clarity.

[docs/guides/embeddings.md](https://github.com/vllm-project/guidellm/pull/710/files/19356b36b1038c30f85608c9c37360baa958481a#diff-6c7a5d04118bad44a4b01f7de9f63343b8ec1726d53b625eacd13e335234486f)Outdated

Align with official benchmark documentation to clarify rate parameter: - Sweep: Total number of strategies including synchronous and throughput - Constant: Requests per second, accepts list for successive streams - Throughput: Number of concurrent request streams (default: 10) - Poisson: Maximum async requests, accepts list for successive streams - Concurrent: Number of concurrent requests, accepts list - Synchronous: No rate parameter Update examples: - Basic example: Use default sweep (5 strategies) - Sweep example: Show --rate 10 for 10 total strategies - Constant example: Show list of rates for successive streams - Throughput example: Use default concurrent streams Addresses PR[vllm-project#710]review comment from[@dbutenhof]. Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

The health monitor logged errors for any worker process death, including processes that completed successfully (exit code 0). This caused misleading error messages during benchmarks, especially for embeddings where workers complete quickly. This change makes the health monitor consistent with shutdown logic by only logging errors for non-zero exit codes (actual failures). Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>

[maryamtahhan](https://github.com/maryamtahhan)

[force-pushed](https://github.com/vllm-project/guidellm/compare/6950e4abdb84b135d2ed85753fcec922e8372db5..7adbb0936315476f186921e0de8464d58ffda46d)the embeddings-mvp-from-scratch branch from

[to](https://github.com/vllm-project/guidellm/commit/6950e4abdb84b135d2ed85753fcec922e8372db5)

`6950e4a`


`7adbb09`

[Compare](https://github.com/vllm-project/guidellm/compare/6950e4abdb84b135d2ed85753fcec922e8372db5..7adbb0936315476f186921e0de8464d58ffda46d)

May 1, 2026 15:12


**requested changes**

[sjmonson](https://github.com/sjmonson)May 1, 2026

[docs/guides/embeddings.md](https://github.com/vllm-project/guidellm/pull/710/files/087c6c35a0b7023028451c66cc96e4f7384c01a0#diff-6c7a5d04118bad44a4b01f7de9f63343b8ec1726d53b625eacd13e335234486f)Outdated

[docs/guides/embeddings.md](https://github.com/vllm-project/guidellm/pull/710/files/087c6c35a0b7023028451c66cc96e4f7384c01a0#diff-6c7a5d04118bad44a4b01f7de9f63343b8ec1726d53b625eacd13e335234486f)Outdated

|
One option to consider is getting less detailed with the use of profiles in GuideLLM. Because it's redundant, and the CLI format will change soon. |

Yeah I had considered this to. I think overall the format of the guide needs a little bit of work and more linking to other relevant sections in the docs, but I didn't want to block the whole feature on it. |

Reduce to single example with essential information only. Remove references to default values and configuration options. Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com> Signed-off-by: Maryam Tahhan <mtahhan@redhat.com>


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 4, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I think a few sections of the expanded documentation were nice (like the sample JSONL dataset, which appears in some other specialized modes) -- but I also don't think any of the documentation you dropped was critical, so let's move ahead.


**approved these changes**

[sjmonson](https://github.com/sjmonson)May 4, 2026

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Adds minimal embeddings support following the pooling pattern (~113 line handler).

Core Implementation:

Synthetic Data Support:

Embeddings-Aware Console Output:

Tests & Documentation:

## Summary

## Details

## Test Plan

## Related Issues

## Use of AI

`## WRITTEN BY AI ##`

)