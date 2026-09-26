# gpu-accelerated-clustering-for-financial-instruments-at-scale

source: https://developer.nvidia.com/blog/gpu-accelerated-clustering-for-financial-instruments-at-scale/

*Use AdaptGrow, a GPU-accelerated matrix factorization algorithm, to turn rolling correlation and tail-dependence matrices into hard clusters, soft factor loadings, and structural-break signals at single-GPU and multi-node scale*

Quant strategies routinely group instruments for portfolio construction, risk aggregation, statistical arbitrage, and trade surveillance. Incorrect groupings can make concentrated positions appear diversified, obscure risk shared across nominal boundaries, and select statistical-arbitrage pairs whose relationships fail under stress.

The practical difficulty is that the right groupings are neither directly observable nor stable. Factor exposures drift, instruments change classifications, and dependencies can change sharply during market stress. A clustering pipeline must therefore separate routine variation from structural change and be inexpensive enough to rerun as new returns arrive.

There are two common ways to group instruments from a dependence matrix. Hard clustering methods are computationally cheap but assign every instrument to exactly one group, which breaks down at sector boundaries and masks the graded exposures that matter for risk budgeting. Soft factorization methods like SymNMF handle boundary instruments and produce usable factor loadings, but their dense matrix objectives have historically limited practical use to moderate instrument counts rather than the scale at which this problem actually lives.

This post covers a workflow that addresses both limitations. The workflow starts with rolling return windows and constructs two complementary inputs: absolute Pearson correlation for broad co-movement and the tail pairwise dependence matrix (TPDM) for joint behavior during extreme observations. SymNMF represents each instrument through a row of nonnegative factor loadings. Retaining the row provides a soft representation; taking its argmax produces a hard label.

A memory-efficient SymNMF formulation reduces peak storage from ~20n2 to ~4n2 bytes, which is what makes ~100,000 instruments fit on a single NVIDIA GB200. For larger problems, a distributed implementation row-shards the dependence matrix and reduces communication to O(nk) rather than O(n2), enabling factorization of one million instruments across 16 nodes. A single adaptive solver, AdaptGrow, handles both correlation and tail-dependence inputs by reading the eigenspectrum to choose between full-batch and block-stochastic gradients, eliminating the need to select or tune separate solvers for different input structures.

The result is a clustering pipeline that produces hard labels, soft factor loadings, and structural-break signals, reruns cheaply as new returns arrive, and scales from a single GPU to multi-node infrastructure without changing the solver interface.

A companion notebook, linked below, implements the full pipeline and reproduces all results in this post.

## Factorization at scale

Scale is constrained first by memory. A dense FP32 dependence matrix requires ~40 GB for 100,000 instruments and ~4 TB for 1 million instruments. A naive SymNMF implementation also materializes several additional n x n intermediates. The trace-based formulation used here eliminates those intermediates, reducing estimated peak storage from approximately 20n2 bytes to 4n2 bytes plus smaller factor buffers. This change is what makes approximately 100,000 instruments fit on one high-memory GPU.

NVIDIA acceleration enters at each stage of the pipeline. PyTorch dispatches the dominant SH matrix multiplications to cuBLAS. cuSOLVER performs the spectral probe used for rank and solver selection. cuDF keeps optional Parquet ingestion and preprocessing on the GPU. For scale-out, PyTorch Distributed row-shards S while keeping a replica of H on each worker. NCCL all-gathers the row-sharded S H products and all-reduces the gradients, so communication operates on O(nk) data rather than the full O(n2) matrix. The environment is packaged with an NVIDIA NGC PyTorch container and `cudf-cu13`

.

In the [companion paper](https://arxiv.org/abs/2607.24518), the 100,000-instrument matrix was distributed across four NVIDIA GB200 GPUs for faster execution, although its 40 GB input fits on one GB200. Across three seeds in FP32, AdaptGrow converged in 13.0 seconds on correlation and 12.4 seconds on TPDM. At 1 million instruments, the 4 TB matrix was row-sharded across 64 GB200 GPUs on 16 nodes; full-batch AdaGrad completed the correlation factorization in approximately 2 minutes, while AdaptGrow completed the TPDM factorization in approximately 4 minutes. These are individual factorization measurements, not end-to-end timings for all 250 temporal windows.[ ](https://arxiv.org/abs/2607.24518)

## The temporal setup

The workflow evaluates 250 rolling windows, approximating daily re-clustering over one trading year. The synthetic return stream contains two controlled events: instruments changing their planted group membership and several groups experiencing a joint tail-stress episode without changing membership.

This controlled setup verifies two different behaviors. Adjusted Rand index (ARI) should identify the membership change, while TPDM should expose the co-crash that ordinary correlation largely misses. For production use, replace the synthetic generator with a returns table while preserving the same windowing, dependence-estimation, factorization, and monitoring stages.

The million-instrument results are separate distributed scale tests and require infrastructure comparable to the published 16-node configuration.

## Choosing the rank k

Start by inspecting the leading eigenvalues from an initial representative window. Choose k at the clearest separation between signal eigenvalues and the noise floor, then keep k fixed across subsequent windows so that stability scores remain comparable. The synthetic data used here has a planted rank of 24. Production data may not contain a sharp gap, so rank selection should also be checked against cluster interpretability and stability.

## Factorizing with SymNMF

For each rolling window, the workflow passes the dependence matrix S and selected rank k to AdaptGrow. The solver returns H, where each row of H contains an instrument’s soft factor loadings, and taking the row-wise argmax produces a hard cluster label.

Each window uses the same fixed-seed initialization and is fitted independently rather than warm-started, preventing previous labels from masking a genuine reclassification. AdaptGrow is a single adaptive solver that auto-configures from the matrix’s eigenvalue spectrum. Both regimes use the same per-coordinate AdaGrad preconditioner and differ only in how the gradient is computed. AdaptGrow seeds its batch fraction from the post-rank eigenvalue gap described in more detail below.

A clean gap selects the full gradient. A flatter post-rank spectrum starts with a cheaper block-sampled gradient corrected using Stochastic Variance Reduced Gradient (SVRG), then expands the sample toward the full gradient if progress stalls. The same solver runs unchanged from one GPU to many.

Mathematically, the diagonal AdaGrad update is defined as:

where g is either the full gradient ∇f(H) (full-batch branch) or a block-sampled estimate of it (stochastic branch), with all operations above being element-wise.

## Why this solver

After selecting the factorization rank k, AdaptGrow examines the post-rank gap ratio

`# phi is seeded from the post-rank eigenvalue gap:` `# gamma_{k+1} >= 5 selects the full gradient; otherwise start sampled` `def` `adaptgrow(S, k, lr, phi` `=` `None` `, steps` `=` `2000` `, eps` `=` `1e` `-` `8` `):` ` ` `phi ` `=` `phi ` `if` `phi ` `is` `not` `None` `else` `seed_from_eigenspectrum(S, k)` ` ` `# fixed-seed init, independent per window (no warm-start)` ` ` `H ` `=` `scale_matched_init(S, k) ` ` ` `# diagonal (per-coordinate) AdaGrad accumulator` ` ` `G ` `=` `torch.zeros_like(H) ` ` ` `for` `t ` `in` `range` `(steps):` ` ` `# clean post-rank gap` ` ` `if` `phi >` `=` `1.0` `: ` ` ` `g ` `=` `4` `*` `(H @ (H.T @ H) ` `-` `S @ H)` ` ` `# flat post-rank spectrum` ` ` `else` `: ` ` ` `g ` `=` `block_svrg_grad(S, H, phi)` ` ` `# same diagonal AdaGrad update either way` ` ` `G ` `+` `=` `g ` `*` `g` ` ` `# projected step ` ` ` `H ` `=` `(H ` `-` `lr ` `*` `g ` `/` `(G.sqrt() ` `+` `eps)).clamp_min(` `0` `) ` ` ` `# grow sampled fraction toward full gradient` ` ` `if` `stagnating() ` `and` `phi < ` `1.0` `: ` ` ` `phi ` `=` `min` `(` `2` `*` `phi, ` `1.0` `)` ` ` `return` `H` |

## Spherical k-means for direct hard clustering

When only one label per instrument is required, spherical k-means provides a lower-cost baseline. It clusters the L2-normalized rows of S using cosine similarity, making it the appropriate comparison for SymNMF on this dependence geometry. The companion paper establishes the formal relationship between the two objectives. In practice, use spherical k-means for well-separated hard clusters and SymNMF when soft factor loadings or boundary instruments matter.

### Tracking stability through time with the Rand index

The same pipeline runs on two dependence matrices that share the latent structure but measure different things:

- Correlation captures co-movement across the full return distribution, driven by the body of the data.
- TPDM captures co-movement conditional on extreme events, which is what drives drawdowns and joint tail risk.

With k fixed and each window factored independently, the study is simple: factor every St, hard-label by argmax on H, and ask how the labels change as the window slides.

### The metric

Since cluster labels are arbitrary across runs, pairs of instruments were compared instead. The ARI scores how often two clusterings put the same pair together or apart, giving 1 for identical clusterings and about 0 for unrelated ones.

### Stability and break detection

ARI(t-Δ, t) is tracked, comparing each window with the one a full window width earlier, where Δ = 50 steps is that width. Consecutive windows overlap by all but one stride, so a reclassification enters gradually and barely moves the step-to-step ARI(t-1, t); spacing the comparison a full width apart lets the accumulated change register as a real dip.

In this synthetic experiment, both curves sit high during the calm period (baseline ARI ≈ 0.93 for correlation and ≈ 0.80 for the noisier, tail-sensitive TPDM), then drop sharply when the window crosses the reclassification event before recovering.

To turn that dip into an alert, the workflow overlays a self-calibrating 3σ control limit: it calibrates on the calm pre-break windows and flags any drop below the limit, without any pre-set threshold.

Why have different tail and body estimators? A co-crash changes co-movement, not group membership, so the relabeling metric doesn’t register it. The hard labels and the correlation curve stay unmoved, and by correlation the stressed sectors still look diversified.

To detect it, the cross-sector dependence is measured among those sectors directly, in each matrix, over time. At the crisis peak, correlation reads just ≈ 0.04 while the TPDM reads ≈ 0.13, several times higher, because the same sectors share tail dependence that correlation never registers. Off the diagonal, the correlation block stays dark while the TPDM’s stressed-sector block lights up. In this synthetic episode, the co-crash is muted in correlation but visible in the TPDM’s cross-sector dependence, even though the hard cluster labels do not change.

## Between spherical k-means and SymNMF

In this synthetic experiment, the two methods recover the same broad structure but differ on a small, important subset of instruments. On the well-separated correlation matrix they reach a cross-method ARI of about 0.83, close enough that spherical k-means is a reasonable approximation but not interchangeable with SymNMF. About 9% of instruments sit at a boundary between clusters, which hard argmax must assign to a single group while the soft factorization keeps them split across both.

The two methods diverge further as the eigenvalue spectrum collapses toward a single dominant factor (the near-rank-1 TPDM regime the paper studies at scale). There every row of S aligns with nearly the same leading direction, so instruments are no longer separable by angle and a hard spherical partition is unstable.

SymNMF retains graded factor loadings in H, which is the useful output when hard cluster labels are no longer well defined. Spherical k-means is therefore the computationally more efficient choice when sectors are angularly well-separated and hard clusters are enough, while SymNMF provides results interpretable both as soft and hard clustering.

## Get started with GPU-accelerated instrument clustering

SymNMF’s dense objective previously limited practical implementations to moderate matrix sizes. The memory-efficient GPU implementation extends that capacity to approximately 100,000 instruments on one NVIDIA GB200 GPU and 1 million instruments across multiple nodes. AdaptGrow uses the eigenspectrum to select either full-batch AdaGrad or lower-cost block-stochastic updates, enabling the same workflow to adapt to clean-gap and flat-spectrum inputs.

The workflow applies this pipeline across 250 synthetic windows using both SymNMF and its matched spherical k-means baseline. The resulting soft loadings, hard labels, and stability diagnostics can support statistical arbitrage, momentum signals, market-neutral portfolio construction, exposure control, and risk budgeting while identifying structural breaks.

## Notebook

The companion notebook reproduces all results in this post, including:

- Generating the synthetic return stream
- Constructing rolling correlation and TPDM matrices
- Selecting the factorization rank
- Running SymNMF and spherical k-means
- Deriving hard and soft cluster outputs
- Calculating adjusted Rand index stability scores
- Detecting the planted structural break
- Reproducing the three figures in this post

Run

end to end—rolling S[clustering_through_time.ipynb](https://github.com/NVIDIA/SymNMF-factors/blob/main/notebooks/clustering_through_time.ipynb)t, independent SymNMF fits, argmax labels, and the stability, tail-risk, and k-means figures. Deploy on [build.nvidia.com](https://build.nvidia.com) with [NVIDIA Brev](https://build.nvidia.com/gpu), or on your own GPU from the [repository](https://github.com/NVIDIA/SymNMF-factors/).

## Stack

[PyTorch](https://pytorch.org) + [cuDF](https://developer.nvidia.com/cudf): [cuBLAS](https://developer.nvidia.com/cublas) for the S·H GEMMs, [cuSOLVER](https://developer.nvidia.com/cusolver) for the spectral probe, [NCCL](https://developer.nvidia.com/nccl) for the distributed runner; cuDF handles on-GPU Parquet ingest (optional, with a pandas fallback). One container: an [NGC PyTorch image](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/pytorch) plus cudf-cu13.

## Scale-out

Distributed PyTorch and NCCL implementations of both algorithms operate on a row-sharded S. AdaptGrow has been validated on up to 64 NVIDIA GB200 GPUs across 16 nodes. The repository’s `scripts/run_distributed.py`

configures multi-node execution with `torchrun`

or Slurm; deployment instructions are provided in `scripts/README.md`

.

## Learn more

- Companion technical paper (SymNMF derivation, spectral rank selection, and GPU speed-up ladder):
*Low-Rank Dependence Decomposition via Accelerated Symmetric Non-negative Matrix Factorization* - Source repository and
`clustering_through_time.ipynb`

notebook:[NVIDIA/SymNMF-factors](https://github.com/NVIDIA/SymNMF-factors/)

## Start the discussion at forums.developer.nvidia.com
