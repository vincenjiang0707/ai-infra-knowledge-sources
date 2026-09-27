# [Issue #3207] [Model Request] BitNet b1.58 2B4T - Scaling Native 1-bit LLM

source: https://github.com/mlc-ai/mlc-llm/issues/3207
state: open | updated: 2026-02-16T11:26:06Z
labels: new-models

## 正文

## ⚙️  Request New Models

- Link to an existing implementation (e.g. Hugging Face/Github): https://huggingface.co/microsoft/bitnet-b1.58-2B-4T
- Is this model architecture supported by MLC-LLM? No

It has just come out. May be a potential model for WebLLM


## 评论 (2)

### qwatts-dev · 2026-02-16

Hi folks, I saw this issue requesting BitNet b1.58 2B4T support for WebLLM. 

While waiting for official compiler-level support through TVM, I spent the weekend experimenting to see what the raw metal of the browser could do. I wrote a "vanilla JS" WebGPU compute kernel that successfully executes the BitNet ternary math (`-1, 0, 1`) entirely without floating-point multiplication. 

My latest release implements 2-bit weight packing, branchless bitwise execution (to prevent warp divergence), and 2D tiling via `var<workgroup>` shared memory. Running a 16.7M parameter matrix on Apple Silicon, the WGSL shader achieved a 10x to 22x compute speedup over the sequential CPU baseline.

It's just the linear layer "engine block" right now, but I wanted to drop the reference implementation here. Hopefully, the raw WGSL logic can be helpful to the TVM engineers designing the automated shader generation for ternary models!

Repo: https://github.com/qwatts-dev/bitnet-webgpu-poc

![Image](https://github.com/user-attachments/assets/03b1770b-6695-49ad-9a9b-5c933d3541c7)

### qwatts-dev · 2026-02-16

Hi folks, following up on my previous vanilla JS WebGPU experiment!

To prove the viability of native 1-bit / 1.58-bit execution in the browser, I just released `v0.3.0`, which successfully executes the actual, pre-trained weights from `microsoft/BitNet-b1.58-2B-4T`.

I extracted the 17.6M parameter `down_proj` layer using `safetensors`, packed the ternary weights (16 weights per `u32`), and ran them through the custom branchless WGSL compute shader. 

It successfully processed the real AI weights entirely without standard floating-point multiplication, hitting a 13.0 ms compute time on an iPhone 14 Pro Max and a 4.8 ms compute time on an M2 Max. 

I know the TVM compiler team is working hard on ternary operator support. I wanted to drop this fully working, hardware-validated WGSL shader logic here in case it helps with the automated shader generation for WebLLM!

Repo: https://github.com/qwatts-dev/bitnet-webgpu-poc
