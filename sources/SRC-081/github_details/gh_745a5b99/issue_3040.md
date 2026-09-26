# [Issue #3040] [Bug] Fix ignore list for linear_attn with Qwen3.8

source: https://github.com/vllm-project/llm-compressor/issues/3040
state: closed | updated: 2026-09-10T06:49:13Z
labels: bug, good first issue, good follow-up issue

## 正文

While applying the following recipe:

```python
recipe = [
    AWQModifier(duo_scaling="both"),
    GPTQModifier(
        targets="Linear", 
        scheme="W4A16",
        ignore=[
            "re:visual.*",
            "re:model.visual.*",
            r"re:.*lm_head",
            "re:.*embed_tokens$",
            r"re:.*linear_attn\.in_proj_a$",
            r"re:.*linear_attn\.in_proj_b$",
        ],
    )
]
```

I notice that the linear attn layers are correctly quantized and the proj_a/proj_b layers are correctly ignored. However, I see extra values in the ignore list:

```yaml
      "model.language_model.layers.62.linear_attn.norm",
      "model.language_model.layers.62.linear_attn",
      "model.language_model.layers.62.linear_attn.in_proj_b",
      "model.language_model.layers.62.linear_attn.in_proj_a",
```

model.language_model.layers.62.linear_attn should not be listed.

## 评论 (4)

### coderabbitai[bot] · 2026-08-17

<!-- This is an auto-generated issue plan by CodeRabbit -->
<details>
<summary>🔗 Related PRs</summary>

vllm-project/llm-compressor#2526 - [AWQ] AWQ as transform [merged]
vllm-project/llm-compressor#2597 - fix(examples): prevent visual modules from being quantized in Qwen2VL w8a8_fp8 example [merged]
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

### Shaurya2k06 · 2026-08-17

Happy to try this out!
cc @dsikka 

### dsikka · 2026-08-17

Thank you!

### Shaurya2k06 · 2026-08-19

Hey @dsikka , could you have a review on the above PR when you get the time? 
I tried to mark the issue as ready for review, wasn't able to :( 
