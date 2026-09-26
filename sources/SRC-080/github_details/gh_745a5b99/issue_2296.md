# [Issue #2296] [AWQ] add option to take smooth layer quantization into accout

source: https://github.com/vllm-project/llm-compressor/issues/2296
state: closed | updated: 2026-08-21T17:34:30Z
labels: enhancement, good first issue, awq, stale

## 正文

normally the way AWQ works is to pick a layer that is going to be quantized, try a bunch of scale factors to find the one that minimizes quantization error when that layer is quantized and then do an [inverse rescale](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/awq/base.py#L520) on the preceeding layer which is normally not quantized. However a problem arises for the [up_proj -> down_proj](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/awq/mappings.py#L51-L54) mapping
because both the smooth and balance layers are targeted for quantization. Since we only take into account the quantization of the balance layers in our current AWQ implementation, we could be making the smooth layer harder to quantize with our choice of scale factor for the balance layer since the smooth layer is basically ignored during the quantization error calculation for quantizing the balance layer.

We should

1) test if this has a significant impact
2) add an option to enable this feature if its beneficial

STEPS

A) add a check [here](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/awq/base.py#L378) for whether smooth_name is in targeted_names and if so, change the get_lowest_common...etc search to include the smooth layer (this is how we determine what module is run to determine the quantization error, so we need smooth layer to be run if we're taking its quantization into accout)
B) add a flag to [compute_best_scale](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/awq/base.py#L567) for if the smooth layer is targeted
C) if necessary add the smooth layer to [this dict](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/awq/base.py#L497)
D) move [the rescale weight code](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/modifiers/awq/base.py#L664-L696) into a function which is called for each balance layer
E) if necessary, call the rescale weight code for 1/_scalesview on the smooth_layer
F) check whether this has an impact on lm_eval performance on some small set of models.
G) check how this affects the runtime of AWQ for those models.

if its beneficial then put up a PR with those changes demonstrating what was tested and how it affects things.

## 评论 (10)

### Etelis · 2026-01-27

Assign me here as well

### Ramshankar07 · 2026-01-27

Can I work on it @Etelis , I'm eager to learn and contribute 

### Etelis · 2026-01-27

@Ramshankar07 Sure go ahead.

### Etelis · 2026-01-27

I'd wait a bit for me to finish running tests to see if it is beneficial (#2295  

### Ramshankar07 · 2026-01-27

Sure thing, Let me know

### HDCharles · 2026-01-27

this is all dealing with the same type of thing but in orthagonal ways. even if https://github.com/vllm-project/llm-compressor/issues/2295 isn't important this one could be. 

They're all kind of heuristic ways of turning the joint problem 
$\min_{s1,s2} Loss(MLP(X,W1,W2) - MLP(X/s1,Q(s1 * W1)/s2, Q(s2 * W2)))$

into 2 disjoint problems $\min_{s1} Loss(MLP(X,W1,W2) - MLP(X/s1,Q(s1 * W1), W2))$ and $\min_{s2} Loss(MLP(X,W1,W2) - MLP(X/s1,s1 * W1/s2, Q(s2 * W2)))$

2295 deals with the ordering, since it makes more sense to look at $Q(\frac{s1 * W1}{s2})$ rather than $\frac{Q(s1 * W1)}{s2}$ whereas this one deals with taking some of problem 2 and taking it into account in problem 1. So it'd be mroe like

$\min_{s1} Loss(MLP(X,W1,W2) - MLP(X/s1,Q(s1 * W1), W2))$ and $\min_{s2} Loss(MLP(X,W1,W2) - MLP(X/s1,\textcolor{red}{Q(}s1 * W1/s2), Q(s2 * W2)))$

i'll assign you @Ramshankar07 

### Ramshankar07 · 2026-01-27

Thanks, @HDCharles. The provided steps are very elaborate for me to check. I'll start a PR in couple of hours.

### qubeena07 · 2026-04-22

Hi @HDCharles @Ramshankar07, Is this still being actively worked on? Happy to take it over if not. Plan to implement steps A–G as outlined above.

### github-actions[bot] · 2026-07-21

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### github-actions[bot] · 2026-08-21

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant. Thank you!
