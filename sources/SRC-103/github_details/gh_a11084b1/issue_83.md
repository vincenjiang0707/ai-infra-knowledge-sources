# [Issue #83] [Documentation]: using-rocprofv3.rst: Grid_<> should be just threads not thread blocks

source: https://github.com/ROCm/rocprofiler-sdk/issues/83
state: closed | updated: 2025-07-24T17:12:10Z
labels: documentation, Under Investigation

## 正文

### Description of errors

<!DOCTYPE html>
Grid_Size | Number of thread blocks required to launch the kernel.
-- | —
Grid_Size_n | Number of thread blocks in the nth dimension required to launch the kernel, where n = X, Y, or Z.

Shoudl it "total number of threads" and NOT "thread blocks"? 

### Attach any links, screenshots, or additional evidence you think will be helpful.

[https://github.com/ROCm/rocprofiler-sdk/blob/amd-staging/source/docs/how-to/using-rocprofv3.rst#output-file-fields](url)

## 评论 (9)

### harkgill-amd · 2025-07-14

Hi @srinathv, `Grid_Size` is the number of thread blocks in the grid whereas `block_size` would be be the number of threads per block. Here's an excerpt from the [HIP Programming Guide](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#single-instruction-multiple-threads-simt) that may be helpful,

- The number of blocks to launch, which defines the grid size (relating to blockDim).
- The number of threads in a block, which defines the block size (relating to blockIdx).

The [Hierarchical Thread Model](https://rocm.docs.amd.com/projects/HIP/en/latest/understand/programming_model.html#hierarchical-thread-model) also better explains this concept,

- Threads are single instances of kernel operations, running concurrently across warps
- Blocks group threads together and enable cooperation and shared memory
- Grids define the number of thread blocks for a single kernel launch

### srinathv · 2025-07-14

Thank you for the clarification.  I will review the test code results to understand my disconnect. 


### markstock · 2025-07-14

A very simple code which creates 1024 workgroups, each with 1024 work items shows the problem. The relevant lines are:
```
# in the program
hipLaunchKernelGGL(simple_add_kernel, 1024, 1024, 0, 0, d_out, d_in, num_elements);
# on the command-line
hipcc --offload-arch=gfx942 simple_kernel.cpp
rocprofv3 --kernel-trace --stats -- ./a.out
```
When compiled with hipcc from rocm/6.3.1, 6.4.0, or 6.4.1, we get the following rocprof output:
```
"Kind","Agent_Id","Queue_Id","Thread_Id","Dispatch_Id","Kernel_Id","Kernel_Name","Correlation_Id","Start_Timestamp","End_Timestamp","Private_Segment_Size","Group_Segment_Size","Workgroup_Size_X","Workgroup_Size_Y","Workgroup_Size_Z","Grid_Size_X","Grid_Size_Y","Grid_Size_Z"
"KERNEL_DISPATCH",4,1,40021,1,11,"simple_add_kernel(float*, float const*, int)",1,2060159320877,2060159329157,0,0,1024,1,1,1048576,1,1
```
If the documentation were correct, I would expect that line to end with `1024,1,1,1024,1,1`.

### harkgill-amd · 2025-07-14

Thanks for pointing this out, was able to reproduce it on my end as well. Not sure if this is necessarily a documentation update or an incorrect value being pushed for `Grid_Size_X` which needs to be fixed. Will investigate and update.

### jrmadsen · 2025-07-15

It appears what we are getting from the internals of ROCm have grid size and workgroup size flipped. Workgroup size is defined by the number of threads in a grid * the number of grids. So Grid_X should be 1024 and Workgroup_X should be 1,048,576 (1024 *1024)

### markstock · 2025-07-15

@jrmadsen rocprof's current output has been consistent for years, and this seems like a new definition of Workgroup size. My personal preference - and how I've been using the language - would have workgroup size be 1024 and grid size be 1024. Maybe "work item" size would be 1024^2.

### srinathv · 2025-07-15

I see @markstock 's comment also highlights the mixing of OpenCL and AMD terminology. 

Workitem  — thread
work group - thread block  <= 1024 threads 
grid - bunch of thread blocks  <= 1024 blocks

wavefront - simD grouping of threads (64 threads per wavefront) 
 
Warp - simT grouping of threads ( 32 threads per warp)


Please pick one and stay consistent.  Then use said terminology in the tool's output with the correct value.  



### harkgill-amd · 2025-07-24

After discussing the discrepancy between the output fields (HSA/OpenCL spec) and the documentation (HIP spec) with the team, we decided to update the docs to align with the HSA/OpenCL definitions. https://github.com/ROCm/rocprofiler-sdk/commit/e948034c835e10c8e8af22f81ccebc4171281352 updates the documentation entries for `Workgroup_Size`, `Grid_Size` and `Grid_Size_n` to the following,

https://github.com/ROCm/rocprofiler-sdk/blob/3a36fd13fed56f9b00ba452d23a27365e892e89e/source/docs/how-to/using-rocprofv3.rst?plain=1#L1530-L1540

With these changes, the aim was to clearly describe the output value for rocprofv3 while also highlighting the equivalent value following the HIP definitions.

### markstock · 2025-07-24

Great - glad to see this resolved so quickly. Thank you!
