# [Issue #1659] [Docs][RL] Guide: RL training loop with llm-d serving (no Kubernetes)

source: https://github.com/llm-d/llm-d/issues/1659
state: open | updated: 2026-09-21T02:22:37Z
labels: release/v0.9

## 正文

### Summary

Create an end-to-end guide showing how to run an RL training loop that uses llm-d for rollout generation, without Kubernetes.

This builds on the non-Kubernetes deployment mode work already merged:
- Proposal: https://github.com/llm-d/llm-d/blob/main/docs/proposals/non-kubernetes-mode.md
- Deployment guide: https://github.com/llm-d/llm-d/pull/1618
- File-discovery plugin PRs in llm-d-router: #908, #1080, #1081, #1135, #1154, #1218, #1338, #1362, #1368, #1404

### What the guide should cover

- Setting up llm-d serving on bare metal using the file-discovery plugin (reference the existing no-kubernetes guide)
- Wiring a training loop (e.g., veRL, OpenRLHF, or a minimal example) to call llm-d for inference rollouts via HTTP API
- Weight synchronization between training and serving
- Example configuration and scripts to run the full loop

### Context

Tracked in v0.8 release goals: https://github.com/llm-d/llm-d/issues/1520

## 评论 (2)

### 0z5a · 2026-09-19

Hi @chcost , I'd be happy to take this.

I have experience with RL serving / rollout systems and would like to build the first version around the existing no-Kubernetes/file-discovery path instead of introducing another deployment mechanism.

### 0z5a · 2026-09-21

# A4 status for the no-Kubernetes RL guide: the serving loop works, the small-scale learning loop does not

Work order A4 / this issue. Author 0z5a. Host gj-5090-2, no k8s and no docker:
vLLM worker <- EPP (file-discovery) <- Envoy (ext_proc) <- client, all bare processes.

Posting this because the second half is a **negative result** and it is cheaper for the next
person to reuse than to rediscover. There is no code PR: the guide's plumbing is fine, the
recipe a reader would plausibly copy out of a small-scale example is not.

## What passed

| item | result |
|---|---|
| every rollout goes through the routing entry point | **PASS** — 192/192 traced `entry=envoy` on `:8082`, never the worker port |
| inventory / checkpoint / atomic rename / drain / controlled restart / republish | **PASS** — bad YAML still admits, partial in-place write is caught, 3 s drain timeout measured 3.391 s with an in-flight 1800-token request returning 200 |
| version barrier with per-stage timing | **PASS** — `unavailable_window` 65.571 s, `iteration_total` 271.876 / 278.444 s; every stage carries its sample count and the host loadavg |
| failure injection and recovery | **PASS** — a replica that is not ready is rejected by the publish guard and the inventory file is byte-identical afterwards |
| prefix-cache reuse after an update | **PASS** — `vllm:prompt_tokens_cached_total` +7104 for a 600-token prompt x12 (592/request, blocks 0..37); changing one token gives the same +7104 |
| incremental cost of routing through Envoy + EPP | median **+3.19 ms** per request (paired, alternating order, n=40/arm, greedy, max_tokens 16), output bit-identical |

## What failed, and why the issue is still open

The learning gate was declared before measurement and never moved: **mean reward >= 0.70 at v0, v1
and v2**. Five consecutive rounds failed it. Each round changed one thing and kept everything else.

| round | the one change | v0 | v1 | v2 | G3 |
|---|---|---|---|---|---|
| R1 | first attempt, lr 2e-4 | 0.781 | **0.000** | 0.000 | FAIL |
| R2 | lr 2e-5 + prompt set re-selected by measured base accuracy | 0.849 | **0.161** | 0.000 | FAIL |
| R3a | token-length normalisation of the loss | 0.8229 | **0.2135** | null (host went down) | FAIL |
| R3b | + KL anchor (beta=1) + per-step parameter-distance cap `max_step_rel=0.0002` | 0.8229 | **0.0833** | **0.0000** | FAIL |
| R4 | truncate the policy term **and** the KL anchor to the answer tokens only | 0.8229 | **0.0000** | **0.0000** | FAIL |

R1's v2 point is 0.000 because v1 already scored 0 on every sample of every prompt: with no
spread inside any group there is no group-relative advantage, so the second boundary moved the
weights only through decoupled weight decay.

The optimiser is excluded as the cause, not by argument but by measurement:

* **The gradient is real, not weight decay.** Update / weight-decay-only ratio was 1818.5x (R3b
  v0->v1) and 1856.5x (v1->v2); every optimizer step had finite non-zero losses and grad norms and
  probed parameters actually moved.
* **Smaller steps did not help.** The pre-registered cap bound on **every** step:
  raw ||dtheta|| 0.00043501 / 0.00031806 / 0.00026262 / 0.00023171 -> applied 0.0002 each time
  (0.02% of the parameter-vector norm per step).
* **KL anchoring did not help.** With beta=1 the KL term sat at 1e-5..1e-3 nats/token, i.e. the
  anchor was effectively a rounding correction while the policy still left the competent region.
* **A 10x lower lr and length normalisation did not help.** R3a cut grad norms 4-7x versus R2 and
  *widened* the advantage spread (56/192 non-zero vs 48), and v1 still fell to 0.2135.

R4 then changed the objective rather than the optimiser, since the reward is a single binary
exact-match on the parsed integer and therefore carries no per-token signal on the scratchpad and
formatting the policy writes first. Truncating the loss (and the KL term) to the answer span did not
stop the collapse either: 0.8229 / 0.0000 / 0.0000.

**Conclusion, as declared before R4 ran:** at this host and this scale, the credit assignment of a
scalar exact-match reward is the main cause of the collapse. No further changes to lr,
`max_step_rel` or `kl_beta` -- those were varied across R1-R3b and are no longer the open question.

## What this means for the guide

* The **serving-side** half of a no-Kubernetes RL loop is demonstrably workable on bare processes:
  routing every rollout through Envoy + EPP, checkpoint -> atomic rename -> drain -> restart ->
  republish, prefix-cache reuse after an update, and per-stage timings all behave.
* The **learning-side** half should not be presented as "run GRPO on a small model with an
  exact-match reward and it improves". In the later rounds (R3b/R4): 0.5B, group 8, 12 max_tokens,
  24 prompts, 192 requests per version -- it does not, and neither the optimiser nor the loss span rescues it. A reader
  following such a recipe on one GPU will see a working server and a destroyed policy.
* If the guide wants a working small-scale example, the candidates below are the ones the evidence
  points at; none of them was run here, and they are listed without results on purpose.

## Next steps (declared in advance, not run here)

* per-token or process rewards instead of one scalar per sequence (reward each answer token, or
  reward format separately from the value)
* a larger base model, where the competent region is wider relative to the update
* a longer warmup / smaller effective step schedule, tested as a follow-up and not as another
  unilateral optimiser tweak
* an off-policy or rejection-sampling objective, so an update never moves on batches whose reward
  spread is zero

## Not claimed

* Not a general statement about RL with llm-d serving. This is one host, one 0.5B base model, one
  task shape (a short integer answer), one reward (binary exact match), and a GRPO-style update.
* No absolute throughput is reported: the host is shared and every timing above is either paired or
  labelled with its loadavg.
* Nothing was pushed and no code PR is proposed -- this is a report, and it was written while
  recording the host's loadavg and the co-tenant GPU state at each stage.

## Evidence

`metrics/{r3b_gates.json,r4_gates.json,rollout_v{0,1,2}.json,train_v{0,1}_to_v{1,2}.json,transition_v{0,1}_to_v{1,2}.json,timings.jsonl,probe_matrix.json,r4-progress.jsonl}`,
`effective-config/a4-m3-r3/r3b-addendum.json` (2026-09-20T06:12:00Z),
`effective-config/a4-m3-r4/{preregistration.json,acceptance.json}` (2026-09-20T15:55:01Z),
`evidence/r4-gpu-*.csv`, `R3B_REPORT.md`, `R4_REPORT.md`.
Floors and gates are read back from the files written before each measurement; failed rounds are
kept, including the one whose v2 point is `null` because the host went down mid-round.

