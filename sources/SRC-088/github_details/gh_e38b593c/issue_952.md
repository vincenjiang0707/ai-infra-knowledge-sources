# [Issue #952] [RFC]: Add native DeepSeek-V4-Flash DSpark support

source: https://github.com/vllm-project/speculators/issues/952
state: open | updated: 2026-08-25T02:25:10Z
labels: 

## 正文

## Summary

This RFC proposes adding native DeepSeek-V4-Flash support to `speculators`: a DSpark draft built on DSV4's own architecture. The implementation and the training run are both complete. The target is `deepseek-ai/DeepSeek-V4-Flash` (Preview), not the later `DeepSeek-V4-Flash-0731` release. The numbers below are measured against the released DeepSeek DSpark draft on the same serve (vLLM 0.23 + vllm-ascend, `num_speculative_tokens=5`, greedy, full `DATASET=all`):

| epoch | 0.5 | 1.0 | 1.5 | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 | 4.5 | 5.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| mean accept_len | 3.84 | 4.06 | 4.18 | 4.25 | 4.29 | 4.35 | 4.36 | 4.39 | 4.41 | 4.40 |
| % of released (4.42) | 87.0 | 91.8 | 94.6 | 96.3 | 97.2 | 98.4 | 98.7 | 99.4 | 99.7 | 99.5 |

![current best vs released draft](https://raw.githubusercontent.com/Sawyer117/speculators/feat/dsv4-dspark/docs/deployment/images/current_best_vs_released_final_ep5p0.png)

Per-dataset accept_len at the final checkpoint, on the same serve:

| | gsm8k | math500 | humaneval | mbpp | mt-bench |
|---|---|---|---|---|---|
| this draft, 5 epochs | 4.849 | 4.565 | 4.933 | 4.555 | 3.079 |
| released DSpark draft | 4.658 | 4.661 | 4.942 | 4.535 | 3.294 |

The curve is flat over the last three checkpoints: the five-dataset mean spans 0.014 across 4.0 / 4.5 /
5.0 epochs and gsm8k's per-checkpoint gain holds at +0.009. The learning rate is a cosine decay reaching
zero at 5 epochs, so the run ends fully annealed. Per-dataset and per-position numbers for all ten
checkpoints are in the evaluation ledger linked below.

## What is implemented

- A DSV4-native draft model: 3 × [MLA (q/o LoRA, per-head attention sink) + 256-routed/1-shared MoE
  (`sqrtsoftplus` scoring, `noaux_tc` top-k) + manifold-constrained hyper-connections], plus the
  DSpark Markov and confidence heads. It is registered as its own speculator type, not as a DFlash
  variant.
- Expert-parallel MoE training alongside FSDP2: each rank owns a disjoint slice of whole routed
  experts, and tokens reach their owner through an all-to-all dispatch (dropless), so the experts
  are held out of FSDP (`ignored_params`) rather than all-gathered. They are still exposed as
  `Shard(0)` DTensors on the same mesh as the FSDP-sharded parameters, so the optimizer, gradient
  clipping and checkpointing need no plain-tensor special casing. This part is model-agnostic.
- Warm-start controls: `--init-layer-from-target`, `--init-{moe,attn,hc,norm}-from-target` and
  `--init-moe-no-router`, initialising draft layers from chosen verifier layers.
- Opt-in `noaux_tc` load balancing for the draft router, following the DeepSeek-V3 rule.
- An online hidden-state path: a plain verifier serve produces hidden states that the trainer
  consumes as a rolling buffer, avoiding full-dataset materialisation.
- Conversion to the vLLM `mtp.*` serving layout, with an independent bit-exact check
  (2378/2378 tensors per checkpoint).

## Code

Branch: [`Sawyer117/speculators@feat/dsv4-dspark`](https://github.com/Sawyer117/speculators/tree/feat/dsv4-dspark).

Entry point:
[`docs/deployment/ascend-npu-dsv4-dspark-pipeline.md`](https://github.com/Sawyer117/speculators/blob/feat/dsv4-dspark/docs/deployment/ascend-npu-dsv4-dspark-pipeline.md).
It opens with a six-step reproduction path — environment, rollout, hidden states, training,
conversion, evaluation — with the exact commands, and indexes the per-stage design documents and the
evaluation ledger behind the table above.

Draft model:
[`src/speculators/models/dsv4_dspark/`](https://github.com/Sawyer117/speculators/tree/feat/dsv4-dspark/src/speculators/models/dsv4_dspark).

## Vendor-specific code

Development was on Ascend NPU (Atlas A2/A3, FSDP2 training; vLLM 0.23 + vllm-ascend for serving).
The vendor-specific parts are confined:

- The draft model is portable PyTorch. `core.py`, `config.py`, `weights.py` and
  `backbone/{attention,moe,hyper,rotary,norm,block}.py` contain no `torch_npu` import and no NPU
  call; NPU appears there only in comments explaining a portable formulation.
- `backbone/kernels.py` is a registry: each op has a torch reference, and a vendor bridge may
  register a faster implementation under the same key at import time. Nothing is NPU-only by
  default.
- Two modules import `torch_npu` — `backbone/moe_grouped_gemm.py` and `backbone/moe_compile.py` —
  with every call site gated on `device.type == "npu"`. They are throughput optimisations, not
  correctness requirements, and can be left out of an upstream PR or moved behind the registry.
- `examples/ascend_npu_dflash/` is operational tooling (launchers, serve scripts, analysis), not
  proposed as-is.
- The fork also carries small device-handling changes in the shared trainer; those would be
  rewritten against `torch.accelerator` rather than guarded `torch.cuda`.

A first upstream PR can therefore be device-agnostic, with the vendor bridge kept downstream.

## Open design question

The backbone is a clean-room implementation, validated component-by-component against
`transformers`' `deepseek_v4` — RMSNorm and the hyper-connection blocks bit-exact, MoE ~1.5e-7, sink
~1.2e-7 — with
[`dsv4_dspark_hf_parity.py`](https://github.com/Sawyer117/speculators/blob/feat/dsv4-dspark/examples/ascend_npu_dflash/dsv4_dspark_hf_parity.py);
routing and rotary conventions were cross-checked against torchtitan's DeepSeek-V4.

Three structures are possible: build on the `transformers` modules (less code, tracks the verifier's
implementation, but couples the draft to their layout), mirror an existing reference such as
torchtitan's, or keep a self-contained implementation. This choice determines most of the diff, so
we would rather settle it before writing the PR than assume.

## Proposed contribution order

Incremental rather than one large PR, from most general to most DSV4-specific:

1. Expert-parallel MoE training alongside FSDP2 (model-agnostic).
2. The `--init-*-from-target` warm-start controls.
3. `noaux_tc` load balancing for MoE draft routers.
4. The DSV4-native draft model.

Is upstreaming this of interest to the project, and if so, which of these components would you want
and in what order? Each can be submitted as a separate PR with tests, and the design can be revised
beforehand if any of it conflicts with planned work.

This work is by @zongzuo and me; questions and collaboration are welcome.


## 评论 (4)

### Sawyer117 · 2026-08-13

@fynnsu @rahul-tuli — hope you don't mind the ping, there's an update worth reporting on this one.

The training run finished, and on our server the draft now measures **4.41 mean acceptance length against 4.42 for the released DeepSeek draft** — same server, same harness, both measured the same way. gsm8k, humaneval and mbpp come out slightly above the released draft; mt-bench is still behind.

If any of it looks useful, what I'd propose merging, roughly in order:

1. **The DSV4-Flash DSpark draft model definition** — MLA + per-head sink attention + 256-expert MoE + mHC, reusing the Markov and confidence heads from #677. This is the part that has actually been trained and evaluated end to end.
2. **Expert-parallel training**, if it's of interest. speculators has no MoE draft today, so there is nothing to shard yet — EP would have to come as a pair: a generic grouped-experts MoE layer, plus FSDP2 `Shard(0)` over the expert dimension.

On the second one I had a look at what is already in flight first. #599 is data-parallel scale-out plus hidden-state transport, and #871 / #298 are Ulysses SP — EP looks like a different axis to me, so I don't think it collides. But if you have a broader picture of how parallelism should look in this library, I would much rather build into that than land something off to the side, and I'm glad to help implement or debug there instead. I also have multi-node Ascend hardware I can test on, which might help with the "needs testing" blocker on #599 — as a second-platform check rather than a substitute for GPU testing.

Whenever you have time, and no hurry at all — even a rough "worth pursuing" or "out of scope" would help me plan.


### shanjiaz · 2026-08-20

@Sawyer117 Hey! Thanks for putting up this RFC. Could we break this into smaller parts and perhaps propose a more detailed design for The DSV4-Flash DSpark draft model definition and Expert-parallel training separately. We would be happy to review. Could we maybe talk more in vLLM slack? https://join.slack.com/t/vllm-dev/shared_invite/zt-4722qavbb-UkVXtje0mgsJ~1As0P6cgA Thank you thank you!

### zihanlin-ai · 2026-08-23

Observations from training a DSpark drafter with an MoE draft stack downstream (a different verifier family, not DSv4 — analogies, not DSv4 data), relevant to the model-definition / EP-training split:

1. **Routing collapse at init.** With draft layers initialized from the verifier's MTP layers, the deep draft slots started out using only 13–22 of 256 experts; loss-free dynamic bias balancing widened utilization but did not by itself fix quality. Per-layer / per-slot expert-utilization counters in the model definition from day one — it is invisible in the loss curve.
2. **Two training regimes.** Frozen experts (train attention / Markov / projector only) fits one device per rank and is where most of our recipe search ran; only full-expert training needs the sharding story. A first-class "experts frozen" switch in the model definition keeps the model PR from blocking on the EP design.
3. **MoE router under DDP** can drop out of the autograd graph on some steps; plain DDP needs `find_unused_parameters=True` or it hangs.
4. **fp32 sharded originals.** With bf16 originals, small AdamW updates vanish (#711 already moved upstream to fp32 + autocast; the small per-expert gradients make it matter more here).
5. **Init source.** Auditing the released V4 DSpark weights, detectable lineage from the public MTP modules appears only in Flash-family layer 0, none elsewhere — so a from-scratch option is worth keeping next to "init from MTP".


### Sawyer117 · 2026-08-25

> Observations from training a DSpark drafter with an MoE draft stack downstream (a different verifier family, not DSv4 — analogies, not DSv4 data), relevant to the model-definition / EP-training split:
> 
> 1. **Routing collapse at init.** With draft layers initialized from the verifier's MTP layers, the deep draft slots started out using only 13–22 of 256 experts; loss-free dynamic bias balancing widened utilization but did not by itself fix quality. Per-layer / per-slot expert-utilization counters in the model definition from day one — it is invisible in the loss curve.
> 2. **Two training regimes.** Frozen experts (train attention / Markov / projector only) fits one device per rank and is where most of our recipe search ran; only full-expert training needs the sharding story. A first-class "experts frozen" switch in the model definition keeps the model PR from blocking on the EP design.
> 3. **MoE router under DDP** can drop out of the autograd graph on some steps; plain DDP needs `find_unused_parameters=True` or it hangs.
> 4. **fp32 sharded originals.** With bf16 originals, small AdamW updates vanish ([DDP + updated AMP strategy #711](https://github.com/vllm-project/speculators/pull/711) already moved upstream to fp32 + autocast; the small per-expert gradients make it matter more here).
> 5. **Init source.** Auditing the released V4 DSpark weights, detectable lineage from the public MTP modules appears only in Flash-family layer 0, none elsewhere — so a from-scratch option is worth keeping next to "init from MTP".

Hi zihanlin @zihanlin-ai , thank you very much for the comment. Do you want to add my wechat to discuss more? we wechat id is: austin_c11
