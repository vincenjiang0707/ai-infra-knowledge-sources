# [Issue #3433] [Distributed] hardware=gpu does not correctly configure process-per-node mode with Slurm

source: https://github.com/AI-Hypercomputer/maxtext/issues/3433
state: closed | updated: 2026-04-08T19:36:37Z
labels: bug

## 正文

### Bug report

The logic for distributed initialisation with `hardware=gpu`:
https://github.com/AI-Hypercomputer/maxtext/blob/37ded59999c631cb18ea63c55febb1856dcf4642/src/maxtext/utils/max_utils.py#L246-L266

Is targeted at running in process-per-node mode (i.e. 1 process driving all GPUs in the machine). However, if `CUDA_VISIBLE_DEVICES` is not set explicitly then this falls through to auto-detection, which assumes process-per-GPU mode on Slurm. The result is that only the 0th GPU on each node is used.

It would be more user-friendly if -- given that this MaxText code is quite explicitly targeted at process-per-node mode -- it did not require the user to explicitly set `CUDA_VISIBLE_DEVICES`.

There is also `hardware=gpu_multiprocess` that defers to JAX's default distributed initialisation and, on a Slurm cluster, correctly yields a process-per-GPU configuration.

### Logs/Output

```
srun --container-image=...--container-remap-root sh -c 'CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 NNODES=2 NODE_RANK=${SLURM_PROCID} JAX_COORDINATOR_PORT=2222 JAX_COORDINATOR_IP=... python3 -m maxtext.trainers.pre_train.train ... hardware=gpu ici_fsdp_parallelism=8 ...'
```
will work, while
```
srun --container-image=...--container-remap-root sh -c 'NNODES=2 NODE_RANK=${SLURM_PROCID} JAX_COORDINATOR_PORT=2222 JAX_COORDINATOR_IP=... python3 -m maxtext.trainers.pre_train.train ... hardware=gpu ici_fsdp_parallelism=8 ...'
```
will yield
```
AssertionError: Number of devices per slice 1 does not match the product of the ICI parallelism 8
```

### Environment Information

_No response_

### Additional Context

_No response_

## 评论 (7)

### shralex · 2026-03-30

@gabeweisz since you contributed this code, could you please take a look on the request ?

### gabeweisz · 2026-03-31

This change is desirable, but I don't think that this behavior is achievable without a change to Jax.

I do not think it is possible to automatically select all GPUs. The reason for this is that, as far as I know, we can't tell how many GPUs are present without calling jax.devices(). However, jax,distributed.initialize() must be called [before the GPU backend is initialized](https://docs.jax.dev/en/latest/_autosummary/jax.distributed.initialize.html), which means that we cannot call jax.devices() to determine how many GPUs are available.

It might be possible to check slurm environment variables like SLURM_JOB_GPUS to see what GPUs are available. Otherwise the behavior of jax.distributed.initialize() in Jax to achieve this. I'll investigate.

### gabeweisz · 2026-04-06

Slurm sets the environment variable "SLURM_STEP_GPUS" to list GPUs assigned to the job.  I will create a PR to check that if CUDA_VISIBLE_DEVICES is not available. You still will need to pass in SLURM_STEP_GPUs (from the local environment, set automatically by slurm) to your container, but that is because there's no way to detect what GPUs are available from Jax without running jax.devices() AFAIK. Without a container this will all work without setting any extra environment variables

### olupton · 2026-04-08

JAX's `jax_cuda_visible_devices` has some logic for a special `"all"` value -- can that be used here?

I am not sure that `SLURM_STEP_GPUS` is reliable.

### gabeweisz · 2026-04-08

SLURM_STEP_GPUS is [part of the slurm documentation](https://slurm.schedmd.com/srun.html) - so if you have evidence that it is not reliable you should take that up with them.

I've confirmed that setting jax_cuda_visible_devices to "all" does not work (at least under ROCm) - we only get one GPU in Slurm regardless of how many are allocated
I did this with:
jax._src.config.update("jax_cuda_visible_devices", "all")
jax._src.config.update("jax_rocm_visible_devices", "all")

I can add this code anyway, but don't have the ability to test it in CUDA. But I can file a bug in ROCm's jax plugin to support "all"

From what I can tell, the special handling for 'all' is to not set visible_devices if jax_cuda_visible_devices is 'all' ([as seen here](https://github.com/jax-ml/jax/blob/369cf5369e3328d84f428c110cf7b12e33ff2277/jax/_src/xla_bridge.py#L516))

This is best effort without changing Jax and XLA - using "CUDA_VISIBLE_DEVICES" is better than not using anything (which would only get you one GPU), and using "SLURM_STEP_GPUS" if "CUDA_VISIBLE_DEVICES" is not set will allow some amount of auto-configuration in Slurm. 

### gabeweisz · 2026-04-08

Requested change made. Now this code will:
- use CUDA_VISIBLE_DEVICES if set
- use SLURM_VISIBLE_DEVICES if CUDA_VISIBLE_DEVICES is not set and SLURM_VISIBLE_DEVICES is set
- set "jax_cuda_visible_devices" and "jax_rocm_visible_devices" to "all" in jax.config" if neither are set

### gabeweisz · 2026-04-08

None of this would be necessary if we could disable [this line of code](https://github.com/jax-ml/jax/blob/2317e50951f2ed5ac99bdac2e90660be236bb6f9/jax/_src/clusters/cluster.py#L88) in Jax for GPUs
