# [Issue #1672] JVP support for FlashAttention

source: https://github.com/Dao-AILab/flash-attention/issues/1672
state: open | updated: 2026-06-27T17:15:01Z
labels: 

## 正文

Hello!

I am a researcher who is trying to implement the sCM paper (https://arxiv.org/pdf/2410.11081), in which the loss function requires computing the Jacobian-Vector Product.

However, I am running into a RuntimeError because the JVP calculation for FlashAttention hasn't been implemented yet:

> RuntimeError: In order to use an autograd.Function with functorch transforms (vmap, grad, jvp, jacrev, ...), it must override the setup_context staticmethod. For more details, please see https://pytorch.org/docs/master/notes/extending.func.html

I would greatly appreciate it if it's possible to support JVP calculation for FlashAttention!

Thank you so much! Looking forward to your response.

## 评论 (24)

### tridao · 2025-05-23

JVP would be nontrival to implement. Probably as challenging to write as the backward pass, which is already quite a bit harder than the attn forward.
I have some ideas there but there hasn't been many volunteers wanting to work on JVP.

That is to say, we don't have any plan to support JVP unless someone volunteers to work on it.

### limsanky · 2025-05-23

I see, thank you so much for your reply.

That is unfortunate to hear, indeed. But thank you so much for all your hard work! :)

By the way, for what it's worth, the authors of the sCM paper (https://arxiv.org/pdf/2410.11081) also propose a way to calculate JVP for FlashAttention in a single forward pass. 
It's detailed in Appendix F (Page 27~28).
Just wanted to let you know about it! Hope it is of some help 

Thanks once again :) 

### Birch-san · 2025-05-25

Seconding this, the [TrigFlow paper](https://arxiv.org/abs/2410.11081) linked above (Cheng Lu, Yang Song (OpenAI)) provides in Appendix F a derivation that would work with online softmax / fused QK. It doesn't look _too_ scary, though I don't know what would be involved in making it hardware-efficient.

<img width="688" alt="Image" src="https://github.com/user-attachments/assets/5eaa49ce-968c-4e3b-9d51-4328a4bde9db" />

<img width="713" alt="Image" src="https://github.com/user-attachments/assets/b1ea26b1-7d99-4af5-8595-53505014e9b8" />

jvp for attention would be useful for a lot of diffusion and flow model use-cases. Diffusion/flow models typically output a value that can be used to obtain the first derivative of the reverse diffusion ODE, but if you can use the jvp to obtain the _second_ derivative: you can either use that to inference accurately around a curved trajectory, or train the model to seek solutions with second derivatives closer to 1 (straight-trajectory), which yields a model that can linear extrapolate the ODE accurately, enabling few-step solutions.

highlighted image-gen research which uses the jvp to achieve few-step generation:

- [NVIDIA Genie](https://research.nvidia.com/labs/toronto-ai/GENIE/)
- [Consistency models](https://proceedings.mlr.press/v202/song23a.html)
  - certainly jvp is used in consistency distillation, I'm less sure whether it's used in consistency training, where [iCT](https://arxiv.org/abs/2310.14189) is the more recent development
- [TrigFlow](https://arxiv.org/abs/2410.11081)
  - this has been further incorporated into [Unified Continuous Generative Models](https://arxiv.org/abs/2505.07447), unclear whether they use jvp though
- [MeanFlow](https://arxiv.org/abs/2505.13447)
  - practitioners are already [implementing this](https://x.com/LodestoneE621/status/1926520450068124037) using jvp approximations (finite difference method)
- inferencing diffusion models via [truncated Taylor method sampler](https://discord.com/channels/729741769192767510/1007710893024481380/1140763177508945950)
  - without retraining, you can get the benefits of NVIDIA Genie, using forward-mode autodiff to obtain the second derivative of the reverse diffusion ODE, to more accurately traverse curved ODE trajectories

and with [text diffusion](https://deepmind.google/models/gemini-diffusion/) becoming more of a reality, these techniques will start to become relevant to language modelling too.

### tridao · 2025-05-26

One option is to naively apply JVP to the standard attention implementation softmax(Q @ K) @ V. That should just work, though probably slow.

The derivation above is for softmax(x) @ V, i.e. you already calculated x = Q @ K. But if you already materialize x in memory then there would be no speedup from flashattention.

o3 can derive the JVP of the softmax(Q @ K) @ V here: https://chatgpt.com/share/67d4d7a6-453c-8012-a844-498e6848915c
Implementing that looks about as hard as the flashattention backward.

### leon532 · 2025-05-26

> One option is to naively apply JVP to the standard attention implementation softmax(Q @ K) @ V. That should just work, though probably slow.
> 
> The derivation above is for softmax(x) @ V, i.e. you already calculated x = Q @ K. But if you already materialize x in memory then there would be no speedup from flashattention.
> 
> o3 can derive the JVP of the softmax(Q @ K) @ V here: https://chatgpt.com/share/67d4d7a6-453c-8012-a844-498e6848915c Implementing that looks about as hard as the flashattention backward.

I think the derivation of sCM provides a flash-attn style to calc jvp, where t_y is calculated through intermedia _m, l, f_, and x is block obtained using Q and K blocks. Also, we should calculate t_x using t_Q and t_K.

In this way, we only need a little changes based on the forward implementation of flash-attn.

Just wanted to confirm whether my understanding is correct. thanks.


### Birch-san · 2025-05-27

I think a good first step would be to implement the algorithm in pure pytorch first.

I've made a little test skeleton, which implements a [memory-efficient attention](https://arxiv.org/abs/2112.05682v2) (i.e. online softmax). there's a stub jvp method (unimplemented). the test invokes the attention with a dual tensor, and compares its output to a known-good reference (math attention).  
https://gist.github.com/Birch-san/5a97046abd7200a90a2f37ef62e67741

I did also have a stab at implementing the jvp, but I found it very hard to do this inside the idioms of torch.autograd.Function; using `ctx.save_for_forward()` on the many intermediates created inside chunks is not allowed, as you can only call `ctx.save_for_forward()` once.

I did separately try to implement the jvp _outside of_ autograd, just as a normal function that happens to output a dual tensor if it receives a dual tensor as input.  
I didn't understand all of what the maths was asking me to do; it wants to divide `g(x)` by `l(x)`, but mine were different shapes, as `g` accumulates via concatenation and `l` accumulates via summation. I think? I also wasn't totally sure how to compute `p @ t_v` as they don't really address it, I think you have to duplicate how you compute `p @ v`, but there are a few operations involved in that so I wasn't sure which of those wanted to operate on whose primals vs on whose tangents.  
so, I don't have much to show there. just a mess that doesn't work.

but overall, I am really pretty sure we don't need to materialize the whole sequence's QK similarities. the `x` to which they refer is only a chunk's similarities, that's why they also provide formulae for chunk-merging.

### tridao · 2025-05-27

I'm not yet convinced that you don't need to materialized the whole sequence QK. Agreed that having an implementation in pure pytorch is the first step, to make sure the algorithm proposed works.

### Ryu1845 · 2025-06-01

This seems to work
https://gist.github.com/Ryu1845/904a9b2c1fd58ca0b5d14119a5452eea

### limsanky · 2025-06-09

Hi @tridao !
There seems to be an implementation provided by @Ryu1845. Do you think this can be used and incorporated for the JVP implementation support?
Thanks again to @Ryu1845 and you for all your hard work!

### tridao · 2025-06-10

Could you guys test with longer sequences?
I'm curious what speed (TFLOPs/sec) you get.

### lucidrains · 2025-06-12

@Ryu1845 hey Sofian! just wanted to say great work on that triton script!

### Ryu1845 · 2025-06-12

Thank you! I'm working on the TFLOP/sec measurements, I'm getting very impressive results which makes me a little suspicious.

### Ryu1845 · 2025-06-12

@tridao 
OK, using the flash attention kernel from here gets me reasonable results. torch's scaled_dot_product_attention was a lot slower.

I'm using 4\*B\*H\*L^2\*D_head for flash attention and 10\*B\*H\*L^2\*D_head for JVP. 4 (fwd) + 2 (t_Q @ K.T) + 2 (Q @ t_K.T) + 2 (P @ t_V) = 10 \* BHL²d

Please correct me if I'm wrong
```
multihead_jvp_time_ms_L_scaling-B1-H2-D32:
         L  Triton Kernel  Naive PyTorch  Flash Attn CUDA
0     32.0       0.007462       0.087451         0.017171
1     64.0       0.008079       0.085264         0.018877
2    128.0       0.010158       0.094209         0.017697
3    256.0       0.013848       0.116408         0.020010
4    512.0       0.020685       0.198025         0.021528
5   1024.0       0.034922       0.437495         0.026477
6   2048.0       0.068099       1.660510         0.039705
7   4096.0       0.161893       7.320213         0.091831
8   8192.0       0.527468      27.747135         0.255655
9  16384.0       1.887918     108.681213         0.994310
multihead_jvp_tflops_L_scaling-B1-H2-D32:
         L  Triton Kernel  Naive PyTorch  Flash Attn CUDA
0     32.0       0.085976       0.005990         0.013892
1     64.0       0.322910       0.033685         0.059678
2    128.0       1.039170       0.113062         0.238698
3    256.0       2.981799       0.334079         0.827469
4    512.0       7.951310       0.875725         3.109307
5   1024.0      18.780606       1.600376        10.990911
6   2048.0      39.941197       1.596995        27.862681
7   4096.0      70.081417       1.455714        47.638361
8   8192.0      89.615112       1.562998        66.322467
9  16384.0      87.306901       1.439166        69.730795
```

### Birch-san · 2025-06-14

Sanity-check on the FLOP count:  
https://gist.github.com/Birch-san/08f49ca5f8fb0bf0174c9f760605ffa5

```
bsz=1
model_dim=320
head_dim=64
seq_len=128

Flash, fwd only
Module                                          FLOP    % Total
-------------------------------------------  -------  ---------
Global                                       20.972M    100.00%
 - aten._scaled_dot_product_flash_attention  20.972M    100.00%

Math, fwd only
Module          FLOP    % Total
-----------  -------  ---------
Global       20.972M    100.00%
 - aten.bmm  20.972M    100.00%

Math, fwd+jvp
Module          FLOP    % Total
-----------  -------  ---------
Global       62.915M    100.00%
 - aten.bmm  62.915M    100.00%

62.915 / 20.972 = 3
```

If we use torch's FLOP counter to count the matmul flops of SDPA math backend's JVP: obtaining the jvp costs 3x more operations than a normal fwd.

If we're only counting matmul FLOPs, then we can just consider the FLOP count of the JVPs of any matmuls involved.  
I think chunked vs unchunked doesn't change the number of matmul operations. Certainly math and flash are aligned on matmul flops for fwd-only. so probably the FLOP count for math attn's jvp tells us what to expect for a chunked JVP too.

if `Q•K.mT`'s flops are given by `mm_flops(q_p, k_p)`, then its tangent's flops are given by `mm_flops(q_t, k_p) + mm_flops(q_p, k_t)`. The same holds for the matmul of attn probabilities with V.  
https://github.com/SHI-Labs/NATTEN/issues/68  
So I think JVP's matmul FLOPs will be double those of the fwd pass?  
And the reason torch reports 3x matmul FLOPs is probably due to computing both the fwd and the jvp? 1+2.

I also tried `torch.func.linearize()` but it was worse:  
https://gist.github.com/Birch-san/b378e14266003c4bf3854f735b40d986

### Birch-san · 2025-06-14

here's a second opinion on benchmark and flop count, using `triton.testing.do_bench` and `torch.utils.flop_counter.FlopCounterMode`. We count JVP FLOPs from math attn, then measure latency of Triton and compute FLOP/s from those two quantities.    
https://gist.github.com/Birch-san/9ae247d7ebffe36a06ae54a75f614804

I haven't done a sweep (and need to call it a night at this point) but here's how it does on 8k sequences (which is the largest I could fit on an H100 with dim 2048):

```bash
python -m jvp_bench --bsz 1 --model-dim 2048 --head-dim 64 --seq-len 8192
```

```
Math, fwd+jvp
Module            FLOP    % Total
-----------  ---------  ---------
Global       1649.267B    100.00%
 - aten.bmm  1649.267B    100.00%

SDPA JVP: 138.9 TFLOP/s
Triton JVP: 497.6 TFLOP/s

sanity-checking whether our latencies make sense by testing a known-fast operation

Flash, fwd only
Module                                           FLOP    % Total
-------------------------------------------  --------  ---------
Global                                       549.756B    100.00%
 - aten._scaled_dot_product_flash_attention  549.756B    100.00%

Flash fwd: 314.1 TFLOP/s
```

So, on a large problem it's ~3.6x faster than unchunked math attn.  
And it appears to be performing more FLOP/s than a fwd-only flash attn operation does. may be more due to increased number of operations than reduced latency.

Note, I had to make some changes to the kernel in order to make the benchmark run:

```
at 106:37:
        qk = qk * qk_scale - m_ij[:, None]  # Scale and subtract max
        p = tl.math.exp2(qk)  # Use exp2 like reference

        # Correction factor
        alpha = tl.math.exp2(m_i - m_ij)
        l_ij = tl.sum(p, 1)

        # Update normalization
        l_i = l_i * alpha + l_ij

        # Update output accumulator
        acc = acc * alpha[:, None] + tl.dot(p, v)
                                     ^
AssertionError: Both operands must be same dtype. Got fp32 and fp16
```

So, I added some downcasts:

```python
# Replace the problematic section in your kernel (around lines 100-120) with this:

        # Online softmax computation following Flash Attention
        m_ij = tl.maximum(m_i, tl.max(qk * scale, 1))
        qk = qk * qk_scale - m_ij[:, None]  # Scale and subtract max
        p = tl.math.exp2(qk)  # Use exp2 like reference
        
        # Correction factor
        alpha = tl.math.exp2(m_i - m_ij)
        l_ij = tl.sum(p, 1)
        
        # Update normalization
        l_i = l_i * alpha + l_ij
        
        # Cast p back to input dtype for matmul
        p_typed = p.to(q.dtype)
        
        # Update output accumulator
        acc = acc * alpha[:, None] + tl.dot(p_typed, v)
        
        # JVP accumulator: (p * tqk) @ v  
        p_tqk = p * (tqk * scale)  # Apply scale to tangent scores
        p_tqk_typed = p_tqk.to(q.dtype)  # Cast tangent weights too
        g_acc = g_acc * alpha[:, None] + tl.dot(p_tqk_typed, v)
        
        # Update mu: sum(p * tqk)
        mu_ij = tl.sum(p_tqk, 1)
        mu_i = mu_i * alpha + mu_ij
        
        # Update p @ tv accumulator  
        p_tv_acc = p_tv_acc * alpha[:, None] + tl.dot(p_typed, tv)
```

I didn't do parity tests to confirm it's still allclose to anything.

### Birch-san · 2025-06-14

Sanity-check on the largest sequence for which you provided FLOP/s, B1-H2-D32… that's 2 heads, head_dim=32?

```bash
python -m jvp_bench --bsz 1 --model-dim 64 --head-dim 32 --seq-len 16384 

Math, fwd+jvp
Module           FLOP    % Total
-----------  --------  ---------
Global       206.158B    100.00%
 - aten.bmm  206.158B    100.00%

SDPA JVP:  68.4 TFLOP/s
Triton JVP: 352.5 TFLOP/s

sanity-checking whether our latencies make sense by testing a known-fast operation

Flash, fwd only
Module                                          FLOP    % Total
-------------------------------------------  -------  ---------
Global                                       68.719B    100.00%
 - aten._scaled_dot_product_flash_attention  68.719B    100.00%

Flash fwd: 214.5 TFLOP/s
```

You reported:  
SDPA JVP: 1.4 TFLOP/s
Triton JVP: 87.3 TFLOP/s
Flash fwd: 69.7 TFLOP/s

Hm, our results are pretty different.

My triton kernel has some extra downcasts in it.  
Maybe your tests were running math attn in fp32?

And we may be computing FLOP/s from different FLOP amounts.

### KohakuBlueleaf · 2025-06-14

For reference, MeanFlow also need jvp support and it even requires the primal output to be compatible with .backward()

https://arxiv.org/abs/2505.13447

| Paper Pseudo Code | Real Code |
|-|-|
|![Image](https://github.com/user-attachments/assets/cf1c5602-8f4b-4bd2-bce7-c2e399fd306a)|![Image](https://github.com/user-attachments/assets/1eb50856-cbb5-4654-9fa2-73f17b0f4f3d)|

### dabeschte · 2025-06-24

> This seems to work https://gist.github.com/Ryu1845/904a9b2c1fd58ca0b5d14119a5452eea

@Ryu1845 
thanks for sharing this.
I tried it out just now and ran into a problem with the second call of the sdpa. the first one was correct, but the second only computed results for the first quarter of the sequence length in my tests.

I think this is happening, because the autotuning changes the block shapes, but the grid size is constant.

I was able to fix that by replacing this line https://gist.github.com/Ryu1845/904a9b2c1fd58ca0b5d14119a5452eea#file-standalone_multihead_jvp_test-py-L273

``` grid = (B * H, triton.cdiv(L, BLOCK_M))```
by this:
``` grid = lambda meta: (B * H, triton.cdiv(L, meta["BLOCK_M"])) ```

### Birch-san · 2025-06-29

I've implemented the JVP on top of the triton fused attention tutorial code.  
With some gymnastics to get autograd to let me compute the fwd+jvp together.  
The autograd function supports backpropping through primal, which Meanflow requires.  
Just need to improve the accuracy of the JVP; it's not as accurate as @Ryu1845's, so need to dig into that (atol=1e-3, but my hope is to able to get down to 5e-4). The current suggestion from Claude is that I've applied the scale factor incorrectly. I also wonder whether I need to track and utilise row-wise maxima of the tangent, but the other kernel didn't need to do that.

https://gist.github.com/Birch-san/c51234fe006cf1ffc680063abb4f572f

### Birch-san · 2025-07-05

actually I think the accuracy of my kernel isn't a problem.

flash-attn tests with `allclose(rtol=1e-3, atol=1e-3)`(see [`test_flash_attn.py`](https://github.com/Dao-AILab/flash-attention/blob/312bb9b35ecbac27ae11bcac38bfaec68dd3aba3/tests/test_flash_attn.py#L2137C58-L2137C80)) so my `atol=1e-3, rtol=1e-5` should be acceptable too.

In fact, only 0.0% of elements fail to satisfy `atol=5e-4, rtol=1e-5`:

```
Mismatched elements: 2 / 40960 (0.0%)
Greatest absolute difference: 0.0009765625 at index (0, 2, 80, 42) (up to 0.0005 allowed)
Greatest relative difference: 0.0009093284606933594 at index (0, 2, 80, 48) (up to 1e-05 allowed)
```

The worst difference was:

```
-1.0732 actual
-1.0742 expected
```

to give an idea of how close these are: they can't even be distinguished in bfloat16:

```
torch.tensor(-1.0732, dtype=torch.bfloat16)
# tensor(-1.0703, dtype=torch.bfloat16)
torch.tensor(-1.0742, dtype=torch.bfloat16)
# tensor(-1.0703, dtype=torch.bfloat16)
```

I investigated Claude's claims. I don't think the scale factor used in the jvp is wrong; Claude notices that it doesn't match the one used in the forward pass, but that's intentional. Primal uses `scale * 1.44269504` to prepare its QK similarities to be exponentiated in base-2 instead of base-e (`1/ln(2)=1.44269504`), to compute primal probabilities. But we don't need to compute tangent probabilities to get the jvp of attention, we only need to compute tangent similarities. so we don't need to do any change-of-base scaling of the tangent QK.  
And also if I ignore all that and just try adding that coefficient to the tangent's scales anyway: accuracy completely fails. so we can be confident there's no merit in that idea.

I also see that my other idea of tracking row-wise maxima of the tangent similarities isn't necessary either. The paper confirms that primal row-wise maxima can be reused. This makes sense; row-wise maxima are for achieving a more accurate softmax. And as we only compute primal probabilities, not tangent probabilities: we don't need row-wise maxima of tangent QK.


### amorehead · 2025-09-03

Hey, everyone. Thanks to your amazing open-source contributions within this thread, I have finalized a `pip`-installable version of the (now training-ready) JVP Flash Attention Triton kernel, along with an additional unit testing suite. Feel free to check it out, and as always, feedback and PRs are welcome!

Repo: https://github.com/amorehead/jvp_flash_attention

### amorehead · 2025-09-15

@tridao, I've now unit tested and empirically verified the correctness of my updated version of Triton's Flash Attention v2 kernel (https://github.com/amorehead/jvp_flash_attention/pull/4). Now, arbitrary (e.g., boolean) `attn_mask` arguments are supported in this implementation of Flash Attention (whereas before the Triton kernel did not support masking). Would it be possible [here](https://github.com/Dao-AILab/flash-attention?tab=readme-ov-file#triton-implementation-of-flashattention) to link others to this JVP Flash Attention implementation in case they are interested in using `attn_mask`s with the Triton version of Flash Attention (or in case they are interested in using Flash Attention with second-order derivatives)?

### Luo-Yihong · 2026-06-27

Hi  @tridao  and the FlashAttention team,
First off, thank you for the incredible work on FlashAttention — it's foundational to so much of the generative modeling community.

I wanted to follow up on this issue because two major research codebases have already implemented and open-sourced JVP-compatible FlashAttention kernels, and it would be extremely valuable for the broader community if these could be upstreamed into the official FlashAttention library.

1. NVlabs / rCM
The [rCM (Score-Regularized Continuous-Time Consistency Model)](https://github.com/NVlabs/rcm) repository by NVIDIA Research explicitly provides:
- "Open-sourced FlashAttention-2 Jacobian-vector product (JVP) kernel with support for parallelisms like FSDP/CP."
- Implementation: https://github.com/NVlabs/rcm/blob/main/rcm/utils/flash_attention_jvp_triton.py
- Features: Triton-based, supports FSDP2, Ulysses Context Parallel, and Selective Activation Checkpointing
- Use case: Scales sCM / MeanFlow distillation to 10B+ parameter video diffusion models

2. Luma Labs / TVM
The [TVM (Terminal Velocity Matching)](https://github.com/lumalabs/tvm) repository by Luma AI also ships a custom fused attention kernel:

- "We develop an efficient Flash Attention kernel that supports backward passes on Jacobian-Vector Products (JVP), crucial for our terminal velocity computation."

- Paper: [arXiv:2511.19797](https://arxiv.org/abs/2511.19797) — Section 7.4 shows the kernel avoids OOM (naïve SDPA runs out of memory) and achieves significant speedup

- Features: Fuses forward + JVP computation, handles multi-step backward passes efficiently, compatible with FSDP

- Use case: Single-stage training of few-step generative models from scratch

Would the FlashAttention team consider reviewing these implementations for potential upstream integration?

### limsanky · 2026-06-27

Hi @tridao, the FA team, and @Luo-Yihong,

I'd also like to strongly recommend [JVP Flash Attention](https://github.com/amorehead/jvp_flash_attention) by @amorehead, because I think their code might provide an excellent starting point in reviewing and/or integrating the JVP functionality into the official repo.

Thanks once again for all your hard work!

