source: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/
lastmod: 2026-09-24

#

`vllm.distributed.device_communicators`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators)

Modules:

-
–[aiter_custom_all_reduce](https://docs.vllm.ai/aiter_custom_all_reduce/#vllm.distributed.device_communicators.aiter_custom_all_reduce)vLLM-owned wrapper over AITER's

`CustomAllreduce`

. -
–[all2all](https://docs.vllm.ai/all2all/#vllm.distributed.device_communicators.all2all) -
–[all_reduce_utils](https://docs.vllm.ai/all_reduce_utils/#vllm.distributed.device_communicators.all_reduce_utils) -
–[base_device_communicator](https://docs.vllm.ai/base_device_communicator/#vllm.distributed.device_communicators.base_device_communicator) -
–[cpu_communicator](https://docs.vllm.ai/cpu_communicator/#vllm.distributed.device_communicators.cpu_communicator) -
–[cuda_communicator](https://docs.vllm.ai/cuda_communicator/#vllm.distributed.device_communicators.cuda_communicator) -
–[cuda_wrapper](https://docs.vllm.ai/cuda_wrapper/#vllm.distributed.device_communicators.cuda_wrapper)This file is a pure Python wrapper for the cudart library.

-
–[custom_all_reduce](https://docs.vllm.ai/custom_all_reduce/#vllm.distributed.device_communicators.custom_all_reduce) -
–[flashinfer_all_reduce](https://docs.vllm.ai/flashinfer_all_reduce/#vllm.distributed.device_communicators.flashinfer_all_reduce) -
–[flashinfer_pcie_ipc_all_reduce](https://docs.vllm.ai/flashinfer_pcie_ipc_all_reduce/#vllm.distributed.device_communicators.flashinfer_pcie_ipc_all_reduce)FlashInfer PCIe CUDA-IPC all-reduce integration.

-
–[pynccl](https://docs.vllm.ai/pynccl/#vllm.distributed.device_communicators.pynccl) -
–[pynccl_wrapper](https://docs.vllm.ai/pynccl_wrapper/#vllm.distributed.device_communicators.pynccl_wrapper) -
–[quick_all_reduce](https://docs.vllm.ai/quick_all_reduce/#vllm.distributed.device_communicators.quick_all_reduce) -
–[ray_communicator](https://docs.vllm.ai/ray_communicator/#vllm.distributed.device_communicators.ray_communicator) -
–[shm_broadcast](https://docs.vllm.ai/shm_broadcast/#vllm.distributed.device_communicators.shm_broadcast) -
–[shm_object_storage](https://docs.vllm.ai/shm_object_storage/#vllm.distributed.device_communicators.shm_object_storage) -
–[xpu_communicator](https://docs.vllm.ai/xpu_communicator/#vllm.distributed.device_communicators.xpu_communicator)