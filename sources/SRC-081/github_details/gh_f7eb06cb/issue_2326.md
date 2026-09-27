# [Issue #2326] Module placement for `BALANCED` VramStrategy flawed

source: https://github.com/ModelCloud/GPTQModel/issues/2326
state: closed | updated: 2026-04-13T07:44:33Z
labels: performance, bug: non-breaking

## 正文

@Qubitium I have tried to use Balanced strategy for distributing non-moe modules between devices and encountered a bug.
When `VramStrategy` is `Balanced` - during forward pass of a `moe_subset` - (or let's say subset having non-empty `forward_device_map`) - the modules from previous subset are placed on devices that were chosen for quantization in round-robin way (see `_prepare_named_module_for_quantization` and `_assign_quant_device_for_module`). The relevant lines from log:
1. after self_attn.o_proj - when moe forward pass - o_proj appeared on cuda:3
```
INFO  HookedLinear forward: module='model.layers.0.self_attn.q_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.self_attn.k_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.self_attn.v_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.self_attn.o_proj' weight_device=cuda:0 input_device=cuda:0
INFO  gc.collect() reclaimed 0 objects in 0.152s
INFO  | gptq    | 0     | self_attn.o_proj          | 4096, 2048    | bf16: 18.0MB | 0.0000000993 | 80      | 0.01000 | 0.880 | 0.110    | cuda 1.69G, 0.4G, 0.4G, 0.82G |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+----------+-------------------------------+---------+
INFO  gc.collect() reclaimed 44 objects in 0.157s
INFO  HookedLinear forward: module='model.layers.0.self_attn.q_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.self_attn.k_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.self_attn.v_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.self_attn.o_proj' weight_device=cuda:3 input_device=cuda:0
```
2. after moe up/down - the o_proj still on cuda:3, and moe up/gate are distributed (probably in round robin way to devices for quantization and remains there)
```
INFO  | gptq    | 0     | mlp.experts.105.up_proj   | 2048, 768     | bf16: 3.4MB  | 0.0003003296 | 5       | 0.01000 | 0.873 | 1.531    | cuda 2.63G, 1.47G, 1.67G, 1.57G |         |
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+----------+---------------------------------+---------+
INFO  gc.collect() reclaimed 5244 objects in 0.186s
INFO  HookedLinear forward: module='model.layers.0.self_attn.q_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.self_attn.k_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.self_attn.v_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.self_attn.o_proj' weight_device=cuda:3 input_device=cuda:0
INFO  HookedLinear forward: module='None' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.mlp.experts.0.gate_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.mlp.experts.0.up_proj' weight_device=cuda:3 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.mlp.experts.0.down_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.mlp.experts.1.gate_proj' weight_device=cuda:1 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.mlp.experts.1.up_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.mlp.experts.1.down_proj' weight_device=cuda:0 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.mlp.experts.2.gate_proj' weight_device=cuda:2 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.mlp.experts.2.up_proj' weight_device=cuda:1 input_device=cuda:0
INFO  HookedLinear forward: module='model.layers.0.mlp.experts.2.down_proj' weight_device=cuda:0 input_device=cuda:0
```

I have used 1 calibration sample and qwen3-coder-30b-a3b-instruct model to reproduce.
I have added log into HookedLinear:
```
         self.forward_hook = None
         self.forward_hook_last = False
+        self.module_name = None  # For logging purposes
...
     def forward(self, input: torch.Tensor) -> torch.Tensor:
         original_device = input.device
         target_device = self.weight.data.device
+        
+        # Log module placement
+        module_name = getattr(self, "module_name", getattr(self, "full_name", getattr(self, "name", "unknown")))
+        log.info(f"HookedLinear forward: module='{module_name}' weight_device={target_device} input_device={original_device}")
+        
         if original_device != target_device:
             input = input.to(device=target_device)
         output = super().forward(input)
```
and to NamedModule:
```
diff --git a/gptqmodel/looper/named_module.py b/gptqmodel/looper/named_module.py
index 5d8bd2a6..10fe136a 100644
--- a/gptqmodel/looper/named_module.py
+++ b/gptqmodel/looper/named_module.py
@@ -31,6 +31,10 @@ class NamedModule(torch.nn.Module):
         self.layer_index = layer_index  # layer index for repeated blocks
         self._parent_lock = get_parent_lock(full_name)
         
+        # Set module_name on HookedLinear for logging purposes
+        if hasattr(module, 'module_name') and module.module_name is None:
+            module.module_name = full_name
+
         # persistent work state for named module (used by some LoopProcessors)
         # store all `processed()` work state/data/result here
         self.state = {}
```

[_log_qwen_balanced_forward_device_retain_from_quantization.txt](https://github.com/user-attachments/files/24406780/_log_qwen_balanced_forward_device_retain_from_quantization.txt)

## 评论 (4)

### avtc · 2026-01-06

@Qubitium 

Expected result for modules to be placed back after quantization - for the self_attn_o to the cuda:0, for moe modules to the place where they were assigned for forward pass.

The issue appear only when `forward_device_map` is non empty.

### Qubitium · 2026-01-08

@avtc  This is issue is on-hold while we fix more pressing bug fixes. Will get back to this performance issue after. 

### Qubitium · 2026-03-31

@avtc Is this issue still valid after merging your pr?

### avtc · 2026-03-31

@Qubitium 
Issue still valid, it is about placement modules, my pr was about placement calibration data.
