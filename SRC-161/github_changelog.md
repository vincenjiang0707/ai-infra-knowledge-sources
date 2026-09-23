# Changelog (aggregated from releases.body)

> releases: 2

## v0.1.1 (2025-10-21)

This is the stable release version of FlashInfer-Bench. It builds the Virtuous Cycle for AI-driven LLM Systems.

## v0.1.2 (2026-02-13)

## What's Changed
* docs: fix the blog link by @zhyncs in https://github.com/flashinfer-ai/flashinfer-bench/pull/93
* Alias flashinfer_bench as fib in README by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/94
* fix: fix linting by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/95
* fix: fix linting by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/96
* Add cutlass license by @tqchen in https://github.com/flashinfer-ai/flashinfer-bench/pull/98
* chore: remove vercel microfrontends dependency by @xslingcn in https://github.com/flashinfer-ai/flashinfer-bench/pull/99
* fix: fix ci tests by @Seven-Streams in https://github.com/flashinfer-ai/flashinfer-bench/pull/97
* ci: drop python 3.9 by @xslingcn in https://github.com/flashinfer-ai/flashinfer-bench/pull/108
* feat: restore leaderboard to main by @xslingcn in https://github.com/flashinfer-ai/flashinfer-bench/pull/107
* docs: python api reference by @xslingcn in https://github.com/flashinfer-ai/flashinfer-bench/pull/109
* docs: enhanced API docs with intro and links by @YiyanZhai in https://github.com/flashinfer-ai/flashinfer-bench/pull/110
* fix: fix the colorFor function's hash-based color assignment for web by @YiyanZhai in https://github.com/flashinfer-ai/flashinfer-bench/pull/113
* fix: smooth chart curves & longer client names in UI by @YiyanZhai in https://github.com/flashinfer-ai/flashinfer-bench/pull/114
* [tvm-ffi] TVMFFIBuilder by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/111
* refactor: Enhance TvmFfiBuilder by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/117
* refactor: rename TvmFfiBuilder -> TVMFFIBuilder by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/118
* refactor: update sampling evaluation logic by @zanderjiang in https://github.com/flashinfer-ai/flashinfer-bench/pull/104
* refactor: Builder System by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/120
* ci: Use uv with cache in unit tests by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/122
* test: update tests for builder by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/123
* docs: Enhance docs with md and add docs for compile by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/124
* update kernel generator by @zanderjiang in https://github.com/flashinfer-ai/flashinfer-bench/pull/101
* feat: Destination-passing Style by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/125
* refactor: rename traceset -> trace_set and avoid singie character variables by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/129
* Add profile_baseline option to BenchmarkConfig by @zhang677 in https://github.com/flashinfer-ai/flashinfer-bench/pull/130
* feat: Per-kernel Apply Config by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/131
* refactor: Add FlashInfer Trace (definitions and workloads) to flashinfer-bench by @YiyanZhai in https://github.com/flashinfer-ai/flashinfer-bench/pull/138
* Fix React Server Components CVE vulnerabilities by @vercel[bot] in https://github.com/flashinfer-ai/flashinfer-bench/pull/128
* Agent FFI integration by @zanderjiang in https://github.com/flashinfer-ai/flashinfer-bench/pull/119
* Docs: Add docstring for modules by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/132
* Add Claude Code GitHub Workflow by @yzh119 in https://github.com/flashinfer-ai/flashinfer-bench/pull/137
* refactor: Provide TracingConfigRegistry and Refactor TracingRuntime by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/133
* Add Claude skills files for new model support by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/136
* Add kernel: deepseek sparse attention by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/146
* refactor: Enhance ApplyRuntime by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/135
* [refactor] apply() Overhead Reduction by @YiyanZhai in https://github.com/flashinfer-ai/flashinfer-bench/pull/121
* feat: adapter for torch.nn.functional.linear by @YiyanZhai in https://github.com/flashinfer-ai/flashinfer-bench/pull/154
* Add kernel: trtllm fp8 block scale moe by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/152
* Support NCU tool by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/139
* feat: cache solution hash by @xslingcn in https://github.com/flashinfer-ai/flashinfer-bench/pull/153
* Add def: add attention variant with page size 64 by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/145
* Add kernel: deepseek sparse attn page size 64 by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/147
* fix: adapter can take page_size 64  by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/157
* Add kernel: gated delta net by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/156
* claude: update skills by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/158
* claude: update skills on cloning repos by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/159
* claude: fix clone repos skill by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/161
* Support Agent Tools by @zanderjiang in https://github.com/flashinfer-ai/flashinfer-bench/pull/140
* update dsa and gdn definitions, op schema and unittests by @yzh119 in https://github.com/flashinfer-ai/flashinfer-bench/pull/164
* fix: gdn test update && decode test on h100 by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/165
* docs: Enhance agent and API docs by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/162
* docs: Add github link to main page by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/167
* docs: merge configurations for mintlify by @xslingcn in https://github.com/flashinfer-ai/flashinfer-bench/pull/171
* Fix README logo and support dark and light mode by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/172
* Update Definition: Deepseek Sparse Attn page size 64 by @zanderjiang in https://github.com/flashinfer-ai/flashinfer-bench/pull/173
* Update README Links by @zanderjiang in https://github.com/flashinfer-ai/flashinfer-bench/pull/176
* fix: Error in Sphinx Docs Build by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/181
* fix: Benchmarking on latest flashinfer-trace by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/179
* Add --required-matched-ratio CLI parameter for configurable correctness thresholds by @xiefan46 in https://github.com/flashinfer-ai/flashinfer-bench/pull/178
* gdn: update number of heads on tp=4 & tp=2 by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/186
* feat: TileLang Support by @zanderjiang in https://github.com/flashinfer-ai/flashinfer-bench/pull/134
* Update solution folder structure by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/185
* web: Update viewer by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/189
* claude: update skills on hugging face reference by @yyihuang in https://github.com/flashinfer-ai/flashinfer-bench/pull/174
* feat: web UI rankings tab by @YiyanZhai in https://github.com/flashinfer-ai/flashinfer-bench/pull/191
* fix: Versioning and release by @Ubospica in https://github.com/flashinfer-ai/flashinfer-bench/pull/192

## New Contributors
* @zhyncs made their first contribution in https://github.com/flashinfer-ai/flashinfer-bench/pull/93
* @tqchen made their first contribution in https://github.com/flashinfer-ai/flashinfer-bench/pull/98
* @Seven-Streams made their first contribution in https://github.com/flashinfer-ai/flashinfer-bench/pull/97
* @zhang677 made their first contribution in https://github.com/flashinfer-ai/flashinfer-bench/pull/130
* @vercel[bot] made their first contribution in https://github.com/flashinfer-ai/flashinfer-bench/pull/128
* @yzh119 made their first contribution in https://github.com/flashinfer-ai/flashinfer-bench/pull/137
* @yyihuang made their first contribution in https://github.com/flashinfer-ai/flashinfer-bench/pull/136
* @xiefan46 made their first contribution in https://github.com/flashinfer-ai/flashinfer-bench/pull/178

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer-bench/compare/v0.1.1...v0.1.2
