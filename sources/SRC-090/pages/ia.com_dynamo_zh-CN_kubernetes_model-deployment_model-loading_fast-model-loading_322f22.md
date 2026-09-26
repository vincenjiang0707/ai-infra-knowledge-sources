source: https://docs.nvidia.com/dynamo/zh-CN/kubernetes/model-deployment/model-loading/fast-model-loading
lastmod: 2026-09-24T19:58:16.636Z

# Fast Model Weight Loading

Cut cold-start weight-load time on shared PVC storage with a concurrent loader and correct filesystem layout

Loading a large checkpoint from a shared PVC into GPU memory can dominate cold start. A 1T-parameter model is hundreds of GiB on disk; with the wrong loader and the wrong filesystem layout it can take over an hour, even on storage that advertises multiple GB/s. This page explains the two independent bottlenecks and how to fix both, with a measured end-to-end example.

This is complementary to [Model Caching](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching): caching gets the weights onto a shared PVC once; this page makes each worker *read* them fast. It applies to the **PVC + Download Job** path, not the ModelExpress object-storage path (which streams from S3/GCS/Azure Blob instead — see [ModelExpress](https://docs.nvidia.com/dynamo/kubernetes/operations/cold-start-optimizations/model-express)).

## TL;DR

Two stacked bottlenecks slow a cold weight load off a shared filesystem:

**The loader’s access pattern (usually dominant).**The default safetensors loader reads single-stream with small effective I/O. On a parallel filesystem this leaves most of the bandwidth idle.**The filesystem layout.**On a striped/parallel filesystem (Lustre, and similar), a file that lives on a single storage target is capped at that one target’s bandwidth no matter how much aggregate the filesystem has.

Fix both:

**Loader:**add`--load-format runai_streamer`

to the vLLM worker (concurrent, multi-threaded, large-block reader; already shipped in Dynamo vLLM runtime images).**Layout (Lustre):**stripe the model files across all storage targets — set the directory default*before*download so files are born wide, or restripe existing files in place with`lfs migrate`

.

In a measured 554 GiB / TP16 deployment these two changes together cut weight load from **~76 min to ~5 min (~14×)** with no re-download. See [Case study](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/fast-model-loading#case-study-kimi-k27-code-554-gib-on-amlfs) below.

## Background: why a cold load is slow

### Bottleneck 1 — loader access pattern

vLLM’s default loader (`--load-format auto`

) memory-maps each safetensors shard and copies tensors out largely single-stream. The effective read is latency-bound against remote storage — small requests at shallow queue depth — so it never fills the pipe. Concurrency and block size both matter: on one Azure Managed Lustre (AMLFS) filesystem, a cache-bypassed `dd`

of a single shard measured:

The default loader sits near the top of that table (small reads), which is why a real load measured only **~124 MB/s effective** — over an order of magnitude below what the same storage delivers to a large-block reader.

** runai-model-streamer** (the

`runai_streamer`

load format) replaces this with a pool of worker threads issuing large, concurrent reads, saturating the storage instead of waiting on it. The package ships in Dynamo’s vLLM runtime images.### Bottleneck 2 — filesystem striping (Lustre)

A parallel filesystem spreads data across multiple **OSTs** (Object Storage Targets — the backing storage volumes). The filesystem’s advertised throughput is the *sum* across all OSTs; you only reach it when many OSTs work in parallel. A file’s layout has two knobs:

**stripe_count**— how many OSTs the file’s bytes are spread across.**stripe_size**— the chunk written to one OST before moving to the next.

The default `stripe_count`

is often **1** — each file lives entirely on one OST. A single-file read is then capped at one OST’s bandwidth, regardless of the filesystem’s aggregate. Striping a file across *all* OSTs lets even one sequential reader pull from all of them at once.

On the same AMLFS (4 OSTs, ~2 GB/s each, 8 GB/s aggregate), large-block read of one shard:

Striping only helps once the reader issues large, concurrent I/O. Wide striping with the default single-stream loader barely moves the needle, and a fast loader on stripe-1 files is still capped at one OST. **You need both fixes** — they multiply.

## How many stripes? (OSTs and capacity)

The maximum useful `stripe_count`

is the **number of OSTs** in the filesystem — you cannot stripe a file across more OSTs than exist. Use `stripe_count=-1`

to mean “all available OSTs.”

The OST count scales with **provisioned capacity**, not the SKU alone. AMLFS provisions roughly **1 OST per 4 TiB** (this matches the 500-SKU’s 4 TB capacity increment). So aggregate bandwidth and max stripe width grow only as you buy more TiB:

Check the live OST count on any Lustre mount with `lfs df`

(see [Inspecting and setting stripe layout](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/fast-model-loading#inspecting-and-setting-stripe-layout)).

## Backend support

`runai_streamer`

is a **vLLM** load format. Striping is filesystem-level and helps every backend, because they all read the same safetensors off the same mount.

For SGLang and TensorRT-LLM, the striping fix alone still helps; there is no `runai_streamer`

equivalent to add. (SGLang’s fast-distribution path is ModelExpress `remote_instance`

— a P2P pull from an already-loaded worker, not a faster first read from storage. See [Model Caching](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching#option-2-modelexpress-p2p-distribution).)

## Runbook: a new model on Lustre storage

This is the end-to-end procedure for bringing up a new large model on a Lustre-backed PVC with both optimizations from the start.

### Stripe the cache directory before downloading

Lustre sets a file’s layout at **creation time**, so the cheapest approach is to widen the target directory first — every file the download writes then inherits wide striping, and you never have to rewrite anything.

From any pod that has the `lfs`

client and mounts the PVC:

`lfs setstripe`

on a directory sets the **default layout for new files**; it does not move existing data. Run it before the download Job. If the `hub/`

subdirectory does not exist yet, create it (or set the layout on the PVC root) so the default is inherited.

If your downloader image lacks the `lfs`

client (for example `python:3.12-slim`

), either add `lustre-client-utils`

to it, or run the `lfs setstripe`

from a separate short-lived pod that has the client before you start the download Job.

### Download the model

Run the normal [PVC + Download Job](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching#step-2-download-the-model). Because the directory default is now wide, every shard lands striped across all OSTs.

### Enable the streaming loader in the DGD

Add the load format and (optionally) a concurrency hint to the vLLM worker:

Unlike `--load-format modelexpress`

, `runai_streamer`

still expects the weights present on the mounted path — Dynamo prefetches/uses the local cache as usual. It changes *how the files are read*, not *where they come from*. No ModelExpress server or `VLLM_PLUGINS`

setting is required.

## Fixing an already-downloaded model (no re-download)

If the weights are already on the PVC with the default `stripe_count=1`

, you do **not** need to re-download. `lfs migrate`

rewrites each file’s data across OSTs in place, preserving the HuggingFace cache symlinks (the `blobs/`

files are the real data; `snapshots/`

are symlinks into them).

### Verify integrity for free

HuggingFace LFS blob **filenames are the file’s SHA-256**. After migrating you can confirm the data is bit-identical at zero extra bookkeeping cost:

`lfs migrate`

is non-destructive (it writes a new layout and swaps only on success), and the mount typically carries a client-side `checksum`

option, so corruption is already unlikely — the SHA-256 sweep is a cheap final gate before you reload the model on top of the restriped data.

## Inspecting and setting stripe layout

You need the `lfs`

client (from `lustre-client-utils`

) on a pod that mounts the PVC. The Azure Lustre CSI node image (`csi-azurelustre-node`

) already contains `lfs`

.

## Case study: Kimi-K2.7-Code, 554 GiB on AMLFS

A real bring-up: `moonshotai/Kimi-K2.7-Code`

(1T-param / 32B-active MoE, native INT4), served aggregated at TP16 across two 8×H100 nodes, weights on an AMLFS-Durable-Premium-500 filesystem (16 TiB, 4 OSTs, 8 GB/s aggregate).

**Before.** Default loader, files at `stripe_count=1`

: weight load took **4575 s (~76 min)** — an effective ~124 MB/s, ~1/60th of the filesystem’s aggregate. Root cause split cleanly into the two bottlenecks above (loader access pattern dominant; single-OST striping secondary).

**Change.** `lfs migrate -c -1 -S 4M`

across all 87 blobs (555 GiB rewritten in place in ~10 min, SHA-256 verified bit-identical, no re-download), plus `--load-format runai_streamer`

with `RUNAI_STREAMER_CONCURRENCY=16`

in the DGD.

**After.** On reload, weight load took **318 s (~5.3 min)** — a **~14.4× speedup** — for the identical 36.96 GiB/GPU (layout-only change; weights unchanged). The model served correctly afterward.

The larger share of the win came from the loader flag (the access pattern was the dominant bottleneck); striping stacked on top by letting those concurrent streams hit all four OSTs at once.

## See also

[Model Caching](https://docs.nvidia.com/dynamo/kubernetes/model-deployment/model-loading/model-caching)— get the weights onto a shared PVC once (download Job, mount config, ModelExpress)[Azure Lustre CSI Driver](https://docs.nvidia.com/dynamo/kubernetes/installation/model-storage/azure-lustre-csi-driver)— provision AMLFS and the striping recommendation for it[Storage for Model Caching on AKS](https://docs.nvidia.com/dynamo/kubernetes/installation/model-storage/aks-storage)— choosing a storage class per cache type[Snapshotting GPU Workers](https://docs.nvidia.com/dynamo/kubernetes/operations/cold-start-optimizations/dynamo-snapshot)— checkpoint/restore and warm-start options for repeated restarts