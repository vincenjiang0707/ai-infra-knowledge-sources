# [Issue #2550] [Docs]: Propose a Kthena variant of the P/D disaggregation guide

source: https://github.com/llm-d/llm-d/issues/2550
state: open | updated: 2026-09-23T01:29:21Z
labels: 

## 正文

### Feature Area

Documentation / Guides

### Problem Statement

We would like to contribute a Kthena ModelServing variant of the existing P/D disaggregation guide, following #2052. The integration uses existing router functionality and requires no runtime changes. Before preparing the PR, we'd like to confirm whether this deployment variant belongs in the llm-d guides.

Users running model servers under Kthena need to configure entry-versus-worker selection, role filters, the decode routing sidecar, and ServingGroup screening. A runnable example would bring these pieces together and explain the distinction between per-role workload revisions and KV-transfer compatibility.

### Proposed Solution

Add a deployment variant under `guides/pd-disaggregation/` with:

- ModelServing manifests for prefill and decode, including the decode routing sidecar.
- Router configuration that selects entry Pods, identifies roles, and constrains P/D selection to a ServingGroup.
- Deployment, request verification, and cleanup steps.
- An explanation of ServingGroup identity, per-role revisions, and KV compatibility.

We would reuse the existing guide components where possible and link to Kthena documentation for controller installation. Before submitting the PR, we would update and validate the example against the versions used by the current guides.

Would this fit as another deployment variant of the existing P/D guide?

### Alternatives Considered

Keep the complete example in Kthena's documentation and add a short reference from the llm-d P/D guide. This would reduce maintenance in llm-d, but leave the example outside the existing guide validation workflow.

### Willingness to Contribute

Yes, I can submit a PR

### Additional Context

Related precedent: #2052, which added a DisaggregatedSet variant of the P/D guide.

#### Existing experiment

The following configuration and results were recorded in our earlier integration experiment; this is not a validation of current llm-d main.

| Component | Configuration |
| --- | --- |
| Kubernetes | 1.36 |
| llm-d Router and disaggregation sidecar | v0.10.0 |
| vLLM | 0.27.0 |
| Model | Qwen3.5-27B |
| Prefill | 4 × NVIDIA L2, TP4, node A |
| Decode | 4 × NVIDIA L2, TP4, node B |
| KV transfer | NixlConnector with UCX |
| Ports | Prefill: 8000; decode sidecar: 8000; decode vLLM: 8200 |

Requests entered through Envoy, with EPP selecting the P/D endpoints and the decode sidecar coordinating prefill and decode across the two nodes.

A successful chat completion returned these fields (excerpt):

```json
{
  "model": "qwen38-27b",
  "content": "llmd-pd-ok",
  "finish_reason": "stop",
  "system_fingerprint": "vllm-0.27.0-tp4-396e4bd4",
  "usage": {
    "completion_tokens": 6,
    "prompt_tokens": 21,
    "total_tokens": 27
  }
}
```

During setup, cross-node transfer initially encountered `handshake_setup_failed` and `NIXL_ERR_BACKEND`. After setting `UCX_NET_DEVICES=eth0` and `UCX_TLS=tcp,cuda_copy` for this environment, the recorded NIXL error check was `NONE`, prefill returned KV-transfer metadata, and decode completed generation without the previous transfer errors. These network settings describe the tested environment, not a general recommendation.

We also updated only the decode role to add the sidecar and change the model-server port. Prefill retained its existing revision:

```text
ROLE      REVISION
prefill   678d977c6d
decode    5f55b4d589
```

The resulting pair could serve P/D requests despite having different workload revisions. This illustrates why workload revision equality is not a general KV-compatibility requirement. Conversely, membership in the same ServingGroup does not guarantee KV compatibility.

These results cover functional inference on the tested configuration. We have not established throughput, TTFT/ITL, or disruption-free rolling-update behavior.


## 评论 (2)

### robertgshaw2-redhat · 2026-09-22

quick question --- I am not super familiar with Kthena

From a breif review of the docs https://kthena.volcano.sh/docs/intro, it seems Kthena has significant overlap with llm-d, for instance

<img width="728" height="395" alt="Image" src="https://github.com/user-attachments/assets/295f4af5-2a4e-4449-86d9-2f99bf8221c0" />

Can you help clarify how to think about how the two projects come together?



### acsoto · 2026-09-23

@robertgshaw2-redhat Hi robert

Yes, there is overlap at the project level. I should have made the scope clearer: this proposal uses Kthena’s ModelServing workload controller, rather than its full serving stack.

In this setup, ModelServing manages the P/D Pods, their grouping, replicas, and rollout lifecycle. llm-d Router handles endpoint selection and P/D request coordination through its EPP and decode sidecar. 

This is similar in scope to the DisaggregatedSet deployment variant in #2052: an alternative workload controller underneath the existing llm-d routing path. The intended audience is users already managing workloads with Kthena who want to use llm-d’s routing capabilities. The guide would document that composition and its boundaries.

You can refer to this https://kthena.volcano.sh/docs/next/ecosystem/llm-d-router-with-kthena
