# [Issue #1591] value instability when training the model with AMD ROCm GPU

source: https://github.com/Dao-AILab/flash-attention/issues/1591
state: closed | updated: 2026-05-29T16:29:19Z
labels: 

## 正文

The arguments are referred from the gpt training codes.

The flash attention layer in my scripts:
"
self.norm1 = nn.LayerNorm(128)
self.dtype = self.norm1.weight.dtype
self.device = self.norm1.weight.device
softmax_scale = num_heads ** (-0.5)
self.self_attn = MHA(embed_dim=128,
                                      num_heads=8,
                                      use_flash_attn=True,
                                      qkv_proj_bias=True,
                                      out_proj_bias=True,
                                      dropout=0.1,
                                      softmax_scale=softmax_scale,
                                      causal=True,
                                      use_alibi=True,
                                      window_size=(-1, -1),
                                      device=self.device,
                                      dtype=self.dtype,
                                      )
"

I have tried many times to train the model with the flash attention layer instructed by the /module/mha.py.  
There are "nan" pop out and stop the training process by chance 90% of the time. The loss of the masked language model never goes down to less than 9.
The nan issue disappears when using the naive attention layer to train my model, and the masked language loss goes down to ~4.

Is there any problem with my condifurations?
I only modify the MHA function as below:

from:
"
if use_alibi:
      assert use_flash_attn, "ALiBi code path requires flash_attn"
      alibi_slopes = torch.tensor(get_alibi_slopes(num_heads), device=device)
"
to
"
if use_alibi:
      assert use_flash_attn, "ALiBi code path requires flash_attn"
      alibi_slopes = torch.tensor(get_alibi_slopes(num_heads), device=device)
      alibi_slopes = alibi_slopes.clone().expand(Settings.batch_size, -1).contiguous()
"
Otherwise, there will be error of size mismatch:
[rank0]:   File "/scratch/project_465001820/miniconda3/envs/scCLIP2/lib/python3.10/site-packages/flash_attn-2.7.4.post1-py3.10.egg/flash_attn/flash_attn_triton_amd/utils.py", line 80, in need_alibi
[rank0]:     assert alibi_slopes.dim() == 2
[rank0]: AssertionError

Then, I tried not to use alibi by setting the use_alibi=False; it works well!


## 评论 (5)

### tridao · 2025-04-13

@rocking5566 does the AMD version support alibi?

### rocking5566 · 2025-04-15

If @TerminatorJ call composable kernel backend, such as `from flash_attn import flash_attn_qkvpacked_func` , alibi is supported.
According to the assert message, looks like you are using triton?
CC @micmelesse 


### micmelesse · 2025-04-15

Alibi is not yet full supported in the triton backend. I am working on a pr which I will put up soon with support for alibi and other features such as a faster backward pass. I am hoping to put up the pr this week or next week.

### micmelesse · 2025-04-22

@TerminatorJ  We enable alibi in this pr, https://github.com/Dao-AILab/flash-attention/pull/1610. 

### micmelesse · 2026-05-29

Closing this issue. 
