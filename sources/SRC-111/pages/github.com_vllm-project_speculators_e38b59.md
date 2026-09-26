source: https://github.com/vllm-project/speculators

Speculators is a library for training speculative decoding draft models that deploy directly to LLM inference engines like vLLM. Speculative decoding is a lossless technique that speeds up LLM inference by using a smaller, faster draft model (i.e. "the speculator") to propose tokens, which are then verified by the larger base model, reducing latency without compromising output quality. The speculator intelligently drafts multiple tokens ahead of time, and the base model verifies them in a single forward pass. This approach boosts performance without sacrificing output quality, as every accepted token is guaranteed to match what the main model would have generated on its own.

Speculators standardizes this process by providing a productionized end-to-end framework to train draft models with reusable formats and tools. Trained models can seamlessly run in vLLM, enabling the deployment of speculative decoding in production-grade inference servers.


💬 Join us on the [vLLM Community Slack](https://inviter.co/vllm-slack) and share your questions, thoughts, or ideas in:

`#speculators`

`#feat-spec-decode`


🎥 Watch our Office Hours presentation: [Video](https://www.youtube.com/live/2ISAr_JVGLs) | [Slides](https://docs.google.com/presentation/d/1s4eAb7v-rdZt8smyULBJWGXjJXrgFTZWnwqYa2-h1l4/edit?slide=id.g3365e070742_6_0#slide=id.g3365e070742_6_0)

Big updates have landed in Speculators! To get a more in-depth look, check out the [Speculators documentation](https://docs.vllm.ai/projects/speculators/en/latest/).

Some of the exciting new features include:

**Multi-Node Online Training via hs_connectors**: Added theplugin package with pluggable backends for transferring hidden states between vLLM and the trainer across nodes. The file-based backend uses a shared filesystem, while the Mooncake backend leverages a distributed store for environments without shared storage, enabling online speculator training at multi-node scale.`hs_connectors`

**DSpark Training Algorithm**: Added support for the DSpark training algorithm, which extends DFlash's anchored-block drafting with a Markov head that conditions each draft position on the previous token within the block, plus a confidence head that predicts per-position acceptance probability. DSpark checkpoints can warm-start from existing DFlash checkpoints.**P-EAGLE Training Support**: Added support for the[P-EAGLE training algorithm](https://docs.vllm.ai/projects/speculators/en/latest/user_guide/algorithms/peagle), which extends EAGLE-3's architecture with parallel multi-token prediction via Conditional-On-Distribution (COD) sampling. Rather than generating draft tokens sequentially, P-EAGLE predicts multiple tokens in a single forward pass, reducing drafting latency. The Red Hat team published a[P-EAGLE speculator for Qwen3-8B](https://huggingface.co/RedHatAI/Qwen3-8B-speculator.peagle).**MTP Finetuning Support**: Added support for finetuning the native Multi-Token Prediction (MTP) heads of models like Qwen3-Next on domain-specific data, following the[FastMTP](https://arxiv.org/abs/2509.18362)approach. Because the MTP head is small (~100M–400M params), it can be trained on pre-extracted hidden states without loading the full verifier**Sliding Window Attention for DFlash and DSpark**: DFlash and DSpark speculators use sliding window attention on all draft layers by default. Use`--sliding-window`

to set the window size and`--full-attention-indices`

to opt specific layers into full attention. Sliding window attention reduces KV cache allocation for long-context sequences and can improve per-position acceptance rates compared to full attention.**DFlash Training Algorithm**: Added support for the DFlash training algorithm with anchored-block drafting, using auxiliary hidden states from multiple verifier layers. Includes CLI options for block size and max anchors, plus DFlash metrics, utilities, and draft model. DFlash models trained through Speculators can now run seamlessly in vLLM as of[vLLM PR #38300](https://github.com/vllm-project/vllm/pull/38300).

**Offline Training Data Generation using vLLM:**Enable the generation of hidden states using vLLM. Data samples are saved to disk and can be used for draft model training.**Draft Model Training Support:**E2E training support of single and multi-layer draft models. Training is supported for MoE, non-MoE, and Vision Language models.**Standardized, Extensible Format:**Provides a Hugging Face-compatible format for defining speculative models, with tools to convert from external research repositories into a standard speculators format for easy adoption.**Seamless vLLM Integration:**Built for direct deployment into vLLM, enabling low-latency, production-grade inference with minimal overhead.

Tip

Read more about Speculators features in this [vLLM blog post](https://blog.vllm.ai/2025/12/13/speculators-v030.html).

The following table summarizes the models that have been trained end-to-end by our team as well as others in the roadmap:

| Verifier Architecture | Verifier Size | Training Support | vLLM Deployment Support |
|---|---|---|---|
| Llama | 8B-Instruct |
|

[EAGLE-3](https://huggingface.co/RedHatAI/Llama-3.3-70B-Instruct-speculator.eagle3)✅[EAGLE-3](https://huggingface.co/RedHatAI/Qwen3-8B-speculator.eagle3)✅[DFlash](https://huggingface.co/RedHatAI/Qwen3-8B-speculator.dflash)✅[P-EAGLE](https://huggingface.co/RedHatAI/Qwen3-8B-speculator.peagle)✅[EAGLE-3](https://huggingface.co/RedHatAI/Qwen3-14B-speculator.eagle3)✅[EAGLE-3](https://huggingface.co/RedHatAI/Qwen3-32B-speculator.eagle3)✅[EAGLE-3](https://huggingface.co/RedHatAI/gpt-oss-20b-speculator.eagle3)✅[EAGLE-3](https://huggingface.co/RedHatAI/gpt-oss-120b-speculator.eagle3)✅[EAGLE-3](https://huggingface.co/RedHatAI/Qwen3-30B-A3B-Instruct-2507-speculator.eagle3)✅[DFlash](https://huggingface.co/RedHatAI/Qwen3-30B-A3B-Instruct-2507-speculator.dflash)✅[DFlash](https://huggingface.co/RedHatAI/Qwen3-30B-A3B-speculator.dflash)✅[EAGLE-3](https://huggingface.co/RedHatAI/Qwen3-235B-A22B-Instruct-2507-speculator.eagle3)✅[EAGLE-3](https://huggingface.co/RedHatAI/Qwen3-235B-A22B-speculator.eagle3)✅[EAGLE-3](https://huggingface.co/RedHatAI/Qwen3-VL-235B-A22B-Instruct-speculator.eagle3)✅[DFlash](https://huggingface.co/RedHatAI/Mistral-Small-4-119B-2603.dflash)✅[DSpark](https://huggingface.co/RedHatAI/Mistral-Small-4-119B-2603-speculator.dspark)✅[EAGLE-3](https://huggingface.co/RedHatAI/gemma-4-31B-it-speculator.eagle3)✅[DFlash](https://huggingface.co/RedHatAI/gemma-4-31B-it-speculator.dflash)✅[EAGLE-3](https://huggingface.co/RedHatAI/gemma-4-26B-A4B-it-speculator.eagle3)✅[DFlash](https://huggingface.co/RedHatAI/NVIDIA-Nemotron-3-Ultra-550B-A55B-speculator.dflash)✅[DFlash](https://huggingface.co/RedHatAI/NVIDIA-Nemotron-3-Super-120B-A12B-speculator.dflash)✅[DSpark](https://huggingface.co/RedHatAI/Kimi-K3-speculator.dspark)✅[DSpark](https://huggingface.co/RedHatAI/Qwen3.6-35B-A3B-speculator.dspark)✅[DSpark](https://huggingface.co/RedHatAI/GLM-5.2-speculator.dspark)✅✅ = Supported, ⏳ = In Progress, ❌ = Not Yet Supported

Models trained through Speculators can run seamlessly in vLLM using a simple `vllm serve <speculator_model>`

command. This will run the model in vLLM using default arguments, defined in the `speculator_config`

of the model's config.json.

`vllm serve RedHatAI/Qwen3-8B-speculator.eagle3`

Served models can then be benchmarked using [GuideLLM](https://github.com/vllm-project/guidellm). Below, we show sample benchmark results where we compare our speculator with its dense counterpart. We also additionally compare [quantization](https://github.com/vllm-project/llm-compressor) to explore additional performance improvements by swapping the dense verifier, `Qwen/Qwen3-8B`

with the quantized FP8 model, [RedHatAI/Qwen3-8B-FP8-dynamic](https://huggingface.co/RedHatAI/Qwen3-8B-FP8-dynamic) in the `speculator_config`

.


Before installing, ensure you have the following:

**Operating System:**Linux or macOS**Python:**3.10 or higher**Package Manager:**pip (recommended) or conda

Install the latest stable release from PyPI:

`pip install speculators`

For the latest development version or to contribute to the project:

```
git clone https://github.com/vllm-project/speculators.git
cd speculators
pip install -e .
```

For development with additional tools:

`pip install -e ".[dev]"`

You can verify your installation by checking the version:

`speculators --version`

Or by importing the package in Python:

```
import speculators
print(speculators.__version__)
```

Speculators is licensed under the [Apache License 2.0](https://github.com/vllm-project/speculators/blob/main/LICENSE).

If you find Speculators helpful in your research or projects, please consider citing it:

```
@misc{speculators2025,
title={Speculators: A Unified Library for Speculative Decoding Algorithms in LLM Serving},
author={Red Hat},
year={2025},
howpublished={\url{https://github.com/vllm-project/speculators}},
}
```