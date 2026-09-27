# [Issue #282] RuntimeError: The expanded size of the tensor (2048) must match the existing size (2080) at non-singleton dimension 2.  Target sizes: [1, 4, 2048, 128].  Tensor sizes: [4, 2080, 128]

source: https://github.com/mit-han-lab/llm-awq/issues/282
state: open | updated: 2025-05-16T09:09:47Z
labels: 

## 正文

python llm-awq/tinychat/nvila_demo.py --model-path VILA/NVILA-8B       \
    --quant_path quant_cache/NVILA-w4-g128-awq-v2.pt      \
    --media drowsy_video1.mp4    \
    --act_scale_path awq_cache/NVILA-VT-smooth-scale.pt \
    --quant_llm --chunk --model_type nvila
I'm facing this issue while running the inference for nvila model

RuntimeError: The expanded size of the tensor (2048) must match the existing size (2080) at non-singleton dimension 2.  Target sizes: [1, 4, 2048, 128].  Tensor sizes: [4, 2080, 128]
how do i fix this?

## 评论 (1)

### witti-stephen · 2025-05-16

The output is 2080 in length, longer then 2048 (I see somewhere it's the KV cache predefined size), you can add a switch (e.g. at the end after your --model type nvila) --max_seq_len 4096, I assume this would need some additional memory but that would solve your problem

ref: https://github.com/NVlabs/VILA/issues/16
