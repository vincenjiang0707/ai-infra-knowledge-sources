# [Issue #2168] [RFC]: Community-Driven Infrastructure Provisioning & Conformance Strategy for llm-d

source: https://github.com/llm-d/llm-d/issues/2168
state: open | updated: 2026-09-18T20:06:14Z
labels: enhancement

## 正文

### Feature Area

Documentation / Guides

### Problem Statement

Setting up an environment to run **llm-d** involves two distinct operational layers:

1. **Infrastructure Provisioning**: Preparing a Kubernetes cluster with hardware accelerators, high-performance networking, CRDs, etc., so it is fully ready to host `llm-d`. 
2. **Stack Installation**: Deploying `llm-d` software components, which is strictly owned and documented by canonical **well-lit path guides**.

These infrastructure requirements must align across multiple configuration dimensions, including the specific well-lit path guide, infrastructure provider, accelerator, etc..

The llm-d stack installation well-lit path guides are generally well maintained and CI-validated. However [infrastructure provisioning guides](https://github.com/llm-d/llm-d/tree/main/docs/infrastructure) are loosely maintained and lack continuous validation. Multiple infra provisioning methods have evolved in the community such as terraform or AI skills, see [Current Infrastructure Provisioning Approaches](?tab=t.0#heading=h.tjdpp5rwbkzn). 

**The dilemma**

If core `llm-d` attempts to maintain official provisioning scripts, Terraform modules, and AI skills across every cloud provider (GKE, EKS, AKS, On-Prem) and accelerator type (NVIDIA GPU, Google TPU, AMD, Intel XPU), engineering velocity on core inference features will stall. Conversely, without clear standards, third-party provisioning methods may fail silently or produce misconfigured clusters.

### Proposed Solution

To address the diverse requirements of infrastructure provisioning tooling for the stack, and a scalable maintenance structure, we propose that core `llm-d` will adopt the following strategy that clearly separates core `llm-d` vs. community contribution boundaries:



1. **llm-d **
    1. llm-d will NOT maintain tooling/guide for per-provider infra provision. This will be shifted to the (new) `llm-d-infra-providers` repo.
    2. llm-d SHOULD host the **Infra Conformance Suite** as the source of truth, contributed by each provider. 
        1. Hosting them in llm-d repo ensures a centralized discovery and consistency checking.
        2. These are executable test suites that validate if a cluster is ready to deploy llm-d.
        3.  The conformance suite is a collection of tests, each labeled with applicable dimensions (chip, rdma, dra, etc.). This allows filtering a list of required conformance tests to pass for a given dimensional space.
2. **llm-d-infra-providers (new repo)** 
     
     1.  **Ownership Model: **This is community owned. Create sub-folders for each provider, and each provider is responsible for reviewing PRs for their own sub-folder.
    4. **Existing Documentation**: Move existing [docs/infrastructure](https://github.com/llm-d/llm-d/tree/main/docs/infrastructure) to the new repo. 
    5. **Quality: **The infra provisioning tools should be qualified against the conformance test suite.
This model removes maintenance overhead from core llm-d, and motivates providers to contribute and improve their infra provisioning experience for llm-d users.





### Alternatives Considered

_No response_

### Willingness to Contribute

Yes, I can submit a PR

### Additional Context

For more details please feel free to comment on this doc: https://docs.google.com/document/d/1lBaH8YPRovsjaoJlklISrTyJPW2aczB9kaEEODroEeM/edit?pli=1&tab=t.0#heading=h.wino7477jklf

## 评论 (7)

### liu-cong · 2026-08-04

cc @yangligt2 @gushob21 @ahg-g @chcost @robertgshaw2-redhat @xiaojun-zhang 

### robertgshaw2-redhat · 2026-08-04

i think this is a great idea. especially focus on the accelerated networking is key in my eyes

### gushob21 · 2026-08-04

I like the idea of new repo llm-d-infra-providers. However, we should define how we want the code to be present in the new repo.  For example, we do the GKE provider work for llm-d in accelerated-platforms repo and it will be duplicate to copy the code/guide to the llm-d-infra-providers repo and maintain it. Would it be OK if the folder for a provider in llm-d-infra-providers points to another git repo?

### xiaojun-zhang · 2026-08-04

like the idea! We did run into the issues mentioned above for XPU CI. 

### liu-cong · 2026-08-05

> I like the idea of new repo llm-d-infra-providers. However, we should define how we want the code to be present in the new repo. For example, we do the GKE provider work for llm-d in accelerated-platforms repo and it will be duplicate to copy the code/guide to the llm-d-infra-providers repo and maintain it. Would it be OK if the folder for a provider in llm-d-infra-providers points to another git repo?

@gushob21 

Yeah this is OK. I don't think we should dictate how each provider should document their infra provision. It's going to be very provider specific I think. The point is that `llm-d-infra-providers` is the centralized discovery mechanism. Each provider can then have the flexibility to define their UX such as linking to other docs/repos. 

### liu-cong · 2026-08-06

also cc @chewong 

### yangligt2 · 2026-09-18

Execution issue for the new repository: #2427 (`[Incubation] llm-d-infra-providers`). It carries the PoC (https://github.com/yangligt2/llm-d-infra-providers-poc), the per-provider OWNERS model discussed above, and a provider-owner nomination table. Approval and repo-creation requests are tracked there.
