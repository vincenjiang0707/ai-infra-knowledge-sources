# [Issue #2427] [Incubation] llm-d-infra-providers: community-owned infrastructure provisioning for llm-d

source: https://github.com/llm-d/llm-d/issues/2427
state: open | updated: 2026-09-23T22:02:39Z
labels: 

## 正文

## Summary

This is the concrete execution step for RFC #2168: create `llm-d-incubation/llm-d-infra-providers`, the community-owned home for per-provider infrastructure provisioning tooling and guides (everything up to "the cluster is ready to host llm-d"). One sub-folder per provider, each with its own OWNERS reviewing its own PRs. Any provisioning method is acceptable (guided docs, scripts/IaC, AI skills), and per the discussion in #2168 a provider sub-folder may link out to externally hosted tooling; this repo is the centralized discovery entry point. Provisioning tooling is qualified against a dimension-labeled conformance/validation suite rather than by prescribing a method.

## Why

Running llm-d has two layers: infrastructure provisioning (accelerators, RDMA networking, drivers, CRDs) and stack installation (well-lit path guides). The guides are maintained and CI-validated; `docs/infrastructure` is loosely maintained, and core llm-d cannot own provisioning tooling for every provider and accelerator without stalling core velocity (see #2168 for the full problem statement; feedback there has been supportive, including from project maintainers).

## Scope

In scope:
- Per-provider provisioning tooling/guides (`providers/<name>/` with per-provider OWNERS), including links to externally hosted provider tooling
- Migration of `llm-d/docs/infrastructure` provider and gateway content
- Pilot home of the dimension-labeled conformance/validation suite (runner + checks + fabric micro-tests) until #2168 settles its final location (the RFC targets core llm-d as the source of truth; the check contract is layout-independent so the move is mechanical)

Out of scope:
- Stack installation (owned by the well-lit path guides in core llm-d)
- Any change to core llm-d release/CI processes

## Evidence: working PoC

https://github.com/yangligt2/llm-d-infra-providers-poc - ready to transfer as the initial content:
- Repo skeleton with GOVERNANCE/CONTRIBUTING/per-provider OWNERS; GKE as pilot provider (guided docs, deterministic provisioning scripts for the DRA+DRANET and multi-networking+gIB paths, and an AI skill); AKS/DigitalOcean/minikube/OpenShift docs migrated from `docs/infrastructure` and awaiting owners.
- Conformance/validation suite: `llmd-infra-check` runner, static checks and NCCL/NIXL fabric micro-tests labeled with the same dimensions the guides use (infra_provider, accelerator, rdma, dra, router_mode, gateway_provider).
- Validated on live GKE clusters. On an 86-node A4X (GB200) cluster the full run passes including the two-node NCCL micro-test: peak bus bandwidth 189.3 GB/s, ~95% of the 4x400G line rate, with sanitized captures committed under `conformance/examples/`.

## Relationship to existing repos

- Distinct from `llm-d-incubation/llm-d-infra` (helm charts for deploying llm-d); this repo is about cluster readiness, not stack deployment.
- `llm-d-incubation/hermes` (cluster configuration scanning / self-test generation) is adjacent to the validation suite; we propose reconciling the two in sig-installation as part of the first milestone rather than blocking repo creation on it.

## First milestone

- [ ] Repo created; PoC content transferred with README stating purpose and goal (per PROJECT.md incubation rules)
- [ ] Provider ownership drive in #sig-installation; seed OWNERS for at least one non-GKE provider
- [ ] Migrate/redirect `llm-d/docs/infrastructure` provider content
- [ ] Resolve the conformance suite's final home in #2168 (core llm-d vs. plugin-path split)
- [ ] Full micro-test qualification runs for the GKE pd-disaggregation and wide-ep-lws profiles

## Maintainers

The ownership model is per-provider: each `providers/<name>/` sub-folder carries its own OWNERS file, and contributions touching a given provider's infrastructure are approved by that provider's maintainers, not by the repo-level maintainers. We explicitly want a maintainer from each infra provider to own approvals for their sub-folder, and ask each provider to nominate at least one. Repo-level maintainers only curate repository structure and the shared conformance framework.

Bootstrap (repo-level and GKE provider):
- @yangligt2 (Google)
- @liu-cong (Google)

## The ask

Create `llm-d-incubation/llm-d-infra-providers` as an incubation repository. SIG: Installation.

/cc @liu-cong @gushob21 @ahg-g @chcost @robertgshaw2-redhat @xiaojun-zhang @chewong


## 评论 (3)

### yangligt2 · 2026-09-18

Two concrete requests to move this forward, following the pattern used for #2193, #2088 and #1154.

### 1. Decision: create the repository

@ahg-g @robertgshaw2-redhat @chcost - the underlying RFC #2168 already has maintainer support (Rob: "great idea, especially the focus on accelerated networking"; Abdullah's platform-per-directory concern from #2168 is addressed by the per-provider OWNERS model above). Requesting an explicit `/lgtm` here so this can be executed under lazy consensus.

@davidgs - once approved, could you create `llm-d-incubation/llm-d-infra-providers` as you did for #2088? We will seed it from the PoC and add the required `CONTRIBUTING.md`, `MAINTAINERS.md`, `OWNERS`, `SECURITY.md` and `.gitignore` in the first PR.

### 2. Provider ownership: who approves what

The repo is organized as `providers/<name>/` with a per-provider `OWNERS` file. Contributions touching a provider's infrastructure are approved by that provider's maintainers, not by repo-level maintainers. The mapping below is derived from `docs/infrastructure`, guide overlays, nightly workflow authorship and `OWNERS` files in `llm-d/llm-d`. If you are tagged, the question is: **would you be listed in `OWNERS` for that provider, or can you name who should be?** Pointing the sub-folder at an externally hosted repo is fine (see #2168 discussion).

| Provider sub-folder | Current content in llm-d | Candidate OWNERS |
|---|---|---|
| `gke` (GPU, TPU, GKE Gateway) | `docs/infrastructure/providers/gke`, `gateway/gke.md`, `*/gke` overlays, `gke-*` nightlies | @yangligt2 @liu-cong (confirmed); @huaxig @rlakhtakia @gushob21 @BenjaminBraunDev |
| `aks` | `docs/infrastructure/providers/aks` | @sulixu @chewong @liulanze |
| `digitalocean` | `docs/infrastructure/providers/digitalocean` | @sudoalok @iambigmomma |
| `openshift`, `openshift-aws`, `minikube` | `docs/infrastructure/providers/{openshift,openshift-aws,minikube}` | @Gregory-Pereira @zdtsw @nerdalert |
| `aws` (EFA) | `pd-disaggregation/*/aws` overlays, `images/gpu-vllm/aws-efa` | @Gregory-Pereira @erezzarum |
| `coreweave` (CKS) | `*/coreweave` overlays, `cks-*` nightlies | @wseaton @BenjaminBraunDev - a CoreWeave nominee would be preferable |
| `amd` (ROCm clusters) | `*/amd` overlays, `amd-*` nightlies | @vcave |
| `intel` (XPU clusters) | `*/xpu` overlays, `intel-*` nightlies | @xiaojun-zhang @XinyuYe-Intel @yao531441 @yuanwu2017 |
| `ibm` (RDMA/IB clusters used by `ibm-*` nightlies) | `docs/infrastructure/rdma`, `ibm-*` nightlies | @diegocastanibm @mamy-CS @praveingk |
| `gateway-providers/` (Istio, agentgateway, Envoy AI Gateway, GKE Gateway) | `docs/infrastructure/gateway/*` | @alexagriffith @liulanze @nacx @rlakhtakia |

@maugustosilva @diegocastanibm - you own most of the nightly environments; the conformance suite is meant to run as a pre-flight in those lanes, so your input on the check contract is welcome even without provider ownership.

If a provider ends up with no owner, its migrated docs stay in the repo marked "owners needed", as in the PoC today.


### github-actions[bot] · 2026-09-18

Cannot apply the lgtm label because Error: yangligt2 is not included in the reviewers role in the OWNERS file

### OguzPastirmaci · 2026-09-21

+1 to creating the repo. I would like to nominate myself and @dkennetzoracle as owners for an OKE (Oracle Kubernetes Engine) provider folder.

Background: I work on AI infrastructure at Oracle Cloud, maintain [oracle-quickstart/oci-hpc-oke](https://github.com/oracle-quickstart/oci-hpc-oke) (Terraform-based provisioning for GPU and RDMA clusters on OKE), and contribute OKE support to [kubernetes-sigs/dranet](https://github.com/kubernetes-sigs/dranet).

I plan to start with guided docs under providers/oke/ that link out to oci-hpc-oke for provisioning, then add llmd-infra-check results from OKE.
