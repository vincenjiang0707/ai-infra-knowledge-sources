source: https://docs.nvidia.com/nsight-compute/Training/index.html

# Training[#](https://docs.nvidia.com#training)

Nsight Compute training content.

NVIDIA Nsight Compute Training resources.

## External Resources[#](https://docs.nvidia.com#external-resources)

**Forum**

**Blogs**

Check the current list of

[blog posts](https://developer.nvidia.com/nsight-compute-blogs)

**Videos**

Check the current list of

[training videos](https://developer.nvidia.com/nsight-compute-videos)

**Code Examples**

Have a look at our coding examples on

[GitHub](https://github.com/NVIDIA/nsight-training)

## Usage Examples[#](https://docs.nvidia.com#usage-examples)

[Filter Options](https://docs.nvidia.com#filter-options)[#](https://docs.nvidia.com#filter-options)

Note that examples will use the term *workload* to refer to either kernels, graphs, ranges, or cmdlists unless stated otherwise.

**Profile first two workloads**`--launch-count 2`

**Profile the first two workloads launched on the device with device ID 1**`--device 1 --launch-count 2`

**Profile the 2nd workload on each GPU**`--launch-skip 1 --launch-count 1 --filter-mode per-gpu`

**Skip the first 2 workloads of each launch configuration before profiling**`--launch-skip 2 --filter-mode per-launch-config`

**Profile “Bar” kernel**`--kernel-name Bar`

**Profile kernels that have “Bar” in their function name**`--kernel-name regex:Bar`

**Profile only the 2nd invocation of kernel “Foo”**`--kernel-id ::Foo:2`

**Profile only the 3rd invocation of kernel “Foo” launched across all CUDA devices**`--kernel-id ::Foo:3`

**Profile only the 2nd invocation of kernel “Foo” launched on the CUDA device with device ID 1**`--kernel-id ::Foo:2 --device 1`

**Profile only the 2nd invocation of kernel “Foo” launched on each CUDA device**`--kernel-id ::Foo:2 --filter-mode per-gpu`

**Profile only the 2nd invocation of kernel “Foo” launched with each unique launch configuration, i.e., grid size, block size, and shared memory bytes**`--kernel-id ::Foo:2 --filter-mode per-launch-config`

**Profile only the 2nd invocation of all kernels that have “Bar” in their name**`--kernel-id ::regex:Bar:2`

**Skip the first 2 workloads before matching “Foo” or “Bar” in kernel names**`--launch-skip-before-match 2 --kernel-name regex:“Foo|Bar”`

**Profile every 7th kernel invocation with mangled name “_FooBar” on CUDA context ID 1 and stream ID 2**`--kernel-id 1:2:_Foobar:7 --kernel-name-base mangled`

**Profile only the 7th invocation of kernel “Foo”, regardless of context ID and stream ID**`--kernel-id ::Foo:7`

**Profile every 7th invocation of kernel “Foo” launched on stream ID 1 with NVTX stream name “cuda_stream”, regardless of context ID**`--kernel-id :1|cuda_stream:Foo:7 --nvtx`

**Profile all workloads launched in the first 3 ranges created by cu(da)ProfilerStart/Stop APIs**`--range-filter :[1-3]:`

**Profile all workloads launched in the 2nd NVTX Push/Pop range A**`--range-filters ::2 --nvtx --nvtx-include A/`

**Profile all workloads launched in NVTX Push/Pop range A except the ones in NVTX Push/Pop range B**`--nvtx --nvtx-include A/ --nvtx-exclude B/`

**Profile all “Foo” kernels except those launched in NVTX Push/Pop range B**`--nvtx --nvtx-exclude B/ --kernel-name Foo`

**Profile all workloads launched in the 2nd NVTX Start/End range A inside the 2nd range created by cu(da)ProfilerStart/Stop APIs**`--range-filter yes:2:2 --nvtx --nvtx-include A`

**Profile all workloads launched in the 1st NVTX Push/Pop range A inside both the 1st and 2nd ranges created by cu(da)ProfilerStart/Stop APIs**`--range-filter yes:[1-2]:1 --nvtx --nvtx-include A/`

**Profile all workloads launched in the 1st range created by cu(da)ProfilerStart/Stop APIs with the 2nd NVTX Push/Pop range A and domain D**`--range-filter no:1:2 --nvtx --nvtx-include D@A/`


Notices

Notices

ALL NVIDIA DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESSED, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES OF NONINFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE.

Information furnished is believed to be accurate and reliable. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication of otherwise under any patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all other information previously supplied. NVIDIA Corporation products are not authorized as critical components in life support devices or systems without express written approval of NVIDIA Corporation.

Trademarks

NVIDIA and the NVIDIA logo are trademarks or registered trademarks of NVIDIA Corporation in the U.S. and other countries. Other company and product names may be trademarks of the respective companies with which they are associated.