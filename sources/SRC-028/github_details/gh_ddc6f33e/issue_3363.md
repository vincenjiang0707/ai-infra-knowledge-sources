# [Issue #3363] [Bug] Tunix GRPO VllmRollout.get_per_token_logps API mismatch and JAX concatenate type error

source: https://github.com/AI-Hypercomputer/maxtext/issues/3363
state: open | updated: 2026-04-17T21:06:46Z
labels: bug

## 正文

### Bug report

When running a full end-to-end GRPO training pipeline using VllmRollout on a TPU v5e-8 slice, the rollout engine crashes during the first micro-batch step due to two consecutive API mismatches between tunix/rl/rl_cluster.py and tunix/rl/rollout/vllm_rollout.py.

**Issue 1: Unexpected Keyword Argument completion_mask**
RLCluster.get_old_per_token_logps passes a completion_mask argument down to the rollout engine, but the VllmRollout.get_per_token_logps method signature does not accept it.

**Traceback:**

```
File "/usr/local/lib/python3.12/site-packages/tunix/rl/grpo/grpo_learner.py", line 267, in _generate_and_compute_advantage
    old_per_token_logps = self.rl_cluster.get_old_per_token_logps(...)
TypeError: VllmRollout.get_per_token_logps() got an unexpected keyword argument 'completion_mask'
```

**Issue 2: JAX concatenate Strict Type Error**
If the completion_mask issue is bypassed, the pipeline immediately crashes on the output. VllmRollout returns native Python lists, but rl_cluster.py passes them directly to jnp.concatenate(). Under strict JAX versions (like 0.4.25), this throws a TypeError because it expects array-like objects, not lists.

**Traceback:**
```
Python
File "/usr/local/lib/python3.12/site-packages/tunix/rl/rl_cluster.py", line 993, in get_old_per_token_logps
    per_token_logps = jnp.concatenate(outs, axis=0)
TypeError: concatenate requires ndarray or scalar arguments, got <class 'list'> at position 0.
```

### Logs/Output

_No response_

### Environment Information

**Environment:**

Hardware: GKE TPU v5e-8 slice

JAX Version: 0.4.25 (Pinned to maintain mesh stability with with_sharding_constraint)

vLLM Version: 0.17.0rc1

Algorithm: GRPO

### Additional Context

_No response_

## 评论 (3)

### karajendran · 2026-03-11

**Context:**
While scaling up GRPO to use rl.num_generations=8 with vLLM on TPU v5e, the training loop crashed during the advantage calculation with this exact error:
TypeError: sub got incompatible shapes for broadcasting: (8, 768), (8, 0).

**Root Cause:**
When the actor model generates its per_token_logps, it outputs a perfect rigid JAX shape (e.g., (8, 768)). However, if vLLM hits an early <EOS> token during rollout, it stops generating and returns a ragged list of varying lengths. When strict JAX versions attempt to parse this ragged list into an array, it collapses the inconsistent dimension to 0, resulting in the (8, 0) shape that instantly kills the GRPO subtraction math.

**The Workaround:**
A dynamic patch that intercepts the completion_mask passed into get_per_token_logps and uses it as a blueprint to dynamically pad (or truncate) vLLM's ragged output with zeros. This forces the data into a perfectly rigid array before JAX attempts the subtraction.

```
# --- Replace the old tunix import with this ---
from maxtext.inference.vllm_decode import VllmRollout

# 1. Save the original method 
original_get_logps = VllmRollout.get_per_token_logps

def patched_get_per_token_logps(self, *args, **kwargs):
    # Fix A: Intercept the mask to use as a blueprint
    completion_mask = kwargs.pop('completion_mask', None)
    
    # Call the actual vLLM execution
    results = original_get_logps(self, *args, **kwargs)
    
    # Extract target length (defaults to 768 if mask is missing)
    target_len = completion_mask.shape[-1] if completion_mask is not None else 768
    
    def pad_sequence(seq):
        seq_arr = jnp.array(seq)
        
        # If vLLM returned an empty array, return a zeroed array of correct shape
        if seq_arr.size == 0:
            return jnp.zeros(target_len)
            
        # Pad with zeros if too short, or truncate if too long
        pad_amount = target_len - seq_arr.shape[0]
        if pad_amount > 0:
            return jnp.pad(seq_arr, (0, pad_amount), constant_values=0.0)
        elif pad_amount < 0:
            return seq_arr[:target_len] 
        return seq_arr

    # Fix B: Process ragged lists and perfectly pad them into a rigid JAX block
    if isinstance(results, list):
        padded_results = [pad_sequence(seq) for seq in results]
        return jnp.stack(padded_results)
        
    elif isinstance(results, dict):
        return {k: jnp.stack([pad_sequence(seq) for seq in v]) if isinstance(v, list) else v for k, v in results.items()}
        
    return results

# 2. Apply the patch
VllmRollout.get_per_token_logps = patched_get_per_token_logps
```

This worked for me.

### RissyRan · 2026-03-30

@A9isha Could you help take a look or triage? Thanks!

### JiwaniZakir · 2026-04-17

Two distinct but related issues here. The `completion_mask` mismatch in `VllmRollout.get_per_token_logps` suggests the interface contract between `rl_cluster.py` and the rollout backends drifted — likely `RLCluster.get_old_per_token_logps` was updated to pass `completion_mask` for masking padding tokens in log-prob computation, but `VllmRollout` was never updated to match the new signature (whereas other rollout implementations may have been). The second error (`concatenate requires ndarray or scalar arguments`) is a downstream consequence of `VllmRollout.get_per_token_logps` returning plain Python lists rather than JAX arrays — JAX 0.4.25 enforces stricter type requirements for `jnp.concatenate` than some earlier versions, so wrapping each element with `jnp.array(out)` before concatenation in `rl_cluster.py` line 993, or having `VllmRollout` return stacked JAX arrays directly, would resolve it. The cleanest fix is to align `VllmRollout.get_per_token_logps` to accept and use `completion_mask` (applying it to zero out non-completion token log-probs) and ensure its return type is a JAX array consistent with what other rollout backends return.
