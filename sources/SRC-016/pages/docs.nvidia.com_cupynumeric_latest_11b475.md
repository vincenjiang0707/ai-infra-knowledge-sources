source: https://docs.nvidia.com/cupynumeric/latest/

# NVIDIA cuPyNumeric[#](https://docs.nvidia.com#nvidia-cupynumeric)

Important

cuPyNumeric has reached end of life and is no longer maintained or supported. The final release is v26.06.01. No further releases, fixes, or support are planned. Existing packages and documentation remain available for historical reference, but we do not recommend starting new projects with cuPyNumeric.

Consider one of the following alternatives for multi-GPU/multi-node array computing:

[nvmath-python](https://docs.nvidia.com/cuda/nvmath-python/latest/overview.html), in particular the[nvmath.distributed module](https://docs.nvidia.com/cuda/nvmath-python/latest/distributed-apis/distribution.html)[CuPy](https://cupy.dev)combined with[mpi4py](https://mpi4py.readthedocs.io/en/stable/)or[Dask Array](https://docs.dask.org/en/latest/how-to/selecting-the-collection-backend.html)&[Dask-CUDA](https://docs.nvidia.com/dask-cuda/latest/)[JAX](https://jax.dev), in particular the[multi-controller module](https://docs.jax.dev/en/latest/501/multiprocess.html)[PyTorch](https://pytorch.org), in particular the[torch.distributed module](https://docs.pytorch.org/docs/stable/distributed)

cuPyNumeric implements the NumPy API on top of the Legate framework, providing transparent accelerated computing that scales from a single CPU to a single GPU, and up to multi-node, multi-GPU systems.

For example, you can run [the final example of the Python CFD course](https://github.com/barbagroup/CFDPython/blob/master/lessons/15_Step_12.ipynb)
completely unmodified on 2048 A100 GPUs in a [DGX SuperPOD](https://www.nvidia.com/en-us/data-center/dgx-superpod/) and achieve
good weak scaling.