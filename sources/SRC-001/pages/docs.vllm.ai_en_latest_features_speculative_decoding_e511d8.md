source: https://docs.vllm.ai/en/latest/features/speculative_decoding/
lastmod: 2026-09-24

# Speculative Decoding[¶](https://docs.vllm.ai#speculative-decoding)

This document shows how to use [Speculative Decoding](https://arxiv.org/pdf/2302.01318) with vLLM to reduce inter-token latency under medium-to-low QPS (queries per second), memory-bound workloads.

To train your own draft models for optimized speculative decoding, see [vllm-project/speculators](https://docs.vllm.ai/speculators/) for seamless training and integration with vLLM.

## vLLM Speculation Methods[¶](https://docs.vllm.ai#vllm-speculation-methods)

vLLM supports a variety of methods of speculative decoding. Model-based methods such as EAGLE, MTP, draft models, PARD and MLP provide the best latency reduction, while simpler methods such as n-gram and suffix decoding provide modest speedups without increasing workload during peak traffic.

[EAGLE](https://docs.vllm.ai/eagle/)[Multi-Token Prediction (MTP)](https://docs.vllm.ai/mtp/)[Draft Model](https://docs.vllm.ai/draft_model/)[Parallel Draft Model (PARD)](https://docs.vllm.ai/parallel_draft_model/)[Multi-Layer Perceptron](https://docs.vllm.ai/mlp/)[N-Gram](https://docs.vllm.ai/n_gram/)[Suffix Decoding](https://docs.vllm.ai/suffix/)[Hidden State Extraction](https://docs.vllm.ai/extract_hidden_states/)[Custom Proposer Backend (Experimental)](https://docs.vllm.ai#custom-proposer-backend-experimental)[Dynamic Speculative Decoding](https://docs.vllm.ai/dynamic_speculative_decoding/)[Adaptive Verification](https://docs.vllm.ai/adaptive_verification/)[Per-Request Acceptance Metrics](https://docs.vllm.ai/acceptance_metrics/)

## Method Selection at a Glance[¶](https://docs.vllm.ai#method-selection-at-a-glance)

Use this qualitative table as a starting point for method selection. Real gains depend on your model family, traffic pattern, hardware, and sampling settings.

| Method | Low QPS (latency focused) | High QPS (throughput focused) | Notes |
|---|---|---|---|
| EAGLE | High gain | Medium to high gain | Strong general-purpose model-based method. |
| MTP | High gain | Medium to high gain | Best when the target model has native MTP support. |
| Draft model | High gain | Medium gain | Needs a separate draft model. |
| Parallel Draft Model | High gain | Medium to high gain | Low draft model latency. |
| MLP speculator | Medium to high gain | Medium gain | Good when compatible MLP speculators are available. |
| N-gram | Low to medium gain | Medium gain | Lightweight and easy to enable. |
| Suffix decoding | Low to medium gain | Medium gain | No extra draft model; dynamic speculation depth. |
| Custom Proposer | Varies | Varies | Bring your own proposer class (experimental). |
| Dynamic Speculative Decoding | High gain | Higher than base SD method | Useful for RL or workload with fluctuating QPS |
| Adaptive Verification | High gain | Higher than base SD method | Sizes verification per request from drafter confidence; currently DSpark only. |

For reproducible measurements in your environment, use [ examples/features/speculative_decoding/spec_decode_offline.py](https://github.com/vllm-project/vllm/blob/main/examples/features/speculative_decoding/spec_decode_offline.py) or the

[benchmark CLI guide](https://docs.vllm.ai/benchmarking/cli/).

## Custom Proposer Backend (Experimental)[¶](https://docs.vllm.ai#custom-proposer-backend-experimental)

You can plug in your own custom proposer class for speculative decoding by setting the method to `custom_class`

and providing the full module path to your class. Your custom class must accept a [ VllmConfig](https://docs.vllm.ai/api/vllm/config/vllm/#vllm.config.vllm.VllmConfig) upon instantiation and implement a

`propose`

method.**Example configuration:**

`speculative_config.method = "custom_class"`

`speculative_config.model = "your_module.YourCustomProposerClass"`


`--speculative-config`

schema[¶](https://docs.vllm.ai#-speculative-config-schema)

Use `--speculative-config`

to pass speculative decoding settings as a JSON object on the CLI:

```bash
vllm serve <target-model> \
--speculative-config '{
"method": "draft_model",
"model": "<draft-model>",
"num_speculative_tokens": 5
}'
```


The same keys are accepted from Python via `LLM(..., speculative_config={...})`

. The tables below highlight common user-facing keys accepted in this JSON object; they are not an exhaustive schema reference. For more details, see the generated [engine arguments reference](https://docs.vllm.ai/configuration/engine_args/) and the API docs for [vllm.config.SpeculativeConfig](https://docs.vllm.ai/api/vllm/config/#vllm.config.SpeculativeConfig).

### Common keys[¶](https://docs.vllm.ai#common-keys)

These keys are commonly used across speculative decoding setups, though some only apply to model-based methods such as `draft_model`

, `mtp`

, `eagle3`

, and `dflash`

.

| Key | Type | Default | Allowed values / meaning |
|---|---|---|---|
`method` | `string` | `None` | Speculation method. Common values include `draft_model` , `ngram` , `suffix` , `mtp` , `eagle3` , and `dflash` . If omitted, vLLM infers the method from the provided configuration when possible. |
`model` | `string` | `None` | Draft model, EAGLE head, or auxiliary model identifier. For `ngram` , `ngram_gpu` , `suffix` , and `mtp` , this can often be omitted. |
`num_speculative_tokens` | `integer > 0` | `None` | Number of speculative tokens to propose per step. Required for methods that do not infer it from model metadata. |
`draft_tensor_parallel_size` | `integer >= 1` | `None` | Tensor parallel size for the draft model. |
`max_model_len` | `integer >= 1` | `None` | Maximum context length for the draft model. |
`parallel_drafting` | `boolean` | `false` | Enable parallel draft token generation. Only compatible with EAGLE and draft-model methods. |
`rejection_sample_method` | `string` | `standard` | `standard` , `synthetic` , or `block` . |
`synthetic_acceptance_rates` | `list[float]` | `None` | Per-position unconditional acceptance rates for `synthetic` rejection sampling. Each entry in `[0, 1]` ; length must equal `num_speculative_tokens` ; must be non-increasing. |
`synthetic_acceptance_length` | `float` | `None` | Target mean acceptance length for `synthetic` ; in `[1, num_speculative_tokens + 1]` . Mutually exclusive with `synthetic_acceptance_rates` . |
`use_heterogeneous_vocab` | `boolean` | `false` | Allow draft and target models with different vocabularies. Builds a token-level intersection at initialisation and constrains draft logits to shared tokens only. Only compatible with `method=draft_model` . Probabilistic draft sampling (`draft_sample_method='probabilistic'` ) is not yet supported when this option is enabled. |

Note

Gemma 4 assistant checkpoints are handled as Gemma 4 MTP speculators, not as generic draft models. Use `"method": "mtp"`

with the assistant checkpoint in `model`

, as shown in the [MTP guide](https://docs.vllm.ai/mtp/#gemma-4-assistant-models).

If startup logs show `SpeculativeConfig(method='draft_model', ...)`

for a Gemma 4 assistant checkpoint, the installed vLLM version does not include Gemma 4 MTP support for that path. Upgrade to a version that includes Gemma 4 MTP support instead of forcing the assistant checkpoint through generic draft-model speculative decoding.

### Method-specific keys[¶](https://docs.vllm.ai#method-specific-keys)

#### N-gram[¶](https://docs.vllm.ai#n-gram)

| Key | Type | Default | Meaning |
|---|---|---|---|
`prompt_lookup_max` | `integer >= 1` | `5` if both lookup bounds are omitted; otherwise mirrors `prompt_lookup_min` when omitted | Maximum n-gram window size. |
`prompt_lookup_min` | `integer >= 1` | `5` if both lookup bounds are omitted; otherwise mirrors `prompt_lookup_max` when omitted | Minimum n-gram window size. |

Example:

```bash
vllm serve <target-model> \
--speculative-config '{
"method": "ngram",
"num_speculative_tokens": 4,
"prompt_lookup_min": 2,
"prompt_lookup_max": 5
}'
```


#### Suffix decoding[¶](https://docs.vllm.ai#suffix-decoding)

| Key | Type | Default | Meaning |
|---|---|---|---|
`suffix_decoding_max_tree_depth` | `integer` | `24` | Maximum combined prefix-match and speculation tree depth. |
`suffix_decoding_max_cached_requests` | `integer` | `10000` | Maximum number of requests cached in the global suffix tree. Set `0` to disable the global cache. |
`suffix_decoding_max_spec_factor` | `float` | `1.0` | Caps speculative length as a multiple of prefix-match length. |
`suffix_decoding_min_token_prob` | `float` | `0.1` | Minimum estimated token probability required to speculate a token. |

Example:

```json
vllm serve <target-model> \
--speculative-config '{
"method": "suffix",
"num_speculative_tokens": 8,
"suffix_decoding_max_tree_depth": 24,
"suffix_decoding_max_cached_requests": 10000,
"suffix_decoding_max_spec_factor": 1.0,
"suffix_decoding_min_token_prob": 0.1
}'
```


#### Cross-Vocabulary Draft Models (TLI)[¶](https://docs.vllm.ai#cross-vocabulary-draft-models-tli)

By default, vLLM requires the draft and target models to share the same vocabulary. Setting `use_heterogeneous_vocab: true`

enables the **Token-Level Intersection (TLI)** algorithm, which allows draft models from a different model family with a different tokenizer.

At initialisation, vLLM builds a mapping between the two vocabularies by normalising token strings and computing their intersection. Draft logits are constrained to the shared tokens before sampling, and the sampled token IDs are translated to the target vocabulary before rejection sampling.

```python from vllm import LLM, SamplingParams

llm = LLM( model="Qwen/Qwen3-8B", speculative_config={

"method": "draft_model", "model": "HuggingFaceTB/SmolLM2-135M-Instruct", "num_speculative_tokens": 3, "use_heterogeneous_vocab": True, }, gpu_memory_utilization=0.5, ) ```

### Notes[¶](https://docs.vllm.ai#notes)

`--speculative-config`

expects a JSON object on the CLI. In YAML config files, use a nested mapping instead of an escaped JSON string.`tensor_parallel_size`

is not a valid key in`speculative_config`

. Use`draft_tensor_parallel_size`

instead.- Keys such as
`temperature`

and`top_p`

are sampling parameters, not`--speculative-config`

fields. - Internal fields such as
`target_model_config`

,`draft_model_config`

,`target_parallel_config`

,`draft_parallel_config`

, and`draft_load_config`

are populated by vLLM and are not intended to be set by users. `use_heterogeneous_vocab`

currently supports greedy draft sampling only. Probabilistic acceptance (temperature > 0 draft sampling) is not yet supported and will be added in a future release.

## Lossless guarantees of Speculative Decoding[¶](https://docs.vllm.ai#lossless-guarantees-of-speculative-decoding)

In vLLM, speculative decoding aims to enhance inference efficiency while maintaining accuracy. This section addresses the lossless guarantees of speculative decoding, breaking down the guarantees into three key areas:

-
**Theoretical Losslessness**- Speculative decoding sampling is theoretically lossless up to the precision limits of hardware numerics. Floating-point errors might cause slight variations in output distributions, as discussed in[Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/pdf/2302.01318) -
**Algorithmic Losslessness**- vLLM’s implementation of speculative decoding is algorithmically validated to be lossless. Key validation tests include:**Rejection Sampler Convergence**: Ensures that samples from vLLM’s rejection sampler align with the target distribution.[View Test Code](https://github.com/vllm-project/vllm/blob/47b65a550866c7ffbd076ecb74106714838ce7da/tests/samplers/test_rejection_sampler.py#L252)**Greedy Sampling Equality**: Confirms that greedy sampling with speculative decoding matches greedy sampling without it. This verifies that vLLM's speculative decoding framework, when integrated with the vLLM forward pass and the vLLM rejection sampler, provides a lossless guarantee. Almost all of the tests in[tests/spec_decode/e2e](https://github.com/vllm-project/vllm/tree/main/tests/v1/spec_decode)verify this property using[this assertion implementation](https://github.com/vllm-project/vllm/blob/b67ae00cdbbe1a58ffc8ff170f0c8d79044a684a/tests/spec_decode/e2e/conftest.py#L291)

-
**vLLM Logprob Stability**- vLLM does not currently guarantee stable token log probabilities (logprobs). This can result in different outputs for the same request across runs. For more details, see the FAQ section titled*Can the output of a prompt vary across runs in vLLM?*in the[FAQs](https://docs.vllm.ai/usage/faq/).

While vLLM strives to ensure losslessness in speculative decoding, variations in generated outputs with and without speculative decoding can occur due to following factors:

**Floating-Point Precision**: Differences in hardware numerical precision may lead to slight discrepancies in the output distribution.**Batch Size and Numerical Stability**: Changes in batch size may cause variations in logprobs and output probabilities, potentially due to non-deterministic behavior in batched operations or numerical instability.

For mitigation strategies, please refer to the FAQ entry *Can the output of a prompt vary across runs in vLLM?* in the [FAQs](https://docs.vllm.ai/usage/faq/).

## Known Feature Incompatibility[¶](https://docs.vllm.ai#known-feature-incompatibility)

- Pipeline parallelism is not composable with speculative decoding as of
`vllm<=0.15.0`

- Speculative decoding with draft models is not supported in
`vllm<=0.10.0`