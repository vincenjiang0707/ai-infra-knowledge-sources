# [Issue #2271] [BUG] Quantized MoE model can't be loaded by vLLM

source: https://github.com/ModelCloud/GPTQModel/issues/2271
state: closed | updated: 2025-12-23T09:17:04Z
labels: bug

## 正文

**Describe the bug**

When quantize a MoE model, if an expert is not activated, it will be retained at its original data type. This is not compatible with VLLM and other inference engines that use FuseMoE layer. It is strongly recommended to modify this behavior, for example, if an expert is not activated, just perform RTN quant by setting their Hessian matrix as the identity matrix.

**GPU Info**

Show output of:

```
nvidia-smi
```

**Software Info**

Operation System/Version + Python Version

Show output of:
```
pip show gptqmodel torch transformers accelerate triton
```

**If you are reporting an inference bug of a post-quantized model, please post the content of `config.json` and `quantize_config.json`.**

**To Reproduce**

How to reproduce this bug if possible.

**Expected behavior**

A clear and concise description of what you expected to happen.

**Model/Datasets**

Make sure your model/dataset is downloadable (on HF for example) so we can reproduce your issue.

**Screenshots**

If applicable, add screenshots to help explain your problem.

**Additional context**

Add any other context about the problem here.


## 评论 (7)

### mratsim · 2025-12-21

The proper solution is to ensure all experts are activated, otherwise quality will be seriously degraded with RTN for use-cases not in calibration data (and with say 64 samples and 128 experts ....).

See:
- https://github.com/ModelCloud/GPTQModel/pull/2235
- https://huggingface.co/cyankiwi/MiMo-V2-Flash-AWQ-4bit/discussions/1#69451d4d0763d2e04cc592d2

### Qubitium · 2025-12-22

@mratsim  In addition to the PR you mentioned, https://github.com/ModelCloud/GPTQModel/pull/2293 will also be merged that does a better job at `rtn` so that moe modules can be quantized naively via simple weight only and calibration-less. 

I personally believe that if the MoE is only activated less than 1% of the time for ALL known input, the problem is moe training bias for that module. That module might be close to be useless in real inference, but we will need it to be not corrupt output. 

### mratsim · 2025-12-22

> I personally believe that if the MoE is only activated less than 1% of the time for ALL known input, the problem is moe training bias for that module. That module might be close to be useless in real inference, but we will need it to be not corrupt output. 

But people are only passing 64~512 samples when calibrating maybe 8K at most with usually 2048 sequence length.

The calibration data is often English-only,  it may contains math, code (often Python-only), some wikipedia stuff. That's really underwhelming compared to  all the languages that people speak, the world knowledge and the specialization domains that out there.

In the worst case, with REAP the model just becomes lobotomized: see https://huggingface.co/cerebras/GLM-4.6-REAP-268B-A32B/discussions/1 where Bill Clinton has been removed from the LLM world knowledge.




### Qubitium · 2025-12-22

> 
> But people are only passing 64~512 samples when calibrating maybe 8K at most with usually 2048 sequence length.

I am saying that some moe modules are activates so in frequently, it is a training bug. I have throw 1 million plus tokens at a model and not a single token got routed  to a module. 

> In the worst case, with REAP the model just becomes lobotomized: see https://huggingface.co/cerebras/GLM-4.6-REAP-268B-A32B/discussions/1 where Bill Clinton has been removed from the LLM world knowledge.

reap is meant trade performance for hacking knowledge for some down stream tasks so this does not surprise me with how reap works.

for example, if you want glm to do only coding tasks, forgetting about bill Clinton  maybe a good tradeoff.


### mratsim · 2025-12-22

> I am saying that some moe modules are activates so in frequently, it is a training bug. I have throw 1 million plus tokens at a model and not a single token got routed to a module.

1M is 0.00001% of 10T and models are now trained on even more, I don't think we can conclude anything from that small a sample.

### Qubitium · 2025-12-23

> > I am saying that some moe modules are activates so in frequently, it is a training bug. I have throw 1 million plus tokens at a model and not a single token got routed to a module.
> 
> 1M is 0.00001% of 10T and models are now trained on even more, I don't think we can conclude anything from that small a sample.

I think we are talking about different things there. I am just saying MoE modules does not have to have extreme routing bias which result in some random module in some random layer having close to 0.0000000% activations. Many moe models do not have this problem. Some do, some don't. I believe for those that don't, the model trainers are well aware and deliberately, and correctly, make sure the routing does not have have extreme bias and opt of more balanced routing. 


### Qubitium · 2025-12-23

@Sekri0  Closing as we have completed this task in:

https://github.com/ModelCloud/GPTQModel/pull/2293
https://github.com/ModelCloud/GPTQModel/pull/2302

We have pending PR to enhance this but post-quantizatino eval testing has shown the new `FailSafe` control, now auto-enabled for all models has neglible effect if the moe model has extreme routing bias where very few modules are rarely activated. You can check the config for control when and how it is triggered.
