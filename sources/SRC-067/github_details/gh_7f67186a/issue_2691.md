# [Issue #2691] Make dropout-disabled FA2 ABI stable with libtorch + cpython

source: https://github.com/Dao-AILab/flash-attention/issues/2691
state: open | updated: 2026-07-18T15:49:54Z
labels: 

## 正文

TL;DR: I (and vllm + sglang + downstream libs) would love for FA2 to be ABI stable! If we drop FA2 C++ generator support and expand the FLASHATTENTION_DISABLE_DROPOUT macro and move the build version minimum to torch 2.10, we can do it pretty cleanly. What are your thoughts? cc @tridao 

The ecosystem/downstream libraries like vllm and sglang would benefit from an ABI stable FA2 just like we have with FA3. ABI stability would mean that it would be possible to build 1 wheel that runs across multiple Python and PyTorch versions, which saves a lot of build resources.

I'm opening this issue to discuss whether upstream would be happy to accept this change + if so the best way to implement it (I propose a plan below). It would be great to have this be in upstream so that downstream forks don't have to duplicate efforts and can simply apply `-dFLASHATTENTION_DISABLE_DROPOUT` to get an ABI stable build.

How can we get there?
* Note: It is already possible to make FA2 CPython agnostic by switching it to use TORCH_LIBRARY instead of pybind11 for binding across C++ and Python
* There is a blocker for general FA2 for LibTorch stability--the Philox and RNG APIs do not have libtorch stable APIs in torch yet. However, these APIs are only needed to support dropout, which neither vllm and sglang need! So it would already be very impactful to have the dropout-disabled FA2 be ABI stable with torch.
	* There is already a compiler flag to disable dropout: FLASHATTENTION_DISABLE_DROPOUT. We should expand this to exclude building with philox and RNG headers when set. I propose a tested impl in https://github.com/Dao-AILab/flash-attention/pull/2669
	* Then, we can safely move dropout-disabled FA2 to use libtorch stable APIs. I do this in this tested PR: https://github.com/Dao-AILab/flash-attention/pull/2688

Some tradeoffs to discuss:
A. One thing I ran into while yanking out the RNG bits for when dropout is disabled: the C++ APIs for mha_fwd/bwd and the mha_varlen_fwd/bwd include an optional Generator argument for which the Python frontend APIs always pass in None. I also did some scouring over GitHub usages of flash_attn_2_cuda (and its common aliases flash_attn_cuda and flash_attn_gpu) and found 0 public uses where a generator is passed in to the module. My current PRs simply get rid of the generator arguments (today the default generator is always used anyway) but that may be too BC-breaking. There's a spectrum of solutions we can go for: we can branch between dropout and no-dropout so that dropout will have the Generator arg while no-dropout will not OR we can maintain a dummy optional and assert it's always None for both paths. Happy to discuss -- my priority is for the no-dropout schema to not have Generator so that we can make it stable right now for torch 2.10+ (vs waiting til 2.13+).
B. Moving to use ABI stable would require the build time minimum version to increase to torch 2.10. If this is not acceptable, we can make a variant built similar to FA3 (flash_api_stable.cpp in hopper), which is a little less ideal due to code duplication.

How does the plan sound? Would the maintainers be interested in having an ABI stable version of FA2 (no dropout) be available?

cc @drisspg @Harry-Chen

## 评论 (2)

### Vedantvijayhumbe · 2026-07-18

hey ! shall I work on this one ? 

### janeyx99 · 2026-07-18

@Vedantvijayhumbe thanks for the interest! I’m currently evaluating the safest for BC/cleanest way to implement the changes, but it’s mostly implemented already. 
