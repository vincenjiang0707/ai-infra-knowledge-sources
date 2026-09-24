# how-to-size-gpus-for-ai-inference-and-tco-without-overspending

source: https://developer.nvidia.com/blog/how-to-size-gpus-for-ai-inference-and-tco-without-overspending/

The surge in AI adoption is transforming everything from chatbots to content generation. Still, a common pain point remains: How can organizations confidently size GPU resources for inference workloads and optimize Total Cost of Ownership (TCO)? With a dizzying mix of latency targets, model choices, quirky traffic patterns, and budget constraints, it’s easy to feel lost in the weeds, even before you’ve deployed a single model.

Today’s inference landscape is shaped by more than just hardware specs or “tokens per second.” Teams face an ever-growing list of sizing decisions: What kind of latency actually matters, Time to First Token (TTFT) average, 99th percentile latency, intertoken latency, or something else? How will your use case’s token patterns drive GPU memory and compute needs? What’s the right balance between on-prem core capacity and cloud-based elasticity?

This post offers a practical framework for mapping your use case to the right GPU footprint, sizing inference GPU infrastructure around real workload behavior rather than guesswork. We’ll walk through the inputs that matter most, including use case, token patterns, latency targets, concurrency, cache hit rate, model choice, and deployment strategy. Along the way, developers and infrastructure teams will see how core-and-flex capacity planning, right-sized GPUs, and model optimization techniques such as quantization, pruning, and distillation can improve performance while lowering TCO.

## Know your use case: Where sizing and TCO begin

Cutting through the noise starts with one deceptively simple question: What problem are you solving? Different use cases map to wildly different infrastructure footprints. At a high level, most inference workloads fall into one of these four buckets:

- AI Chatbots/Copilots
- AI Agents (deep research and reasoning)
- Content Generation
- Translation Apps

| Use Case | Cached Input Tokens | Input Tokens | Output Tokens | Example Scenario |
|---|---|---|---|---|
| AI Chatbots/Copilots: Long input / short output | 1,000 – 5,000 | 2,000 – 8,000 | 200 – 800 | Limited RAG, multi-turn conversations |
| AI Agents: Extreme long context | >128,000 | 500 – 1,000 | 200 – 300 | Deep research, extended RAG |
| Content Generation: Short input / long output | 50 – 300 | 200 – 1,000 | 1,000 – 4,000 | Email/story generation, search |
| Translation Apps | 50 – 250 | 200 – 1,000 | 200 – 1,000 | Language/code translation, refactoring |

*Table 1. Use cases for GPU input and output tokens in various workload scenarios; these are illustrative figures, the values observed in real-world production scenarios could vary drastically*

### Key sizing inputs for smarter TCO

After mapping your use case, build your sizing plan around these dimensions:

**Model Selection (LLM):**Bigger isn’t always better. Consider mainstream models like Nemotron 3.5 Lightning, Inkling Small, Muse Glimmer, or others that fit your data and latency requirements. A smaller fine-tuned model could also be leveraged.**App Scale:**Gauge the size of your application and anticipate user base growth.**DAUs and Concurrency:**Know your Daily Active Users (DAUs) and how many requests they’ll issue simultaneously. High concurrency strains GPU memory and latency more than raw DAUs.**ISL/OSL:**Predict input and output string lengths (tokens per prompt), longer strings mean higher GPU memory and compute demand.**Cache hit rate:**Estimate the share of input tokens that repeat across requests and can be served from the KV cache rather than recomputed. A higher cache hit rate skips prefill for those tokens, reducing TTFT and cost per request, which can lower the GPU capacity you need for the same traffic.**Latency Metrics:**TTFT is critical for responsive user experiences. Consider the 99th percentile and intertoken latency metrics as well.**Requests per DAU per Day:**Once you know DAUs, multiply by requests per user to estimate total daily workload.**Contract Length:**Stable, predictable traffic may warrant long-term contracts or on-prem infrastructure. Volatile or experimental workloads benefit from flexible, on-demand (cloud or spot) capacity.

### Implementing a core-and-flex model: De-risk and optimize spend

Don’t let unpredictable workloads drive up costs. Adopt a core-and-flex strategy:

**Core:**Establish a baseline of on-prem or reserved cloud GPU capacity for steady-state workloads. This reduces the risk of price volatility and ensures a reliable service for the bulk of your users.**Flex:**Layer in public cloud elasticity (spot or on-demand GPUs) to handle surges, launches, or experiments. This turns opex into the buffer that allows innovation without overcommitting.

This model strikes a balance between capital efficiency (capex) and operational agility (opex), ensuring you aren’t overprovisioning or stifling growth.

### Don’t forget the practical factors

**Colocation:**If your data is on-prem and your capacity is stable, you might skip this. However, rapid expansion or data residency requirements may necessitate colocation partners for scale-out.**Choosing the Right GPU:**Match the GPU to your workload’s memory footprint, latency targets, and concurrency profile. When capacity runs ahead of what a workload needs, utilization drops and cost per token rises; when it runs behind the workload’s memory or compute demands, throughput and latency are constrained. Right-sizing to the specific model and prompt lengths you run keeps performance and cost aligned.

### Sample scenarios

The following scenarios illustrate how different enterprise workloads can approach GPU sizing and TCO estimation. These examples are intended for demonstration purposes only; actual GPU counts, configurations, and cost outcomes will vary based on model type, workload complexity, concurrency, and performance targets.

**1. Financial services – Copilot for relationship managers**

A local credit union deploys an AI copilot for relationship managers, analyzing complex client emails (long input, short output) to deliver quick, tailored responses and knowledge retrieval. Each copilot session averages 5,000 input tokens and 500 output tokens per query.

**TTFT:**Aim for sub-1 second latency to provide a responsive, seamless user experience in client communication contexts.**Concurrency:**For small- to medium-sized teams, planning for 10-50 concurrent sessions is often sufficient. Burst scaling may be needed during high-traffic periods.**Precision:**For knowledge-intensive and compliance-critical tasks, use high-precision (FP16 or BF16) inference modes to ensure consistent, accurate output.**LLM Model Type:**Medium-sized (7-13B parameters) instruction-tuned models optimized for reasoning, summarization, and retrieval-augmented generation with internal knowledge bases is usually a good fit for tasks requiring nuanced understanding of written communications.**Memory Recommendations:**A GPU with around 24GB of memory is recommended for a smaller 7-8B model, scaling to 48GB for a 13B model to leave headroom for the KV cache at these prompt lengths, while optimizing for multi-user scenarios and fast retrieval.

**2. Life sciences — AI agent for drug discovery**

A pharmaceutical start-up lab uses an AI agent to support scientific research teams, processing full-text research articles (extremely long context) to surface insights and generate result summaries. Queries often involve 20,000 input tokens and 2,000 output tokens.

**TTFT:**Target under 2 seconds given the very large context, balancing responsiveness with the need to process full-text scientific inputs.**Concurrency:**Provision for 20-30 concurrent users to handle collaborative research; consider additional headroom for peaks.**Precision:**High-precision (FP16 or higher) is crucial when processing technical and scientific content to preserve factual accuracy.**LLM Model Type:**Employ long-context models (16K-32K tokens) fine-tuned or adapted through continued pretraining on biomedical literature or domain-specific corpora.**Memory Recommendations:**Opt for very high memory capacity, typically exceeding 80GB per unit, to support ISL/OSL requests, and to ensure stable performance during batch or parallel workflows.

**3. Media and marketing – Real-time content generator**

A mid-size digital marketing agency builds a generative system that creates personalized emails and ad copy from short briefs (500 input, 2,000 output tokens). With campaign launches requiring bursts of increased simultaneous users and a strong need to balance creative output speed and cost efficiency during production cycles.

**TTFT:**Responsive creative generation benefits from TTFT below 1 second for short inputs and medium-length outputs.**Concurrency:**Plan for rapid scaling to support bursty, campaign-driven usage; design for 50-100+ simultaneous users during peak marketing pushes.**Precision:**FP16 precision provides an optimal blend of quality and efficiency for creative copy generation and personalization tasks.**LLM Model Type:**Use general-purpose instruction-tuned or conversational LLMs (3-7B parameters) adapted via lightweight fine-tuning or prompt engineering to follow marketing prompts and stylistic tones.**Memory Recommendations:**16-24GB of memory per GPU typically accommodates advertising prompt sizes and supports efficient batch scheduling at scale.

**4. Technology consulting — Large scale translation platform**

An enterprise IT firm develops a multilingual code and documentation translation tool for client deployments. Each request (1,000 tokens input/output) comes from globally distributed teams.

**TTFT:**Low TTFT (well below 1 second) is vital for a smooth, interactive translation experience, especially in automated workflows.**Concurrency:**For overnight batch activity and global demand surges, size the system to handle hundreds of concurrent requests, and plan for elastic expansion, ideally with auto-scaling.**Precision:**For language and code translation, FP16 or INT8 precision provides sufficient fidelity with high throughput and cost savings.**LLM Model Type:**Medium to large multilingual models (e.g., mixture-of-experts or extended vocabulary architectures), with architectural support for code and domain-specific translation, work best for enterprise-grade platforms.**Memory Recommendations:**Entry-level GPUs (8-16GB of memory) are suitable for handling requests, particularly when orchestrated in a distributed, scalable cloud environment.

## Optimizing models for a better TCO

Optimizing for TCO often comes down to strategically reducing your model’s memory footprint, one of the highest-leverage moves available. A smaller footprint lets you serve on compact or lower-cost GPUs, and in many cases drop an entire GPU tier. There are three levers, roughly in order of engineering effort:

**Quantization:**Reduce numerical precision (FP16 -> FP8/INT8), cutting memory 25-50% with no retraining required.**Pruning:**Remove less critical layers or neurons to shrink parameter count and compute.**Knowledge distillation:**Transfer capability from a large teacher into a smaller, faster student.

None of these are one-time efforts; revisit them as models and workloads evolve. At enterprise scale, the cumulative savings in hardware, power, and operational overhead justify the investment.

## Quantization: The quick win

Models typically ship in 16-bit floating point (FP16/BF16) at two bytes per parameter. Quantization re-expresses the weights, and optionally activations and KV cache, in an 8-bit format (FP8 or INT8) at one byte, roughly halving weight memory. That freed memory lets you drop to a smaller GPU, or fit a larger batch or longer KV cache on the same GPU to raise throughput and lower cost per token.

It’s the “quick win” because it needs no retraining. Post-training quantization (PTQ) converts an already-trained model in place, using only a small set of representative prompts for a calibration pass that sets per-layer scaling factors mapping the FP16 range into 8-bit with minimal distortion.

FP8 is the recommended starting point – typically close to lossless for inference, with more headroom than INT8 or INT4. Accuracy tolerance varies by use case; validate against your workload before production. When PTQ loss exceeds acceptable thresholds, escalate to Quantization-Aware Training (QAT), which fine-tunes with quantization simulated in the forward pass so weights adapt to lower precision. Refer to ModelOpt for more information.

NVIDIA ModelOpt makes PTQ a few lines of code:

`import` `torch` `import` `modelopt.torch.quantization as mtq` `from` `modelopt.torch.export ` `import` `export_hf_checkpoint` `from` `transformers ` `import` `AutoModelForCausalLM, AutoTokenizer` `model ` `=` `AutoModelForCausalLM.from_pretrained(` ` ` `"meta-llama/Llama-3.1-8B-Instruct"` `, dtype` `=` `torch.float16, device_map` `=` `"auto"` `).` `eval` `()` `tokenizer ` `=` `AutoTokenizer.from_pretrained(` `"meta-llama/Llama-3.1-8B-Instruct"` `)` `def` `calibration_loop(model):` ` ` `for` `prompt ` `in` `[` `"Summarize this client email:"` `, ` `"What are the key risks here?"` `]:` ` ` `inputs ` `=` `tokenizer(prompt, return_tensors` `=` `"pt"` `).to(model.device)` ` ` `with torch.no_grad():` ` ` `model(` `*` `*` `inputs)` `model ` `=` `mtq.quantize(model, mtq.FP8_DEFAULT_CFG, forward_loop` `=` `calibration_loop)` `export_hf_checkpoint(model, export_dir` `=` `"./llama-3.1-8b-fp8"` `)` |

As shown in Figure 1, above, FP8 quantization reduces Llama-3.1-8B weight memory from 16.06GB to 9.08GB — a **43.5% reduction** with no retraining. For deeper walkthroughs, see[ Optimizing LLMs for Performance and Accuracy with Post-Training Quantization](https://developer.nvidia.com/blog/optimizing-llms-for-performance-and-accuracy-with-post-training-quantization/),[ Post-Training Quantization of LLMs with NVIDIA NeMo and TensorRT Model Optimizer](https://developer.nvidia.com/blog/post-training-quantization-of-llms-with-nvidia-nemo-and-nvidia-tensorrt-model-optimizer/), and[ Turning FP8 Checkpoints into High-Performance Inference Engines with TensorRT](https://developer.nvidia.com/blog/model-quantization-turn-fp8-checkpoints-into-high-performance-inference-engines-with-nvidia-tensorrt/).

## Pruning and distillation: Going further

When quantization isn’t enough, pruning and distillation enable deeper compression. Pruning removes less critical components, including entire layers (depth pruning) or attention heads, FFN channels, and embedding dimensions (width pruning). Knowledge distillation recovers accuracy by training the pruned student against the original teacher. The one-time compute cost is offset by sustained savings in hardware utilization, power, and operational overhead.

The example below uses NVIDIA NeMo with Qwen3-8B as the teacher, targeting a ~6B student. Convert the Hugging Face model to NeMo checkpoint format and preprocess WikiText-103-v1 first, then prune. The pruning step is where the architecture is actually reshaped – depth pruning trims 36->24 layers, while width pruning shrinks ffn_hidden_size 12288->9216 and hidden_size 4096->3584, both yielding roughly 6B parameters:

Prerequisites: 2x NVIDIA H100 or A100 80GB GPUs, a Docker-enabled environment, and the NeMo container (nvcr.io/nvidia/nemo:25.11, nvidia-modelopt==0.37.0).

### Step: Prune (depth or width)

`NEMO_TEACHER_PATH=` `"./nemo_ckpt/Qwen3-8B.nemo"` `# original (un-pruned) Qwen3-8B .nemo` `# Pruning runs single-GPU — FastNAS asserts tp_size=1 for both depth and width pruning` `PRUNE_COMMON="--devices 1 --tp_size 1 --pp_size 1 \` ` ` `--restore_path ${NEMO_TEACHER_PATH} --legacy_ckpt \` ` ` `--seq_length ${SEQ_LENGTH} --num_train_samples ${NUM_TRAIN_SAMPLES} --mbs ${MICRO_BATCH_SIZE} \` ` ` `--data_paths ${DATA_PATHS} --index_mapping_dir ${INDEX_MAPPING_DIR}"` `PRUNE=` `"torchrun --nproc_per_node 1 ${NEMO_ROOT}/scripts/llm/gpt_prune.py"` `# Step 1a — Depth pruning: 36 → 24 layers (~6B model)` `${PRUNE} ${PRUNE_COMMON} --save_path ${ROOT_DIR}` `/Qwen3-8B-nemo-depth-pruned` `\` ` ` `--target_num_layers 24` `# Step 1b — Width pruning: ffn_hidden_size 12288→9216, hidden_size 4096→3584` `${PRUNE} ${PRUNE_COMMON} --save_path ${ROOT_DIR}` `/Qwen3-8B-nemo-width-pruned` `\` ` ` `--target_ffn_hidden_size 9216 --target_hidden_size 3584` `#Step 2 — Distillation: train each pruned student against the teacher` `TRAIN=` `"torchrun --nproc_per_node ${DEVICES} ${NEMO_ROOT}/scripts/llm/gpt_train.py"` `# Step 2a — Depth-pruned student` `${TRAIN} \` ` ` `--name depth_distill --model_path ${ROOT_DIR}` `/Qwen3-8B-nemo-depth-pruned` `\` ` ` `--teacher_path ${NEMO_TEACHER_PATH} --log_dir ${ROOT_DIR}` `/depth_distill_logs` `--legacy_ckpt \` ` ` `--data_paths ${DATA_PATHS} --index_mapping_dir ${INDEX_MAPPING_DIR} --seq_length ${SEQ_LENGTH} \` ` ` `--max_steps ${MAX_STEPS} --gbs ${GLOBAL_BATCH_SIZE} --mbs ${MICRO_BATCH_SIZE} \` ` ` `--val_check_interval ${VAL_CHECK_INTERVAL} --precision bf16-mixed` `# Step 2b — Width-pruned student (same as above, swap the two lines below)` `# --name width_distill --model_path ${ROOT_DIR}/Qwen3-8B-nemo-width-pruned` |

Note: For demonstrative purposes, the dataset used here is comparatively small, so these numbers should be treated as illustrative rather than definitive. As Figure 2 shows, above, in this run width pruning reached a lower final validation loss (3.21 vs 3.60), while depth pruning converged faster. For scale reference, the NVIDIA published run produces a 6B depth-pruned model that is 30% faster than Qwen3-4B at higher MMLU accuracy (72.5 vs 70.0).

For the full pipeline, end-to-end documentation, and architectural recommendations, see[ LLM Model Pruning and Knowledge Distillation with NVIDIA NeMo Framework](https://developer.nvidia.com/blog/llm-model-pruning-and-knowledge-distillation-with-nvidia-nemo-framework/),[ Pruning and Distilling LLMs Using NVIDIA TensorRT Model Optimizer](https://developer.nvidia.com/blog/pruning-and-distilling-llms-using-nvidia-tensorrt-model-optimizer/), and the[ Llama-3.1-to-Minitron blog](https://developer.nvidia.com/blog/how-to-prune-and-distill-llama-3-1-8b-to-an-nvidia-llama-3-1-minitron-4b-model/).

## Where to go next

GPU sizing is an ongoing optimization, not a fixed choice made at deployment. Quantization, pruning, and distillation give teams concrete levers to cut infrastructure cost without sacrificing performance. Start with quantization for an immediate footprint reduction, layer in pruning and distillation as workloads mature, and revisit as models evolve – producing smaller, faster models that expand AI’s reach across mobile, edge, and embedded applications.

To get started with model optimization, check out the NVIDIA Model Optimizer [GitHub](https://github.com/NVIDIA/Model-Optimizer) and [Hugging Face](https://huggingface.co/docs/diffusers/en/quantization/modelopt) with a deeper dive into [model quantization](https://developer.nvidia.com/blog/model-quantization-post-training-quantization-using-nvidia-model-optimizer/) on how to post-train quantization with Model Optimizer.

## Start the discussion at forums.developer.nvidia.com
