# [Issue #3459] [Question] Showcase / question: a board-proven offline language runtime on ESP32-C3, and whether this points to a more extreme form of language-runtime compilation

source: https://github.com/mlc-ai/mlc-llm/issues/3459
state: open | updated: 2026-04-24T10:53:58Z
labels: question

## 正文

## ❓ General Questions

Hi MLC folks,                                                                                                                                                                         
                                                                                                                                                                                        
  I wanted to share a small but unusual language-runtime project that may be relevant to the broader question of how far language capability can be compiled into deployment-specific execution forms.                                                                                                                                                                      
                                                                                                                                                                                        
  We built a public demo line called Engram and deployed it on a commodity ESP32-C3.                                                                                                    
                                                                                                                                                                                        
  Current public numbers:                                                                                                                                                               
                                                                                                                                                                                        
  * Host-side benchmark capability                                                                                                                                                      
    * `LogiQA = 0.392523`
    * `IFEval = 0.780037`                                                                                                                                                               
                                                                                                                                                                                        
  * Published board proof                                                                                                                                                               
    * `LogiQA 642 = 249 / 642 = 0.3878504672897196`                                                                                                                                     
    * `host_full_match = 642 / 642`                                                                                                                                                     
    * runtime artifact size = `1,380,771 bytes`                                                                                                                                         
                                                                                                                                                                                        
  Important scope note:                                                                                                                                                                 
                                                                                                                                                                                        
  This is **not** presented as unrestricted open-input native LLM generation on MCU.                                                                                                    
                                                                                                                                                                                        
  The board-side path is closer to a flash-resident, table-driven runtime with:                                                                                                         
                                                                                                                                                                                        
  * packed token weights                                                                                                                                                                
  * hashed lookup structures                                                                                                                                                            
  * fixed compiled probe batches                                                                                                                                                        
  * streaming fold / checksum style execution over precompiled structures                                                                                                               
                                                                                                                                                                                        
  So this is not a standard dense graph language runtime compiled for a smaller device. It is closer to a task-specialized language runtime whose behavior has been crystallized into a compact executable form.                                                                                                                                                              
                                                                                                                                                                                        
  Repo:                                                                                                                                                                                 
  https://github.com/Alpha-Guardian/Engram                                                                                                                                              
                                                                                                                                                                                        
  Why I’m posting here is that MLC LLM seems to sit on one of the clearest public paths from model semantics to deployment-specific runtime form.                                       
                                                                                                                                                                                        
  What I’d be curious about is whether systems like this should be thought of as:                                                                                                       
                                                                                                                                                                                        
  * outside the normal compiled-runtime path for LLMs                                                                                                                                   
  * an extreme endpoint of language-runtime compilation                                                                                                                                 
  * or an early indication that some language-task capability may eventually be deployed in more specialized executable forms than a conventional dense runtime                         
                                                                                                                                                                                        
  If this direction is relevant to your team, I’d be glad to compare notes.           


## 评论 (3)

### JiwaniZakir · 2026-03-27

The ESP32-C3's constraints (160 MHz single-core RISC-V, ~400 KB SRAM, no FPU) place this well outside the current assumptions in MLC-LLM's compilation pipeline, which targets devices with at least several hundred MB of addressable memory for even the most aggressively quantized models (e.g., 4-bit Llama at ~2 GB+). The benchmark numbers you're citing (LogiQA ~0.39, IFEval ~0.78) suggest this isn't a weight-based autoregressive model at all, but rather something closer to a compiled finite-state or lookup-augmented decision structure — which is a fundamentally different artifact than what MLC's `relax` + TVM backend produces. The relevant boundary here is that MLC's compilation target is a *weight-carrying* runtime; what you're describing sounds more like a *knowledge-distilled control structure* where the "weights" have been compiled away into program logic, which is architecturally distinct from the quantize-and-deploy path MLC optimizes. If the goal is to understand whether MLC's compilation stack could emit such artifacts, the answer is currently no — that would require a novel lowering pass that converts attention/MLP subgraphs into branching logic rather than tensor kernels, which nothing in `tvm/relax` or `mlc_llm/compiler` currently targets.

### rehan243 · 2026-04-21

oh interesting, you're running Engram on ESP32-C3? That's wild — we tried pushing a distilled LLM onto a similar microcontroller (STM32 series), got stuck on RAM and flash constraints fast. How're you handling quantization and model partitioning? The thing is, for extreme language-runtime compilation, we've had to hack around with ultra-low bit quantizers (like 2-bit) and strip out everything but basic token prediction.

Fwiw, if you're using mlc-llm, you can do something like:

```python
from mlc_llm.quantization import quantize_model
model = quantize_model("path_to_model", bits=2)
```

We found this cut RAM usage by ~60%, but honestly, token latency went up unless you cache aggressively. Also, curious if you're using custom ops on the ESP side or just standard C? For our STM32 setup, we had to replace most tensor routines with fixed-point math.

Anyway, the board-proven runtime angle's super cool — the docs don’t really cover these microcontroller deployments, so you’re kinda blazing the trail here.

### Juemian-Deng · 2026-04-24

> oh interesting, you're running Engram on ESP32-C3? That's wild — we tried pushing a distilled LLM onto a similar microcontroller (STM32 series), got stuck on RAM and flash constraints fast. How're you handling quantization and model partitioning? The thing is, for extreme language-runtime compilation, we've had to hack around with ultra-low bit quantizers (like 2-bit) and strip out everything but basic token prediction.
> 
> Fwiw, if you're using mlc-llm, you can do something like:
> 
> from mlc_llm.quantization import quantize_model
> model = quantize_model("path_to_model", bits=2)
> We found this cut RAM usage by ~60%, but honestly, token latency went up unless you cache aggressively. Also, curious if you're using custom ops on the ESP side or just standard C? For our STM32 setup, we had to replace most tensor routines with fixed-point math.
> 
> Anyway, the board-proven runtime angle's super cool — the docs don’t really cover these microcontroller deployments, so you’re kinda blazing the trail here.

Thanks — just to clarify, we aren't framing the public ESP32-C3 result as a full-fledged, general-purpose LLM deployment on an MCU.

Right now, the repo just shows a bounded, fixed-batch proof-of-concept on the board, alongside a separate, narrowly scoped open-input loop for the C3. Because of that, we consider it a constrained compiled artifact rather than unrestricted LLM inference.

We're keeping the public discussion limited to this scope for now. The exact details are outlined here:

docs/BOARD_METRICS.md

docs/OPEN_INPUT_ROADMAP.md

docs/OPEN_INPUT_DEMO.md

docs/REPRODUCE.md
