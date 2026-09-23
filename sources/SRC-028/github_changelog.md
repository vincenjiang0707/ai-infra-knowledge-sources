# Changelog (aggregated from releases.body)

> releases: 4

## v0.2.0 (2024-04-05)

# Major Changes

- Support JetStream [MaxText](https://github.com/google/maxtext) inference on Cloud TPU VM
- Support [JetStream Pytorch](https://github.com/google/jetstream-pytorch) inference on Cloud TPU VM
- Support Continuous Batching with interleaved mode in JetStream
- Support online serving benchmarking

## What's Changed
* Add unit tests CI github action by @JoeZijunZhou in https://github.com/google/JetStream/pull/1
* Refine thread in orchestrator by @JoeZijunZhou in https://github.com/google/JetStream/pull/2
* Optimize maximum threads to saturate decoding capacity by @JoeZijunZhou in https://github.com/google/JetStream/pull/3
* Add benchmarks maximum threads config by @JoeZijunZhou in https://github.com/google/JetStream/pull/4
* First support necessary for MaxText by @rwitten in https://github.com/google/JetStream/pull/5
* Support gracefully stopping orchestrator and server by @JoeZijunZhou in https://github.com/google/JetStream/pull/6
* Save request outputs and add eval accuracy support by @FanhaiLu1 in https://github.com/google/JetStream/pull/8
* Use parameter based num as inference request max output length  by @FanhaiLu1 in https://github.com/google/JetStream/pull/10
* Fix output token drop issue by @JoeZijunZhou in https://github.com/google/JetStream/pull/9
* Add option to warm up by @qihqi in https://github.com/google/JetStream/pull/11
* Replace token_list with generated_text in saved outputs by @FanhaiLu1 in https://github.com/google/JetStream/pull/12
* Refine requester util by @JoeZijunZhou in https://github.com/google/JetStream/pull/15
* Adds filtering for sharegpt based on conversation starter. by @patemotter in https://github.com/google/JetStream/pull/17
* Allows more requests than available data. by @patemotter in https://github.com/google/JetStream/pull/19
* Fix starvation with async server and interleaving optimization by @JoeZijunZhou in https://github.com/google/JetStream/pull/13
* Add Token util unit test by @FanhaiLu1 in https://github.com/google/JetStream/pull/20
* Fix llama2 decode bug in tokenizer by @FanhaiLu1 in https://github.com/google/JetStream/pull/22
* Fix whitespace replacement bug by @FanhaiLu1 in https://github.com/google/JetStream/pull/24
* Update benchmark to run openorca dataset by @morgandu in https://github.com/google/JetStream/pull/21
* Add model ckpt conversion and AQT scripts for JetStream MaxText Serving by @JoeZijunZhou in https://github.com/google/JetStream/pull/23
* Refactor to sample before tokenize by @morgandu in https://github.com/google/JetStream/pull/26
* Update ckpt conversion scripts by @JoeZijunZhou in https://github.com/google/JetStream/pull/25
* move tokenizer model to third party llama2 by @FanhaiLu1 in https://github.com/google/JetStream/pull/27
* Support JetStream MaxText user guide by @JoeZijunZhou in https://github.com/google/JetStream/pull/28
* Enable pylint linter and pyink formatter by @JoeZijunZhou in https://github.com/google/JetStream/pull/29
* Update README by @JoeZijunZhou in https://github.com/google/JetStream/pull/30
* Release v0.2.0 by @JoeZijunZhou in https://github.com/google/JetStream/pull/31

## New Contributors
* @JoeZijunZhou made their first contribution in https://github.com/google/JetStream/pull/1
* @rwitten made their first contribution in https://github.com/google/JetStream/pull/5
* @FanhaiLu1 made their first contribution in https://github.com/google/JetStream/pull/8
* @qihqi made their first contribution in https://github.com/google/JetStream/pull/11
* @patemotter made their first contribution in https://github.com/google/JetStream/pull/17
* @morgandu made their first contribution in https://github.com/google/JetStream/pull/21

**Full Changelog**: https://github.com/google/JetStream/commits/v0.2.0

## v0.2.1 (2024-05-03)

## Key Changes

- Support Llama3 tokenizer
- JetStream Tokenizer refactor
- Disaggregation preparation work

## What's Changed
* add sample_idx in InputRequest for debugging by @morgandu in https://github.com/google/JetStream/pull/32
* Update README.md with user guides by @JoeZijunZhou in https://github.com/google/JetStream/pull/34
* Update README.md with PT user guide by @JoeZijunZhou in https://github.com/google/JetStream/pull/35
* Reorganize unit tests and update CICD by @JoeZijunZhou in https://github.com/google/JetStream/pull/37
* Add badges for JetStream by @JoeZijunZhou in https://github.com/google/JetStream/pull/38
* Bump idna from 3.6 to 3.7 by @dependabot in https://github.com/google/JetStream/pull/39
* Reformat benchmark metrics by @yeandy in https://github.com/google/JetStream/pull/42
* Update server host default value by @JoeZijunZhou in https://github.com/google/JetStream/pull/43
* Refactor readme by @FanhaiLu1 in https://github.com/google/JetStream/pull/41
* Add missing Documentation by @FanhaiLu1 in https://github.com/google/JetStream/pull/47
* Update README.md to fix broken link by @charbull in https://github.com/google/JetStream/pull/50
* Add np padded token support by @FanhaiLu1 in https://github.com/google/JetStream/pull/49
* Format token utils and test by @FanhaiLu1 in https://github.com/google/JetStream/pull/51
* Align Tokenizer in JetStream by @JoeZijunZhou in https://github.com/google/JetStream/pull/40
* Do nothing for nd array in copy_to_host_async by @FanhaiLu1 in https://github.com/google/JetStream/pull/52
* Add jax_padding support driver and server lib by @FanhaiLu1 in https://github.com/google/JetStream/pull/54
* Update maxtext user guide by @JoeZijunZhou in https://github.com/google/JetStream/pull/56
* Fix benchmark script type issue by @JoeZijunZhou in https://github.com/google/JetStream/pull/59
* Fix requester flag default value by @JoeZijunZhou in https://github.com/google/JetStream/pull/60
* Fix float division by zero in benchmark by @FanhaiLu1 in https://github.com/google/JetStream/pull/62
* Register IFRT proxy backend when proxy is defined in the jax_platforms by @zhihaoshan-google in https://github.com/google/JetStream/pull/63
* Add an abstract class for Tokenizer by @bhavya01 in https://github.com/google/JetStream/pull/53
* refactor slice_to_num_chips to adapt to Cloud config by @zhihaoshan-google in https://github.com/google/JetStream/pull/65
* Support llama3 tokenizer by @bhavya01 in https://github.com/google/JetStream/pull/67
* Prerequisite work for supporting disaggregation: by @zhihaoshan-google in https://github.com/google/JetStream/pull/68
* Create __init__.py in Jetstream/third_party by @bhavya01 in https://github.com/google/JetStream/pull/69
* Add tokenize_and_pad function to backward compatible  by @FanhaiLu1 in https://github.com/google/JetStream/pull/70
* Release v0.2.1 by @JoeZijunZhou in https://github.com/google/JetStream/pull/72
* Bump tqdm from 4.66.1 to 4.66.3 in the pip group across 1 directory by @dependabot in https://github.com/google/JetStream/pull/73
* Release v0.2.1 with docs update by @JoeZijunZhou in https://github.com/google/JetStream/pull/74

## New Contributors
* @dependabot made their first contribution in https://github.com/google/JetStream/pull/39
* @yeandy made their first contribution in https://github.com/google/JetStream/pull/42
* @charbull made their first contribution in https://github.com/google/JetStream/pull/50
* @zhihaoshan-google made their first contribution in https://github.com/google/JetStream/pull/63
* @bhavya01 made their first contribution in https://github.com/google/JetStream/pull/53

**Full Changelog**: https://github.com/google/JetStream/compare/v0.2.0...v0.2.1

## v0.2.2 (2024-05-31)

## Key Changes

- Enable observability in JetStream Server (prometheus metrics)
- Enable JAX profiler support on single-host JetStream Server
- Support both text and token ids I/O for JetStream Decode API
- Add health check API
- Support MLPerf evaluation
- Enable JetStream Server E2E tests
- Increase unit test coverage (>=96%)

## What's Changed
* Accuracy eval mlperf by @jwyang-google in https://github.com/google/JetStream/pull/76
* Add metadata metrics by @yeandy in https://github.com/google/JetStream/pull/77
* Fix pad_tokens function description by @FanhaiLu1 in https://github.com/google/JetStream/pull/80
* Prometheus Metrics by @Bslabe123 in https://github.com/google/JetStream/pull/71
* Update JetStream grpc proto to support I/O with text and token ids by @JoeZijunZhou in https://github.com/google/JetStream/pull/78
* Update benchmark script to easily test llama-3 by @bhavya01 in https://github.com/google/JetStream/pull/83
* Unit test coverage cleanup by @JoeZijunZhou in https://github.com/google/JetStream/pull/81
* Allow tokenizer to customize stop_tokens by @qihqi in https://github.com/google/JetStream/pull/84
* Decode Batch Percentage Metrics/Improved Scraping by @Bslabe123 in https://github.com/google/JetStream/pull/82
* Bump requests from 2.31.0 to 2.32.0 in the pip group across 1 directory by @dependabot in https://github.com/google/JetStream/pull/86
* Add profiling support and update docs by @JoeZijunZhou in https://github.com/google/JetStream/pull/85
* Add ray disaggregated serving support by @FanhaiLu1 in https://github.com/google/JetStream/pull/87
* Ensure server warmup before benchmark by @JoeZijunZhou in https://github.com/google/JetStream/pull/91
* Add healthcheck support for JetStream by @vivianrwu in https://github.com/google/JetStream/pull/90
* Add JetStream E2E test CI by @JoeZijunZhou in https://github.com/google/JetStream/pull/89
* Release v0.2.2 by @JoeZijunZhou in https://github.com/google/JetStream/pull/95

## New Contributors
* @jwyang-google made their first contribution in https://github.com/google/JetStream/pull/76
* @Bslabe123 made their first contribution in https://github.com/google/JetStream/pull/71
* @vivianrwu made their first contribution in https://github.com/google/JetStream/pull/90

**Full Changelog**: https://github.com/google/JetStream/compare/v0.2.1...v0.2.2

## v0.3 (2024-12-18)

## Key Changes 
* Observability improvements in JetStream Server (prometheus metrics)
* Tensorboard support for remote access
* Engine API update for TTFT and TPOT measurements
* Hugginface tokenizer support
* Copybara G3 support
* Threading optimizations

## What's Changed
* Add tensorboard plugin dep for remote access by @JoeZijunZhou in https://github.com/AI-Hypercomputer/JetStream/pull/97
* Update benchmark config for xlml automation by @morgandu in https://github.com/AI-Hypercomputer/JetStream/pull/96
* Minor fix by @morgandu in https://github.com/AI-Hypercomputer/JetStream/pull/98
* Add ssh port forward support for profile readme by @FanhaiLu1 in https://github.com/AI-Hypercomputer/JetStream/pull/99
* Add inference sampling utils in JetStream by @JoeZijunZhou in https://github.com/AI-Hypercomputer/JetStream/pull/100
* Add profiling server for proxy backend by @zhihaoshan-google in https://github.com/AI-Hypercomputer/JetStream/pull/101
* Change `jetstream_slots_available_percentage` to `jetstream_slots_used_percentage` by @Bslabe123 in https://github.com/AI-Hypercomputer/JetStream/pull/102
* Bump urllib3 from 2.2.0 to 2.2.2 in the pip group across 1 directory by @dependabot in https://github.com/AI-Hypercomputer/JetStream/pull/104
* Added `jetstream_transfer_backlog_size` and `jetstream_generate_backlog_size` metrics by @Bslabe123 in https://github.com/AI-Hypercomputer/JetStream/pull/103
* Update docs for benchmark warmup mode by @JoeZijunZhou in https://github.com/AI-Hypercomputer/JetStream/pull/106
* Update docs with metrics observation instructions by @Bslabe123 in https://github.com/AI-Hypercomputer/JetStream/pull/107
* Prefill return first token by @jwyang-google in https://github.com/AI-Hypercomputer/JetStream/pull/105
* change the detokenization thread to return the actual eos token. by @jwyang-google in https://github.com/AI-Hypercomputer/JetStream/pull/108
* Add loadgen in dev image  by @morgandu in https://github.com/AI-Hypercomputer/JetStream/pull/109
* Bump certifi from 2024.2.2 to 2024.7.4 in the pip group by @dependabot in https://github.com/AI-Hypercomputer/JetStream/pull/110
* Bump zipp from 3.17.0 to 3.19.1 in the pip group by @dependabot in https://github.com/AI-Hypercomputer/JetStream/pull/111
* Model warmup support with AOT and endpoint for JetStream by @vivianrwu in https://github.com/AI-Hypercomputer/JetStream/pull/92
* Cleanup orchestrator proto by @JoeZijunZhou in https://github.com/AI-Hypercomputer/JetStream/pull/112
* Update images for mlperf by @morgandu in https://github.com/AI-Hypercomputer/JetStream/pull/113
* image fix by @morgandu in https://github.com/AI-Hypercomputer/JetStream/pull/114
* del prefill_result & update dev image by @morgandu in https://github.com/AI-Hypercomputer/JetStream/pull/116
* Fix benchmark script for saving benchmark result by @lsy323 in https://github.com/AI-Hypercomputer/JetStream/pull/117
* Add `jetstream_server_startup_latency` metric by @Bslabe123 in https://github.com/AI-Hypercomputer/JetStream/pull/118
* Add http server to JetStream by @JoeZijunZhou in https://github.com/AI-Hypercomputer/JetStream/pull/115
* Free engine resource for the slot after finished one request decoding by @FanhaiLu1 in https://github.com/AI-Hypercomputer/JetStream/pull/119
* Add `jetstream_request_success_count` metric by @Bslabe123 in https://github.com/AI-Hypercomputer/JetStream/pull/124
* Request input/output size metrics by @Bslabe123 in https://github.com/AI-Hypercomputer/JetStream/pull/123
* Makefile by @Bslabe123 in https://github.com/AI-Hypercomputer/JetStream/pull/125
* Various request time metrics by @Bslabe123 in https://github.com/AI-Hypercomputer/JetStream/pull/121
* Standalone JetStream removes pinned deps by @JoeZijunZhou in https://github.com/AI-Hypercomputer/JetStream/pull/129
* Update deps file by @JoeZijunZhou in https://github.com/AI-Hypercomputer/JetStream/pull/130
* Manual model warmup to resolve AOT model warmup performance degradation by @vivianrwu in https://github.com/AI-Hypercomputer/JetStream/pull/126
* Update JetStream instructions by @yeandy in https://github.com/AI-Hypercomputer/JetStream/pull/132
* Add an optional parameter for sampling in prefill / sample. by @qihqi in https://github.com/AI-Hypercomputer/JetStream/pull/133
* remove excessive logs in production run by changing from DEBUG to INFO by @jwyang-google in https://github.com/AI-Hypercomputer/JetStream/pull/134
* Change the default message for requester.py and remove mlperf 4.1 install for proxy version support. by @zhihaoshan-google in https://github.com/AI-Hypercomputer/JetStream/pull/136
* Change previewutilities -> pathwaysutils by @vivianrwu in https://github.com/AI-Hypercomputer/JetStream/pull/138
* Add option to use hf tokenizer by @RissyRan in https://github.com/AI-Hypercomputer/JetStream/pull/147
* Rename third_party folder to Avoid Copybara g3 Errors  by @jyj0w0 in https://github.com/AI-Hypercomputer/JetStream/pull/148
* add seperate prefill detokenization thread by @zhihaoshan-google in https://github.com/AI-Hypercomputer/JetStream/pull/152
* Revert the change created by copybara  by @jyj0w0 in https://github.com/AI-Hypercomputer/JetStream/pull/156

## New Contributors
* @lsy323 made their first contribution in https://github.com/AI-Hypercomputer/JetStream/pull/117
* @RissyRan made their first contribution in https://github.com/AI-Hypercomputer/JetStream/pull/147
* @jyj0w0 made their first contribution in https://github.com/AI-Hypercomputer/JetStream/pull/148

**Full Changelog**: https://github.com/AI-Hypercomputer/JetStream/compare/v0.2.2...v0.3
