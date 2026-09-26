source: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/eplb_utils/
lastmod: 2026-09-24

#

`vllm.distributed.eplb.eplb_utils`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils)

Utility functions for EPLB (Expert Parallel Load Balancing).

Classes:

-
–[CpuGpuEvent](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.CpuGpuEvent)Combines a CUDA event with a CPU threading event to enforce record->wait


Functions:

-
–[device_stream](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.device_stream)Platform-agnostic context manager that activates

*stream*as the -
–[override_envs_for_eplb](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.override_envs_for_eplb)Override environment variables for EPLB when specific conditions are met.


##

`CpuGpuEvent`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.CpuGpuEvent)

Combines a CUDA event with a CPU threading event to enforce record->wait ordering across two threads.

This class is designed for exactly two threads: one producer that calls record() and one consumer that calls wait(). Using it with more than two threads is not supported and will produce undefined behavior.

CUDA events alone are insufficient for cross-thread synchronization because waiting on an unrecorded CUDA event is a no-op. The wait will return immediately instead of blocking. This class adds a threading.Event so that the waiting thread blocks on the CPU side until record() is called, at which point the CUDA event is guaranteed to be in-flight and event.wait() will correctly synchronize the GPU stream.

Methods:

-
–[record](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.CpuGpuEvent.record)Unblocks the waiting thread after calling event.record().

-
–[wait](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.CpuGpuEvent.wait)Blocks the calling thread until record finishes. Used to guarantee that the


## Source code in `vllm/distributed/eplb/eplb_utils.py`


###

`record(stream=None)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.CpuGpuEvent.record)

Unblocks the waiting thread after calling event.record().

Should only be called by the main thread.

## Source code in `vllm/distributed/eplb/eplb_utils.py`


###

`wait(stream=None)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.CpuGpuEvent.wait)

Blocks the calling thread until record finishes. Used to guarantee that the record kernel is called before wait.

Should only be called by the Async Eplb thread.

## Source code in `vllm/distributed/eplb/eplb_utils.py`


##

`device_stream(stream)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.device_stream)

Platform-agnostic context manager that activates *stream* as the current accelerator stream for the duration of the `with`

block. A no-op when *stream* is `None`

.

## Source code in `vllm/distributed/eplb/eplb_utils.py`


##

`override_envs_for_eplb(parallel_config, moe_backend=None)`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.override_envs_for_eplb)

Override environment variables for EPLB when specific conditions are met.

Parameters:

-

(`parallel_config`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.override_envs_for_eplb(parallel_config))

) –[ParallelConfig](https://docs.vllm.ai/config/#vllm.config.ParallelConfig)The parallel configuration object.

-

(`moe_backend`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.eplb_utils.override_envs_for_eplb(moe_backend))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)| None`None`

) –The configured MoE backend (e.g.

`deep_gemm_mega_moe`

).