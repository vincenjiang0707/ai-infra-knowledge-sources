# [Issue #451] [Usage] Per-strategy max_requests constraints not respected in Sweep Mode

source: https://github.com/vllm-project/guidellm/issues/451
state: closed | updated: 2026-07-01T21:58:17Z
labels: feature, cli

## 正文

**Describe the bug**  
When using Sweep Mode with a custom profile that specifies a list of `max_requests` values under `constraints`, all sub-strategies appear to use the same `max_requests` value instead of the respective value from the list.

**Purpose / Expected Behavior**  
I would like to assign a different `max_requests` value to each strategy generated during a sweep (e.g., for fine-grained control over benchmark duration or resource usage per point in the sweep).

**Environment**  
- GuideLLM version: 0.4.0-dev
- Python version: 3.12
- Backend: vLLM 

**To Reproduce**  
1. Clone and install GuideLLM:
   ```bash
   git clone https://github.com/vllm-project/guidellm.git
   cd guidellm
   pip install -e .
   ```

2. Create a profile file `myProfile.json`:
   ```json
   {
     "profile": {
       "type_": "sweep",
       "sweep_size": 5,
       "constraints": {
         "max_requests": [10, 100, 100, 100, 100]
       }
     },
     "target": "http://localhost:8000",
     "data": [
       "prompt_tokens=512,prompt_tokens_stdev=128,prompt_tokens_min=1,prompt_tokens_max=1024,output_tokens=256,output_tokens_stdev=64,output_tokens_min=1,output_tokens_max=1024"
     ],
     "output_formats": ["benchmarks_json.html"]
   }
   ```

3. Run the benchmark:
   ```bash
   guidellm benchmark run --scenario src/guidellm/benchmark/scenarios/myProfile.json
   ```

**Observed Behavior**  
All five sweep strategies show the same `max_requests` value (all use 10), as shown in the output table:

![Sweep strategies all using same max_requests](https://github.com/user-attachments/assets/aba4ee4d-4e39-4c82-9b57-7087920c49b1)

This suggests the per-strategy constraint in `constraints.max_requests` is not being applied correctly.



**Additional Context**  
- Is the `constraints` field documented for per-strategy configuration in sweep mode?  

## 评论 (3)

### markurtz · 2025-11-19

Thanks @AiKiAi-stack, adding this on as a general feature request. Let us know if you're interested in contributing/working on it, otherwise we'll work on getting this typed up and added to the roadmap

### AiKiAi-stack · 2025-11-20

Thanks! Yes, I'm interested in contributing and would like to work on this feature. 

### sjmonson · 2025-11-24

See also #253
