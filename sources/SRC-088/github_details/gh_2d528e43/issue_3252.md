# [Issue #3252] [Bug] Auto batch size detection in `generate_ until` is overly conservative

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3252
state: open | updated: 2026-09-23T23:22:27Z
labels: 

## 正文

### Describe the bug

When using `batch_size="auto"` with the `generate_until` function, the automatic batch size detection mechanism is overly conservative and often results in a batch size of 1. This significantly hinders performance and negates the benefit of the auto-sizing feature.

The root cause is that when `generate_until` calls `_detect_batch_size`, it doesn't pass any information about the actual lengths of the input requests.

As a result, `_detect_batch_size` falls back to using the model's maximum possible sequence length (`self.max_length`) to create its test tensor for estimating the batch size.

This means that even if all actual input prompts are short, the batch size is determined based on the worst-case scenario of a full-context input, which almost always leads to `batch_size=1` on modern GPUs with large models. This behavior is different from how `loglikelihood` functions use `_detect_batch_size`, where they pass request-specific information.

### To Reproduce

1.  Use a large language model.
2.  Run an evaluation that uses the `generate_until` method.
3.  Set the batch size argument to `auto`, for example: `--batch_size auto`.
4.  Observe the log output, which will show:
    ```
    Passed argument batch_size = auto. Detecting largest batch size
    Determined Largest batch size: 1
    ```

### Expected behavior

The `auto` batch size mechanism should detect a batch size larger than 1 by considering the actual input lengths and the `max_gen_toks` parameter, leading to faster evaluations. The estimated sequence length should be more realistic.

### Suggested Solution

A more accurate estimation can be achieved by calculating the expected maximum sequence length within `generate_until` and passing it to `_detect_batch_size`.

1.  **Modify `_detect_batch_size`** to accept an optional `max_length` argument. If provided, this length is used for the test tensor instead of `self.max_length`.

    ```python
    def _detect_batch_size(self, requests: Sequence | None = None, pos: int = 0, max_length: int | None = None):
        if max_length is not None:
            # Use the provided max_length
            ...
        elif requests:
            # Current logic for loglikelihood
            ...
        else:
            # Fallback to self.max_length
            max_length = self.max_length
            ...
    ```

2.  **Update `generate_until`** to calculate this `max_length` before calling `_detect_batch_size`. The logic would be:
    *   Find the maximum token length of all input contexts in the `requests` list.
    *   Get `max_gen_toks` from the generation arguments.
    *   Calculate `estimated_max_length = max_input_length + max_gen_toks`.
    *   Call `_detect_batch_size(max_length=estimated_max_length)`.

This approach would provide a much more realistic sequence length for batch size estimation, unlocking the performance benefits of the `auto` batch size feature for generation tasks.

Thank you for considering this improvement!

## 评论 (3)

### akashe · 2025-09-30

I have had the same experience. The auto batch size detection is way too conservative. I was earlier using 16GB VRAM where it detected auto batch size as 1 for gsm8k task. With batch size 1 it used around 7GB VRAM to evaluate a finetuned "Qwen/Qwen2.5-3B" model. I switched to 48GB VRAM and still the auto batch size was detected as 1!

### fxmarty-amd · 2025-10-15

+100

### Anassbzdd · 2026-09-23

Hi, I’d be happy to work on this. Is anyone already working on it, or can I submit a PR?
