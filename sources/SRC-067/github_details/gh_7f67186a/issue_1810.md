# [Issue #1810] FA3 attention sinks blackwell sm120

source: https://github.com/Dao-AILab/flash-attention/issues/1810
state: open | updated: 2026-07-31T16:53:56Z
labels: 

## 正文

Hi why can;t we use gpt-oss models with 50 series cards and rtx pro 6000? It says it requires attention sinks and FA3 and that FA3 is not supported. These cards have been out for 8 months I wonder why is there so little support? Is there 2 blackwell architectures? sm100 and sm120?

## 评论 (7)

### tridao · 2025-08-13

sounds great, would you like to contribute a PR?

### fernandaspets · 2025-08-13

> sounds great, would you like to contribute a PR?

yes I have to learn how though i did some research yesterday. its way beyond me but im interested so will try to learn more. not user if this is something that requires years of training but happy to try and learn and contribute. thanks for responding!

### rpcarvalheira · 2025-08-14

#1683 tries to solve that. However, flash-attention is not simple, neither an easy solution, so, you'll have to help debugging with @loscrossos as all applications have bugs and normally, forks may be outdated, which means you'll have to be patient, since there will be no simple solution or fast fixes.

Try that solution and if you cannot contribute with code, you can always provide issues and report bugs in a well described manner. Since you're using AI, you can already request for LLM's help on that aspect and provide references, logs, context, process to replicate and any additional information needed; these may help the community as well. If you cannot do any of these, it's a good time to think about sponsoring projects. :)

### cmp-nct · 2025-08-15

@tridao I also found it the hard way, compiled FA3 for 6 hours and then it didn't work for the 5090 and gpt-oss-* 
Wouldn't it be possible to just use the CUDA 8.9 architecture until V12 is supported ? 
So 50xx cards can run, just without optimized kernels ?


### JINO-ROHIT · 2026-07-20

hi, id like to take a stab at this issue, is anyone working on this? can this be assigned to me?

### fernandaspets · 2026-07-22

> hi, id like to take a stab at this issue, is anyone working on this? can this be assigned to me?

yes there is a community now for sm120 on discord: https://discord.gg/jQwPtBKVP and then also the repo here https://github.com/local-inference-lab/rtx6kpro

 vllm fork for sm120 with custom kernels. very active new developments every single day

### arbi-dev · 2026-07-31

FYI: opened #2752, which removes the `assert learnable_sink is None` in the FA4 CuTeDSL SM80 forward kernel (`flash_attn/cute/flash_fwd.py`). `FlashAttentionForwardSm120` subclasses that kernel without overriding `__call__`/`kernel`, so this should also enable `learnable_sink` on SM120 (RTX 50-series) through `flash_attn.cute.flash_attn_func(..., learnable_sink=...)`.

Caveat: I verified this on real SM80 hardware (2x RTX 4090, cosine similarity > 0.99998 against a PyTorch SDPA+sink reference across several shapes), but I don't have SM120 hardware to confirm directly — flagging for anyone who can test on an actual RTX 50-series card. This is FA4's CuTeDSL forward path specifically, not FA3 (which remains Hopper-only).
