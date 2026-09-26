# [Issue #2308] [Announcement] NCCL EP and NCCL M2N are moving to NVIDIA/nccl-extensions

source: https://github.com/NVIDIA/nccl/issues/2308
state: open | updated: 2026-09-18T01:55:12Z
labels: Community Discussion

## 正文

We are moving NCCL EP and NCCL M2N from the NCCL `contrib/` directory to the recently open-sourced [NVIDIA/nccl-extensions](https://github.com/NVIDIA/nccl-extensions) repository.

The new repository is the primary home and source of truth for:
- [nccl_ep](https://github.com/NVIDIA/nccl-extensions/tree/main/nccl_ep) — optimized dispatch and combine primitives for Expert Parallelism and Mixture-of-Experts workloads.
- [nccl_m2n](https://github.com/NVIDIA/nccl-extensions/tree/main/nccl_m2n) — mesh-to-mesh tensor transfer and resharding primitives, including communication between disjoint training and inference process groups.

### Why we are making this change

The NCCL [contrib/](https://github.com/NVIDIA/nccl/tree/master/contrib) directory provides a place for independently maintained projects that build on NCCL's public host and device APIs. It has been valuable for introducing and developing new communication capabilities alongside NCCL.

As some of these projects gain broader adoption, development activity, and community interest, a dedicated repository provides a clearer and more scalable home for them. In particular, nccl-extensions enables:
- Focused issue tracking and code review for extension-specific work.
- A development lifecycle that can evolve independently of the NCCL core repository.
- A single destination for emerging AI communication patterns built on NCCL APIs.
- Clearer ownership and contribution paths for users and developers.

### Where to submit issues and contributions

Effective immediately, please direct all new bug reports, feature requests, questions, and pull requests related to NCCL EP or NCCL M2N to the [NVIDIA/nccl-extensions](https://github.com/NVIDIA/nccl-extensions) repository:

- [Open an issue](https://github.com/NVIDIA/nccl-extensions/issues/new)
- [Open a pull request](https://github.com/NVIDIA/nccl-extensions/compare)

Issues and pull requests concerning NCCL core should continue to be submitted to this repository.

### Future contrib/ transitions

We expect to follow a similar approach for other projects in `contrib/` when their adoption, scope, and development activity would benefit from a dedicated home. These transitions will be evaluated individually and communicated to the community when appropriate.

Thank you to everyone who has used, tested, contributed to, and provided feedback on NCCL EP and NCCL M2N. We look forward to continuing their development in NCCL Extensions.


## 评论 (2)

### xiaofanl-nvidia · 2026-08-23

Assigning to myself to remove ep and m2n from contrib/ after a while. Currently planning removal before 2.32U1 release. Please let us know if that'll break anyone's production workflow and we can keep it for a bit longer. 

### 0z5a · 2026-09-18

Following the EP/M2N migration, I'd like to take a small, test-only M2N task: hardening the byte-pattern initializer/validator against aligned block-misrouting blind spots.

The current tests/test_helpers.cu uses globalIdx % 256. For a 1-D tensor, swapping 256-byte blocks leaves the test payload unchanged. I'd add a deterministic global-position-dependent pattern and targeted negative tests, then validate same-dim and cross-dim resharding on multi-GPU L20 hardware.

This is a test-oracle limitation identified from the source, not a reproduced NCCL transport bug. The first PR would stay within test helpers, regressions, and documentation, without changing communication kernels or protocols.

Is anyone already working on this, and what would be the preferred tracking issue in nccl-extensions?
