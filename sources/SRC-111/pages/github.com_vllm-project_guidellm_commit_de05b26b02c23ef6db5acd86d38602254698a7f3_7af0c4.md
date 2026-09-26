source: https://github.com/vllm-project/guidellm/commit/de05b26b02c23ef6db5acd86d38602254698a7f3

|
| `1` | `+`# Benchmarking Different Workload Shapes |
| `2` | `+` |
| `3` | `+`Not all LLM workloads are the same. A chatbot, a summarization pipeline, and a code generator stress your server in completely different ways. This guide shows how to configure GuideLLM for each specific workload type and explains why metrics behave differently. |
| `4` | `+` |
| `5` | `+`## Prerequisites |
| `6` | `+` |
| `7` | `+`- A running OpenAI-compatible server ([setup guide](../getting-started/server.md)) |
| `8` | `+`- GuideLLM installed ([install guide](../getting-started/install.md)) |
| `9` | `+` |
| `10` | `+`## Why Workload Shape Matters |
| `11` | `+` |
| `12` | `+`LLM requests have two phases: |
| `13` | `+` |
| `14` | `+`- **Prefill**: the server processes all input tokens at once. This determines time-to-first-token (TTFT). |
| `15` | `+`- **Decode**: the server generates output tokens one at a time. This determines inter-token latency (ITL) and overall throughput. |
| `16` | `+` |
| `17` | `+`The ratio of input to output tokens shifts which phase dominates. A workload with long prompts and short responses is prefill-bound. A workload with short prompts and long responses is decode-bound. Each has different bottlenecks and different metrics to watch. |
| `18` | `+` |
| `19` | `+`## The Four Common Shapes |
| `20` | `+` |
| `21` | `+`### 1. Chat / Conversational |
| `22` | `+` |
| `23` | `+`A user sends a short message and expects a medium-length response **(decode-bound)**. Typical of chatbots, customer support, and Q&A interfaces. |
| `24` | `+` |
| `25` | `+````bash |
| `26` | `+`guidellm run \ |
| `27` | `+` --backend kind=openai_http,target=http://localhost:8000 \ |
| `28` | `+` --data kind=synthetic_text,prompt_tokens=256,output_tokens=512 \ |
| `29` | `+` --profile kind=sweep,sweep_size=10 \ |
| `30` | `+` --constraint kind=max_duration,seconds=120 \ |
| `31` | `+` --seed kind=static,value=42 \ |
| `32` | `+` --output kind=json,path=chat_workload.json |
| `33` | `+```` |
| `34` | `+` |
| `35` | `+`**What to watch:** Both TTFT and ITL matter. Users are waiting for the response to start streaming (TTFT) and then reading it as it arrives (ITL). If either is too slow, the experience feels laggy. |
| `36` | `+` |
| `37` | `+`### 2. Summarization / RAG |
| `38` | `+` |
| `39` | `+`A retrieval-augmented generation pipeline stuffs a large context into the prompt and expects a concise answer. Long input, short output. **(prefill-bound)** |
| `40` | `+` |
| `41` | `+````bash |
| `42` | `+`guidellm run \ |
| `43` | `+` --backend kind=openai_http,target=http://localhost:8000 \ |
| `44` | `+` --data kind=synthetic_text,prompt_tokens=2048,output_tokens=128 \ |
| `45` | `+` --profile kind=sweep,sweep_size=10 \ |
| `46` | `+` --constraint kind=max_duration,seconds=120 \ |
| `47` | `+` --seed kind=static,value=42 \ |
| `48` | `+` --output kind=json,path=summarization_workload.json |
| `49` | `+```` |
| `50` | `+` |
| `51` | `+`**What to watch:** TTFT dominates. The server spends most of its time processing the long prompt before generating a short answer. ITL matters less because there are so few output tokens. Throughput (tokens/sec) will look lower than chat because prefill is the bottleneck. |
| `52` | `+` |
| `53` | `+`### 3. Code Generation |
| `54` | `+` |
| `55` | `+`A developer gives a short instruction and expects a long block of generated code. Short input, long output. **(prefill-bound)** |
| `56` | `+` |
| `57` | `+````bash |
| `58` | `+`guidellm run \ |
| `59` | `+` --backend kind=openai_http,target=http://localhost:8000 \ |
| `60` | `+` --data kind=synthetic_text,prompt_tokens=128,output_tokens=1024 \ |
| `61` | `+` --profile kind=sweep,sweep_size=10 \ |
| `62` | `+` --constraint kind=max_duration,seconds=120 \ |
| `63` | `+` --seed kind=static,value=42 \ |
| `64` | `+` --output kind=json,path=codegen_workload.json |
| `65` | `+```` |
| `66` | `+` |
| `67` | `+`**What to watch:** ITL dominates. TTFT will be fast (short prompt to prefill), but the server spends most of its time decoding a long output. High ITL means the code takes forever to stream in. Throughput (tokens/sec) is the key metric here. |
| `68` | `+` |
| `69` | `+`### 4. Balanced / General Purpose |
| `70` | `+` |
| `71` | `+`Equal input and output lengths **(balanced)**. A good starting point when you are not sure what your workload looks like, or when you want a general performance baseline. |
| `72` | `+` |
| `73` | `+````bash |
| `74` | `+`guidellm run \ |
| `75` | `+` --backend kind=openai_http,target=http://localhost:8000 \ |
| `76` | `+` --data kind=synthetic_text,prompt_tokens=1000,output_tokens=1000 \ |
| `77` | `+` --profile kind=sweep,sweep_size=10 \ |
| `78` | `+` --constraint kind=max_duration,seconds=120 \ |
| `79` | `+` --seed kind=static,value=42 \ |
| `80` | `+` --output kind=json,path=balanced_workload.json |
| `81` | `+```` |
| `82` | `+` |
| `83` | `+`**What to watch:** Both phases contribute roughly equally. This gives the most balanced view of your server's capabilities but may not reflect your actual production workload. |
| `84` | `+` |
| `85` | `+`## Comparing Results Across Shapes |
| `86` | `+` |
| `87` | `+`Run all four shapes on the same server and compare the results side by side. |
| `88` | `+` |
| `89` | `+`| Workload | Tokens (in/out) | Throughput (tok/s) | TTFT p50 (ms) | ITL p50 (ms) | Bottleneck | |
| `90` | `+`|----------|-----------------|-------------------|---------------|-------------|------------| |
| `91` | `+`| Chat | 256 / 512 | 1850 | 35 | 12 | Mixed | |
| `92` | `+`| Summarization | 2048 / 128 | 920 | 180 | 9 | Prefill (TTFT) | |
| `93` | `+`| Code gen | 128 / 1024 | 2100 | 18 | 14 | Decode (ITL) | |
| `94` | `+`| Balanced | 1000 / 1000 | 1350 | 95 | 13 | Mixed | |
| `95` | `+` |
| `96` | `+`Key observations: |
| `97` | `+` |
| `98` | `+`- **Summarization has the highest TTFT** because the server processes 2048 input tokens before generating the first output token **(prefill-bound)**. But ITL is the lowest because there are very few tokens to decode. |
| `99` | `+`- **Code gen has the highest throughput** because the short prompt prefills quickly, and the server spends most of its time in the efficient decode phase. But requests take the longest end-to-end because of 1024 output tokens. |
| `100` | `+`- **Chat is the most balanced** — neither phase dominates, so both TTFT and ITL need to be within SLO. |
| `101` | `+`- **Throughput numbers are not directly comparable** across shapes because total tokens per request differ. Use `output_tokens_per_second` for an apples-to-apples decode throughput comparison. |
| `102` | `+` |
| `103` | `+`## Choosing Your Benchmark Configuration |
| `104` | `+` |
| `105` | `+`If you know your workload: |
| `106` | `+` |
| `107` | `+`| Your application | Recommended config | Primary metric | |
| `108` | `+`|-----------------|-------------------|----------------| |
| `109` | `+`| Chatbot, Q&A | `prompt_tokens=256,output_tokens=512` | TTFT p99 and ITL p50 | |
| `110` | `+`| RAG, summarization, search | `prompt_tokens=2048,output_tokens=128` | TTFT p99 | |
| `111` | `+`| Code gen, writing, translation | `prompt_tokens=128,output_tokens=1024` | ITL p50 and throughput | |
| `112` | `+`| Unknown or mixed | `prompt_tokens=1000,output_tokens=1000` | All metrics | |
| `113` | `+` |
| `114` | `+`If you have real production data, use it instead of synthetic. GuideLLM supports custom datasets via JSONL files or HuggingFace datasets — see the [Datasets guide](../guides/datasets.md) for details. |
| `115` | `+` |
| `116` | `+`## Tuning Your Server for a Workload Shape |
| `117` | `+` |
| `118` | `+`The benchmark results can guide server configuration: |
| `119` | `+` |
| `120` | `+`**Prefill-bound (high TTFT):** |
| `121` | `+`- Enable chunked prefill (`--enable-chunked-prefill`) to overlap prefill with decode |
| `122` | `+`- Increase tensor parallelism to spread the prefill computation across GPUs |
| `123` | `+`- Consider a shorter `--max-model-len` if your prompts don't need the full context window |
| `124` | `+` |
| `125` | `+`**Decode-bound (high ITL):** |
| `126` | `+`- Check if you are memory-bandwidth limited — larger batch sizes help divide memory reads |
| `127` | `+`- Try quantized models (FP8, W4A16) to reduce memory bandwidth pressure |
| `128` | `+`- Consider speculative decoding for latency-sensitive workloads |
| `129` | `+` |
| `130` | `+`## Next Steps |
| `131` | `+` |
| `132` | `+`- [Finding Your Server's Optimal Concurrency Limit](optimal_concurrency.md) to optimize the load level for your chosen workload shape |
## 0 commit comments