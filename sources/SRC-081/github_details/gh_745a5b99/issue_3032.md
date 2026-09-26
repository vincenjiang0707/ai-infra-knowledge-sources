# [Issue #3032] [Feature] Multimodal calibration dataset support in oneshot

source: https://github.com/vllm-project/llm-compressor/issues/3032
state: closed | updated: 2026-09-05T18:25:19Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**
I am trying to quantize multimodal models such as google/gemma-4-E4B-it using a calibration mixture containing text, images, audio, and combined image-audio conversations.

The current dataset pipeline and examples appear primarily designed around text samples such as:

{"text": "..."}

For multimodal calibration, the model must receive all processor-generated inputs, for example:

{
    "input_ids": ...,
    "attention_mask": ...,
    "pixel_values": ...,
    "image_position_ids": ...,
    "input_features": ...,
    "input_features_mask": ...,
    "mm_token_type_ids": ...,
}

This is important even when only the language decoder is quantized. The vision and audio encoders may remain in BF16, but their outputs must still pass through the model so that activation observers on the decoder see realistic image- and audio-conditioned distributions.

**Describe the solution you'd like**
I would like oneshot() to provide first-class support for processor-aware multimodal calibration datasets.

**Describe alternatives you've considered**
N/A

**Additional context**
N/A


## 评论 (2)

### coderabbitai[bot] · 2026-08-15

<!-- This is an auto-generated issue plan by CodeRabbit -->
<details>
<summary>🔗 Related PRs</summary>

vllm-project/llm-compressor#2824 - [Autoround] add custom dataset support [closed]
</details>

---
<details>
<summary>📝 Issue Planner</summary>

<sub>Check the box below or use the `@coderabbitai plan` command to generate an implementation plan and prompts that you can use with your favorite coding assistant.</sub>

- [ ] <!-- {"checkboxId": "8d4f2b9c-3e1a-4f7c-a9b2-d5e8f1c4a7b9"} --> Create Plan
</details>


---
<details>
<summary> 🧪 Issue enrichment is currently in open beta.</summary>


You can configure auto-planning by selecting labels in the issue_enrichment configuration.

To disable automatic issue enrichment, add the following to your `.coderabbit.yaml`:
```yaml
issue_enrichment:
  auto_enrich:
    enabled: false
```
</details>

💬 Have feedback or questions? Drop into our [discord](https://discord.gg/coderabbit)!

### brian-dellabetta · 2026-08-18

Hi @sudo-0x2a , check out this Qwen VL example using flickr, a text+image dataset -- https://github.com/vllm-project/llm-compressor/blob/main/examples/quantizing_moe/qwen3_vl_moe_example.py


