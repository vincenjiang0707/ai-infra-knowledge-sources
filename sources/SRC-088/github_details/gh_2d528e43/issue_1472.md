# [Issue #1472] evaluation extremely slow with llama_cpp/gguf

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/1472
state: open | updated: 2026-07-30T03:12:07Z
labels: bug

## 正文

Evaluation of gguf models via llama_cpp server is extremely slow. All the layers are offloaded to the GPU so normally it should work fine, but truthfulqa takes 10 hours, it should normally take ~40 minutes or even less.
`lm_eval --model gguf --model_args base_url=http://localhost:8000 --batch_size 16 --tasks truthfulqa_mc2 --num_fewshot 0`


## 评论 (6)

### Andy1314Chen · 2024-02-27

> Note that for externally hosted models, configs such as --device and --batch_size should not be used and do not function. 

i have the same problem. What can I do to make it support batch processing？？

### linotfan · 2024-02-27

It seems to be an [issue ](https://github.com/ggerganov/llama.cpp/discussions/229)with llama.cpp.

### mobicham · 2024-02-27

> It seems to be an [issue ](https://github.com/ggerganov/llama.cpp/discussions/229)with llama.cpp.

So basically they say it's a problem with quantized models running with large prompts. 
That sounds strange because the impact of the dequantization step should actually matter much less with longer prompts and larger batches sizes.  


### tcofala · 2024-07-09

Hey,
Is there anything new on this topic. I am experiencing the same problems when evaluating a local llama.cpp server hosting a GGUF.

### baberabb · 2024-08-21

So I'm looking into our current implementation and looks like it's wrong for logliklihood/multiple-choice tasks as the llama.ccp server does not as yet return the logprobs of the prompt. Theres an open issue [here](https://github.com/ggerganov/llama.cpp/issues/8942). 

Looking into alternates. Whats the usual way people load gguf models? I'm trying [llama-ccp-python](https://github.com/abetlen/llama-cpp-python) (they also have a server implementation) but can't seem to get it working in my environment.


### snailwei · 2026-07-30

It's really too slow with enough GPU, the 2xA100/80G for running a `DavidAU/Qwen3.6-27B-Fable-Fusion-711-Uncensored-Heretic-NM-DAU-NEO-MAX-MTP-GGUF` is too slow, half of the GPU RAM was not used at all even with `--gpu-layers all`,  the kvcache barely dose not work!
