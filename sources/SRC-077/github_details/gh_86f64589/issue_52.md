# [Issue #52] Wrong solution to L3-31_VisionAttention in the artifact repo

source: https://github.com/meta-pytorch/KernelAgent/issues/52
state: open | updated: 2025-12-04T18:53:10Z
labels: 

## 正文

Dear KernelAgent team,

Thanks for sharing your work with the community. After carefully examining some results from the artifact reposiroty, I found that the solution to 31_VisionAttention of KernelBench Level 3 might be wrong.

https://github.com/Laurawly/kernelagent-artifacts/blob/main/L3/31_VisionAttention/final_kernel.py

The solution does not implement the attention mechanism. It only implements LayerNorm, but it passes the "wrong test" anyway.

I have tried to generate a solution using the complex Fuser pipeline, but it also gave me a false success. There's no Triton-based attention in the solution, because the test allows the agent to use `torch.bmm()` and `Tensor.matmul()`.

Would you release all artifacts for us to better understand the situation? Thanks.

## 评论 (6)

### Jack-Khuu · 2025-12-03

cc @Laurawly 

### Laurawly · 2025-12-03

> Dear KernelAgent team,
> 
> Thanks for sharing your work with the community. After carefully examining some results from the artifact reposiroty, I found that the solution to 31_VisionAttention of KernelBench Level 3 might be wrong.
> 
> https://github.com/Laurawly/kernelagent-artifacts/blob/main/L3/31_VisionAttention/final_kernel.py
> 
> The solution does not implement the attention mechanism. It only implements LayerNorm, but it passes the "wrong test" anyway.
> 
> I have tried to generate a solution using the complex Fuser pipeline, but it also gave me a false success. There's no Triton-based attention in the solution, because the test allows the agent to use `torch.bmm()` and `Tensor.matmul()`.
> 
> Would you release all artifacts for us to better understand the situation? Thanks.

Thanks a lot for digging into the artifacts and reporting this!

You were absolutely right: the old 31_VisionAttention artifact only did per-token LayerNorm and our Level-3 test let it slip. We’ve since tightened KernelAgent’s verification (no more doing the core math in PyTorch), rebuilt the test against the original nn.MultiheadAttention + LayerNorm model, and re-ran the pipeline so the new final_kernel.py implements full attention + residual + LayerNorm in Triton:

L3/31_VisionAttention/final_kernel.py

L3/31_VisionAttention/test.py

Feedback like this is exactly what helps us make KernelAgent a more reliable way to auto-generate high-performance Triton kernels.

### mzweilin · 2025-12-03

@Laurawly Thanks for the update. The new solution looks good to me! Are you going to release the updated implementation soon?

### sandlbn · 2025-12-04

I tried yesterday, and the translated solution was incorrect. The attention is still computed in pure PyTorch, and only the residual plus layer normalization is fused in Triton (I used the latest main branch). The generated kernel is attached.
As a possible simple solution, you should check whether the @jit tag is present on every kernel and then try running it—even with some random data—to verify that they pass a basic test.

[vision_kernel.py](https://github.com/user-attachments/files/23937981/vision_kernel.py)

### mzweilin · 2025-12-04

I was able to generate a solution using `anthropic/claude-sonnet-4.5` with the TritonKernelAgent directly. The code fails quietly if we don't configure the model and it switches to the complex pipeline which uses OpenAI's models by default.

I didn't get flashattention though.

[test.py](https://github.com/user-attachments/files/23939566/test.py)
[final_kernel.py](https://github.com/user-attachments/files/23939565/final_kernel.py)

### Laurawly · 2025-12-04

Thanks again for digging into this!

Just to clarify the “no flashattention” point: the current 31 artifact does use a FlashAttention-style kernel. In final_kernel.py, _flash_attn_fwd_kernel tiles over K/V, keeps running m_i and l_i, updates acc on the fly, and never materializes the full [L, L] matrix—this online softmax over sequence tiles is the core FlashAttention idea (just without causal mask or a fancy layout). Also note that our artifacts were generated with a GPT-5–based KernelAgent, so you may see slightly different kernels than with anthropic/claude-sonnet-4.5

Artifact link for reference:
https://github.com/Laurawly/kernelagent-artifacts/blob/main/L3/31_VisionAttention/final_kernel.py
