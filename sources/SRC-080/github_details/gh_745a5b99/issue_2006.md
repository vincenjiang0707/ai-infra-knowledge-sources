# [Issue #2006] [RFC]: MR-GPTQ (GPTQ+NVFP4)

source: https://github.com/vllm-project/llm-compressor/issues/2006
state: closed | updated: 2026-09-23T05:47:26Z
labels: enhancement, keep-open

## 正文

A new paper came out that tailors GPTQ to MXFP4 and NVFP4 storage format:
- https://arxiv.org/pdf/2509.23202

> The recent hardware-accelerated microscaling 4-bit floating-point formats such as MXFP4 and NVFP4, supported on NVIDIA and AMD GPUs, promise to revolutionize large language model (LLM) inference. Yet, their practical benefits remain unproven. We present the first comprehensive study of MXFP4 and NVFP4 for post-training quantization, revealing gaps between their promise and real-world performance. Our analysis shows that state-of-the-art methods struggle with FP4, due to two key issues: (1) NVFP4's small group size provably neutralizes traditional outlier mitigation techniques; (2) MXFP4's power-of-two scale quantization severely degrades accuracy due to high induced error. To bridge this gap, we introduce Micro-Rotated-GPTQ (MR-GPTQ), a variant of the classic GPTQ quantization algorithm that tailors the quantization process to FP4's unique properties, by using block-wise Hadamard transforms and format-specific optimizations. We support our proposal with a set of high-performance GPU kernels that enable the MR-GPTQ format with negligible overhead, by rotation fusion into the weights, and fast online computation of the activations. This leads to speedups vs. FP16 of up to 3.6x layer-wise, and 2.2x end-to-end on NVIDIA B200, and of 6x layer-wise and 4x end-to-end on RTX5090. Our extensive empirical evaluation demonstrates that MR-GPTQ matches or outperforms state-of-the-art accuracy, significantly boosting MXFP4, to the point where it can near the accuracy that of NVFP4. We conclude that, while FP4 is not an automatic upgrade over INT4, format-specialized methods like MR-GPTQ can unlock a new frontier of accuracy-performance trade-offs. 

The models are supported in vLLM since https://github.com/vllm-project/vllm/pull/24440 and reference quantization framework is https://github.com/IST-DASLab/FP-Quant

## 评论 (4)

### kylesayrs · 2025-11-10

Hi @mratsim!

This technique has been implemented in LLM Compressor through transforms + GPTQ. More work needs to be done to verify these results, but you can try out this configuration yourself using the below example and changing QuantizationModifier to GPTQModifier.

https://github.com/vllm-project/llm-compressor/blob/main/examples/transform/quip_example.py 

### mratsim · 2025-11-10

I managed to quantize Qwen3-4b, with llmcompressor 0.8.1, currently rebuilding a vllm from source due to Hadacore kernels not being built for SM120: https://github.com/vllm-project/vllm/pull/28391

### mratsim · 2025-11-10

I manage to load the weights, though the output is garbage, have to experiment to isolate the issue.

Recipe:
```python
DAMPENING_FRAC=0.005
recipe = [
    QuIPModifier(
        rotations=["v", "u"], transform_block_size=32, transform_type="hadamard"
    ),
    GPTQModifier(
        ignore=["lm_head"],
        dampening_frac=DAMPENING_FRAC,
        block_size=32,
        config_groups={
            "group_0": {
                "targets": ["Linear"],
                "weights": {
                    "num_bits": 4,
                    "type": "int",
                    "symmetric": True,
                    "group_size": 32,
                    "strategy": "group",
                    "dynamic": False,
                    "actorder": "group",
                    "observer": "mse",
                },
            }
        },
    ),
]
```

- QUIP+GPTQ+NVFP4

<img width="1283" height="1221" alt="Image" src="https://github.com/user-attachments/assets/5bdd462a-3a15-420e-9451-02acfc1e5ad6" />

- For reference GPTQ + INT3 quantization

<img width="1285" height="1169" alt="Image" src="https://github.com/user-attachments/assets/ee1d46ae-6973-4646-ba64-96e3630ce999" />


### kylesayrs · 2026-09-23

There are existing examples of using MR-GPTQ as well as integration with vLLM. While the feature is functional, future work on the MR-GPTQ pathway being deprioritized for now. If anyone is still interested in this feature, please open a new ticket or reach out on the [vLLM slack](https://inviter.co/vllm-slack)!
