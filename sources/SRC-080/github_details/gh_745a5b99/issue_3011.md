# [Issue #3011] Untruncated text calibration produces a misleading 16 GiB CUDA OOM in mask expansion; warn or guard when max_seq_length is unset

source: https://github.com/vllm-project/llm-compressor/issues/3011
state: closed | updated: 2026-08-31T16:05:14Z
labels: 

## 正文

### ⚙️ Your current environment

- llmcompressor 0.12.1.dev100+g170a2e19 (traceback below); the same 16.00 GiB OOM also killed earlier runs on released 0.12.0.1 (both `pipeline="basic"` and CPU-offload variants)
- transformers 5.10.1, torch 2.11.0+cu130
- 1x RTX 5090 32 GB (sm_120), driver 580.173.02, Ubuntu 24.04
- Dataset: `HuggingFaceH4/ultrachat_200k` train_sft, 128 samples, rendered through the model chat template. Longest sample 3,994 tokens; only 10 of 128 exceed 2,048.

### 🐛 Describe the bug

Calling `oneshot()` with a text dataset and no `max_seq_length` reliably OOMs a 32 GB card during calibration of Qwen3-8B, with the allocation landing in transformers' attention-mask expansion:

```
File ".../transformers/masking_utils.py", line 52, in and_mask
    result = result & mask(batch_idx, head_idx, q_idx, kv_idx).to(result.device)
torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 16.00 GiB.
```

Setting `max_seq_length=2048` and changing nothing else makes the identical run complete with headroom. We have not pinned down which broadcast produces the 16.00 GiB request (calibration `batch_size` defaults to 1, so it is not simple cross-sample padding); full logs available on request.

What makes this worth an issue is how misleading the failure is. The error points at GPU capacity, not sample length, so the natural responses are `pipeline="basic"`, CPU offload via device_map, or concluding the model does not fit the card. None of them help, and each failed attempt costs a full calibration cycle. It took us several such cycles to find the actual cause.

Related but distinct prior work: #2649 fixed truncation for pre-tokenized datasets, and #2917 fixed truncation state leaking into the saved tokenizer. This report is about the untruncated-text path and the quality of the failure when it bites.

Proposal, any of which would have saved the debugging time:

1. Log a prominent warning when tokenizing calibration text with no `max_seq_length` set, including the longest sample length found.
2. Or apply a documented default truncation for text datasets (matching what most recipes in `examples/` opt into).
3. Or catch OOM during calibration and re-raise with a hint naming `max_seq_length` when long samples are present.

Happy to submit a small PR for option 1, or whichever direction maintainers prefer.

### 🛠️ Steps to reproduce

```python
from datasets import load_dataset
from transformers import AutoTokenizer
from llmcompressor import oneshot
from llmcompressor.modifiers.quantization import QuantizationModifier

MODEL = "Qwen/Qwen3-8B"
tok = AutoTokenizer.from_pretrained(MODEL)
ds = load_dataset("HuggingFaceH4/ultrachat_200k", split="train_sft") \
    .shuffle(seed=3407).select(range(128))
ds = ds.map(lambda ex: {"text": tok.apply_chat_template(ex["messages"], tokenize=False)},
            remove_columns=ds.column_names)
recipe = QuantizationModifier(targets="Linear", scheme="NVFP4", ignore=["lm_head"])
oneshot(model=MODEL, dataset=ds, recipe=recipe,
        num_calibration_samples=128, output_dir="out-nvfp4")   # no max_seq_length -> OOM on 32 GB
```

Add `max_seq_length=2048` to the `oneshot()` call and it completes.

Hit while producing the quantization benchmark at https://github.com/Rodder5/sm120-quant-bench.


## 评论 (7)

### Rodder5 · 2026-08-08

Additional data point that tightens the repro and adds a version-specific wrinkle.

Re-running the same script with only **8 calibration samples** (batch_size default 1) on the released combo `llmcompressor==0.12.0.1` + `compressed-tensors==0.17.0` produces the identical **16.00 GiB** allocation, failing during calibration of the first decoder layer at `create_causal_mask` inside the autowrapped subgraph:

```
>         causal_mask_mapping = {'full_attention': create_causal_mask(**mask_kwargs)}
CUDA out of memory. Tried to allocate 16.00 GiB.
```

Two implications. First, the allocation is invariant to sample count (128 vs 8 samples, same 16.00 GiB), which should narrow down which broadcast produces it. Second, on 0.12.0.1 the failure is even harder to diagnose than reported above: `append_autowrap_source_on_fail` (pipelines/sequential/ast_helpers.py) re-raises it as a `RuntimeError` headlined by the autowrapped source dump, so the user-visible error begins with generated code rather than "CUDA out of memory". On current main the same configuration surfaces the OOM directly from transformers' `masking_utils`.

Same environment as the original report otherwise; `max_seq_length=2048` still resolves it in both versions.

### brian-dellabetta · 2026-08-10

Hi @Rodder5 , this sounds like expected behavior to me? If you pass in a dataset without setting max_seq_length, it will use the calibration set exactly as it's passed in. If a given sample has a very large sequence length, it will OOM elsewhere in the pipeline when activations are cached in modifiers etc. You can either set `max_seq_length` or truncate the dataset ahead of time.

### Rodder5 · 2026-08-10

Thanks @brian-dellabetta, agreed it is expected behavior mechanically, and truncating is exactly the fix we landed on. The report is about the diagnosability of the failure rather than its existence.

What makes it expensive in practice: the OOM points at GPU capacity, so the natural responses are pipeline="basic", CPU offload via device_map, or concluding the model does not fit the card, and none of them move the error (the allocation is per-sample activations). On the released 0.12.0.1 it is harder still: the autowrap error handler re-raises the OOM under a dump of generated source, so the first thing the user reads is autowrapped code rather than "CUDA out of memory" (trace in my second comment). Each wrong guess costs a full calibration cycle; it took us several to find the cause, and nothing in the failure names `max_seq_length`.

The minimal version of what I am proposing: a one-line `logger.warning` at calibration tokenization when `max_seq_length` is unset and a sample exceeds some threshold, reporting the longest tokenized sample length. No behavior change, just a signpost at the moment the footgun is armed. Would a small PR along those lines be acceptable? Happy to keep it to whatever shape you prefer, or close this if you consider the current behavior sufficiently documented.

### brian-dellabetta · 2026-08-11

Hi @Rodder5 , in an effort to reduce the number of warnings, what do you think about just updating the OOM error to include a smaller calibration dataset? Would this update reduce confusion/friction?

* #3020

### Rodder5 · 2026-08-11

Yes, this would have saved us most of the debugging time, and I think the error-site message is the right call over a warning, no noise for anyone who doesn't hit it. Two small thoughts from the data in this thread: the allocation was invariant to sample count in our repro (8 vs 128 samples, identical 16.00 GiB), so max_seq_length is usually the lever, might be worth naming it first. And our original failure surfaced under pipeline="basic" as well, does that path share this message? Either way, happy with this as the resolution. Thanks for picking it up.

### brian-dellabetta · 2026-08-11

Hi @Rodder5 , although your error was a result of sequence length, a high num_calibration_samples can likewise cause OOMs in GPTQ, AWQ, or QuantizationModifier because activations are cached as part of the modifier life cycle or, at the very least, between sequential targets.

`pipeline="basic"` really should never be run outside of data-free flows. It will always be more memory-intensive than sequential, the models we target are all very sequential. Did you see it suggested somewhere?

### Rodder5 · 2026-08-11

Fair point on num_calibration_samples, my invariance result was specific to the mask broadcast, and activation caching across the modifier lifecycle is a different budget. On pipeline="basic": no, nothing suggested it, that was my own wrong turn, and your question made me re-read the original log to answer it properly. What I found is embarrassing in a useful way: the "tracer failure" that sent me to basic in the first place was this same OOM, printed beneath the autowrapped source dump, and I misread the wrapped input-guard source as a raised ValueError. So there was one bug presenting as three, and every wrong turn I took traces back to the error presentation at exactly the site your PR improves. Consider this the strongest field evidence for #3020 I can offer.

