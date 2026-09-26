# run-massive-scale-umap-in-minutes-using-multiple-gpus-without-losing-accuracy

source: https://developer.nvidia.com/blog/run-massive-scale-umap-in-minutes-using-multiple-gpus-without-losing-accuracy/

Uniform Manifold Approximation and Projection (UMAP) is a dimensionality reduction technique widely used for visualization and feature extraction. Applications range across exploratory data analysis, topic modeling, and single-cell analysis. Many of these workflows are iterative and exploratory, requiring UMAP to be run repeatedly as users analyze their data or tune parameters. As datasets grow, the cost of each UMAP run increases substantially, making interactive exploration and iterative analysis increasingly difficult.

A critical step in the UMAP algorithm is the construction of an all-neighbors kNN graph over the dataset, which finds the k-nearest neighbors for every vector in the dataset. All-neighbors graph construction becomes increasingly expensive as datasets scale to tens or hundreds of millions of vectors.

The previous post, [Even Faster and More Scalable UMAP on the GPU with NVIDIA cuML](https://developer.nvidia.com/blog/even-faster-and-more-scalable-umap-on-the-gpu-with-rapids-cuml/), demonstrates how to scale UMAP using an out-of-core approach, making it possible to fit UMAP on datasets that were previously too large for a single GPU. However, the training stage remained limited to a single GPU and only the `transform()`

step was able to use multiple GPUs.

This post introduces a feature released in [NVIDIA cuML](https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cuml) and [NVIDIA cuVS 25.06](https://github.com/NVIDIA/cuvs/releases) that removes this limitation by distributing the expensive all-neighbors graph construction step across multiple GPUs. The feature significantly improves the scale and reduces the overall training runtime.

We also explain how to use cuML multi-GPU UMAP to accelerate workflows on datasets with tens to hundreds of millions of vectors. In practice, this approach delivers substantial end-to-end speedups on massive-scale datasets, as this post will show. This enables UMAP to run on workloads of several hundred gigabytes in minutes instead of hours or even days.

## How does NVIDIA cuML UMAP scale across multiple GPUs?

The [key idea for enabling the out-of-core approach for scaling UMAP](https://developer.nvidia.com/blog/even-faster-and-more-scalable-umap-on-the-gpu-with-rapids-cuml/) is constructing the all-neighbors kNN graph without requiring the entire dataset to fit in GPU memory at once, as introduced in the previous post. The approach accomplishes this by partitioning the dataset into balanced clusters and overlapping the vectors across nearby clusters to preserve nearest-neighbor relationships across the cluster boundaries.

Local kNN graphs are computed independently for each cluster, and these local graphs are merged into a single global all-neighbors graph. This makes it possible to run UMAP at scales that were previously too large to fit in GPU memory, while still preserving embedding quality.

This technique already decomposes the problem into independent units of work, so it extends naturally to a multi-GPU setting. Each cluster can be processed in isolation, meaning the computation of the local kNN graphs does not require access to the full dataset or coordination with other clusters. As a result, the clusters can be distributed across GPUs, where each GPU independently gathers the data for its assigned clusters from CPU memory.

Each GPU then computes local all-neighbors kNN graphs and merges each one with the global kNN graph. Computing these local kNN graphs independently avoids the need for expensive all-to-all communication that would typically limit scale in distributed all-neighbors kNN workloads. This method can produce major end-to-end performance gains on very large datasets.

## How to configure UMAP for multiple GPUs

This section provides copy-and-paste examples of the new feature. First, it’s important to understand two hyperparameters that provide the space, time, and quality tradeoff.

cuML multi-GPU UMAP follows the same steps as the single-GPU UMAP implementation, with the following two hyperparameters:

`knn_n_clusters`

: The number of clusters the data will be partitioned into`knn_overlap_factor`

: The total number of closest clusters each data point will be assigned to.

The `knn_n_clusters`

are approximately balanced, meaning the vectors are distributed approximately evenly across available GPUs for processing. Increasing this value reduces the number of points assigned to each cluster, lowering the amount of data that needs to fit in the memory of each GPU. For more details on the balanced k-means implementation, see our paper, [Massive-Scale Out-Of-Core UMAP on the GPU](https://openreview.net/forum?id=CR35IJQD2J).

As mentioned, `knn_overlap_factor`

increases the overlap of points across clusters, preserving more of the true nearest neighbors across cluster boundaries. Increasing this parameter generally improves the quality of the all-neighbors kNN graph, which improves the quality of the final UMAP embeddings. The improved quality comes with the tradeoff of increasing computation time and memory usage, as more vectors need to be processed per cluster.

`knn_overlap_factor`

and `knn_n_clusters`

together provide a controllable trade-off between space, time, and quality.

The distributed all-neighbors graph construction directly exposes these parameters as the [cuVS all-neighbors API.](https://docs.rapids.ai/api/cuvs/stable/cpp_api/neighbors_all_neighbors/) While cuML UMAP uses them internally, it is also available directly for applications that require standalone all-neighbors graph construction.

Python example of the cuVS all-neighbors API using multiple GPUs (Example 1):

`from` `cuvs.neighbors ` `import` `all_neighbors` `from` `cuvs.common ` `import` `MultiGpuResources` `params ` `=` `all_neighbors.AllNeighborsParams(` ` ` `algo` `=` `"nn_descent"` `,` ` ` `n_clusters` `=` `32` `,` ` ` `overlap_factor` `=` `2` `)` `# Using all GPUs on the system` `res ` `=` `MultiGpuResources()` `indices, distances ` `=` `all_neighbors.build(` ` ` `data,` ` ` `k,` ` ` `params,` ` ` `distances` `=` `cupy.empty((n_rows, k))` ` ` `resources` `=` `res` `)` |

The `n_clusters`

and `overlap_factor`

correspond to the `knn_n_clusters`

and `knn_overlap_factor`

arguments exposed by cuML UMAP, which forwards them to this cuVS all-neighbors API during graph construction.

### Practical configuration considerations

A good starting point for a quality embedding is `knn_overlap_factor=2`

. In practice:

- Smaller increments of
`knn_overlap_factor`

(2->3->4) work well for moderate scales. - Larger datasets that have a large
`knn_n_clusters`

(> 100) may benefit from larger increments of`knn_overlap_factor`

(2->4->6).

Increase `knn_overlap_factor`

carefully, because while higher values of `knn_overlap_factor`

will improve kNN recall, they will also significantly increase the computation time for each cluster.

To manage the memory trade-off while improving embedding quality, raise `knn_overlap_factor`

while also increasing `knn_n_clusters`

to keep the memory usage fairly constant.

For example, doubling the overlap factor will double the expected number of points per cluster, so doubling the number of clusters will maintain the points per cluster. It is suggested to use enough `knn_n_clusters`

such that each local graph and vectors in that cluster comfortably fit in GPU memory.

### GPU memory requirements

The memory required on each GPU depends on the dataset and the local kNN graph being constructed. For a dataset with

In practice, additional memory is also required for overhead like temporary workspace allocations during graph construction. Because of this, the actual peak memory usage can be higher than estimated here. We therefore recommend choosing `knn_overlap_factor`

and `knn_n_clusters`

comfortably below the available GPU memory.

For example, when using GPUs with 80 GB memory and a dataset with `float32`

(sizeof(data)=4) vectors (409 GB), you might choose `knn_overlap_factor=2`

and `knn_n_clusters=24`

. This makes the data size of each cluster `int64`

(sizeof(index) = 8) and distance type `float32`

(sizeof(distance)=4), and k=15,

Memory usage scales proportionally with `knn_overlap_factor`

because it decides the number of duplications per vector. In contrast, memory usage scales inversely with `knn_n_clusters`

.

## How to use multi-GPU UMAP in NVIDIA cuML

Using multi-GPU UMAP in NVIDIA cuML requires only a few additional configuration options beyond previous cuML UMAP usage.

In the following Python example of using multi-GPU UMAP (Example 2), the top example will construct the UMAP embedding with all available GPUs, while the bottom example will use only GPUs with IDs 0, 4, and 5:

`from` `cuml.manifold ` `import` `UMAP` `# Using all GPUs on the system` `umap ` `=` `UMAP(` `build_kwds` `=` `{` `"knn_n_clusters"` `: ` `32` `,` `"knn_overlap_factor"` `: ` `2` `,` `},` `device_ids` `=` `"all"` `,` `)` `embedding ` `=` `umap.fit_transform(data)` `# Using a subset of GPUs` `umap ` `=` `UMAP(` `build_kwds` `=` `{` `"knn_n_clusters"` `: ` `32` `,` `"knn_overlap_factor"` `: ` `2` `,` `},` `device_ids` `=` `[` `0` `, ` `4` `, ` `5` `],` `)` `embedding ` `=` `umap.fit_transform(data)` |

Here, the `device_ids`

argument controls which GPUs participate in the workload, while `knn_n_clusters`

and `knn_overlap_factor`

control how the all-neighbors kNN graph is constructed.

In general, increasing the number of GPUs reduces runtime by distributing the all-neighbors construction across devices. The next sections show the visualization results for a massive-scale dataset, and benchmarks that demonstrate the strong scaling effects as GPUs are added.

Finally, Example 3 below shows running cuML UMAP on the precomputed all-neighbors graph generated by cuVS in Example 1:

`from` `cuml.manifold.umap ` `import` `UMAP as cuUMAP` `# Using indices, distances from Example 1 computed by cuVS all-neighbors` `gpu_umap ` `=` `cuUMAP(` ` ` `precomputed_knn` `=` `(indices, distances),` `)` `gpu_embedding ` `=` `gpu_umap.fit_transform(data)` |

While Example 1 shows that the all-neighbors graph can be computed outside of UMAP, Example 3 demonstrates how easy it is to provide a precomputed all-neighbors graph to UMAP through the `precomputed_knn argument`

. The [CPU UMAP](https://github.com/lmcinnes/umap) also accepts this argument.

## Visualizing massive-scale embeddings

Figure 1 compares embeddings generated on the 106M x 2048 [MIRACL dataset](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00595/117438) using the [CPU reference implementation](https://github.com/lmcinnes/umap) with a precomputed GPU all-neighbors graph and cuML native GPU UMAP implementation. We precomputed the all-neighbors graph because it is computationally infeasible to compute on the CPU at this scale.

Note that UMAP is invariant to scale, translations, and rotations. This means these embeddings are functionally identical, even though the images look slightly different.

The resulting embeddings show comparable global structure, demonstrating that the GPU all-neighbors graph preserves the neighborhood relationships needed to produce high-quality visualizations even at a massive scale.

## What is the performance of multi-GPU UMAP on datasets that exceed single-GPU memory?

We evaluated the performance impact of using multi-GPU UMAP on datasets that exceed single-GPU memory ([Wiki](https://docs.rapids.ai/api/cuvs/stable/cuvs_bench/wiki_all_dataset/) and [MIRACL](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00595/117438)). All benchmarks were executed on an [NVIDIA DGX](https://www.nvidia.com/en-us/data-center/dgx-platform/) system with eight [NVIDIA H100](https://www.nvidia.com/en-us/data-center/h100/) GPUs and an Intel Xeon 8480CL 224-core CPU with 2TiB of RAM.

The [trustworthiness score](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.trustworthiness.html) is a popular measure of embedding quality, returning a number between 0 and 1 (higher is better). It measures the degree to which the local neighborhood structure is preserved in the low-dimensional UMAP embedded space as compared to the original high-dimensional space.

### End-to-end speedup at massive scale

Figure 2a (top) shows the runtime scaling behavior of the widely used CPU reference implementation on progressively larger subsamples of the Wiki and MIRACL datasets. As the dataset size increases, the runtime grows rapidly due to the memory and computation cost. At full scale, the CPU implementation failed to complete because of excessive memory consumption, even on a system with 2 TiB of RAM.

To estimate runtime at these scales, we projected the full-scale CPU runtime by extrapolating the measured scaling trend from smaller subsamples. For full details of this methodology, see our paper, [Massive-Scale Out-Of-Core UMAP on the GPU](https://openreview.net/forum?id=CR35IJQD2J).

Figure 2b (bottom) compares the projected CPU runtime against the actual runtime of cuML multi-GPU UMAP running on eight NVIDIA H100 GPUs. On the 106M vector MIRACL dataset, cuML achieves up to 74x end-to-end speedup over the projected CPU runtime.

Most importantly, this makes UMAP practical at previously intractable scales, completing end-to-end processing of the 106M vector dataset in just 8 minutes.

### Multi-GPU scaling

Figure 3 shows the scaling behavior of cuML multi-GPU UMAP on the Wiki and MIRACL datasets as the number of GPUs increases from one to eight H100 GPUs. The performance improvement is achieved while preserving comparable embedding quality across GPU configurations.

For additional details about the multi-GPU all-neighbors UMAP implementation, including more rigorous evaluation, see our paper, [Massive-Scale Out-Of-Core UMAP on the GPU](https://openreview.net/forum?id=CR35IJQD2J).

## Get started with UMAP using multiple GPUs

[NVIDIA cuVS](https://github.com/NVIDIA/cuvs) now provides multi-GPU all-neighbors graph construction, unlocking UMAP training in [NVIDIA cuML](https://github.com/rapidsai/cuml) at unprecedented scale and performance. These capabilities make large-scale visualization and embedding workflows such as [topic modeling](https://medium.com/rapids-ai/faster-topic-modeling-with-bertopic-and-rapids-cuml-5c7559aba898) and [single-cell analysis](https://build.nvidia.com/nvidia/single-cell-analysis) more practical, enabling even faster iteration and exploration.

To get started with multi-GPU UMAP in cuML and cuVS, see the [RAPIDS Installation Guide](https://docs.rapids.ai/install/). For more information about the all-neighbors APIs in NVIDIA cuVS, see the [cuVS API Guide](https://docs.nvidia.com/cuvs/user-guide/api-guides/indexing-guide/all-neighbors).

### Acknowledgments

*We’d like to thank Manas Singh and Mike Grauer for their valuable contributions to drafting and reviewing this post. We’re also deeply grateful to Leland McInnes for creating and sharing the UMAP algorithm with the world, and for his continued support in our advancements of its GPU acceleration.*

## Start the discussion at forums.developer.nvidia.com
