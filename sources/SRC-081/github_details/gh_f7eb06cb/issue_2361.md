# [Issue #2361] Qwen3-Coder-30B-A3B 24g vram awq AssertionError probably due to offloading

source: https://github.com/ModelCloud/GPTQModel/issues/2361
state: closed | updated: 2026-01-19T01:25:30Z
labels: bug

## 正文

When using AWQ for quantizing Qwen3-Coder-30B-A3B on 4090 (24g vram):
```python
config = QuantizeConfig(
    quant_method='awq',
    sym=False,
    offload_to_disk=False,
    true_sequential=True,
    vram_strategy='balanced',
    dynamic={r'-:.*mlp\.gate$':{},r'-:.*mlp\.shared_expert_gate$':{}}
)
ds = load_dataset('codeparrot/self-instruct-starcoder', split='curated[:5120]').shuffle().select(range(int(getenv('N', 512))))
model = GPTQModel.load('Qwen/Qwen3-Coder-30B-A3B-Instruct', config)
tok = AutoTokenizer.from_pretrained('Qwen/Qwen3-Coder-30B-A3B-Instruct')
model.quantize(ds.map(lambda i: {'input_ids': tok.apply_chat_template([
    {'role': 'user', 'content': i['instruction'].strip()},
    {'role': 'assistant', 'content': i['output'].strip()}
], tokenize=True)}, remove_columns=('instruction', 'output', 'most_similar', 'avg_similarity_score')), batch_size=1)
```
I don't have the full output now. But this is the error when running half-way:
```
AssertionError: Device mismatch for 'model.layers.0.mlp.experts.7.down_proj' process task: module weight on cpu, thread target cuda:0.
```

I think this should be related of offloading because some tensor is not moved to gpu before use? GPTQ is perfectly fine though.

## 评论 (3)

### ZX-ModelCloud · 2026-01-16

I cannot reproduce this error.
Please provide your environment details, such as the versions of PyTorch, GPTQModel, Transformers, etc.

### ZisIsNotZis · 2026-01-16

## Environment
```
(q.venv) z@z3:~$ pip list|grep -Pi 'torch|transform|gpt'
Using Python 3.12.3 environment at: /home/z/q.venv
gptqmodel                5.6.12
torch                    2.9.1
torchao                  0.15.0
transformers             4.57.3
(q.venv) z@z3:~$ nvidia-smi
Fri Jan 16 13:24:03 2026       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4090        Off |   00000000:4C:00.0 Off |                  Off |
| 32%   37C    P0             70W /  450W |       0MiB /  24564MiB |      3%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
(q.venv) z@z3:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 24.04.3 LTS
Release:	24.04
Codename:	noble
```
## Config
```py
QuantizeConfig(bits=4,
               dynamic={'-:.*mlp\\.gate$': {},
                        '-:.*mlp\\.shared_expert_gate$': {}},
               group_size=128,
               damp_percent=0.05,
               damp_auto_increment=0.01,
               desc_act=True,
               act_group_aware=False,
               static_groups=False,
               sym=False,
               true_sequential=True,
               lm_head=False,
               quant_method='awq',
               format=<FORMAT.GEMM: 'gemm'>,
               mse=0.0,
               meta={},
               device=None,
               pack_dtype=torch.int32,
               pack_impl='cpu',
               adapter=None,
               offload_to_disk=False,
               offload_to_disk_path=None,
               rotation=None,
               is_marlin_format=False,
               fail_safe=False,
               gptaq=False,
               gptaq_alpha=0.25,
               gptaq_memory_device='auto',
               zero_point=True,
               mock_quantization=False,
               hessian_chunk_size=None,
               hessian_chunk_bytes=None,
               hessian_use_bfloat16_staging=False,
               vram_strategy=<VRAMStrategy.BALANCED: 'balanced'
```
## Log (after the model dump)
```
Total parameters: 30.53B  | Total buffers: 64
Trainable: 30.53B  | Frozen: 0
INFO:tokenicer.tokenicer:Tokenicer: Auto fixed pad_token_id=151643 (token='<|endoftext|>').
INFO  Model: Loaded `generation_config`: GenerationConfig {
  "do_sample": true,
  "eos_token_id": [
    151645,
    151643
  ],
  "pad_token_id": 151643,
  "repetition_penalty": 1.05,
  "temperature": 0.7,
  "top_k": 20,
  "top_p": 0.8
}

INFO  Kernel: loaded -> `[]`                                                                                                                                                                                                                 
INFO  Packing Kernel: selected: `TorchQuantLinear`                                                                                                                                                                                           
INFO  Packing Kernel: selected: `TorchQuantLinear`                                                                                                                                                                                           
INFO  Calibration: Sort in descending order by length                                                                                                                                                                                        
INFO  Calibration: Total padded tokens: 0                                                                                                                                                                                                    
INFO  Calibration: Total non-padded tokens: 90778                                                                                                                                                                                            
INFO  Calibration: Total tokens: 90778                                                                                                                                                                                                       
WARN  The average length of input_ids of calibration_dataset should be greater than 256: actual avg: 177.30078125.                                                                                                                           
INFO  Calibration: Sort in descending order by length                                                                                                                                                                                        
INFO  Calibration: Total padded tokens: 0                                                                                                                                                                                                    
INFO  Calibration: Total non-padded tokens: 90778                                                                                                                                                                                            
INFO  Calibration: Total tokens: 90778                                                                                                                                                                                                       
WARN  The average length of input_ids of calibration_dataset should be greater than 256: actual avg: 177.30078125.                                                                                                                           
INFO  Disk subsystem write throughput detected at 676.1 MB/s.                                                                                                                                                                                
INFO  ModuleLooper: capturing layer inputs from 512 calibration batches                                                                                                                                                                      
INFO  ModuleLooper: capturing layer inputs from 512 calibration batches                                                                                                                                                                      
INFO  +------------+-------+--------+-------+---------+--------+---------+                                                                                                                                                                   
INFO  | region     | count | last_s | avg_s | total_s | pct    | source  |                                                                                                                                                                   
INFO  +------------+-------+--------+-------+---------+--------+---------+                                                                                                                                                                   
INFO  | Capture inputs | 2     | 0.576  | 0.655 | 1.311   | 100.0% | cache_inputs:Qwen3MoeDecoderLayer |                                                                                                                                     
INFO  +----------------+-------+--------+-------+---------+--------+-----------------------------------+                                                                                                                                     
INFO  GC completed in 0.004s (pass #1) at 2026-01-16T05:25:36.577222+00:00; devices=cuda:0; VRAM cuda:0=2.8G; since last GC: n/a.                                                                                                            
Quantizing layer 0 of 47 [0 of 47] ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:00:51 / 0:40:48 [1/48] 2.1%
Quantizing layer 0 of 47 [0 of 47] ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:00:51 / 0:40:48 [1/48] 2.1%
INFO  AWQProcessor: layer 0 tracking 389 modules before quantization (subsets processed=4/4); first modules=['self_attn.q_proj', 'self_attn.k_proj', 'self_attn.v_proj', 'self_attn.o_proj', 'mlp.experts.0.gate_proj', 'mlp.experts.0.up_proj', 'mlp.experts.1.gate_proj', 'mlp.experts.1.up_proj']
INFO  AWQProcessor: layer 0 sanitized 130 scaling groups; sample=[['self_attn.q_proj', 'self_attn.k_proj', 'self_attn.v_proj'], ['mlp.experts.0.gate_proj', 'mlp.experts.0.up_proj', 'mlp.experts.1.gate_proj', 'mlp.experts.1.up_proj'], ['mlp.experts.0.down_proj']]
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+----------+--------------+---------+                                                                          
INFO  | process | layer | module                    | feat: in, out | dtype: size  | loss         | samples | damp    | time  | fwd_time | (v)ram       | dynamic |                                                                          
INFO  +---------+-------+---------------------------+---------------+--------------+--------------+---------+---------+-------+----------+--------------+---------+                                                                          
INFO  | awq     | 0     | self_attn.q_proj          | 2048, 4096    | f16: 32.0MB  | 0.0000002347 | 512     |         | 0.003 |          | cuda 6.13G   |         |                                                   

...
                                                                   
INFO  awq | layer=0 module=mlp.experts.119.down_proj loss=0.0000012335 samples=512 time=72.878s                                                                                                                                              
INFO  | process | layer | module                    | feat: in, out | dtype: size  | loss           | samples | damp    | time   | fwd_time | (v)ram       | dynamic |                                                                       
INFO  +---------+-------+---------------------------+---------------+--------------+----------------+---------+---------+--------+----------+--------------+---------+                                                                       
INFO  | awq     | 0     | mlp.experts.120.down_proj | 768, 2048     | f16: 6.0MB   | 0.0000017083   | 512     |         | 73.087 |          | cuda 6.13G   |         |                                                
INFO  +---------+-------+---------------------------+---------------+--------------+----------------+---------+---------+--------+----------+--------------+---------+                                                                       
INFO  awq | layer=0 module=mlp.experts.120.down_proj loss=0.0000017083 samples=512 time=73.087s                                                                                                                                              
INFO  | awq     | 0     | mlp.experts.121.down_proj | 768, 2048     | f16: 6.0MB   | 0.0000013218   | 512     |         | 73.293 |          | cuda 6.13G   |         |                                                
INFO  +---------+-------+---------------------------+---------------+--------------+----------------+---------+---------+--------+----------+--------------+---------+                                                                       
INFO  awq | layer=0 module=mlp.experts.121.down_proj loss=0.0000013218 samples=512 time=73.293s                                                                                                                                              
INFO  | awq     | 0     | mlp.experts.122.down_proj | 768, 2048     | f16: 6.0MB   | 0.0000015446   | 512     |         | 73.501 |          | cuda 6.13G   |         |                                                
INFO  +---------+-------+---------------------------+---------------+--------------+----------------+---------+---------+--------+----------+--------------+---------+                                                                       
INFO  awq | layer=0 module=mlp.experts.122.down_proj loss=0.0000015446 samples=512 time=73.501s                                                                                                                                              
INFO  | awq     | 0     | mlp.experts.123.down_proj | 768, 2048     | f16: 6.0MB   | 0.0000004746   | 512     |         | 73.708 |          | cuda 6.13G   |         |                                                
INFO  +---------+-------+---------------------------+---------------+--------------+----------------+---------+---------+--------+----------+--------------+---------+                                                                       
INFO  awq | layer=0 module=mlp.experts.123.down_proj loss=0.0000004746 samples=512 time=73.708s                                                                                                                                              
INFO  | awq     | 0     | mlp.experts.124.down_proj | 768, 2048     | f16: 6.0MB   | 0.0000070564   | 512     |         | 73.916 |          | cuda 6.13G   |         |                                                
INFO  +---------+-------+---------------------------+---------------+--------------+----------------+---------+---------+--------+----------+--------------+---------+                                                                       
INFO  awq | layer=0 module=mlp.experts.124.down_proj loss=0.0000070564 samples=512 time=73.916s                                                                                                                                              
INFO  | awq     | 0     | mlp.experts.125.down_proj | 768, 2048     | f16: 6.0MB   | 0.0000057580   | 512     |         | 74.124 |          | cuda 6.13G   |         |                                                
INFO  +---------+-------+---------------------------+---------------+--------------+----------------+---------+---------+--------+----------+--------------+---------+                                                                       
INFO  awq | layer=0 module=mlp.experts.125.down_proj loss=0.0000057580 samples=512 time=74.124s                                                                                                                                              
INFO  | awq     | 0     | mlp.experts.126.down_proj | 768, 2048     | f16: 6.0MB   | 0.0000042364   | 512     |         | 74.334 |          | cuda 6.13G   |         |                                                
INFO  +---------+-------+---------------------------+---------------+--------------+----------------+---------+---------+--------+----------+--------------+---------+                                                                       
INFO  awq | layer=0 module=mlp.experts.126.down_proj loss=0.0000042364 samples=512 time=74.334s                                                                                                                                              
INFO  | awq     | 0     | mlp.experts.127.down_proj | 768, 2048     | f16: 6.0MB   | 0.0000015834   | 512     |         | 74.542 |          | cuda 6.13G   |         |                                                
INFO  +---------+-------+---------------------------+---------------+--------------+----------------+---------+---------+--------+----------+--------------+---------+                                                                       
Traceback (most recent call last):erts.127.down_proj loss=0.0000015834 samples=512 time=74.542s                                                                                                                                              
  File "/home/z/q.venv/lib/python3.12/site-packages/gptqmodel/utils/threadx.py", line 415, in _run░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░| 0:03:10 / 2:32:00 [1/48] 2.1%
    result = fn(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^
  File "/home/z/q.venv/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/z/q.venv/lib/python3.12/site-packages/gptqmodel/looper/stage_subset.py", line 441, in _process_on_worker
    assert actual_device == target_device, (
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Device mismatch for 'model.layers.0.mlp.experts.4.down_proj' process task: module weight on cpu, thread target cuda:0.
```
@ZX-ModelCloud 

### ZX-ModelCloud · 2026-01-19

I reproduced this issue in gptqmodel **v5.6.12**, but I couldn't reproduce it in the latest code.
You can [install from the latest source](https://github.com/ModelCloud/GPTQModel?tab=readme-ov-file#install-from-source) code and try again.
