# [Issue #63] KernelBench Format Support

source: https://github.com/meta-pytorch/KernelAgent/issues/63
state: open | updated: 2025-12-15T20:44:00Z
labels: enhancement

## 正文

## Problem

The Fuser outputs `kernel_function(...)` with arguments that don't have a 1:1 mapping to the original Model's parameters. Static/heuristic mapping fails for:

- Fused operations (Conv+BN → fused_weight, fused_bias)
- Reordered arguments
- Computed intermediates
- Non-obvious naming conventions

## Solution: LLM Mapping Step

Add a new pipeline step that uses an LLM to generate the argument mapping by inspecting:

1. Original KernelBench problem (Model class, get_inputs, get_init_inputs)
2. Generated composed kernel (kernel_function signature)
3. Subgraphs metadata (operation fusion info)

## Pipeline

```
extract → dispatch → compose → map_kernelbench (LLM) → format_kernelbench
```

## LLM Mapping Step

**Input to LLM:**
- Original Model code
- kernel_function signature + implementation
- Subgraph fusion information

**Output from LLM:**
```json
{
  "args": [
    {"kernel_arg": "x", "source": "input", "expr": "inputs[0]"},
    {"kernel_arg": "weight", "source": "param", "expr": "model.conv.weight"},
    {"kernel_arg": "fused_bias", "source": "computed", "expr": "fuse_conv_bn_bias(model)"}
  ],
  "helpers_needed": ["fuse_conv_bn_weights"],
  "notes": "BN folded into conv, need to fuse weights at load time"
}
```

## Format Step

Takes the LLM-generated mapping and produces final `kernelbench_model.py`:

- Generates `ModelNew.__init__` with correct parameter registration
- Generates `forward()` that calls kernel_function with mapped args
- Includes any helper functions (weight fusion, etc.)

## Why This Works or it should 

1. **LLM understands the transformation** - it can read both sides and reason about the correspondence, it will be extremely hard for static method 
2. **Handles edge cases** - fused weights, reordered args, computed values
3. **Produces explicit mapping** - debuggable, auditable
4. **Reuses existing infrastructure** - same LLM dispatch pattern as kernel generation

## Verification

After generation, run:

```python
original_out = Model(*init_inputs).forward(*inputs)
new_out = ModelNew(*init_inputs).forward(*inputs)
assert torch.allclose(original_out, new_out, rtol=1e-3)
```

If verification fails, can re-run mapping step with error feedback.

## Implementation Scope

1. `kernelbench_mapping.j2` - prompt template for LLM mapping
2. `Fuser/kernelbench_mapper.py` - calls LLM, parses mapping JSON
3. `Fuser/kernelbench_formatter.py` - applies mapping to generate final code
4. Pipeline integration via `--output-format kernelbench` flag

---

## Prompt Template

```jinja2
You are analyzing a Triton kernel generated from a PyTorch model to create an argument mapping.

## Original PyTorch Model

```python
{{ original_model_code }}
```

## Generated Triton Kernel

```python
{{ kernel_function_code }}
```

## Subgraph Info

{{ subgraph_info }}

## Task

Analyze how `kernel_function` arguments map to the original Model's parameters and inputs.

Output a JSON mapping:

```json
{
  "args": [
    {
      "kernel_arg": "<argument name in kernel_function>",
      "source": "input|param|buffer|computed",
      "expr": "<Python expression to get value from Model instance or inputs>"
    }
  ],
  "weight_fusion": {
    "needed": true|false,
    "description": "<what fusion is needed, e.g., Conv+BN weight folding>"
  },
  "forward_inputs": ["<list of forward() parameter names>"]
}
```

Rules:
- `source: "input"` → comes from forward() arguments, expr like `x` or `inputs[0]`
- `source: "param"` → comes from model parameter, expr like `self.conv.weight`
- `source: "buffer"` → comes from model buffer, expr like `self.bn.running_mean`
- `source: "computed"` → requires computation, expr like `self.fused_weight` (will be precomputed)

For fused operations (e.g., Conv+BN), identify which weights need to be fused at load time.

Output only valid JSON, no explanation.
```
---

## Example Usage

```bash
# Full pipeline with KernelBench output
python -m Fuser.pipeline \
    --problem /path/to/kernelbench/level2/problem.py \
    --output-format kernelbench \
    --verify

# Standalone mapping step
python -m Fuser.kernelbench_mapper \
    --problem /path/to/problem.py \
    --composed-kernel /path/to/composed.py \
    --subgraphs /path/to/subgraphs.json \
    --output /path/to/mapping.json
```

## 评论 (1)

### Jack-Khuu · 2025-12-15

This seems reasonable to me. Unlikely to affect perf, but would help OOTB usability 

@Laurawly 
