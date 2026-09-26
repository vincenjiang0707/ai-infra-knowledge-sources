# [Issue #2362] How to reproduce reported 1613 TFLOPS at seqlen=32k on Blackwell?

source: https://github.com/Dao-AILab/flash-attention/issues/2362
state: closed | updated: 2026-06-15T23:53:29Z
labels: 

## 正文

Hi FA4 team, thank you for releasing the amazing work on FlashAttention-4!

We are trying to reproduce the reported 1613 TFLOPS at seqlen=32k (BF16, non-causal, B200) from the paper, but are getting varying results depending on the benchmark settings used with [bench_sm90.py](https://github.com/Dao-AILab/flash-attention/blob/main/benchmarks/bench_sm90.py) (we run each setting 3 times and report the range of reported TFLOPs):

| `--warmup` | `--rep` | TFLOPS |                                                                                                                                                                                                                                               
  |---|---|---|                                                                                                                                                                                                                                                                 
  | 1 | 1 | ~1627–1634 |                                                                                                                                                                                                                                                          
  | 1 | 10 | ~1587–1634 |                                                                                                                                                                                                                                                         
  | 5 | 30 | ~1445–1474 |

We noticed bench_sm90.py defaults to --warmup 5 --rep 30 (`python benchmarks/bench_sm90.py --direction fwd --hdim 128 --seqlen 32k --batch 1 --non-causal-only --warmup 5 --rep 30`) but this gives numbers significantly below the paper's reported value, while --warmup 1 --rep 1 performs better than that. 

The performance variations across different settings might be related to a lowered GPU clock frequency, when mutiple back-to-back FA4 runs heat up the device.

## Environment

For your reference, our environment is as follows:
                                                                                                          
  - GPU: NVIDIA B200
  - CUDA: 13.1
  - PyTorch: 2.10.0a0+b4e4ee81d3.nv25.12
  - Config: batch=1, seqlen=32768, nheads=16, hdim=128, non-causal, BF16    
  - FA repo version: 71bf77c87a75c0dfb25fab8ee4abd7f57d10c9cc                                                                                                      


## L2 and I-cache considerations                                                                                                                                                                                                                                                   
                                                                                                          
We also noticed that bench_sm90.py runs back-to-back iterations with no L2 flush and no sleep between runs:                                                                                                                                                                     
   
  ### bench_sm90.py        
```python                                                                                                                                                                                                                                                         
  for _ in range(warmup):                                                                                 
      _flash_attn_fwd(q, k, v, **kwargs)                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                  
  torch.cuda.synchronize()                                                                                                                                                                                                                                                        
  start.record()                                                                                                                                                                                                                                                                  
  for _ in range(rep):                                                                                                                                                                                                                                                            
      _flash_attn_fwd(q, k, v, **kwargs)                                                                  
  end.record()                                                                                                                                                                                                                                                                    
```

This means both the L2 data cache and SM instruction cache (I-cache) are warm throughout all timed runs.                                                                                                                                    

----
Could you clarify:                                                                                                                                                                                                                                                              
  1. What exact command/settings were used to generate the numbers reported in the paper?                 
  2. Are there any environment requirements (e.g. locked GPU clocks, specific CUDA version, persistence mode) needed to reproduce the reported numbers?
  3. Is the intent to measure with hot L2/I-cache (kernel in isolation) or cold cache (when running a model end-to-end, we might not be able to maintain hot cache)?

We wanted to ensure that we followed the correct setting for benchmarking FA4 implementation. Thanks so much for your help!

## 评论 (3)

### tridao · 2026-03-17

`bench_sm90.py` was written recently for tile size tuning on Sm90 so it wasn't done carefully. Try `benchmarks/benchmark_attn.py`. By default we use warmup=5 and rep=10 (we included these details in the paper i think, if not we'll update). The repeat matters because more repeat will cause power throttling (one can argue whether one should measure the power-throttled or non-power-throttled number). 
`benchmark_attn.py` uses triton.testing.do_bench which does L2 cache flushing.

### tridao · 2026-03-17

The numbers you showed w warmup=1 and repeats=10 (1587-1634 TFLOPS) isn't far off (within 1-2%, which is normal). There's variation between GPUs too. In practice we make sure to run the script to compare methods on the same GPUs (and the same inputs, as input value distribution will change the results slightly).



### LemonAndRabbit · 2026-06-15

Thank you so much for providing the details!
