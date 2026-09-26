# [Issue #82] [Issue]: rocprofv3 BEFORE flux run is not working

source: https://github.com/ROCm/rocprofiler-sdk/issues/82
state: closed | updated: 2025-08-07T18:30:41Z
labels: Under Investigation

## 正文

### Problem Description

On a system that uses the Flux scheduler,  `rocprofv3` **before** the mpi launcher `flux run` does not work:

Error: 
$ rocprofv3 -- flux run -N 1 -n 1 ./mpi_hip_matrix_norm-output
flux-run: ERROR: signal handler must be signal.SIG_IGN, signal.SIG_DFL, or a callable object

Note:
$ flux run -N 1 -n 1 rocprofv3 -- ./mpi_hip_matrix_norm-output
exits clean. 

### Operating System

OS: NAME="Red Hat Enterprise Linux" VERSION="8.10 (Ootpa)"

### CPU

model name      : AMD Instinct MI300A Accelerator

### GPU

model name      : AMD Instinct MI300A Accelerator

### ROCm Version

ROCm 6.4.1

### ROCm Component

rocprofiler

### Steps to Reproduce

On a system running the flux scheduler (LC at LLNL).  An test with rocrpofv3 as described in https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/latest/how-to/using-rocprofv3-with-mpi.html#using-rocprofv3-with-mpi


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (6)

### ppanchad-amd · 2025-07-14

Hi @srinathv. Internal ticket has been created to investigate this issue. Thanks!

### darren-amd · 2025-07-21

Hi @srinathv,

Thanks for reporting the issue. Could you please share the sample `mpi_hip_matrix_norm-output` that you are running? Could you also verify if the same issue occurs with mpi? Thanks! 

### srinathv · 2025-07-23

The test example:

#include <mpi.h>
#include <hip/hip_runtime.h>
#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define N 1024 // Matrix size (N x N)
#define NUM_ITER 100 // Reduced for debugging purposes

__global__ void compute_l2_norm(const float* matrix, float* norm, int n) {
    __shared__ float sum[256];
    int idx = threadIdx.x + blockIdx.x * blockDim.x;
    int tid = threadIdx.x;

    sum[tid] = 0.0f;

    for (int i = idx; i < n * n; i += blockDim.x * gridDim.x) {
        sum[tid] += matrix[i] * matrix[i];
    }

    __syncthreads();

    for (int s = blockDim.x / 2; s > 0; s >>= 1) {
        if (tid < s) {
            sum[tid] += sum[tid + s];
        }
        __syncthreads();
    }

    if (tid == 0) {
        atomicAdd(norm, sum[0]);
    }
}

void generate_random_matrix(float* matrix, int size) {
    for (int i = 0; i < size * size; ++i) {
        matrix[i] = static_cast<float>(rand()) / RAND_MAX;
    }
}

float compute_matrix_norm(float* d_matrix, float* d_norm, int n) {
    const int threads_per_block = 256;
    const int blocks_per_grid = (n * n + threads_per_block - 1) / threads_per_block;

    hipMemset(d_norm, 0, sizeof(float));

    hipLaunchKernelGGL(compute_l2_norm, dim3(blocks_per_grid), dim3(threads_per_block), 0, 0, d_matrix, d_norm, n);

    float norm = 0.0f;
    hipMemcpy(&norm, d_norm, sizeof(float), hipMemcpyDeviceToHost);

    return std::sqrt(norm);
}

void using_allreduce(MPI_Comm comm, const std::vector<float>& norms, std::vector<float>& smallest_norms) {
    float local_min = *std::min_element(norms.begin(), norms.end());
    float global_min;

    MPI_Allreduce(&local_min, &global_min, 1, MPI_FLOAT, MPI_MIN, comm);

    smallest_norms.push_back(global_min);
}

void using_reduce_bcast(MPI_Comm comm, const std::vector<float>& norms, std::vector<float>& smallest_norms) {
    float local_min = *std::min_element(norms.begin(), norms.end());
    float global_min;
    const int root = 0;

    int rank;
    MPI_Comm_rank(comm, &rank);

    if (rank == root) {
        MPI_Reduce(MPI_IN_PLACE, &global_min, 1, MPI_FLOAT, MPI_MIN, root, comm);
    } else {
        MPI_Reduce(&local_min, &global_min, 1, MPI_FLOAT, MPI_MIN, root, comm);
    }

    MPI_Bcast(&global_min, 1, MPI_FLOAT, root, comm);

    smallest_norms.push_back(global_min);
}

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm comm = MPI_COMM_WORLD;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    hipSetDevice(rank);

    srand(time(NULL) + rank);

    const int matrix_size = N * N;
    float* h_matrix = new float[matrix_size];
    float* d_matrix;
    float* d_norm;

    hipMalloc(&d_matrix, matrix_size * sizeof(float));
    hipMalloc(&d_norm, sizeof(float));

    std::vector<float> norms;
    for (int iter = 0; iter < NUM_ITER; ++iter) {
        generate_random_matrix(h_matrix, N);

        hipMemcpy(d_matrix, h_matrix, matrix_size * sizeof(float), hipMemcpyHostToDevice);

        float norm = compute_matrix_norm(d_matrix, d_norm, N);

        norms.push_back(norm);

        // Print intermediate norms for debugging
        std::cout << "Iteration " << iter << ", Rank " << rank << ": Norm = " << norm << std::endl;
    }

    std::vector<float> smallest_norms_allreduce;
    std::vector<float> smallest_norms_reduce_bcast;

    using_allreduce(comm, norms, smallest_norms_allreduce);
    using_reduce_bcast(comm, norms, smallest_norms_reduce_bcast);

    if (rank == 0) {
        std::cout << "Smallest norms using MPI_Allreduce: ";
        for (float val : smallest_norms_allreduce) {
            std::cout << val << " ";
        }
        std::cout << "\n";

        std::cout << "Smallest norms using MPI_Reduce + MPI_Bcast: ";
        for (float val : smallest_norms_reduce_bcast) {
            std::cout << val << " ";
        }
        std::cout << "\n";
    }

    delete[] h_matrix;
    hipFree(d_matrix);
    hipFree(d_norm);

    MPI_Finalize();
    return 0;
}


--- 
I have not tested vs. mpi run. 

### srinathv · 2025-07-25

Today I have tested with a build of OpenMPI on mi300a system.  The example code _does_ run to completion with rocprov3 BEFORE mpirun.  

Note, this OpenMPI build does NOT exploit the Slingshot attributes of the system of interest. 


### darren-amd · 2025-08-06

Hi @srinathv,

The issue appears to be coming from when flux is trying to restore the signal handlers [here](https://github.com/flux-framework/flux-core/blob/56c98db68acee51db413ecf9d53f2e4588bf378b/src/bindings/python/flux/util.py#L97). I believe it is due to an issue with flux trying to use the signal handlers that rocprofv3 set. I was able to fix the issue by validating the signal before restoring it, such as:
```
def func_wrapper(future, *args, **kwargs):
        # python only allows `signal.signal` calls in the main thread
        active = False
        original_handler = None
        flux_handle = future.get_flux()
        if (
            threading.current_thread() is threading.main_thread()
            and flux_handle is not None
            and not flux_handle.reactor_running()
        ):
            handler_to_restore = signal.getsignal(signal.SIGINT)

            # change here
            is_valid_handler = callable(handler_to_restore) or handler_to_restore in (
                signal.SIG_DFL,
                signal.SIG_IGN,
            )

            if is_valid_handler:
                original_handler = handler_to_restore
            else:
                original_handler = signal.SIG_DFL
            # end change

            signal.signal(signal.SIGINT, signal.SIG_DFL)
            active = True

        retval = func(future, *args, **kwargs)

        if active:
            signal.signal(signal.SIGINT, original_handler)
        return retval

    return func_wrapper
```

I would also suggest opening a ticket in the flux repository, in case this comes up in future workloads.


### systems-assistant[bot] · 2025-08-07

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/144
