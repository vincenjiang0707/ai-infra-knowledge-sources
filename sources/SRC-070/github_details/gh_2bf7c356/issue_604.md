# [Issue #604] Hybrid-EP has hang and precision issues in SFT training with variable sequence lengths

source: https://github.com/deepseek-ai/DeepEP/issues/604
state: open | updated: 2026-05-09T04:16:28Z
labels: 

## 正文

hello DeepEp and HybridEp team
I found some bugs about HybridEp

1. During SFT training, each rank may have a different `max_num_of_tokens_per_rank ` in `HybridEPBuffer.__init__().` In `update_template_config` calls, the `num_of_tokens_per_rank` in the hidden state is also different. This causes some ranks to wait at an all_gather while others skip it, resulting in a hang.

the hang place is `bool HybridEPBuffer::update_buffer`. some ranks `need_reallocate=false` so skip the all_gather in `allgather_obj.update(buffer_config);`

2. In `dispatch_with_permute`, `metadata_preprocessing` receives a `routing_map`, but the length of `routing_map` is different. This leads to different input lengths for the `all_gather_into_tensor` operation in `Executor::allgather_routing_map`, causing precision issues.

Fix:
1. I try to use `max_num_of_tokens_per_rank=next_power_of_two(max_num_of_tokens_per_rank)` so that the length is always max_length.
2. Fix precision issue by padding `routing_map` to `max_num_of_tokens_per_rank`. 


`pad_rows = config.max_num_of_tokens_per_rank - num_of_tokens_per_rank` 
`routing_map = torch.nn.functional.pad(routing_map, (0, 0, 0, pad_rows), value=False)`

Training normally after these two fixes


## 评论 (1)

### Autumn1998 · 2026-05-09

Hi, thank you for the information. For this situation where the number of tokens from attn by each rank is inconsistent, there is currently no official support. The only workaround is through an approach similar to padding. Sorry about that!
