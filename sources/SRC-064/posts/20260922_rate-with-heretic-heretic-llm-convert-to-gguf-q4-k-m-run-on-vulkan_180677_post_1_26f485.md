# Build an uncensored/abliterated Greek-native LLM for local use. Best candidate: ilsp/Llama-Krikri-8B-Instruct (Llama 3.1 8B Greek fine-tune). Plan: abliterate with Heretic (heretic-llm), convert to GGUF Q4_K_M, run on Vulkan

source: https://discuss.huggingface.co/t/build-an-uncensored-abliterated-greek-native-llm-for-local-use-best-candidate-ilsp-llama-krikri-8b-instruct-llama-3-1-8b-greek-fine-tune-plan-abliterate-with-heretic-heretic-llm-convert-to-gguf-q4-k-m-run-on-vulkan/180677#post_1
published: Tue, 22 Sep 2026 02:48:37 +0000

Hey everyone,

Setup: GMKtec EVO-X3, AMD Ryzen AI MAX+ 395 (Strix Halo), Radeon 8060S, 117.55 GiB unified memory, Ubuntu 24.04, Vulkan/RADV, llama.cpp built with GGML_VULKAN=ON. Running Qwen3-32B-heretic-Q8_0 on llama-server (127.0.0.1:8081).

Goal: build an uncensored/abliterated Greek-native LLM for local use. Best candidate: ilsp/Llama-Krikri-8B-Instruct (Llama 3.1 8B Greek fine-tune). Plan: abliterate with Heretic (heretic-llm), convert to GGUF Q4_K_M, run on Vulkan.

Questions:

- Has anyone abliterated Llama-Krikri-8B or any Greek fine-tune? Does Heretic support it?
- Best workflow: abliterate safetensors then convert to GGUF, or use abliterate.cpp on GGUF? Any pitfalls?
- Best quantization for Greek on Strix Halo: Q4_K_M, Q5_K_M, Q6_K? Need quality/speed balance.
- Recommended llama.cpp Vulkan flags for Strix Halo: -ngl 99, -c 32768, flash attention, q8_0 KV cache, speculative decoding? Any known issues?
- Any existing uncensored Greek models I missed (Krikri, Meltemi, Sophea, etc.)?

Thanks!

Good news on candidate choice, Krikri is already the strongest open Greek pick, ILSP’s own benchmarks show it beating Meltemi-7B by +11.6% average on Greek tasks and outperforming plain Llama-3.1-8B by +10.8%, so you’re not leaving anything on the table there. No public Sophea Greek model turned up, and nothing indicates anyone’s abliterated Krikri specifically yet, you’d likely be first.

-
Heretic operates on activation directions at the architecture level (standard Llama structure), it doesn’t need language-specific support, it’s already been run successfully on other Llama/Qwen/Gemma/Mistral fine-tunes regardless of target language, so Krikri being a Llama-3.1 fine-tune should work fine. Only real risk: since Krikri went through DPO alignment specifically including “manually created data targeting Greek-specific safety concerns,” the refusal direction might be more diffuse/entangled with Greek-language safety training than a stock English-only model, worth running Heretic’s own eval harness on Greek-language refusal prompts specifically rather than just the default English marker suite, or you might get a checkpoint that looks abliterated on English but still refuses in Greek.

-
Abliterate the safetensors first, then GGUF convert, not the other way. Heretic operates on the model’s actual weight tensors/activation space, GGUF is a post-quantization serialization format, doing it in reverse means operating on already-quantized, format-mangled tensors, current abliterate.cpp-style GGUF-native tools exist but are less mature/tested than doing it on full-precision safetensors first.

-
For an 8B model with 117GB unified memory, Q6_K or even Q8_0 costs you almost nothing memory-wise and Greek (non-Latin-heavy tokenization, more fragile to precision loss than English) benefits more from higher quant than a model that’s already comfortable in English. Q4_K_M is really for VRAM-constrained setups, you’re not, so go Q6_K minimum, Q8_0 if you want to be safe against any Greek-specific degradation.

-
Solid baseline flags for gfx1151: `-ngl 99 -fa on -ctk q8_0 -ctv q8_0 -c 32768 -b 2048 -ub 256`

. Speculative decoding (`--spec-type draft-mtp`

) is worth adding if you can find/pair a draft model in Krikri’s format, reported +79% gains on Strix Halo in recent community benchmarks. Known pitfall: avoid `--mlock`

on Strix Halo, it pins weights in system RAM and blocks GPU upload, and skip `--fit`

, reported free VRAM is a constant on this platform so it sizes against fiction rather than real available memory.