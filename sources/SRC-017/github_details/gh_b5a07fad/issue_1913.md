# [Issue #1913] NCCL 2.28.9 GIN Incompatible with External Network Plugins on Multi-Rail EFA

source: https://github.com/NVIDIA/nccl/issues/1913
state: closed | updated: 2026-08-27T02:37:41Z
labels: 

## 正文

# NCCL 2.28.9 GIN Incompatible with External Network Plugins on Multi-Rail EFA

## Summary

NCCL 2.28.9 with GIN (GPU-Initiated Networking) enabled fails when used with external network plugins, specifically the AWS OFI NCCL plugin (`aws-ofi-nccl`) on multi-rail EFA configurations. The issue manifests as multi-rail configuration mismatches and internal NCCL errors during collective operations.

**Key Finding**: GIN appears to be incompatible with external network plugins that abstract multi-rail network topologies. No GIN-specific log messages appear even when `NCCL_GIN_ENABLE=1` is set, suggesting GIN may silently disable itself when external plugins are detected.

## Environment

**Hardware:**
- Platform: AWS HyperPod (SageMaker)
- Instance Type: ml.p5.48xlarge (2 nodes)
- GPUs: NVIDIA H100 80GB HBM3 (2 GPUs per node, 4 ranks total)
- Network: Elastic Fabric Adapter (EFA) - 32 devices per node (8 used)
- Network Bandwidth: 400 Gbps total (3200 Gbps across all 32 EFA)

**Software:**
- NCCL Version: 2.28.9 (built from source, GitHub tag v2.28.9-1)
- CUDA Version: 12.8
- Driver Version: 555.42.06 (CUDA Runtime 12.4.0)
- AWS OFI NCCL Plugin: GitHub main branch (latest)
- Libfabric: 2.1 (AWS-provided in container)
- Container Base: `public.ecr.aws/hpc-cloud/nccl-tests:latest`
- OS: Ubuntu 22.04 (in container)
- MPI: OpenMPI (AWS-provided)

**GIN Configuration:**
```bash
NCCL_GIN_ENABLE=1
NCCL_GIN_TYPE=2        # Proxy backend
NCCL_GIN_NCONTEXTS=16
NCCL_DEBUG=INFO
NCCL_DEBUG_SUBSYS=INIT,NET,ENV,GIN
```

**EFA Configuration:**
```bash
FI_PROVIDER=efa
FI_EFA_FORK_SAFE=1
FI_EFA_USE_DEVICE_RDMA=1
```

## What Works ✅

### Test 1: NCCL 2.27.7 (Pre-GIN) + AWS OFI Plugin + EFA
- **Status**: Success
- **Performance**: 12.01 GB/s bus bandwidth
- **Network Backend**: NET/Libfabric (EFA)
- **Configuration**: Standard AWS setup with pre-built NCCL 2.27.7
- **Test Command**: `all_reduce_perf -b 8 -e 8G -f 2 -g 1 -c 1 -n 100`

### Test 2: NCCL 2.28.9 + GIN Enabled + TCP Socket (No Plugin)
- **Status**: Success
- **Performance**: ~1.25 GB/s bus bandwidth (TCP limited)
- **Network Backend**: NET/Socket (TCP) - plugin failed to load
- **GIN Status**: Confirmed active via debug logs showing `NCCL_GIN_TYPE=2` detection
- **Key Finding**: GIN works correctly when external plugins are absent

## What Fails ❌

### Test 3: NCCL 2.28.9 + GIN Enabled + AWS OFI Plugin + EFA
- **Status**: Crash during ncclAllReduce initialization
- **Error Type**: Multi-rail configuration mismatch + internal NCCL error
- **Network Backend**: NET/Plugin: Libfabric (v11) - loaded successfully
- **GIN Status**: No GIN-related log messages despite `NCCL_GIN_ENABLE=1` and `NCCL_DEBUG_SUBSYS=GIN`

## Error Messages

### 1. Multi-Rail Configuration Warnings
```
NET/OFI Unexpected number of remote rails for dev 0. Expected 3 but got 2
NET/OFI Unexpected number of remote rails for dev 1. Expected 2 but got 3
NET/OFI Unexpected number of remote rails for dev 2. Expected 1 but got 2
NET/OFI Unexpected number of remote rails for dev 3. Expected 2 but got 1
NET/OFI Unexpected number of remote rails for dev 4. Expected 3 but got 2
NET/OFI Unexpected number of remote rails for dev 5. Expected 2 but got 3
NET/OFI Unexpected number of remote rails for dev 6. Expected 1 but got 2
NET/OFI Unexpected number of remote rails for dev 7. Expected 2 but got 1
```

**Analysis**: Different nodes report inconsistent rail counts for the same device IDs, suggesting a topology discovery or communication protocol mismatch between nodes.

### 2. NCCL Internal Error
```
nccl-gin-efa-test-worker-0:19817:19817 [0] NCCL INFO include/socket.h:403 -> 2
nccl-gin-efa-test-worker-0:19817:19817 [0] NCCL INFO transport/net.cc:476 -> 2
nccl-gin-efa-test-worker-0:19817:19817 [0] NCCL INFO transport/net.cc:1202 -> 2 [Async thread]
Test NCCL failure all_reduce.cu:471 'internal error - please report this issue to the NCCL developers'
Exit code: 3
```

**Context**: This error occurs immediately after the rail mismatch warnings, during the connection establishment phase before any actual data transfer.

### 3. Silent GIN Behavior
Despite setting:
```bash
NCCL_GIN_ENABLE=1
NCCL_DEBUG_SUBSYS=INIT,NET,ENV,GIN
```

**No GIN-specific log messages appear in the output**, such as:
- GIN initialization messages
- GIN context creation
- GIN backend selection confirmation

**Expected behavior**: NCCL should log GIN activation status or warn if GIN cannot be enabled due to plugin incompatibility.

## Additional Diagnostic Test

### Test 4: NCCL 2.28.9 WITHOUT GIN + AWS OFI Plugin + EFA
To isolate whether the problem is GIN-specific, we tested NCCL 2.28.9 with the AWS OFI plugin but with GIN explicitly disabled:

```bash
NCCL_GIN_ENABLE=0  # Explicitly disabled
```

- **Status**: Hang/Deadlock
- **Duration**: 54 minutes before Kubernetes terminated (BackoffLimitExceeded)
- **Behavior**: Workers connected successfully, test launched, but hung during communication
- **Key Finding**: NCCL 2.28.9 has compatibility issues with the AWS OFI plugin even without GIN

This suggests two separate issues:
1. **Primary issue**: NCCL 2.28.9 + AWS OFI plugin incompatibility (affects all configurations)
2. **Secondary issue**: GIN + external plugin incompatibility (observed via rail mismatches)

## Reproduction Steps

### 1. Build NCCL 2.28.9 with GIN Support
```bash
git clone --branch v2.28.9-1 https://github.com/NVIDIA/nccl.git
cd nccl
make -j$(nproc) src.build
```

### 2. Build AWS OFI NCCL Plugin
```bash
git clone https://github.com/aws/aws-ofi-nccl.git
cd aws-ofi-nccl
./autogen.sh
./configure --with-libfabric=/opt/amazon/efa \
            --with-cuda=/usr/local/cuda \
            --with-nccl=/workspace/nccl/build \
            --prefix=/workspace/aws-ofi-nccl/install
make -j$(nproc)
make install
```

### 3. Build NCCL Tests
```bash
git clone https://github.com/NVIDIA/nccl-tests.git
cd nccl-tests
make MPI=1 MPI_HOME=/opt/amazon/openmpi NCCL_HOME=/workspace/nccl/build -j$(nproc)
```

### 4. Set Environment Variables
```bash
export LD_LIBRARY_PATH=/workspace/aws-ofi-nccl/install/lib:/workspace/nccl/build/lib:/opt/amazon/efa/lib:/opt/amazon/openmpi/lib:/usr/local/cuda/lib64:/usr/local/lib
export NCCL_DEBUG=INFO
export NCCL_DEBUG_SUBSYS=INIT,NET,ENV,GIN
export NCCL_GIN_ENABLE=1
export NCCL_GIN_TYPE=2
export NCCL_GIN_NCONTEXTS=16
export FI_PROVIDER=efa
export FI_EFA_FORK_SAFE=1
export FI_EFA_USE_DEVICE_RDMA=1
export NCCL_BUFFSIZE=8388608
export NCCL_P2P_NET_CHUNKSIZE=524288
```

### 5. Run NCCL Test
```bash
mpirun --allow-run-as-root --tag-output \
  -np 4 -N 2 \
  --bind-to none \
  --mca pml ^ucx \
  --mca btl tcp,self \
  --mca btl_tcp_if_exclude lo,docker0,veth_def_agent \
  -x LD_LIBRARY_PATH \
  -x NCCL_DEBUG -x NCCL_DEBUG_SUBSYS \
  -x NCCL_GIN_ENABLE -x NCCL_GIN_TYPE -x NCCL_GIN_NCONTEXTS \
  -x FI_PROVIDER -x FI_EFA_FORK_SAFE -x FI_EFA_USE_DEVICE_RDMA \
  -x NCCL_BUFFSIZE -x NCCL_P2P_NET_CHUNKSIZE \
  /workspace/nccl-tests/build/all_reduce_perf -b 8 -e 8G -f 2 -g 1 -c 1 -n 100
```

## Analysis and Root Cause Hypotheses

### 1. GIN + External Plugin Architecture Incompatibility
**Hypothesis**: GIN may only support built-in NCCL transports (Socket, IB/Verbs, etc.) and not external plugins loaded via `libnccl-net.so`.

**Evidence**:
- GIN works perfectly with TCP Socket transport (no plugin)
- GIN produces no log messages when AWS OFI plugin is loaded
- No documentation exists about GIN compatibility with third-party plugins

**Question for NCCL developers**: Is GIN designed to work with external network plugins, or only with built-in transports?

### 2. Multi-Rail Topology Discovery Mismatch
**Hypothesis**: GIN's Proxy backend (Type 2) may handle network topology discovery differently than standard NCCL, causing inconsistent multi-rail configuration views between nodes.

**Evidence**:
- Rail count mismatches appear immediately (dev 0 expects 3 but gets 2, dev 1 expects 2 but gets 3)
- The pattern shows systematic disagreement, not random errors
- AWS OFI plugin successfully discovers multi-rail topology in NCCL 2.27.7

**Question**: Does GIN Type 2 (Proxy backend) interact with plugin-provided topology information? Should the plugin expose additional interfaces for GIN compatibility?

### 3. Silent GIN Disablement
**Hypothesis**: NCCL may silently disable GIN when it detects an external plugin is loaded, but fails to log a warning.

**Evidence**:
- Zero GIN-related log messages despite `NCCL_DEBUG_SUBSYS=GIN`
- Plugin loads successfully: "NET/Plugin: Loaded net plugin Libfabric (v11)"
- GIN logs appear correctly in TCP Socket test

**Question**: Should NCCL log a warning if GIN cannot activate due to plugin incompatibility? Are there environment variables to force or debug GIN activation attempts?

### 4. GIN Type 2 vs Type 3 Compatibility
**Hypothesis**: Different GIN backends may have different plugin compatibility characteristics.

**Question**: Does GIN Type 3 (GDAKI backend) have different external plugin compatibility compared to Type 2 (Proxy backend)? Are there recommended GIN configurations for EFA environments?

## Questions for NCCL Developers

1. **Is GIN designed to work with external network plugins like aws-ofi-nccl?**
   - If yes: What interfaces must plugins implement for GIN compatibility?
   - If no: Can this be documented clearly in GIN documentation?

2. **Should NCCL log a warning if GIN cannot activate due to plugin incompatibility?**
   - Current behavior: Silent (no GIN logs appear)
   - Expected behavior: Warning message explaining why GIN is disabled

3. **Are there specific NCCL environment variables to force or debug GIN activation?**
   - `NCCL_GIN_ENABLE=1` appears to be ignored silently
   - Need verbose GIN initialization logs

4. **Does GIN Type 3 (GDAKI backend) have different plugin compatibility?**
   - We only tested Type 2 (Proxy backend)
   - Would Type 3 work with external plugins?

5. **What is the source of the "Unexpected number of remote rails" error?**
   - Is this from NCCL core or from the plugin?
   - Where in the NCCL codebase does this check occur? (`transport/net.cc:1202`?)

6. **NCCL 2.28.9 compatibility**: Are there known issues with NCCL 2.28.9 and certain plugin versions?
   - Test 4 showed deadlock even without GIN
   - NCCL 2.27.7 works perfectly with the same plugin

## Desired Outcome

One of the following outcomes would resolve this issue:

**Option A**: GIN can be made compatible with external plugins
- Document required plugin interfaces for GIN support
- Provide guidance for plugin developers

**Option B**: GIN incompatibility with external plugins is by design
- Document this limitation clearly in GIN documentation
- Provide clear error messages when incompatible configurations are detected

**Option C**: Improved diagnostics
- NCCL logs clear warnings when GIN cannot activate
- Provide environment variables for detailed GIN initialization debugging

## Performance Comparison Table

| Configuration | NCCL Version | GIN | Network | Plugin | Status | Bandwidth | Notes |
|---------------|-------------|-----|---------|--------|--------|-----------|-------|
| Baseline | 2.27.7 | No | EFA | AWS OFI | ✅ Success | 12.01 GB/s | Production ready |
| GIN + Socket | 2.28.9 | Yes (Type 2) | TCP | None | ✅ Success | 1.25 GB/s | GIN confirmed working |
| GIN + EFA | 2.28.9 | Yes (Type 2) | EFA | AWS OFI | ❌ Failed | N/A | Rail mismatch error |
| No GIN + EFA | 2.28.9 | No | EFA | AWS OFI | ❌ Hung | N/A | Deadlock after 54 min |

## Additional Context

### Successful Plugin Load (Before Crash)
```
NCCL INFO NET/Plugin: Loaded net plugin Libfabric (v11)
NCCL INFO NET/OFI Selected Provider is efa
NCCL INFO NET/OFI Plugin: v0.0.0
NCCL INFO NET/OFI Min NCCL version supported: 2.12
NCCL INFO NET/OFI Using EFA multi-rail support
NCCL INFO NET/OFI Discovered 5 NIC groups
```

The plugin loads successfully and detects the multi-rail configuration, but subsequently fails during connection establishment.

### EFA Device Information
```bash
# fi_info -p efa
# Shows 32 EFA devices total (8 per node in our test)
# Each EFA device supports RDMA capabilities
```

### GPU Information
```bash
nvidia-smi --query-gpu=name,driver_version,cuda_version --format=csv
# Output: H100 80GB HBM3, Driver 555.42.06, CUDA 12.4
```

## Attached Files

- Full test logs with `NCCL_DEBUG=INFO`: (available upon request)
- Test configurations (Kubernetes YAML): (available upon request)
- Complete build scripts: (available upon request)

## Contact Information

- Platform: AWS HyperPod (SageMaker)
- Test Date: January 2025
- Test Duration: Multiple days of systematic troubleshooting

---

**This issue is also being filed with the AWS OFI NCCL plugin repository** to investigate from both the NCCL and plugin perspectives.


## 评论 (5)

### dmvevents · 2025-11-18

## Solution Found: OFI_NCCL_FORCE_NUM_RAILS

We've successfully resolved the GIN + AWS EFA multi-rail compatibility issue.

**Solution:**
Set the `OFI_NCCL_FORCE_NUM_RAILS` environment variable to force consistent rail count across all EFA devices:

```yaml
env:
  - name: OFI_NCCL_FORCE_NUM_RAILS
    value: "2"  # Force 2 rails per device
  - name: NCCL_GIN_ENABLE
    value: "1"
  - name: NCCL_GIN_TYPE
    value: "2"
```

**Root Cause:**
Multi-rail EFA devices reported inconsistent rail counts (1-3 rails per device), causing topology mismatch when GIN attempted to initialize.

**Results:**
- ✅ Rail mismatch error completely eliminated
- ✅ GIN + EFA tests complete successfully  
- ✅ Performance: ~7.3 GB/s average bandwidth
- ✅ Stable operation confirmed

**Complete testing results and configurations:**
https://github.com/dmvevents/nccl-gin-aws-hyperpod-testing

The `OFI_NCCL_FORCE_NUM_RAILS` variable was added to aws-ofi-nccl in PR #771 specifically for heterogeneous multi-rail configurations.

### xiaofanl-nvidia · 2025-12-06

@dmvevents - 
Today GIN support requires the following (https://github.com/NVIDIA/nccl/releases/tag/v2.28.7-1): 
- CUDA 12.2 or later when compiling the GPU code
- NVIDIA GPUs: Volta or newer. NVIDIA GPU drivers >= 510.40.3
- NVIDIA NICs: CX4 or newer. rdma-core >= 44.0
- Requires nvidia-peermem or DMABUF support. When using DMABUF, linux kernel >= 6.1 is required.

We are actively working on EFA support for GIN. And we will review other findings above to ensure we handle unsupported cases better. 

### dmvevents · 2026-04-28

Thanks @xiaofanl-nvidia for the clear response on GIN requirements and the note that EFA support is being actively worked on.

That's exactly what we needed to know. We'll track the GIN + EFA work on our side and re-test once support is available. In the meantime, the `OFI_NCCL_FORCE_NUM_RAILS` workaround on the aws-ofi-nccl side keeps things stable for non-GIN configurations.

A couple of questions:

1. Is there a target NCCL release version for GIN + EFA support, or is it too early to say?
2. When GIN + EFA lands, will it require changes on the aws-ofi-nccl plugin side as well, or will it be transparent?

Happy to help test pre-release builds when you're ready. We have multi-node P5 (H100) environments with 32 EFA devices per node readily available.


### huangzhilin-hzl · 2026-06-04

```bash
> [@dmvevents](https://github.com/dmvevents) - Today GIN support requires the following (https://github.com/NVIDIA/nccl/releases/tag/v2.28.7-1):今天 GIN 支持要求如下（ https://github.com/NVIDIA/nccl/releases/tag/v2.28.7-1）：
> 
> * CUDA 12.2 or later when compiling the GPU code编译 GPU 代码时需使用 CUDA 12.2 或更高版本
> * NVIDIA GPUs: Volta or newer. NVIDIA GPU drivers >= 510.40.3NVIDIA GPU：Volta 或更新型号。NVIDIA GPU 驱动程序 >= 510.40.3
> * NVIDIA NICs: CX4 or newer. rdma-core >= 44.0NVIDIA 网卡：CX4 或更新型号。rdma-core >= 44.0
> * Requires nvidia-peermem or DMABUF support. When using DMABUF, linux kernel >= 6.1 is required.需要 nvidia-peermem 或 DMABUF 支持。使用 DMABUF 时，需 Linux 内核 >= 6.1。
> 
> We are actively working on EFA support for GIN. And we will review other findings above to ensure we handle unsupported cases better.我们正在积极为 GIN 开发 EFA 支持。我们也会审查上述其他发现，以确保更好地处理不受支持的情况。
```

Hi @xiaofanl-nvidia, thanks for the clarification.

Could you confirm whether GIN is expected to support the legacy `nv_peer_mem` module? From the source, GIN seems to require `nvidia_peermem` or DMA-BUF, and does not treat `/sys/module/nv_peer_mem` as supported. Is that expected?

### dmvevents · 2026-08-27

Update from the issue author: this is no longer blocking us on current
stacks, so I am closing it from my side. For clarity, here is what we
now run and what remains untested.

What changed since the report (which was against NCCL 2.28.9):

- In our build/test setup, NCCL 2.30.4's GIN v2 path works with an
  external network plugin: aws-ofi-nccl at commit 6e504db3 ("gin: Size
  active_put_signal to full sequence number space", 2026-04), which
  implements the `ncclGinPlugin` interface. That commit is the exact
  revision we test, not just an example.

Working configuration: AWS p5en.48xlarge (H200, 16 EFA NICs/node),
NCCL 2.30.4 + aws-ofi-nccl@6e504db3, `NCCL_GIN_TYPE=2` (CPU-proxy GIN):

- GIN initializes cleanly on all ranks (`NET/OFI gin: Initializing`,
  `Selected provider is efa, fabric is efa-direct`), no topology
  validation failure.
- Sustained MoE all-to-all over GIN/EFA: DeepEP V2 (ElasticBuffer)
  dispatch/combine at EP16 across 2 nodes, e.g. dispatch p50 ~321us /
  combine p50 ~308us at 384 experts (hidden 7168, top-8), and the same
  substrate passed our vLLM / SGLang / TensorRT-LLM load tests.
- One requirement specific to this plugin's GIN path on EFA: its GIN
  init probes GDRCopy and requires the host gdrdrv kernel module at
  version >= 2.5 (gdrdrv 2.5 ships with the released GDRCopy 2.5.x —
  install/upgrade gdrcopy on the host to get it).

Caveat on the original bug: I have not tested NCCL 2.30.4 + current
aws-ofi-nccl on the configuration this issue was filed from
(p5.48xlarge H100, 32 EFA NICs/node). The p5en setup above has half the
NICs per node, so the absence of the rail-count mismatch there may be
due to the simpler topology as much as to newer NCCL — I cannot claim
the underlying multi-rail validation issue is fixed for 32-NIC hosts.
Closing because it no longer blocks us; if the team wants to keep
tracking the 32-NIC configuration, let me know and I will reopen.

Thanks @xiaofanl-nvidia for the earlier guidance, and the offer stands:
happy to test pre-release GIN/EFA builds on multi-node P5/P5en.
