source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/system-setup/multi-node-setup.html

# Multi-node setup for AI workloads[#](https://rocm.docs.amd.com#multi-node-setup-for-ai-workloads)

2026-02-19

6 min read time

AMD provides ready-to-use Docker images for AMD Instinct™ MI300X and MI325X GPUs containing ROCm-capable deep learning frameworks and essential software components. These Docker images can run and leverage multiple nodes if they are available. This page describes how to enable the multi-node training of AI workloads on AMD Instinct GPUs.

## Prerequisites[#](https://rocm.docs.amd.com#prerequisites)

Before starting, ensure your environment meets the following requirements:

Multi-node networking: your cluster should have a configured multi-node network. For setup instructions, see the

[Multi-node network configuration for AMD Instinct GPUs](https://instinct.docs.amd.com/projects/gpu-cluster-networking/en/latest/how-to/multi-node-config.html)guide in the Instinct documentation.ROCm Docker container to simplify environment setup for AI workloads. See the following resources to get started:

Slurm workload manager to run the

[provided examples](https://rocm.docs.amd.com#multi-node-setup-training-examples).

## Install required packages[#](https://rocm.docs.amd.com#install-required-packages)

To run multi-node workloads, ensure you have all the required packages installed based on your network device. For example, on Ubuntu systems:

```
apt install -y iproute2
apt install -y linux-headers-"$(uname -r)" libelf-dev
apt install -y gcc make libtool autoconf librdmacm-dev rdmacm-utils infiniband-diags ibverbs-utils perftest ethtool libibverbs-dev rdma-core strace libibmad5 libibnetdisc5 ibverbs-providers libibumad-dev libibumad3 libibverbs1 libnl-3-dev libnl-route-3-dev
```

### Compile and install the RoCE library[#](https://rocm.docs.amd.com#compile-and-install-the-roce-library)

If you’re using Broadcom NICs, you need to compile and install the RoCE (RDMA
over Converged Ethernet) library. See [RoCE cluster network configuration guide
for AMD Instinct GPUs](https://instinct.docs.amd.com/projects/gpu-cluster-networking/en/latest/how-to/roce-network-config.html)
for more information.

See the [Ethernet networking guide for AMD
Instinct MI300X GPU clusters: Compiling Broadcom NIC software from source](https://docs.broadcom.com/doc/957608-AN2XX#page=81) for more details.

Important

It is crucial to install the exact same version of the RoCE library that is installed on your host system. Also, ensure that the path to these libraries on the host is correctly mounted into your Docker container. Failure to do so can lead to compatibility issues and communication failures.

Set

`BUILD_DIR`

to the path on the host system where the Broadcom drivers and`bnxt_rocelib`

source are located. Then, navigate to the`bnxt_rocelib`

directory.export BUILD_DIR=/path/to/your/broadcom_drivers_on_host cd $BUILD_DIR/drivers_linux/bnxt_rocelib/

The

`bnxt_rocelib`

directory contains a version of`libbnxt_re`

in a zipped`.tar.gz`

file.tar -xf libbnxt_re-a.b.c.d.tar.gz cd libbnxt_re-a.b.c.d

Compile and install the RoCE library.

sh autogen.sh ./configure make find /usr/lib64/ /usr/lib -name "libbnxt_re-rdmav*.so" -exec mv {} {}.inbox \; make install all sh -c "echo /usr/local/lib >> /etc/ld.so.conf" ldconfig cp -f bnxt_re.driver /etc/libibverbs.d/ find . -name "*.so" -exec md5sum {} \; BUILT_MD5SUM=$(find . -name "libbnxt_re-rdmav*.so" -exec md5sum {} \; | cut -d " " -f 1)


## Environment setup[#](https://rocm.docs.amd.com#environment-setup)

Before running multi-node workloads, set these essential environment variables:

### Master address[#](https://rocm.docs.amd.com#master-address)

By default, `localhost`

is used for single-node configurations. Change
`localhost`

to the master node’s resolvable hostname or IP address:

```
export MASTER_ADDR="${MASTER_ADDR:-localhost}"
```

### Number of nodes[#](https://rocm.docs.amd.com#number-of-nodes)

Set the number of nodes you want to train on (for example, `2`

, `4`

, or `8`

):

```
export NNODES="${NNODES:-<num_nodes>}"
```

### Node ranks[#](https://rocm.docs.amd.com#node-ranks)

Set the rank of each node (`0`

for master, `1`

for the first worker node, and so on).
Node ranks should be unique across all nodes in the cluster.

```
export NODE_RANK="${NODE_RANK:-<node_rank>}"
```

### Network interface[#](https://rocm.docs.amd.com#network-interface)

Update the network interface in the script to match your system’s network interface. To find your network interface, run the following (outside of any Docker container):

```
ip a
```

Look for an active interface (status “UP”) with an IP address in the same subnet as your other nodes. Then, update the following variable in the script, for example:

```
export NCCL_SOCKET_IFNAME=ens50f0np0
```

This variable specifies which network interface to use for inter-node communication. Setting this variable to the incorrect interface can result in communication failures or significantly reduced performance.

Tip

This command sets `NCCL_SOCKET_IFNAME`

’s value to the last RDMA interface.

```
export NCCL_SOCKET_IFNAME=$(rdma link show | awk '{print $NF}' | sort | tail -n1)
```

### RDMA/IB interface[#](https://rocm.docs.amd.com#rdma-ib-interface)

Set the RDMA interfaces to be used for communication. NICs can come from different vendors and the names of the RDMA interface can be different. To get the list of all the RDMA/IB devices, run:

```
ibv_devices
```

The command below gets the list of all RDMA/IB devices and puts them in a
comma-separated format. If
(`rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7`

) are your RDMA
interfaces, then set:

```
# If using Broadcom NIC
export NCCL_IB_HCA=rdma0,rdma1,rdma2,rdma3,rdma4,rdma5,rdma6,rdma7
# If using Mellanox NIC
# export NCCL_IB_HCA=mlx5_0,mlx5_1,mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_8,mlx5_9
```

Tip

Alternatively, if you want to choose the RDMA interface automatically, you can use the following. This command will sort the RDMA interfaces and then select the first eight RDMA interfaces.

```
export NCCL_IB_HCA=$(ibv_devices | awk 'NR>2 {print $1}' | sort | head -n 8 | paste -sd,)
```

### Global ID index[#](https://rocm.docs.amd.com#global-id-index)

Update the global ID index if you’re using RoCE.

```
export NCCL_IB_GID_INDEX=3
```

## Multi-node training examples[#](https://rocm.docs.amd.com#multi-node-training-examples)

The following examples use the Slurm workload manager to launch jobs on
multiple nodes. To run these scripts as-is, you must have a Slurm environment
configured. The scripts are designed to work with both Broadcom Thor 2 and
Mellanox NICs by automatically installing the required libraries and setting
the necessary environment variables. For systems with Broadcom NICs, the
scripts assume the host’s RoCE library is located in the `/opt`

directory.

The following benchmarking examples demonstrate the training of a Llama 3 8B model across multiple 8-GPU nodes, using FSDP for intra-node parallelism and DP for inter-node parallelism.

### JAX MaxText[#](https://rocm.docs.amd.com#jax-maxtext)

Download the desired multi-node benchmarking script from

[ROCm/MAD](https://github.com/ROCm/MAD/tree/develop/scripts/jax-maxtext/gpu-rocm).`wget https://raw.githubusercontent.com/ROCm/MAD/refs/heads/develop/scripts/jax-maxtext/gpu-rocm/llama3_8b_multinode.sh`

Or clone the

[ROCm/MAD](https://github.com/ROCm/MAD)repository.git clone https://github.com/ROCm/MAD cd scripts/jax-maxtext/gpu-rocm

Run the benchmark for multi-node training.

sbatch -N <num_nodes> llama3_8b_multinode.sh


### PyTorch training[#](https://rocm.docs.amd.com#pytorch-training)

Note

The ROCm PyTorch Training Docker image now focuses on [Training a model
with Primus and PyTorch](https://rocm.docs.amd.com/training/benchmark-docker/primus-pytorch.html). The
following example refers to the legacy workflow [Training a
model with PyTorch](https://rocm.docs.amd.com/training/benchmark-docker/previous-versions/pytorch-training-v25.9.html#amd-pytorch-training-multinode-examples-v259).

Download the

`run_multinode_train.sh`

benchmarking script from[ROCm/MAD](https://github.com/ROCm/MAD/tree/develop/scripts/pytorch_train).`wget https://raw.githubusercontent.com/ROCm/MAD/refs/heads/develop/scripts/pytorch_train/run_multinode_train.sh`

Or clone the

[ROCm/MAD](https://github.com/ROCm/MAD)repository.git clone https://github.com/ROCm/MAD cd scripts/pytorch_train

Run the benchmark for multi-node training.

sbatch -N <num_nodes> run_multinode_train.sh


See also

See [Training a model with PyTorch](https://rocm.docs.amd.com/training/benchmark-docker/previous-versions/pytorch-training-v25.9.html#amd-pytorch-training-multinode-examples-v259) for more examples and information.

### Megatron-LM[#](https://rocm.docs.amd.com#megatron-lm)

Note

The Megatron-LM Docker image now focuses on [Training a model with
Primus and Megatron](https://rocm.docs.amd.com/training/benchmark-docker/previous-versions/primus-megatron-v25.8.html#amd-primus-megatron-multi-node-examples). The
following example refers to the legacy Megatron-LM [Training a model
with Megatron-LM](https://rocm.docs.amd.com/training/benchmark-docker/previous-versions/megatron-lm-v25.9.html#amd-megatron-lm-multi-node-examples) and might have
limited support.

Download the

`train_llama_slurm.sh`

benchmarking script from[ROCm/Megatron-LM](https://github.com/ROCm/Megatron-LM/blob/rocm_dev/examples/llama/train_llama_slurm.sh).Set the network interface parameters as per the above guidelines and run the script.

cd </path/to/your/Megatron-LM> export NETWORK_INTERFACE=$NCCL_SOCKET_IFNAME export NCCL_IB_HCA=$NCCL_IB_HCA export IMAGE=docker.io/rocm/megatron-lm:latest OR your preferred image export DATA_CACHE_PATH=/nfs/mounted/repo sbatch –N <num_nodes> examples/llama/train_llama_slurm.sh <MODEL_SIZE> <MBS> <GBS> <SEQ_LENGTH> <FSDP> <RECOMPUTE>


For example, to run a Llama 3 8B workload in BF16 precision, use the following command.

MODEL_NAME=llama3 sbatch –N 8 examples/llama/train_llama_slurm.sh 8 2 128 8192 0 0 # Other parameters, such as TP, FP8 datatype, can be adjusted in the script.