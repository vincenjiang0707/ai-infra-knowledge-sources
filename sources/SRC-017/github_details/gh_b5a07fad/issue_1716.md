# [Issue #1716] [feature request] Please add MIG support

source: https://github.com/NVIDIA/nccl/issues/1716
state: open | updated: 2026-09-10T17:05:34Z
labels: 

## 正文

Please add MIG support in NCCL.

The need: We, developers, need to able to do multi-gpu CI and with MIG available and NCCL not supporting it makes things much more complicated and expensive - especially for open source projects. It'd much cheaper to rent 1x A100 or H100 split it 4 way and do a 4-way gpu testing on CI, than paying for 4 gpus. 

At the last GTC I spent a long time waiting in line to talk to NVIDIA MIG experts and the experts were just sales people who couldn't answer my question.

Thank you!

## 评论 (30)

### sjeaugey · 2025-05-23

Ok, I'll try to summarize the challenges.

1. With MIG, each GPU slice does not come with a different CUDA index. NCCL algorithms heavily rely on having the full vision of the node to optimize the paths and therefore rely on using CUDA indexes.
2. Our topology detection code associates one PCI device with one GPU and one rank in the NCCL communicator. Having multiple ranks per physical GPU requires us to support having multiple ranks per GPU. This requires major changes in the topology code (which is already quite complex).
3. Communication between MIG instances cannot use CUDA P2P, so all communication needs to go through shared memory. That's going to be slow. Hopefully not slow enough that you can't run your CI, but managing timeouts/performance expectations may be an additional concern.

We are actively working on 2 to remove the restriction of one rank per physical GPU. I think this is the biggest road block right now.

### stas00 · 2025-05-23

Thank you for the detailed sharing of obstacles, Sylvain. 

Needless to say that high performance isn't required for CI use-case. Just being able to use MIG+NCCL would be amazing. Typically CI uses tiny models so using non-P2P comms would be perfectly fine.

### kkndyu · 2025-05-31

Jason: Buy more, save more, and poor guys are NOT our customers :-)

### seemethere · 2025-09-09

Is there any update on this? Would love to have this be enabled for us

### mnicely · 2025-09-09

MIG support is on our roadmap. We're targeting for Q4'25. I'll reach back out if things get delayed

### Bazinga-0411 · 2025-10-31

https://github.com/vickiegpt/nccl-mig

### HaowenGuan · 2026-02-13

> MIG support is on our roadmap. We're targeting for Q4'25. I'll reach back out if things get delayed

Appreciate the update earlier — Is there any update to MIG support?

### gab9talavera · 2026-02-13

@HaowenGuan what are your specific use cases for MIG? Would MPS or Multi-Rank GPU support satisfy with your use case?


### HaowenGuan · 2026-02-14

> @HaowenGuan what are your specific use cases for MIG? Would MPS or Multi-Rank GPU support satisfy with your use case?
> 

I am trying to deploy sglang to serve LLM using multiple gpus, which uses NCCL to communication between gpus.
I need this support because my institute partition H200 into MIG.

### marcofaltelli · 2026-03-12

> [@HaowenGuan](https://github.com/HaowenGuan) what are your specific use cases for MIG? Would MPS or Multi-Rank GPU support satisfy with your use case?

Hi @gab9talavera , I may be late to the party, but I'm also interested in this.
Sometimes we are interested in testing software that uses NCCL in small instances (which is a great use case for MIG) just to build some initial confidence with it.
Broadly speaking, this currently limits the deployment of MIGs in circumstances where they could be useful (cloud-based clusters like OpenStack/Kubernetes ones).
We recently tried to do HPL on a MIG instance to quantify the performance of MIG profiles, but it failed since it also relies on NCCL.

### gab9talavera · 2026-05-29

Hi all, thanks for the continued interest here. We are still working toward official NCCL support for MIG. In the meantime, NCCL 2.30u1 branch includes experimental multi-rank GPU building blocks that may be useful to try for MIG/resource-sharing experiments. These are not officially supported for MIG, and performance/behavior may vary. Current experimentation is limited to up to 2 MIG instances. Also worth noting: NCCL over NVLink is not supported for MIG today because CUDA does not currently expose P2P/NVLink path for MIG devices. To help us prioritize, could folks share how many MIG instances they need to use and which GPU/system generation they are targeting?

### stas00 · 2026-05-29

Thank you for the update, Gabrielle

Are you planning to raise the max number of MIG instances from 7 to a higher number? There is a lot more memory and SMs to limit at 7, since the inception time when gpus were much smaller.

The ideal use case is 8 instances, since we often need to test 3D parallelism and if this could be done on a single GPU this would be so much easier. The CI work would be much cheaper, especially for open source projects, like Deepspeed, where a lot of tests require multiple gpus.

generations: H, B, R

### hawkinsp · 2026-05-29

H100 and B200 support would be most helpful for CI use cases, and I think we partition the maximum number of ways (7?). But 2-way support would already be very helpful.

### marcofaltelli · 2026-06-08

> Hi all, thanks for the continued interest here. We are still working toward official NCCL support for MIG. In the meantime, NCCL 2.30u1 branch includes experimental multi-rank GPU building blocks that may be useful to try for MIG/resource-sharing experiments. These are not officially supported for MIG, and performance/behavior may vary. Current experimentation is limited to up to 2 MIG instances. Also worth noting: NCCL over NVLink is not supported for MIG today because CUDA does not currently expose P2P/NVLink path for MIG devices. To help us prioritize, could folks share how many MIG instances they need to use and which GPU/system generation they are targeting?

Hopper and Blackwell support would be really helpful. 7 MIG instances per-GPU is fine but also raising it to 8 is ok

### blhtx · 2026-07-08

Hi all, I just wanted to add that we have been waiting for NCCL to support MiG also.  We have an education use case.  For our University, A100 and newer would be useful.  2-way support would be most needed, but 4-way would also be useful.  We have been in contact with the DGX station team requesting support for NCCL and MiG while evaluating the GB300 workstations.

### mnicely · 2026-07-08

[NCCL Roadmap: Aug - Oct 2026](https://github.com/NVIDIA/nccl/issues/2272)

### stas00 · 2026-07-08

Thank you for lining it up in your plans, @mnicely!

### mnicely · 2026-07-08

The next step is for us to explain exactly what will be available to on Day 0, so we can get feedback from the community on where our support falls short

### stas00 · 2026-07-08

Excellent, please ping me when you have a plan and I can help announce your RFC on twitter.

### xiaofanl-nvidia · 2026-08-23

Hi all, we have added experimental MIG support from NCCL, and had some limited QA coverage. More details here: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/communicators.html#using-mig-instances

@stas00 @blhtx @seemethere @marcofaltelli @hawkinsp can you give it a try? 

One thing we have found (and verified) during testing is that MIG doesn't support P2P from CUDA using either PCIE or NVLINK so multi-GPU + MIG use case is very limited (also no NVLS and no MNNVL as a result). But the current support should help with some CI or development use cases with SHM (between MIG partitions) and NIC (across multiple GPUs). 

We validated Hopper and Blackwell with popular host side collectives to ensure they are functional. We haven't tested device APIs yet. 

I'll wait for a while in case you find anything fundamentally broken, and then close it after a couple of weeks. You can always open new issues for the future. 


### stas00 · 2026-08-31

@xiaofanl-nvidia, that's amazing news - thank you very much!

I tried it out on H200 and it worked, yay!

The docs need fixing it seems:

1. The doc says MIG "does not require NCCL_MULTI_RANK_GPU_ENABLE" because each instance is a distinct CUDA device. That is false whenever two ranks sit on slices of the same physical GPU, which is the entire point of MIG for CI. NCCL identifies ranks by the parent device and refuses without the flag.
2. The doc says NCCL "will not use NVLink SHARP because NVLS is not supported with MIG". It does try: with the multi-rank flag set and NVLS left at its default, init aborts in ncclNvlsInit. You must pass NCCL_NVLS_ENABLE=0 yourself.
3. NCCL_MNNVL_ENABLE=0, which the doc presents as mandatory, made no difference here — the four-slice run passed without it. It may matter on NVL72 systems, but it is not required on an H200 node.




### stas00 · 2026-08-31

Do you think we need to ask pytorch/torchrun to be MIG-aware and handle LOCAL_RANK/CUDA_VISIBLE_DEVICES correctly under MIG?

Currently this requires a super awkward:

```bash
torchrun --nproc_per_node 4 --no-python bash -c '
export CUDA_VISIBLE_DEVICES=$(echo $MIG_UUIDS | cut -d, -f$((LOCAL_RANK+1)))
export LOCAL_RANK=0
exec python train.py'
```

### stas00 · 2026-08-31

@xiaofanl-nvidia, I did a bunch of benchmarks - you can see them here
https://github.com/stas00/ml-engineering/blob/master/training/emulate-multi-node.md#emulating-multiple-gpus-with-a-single-gpu
if you read it and find some better ways to go about using it please let me know.

also shared here https://x.com/StasBekman/status/2094287881938292850

### marksantesson · 2026-09-01

@stas00 , thanks for you report on you experience using MIG! Your linked github benchmark page indicates you were using v2.31.2... is that the version you were using when you noticed that NCCL_MULTI_RANK_GPU_ENABLE=1 and NCCL_NVLS_ENABLE=0 were required? That sounds more like the behavior I would expect in some versions of v2.30.

The documentation could be clearer: you do not need to disable MNNVL if you do not have that feature available.

### stas00 · 2026-09-01

I re-checked it was 2.31.2 through and through.

NCCL version 2.31.2+cuda13.3 in the log, LD_PRELOADed over PyTorch 2.9.1+cu130, whose bundled NCCL is 2.27.7. 

NCCL_MULTI_RANK_GPU_ENABLE was required on 2.31.2, and NCCL asked for it by name. Four MIG ranks with no flags failed at init with:

`init.cc:1141 (initTransportsRank) NCCL WARN Multiple Ranks are using the same GPU/Partition. Set NCCL_MULTI_RANK_GPU_ENABLE=1 to enable this configuration.`

For contrast, the same launch on the bundled 2.27.7 fails with the older Duplicate GPU detected : rank 0 and rank 1 both on CUDA device 59000, so the two versions are clearly distinguishable in the logs.

NCCL_NVLS_ENABLE=0 is where I'd hedge. With MULTI_RANK_GPU_ENABLE=1 alone, init still failed on 2.31.2:

`transport/nvls.cc:255 (ncclNvlsInit) NCCL WARN NCCL_NVLS_ENABLE has been set to "1" and communicator has multiple ranks using the same NVML device. This is not compatible with NCCL_NVLS_ENABLE=1.`

Adding NCCL_NVLS_ENABLE=0 made things work. 

I wonder if it's the same as MNNVL, perhaps if you test on a system w/o SHARP then this flag doesn't matter?



### marksantesson · 2026-09-02

@stas00 , thanks for that info, that is helpful! It looks like something is setting your `NCCL_NVLS_ENABLE` to 1. The default should be 2. A value of 1 is interpreted as requiring NVLS, so it gives you that error message since it cannot support NVLS with multiple ranks per nvml id. A value of 2 supports NVLS if it can (which, in this case, it cannot). A value of 0 disables NVLS. In your case, 2 should be the same as 0.

Could something else in your environment, or system setup, be setting NCCL_NVLS_ENABLE=1?

Since you are using the correct version for MIG, the necessity of using NCCL_MULTI_RANK_GPU_ENABLE implies that you have multiple ranks running on hosts with the same `hostHash` and `gpuUuid`. Would it be possible for you to send me a log file of NCCL initialization with `NCCL_DEBUG=INFO` and `NCCL_DEBUG_SUBSYS=INIT,ENV` Also, the output from `nvidia-smi` while it is running would be very helpful. I'm trying to verify the host names and devices that NCCL is using. If you happen to have the output from running one of the perf tests from nccl-tests, that would be ideal.

### stas00 · 2026-09-02

You're absolutely correct about NCCL_NVLS_ENABLE=1 being preset, I have missed it came from the env. So that was my mistake.

I had no idea about the value 2 - love it! Thank you for sharing that with me, Mark.

I'm swamped at the moment, but I will try to get those logs to you in the next few days, Mark. 

### sjeaugey · 2026-09-02

> I had no idea about the value 2 - love it! Thank you for sharing that with me, Mark.

The best, as always, is to not set environment variables which you don't absolutely need. This is a recipe for future trouble.

See the [NCCL user guide](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html) for which env vars are ok to set (mostly platform-specific configuration), and those which should not be set unless needed for experiments, or as a temporary workaround.

### stas00 · 2026-09-03

@marksantesson, this is via Claude agent that has been doing the actual benchmarking, after cleaning its over achiever copious comments:

NCCL 2.31.2+cuda13.3 (driver 580.159.03, H200) — same version as the benchmark page. I re-ran the ablation to answer this properly:

- `NCCL_NVLS_ENABLE=0`: you're right, it is *not* required. Our pod spec exports `NCCL_NVLS_ENABLE=1`, and with that in the environment 2.31.2 aborts with `NCCL_NVLS_ENABLE has been set to "1" and communicator has multiple ranks using the same NVML device`. Left at the default (2), four ranks over four `1g.35gb` instances come up fine. 

- `NCCL_MULTI_RANK_GPU_ENABLE=1`: still required on 2.31.2. Without it: `Multiple Ranks are using the same GPU/Partition. Set NCCL_MULTI_RANK_GPU_ENABLE=1 to enable this.` The init log shows why — every rank logs `cudaDev 0 nvmlDev 0 busId 59000`, so NCCL is identifying the parent GPU rather than the MIG compute instance, even though each rank has a distinct `MIG-…` UUID in `CUDA_VISIBLE_DEVICES`.

- MNNVL: agreed, nothing to disable here. Logs show `MNNVL busId 0x59000 fabric UUID 0.0 cliqueId 0x0 state 3 healthMask 0x0` and `MNNVL 0`; I did not set `NCCL_MNNVL_ENABLE` in any of these runs.
nccl-tests `all_reduce_perf -b 8 -e 128M -f 2 -g 1`, 4 ranks: 4× `1g.35gb` on one H200 gives 48.84 GB/s average busbw, 251.09 GB/s at 128 MiB; 4 whole H200s give 73.78 GB/s average, 327.61 GB/s at 128 MiB.

Two small things that cost me time and might be worth documenting: the `nvidia-nccl-cu13` wheel has no `libnccl.so` symlink, so building nccl-tests against it silently links the older system libnccl; and under MIG, nccl-tests needs `NCCL_TESTS_DEVICE=0` because it otherwise derives its device index from `localRank*nThreads*nGpus`.

On host names and devices — `nvidia-smi` taken 12s into the passing run (single node `stas-dev-5-0`, GPU 0 carved into 4x 1g.35gb):

```
|    0    3    0           865632      C   .../bin/python        274MiB |
|    0    4    0           865633      C   .../bin/python        278MiB |
|    0    5    0           865634      C   .../bin/python        278MiB |
|    0    6    0           865635      C   .../bin/python        278MiB |
```

Those PIDs are the same ones in the NCCL log prefixes for ranks 0-3, so each rank really is on its own GPU instance (GI 3, 4, 5, 6 — distinct MIG UUIDs passed one per rank via `CUDA_VISIBLE_DEVICES`, each with 26 SMs and 33280 MiB). NCCL's own view of all four is identical: `cudaDev 0 nvmlDev 0 busId 59000`, and `nRanks 4 nNodes 1 localRanks 4`. The driver distinguishes the instances; NCCL's device identity resolves to the parent GPU.

Also of note: NCCL initializes the network (`NET/OFI Selected provider is efa, fabric is efa-direct (found 16 nics)`, `Using network Libfabric`) but doesn't use it for this communicator — all 256 channel lines are `via P2P/CUMEM`.

I have the full `nvidia-smi` output for all three arms plus the nccl-tests run, and the corresponding `NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,ENV` logs; happy to attach any of them.


### marksantesson · 2026-09-10

@stas00 , I'm sorry for not updating you recently... I've got what I need from you for now and we are working on this internally. I'll update you when we have further progress. Thanks for your help!
