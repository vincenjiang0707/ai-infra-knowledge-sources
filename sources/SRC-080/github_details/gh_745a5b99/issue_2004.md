# [Issue #2004] GPTAQ (ex-GPTQv2) algorithm support

source: https://github.com/vllm-project/llm-compressor/issues/2004
state: closed | updated: 2026-07-12T18:02:28Z
labels: stale

## 正文

I tried to look into the code, can you confirm that GPTAQ (which was also named GPTQv2 at one point) is not a currently supported quantization algorithm.

In that case is there interest to support it? There doesn't seem to require a change on inference servers except maybe for MoE as it requires `asymmetric`.

Paper: https://arxiv.org/pdf/2504.02692
Impl: https://github.com/Intelligent-Computing-Lab-Yale/GPTQv2
Another: https://github.com/ModelCloud/GPTQModel/blob/main/gptqmodel/quantization/gptqv2.py

## 评论 (23)

### kylesayrs · 2025-11-10

Hi @mratsim!

This technique of optimizing towards full precision outputs (ie, computing hessians w.r.t. unquantized inputs) can be implemented using a `propagate_error` argument as follows:

<details>
```python3
propagate_error = False  # False = GPTAQ

for subgraph_index, subgraph in enumerate(subgraphs):
  # prepare tqdm description texts
  calib_desc = f"({subgraph_index + 1}/{num_subgraphs}): Calibrating"
  prop_desc = f"({subgraph_index + 1}/{num_subgraphs}): Propagating"
  
  # reduce memory movement by keeping modules onloaded
  with disable_offloading():
      # do a preliminary pass to trigger modifier hooks
      for batch_idx in tqdm(range(len(dataloader)), desc=calib_desc):
          inputs = activations.fetch(batch_idx, subgraph.input_names)
          outputs = subgraph.forward(model, **inputs)

          if not propagate_error:
              activations.update(batch_idx, outputs)
              activations.delete(batch_idx, subgraph.consumed_names)
  
      LifecycleCallbacks.sequential_epoch_end(subgraph)
  
      # this pass does not trigger modifier hooks
      # and is only used for capturing outputs of newly compressed modules
      with HooksMixin.disable_hooks():
          for batch_idx in tqdm(range(len(dataloader)), desc=prop_desc):
              inputs = activations.fetch(batch_idx, subgraph.input_names)
              output = subgraph.forward(model, **inputs)

              if propagate_error:
                  activations.update(batch_idx, output)
                  activations.delete(batch_idx, subgraph.consumed_names)
```
</details>

It's nice to see that some research has shown that this leads to marginally better returns! We can add this implementation, and if research shows that this is more effective, we can make this option a default.

### kylesayrs · 2025-11-10

Upon second read, there is a difference between the algorithm described by GPTAQ and the `propagate_error argument`.

In a diagram, this is GPTAQ
<img width="471" height="211" alt="Image" src="https://github.com/user-attachments/assets/4edf60e6-9c97-4ff3-94f4-a72844aa601a" />

And this is the `propagate_error` argument.
<img width="471" height="211" alt="Image" src="https://github.com/user-attachments/assets/5b2cd1f9-2e01-4d9e-88a9-f05728de083a" />

This GPTAQ algorithm could be implemented in LLM Compressor, although I have to better understand exactly how its implementation differs from LLM Compressor's current sequential pipeline implementation.

### kylesayrs · 2025-11-10

Seems like this would require changes to the GPTQ algorithm, which could be made by implementing an argument on the GPTQModifier.

https://github.com/Intelligent-Computing-Lab-Panda/GPTAQ/blob/main/fake_quant/gptaq_utils.py#L43

### HDCharles · 2025-11-13

Isn't the bigger issue getting the activations from both runs? Like if we have x going into a model A->B->C, we run x through A, do gptqv2 get A_out and A_quant_out, put both into B ...etc. it's going to be 2x memory and computation. The offloading will be a fixed cost so maybe the performance will not be as bad as 2x but it's still pretty far away from what's currently there no?

### farzadab · 2025-12-23

I see there hasn't been any progress on this recently. I'm new to the repo and I wanted to see if I could switch to it, but the possibility of supporting GPTAQ seems quite important to me.

Since you've looked into this, is it possible to explain a bit whether this is possible in the current repo structure and how one would go about adding it? I know GPTAQ closely but I don't know how `llm-compressor` works.


As @HDCharles mentioned, the main thing I'm worried about is whether the second run can be supported. The original GPTAQ implementation is quite sequential: you quantize one layer, moving all hidden states (quantized and full-precision) forward in tandem. At a glance it seems `llm-compressor` assumes that each batch is handled separately which quite complicates things with memory: unlike the Hessian computation, you can't compute `dXXT` batch-wise before the previous layers are quantized.

### HDCharles · 2026-01-06

1)
 so you're right that our existing GPTQ implementation isn't as sequential as the paper, though i'm not sure you're description is accurate or that's the main problem with implementing GPTAQ

to be precise:

instead of taking a single layer, quantizing it with GPTQ (using the fp activation it got), getting new outputs once the layer is quantized and then moving to the next layer, llm compressor instead uses the sequential pipeline to run several modules together in a chunk, then does GPTQ on each using the fp activation each saw. iirc the next part is disabled by default there's an option to enable it: we then recalculate the output of the chunk using the altered weights from quantization and then progress to the next chunk.

so instead of sequentially doing  A -> B -> C -> D -> E -> F, we're doing (A,B,C) -> (D, E, F) which seems to work in practice and is significantly faster.
(note we've collaborate with the GPTQ authors a significant amount so this approach isn't something random and unverified)

2)
I don't *think* this would prevent GPTAQ from being workable with the sequential pipeline, if GPTQ is acceptable then this chunked approach seems like it would be fine for GPTAQ. Maybe you can expand on this point if you still think thats the problem.

3)
In my mind the main gap is basically that we have to do a few things

we now do:

a) sequential pipeline full precision -> cache
b) GPTQ
c) (option) sequential pipeline fake quantized -> overwrite cache

for GPTAQ we need:

ai)sequential pipeline with inputs from full precisin path -> cache_fp
aii) sequential pipelin with inputs from fake quantized path -> cache_fake_q
b) GPTAQ
c) sequential pipeline with inputs from fake quantized path -> overwrite cache_fake_q

compared to those structural change, the change to the hessian calculation seems fairly small but i may be missing something.

if someone wants to work on this let me know and i can assign you, if i get the bandwidth i may try to take a shot at it but our team is more focused on general sequential pipeline performance improvements in the medium term and in general we've seen more interest in AWQ flows than GPTQ.







### mratsim · 2026-01-06

> in general we've seen more interest in AWQ flows than GPTQ.

That's likely because AWQ is much faster to quantize than GPTQ, especially given that models are now 100+ to 200+ billions of parameters.

That said, I would be keen to explore rotations/hadamard/trellis based quantization methods provided vLLM can run them.

### HDCharles · 2026-01-07

AWQ is wayyyyy slower than GPTQ, and further it should be orthagonal. one thing we're hoping to look into is AWQ+GPTQ but we need to get some other things working first

thus far only AWQ and smoothquant seem to actually be helpful as far as transforms, the rotation based techniques we support (spinquant and quip) see poor results both in our tests and based on findings of our research collaborators. Its one reason for this paper from said collaborators: https://arxiv.org/abs/2509.23202 which is where most of our focus with transforms will likely be going forward but its currently lacking vLLM support for micro rotations.

### mratsim · 2026-01-08

> AWQ is wayyyyy slower than GPTQ, and further it should be orthagonal. one thing we're hoping to look into is AWQ+GPTQ but we need to get some other things working first

That seems to contradict literature, see HQQ: https://dropbox.github.io/hqq_blog/

<img width="574" height="1178" alt="Image" src="https://github.com/user-attachments/assets/0678b086-e96e-4b57-87c2-4a2014f9007f" />

### brian-dellabetta · 2026-01-09

Just FYI, we recently added a `batch_size` to `oneshot` that greatly reduces the amount of time AWQModifier takes to run. I saw more than a 60% reduction in runtime when using `batch_size=32` on Qwen 3 30B. The reduction is less pronounced with other modifiers because the biggest bottleneck for AWQ is running forward passes in a grid search over scales. This may be the culprit for discrepancy in GPTQ/AWQ runtimes

### HDCharles · 2026-01-27

also these models are not MoE models and AWQ especially struggles with MoE

### phaelon74 · 2026-03-11

> Just FYI, we recently added a `batch_size` to `oneshot` that greatly reduces the amount of time AWQModifier takes to run. I saw more than a 60% reduction in runtime when using `batch_size=32` on Qwen 3 30B. The reduction is less pronounced with other modifiers because the biggest bottleneck for AWQ is running forward passes in a grid search over scales. This may be the culprit for discrepancy in GPTQ/AWQ runtimes

I have extensive use with batching and it degrades every model I quanted, even at batch 2.  Were you doing GPTQ, AWQ, or another?

### phaelon74 · 2026-03-11

> also these models are not MoE models and AWQ especially struggles with MoE

I have not seen this, and my graph would show otherwise, that QuantTrio obtained an insane KLD, on AWQ for Qwen3.5-397B.  For your statement, how does this manifest?

<img width="1763" height="1031" alt="Image" src="https://github.com/user-attachments/assets/c40ea206-9b30-4599-b081-e97901dc5b23" />


### HDCharles · 2026-03-11

> > Just FYI, we recently added a `batch_size` to `oneshot` that greatly reduces the amount of time AWQModifier takes to run. I saw more than a 60% reduction in runtime when using `batch_size=32` on Qwen 3 30B. The reduction is less pronounced with other modifiers because the biggest bottleneck for AWQ is running forward passes in a grid search over scales. This may be the culprit for discrepancy in GPTQ/AWQ runtimes
> 
> I have extensive use with batching and it degrades every model I quanted, even at batch 2. Were you doing GPTQ, AWQ, or another?

can you raise a separate issue for this, thats a very surprising result

### HDCharles · 2026-03-11

we're talking about time to quantize the model, no KLD or accuracy

### phaelon74 · 2026-03-11

> we're talking about time to quantize the model, no KLD or accuracy

Right on, thanks for the context.  So it's a time to quant, where you see AWQs struggle.  I have noticed "some" struggle in AWQ and others have no issue.  GLM4.6 took FOREVER, but GLM4.7 sailed smoothly.  I also had my modeling file for GLM4.7 so that might have helped a lot too.

### phaelon74 · 2026-03-11

> > > Just FYI, we recently added a `batch_size` to `oneshot` that greatly reduces the amount of time AWQModifier takes to run. I saw more than a 60% reduction in runtime when using `batch_size=32` on Qwen 3 30B. The reduction is less pronounced with other modifiers because the biggest bottleneck for AWQ is running forward passes in a grid search over scales. This may be the culprit for discrepancy in GPTQ/AWQ runtimes
> > 
> > 
> > I have extensive use with batching and it degrades every model I quanted, even at batch 2. Were you doing GPTQ, AWQ, or another?
> 
> can you raise a separate issue for this, thats a very surprising result

I can try sure, I'll have to dig my scripts back out again.  At batch size 16 or 32 degradation was massive.  KLD off by .10-.15 in some extreme cases.  For 2-8, I seemed to see behaviors that saw KLD slide by 0.02-4 which was substantially enough for me to notice it, anecdotally when using the model.  I'll go back to my notes.

### HDCharles · 2026-03-11

There should be no difference to the results based on batch size we tested eval accuracy and got within margin of error so yeah that'd be a big bug.

### brian-dellabetta · 2026-03-12

> > Just FYI, we recently added a `batch_size` to `oneshot` that greatly reduces the amount of time AWQModifier takes to run. I saw more than a 60% reduction in runtime when using `batch_size=32` on Qwen 3 30B. The reduction is less pronounced with other modifiers because the biggest bottleneck for AWQ is running forward passes in a grid search over scales. This may be the culprit for discrepancy in GPTQ/AWQ runtimes
> 
> I have extensive use with batching and it degrades every model I quanted, even at batch 2. Were you doing GPTQ, AWQ, or another?

@phaelon74 the only reason i could think this would be an issue is if your calibration dataset is not the same length. in that case it either truncates or pads depending on what you set as `data_collator` field in oneshot (defaults to "truncation"). Are you using samples with all the same sequence length?

### HDCharles · 2026-03-12

oh yeah thats a good point, if we're truncating/padding that would change the numerics, it shouldn't be a ton though

### phaelon74 · 2026-03-13

> > > Just FYI, we recently added a `batch_size` to `oneshot` that greatly reduces the amount of time AWQModifier takes to run. I saw more than a 60% reduction in runtime when using `batch_size=32` on Qwen 3 30B. The reduction is less pronounced with other modifiers because the biggest bottleneck for AWQ is running forward passes in a grid search over scales. This may be the culprit for discrepancy in GPTQ/AWQ runtimes
> > 
> > 
> > I have extensive use with batching and it degrades every model I quanted, even at batch 2. Were you doing GPTQ, AWQ, or another?
> 
> [@phaelon74](https://github.com/phaelon74) the only reason i could think this would be an issue is if your calibration dataset is not the same length. in that case it either truncates or pads depending on what you set as `data_collator` field in oneshot (defaults to "truncation"). Are you using samples with all the same sequence length?

You are a genius @brian-dellabetta .  This is 100% it (@HDCharles ).  I did batching size 2/4 on a dataset that was the same length, and saw no issues.  Expanded to 8/16/32 on my master dataset which has lots of stuff in it.  That's where I then saw degradation.  As soon as this NVFP4 finishes QADing I will rerun this to confirm it was this.  Thanks again gents!!

### github-actions[bot] · 2026-06-11

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!

### github-actions[bot] · 2026-07-12

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant. Thank you!
