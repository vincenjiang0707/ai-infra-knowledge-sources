# gpu-native-operators-in-ray-data

source: https://www.anyscale.com/blog/gpu-native-operators-in-ray-data

Ray Data is a data engine built on Ray focused on AI workloads such as multimodal data processing and training data loading. Due to its focus on AI workloads, GPUs are a core feature of Ray Data - Ray Data is able to treat GPUs as a scheduling resource and thus is able to easily scale data processing tasks across GPUs.

Despite this, Ray Data has had limited native functionality that executes directly on the GPU, delegating that responsibility to user defined functions that call GPU-enabled libraries like PyTorch or JAX.

Recently, the Ray Data team at Anyscale has collaborated with the NVIDIA cuDF team to better integrate GPU-based operators into Ray Data. In particular, we’re excited to announce two new features:

On select data curation workloads, these enhancements have enabled up to 3x better TCO compared to CPU-based solutions.

You can try this out today on Ray by `pip install -U ray==2.58`

.

## LinkBackground

Ray Data offers a set of canonical data processing operations, from IO to shuffle to UDFs. One of Ray Data’s differentiating features is that it has first-class support for GPUs for its UDFs. For example, one can schedule custom code leveraging a GPU as follows:

```
import ray
ds = ray.data.read_parquet("s3://my-bucket/documents/")
def compute_gpu(batch: pd.DataFrame):
...
ds = ds.map_batches(compute_gpu, num_gpus=1, batch_size=4096, batch_format="pandas")
```


The above code will automatically launch multiple `compute_gpu`

calls, all running on different processes attached to different GPUs across your Ray cluster.

In using Ray Data for data deduplication tasks, we noticed two opportunities for improvement:

There were compute-intensive dataframe operations in the pipeline that could be accelerated by using cuDF, but this would require the user to convert data formats manually

The specific tasks had heavy hash-aggregation steps that were compute intensive and could benefit from improved GPU acceleration.


In order to address these opportunities, we added two key features to Ray Data: cuDF batch format support and a GPU-native shuffle backend based on RapidsMPF.

### LinkcuDF as a first-class batch format

Ray Data has 3 native batch formats - Pandas Dataframes, Numpy Arrays, and PyArrow Tables. Batch formats serve two purposes -- to be the data exchange format between stages, and to provide users with a more familiar interface to write custom processing functions.

As of Ray 2.58, `map_batches`

now accepts `batch_format="cudf"`

, which hands your UDF a `cudf.DataFrame`

instead of a pandas DataFrame or Arrow table.

**cuDF** is NVIDIA's open-source GPU-accelerated DataFrame library, one of the NVIDIA CUDA-XTM libraries for data processing. It provides a Pandas-like API with GPU-accelerated operations. For certain computationally-heavy operations, cuDF can be up to order of magnitude faster and cheaper than alternative CPU equivalent operations.

```
import ray
ds = ray.data.read_parquet("s3://my-bucket/documents/")
def add_minhash(batch): # batch is a cudf.DataFrame
batch["minhash"] = batch["text"].str.minhash(seed=42, ...)
return batch
ds = ds.map_batches(add_minhash, batch_format="cudf", num_gpus=1, batch_size=4096)
```


### LinkGPU-native shuffle via RapidsMPF

Users can now leverage GPU-accelerated `repartition`

and hash aggregations through a new GPU execution path built on [ RapidsMPF](https://docs.rapids.ai/api/rapidsmpf/stable/). Ranks talk to each other directly over UCXX. Between ranks, shuffled data take advantage of high performance transports like RDMA or NVLink, skipping the CPU and Ray object store.

Similar to cuDF, for certain computationally-heavy operations, RapidsMPF-based shuffle can be up to order of magnitude faster and cheaper than alternative CPU equivalent operations.

```
from ray.data.context import DataContext, ShuffleStrategy
ctx = DataContext.get_current()
ctx.shuffle_strategy = ShuffleStrategy.GPU_SHUFFLE
ds.repartition(num_blocks=256, keys=["doc_id"])
ds.groupby("band_id").count()
```


## LinkBenchmarks: fuzzy deduplication

The motivating workload for our collaboration has been **fuzzy document deduplication**, a standard workload for data curation for foundation model training. For our benchmarking, we used [the standard MinHash-LSH approach](https://huggingface.co/blog/dedup) , outlined below:

**Generate MinHash signatures**for every document.**Generate LSH bands**from those signatures.**Group by band**to find candidate duplicate pairs.**Deduplicate the candidate edges.****Compute connected components**by traversing the graph.**Filter duplicates****Persist the survivors.**

Step 1 involves generating hash values for each n-gram, and hashing is a compute-intensive operation.

Step 3 and Step 5 are the most shuffle-intensive -- a groupby operation is used to form duplicate pairs, and the connected components algorithm is a series of groupby operations.

In the below experiments, we were able to see improved performance for these steps due to GPU integration and acceleration.

In the below experiments, we used the FineWeb 10BT dataset on cluster sizes between 2 to 8 nodes. For CPU, we used the m8id.4xlarge instance type, which has 16 vCPUs, 64 GiB memory, and costs 1.04416 dollars per hour.

For GPU evaluation, we used the g6.4xlarge instance type, which has 16 vCPUs, 64 GiB memory, and costs 1.3232 dollars per hour.

Experiment code can be [ found here](https://github.com/ray-project/gpu-deduplication) using Ray 2.58

### LinkGenerating MinHash signatures

In this phase, we break each document into a set of n-grams (where n is set to 5), and we generate 128 hashes per each n-gram.

The hashing step is compute-intensive, and we compare a baseline Numpy-based solution with the cuDF built-in hashing implementation.

|
|
|
|
|---|---|---|---|
CPU baseline (s) | 1899 | 963 | 519 |
GPU (with cuDF) (s) | 125 | 63 | 33 |
|
|
|
|

From the above results, we see that GPU acceleration improves this stage of the workload up to **15x faster **than a similarly sized CPU cluster.

### LinkThe grouping stages

In steps 3 and 5, we perform locality-sensitive hashing, which creates groups documents if they have hash collisions; and we implement an [ iterative connected components detection algorithm](https://research.google/pubs/connected-components-in-mapreduce-and-beyond/) in order to find documents that have transitive collisions (for example, if document A is found to be similar to document B, and document C is found to be similar to document B, then document A should be similar to document C).

|
|
|
|
|---|---|---|---|
CPU baseline (s) | 1634 | 850 | 434 |
GPU (with RapidsMPF) (s) | 542 | 356 | 281 |
|
|
|
|

In this comparison, while increasing the number of GPUs improves runtime, the marginal improvement diminishes at higher scale, thereby decreasing cost savings.

Since these stages are shuffle intensive, adding more GPUs adds more communication overhead. For this particular dataset and workload, 2 GPUs was optimal, so the dataset was likely too small to take advantage of all 8 GPUs.

### LinkEnd-to-end Pipeline

|
|
|
|
|---|---|---|---|
CPU baseline (s) | 3718 | 1891 | 989 |
GPU acceleration (s) | 939 | 511 | 360 |
|
|
|
|
CPU baseline ($) |
|
|
|
GPU acceleration ($) |
|
|
|
|
|
|
|

From the full pipeline on a fixed hardware configuration, we see that the GPU-accelerated solution is:

4x faster and 3.1x better TCO than the lowest cost CPU comparison point (at 2 nodes)

Provides TCO and runtime improvements across the board on all node scales


## LinkWhat's next

While the results above are promising, we are still far from the upper limits of performance. In particular, operator fusion between sequential operators that use cuDF and RapidsMPF will provide a significant step change in performance. This will allow Ray Data to avoid unnecessary host-to-device round trips between stages, allowing the data to stay within GPU memory.

In working with end users, another step is to enable** GPU shuffle for data preprocessors** so that feature-engineering pipelines built on Ray Data's preprocessor API pick up the GPU path.

We’re excited to continue investing in this area to bring the best data processing performance for your AI data workloads. Ray Data GPU shuffle is experimental today and available as part of Ray 2.58. If you try it, we'd like to hear your feedback!
