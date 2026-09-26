# [Issue #170] os.environ.get取值异常

source: https://github.com/Ascend/pytorch/issues/170
state: open | updated: 2026-09-24T08:28:39Z
labels: 

## 正文

-> if self.distributed_type == DistributedType.DEEPSPEED and self._mixed_precision != "fp8":                                                                                                                    
[rank0]: Traceback (most recent call last):                                                                                                                                                                      
[rank0]:   File "/app/src/llamafactory/launcher.py", line 185, in <module>                                                                                                                                      
 [rank0]:     run_exp()                                                                                                                                                                                           
[rank0]:   File "/app/src/llamafactory/train/tuner.py", line 156, in run_exp                                                                                                                                    
 [rank0]:     _training_function(config={"args": args, "callbacks": callbacks})                                                                                                                                   
[rank0]:   File "/app/src/llamafactory/train/tuner.py", line 124, in _training_function                                                                                                                          
[rank0]:     run_sft(model_args, data_args, training_args, finetuning_args, generating_args, callbacks)                                                                                                          
[rank0]:   File "/app/src/llamafactory/train/sft/workflow.py", line 106, in run_sft                                                                                                                             
 [rank0]:     trainer = CustomSeq2SeqTrainer(                                                                                                                                                                     
[rank0]:               ^^^^^^^^^^^^^^^^^^^^^                                                                                                                                                                     
[rank0]:   File "/app/src/llamafactory/train/sft/trainer.py", line 67, in __init__                                                                                                                               
[rank0]:     super().__init__(**kwargs)                                                                                                                                                                         
 [rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/transformers/trainer_seq2seq.py", line 74, in __init__                                                                                   
 [rank0]:     super().__init__(                                                                                                                                                                                   
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/transformers/trainer.py", line 409, in __init__                                                                                           
[rank0]:     self.create_accelerator_and_postprocess()                                                                                                                                                           
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/transformers/trainer.py", line 810, in create_accelerator_and_postprocess                                                                
 [rank0]:     self.accelerator = Accelerator(**args)                                                                                                                                                              
[rank0]:                        ^^^^^^^^^^^^^^^^^^^                                                                                                                                                             
 [rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/accelerate/accelerator.py", line 477, in __init__                                                                                         
[rank0]:     self.fp8_enabled = self.state.mixed_precision == "fp8" or mixed_precision == "fp8"                                                                                                                  
[rank0]:                        ^^^^^^^^^^^^^^^^^^^^^^^^^^                                                                                                                                                       
[rank0]:   File "/usr/local/python3.11.15/lib/python3.11/site-packages/accelerate/state.py", line 1234, in __getattr__                                                                                           
[rank0]:     raise AttributeError(f"'AcceleratorState' object has no attribute '{name}'")                                                                                                                        
[rank0]: AttributeError: 'AcceleratorState' object has no attribute 'mixed_precision'. Did you mean: '_mixed_precision'?    

我在用llamafactory + deepspeed进行模型微调时，遇到了上方的异常，发现ACCELERATE_USE_DEEPSPEED这个环境变量取值异常。
似乎是patch_getenv.py中的patch导致了accelerate的代码中奇怪的行为(get和[] 行为不一致引起)。
---------------------------------
# accelerate-1.15.0  state.py:974 行
            elif os.environ.get("ACCELERATE_USE_DEEPSPEED", "false").lower() == "true" and not cpu:
                self.distributed_type = DistributedType.DEEPSPEED
                if not isinstance(deepspeed_plugin, dict):
                    deepspeed_plugin.set_mixed_precision(mixed_precision)
                    deepspeed_plugin.select(_from_accelerator_state=True)
                else:
                    for plugin in deepspeed_plugin.values():
                        plugin.set_mixed_precision(mixed_precision)
                    # The first plugin passed in is always the active one
                    first_plugin = next(iter(deepspeed_plugin.values()))
                    first_plugin.select(_from_accelerator_state=True)
                self.deepspeed_plugins = deepspeed_plugin

---------------------------------
torch_npu/utils/patch_getenv.py:26:def _patched_environ_get(key, default=None):                                                                                                                                  
torch_npu/utils/patch_getenv.py:36:os.environ.get = _patched_environ_get  
----------------------------------
 (Pdb)os.environ.get                                                                                                                                                                                             
<function _patched_environ_get at 0xfffdc0967ec0>
 (Pdb)  print(os.environ.get("ACCELERATE_USE_DEEPSPEED", "false"), os.environ.get("ACCELERATE_USE_DEEPSPEED"])                                                                                                                                                                                                                                                                                                             false true
----------------------------------

## 评论 (2)

### ascend-robot · 2026-09-24

Hello,

This repo is only a mirror with no active development or maintenance.
All bug reports, questions and code contributions should be submitted via the original repository link below.
Thanks for your interest!

Original Repository Link: https://gitcode.com/Ascend/pytorch

### bean002 · 2026-09-24

请帮我转提到gitcode @ascend-robot 
