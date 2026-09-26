source: https://docs.nvidia.com/deploy/mps/common-tasks.html

# Common Tasks[#](https://docs.nvidia.com#common-tasks)

This page covers common MPS administration and usage tasks. Where the commands differ
between [Legacy MPS v2](https://docs.nvidia.com/mpsv2-interface.html#mpsv2-interface) and [MPS v3](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-interface), both
are shown in the tabs below.

## nvidia-cuda-mps-control[#](https://docs.nvidia.com#nvidia-cuda-mps-control)

Typically stored under `/usr/bin`

on Linux and QNX systems and typically run with
superuser privileges, this control daemon is used to manage the `nvidia-cuda-mps-server`

described in the following section. These are the relevant use cases:

```
$ nvidia-cuda-mps-control -d # Start daemon in background process.
$ ps -ef | grep mps # Check if the MPS daemon is running, for Linux.
$ pidin | grep mps # See if the MPS daemon is running, for QNX.
$ echo quit | nvidia-cuda-mps-control # Shut the daemon down.
$ nvidia-cuda-mps-control -f # Start daemon in foreground.
$ nvidia-cuda-mps-control -v # Print version of control daemon executable.
$ nvidia-cuda-mps-control -S # Start daemon with static partitioning mode enabled.
```

```
$ nvidia-cuda-mps-control -d -p 3 # Start daemon in background process.
$ nvidia-cuda-mps-control server list # List running MPS servers.
$ nvidia-cuda-mps-control -q # Shut the daemon down.
$ nvidia-cuda-mps-control -f -p 3 # Start daemon in foreground.
$ nvidia-cuda-mps-control -v # Print version of control daemon executable.
```

The nvidia-cuda-mps-control has a man page available as part of the installation:

`man nvidia-cuda-mps-control`


## nvidia-cuda-mps-server[#](https://docs.nvidia.com#nvidia-cuda-mps-server)

Typically stored under `/usr/bin`

on Linux and QNX systems, this daemon is run under the
same $UID as the client application running on the node. The `nvidia-cuda-mps-server`

instances are created on-demand when client applications connect to the
control daemon. The server binary should not be invoked directly, and instead the
control daemon should be used to manage the startup and shutdown of servers.

The `nvidia-cuda-mps-server`

process owns the CUDA context on the GPU and
uses it to execute GPU operations for its client application processes. Due to this, when
querying active processes via `nvidia-smi`

(or any NVML-based application) `nvidia-cuda-mps-server`

will appear as the active CUDA process rather than any of the client processes.

The version of the `nvidia-cuda-mps-server`

executable can be printed with:

```
nvidia-cuda-mps-server -v
```

## Starting and Stopping MPS on Linux[#](https://docs.nvidia.com#starting-and-stopping-mps-on-linux)

To view the daemon and server log files, refer to [Appendix: Logging](https://docs.nvidia.com/appendix-logging.html#appendix-logging).

### On a Multi-user System[#](https://docs.nvidia.com#on-a-multi-user-system)

To cause all users of the system to run CUDA applications via MPS you will need to set up the MPS control daemon to run when the system starts.

#### Starting MPS control daemon[#](https://docs.nvidia.com#starting-mps-control-daemon)

As root, run the commands:

```
$ export CUDA_VISIBLE_DEVICES=0 # Select GPU 0.
$ nvidia-smi -i 0 -c EXCLUSIVE_PROCESS # Set GPU 0 to exclusive mode.
$ nvidia-cuda-mps-control -d # Start the daemon.
```

```
$ export CUDA_VISIBLE_DEVICES=0 # Select GPU 0.
$ nvidia-smi -i 0 -c EXCLUSIVE_PROCESS # Set GPU 0 to exclusive mode.
$ nvidia-cuda-mps-control -d -p 3 # Start the daemon.
```

This will start the MPS control daemon that will spawn a new MPS Server instance
for any $UID starting an application and associate it with the GPU visible to the control
daemon. Only one instance of the `nvidia-cuda-mps-control`

daemon should be run per
node. Note that `CUDA_VISIBLE_DEVICES`

should not be set in the client process’s
environment.

Under MPS v3, each connecting UID is automatically served by a `uid_<uid>`

server. You
can also create named servers explicitly; refer to [MPS v3 Interface](https://docs.nvidia.com/mpsv3-interface.html#mpsv3-interface).

#### Shutting Down MPS Control Daemon[#](https://docs.nvidia.com#shutting-down-mps-control-daemon)

To shut down the daemon, as root, run:

```
$ echo quit | nvidia-cuda-mps-control
```

```
$ nvidia-cuda-mps-control -q
```

### On a Single-User System[#](https://docs.nvidia.com#on-a-single-user-system)

When running as a single user, the control daemon must be launched with the same user ID as that of the client process.

#### Starting MPS Control Daemon[#](https://docs.nvidia.com#id2)

As $UID, run the commands:

```
$ export CUDA_VISIBLE_DEVICES=0 # Select GPU 0.
$ export CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps # Select a location that's accessible to the given $UID.
$ export CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log # Select a location that's accessible to the given $UID.
$ nvidia-cuda-mps-control -d # Start the daemon.
```

```
$ export CUDA_VISIBLE_DEVICES=0 # Select GPU 0.
$ export CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps # Select a location that's accessible to the given $UID.
$ export CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log # Select a location that's accessible to the given $UID.
$ nvidia-cuda-mps-control -d -p 3 # Start the daemon.
```

This will start the MPS control daemon that will spawn a new MPS Server instance for that $UID starting an application and associate it with GPU visible to the control daemon.

#### Starting MPS client application[#](https://docs.nvidia.com#starting-mps-client-application)

Set the following variables in the client process’s environment. Note that
`CUDA_VISIBLE_DEVICES`

should not be set in the client’s environment.

```
$ export CUDA_MPS_PIPE_DIRECTORY=/tmp/nvidia-mps # Set to the same location as the MPS control daemon.
$ export CUDA_MPS_LOG_DIRECTORY=/tmp/nvidia-log # Set to the same location as the MPS control daemon.
```

#### Shutting Down MPS[#](https://docs.nvidia.com#shutting-down-mps)

To shut down the daemon, as $UID, run:

```
$ echo quit | nvidia-cuda-mps-control
```

```
$ nvidia-cuda-mps-control -q
```

## Best Practices for SM Partitioning[#](https://docs.nvidia.com#best-practices-for-sm-partitioning)

Creating a context is a costly operation in terms of time, memory, and the hardware resources.

If a context with execution affinity is created at kernel launch time, the user will observe a sudden increase in latency and memory footprint as a result of the context creation. To avoid paying the latency of context creation and the abrupt increase in memory usage at kernel launch time, it is recommended that users create a pool of contexts with different SM partitions upfront and select context with the suitable SM partition on kernel launch:

```
int device = 0;
cudaDeviceProp prop;
const Int CONTEXT_POOL_SIZE = 4;
CUcontext contextPool[CONTEXT_POOL_SIZE];
int smCounts[CONTEXT_POOL_SIZE];
cudaSetDevice(device);
cudaGetDeviceProperties(&prop, device);
smCounts[0] = 1; smCounts[1] = 2;
smCounts[3] = (prop. multiProcessorCount - 3) / 3;
smCounts[4] = (prop. multiProcessorCount - 3) / 3 * 2;
for (int i = 0; i < CONTEXT_POOL_SIZE; i++) {
CUexecAffinityParam affinity;
affinity.type = CU_EXEC_AFFINITY_TYPE_SM_COUNT;
affinity.param.smCount.val = smCounts[i];
cuCtxCreate_v3(&contextPool[i], affinity, 1, 0, deviceOrdinal);
}
for (int i = 0; i < CONTEXT_POOL_SIZE; i++) {
std::thread([i]() {
int numSms = 0;
int numBlocksPerSm = 0;
int numThreads = 128;
CUexecAffinityParam affinity;
cuCtxSetCurrent(contextPool[i]);
cuCtxGetExecAffinity(&affinity, CU_EXEC_AFFINITY_TYPE_SM_COUNT);
numSms = affinity.param.smCount.val;
cudaOccupancyMaxActiveBlocksPerMultiprocessor(
&numBlocksPerSm, kernel, numThreads, 0);
void *kernelArgs[] = { /* add kernel args */ };
dim3 dimBlock(numThreads, 1, 1);
dim3 dimGrid(numSms * numBlocksPerSm, 1, 1);
cudaLaunchCooperativeKernel((void*)my_kernel, dimGrid, dimBlock, kernelArgs);
};
}
```

### Using Static SM Partitioning[#](https://docs.nvidia.com#using-static-sm-partitioning)

Static SM partitioning mode allows users to create exclusive SM partitions for MPS clients on NVIDIA Ampere architecture and newer GPUs, providing deterministic resource allocation and improved isolation.

Starting with Driver version r610, partial error isolation is supported when static SM partitioning
is enabled. Because an SM is owned only by one partition, the driver can attribute SM error state to the faulting
partition/client. Clients in different SM partitions are isolated from each other’s SM-triggered faults.
On fault detection, the driver terminates work for the faulting client and prevents additional work
from being submitted. Terminated operations may report `CUDA_ERROR_LAUNCH_FAILED`

or a more specific CUDA error. It
should be noted that this is a partial isolation not a guarantee that every possible GPU or system-level failure
is isolated per process.

Performance note

This mode trades some MPS flexibility for isolation. SMs reserved for a partition remain exclusive to the clients assigned to that partition; other clients cannot automatically borrow idle SMs from it. It is best suited for workloads with known resource needs, workloads that can tolerate strict resource limits, or deployments where fault containment is more important than opportunistic sharing.

The following example demonstrates the minimal workflow for configuring and using static partitions.

#### Basic Workflow[#](https://docs.nvidia.com#basic-workflow)

```
# 1. Start the MPS control daemon with static partitioning enabled
$ nvidia-cuda-mps-control -d -S
# 2. Create an SM partition with 7 chunks. The first partitioning command
# will perform a lightweight CUDA initialization.
$ echo "sm_partition add GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65 7" | nvidia-cuda-mps-control
GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65/Dx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# 3. View the current partitioning configuration
$ echo "lspart" | nvidia-cuda-mps-control
GPU Partition free used free used clients
chunk chunk SM SM
GPU-74d43ed3 - 3 7 24 56 -
GPU-74d43ed3 Dx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA - 7 - 56 -
# 4. Assign the partition to a client application. The MPS server will start
# on client application connection.
$ export CUDA_MPS_SM_PARTITION=GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65/Dx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
$ ./nbody
# 5. After the application completes, remove the partition
$ echo "sm_partition rm GPU-74d43ed3 Dx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" | nvidia-cuda-mps-control
```

```
# 1. Start the MPS control daemon
$ nvidia-cuda-mps-control -d -p 3
# 2. Create a server to own the partitions
$ nvidia-cuda-mps-control server create training
# 3. Create an SM partition with 4 chunks
$ nvidia-cuda-mps-control sm-partition create large --server=training --device=GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65 --chunks=4
SM partition 'large' created on device GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65 (sm-count=34)
CUDA_MPS_SM_PARTITION=GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65/Kp8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# 4. View the current partitioning configuration
$ nvidia-cuda-mps-control sm-partition list --server=training --all
SERVER DEVICE NAME CHUNKS SM-COUNT INCLUDE-REMAINDER STATUS VISIBLE-UUID
training GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65 large 4 34 false created Kp8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# 5. Assign the partition to a client application. The MPS server will start
# on client application connection.
$ export CUDA_MPS_SM_PARTITION=GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65/Kp8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
$ ./nbody
# 6. After the application completes, remove the partition
$ nvidia-cuda-mps-control sm-partition delete large --server=training --device=GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65
```

#### Multiple Partitions Example[#](https://docs.nvidia.com#multiple-partitions-example)

The following example demonstrates creating multiple partitions for different workloads:

```
# Start MPS control with static partitioning
$ nvidia-cuda-mps-control -d -S
# View the current partitioning configuration
$ echo "lspart" | nvidia-cuda-mps-control
GPU Partition free used free used clients
chunk chunk SM SM
GPU-74d43ed3 - 10 0 92 92 -
# Create three partitions with different sizes
$ echo "sm_partition add GPU-74d43ed3 5" | nvidia-cuda-mps-control
GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65/Dx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
$ echo "sm_partition add GPU-74d43ed3 3" | nvidia-cuda-mps-control
GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65/Cx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
$ echo "sm_partition add GPU-74d43ed3 2" | nvidia-cuda-mps-control
GPU-74d43ed3-cdf7-e667-3644-bf5b4f46ed65/Bx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# Run different applications on different partitions
$ CUDA_MPS_SM_PARTITION=GPU-74d43ed3/Dx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ./large_workload &
$ CUDA_MPS_SM_PARTITION=GPU-74d43ed3/Cx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ./medium_workload &
$ CUDA_MPS_SM_PARTITION=GPU-74d43ed3/Bx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ./small_workload &
# Check partition usage
$ echo "lspart" | nvidia-cuda-mps-control
GPU Partition free used free used clients
chunk chunk SM SM
GPU-74d43ed3 - 0 10 0 80 -
GPU-74d43ed3 Dx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA - 5 - 40 Yes
GPU-74d43ed3 Cx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA - 3 - 24 Yes
GPU-74d43ed3 Bx4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA - 2 - 28 Yes
```

```
# Start the MPS control daemon and create a server
$ nvidia-cuda-mps-control -d -p 3
$ nvidia-cuda-mps-control server create training
# Create three partitions with different sizes. Each prints the value to
# assign to CUDA_MPS_SM_PARTITION.
$ nvidia-cuda-mps-control sm-partition create large --server=training --device=0 --chunks=5
$ nvidia-cuda-mps-control sm-partition create medium --server=training --device=0 --chunks=3
$ nvidia-cuda-mps-control sm-partition create small --server=training --device=0 --chunks=2
# View the current partitioning configuration
$ nvidia-cuda-mps-control sm-partition list --server=training --all
SERVER DEVICE NAME CHUNKS SM-COUNT INCLUDE-REMAINDER STATUS VISIBLE-UUID
training GPU-74d43ed3 large 5 40 false created Kp8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
training GPU-74d43ed3 medium 3 24 false created Jn6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
training GPU-74d43ed3 small 2 28 false created Hm2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# Run different applications on different partitions
$ CUDA_MPS_SM_PARTITION=GPU-74d43ed3/Kp8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ./large_workload &
$ CUDA_MPS_SM_PARTITION=GPU-74d43ed3/Jn6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ./medium_workload &
$ CUDA_MPS_SM_PARTITION=GPU-74d43ed3/Hm2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA ./small_workload &
```