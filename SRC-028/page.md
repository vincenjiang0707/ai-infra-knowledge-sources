# JetStream

source: https://github.com/AI-Hypercomputer/maxtext/releases

# Releases: AI-Hypercomputer/maxtext

## Release list

## mlperf6.1-dsv3-v3.0

mlperf6.1-dsv3-v3.0

## mlperf6.1-dsv3-v2.0

Branch cut for MLPerf 6.1 on DS v3

## mlperf6.1-dsv3-v1.0

Initial branch cut for MLPerf 6.1 on DS v3

## maxtext-v0.2.4

#### Changes

-
**Flax NNX Migration**: Enabled`pure_nnx`

,`enable_nnx`

, and`pure_nnx_decoder`

configurations by default ([PR #3526](https://github.com/AI-Hypercomputer/maxtext/pull/3526)), migrating MaxText primarily on Flax NNX ([PR #2885](https://github.com/AI-Hypercomputer/maxtext/pull/2885)). -
**Dependency Upgrades**: Upgraded JAX to version 0.10.2 for pre-training and 0.11.0 for post-training. -
**Model Support & Architecture**:**DeepSeek-V4**: Full model integration, decoders, and configuration stack ([PR #4153](https://github.com/AI-Hypercomputer/maxtext/pull/4153)), added HyperHead, aligned Sinkhorn implementation ([PR #4337](https://github.com/AI-Hypercomputer/maxtext/pull/4337)), and added checkpoint conversion support ([PR #4336](https://github.com/AI-Hypercomputer/maxtext/pull/4336)). See the[user guide](https://github.com/AI-Hypercomputer/maxtext/blob/main/tests/end_to_end/tpu/deepseek/Run_DeepSeek.md)for more details.**Qwen3-VL**: Added support for Qwen3-VL models ([PR #4293](https://github.com/AI-Hypercomputer/maxtext/pull/4293),[PR #4517](https://github.com/AI-Hypercomputer/maxtext/pull/4517)) and Qwen3-VL-4B ([PR #4263](https://github.com/AI-Hypercomputer/maxtext/pull/4263)).**Apple Envy MoE**: Added model configurations and support for Apple Envy Switch architectures.**Chunked MoE**: Added chunked MoE support via`num_moe_token_chunks`

to reduce memory footprint ([PR #4499](https://github.com/AI-Hypercomputer/maxtext/pull/4499)).**Block Diffusion**: Added block-diffusion pre-training support ([PR #4776](https://github.com/AI-Hypercomputer/maxtext/pull/4776)), model-independent block corruption utilities ([PR #4737](https://github.com/AI-Hypercomputer/maxtext/pull/4737)), and causal-block attention across Dense, Splash, and Tokamax kernels ([PR #4743](https://github.com/AI-Hypercomputer/maxtext/pull/4743)).

-
**LoRA & QLoRA**: Added native LoRA and QLoRA support for Gemma4, Gemma3, Qwen3, and Llama3, along with interactive tutorials ([PR #3969](https://github.com/AI-Hypercomputer/maxtext/pull/3969),[PR #4265](https://github.com/AI-Hypercomputer/maxtext/pull/4265),[PR #4068](https://github.com/AI-Hypercomputer/maxtext/pull/4068),[PR #3968](https://github.com/AI-Hypercomputer/maxtext/pull/3968),[PR #3970](https://github.com/AI-Hypercomputer/maxtext/pull/3970),[PR #4417](https://github.com/AI-Hypercomputer/maxtext/pull/4417)). -
**Context Parallelism (CP), Ring Attention**:- Added Ulysses and USP CP strategy and packing (
[PR #4687](https://github.com/AI-Hypercomputer/maxtext/pull/4687),[PR #4825](https://github.com/AI-Hypercomputer/maxtext/pull/4825),[PR #4836](https://github.com/AI-Hypercomputer/maxtext/pull/4836)), Tokamax load-balanced Ring Attention ([PR #4266](https://github.com/AI-Hypercomputer/maxtext/pull/4266),[PR #4537](https://github.com/AI-Hypercomputer/maxtext/pull/4537),[PR #4622](https://github.com/AI-Hypercomputer/maxtext/pull/4622)), and sequence packing for USP and All-Gather CP ([PR #4230](https://github.com/AI-Hypercomputer/maxtext/pull/4230),[PR #4887](https://github.com/AI-Hypercomputer/maxtext/pull/4887)). - DeepSeek MoE & MLA: Added Ring Attention with DSA Sparse Indexer
[PR #4767](https://github.com/AI-Hypercomputer/maxtext/pull/4767), auxiliary loss-free and sequence-wise load balancing[PR #4753](https://github.com/AI-Hypercomputer/maxtext/pull/4753), MLA QK head chunking[PR #4564](https://github.com/AI-Hypercomputer/maxtext/pull/4564), optimized generate_mask[PR #4437](https://github.com/AI-Hypercomputer/maxtext/pull/4437), and Approximate Top-K[PR #4243](https://github.com/AI-Hypercomputer/maxtext/pull/4243). - Positional Embeddings: Added YaRN RoPE config
[PR #4238](https://github.com/AI-Hypercomputer/maxtext/pull/4238), standardized MRoPE to BS3 convention for multimodal training[PR #4709](https://github.com/AI-Hypercomputer/maxtext/pull/4709), and fixed Qwen3.5 partial rotary factor handling. - Kernels & Megacore: Added configurable attention_for_vit kernels
[PR #4232](https://github.com/AI-Hypercomputer/maxtext/pull/4232)and enabled Megacore for Splash Attention dkv backward[PR #4755](https://github.com/AI-Hypercomputer/maxtext/pull/4755).

- Added Ulysses and USP CP strategy and packing (
-
**Quantization & Performance**: Added FP4 [E2M1] ([PR #4495](https://github.com/AI-Hypercomputer/maxtext/pull/4495)) and experimental attention quantization ([PR #4487](https://github.com/AI-Hypercomputer/maxtext/pull/4487)); enabled TE Collective GEMMs ([PR #4470](https://github.com/AI-Hypercomputer/maxtext/pull/4470)) and overlap ([PR #4307](https://github.com/AI-Hypercomputer/maxtext/pull/4307)), MoE comms with collective matmul ([PR #4295](https://github.com/AI-Hypercomputer/maxtext/pull/4295)), Tokamax GMM v2 ([MoE configuration guide](https://github.com/AI-Hypercomputer/maxtext/blob/main/docs/reference/core_concepts/moe_configuration.md)), and double-buffered inner scans during gradient accumulation ([PR #4316](https://github.com/AI-Hypercomputer/maxtext/pull/4316)). -
**Checkpointing**: Added support for Multi-tier checkpointing in Pathways. -
**Goodput & Elasticity**: -
**Post Training**:- Added
`reward_functions_path`

and`reward_functions`

CLI knobs for custom rewards ([PR #4149](https://github.com/AI-Hypercomputer/maxtext/pull/4149)) to RL training. - Updated tutorials with
`AgenticGRPOLearner`

for async RL training ([PR #4181](https://github.com/AI-Hypercomputer/maxtext/pull/4181)) and added GRPO Gemma4-e4b tutorial ([PR #4427](https://github.com/AI-Hypercomputer/maxtext/pull/4427)). - Added RL support for Qwen3 30B and GPT-OSS 20B. See the
[Qwen3 30B RL tutorial](https://maxtext.readthedocs.io/en/latest/tutorials/posttraining/rl_qwen3_30b.html)and[GPT-OSS 20B RL tutorial](https://maxtext.readthedocs.io/en/latest/tutorials/posttraining/rl_gptoss_20b.html)for recipes. - Added support for DPO along with tutorials (
[PR #4362](https://github.com/AI-Hypercomputer/maxtext/pull/4362)).

- Added
-
**Usability & Infrastructure**:- Added wandb logging support (
[PR #3053](https://github.com/AI-Hypercomputer/maxtext/pull/3053)). - Added Hugging Face Grain streaming integration and onboarding guide (
[PR #4486](https://github.com/AI-Hypercomputer/maxtext/pull/4486)). - Added Simple-evals runner support for gpt-oss model family (
[PR #4644](https://github.com/AI-Hypercomputer/maxtext/pull/4644)). - Added scripts to run vanilla DiLoCo on MaxText (
[PR #4095](https://github.com/AI-Hypercomputer/maxtext/pull/4095)). - Added option to enable on-demand profiling server in ML Diagnostics (
[PR #4131](https://github.com/AI-Hypercomputer/maxtext/pull/4131)).

- Added wandb logging support (

#### Bug Fixes

-
**Post-Training**:- Resolved Gemma 3/4 RL rollout gibberish issue by unrolling scanned weights for vLLM adapter (
[PR #4536](https://github.com/AI-Hypercomputer/maxtext/pull/4536),[PR #4519](https://github.com/AI-Hypercomputer/maxtext/pull/4519),[PR #4404](https://github.com/AI-Hypercomputer/maxtext/pull/4404)). - Fixed RL LR schedule defaults (
[PR #4225](https://github.com/AI-Hypercomputer/maxtext/pull/4225)), added`drop_remainder=True`

to prevent shape mismatches on tail batches during GRPO training ([PR #4252](https://github.com/AI-Hypercomputer/maxtext/pull/4252)) and resolved Qwen3.5 MRoPE/Kv-cache rollout issues ([PR #4177](https://github.com/AI-Hypercomputer/maxtext/pull/4177)).

- Resolved Gemma 3/4 RL rollout gibberish issue by unrolling scanned weights for vLLM adapter (
-
**Compilation**: -
**Model-Specific Fixes**: -
**NNX, MoE & MTP**:

#### Deprecations

**Tensor Transpose Parallelism Removed**: Completely removed the`tensor_transpose`

physical mesh axis and deleted`ici_tensor_transpose_parallelism`

and`dcn_tensor_transpose_parallelism`

configuration options.**Flax Linen Deprecation Warning**: Flax Linen is now deprecated in favor of Flax NNX; running with`pure_nnx=False`

or`enable_nnx=False`

will issue a deprecation warning.

## maxtext-v0.2.3

## Changes

- Upgraded JAX to version 0.10.0 for pre-training and 0.10.1 for post-training.
**New vLLM-Powered Evaluation Framework**: Introduced an eval framework for running lm-eval, evalchemy, and custom benchmarking against MaxText checkpoints. See the[evaluation guide](https://maxtext.readthedocs.io/en/latest/guides/eval_framework.html)for details.- Added support for pre-training new models:
**Direct Preference Optimization (DPO/ORPO) Support**: Full support for DPO and ORPO alignment pipelines. See the[DPO tutorial](https://maxtext.readthedocs.io/en/latest/tutorials/posttraining/dpo.html)for details.**Reinforcement Learning (RL) Recipe**: Added a pre-configured[RL recipe for Qwen3-30b-a3b](https://maxtext.readthedocs.io/en/latest/tutorials/posttraining/rl_qwen3_30b.html).**Iterative Quality Monitoring (RL)**: Added intermediate evaluation hooks to automatically run quality benchmarks during RL training (every`eval_interval`

steps), optimized with a new`eval_batch_size`

configuration knob.**Developer Extensibility**: Added`dataset_processor_path`

CLI knob for custom dataset integration, and refactored shared post-training hooks to simplify custom SFT, DPO, and RL workflow development.**Generalized Learn-to-Init (LTI) for Distillation**: Enhanced post-training distillation capabilities with generalized LTI support.- Added support for recording elastic goodput events during training to track efficiency (
[PR #3901](https://github.com/AI-Hypercomputer/maxtext/pull/3901)). **Installation Updates**: Updated the`[tpu-post-train]`

installation command to require`UV_TORCH_BACKEND=cpu`

(see[Installation Guide](https://github.com/AI-Hypercomputer/maxtext/blob/maxtext-v0.2.3/install_maxtext.md)).**Zero1 AOT Compilation**: Added zero1 support to Ahead-Of-Time (AOT) compilation in train compile, improving compilation capabilities for zero1 config.**MoE Performance Optimization**: Integrated ragged gather reduce into Mixture of Experts (MoE) layers to optimize memory and performance by replacing ragged scatter and supporting backward pass.- Added
[E2E scripts](https://github.com/AI-Hypercomputer/maxtext/tree/main/tests/end_to_end/tpu/gemma3/4b)to run checkpoint conversion, pre-training and post-training (SFT, RL) with Gemma3-4B model. **Bug Fixes and Usability Enhancements**:**Attention Masking Fix in RL**: Fixed an issue in`TunixMaxTextAdapter`

where queries at non-pad positions could attend to pad-position keys during training, which was corrupting log-probabilities and affecting GRPO training reward trajectories ([PR #4016](https://github.com/AI-Hypercomputer/maxtext/pull/4016)).**JAX/NNX Gradient Mutation Fix**: Refactored post-training loops (`train_distill`

,`train_sft`

,`train_rl`

) to use`jax.value_and_grad`

with explicit NNX state split/merge instead of nesting`nnx.value_and_grad`

inside`nnx.jit`

([PR #3652](https://github.com/AI-Hypercomputer/maxtext/pull/3652)).**Qwen3-MoE Checkpoint Conversion**: Fixed checkpoint conversion issues for Qwen3-MoE models ([PR #3868](https://github.com/AI-Hypercomputer/maxtext/pull/3868)).**Duplicate Configuration Failures Fix**: Allowed identical config overrides and handled configuration exceptions cleanly ([PR #3933](https://github.com/AI-Hypercomputer/maxtext/pull/3933)).

**Documentation Improvements**: Updated[Getting started](https://maxtext.readthedocs.io/en/latest/getting_started.html)guide, including new guides for the[evaluation framework](https://maxtext.readthedocs.io/en/latest/guides/eval_framework.html)and the[DPO tutorial](https://maxtext.readthedocs.io/en/latest/tutorials/posttraining/dpo.html).

## Deprecations

- Deleted
[legacy DPO implementation](https://github.com/AI-Hypercomputer/maxtext/pull/3997)in favor of the integrated[DPO trainer](https://maxtext.readthedocs.io/en/latest/tutorials/posttraining/dpo.html). - Removed stack trace collection feature.

## maxtext-v0.2.2

### Changes

- Upgraded JAX to version 0.9.2, improving support for both pre-training and post-training.
- Introduced simplified APIs for accessing MaxText models.
- Included
[maxtext_with_gepa.ipynb](https://github.com/AI-Hypercomputer/maxtext/blob/3c7d8d27864fc12cccac07786f02bd0e5262c982/src/maxtext/examples/maxtext_with_gepa.ipynb), a new notebook demonstrating AIME prompt optimization using the GEPA framework within MaxText. - Added support for Kimi-K2 models and the MuonClip optimizer. Users can explore this with the
[kimi-k2-1t](https://github.com/AI-Hypercomputer/maxtext/blob/fa5b5ebf9a8e4f7a33bd88eae051dc21f3147791/src/maxtext/configs/models/kimi-k2-1t.yml)config (see[user guide](https://github.com/AI-Hypercomputer/maxtext/blob/fa5b5ebf9a8e4f7a33bd88eae051dc21f3147791/tests/end_to_end/tpu/kimi/Run_Kimi.md)for details). - Kimi-K2-Thinking, Kimi-K2.5 (text), and Kimi-K2.6 (text) are now supported. See
[Run_Kimi.md](https://github.com/AI-Hypercomputer/maxtext/blob/main/tests/end_to_end/tpu/kimi/Run_Kimi.md#quantized-variants-k2-thinking-k25-k26)for details. [DeepSeek-V3.2](https://arxiv.org/pdf/2512.02556)is now supported, including DeepSeek Sparse Attention for handling long contexts. Use the[deepseek3.2-671b](https://github.com/AI-Hypercomputer/maxtext/blob/20d93f62a91899dbbb8f23562973d75104411d3a/src/maxtext/configs/models/deepseek3.2-671b.yml)config to try it out (refer to the[user guide](https://github.com/AI-Hypercomputer/maxtext/blob/20d93f62a91899dbbb8f23562973d75104411d3a/tests/end_to_end/tpu/deepseek/Run_DeepSeek.md)for more information).- Support has been added for Gemma 4 multi-modal models (26B MoE and 31B dense). These can be used with the
[gemma4-26b](https://github.com/AI-Hypercomputer/maxtext/blob/cdc587f0935a5e2d6f8287b96669cf2e87a0acdc/src/maxtext/configs/models/gemma4-26b.yml)and[gemma4-31b](https://github.com/AI-Hypercomputer/maxtext/blob/cdc587f0935a5e2d6f8287b96669cf2e87a0acdc/src/maxtext/configs/models/gemma4-31b.yml)configs. See[Run_Gemma4.md](https://github.com/AI-Hypercomputer/maxtext/blob/cdc587f0935a5e2d6f8287b96669cf2e87a0acdc/tests/end_to_end/tpu/gemma4/Run_Gemma4.md)for further details. - Support has been added for Gemma 4 inference using
[MaxText on vLLM plugin](https://maxtext.readthedocs.io/en/maxtext-v0.2.2/tutorials/inference.html). - Enhanced RL capabilities with support for the
`open-r1/OpenR1-Math-220k`

dataset and`nvidia/OpenMathReasoning`

. - Added more evaluation modes for RL like majority voting and pass@1 estimation.
- Sync weights to vllm prior to pre RL evaluation.
- More robust usage of math-verify in RL.
- MaxText's Supervised Fine-Tuning (SFT) now supports non-instruct models.
- Added support for tensor parallelism using the Fused MoE kernel for MaxText on vLLM inference.
- Added support for MaxText to vllm converters for Qwen3 and Gemma4 family of models.
[validate_converter.py](https://github.com/AI-Hypercomputer/maxtext/blob/472f53b70089e661be399ad3905c05a53a172ec5/src/maxtext/integration/vllm/torchax_converter/validate_converter.py#L108)now runs on multislice environment to test larger models with utilities to compare maxtext and vllm weights.

### Deprecations

- Legacy
`MaxText.*`

shims have been removed. Please refer to[src/MaxText/README.md](https://github.com/AI-Hypercomputer/maxtext/blob/0536605a8ca116087ed93178433a67e905be566c/src/MaxText/README.md)for details on the new command locations and how to migrate. - Sequence parallelism has been deprecated, please use context parallelism instead.
- The flag
`expert_shard_attention_option`

is deprecated, use`custom_mesh_and_rule=ep-as-cp`

for the same functionality.

## maxtext-v0.2.1

- Use the new maxtext[runner] installation option to build Docker images without cloning the repository. This can be used for scheduling jobs through XPK. See the
[MaxText installation instructions](https://maxtext.readthedocs.io/en/maxtext-v0.2.1/build_maxtext.html)for more info. - Config can now be inferred for most MaxText commands. If you choose not to provide a config, MaxText will now
[select an appropriate one](https://github.com/AI-Hypercomputer/maxtext/blob/9e786c888cc7acdfc00a8f73064e285017e80b86/src/maxtext/configs/pyconfig.py#L51-L67). - Configs in MaxText PyPI will now be picked up without storing them locally.
- New features from DeepSeek-AI are now supported: Conditional Memory via Scalable Lookup (
[Engram](https://arxiv.org/abs/2601.07372)) and Manifold-Constrained Hyper-Connections ([mHC](https://arxiv.org/abs/2512.24880)). Try them out with our[deepseek-custom](https://github.com/AI-Hypercomputer/maxtext/blob/9e786c888cc7acdfc00a8f73064e285017e80b86/src/maxtext/configs/models/deepseek-custom.yml)starter config. - MaxText now supports customizing your own mesh and logical rules. Two examples guiding how to use your own mesh and rules for sharding are provided in the
[custom_mesh_and_rule](https://github.com/AI-Hypercomputer/maxtext/tree/9e786c888cc7acdfc00a8f73064e285017e80b86/src/maxtext/configs/custom_mesh_and_rule)directory.

## maxtext-v0.2.0

# Changes

[Qwen3-Next](https://github.com/AI-Hypercomputer/maxtext/blob/main/tests/end_to_end/tpu/qwen/next/run_qwen3_next.md)is now supported.- New
`tpu-post-train`

target in PyPI. Please also use this installation option for running vllm_decode. See the[MaxText installation instructions](https://maxtext.readthedocs.io/en/latest/install_maxtext.html)for more info. - New MaxText structure! MaxText has been restructured according to
[RESTRUCTURE.md](https://github.com/AI-Hypercomputer/maxtext/blob/1b9e38aa0a19b6018feb3aed757406126b6953a1/RESTRUCTURE.md). Please feel free to share your thoughts and feedback. [Muon optimizer](https://kellerjordan.github.io/posts/muon)is now supported.- DeepSeek V3.1 is now supported. Use existing configs for
[DeepSeek V3 671B](https://github.com/AI-Hypercomputer/maxtext/blob/main/src/maxtext/configs/models/deepseek3-671b.yml)and load in V3.1 checkpoint to use model. [New RL and SFT Notebook tutorials](https://github.com/AI-Hypercomputer/maxtext/tree/main/src/maxtext/examples)are available.- The
[ReadTheDocs documentation site](https://maxtext.readthedocs.io/en/latest/index.html)has been reorganized. - Multi-host support for GSPO and GRPO is now available via
[new RL tutorials](https://maxtext.readthedocs.io/en/latest/tutorials/posttraining/rl_on_multi_host.html). - A new guide,
[What is Post Training in MaxText?](https://maxtext.readthedocs.io/en/latest/tutorials/post_training_index.html), is now available. - Ironwood TPU co-designed AI stack announced. Read the
[blog post on its co-design with MaxText](https://cloud.google.com/blog/products/compute/inside-the-ironwood-tpu-codesigned-ai-stack?e=48754805). [Optimized models tiering documentation](https://maxtext.readthedocs.io/en/latest/reference/models/tiering.html)has been refreshed.- Added Versioning. Check out our
[first set of release notes](https://maxtext.readthedocs.io/en/latest/release_notes.html)! - Post-Training (SFT, RL) via
[Tunix](https://github.com/google/tunix)is now available. - Vocabulary tiling (
[PR](https://github.com/AI-Hypercomputer/maxtext/pull/2242)) is now supported in MaxText! Adjust config`num_vocab_tiling`

to unlock more efficient memory usage. - The GPT-OSS family of models (20B, 120B) is now supported.

# Deprecations

- Many MaxText modules have changed locations. Core commands like train, decode, sft, etc. will still work as expected temporarily. Please update your commands to the latest file locations
- install_maxtext_github_deps installation script replaced with install_maxtext_tpu_github_deps
`tools/setup/setup_post_training_requirements.sh`

for post training dependency installation is deprecated in favor of[pip installation](https://maxtext.readthedocs.io/en/latest/install_maxtext.html)

## maxtext-tutorial-v1.5.0

Merge pull request #2898 from AI-Hypercomputer:tests_docker_image PiperOrigin-RevId: 850456883

## maxtext-tutorial-v1.4.0

maxtext-tutorial-v1.4.0