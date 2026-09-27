# [Issue #100] Weight Sharding

source: https://github.com/dropbox/hqq/issues/100
state: closed | updated: 2024-08-28T10:07:05Z
labels: 

## 正文

I'm trying to quantize 405b, but then I'm unable to upload it to HF since it's ~200GB and HF LFS has a limit on 50GB file sizes. Is there a correct way to shard the model file so it can be loaded again with AutoHQQ?

## 评论 (2)

### mobicham · 2024-08-02

There's a pull request for sharded safetensors serialization on-going: https://github.com/huggingface/transformers/pull/32379 
Once this is fixed, it's gonna be possible to save hqq-quantized models directly via `model.save_pretrained` as sharded safetensors

### mobicham · 2024-08-28

Closing this since we are very close to full transformers serialization support here: https://github.com/huggingface/transformers/pull/33141
