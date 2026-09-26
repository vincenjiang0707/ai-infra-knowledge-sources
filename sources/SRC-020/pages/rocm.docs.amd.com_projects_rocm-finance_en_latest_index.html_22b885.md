source: https://rocm.docs.amd.com/projects/rocm-finance/en/latest/index.html

# AMD Finance documentation[#](https://rocm.docs.amd.com#amd-finance-documentation)

2026-07-30

1 min read time

Within the ROCm ecosystem, the AMD Finance toolkit includes production‑ready support for industry‑leading Gradient Boosting Machine (GBM) libraries for high-performance finance use cases:

Finance use cases |
|
|
|
|---|---|---|---|
Best for |
General use |
Large datasets |
GPU-intensive tasks |
Tree growth strategy |
Level-wise |
Leaf-wise |
Level-wise (GPU) |
Categorical feature handling |
Manual encoding |
Manual + binning |
Manual encoding |
Overfitting control |
L1/L2 + early stop |
L1/L2 + sampling |
Regularization |

These components are accelerated on AMD Instinct GPUs through optimized ROCm libraries, leveraging the latest AMD GPU architectures. ROCm enablement of these libraries introduces optimized kernels, memory‑management enhancements, and seamless multi‑GPU scaling, delivering performance gains over CPU-only baselines in intensive workloads.

The AMD Finance source code is hosted on GitHub at
[AMD-Ecosystem/ROCm-finance](https://github.com/AMD-Ecosystem/ROCm-finance).

AMD Finance documentation is organized into the following categories: