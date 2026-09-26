# [Issue #198] How to Get Overall Benchmark Results for New Model

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/198
state: open | updated: 2026-03-11T20:59:40Z
labels: 

## 正文

### Context

I used the kernel_generator (based on `examples/kernel_generator`) with FlashInfer-Bench’s definitions to generate optimized solutions for a new model (e.g., Gemini-3.1-pro, GPT-5.2). Solutions are saved under `flashinfer-trace/solutions/<author>/<op_type>/<definition_name>/`. I then ran:

```bash
flashinfer-bench run --local /path/to/flashinfer-trace
```

### Question

**How do I compute the overall benchmark correctness rate and speedup for the generated solutions?**


### What I tried

1. **`flashinfer-bench report summary`**  

   ```bash
   flashinfer-bench report summary --local /path/to/flashinfer-trace
   ```
    But nothing shows.

2. **`flashinfer-bench report visualize`**  
  
  ```bash
   flashinfer-bench report visualize --local /path/to/flashinfer-trace
   ```
    
I hit an error :
   ```text
   AttributeError: 'Evaluation' object has no attribute 'get'
   ```


## 评论 (2)

### Ubospica · 2026-02-27

We will add accumulate score in report summary soon. cc @YiyanZhai 

### YiyanZhai · 2026-03-11

This PR (https://github.com/flashinfer-ai/flashinfer-bench/pull/213) added the ranking to summary cli.
