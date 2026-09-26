# [Issue #299] Failure when testing on 2-nodes

source: https://github.com/NVIDIA/nccl-tests/issues/299
state: open | updated: 2025-04-01T17:42:40Z
labels: invalid, question

## 正文

Hi!

I am currently testing 2 H100 nodes (each node has 8 gpus).
But following error occurs and maybe related to ssh connection.
Is it possible to change port or something other things to try instead of this ?
- For single node, nccl-test works fine.

```
root@yj-videogen-multinode-job-master-0:/workspace/nccl-tests# mpirun --allow-run-as-root -x NCCL_SHM_DISABLED=1 -x NCCL_DEBUG=INFO -np 16 -N 8 -H hostfile ./build/all_
reduce_perf -b 8 -e 1G -f 2
ssh: connect to host (worker_ip) port 22: Connection refused
--------------------------------------------------------------------------
PRTE has lost communication with a remote daemon.

  HNP daemon   : [prterun-yj-videogen-multinode-job-master-0-34@0,0] on node yj-videogen-multinode-job-master-0
  Remote daemon: [prterun-yj-videogen-multinode-job-master-0-34@0,1] on node (worker_ip)

This is usually due to either a failure of the TCP network
connection to the node, or possibly an internal failure of
the daemon itself. We cannot recover from this failure, and
therefore will terminate the job.
--------------------------------------------------------------------------
```

## 评论 (2)

### kiskra-nvidia · 2025-04-01

Your MPI installation does not work correctly in a multi-node setting. You need to fix that first before you try running NCCL tests. I'm guessing you'll see the same issue with an MPI "hello world"-type problem, or even something as simple as:

```
mpirun --allow-run-as-root -x NCCL_SHM_DISABLED=1 -x NCCL_DEBUG=INFO -np 16 -N 8 -H hostname
```

### AddyLaddy · 2025-04-01

My favorite "canary" test of an MPI installation is to download and compile a simple MPI program:

```
wget https://raw.githubusercontent.com/pmodels/mpich/main/examples/cpi.c
mpicc -o cpi cpi.c
```

This does more than just a "Hello World!" printf and demonstrates that basic MPI Collectives calls are functional across the job
