# [Issue #3482] [Bug] Multi-turn chat with Qwen3-0.6B truncates output during thinking phase

source: https://github.com/mlc-ai/mlc-llm/issues/3482
state: closed | updated: 2026-04-20T14:59:10Z
labels: bug

## 正文

Love the project — great work! 🎉 I ran into a fun little bug while playing with multi-turn chat and thought I'd share.

### Environment

- OS: macOS (Apple Silicon, osx-arm64)
- Python: 3.12.12
- mlc-llm-nightly-cpu: 0.20.dev159
- mlc-ai-nightly-cpu: 0.20.dev912

### Model

- `Qwen3-0.6B-q4f16_1-MLC`
- `Qwen3-0.6B-q0f16-MLC` (also affected)
- `Qwen3-1.7B-q4f16_1-MLC` (NOT affected)

### Description

When using `MLCEngine` for multi-turn chat with Qwen3-0.6B models (both q4f16_1 and q0f16), the model output gets truncated starting from the second turn. The truncation occurs during the thinking phase — the model stops generating before it can output the `</think>` closing tag and the actual response content. A typical truncated output looks like:

```
<think>
Okay, the user wants me to summarize the three benefits of exercise in one sentence.
Let me recall the previous answers. The original benefits were improving health,
boosting mood, and increasing energy. So, I need to combine these into a concise
sentence. Let me think of a way to express all three in one...
```

The output ends abruptly mid-thought, never reaching `</think>` or producing any response.

### Steps to Reproduce

```python
from mlc_llm import MLCEngine

model = "HF://mlc-ai/Qwen3-0.6B-q4f16_1-MLC"
engine = MLCEngine(model)

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# Turn 1: works fine, full thinking + response output
messages.append({"role": "user", "content": "What are three benefits of exercise?"})
response = engine.chat.completions.create(messages=messages, stream=False)
assistant_reply = response.choices[0].message.content
print("Turn 1 response:\n", assistant_reply)
messages.append({"role": "assistant", "content": assistant_reply})

print("\n")

# Turn 2: output truncated after </think>, no actual response content
messages.append({"role": "user", "content": "Now summarize those three points in one sentence."})
response = engine.chat.completions.create(messages=messages, stream=False)
print("Turn 2 response:",response.choices[0].message.content)  # Truncated

engine.terminate()
```

The following example demonstrates that the issue can be reproduced by simply prepending `<think>\n\n</think>\n\n` to the assistant message content, without any actual thinking output:

```python
from mlc_llm import MLCEngine

model = "HF://mlc-ai/Qwen3-0.6B-q4f16_1-MLC"
engine = MLCEngine(model)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What are three benefits of exercise?"},
    # Simulate a first-turn reply with <think>\n\n</think>\n\n prefix
    {"role": "assistant", "content": "<think>\n\n</think>\n\n1. Improves health. 2. Boosts mood. 3. Increases energy."},
    {"role": "user", "content": "Now summarize those three points in one sentence."},
]

response = engine.chat.completions.create(messages=messages, stream=False)
print("Response:", response.choices[0].message.content)  # Truncated

engine.terminate()
```

If you change the prefix to `<think>\n\n</think>` (without trailing newline), the response will be complete.

### Key Observations

1. **Only affects small models**: Qwen3-0.6B (both q4f16_1 and q0f16) is affected. Qwen3-1.7B-q4f16_1 works correctly with the same conversation.

2. **Truncation position**: The output truncates during the thinking phase, before `</think>` is ever generated. The model stops mid-thought and never produces the actual response content.

3. **Disabling thinking resolves the issue**: If thinking mode is disabled (so the model does not output `<think>...</think>` blocks), multi-turn chat works correctly without truncation.

4. **Stripping thinking content from history resolves the issue**: If `<think>...</think>` blocks are removed from assistant messages before sending them back as context, the issue does not occur.

5. **Narrowed down to `</think>` + trailing newline**: Through controlled experiments, replacing the thinking content in history with different variants:
   - `<think></think>` → no truncation
   - `<think>\n\n</think>` → no truncation
   - `<think>\n\n</think>\n\n` → **truncation reproduced**
   - `<think>\n\n</think>\n` → **truncation reproduced**

   This shows the issue is specifically triggered by newline characters following the `</think>` tag in the conversation history.

6. **ollama does NOT have this issue**: Running the same Qwen3-0.6B model via ollama (`qwen3:0.6b`) with identical conversation content (including `<think>\n\n</think>\n\n` in history) does **not** produce truncation. This confirms the issue is specific to mlc-llm's implementation, not the model itself.

7. **Reproducible in both mlc-llm and web-llm**: This issue can be reproduced in both the mlc-llm Python SDK and the web-llm JavaScript SDK, suggesting the root cause is in the shared underlying engine rather than a platform-specific issue.

### Workaround

Strip `<think>...</think>` blocks from assistant messages before including them in the conversation history:

```python
import re

def strip_thinking(messages):
    cleaned = []
    for msg in messages:
        if msg["role"] == "assistant":
            content = re.sub(r"<think>.*?</think>\s*", "", msg["content"], flags=re.DOTALL)
            cleaned.append({"role": "assistant", "content": content})
        else:
            cleaned.append(msg)
    return cleaned

# Use strip_thinking(messages) when calling engine.chat.completions.create()
```


### Feature Request

It would also be nice if mlc-llm could support the `extra_body.enable_thinking` field in `chat.completions.create()` to gracefully toggle Qwen3's thinking mode, similar to what web-llm has implemented in [mlc-ai/web-llm#686](https://github.com/mlc-ai/web-llm/pull/686). This would provide a cleaner way to control thinking behavior without relying on prompt-level workarounds.


## 评论 (2)

### MasterJH5574 · 2026-04-18

Hi @wopelo, thank you for reporting! #3484 is expected to fix this issue. The nightly wheel will be updated in a day after this PR is merged. We've also updated all published qwen3 models under https://huggingface.co/mlc-ai, so you can remove the model from your cache (in `~/.cache/mlc_llm/model_weights/hf/mlc-ai/`), update mlc-llm package to the latest (after the nightly built is done), and try again.

Feel free to let us know if the issue persists.

And also thank you for referring to the web-llm PR. That's a good idea and we'll leave it as an followup.

### MasterJH5574 · 2026-04-20

The nightly wheels should have been updated.
