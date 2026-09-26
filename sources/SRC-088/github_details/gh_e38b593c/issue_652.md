# [Issue #652] [RFC]: Use vLLM Render Endpoint in preprocessing for Tokenization Alignment

source: https://github.com/vllm-project/speculators/issues/652
state: open | updated: 2026-06-27T16:51:09Z
labels: RFC

## 正文

### Motivation.
Speculators preprocesses training data by applying chat templates and tokenizing with HuggingFace's AutoProcessor/AutoTokenizer, then sends the resulting token IDs to vLLM's Completions API for hidden-state extraction. This assumes the HF tokenizer and vLLM's internal preprocessing produce identical token sequences for the same conversation. They sometimes don't, and the divergence occurs at two distinct layers. Tokenizer-level divergence. vLLM maintains a tokenizer registry (vllm/tokenizers/registry.py) with custom tokenizer backends that replace AutoTokenizer entirely when tokenizer_mode="auto". When vLLM auto-detects one of these models, it loads the custom tokenizer instead of HF's. Preprocessing-level divergence. Even when the underlying tokenizer is the same (e.g., gpt-oss uses HF's tokenizer for raw text encoding), vLLM applies additional conversation-level preprocessing that apply_chat_template() does not replicate. For gpt-oss specifically, vLLM uses Harmony's Rust encoder (openai_harmony.load_harmony_encoding) to render conversations into token sequences via `render_for_completion()`, which injects system preambles, formats tool descriptions, and structures messages in a way that is different from the Jinja2 chat template. vLLM also applies tool parsers and reasoning parsers that further transform the token sequence.

**Two code paths for text-only vs. multimodal.** Speculators currently maintains two separate data flows depending on content type. Text-only data is tokenized locally with HF and sent as pre-tokenized input_ids to the Completions API. Multimodal data sends raw messages to the Chat Completions API, letting vLLM handle tokenization, because the Completions API cannot carry image/video/audio references. This split creates its own problems: the text-only path is vulnerable to the tokenizer divergence described above, while the multimodal path relies on vLLM and HF inserting placeholder tokens at the same positions to keep the locally-built loss mask aligned.  A single path that delegates all tokenization to vLLM would eliminate this branching and make our preprocessing step more maintainable.

### Proposed Change.

Skip the local preprocessing step entirely and use a single vLLM instance for both tokenization and hidden-state extraction. The vLLM server already tokenizes inputs through its full preprocessing pipeline (chat template rendering, Harmony encoding, tool/reasoning parsing) before running the model. Speculators should send raw conversations to the Chat Completions API and let vLLM handle all tokenization, rather than tokenizing locally with HF and sending pre-tokenized IDs to the Completions API. This eliminates the tokenizer divergence problem and simplify the training process. Requests must forward chat_template_kwargs (e.g., enable_thinking for Gemma 4) so the rendered token sequence matches what vLLM produces at inference time with the same settings. Currently, preprocessing truncates input_ids to seq_length before sending to vLLM. With raw messages, truncation must happen at the conversation level (dropping early turns) or via max_model_len on the vLLM server side, since the Completions API pre-truncated path is no longer used.

### Open Questions
- How to efficiently return loss masks from the hidden-state extraction endpoint without a second pass
- Currently speculators truncates input_ids to seq_length locally before sending them to vLLM. If we switch to sending raw messages and letting vLLM tokenize, we lose that truncation point. We need a strategy for enforcing length limits when speculators no longer owns the tokenization step.

## 评论 (7)

### shanjiaz · 2026-06-24

@WindChimeRan is working on this.

### WindChimeRan · 2026-06-24

Hi @shanjiaz . I investigated the core claim. For shipping models, this is largely a non-issue.

**What I found:**

- Standard HF models: vLLM render calls the same `tokenizer.apply_chat_template` we call ([`vllm/renderers/hf.py:740`](https://github.com/vllm-project/vllm/blob/main/vllm/renderers/hf.py#L740)). Byte-identical across all cases including tools and multimodal.
- gpt-oss does NOT bypass `apply_chat_template`. It ships an HF chat template that emits Harmony and matches vLLM to the token (74==74, see the repro script in my branch, linked below) when date/effort are aligned.
- The text path sends `prompt=token_ids` verbatim ([`vllm_client.py:190-196`](https://github.com/vllm-project/speculators/blob/main/src/speculators/data_generation/vllm_client.py#L190-L196)) — no re-tokenization happens. The multimodal path pins `add_generation_prompt=False` ([`:203`](https://github.com/vllm-project/speculators/blob/main/src/speculators/data_generation/vllm_client.py#L203)). Both hard-assert token equality (`:106`) — a mismatch crashes, doesn't silently degrade.

**The one real divergence** is gpt-oss specific: vLLM injects a serving-time `Current date:` and `Reasoning:` effort into the preamble ([`harmony_utils.py:get_system_message`](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/parser/harmony_utils.py#L103-L138), with the literal comment "This brings non-determinism in vLLM"). But `apply_chat_template(reasoning_effort=..., strftime_now=...)` reproduces the served tokens exactly — it's a plumbing gap, not an encoder mismatch.

**Simpler fix if/when gpt-oss drafting ships:** add `--reasoning-effort` / `--serving-date` to `prepare_data.py` (~20 lines, one repo). No render endpoint, no subprocess lifecycle, no upstream vLLM changes needed.

Reproduction script + test: [branch](https://github.com/vllm-project/speculators/compare/main...WindChimeRan:speculators:652-render-tokenization-alignment) (`scripts/verify_tokenization_alignment.py`).

Happy to discuss.

### shanjiaz · 2026-06-25

@WindChimeRan Revised the RFC and discussed offline. Let us know what you think! Thanks.

### WindChimeRan · 2026-06-26

**Tracker**:

* [Speculator] PR 1: #665, blocked by PR 2
* [vLLM] PR 2: https://github.com/vllm-project/vllm/pull/46846

**Design tradeoff:**
* For models whose templates lack `{% generation %}` tags (e.g. Qwen3, gpt-oss), the assistant-mask fallback (regex-based span detection) stays in speculators — it's training-specific logic that doesn't belong in vLLM's general-purpose render endpoint. PR 2 returns `null` for `loss_mask` when the template doesn't support it; speculators handles the rest.

**Duplicate work check on vllm loss mask**

* OpenRLHF — tracks `action_ranges` from prompt length boundaries, fills a zeros tensor with 1s at response positions
* veRL — uses `get_eos_mask` to mark tokens valid up to EOS
* TRL — builds `completion_mask = torch.ones_like(completion_ids)` for all completion tokens

These RL frameworks have it easier than speculators though — they generate the completions themselves, so they know exactly where the prompt ends and the response begins. They don't need `{% generation %}` template tracking. Speculators is the harder case because it tokenizes existing multi-turn conversations where assistant spans are interleaved.

**Out-of-scope**: Future work, out of scope but might be the right thing to do in the future:

* Long-term, the vLLM Rust frontend's `ChatRenderer` (minijinja) should be the single rendering implementation backing both serving and the render endpoint, with `{% generation %}` span tracking for native assistant-mask support — eliminating the current Python/Rust dual-stack.

### shanjiaz · 2026-06-27

@WindChimeRan Thanks for the update, I think instead of having two separate vLLM instances for pre-processing and hidden states extraction, we would prefer having the same instance for both. (For online and offline) I'm not sure the PR on speculators side address that gap and I don't think it's out of the scope of this issue. Let me know what you think!

### WindChimeRan · 2026-06-27

@shanjiaz The code is fine. It's just a doc clarity issue. I've updated the PR description and the `--help` doc. 

In a nutshell, if you point `--render-endpoint` to the same url, then it's single instance. if you point it to two different url (and launch a separated renderer server), then it's two instance. 

Will make a followup PR to #655 to make sure claude agent follows the best practice in both online & offline training scenario. 

### shanjiaz · 2026-06-27

Sounds good! Will take a look and try it out. 

