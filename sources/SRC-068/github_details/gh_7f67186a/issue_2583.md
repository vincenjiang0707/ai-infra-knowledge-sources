# [Issue #2583] Unsafe torch.load in FlashAttention training / eval checkpoint paths

source: https://github.com/Dao-AILab/flash-attention/issues/2583
state: closed | updated: 2026-06-05T04:18:18Z
labels: 

## 正文

So apparently someone issued [CVE-2026-31253](https://www.notion.so/CVE-2026-31253-35d1e1393188813f9e77e2038104bc49) because `torch.load` is being used in Flash Attention without `weights_only=True` in [this function](https://github.com/Dao-AILab/flash-attention/blob/4178915405522cb161ece80005e882c7465693b7/training/src/utils/checkpoint.py#L20) and [this function](https://github.com/Dao-AILab/flash-attention/blob/4178915405522cb161ece80005e882c7465693b7/training/src/eval.py#L34). Presumably they may take issue with [this](https://github.com/Dao-AILab/flash-attention/blob/4178915405522cb161ece80005e882c7465693b7/flash_attn/utils/pretrained.py#L62) and [this](https://github.com/Dao-AILab/flash-attention/blob/4178915405522cb161ece80005e882c7465693b7/flash_attn/models/llama.py#L388) as well.

I don't see any PR or issue open for this, not sure why that wasn't done before the CVE was issued, but I figured I'd start one.

## 评论 (1)

### warsang · 2026-05-28

(Not the CVE author, just saw it on my feed and looked at it, found the same missed sinks as pganssle) 

Opened https://github.com/Dao-AILab/flash-attention/pull/2600/ as well; not sure how important that file is in relation to the wider flash-attention project but it follows a similar pattern but using direct pickle instead of torch.load
