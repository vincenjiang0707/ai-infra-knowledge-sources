source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/performance_and_tuning.html

# Performance and tuning[](https://docs.nvidia.com#performance-and-tuning)

## Performance issues[](https://docs.nvidia.com#performance-issues)

Performance issues may be caused by a variety of factors and may be specific to a particular application or particular hardware. Under these conditions it is important to differentiate a NCCL performance bug from possible configuration or hardware issues.

`nvbandwidth`

([https://github.com/NVIDIA/nvbandwidth](https://github.com/NVIDIA/nvbandwidth)). This tool can be used to measure GPU memory bandwidth and GPU-to-GPU bandwidth (via NVLink or PCIe). When compiled with multinode support, it can also measure Multi-node NVLink (MNNVL) bandwidth between nodes.

`nvloom`

([https://github.com/NVIDIA/nvloom](https://github.com/NVIDIA/nvloom)). Is an alternative tool to measure GPU memory bandwidth and GPU-to-GPU bandwidth (via NVLink or PCIe). It delivers similar functionality to `nvbandwidth`

, however, it also provides benchmarks for NVLink SHARP systems.

### Intra-node communication[](https://docs.nvidia.com#intra-node-communication)

By default, `nvbandwidth`

is compiled to test intra-node communication. Possible issues to look out for are node topology and NVLink issues.
`nvidia-smi topo -m`

shows the intra-node topology, which can be used to determine the expected communication bandwidth between components.
Another check to run is `nvidia-smi topo -p2p n`

to verify if GPUs can communicate directly with each other over NVLink. With this information `nvbandwidth`

can be used to verify if the expected bandwidth between individual pairs of GPUs can be achieved (via PCIe or NVLink).

In the case of `nvloom`

pairwise and multicast tests can be run in order to benchmark local communication:

```
srun/mpirun -n <number of processes> ./nvloom -s pairwise --sizeMin 1M --sizeMax 4G
srun/mpirun -n <number of processes> ./nvloom -s multicast --sizeMin 1M --sizeMax 4G
```

### Inter-node communication[](https://docs.nvidia.com#inter-node-communication)

To profile inter-node performance, `nvbandwidth`

must be compiled with multinode support:

```
cmake -DMULTINODE=1 .
make
```

Once compiled, the tool can be used to measure the bandwidth and latency of the network.

```
srun/mpirun -n <number of processes> ./nvbandwidth -p multinode
```

This will run tests prefixed with `multinode`

using given number of processes.

The equivalent test for `nvloom`

is to run:

```
srun/mpirun -n <number of processes> ./nvloom -p gpu-to-rack rack-to-rack fabric-stress --sizeMin 1M --sizeMax 4G
```

Bandwidth reported by `nvbandwidth`

(or `nvloom`

) lower than the expected peak bandwidth indicates an issue with
inter-GPU communication. One possible cause is that there is no NVLink connection between the GPUs. Please use `nvidia-smi topo -p2p n`

to verify
if GPUs can communicate directly with each other over NVLink.

To test fabric performance, `ib_write_bw`

and `ib_write_lat`

can be used to
measure bandwidth and latency between nodes, as described in
[Networking Troubleshooting](https://docs.nvidia.com/networking_troubleshooting.html).

If `nvbandwidth`

/`nvloom`

and `ib_write_bw`

results match the expectations for the hardware but NCCL performance is below expectations, the NCCL configuration might be suboptimal. Check [Tuning NCCL configuration](https://docs.nvidia.com#optimize-nccl-config) for the guidance on tweaking NCCL configuration.

### Multi-node NVLink (MNNVL) issues[](https://docs.nvidia.com#multi-node-nvlink-mnnvl-issues)

NCCL uses MNNVL for inter-node communication within the same NVLink domain if available. If it is not used and not disabled by the user (i.e. NCCL_MNNVL_ENABLE is not set to 0) there might be an underlying issue with the service.
To diagnose the issue, you may use Internode Memory Exchange (IMEX) service. You can use `nvidia-imex-ctl`

utility to check the status of the IMEX domain. NOTE: this requires IMEX daemon to be running on every node of the domain and may potentially require sudo privileges.

```
nvidia-imex-ctl -H -N
```

Check the output first for the `Domain State`

line. If it is not `UP`

then you should check status of each node in the domain and their connectivity matrices. Some of the common causes of issues may include:

Node down (status

`UNAVAILABLE`

and connectivity matrix shows`I/N/D`

)Driver version mismatch between nodes (status

`READY`

and connectivity matrix shows`V`

)

A healthy IMEX domain should have all nodes in the domain in the `READY`

state and connectivity matrix showing `C`

.

In some cases NCCL may report this warning:

```
transport/p2p.cc:XXX NCCL WARN Cuda failure 800 'operation not permitted'
```

This may indicate that the current user has no write access to IMEX security files located at `/dev/nvidia-caps-imex-channels/channel*`

.
Changing their permissions to allow write access should fix the issue.

In cases when user has no access to IMEX daemon an alternative is to use `nvidia-smi -q | grep -v GUID | grep -A4 Fabric`

to check the NVLink fabric status as well as verify that the cliqueId is the same across all the nodes in the NVLink domain.

### Tuning NCCL configuration[](https://docs.nvidia.com#tuning-nccl-configuration)

NCCL is tuned to run optimally on a wide range of systems and re-tuned with newer release. However, there are some edge cases where a system can benefit from different settings. The most common tuning parameters are listed below.

NOTE: In general we discourage the use of these variables in production since a tuning gain in one benchmark situation can lead to suboptimal settings elsewhere.

```
NCCL_MIN_CTAS, NCCL_MAX_CTAS - Increasing the number of CTAs will consume more GPU resources but possibly increase throughput.
NCCL_CHUNK_SIZE - Controls the size of messages sent through the network for ncclSend/ncclRecv and AlltoAll operations.
Increasing this number may help improve bandwidth in latency-bound cases.
NCCL_IB_QPS_PER_CONNECTION - This controls the number of QPs per connection. The default value is 1. However, on
systems with ECMP routing enabled or multiple ports per NIC, increasing this value
can improve path diversity on the network and increase throughput.
NCCL_CROSS_NIC - This controls whether NCCL allows rings and trees to use different NICs, causing inter-node
communication to use different NICs on different nodes. Forcing cross-NIC communication may
improve performance in unoptimized rail configurations but may create congestion on other
networks. The default value is 2.
```

#### RoCE considerations[](https://docs.nvidia.com#roce-considerations)

On RoCE fabric, using multiple QPs per connection is often necessary to achieve optimal performance.

### CPU and memory affinity[](https://docs.nvidia.com#cpu-and-memory-affinity)

Incorrect process placement with respect to the CPU and memory can have a serious performance impact. On NUMA systems, each rank should generally use CPU cores and host memory close to its GPU and, for multi-node jobs, its NIC.

#### How NCCL handles affinity[](https://docs.nvidia.com#how-nccl-handles-affinity)

By default, NCCL uses the intersection of the CPU affinity inherited from the launcher or parent process and the CPU affinity associated with the GPU.
If the intersection is empty, NCCL leaves the inherited CPU affinity unchanged.
Setting `NCCL_IGNORE_CPU_AFFINITY=1`

makes NCCL ignore the inherited affinity and use the GPU affinity only.
NCCL still cannot use CPUs excluded by cpuset, cgroup, or container restrictions.
Set CPU, GPU, and memory placement before NCCL communicators are created.

To inspect the affinity used by NCCL, run with:

```
NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,GRAPH,ENV ./my_nccl_app
```

Look for `ncclTopoGetCpuAffinity: Affinity for GPU ...`

in the log.
Use `nvidia-smi topo -m`

and `lscpu --extended=CPU,NODE,SOCKET,CORE`

to inspect GPU, NIC, CPU, and NUMA locality.

#### Controlling affinity with Slurm[](https://docs.nvidia.com#controlling-affinity-with-slurm)

Slurm controls CPU and memory placement with `--cpu-bind`

and `--mem-bind`

when the required task affinity support is configured by the site.
GPU assignment and binding use Slurm’s GRES/TRES support, for example `--gpu-bind`

or `--tres-bind=gres/gpu:...`

.
`CUDA_VISIBLE_DEVICES`

can also be used to control which GPUs are visible to each process.

#### Controlling affinity with Open MPI `mpirun`

[](https://docs.nvidia.com#controlling-affinity-with-open-mpi-mpirun)

Open MPI provides `--map-by`

and `--bind-to`

for rank and CPU placement.
Use `--report-bindings`

to verify the resulting CPU binding, for example:

```
mpirun -np <nranks> \
--map-by ppr:1:numa:PE=<cores_per_rank> \
--bind-to core \
--report-bindings \
./my_nccl_app
```

GPU assignment remains application- or launcher-specific; select the intended GPU per local rank or set `CUDA_VISIBLE_DEVICES`

appropriately.

As an alternative for direct launches or wrapper scripts, `numactl`

can bind a process to specific CPU cores or NUMA memory nodes.