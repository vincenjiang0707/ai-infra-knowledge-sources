# [Issue #20] Great work!

source: https://github.com/LLMServe/DistServe/issues/20
state: open | updated: 2024-07-16T08:27:01Z
labels: 

## 正文

Congratulations, great work!
I'm wondering if you guys will continue to develop the framework to reach vllm scale.
If so, please share some docs/roadmaps about system architecture design to the community, so everyone can help to contribute

## 评论 (2)

### irasin · 2024-07-05

BTW，given the same model and sampling_params, I found the generated results of DistServe is different from vllm.

I tested the model `meta-llama/Llama-2-7b-hf` on the NV A10 GPUs with the sampling params as below

```python
sampling_params = SamplingParams(temperature=0, ignore_eos=True, max_tokens=64)
```

the prompt is
```python
"Simply put, the theory of relativity states that ",
```

vllm result:
```text
1) the speed of light is constant in all inertial reference frames, and 2) the laws of physics are the same for all inertial reference frames.
The theory of relativity is a theory of physics that describes the relationship between space and time. It is based on the principle that the speed
```

DistServe result:
```text
1) the speed of light is the same for all observers in an inertial frame of reference is not a constant.
The speed of light is the same for all observers.
The speed of light is the same for all observers.
The speed of light is the same for all observers
```

Is there something wrong here?


### irasin · 2024-07-16

@interestingLSY @GindaChen 
