# [Issue #3106] Qwen3-Omni-30B-A3B-Thinking量化fp8_DYNAMIC问题，单卡OOM，双卡RuntimeError: We could not revert some weight conversions because of offlading...

source: https://github.com/vllm-project/llm-compressor/issues/3106
state: open | updated: 2026-08-27T16:21:43Z
labels: 

## 正文

做Qwen3-Omni-30B-A3B-Thinking量化的时候，使用单卡(NVIDIA RTX Pro 6000(96G))出现OOM问题。
换成双卡：
oneshot(
    model=model,
    recipe=recipe,
    save_compressed=True,
    output_dir=OUTPUT_DIR,
)
出现：RuntimeError: We could not revert some weight conversions because of offlading, and several weights needed for a single conversion operation living in different shard files. Try reducing `max_shard_size` a bit, or worst case set `save_original_format=False`.
如果：1、设置oneshot里save_compressed=False。
2、调用 model.save_pretrained() 手动保存，并指定 save_original_format=False 和 max_shard_size。
量化得到的模型，在vllm中运行出现：KeyError: 'layers.0.self_attn.qkv.weight_scale'


## 评论 (0)
