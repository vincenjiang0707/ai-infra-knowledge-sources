source: https://docs.nvidia.com/cuda/cutile-python/quickstart.html

# Quickstart[#](https://docs.nvidia.com#quickstart)

This page will guide you through getting setup and running with cuTile Python, including running a first example.

## Prerequisites[#](https://docs.nvidia.com#prerequisites)

cuTile Python requires the following:


Linux x86_64, Linux aarch64 or Windows x86_64

A GPU with compute capability 8.x, 9.x, 10.x, 11.x or 12.x

NVIDIA Driver r580 or later

Python version 3.10, 3.11, 3.12, 3.13, 3.14, or 3.14t


## Installing cuTile Python[#](https://docs.nvidia.com#installing-cutile-python)

cuTile Python depends on CUDA TileIR compiler `tileiras`

,
which futher depends on `ptxas`

and `libnvvm`

from the CUDA Toolkit. They can be installed
as python packages per virtual environment or at system wide CTK locations.

If your system does not have system-wide CUDA Toolkit (13.1+),
you can install cuTile Python along with the optional `[tileiras]`

,
which installs `nvidia-cuda-tileiras`

, `nvidia-cuda-nvcc`

and
`nvidia-nvvm`

into your Python virtual environment.

```
pip install --upgrade cuda-tile[tileiras]
```

Note: the package versions for `nvidia-cuda-tileiras`

, `nvidia-cuda-nvcc`

and
`nvidia-nvvm`

must match up to the same major.minor version.

cuTile python supports different versions of tileiras.
To use a specific version of `tileiras`

python pacakge, i.e. 13.3 run

```
pip install cuda-toolkit[tileiras,nvvm,nvcc]>=13.3
```

Alternatively if you already have system-wide CUDA Toolkit (13.1+) installed,
you can install cuTile Python as a standalone package.
cuTile automatically searches for `tileiras`

from the location of CUDA Toolkit.

```
pip install cuda-tile
```

## Other Packages[#](https://docs.nvidia.com#other-packages)

Some of the cuTile Python samples also use other Python packages.

The quickstart sample on this page uses cupy, which can be installed with:

```
pip install cupy-cuda13x
```

The cuTile Python samples in the `samples/`

directory also use pytest, torch, and numpy packages.

For PyTorch installation instructions, see [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/).

Pytest and Numpy can be installed with:

```
pip install pytest numpy
```

## Example Code[#](https://docs.nvidia.com#example-code)

The following example shows vector addition, a typical first kernel for CUDA, but uses cuTile for tile-based programming. This makes use of a 1-dimensional tile to add two 1-dimensional vectors.

This example shows a structure common to cuTile kernels:

Load one or more tiles from GPU memory

Perform computation(s) on the tile(s), resulting in new tile(s)

Write the resulting tile(s) out to GPU memory


In this case, the kernel loads tiles from two vectors, `a`

and `b`

. These loads create tiles called `a_tile`

and `b_tile`

. These tiles are added together to form a third tile, called `result`

. In the last step, the kernel stores the `result`

tile to the output vector `c`

.
More samples can be found in the cuTile Python [repository](https://github.com/nvidia/cutile-python).

```
# SPDX-FileCopyrightText: Copyright (c) <2025> NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# SPDX-License-Identifier: Apache-2.0
"""
Example demonstrating simple vector addition.
Shows how to perform elementwise operations on vectors.
"""
import cupy as cp
import numpy as np
import cuda.tile as ct
@ct.kernel
def vector_add(a, b, c, tile_size: ct.Constant[int]):
# Get the 1D pid
pid = ct.bid(0)
# Load input tiles
a_tile = ct.load(a, index=(pid,), shape=(tile_size,))
b_tile = ct.load(b, index=(pid,), shape=(tile_size,))
# Perform elementwise addition
result = a_tile + b_tile
# Store result
ct.store(c, index=(pid, ), tile=result)
def test():
# Create input data
vector_size = 2**12
tile_size = 2**4
grid = (ct.cdiv(vector_size, tile_size), 1, 1)
rng = cp.random.default_rng()
a = rng.random(vector_size)
b = rng.random(vector_size)
c = cp.zeros_like(a)
# Launch kernel
ct.launch(cp.cuda.get_current_stream(),
grid, # 1D grid of processors
vector_add,
(a, b, c, tile_size))
# Copy to host only to compare
a_np = cp.asnumpy(a)
b_np = cp.asnumpy(b)
c_np = cp.asnumpy(c)
# Verify results
expected = a_np + b_np
np.testing.assert_array_almost_equal(c_np, expected)
print("✓ vector_add_example passed!")
if __name__ == "__main__":
test()
```

Run this from a command line as shown below. If everything has been setup correctly, the test will print that the example passed.

```
$ python3 samples/quickstart/VectorAdd_quickstart.py
✓ vector_add_example passed!
```

To run more of the cuTile Python examples, you can directly run the samples by invoking them in the same way as the quickstart example:

```
$ python3 samples/FFT.py
# output not shown
```

You can also use pytest to run all the samples:

```
$ pytest samples
========================= test session starts =========================
platform linux -- Python 3.12.3, pytest-9.0.1, pluggy-1.6.0
rootdir: /home/ascudiero/sw/cutile-python
configfile: pytest.ini
collected 6 items
samples/test_samples.py ...... [100%]
========================= 6 passed in 30.74s ==========================
```

## Developer Tools[#](https://docs.nvidia.com#developer-tools)

[NVIDIA Nsight Compute](https://developer.nvidia.com/nsight-compute) can profile cuTile Python kernels in the same way as SIMT CUDA kernels. With NVIDIA Nsight Compute installed, the quickstart vector addition kernel introduced here can be profiled using the following command to create a profile:

```
ncu -o VecAddProfile --set detailed python3 VectorAdd_quickstart.py
```

This profile can then be loaded in a graphical instance of Nsight Compute and the kernel `vector_add`

selected to see statistics about the kernel.

Note

Capturing detailed statistics for cuTile Python kernels requires running on NVIDIA Driver equals or later than r580.126.09 (linux) or r582.16 (windows).