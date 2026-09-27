# [Issue #4061] [MP][Platform][Ascend] LMCache MP Mode support Ascend NPU

source: https://github.com/LMCache/LMCache/issues/4061
state: open | updated: 2026-09-20T06:45:07Z
labels: 

## 正文

[MP][Ascend] LMCache MP Mode support Ascend NPU

**Is your feature request related to a problem? Please describe.**
Currently, LMCache supports Ascend NPU in in-process mode, but MP (Multiprocess) mode — the recommended production deployment architecture where LMCache runs as a standalone service decoupled from the inference engine — does not yet support Ascend NPU. 

This creates a significant gap for users who want to deploy LMCache on Ascend-based hardware in production environments. The MP architecture was officially released in April 2026, and without Ascend support, users on Ascend platforms cannot leverage the robustness and scalability benefits that MP mode provides.

The key blockers include:
- Ascend-specific KV cache format variants are not fully handled in MP mode's serialization/deserialization paths
- Python-side memory management primitives like pinned memory are not verified for MP mode multi-process scenarios
- Custom Ascend kernels required for MP mode cross-process KV transfer are not yet available


**Describe the solution you'd like**
We propose a three-phase implementation plan to fully support Ascend NPU in LMCache MP mode:

**Phase 1: Ascend NPU KV Cache Format Support (Operator Repository Separated)**

- Extend `KVCacheFormat` enumeration to ensure MP mode format detection is consistent with C++ `types.h` definitions (enum values must match exactly)
- Adapt MP mode serialization/deserialization to support Ascend-specific format variants
- Keep Ascend kernel implementations in a separate repository (`LMCache-Ascend/csrc/`) during development to maintain main repository interface stability
- Validate that KV cache can be correctly serialized and deserialized across processes in MP mode

**Phase 2: Python-side Support — Pinned Memory and Memory Management**

- Extend the existing `HostRegisteredMemoryManager` singleton to ensure compatibility with MP mode multi-process scenarios (handling access to the same pinned memory region across different processes)
- Adapt `AscendMixedMemoryAllocator` to support pinned memory allocation/deallocation in MP mode
- Verify zero-copy or efficient data transfer paths between Ascend NPU and host CPU work correctly when Cache Server and inference engine run in separate processes
- Ensure proper thread-safety and process-safety for shared memory regions

**Phase 3: Operator Integration and Full Validation**

- Merge the newly developed Ascend operators from the separate repository into the main LMCache repository's `csrc/` directory
- Update C++ and Python bindings to expose Ascend-specific operators for MP mode
- Full end-to-end validation across the MP stack: KV cache storage → retrieval → NPU restoration → inference engine consumption
- Add comprehensive unit tests and integration tests for Ascend MP mode in CI/CD (or provide a test plan for hardware-available environments)
- Update documentation with Ascend MP mode deployment instructions and known limitations

**Timeline**:
- Phase 1: ~2 weeks
- Phase 2: ~2 weeks  
- Phase 3: ~1 week

**Describe alternatives you've considered**
1. **Single-process mode only**: Users could continue using single-process mode with Ascend, but this loses the key benefits of MP mode (decoupling, robustness, scalability) and is not recommended for production.

2. **Manual KV transfer via host memory**: Instead of supporting Ascend natively in MP mode, we could copy KV cache to host CPU memory and rely on host-side processing. However, this adds significant overhead and defeats the purpose of efficient NPU utilization.

3. **Postpone Ascend MP support**: We could wait for a more unified cross-hardware abstraction layer, but given that LMCache-Ascend already has basic support and vLLM Ascend integration is maturing, immediate support is more practical for users.

**Additional context**
- **Current LMCache-Ascend status**: Basic support for vLLM v0.11.x+ with `SEPARATE_KV` format is already functional for 910B/310P chips in single-process mode. The `LMCache-Ascend` repository has kernel implementations in `csrc/` and Python memory management utilities.
- **vLLM-Ascend**: Huawei's vLLM fork supports Ascend NPU with KV cache format as documented in their configuration guidelines.
- **Target platforms**: Ascend 910B, 910C.
- **Dependencies**: vLLM v0.20.x+, PyTorch with Ascend extensions, CANN (Huawei Compute Architecture for Neural Networks) toolkit.

We are willing to contribute the implementation following this plan and coordinate with maintainers on code review and integration timelines. Please let us know if any adjustments to the approach are desired.

## Tasks

- [ ] **1. KV format support** (Phase 1)
  - [x] **GQA (non-MLA)** — per-layer `(K, V)` paged tuples (`NL_X_TWO_X_NB_BS_NH_HS`); merge in #3968 
  - [x] **MLA / DSA** — per-layer plane tuples with unequal plane widths (`NL_X_NP_X_NB_BS_ONE_HS`): MLA `(latent, rope)`, DSA `(latent, rope, dsa)`, plus the DSA indexer k-cache; core is in #5138.
- [x] **2. Engine-driven transfer on NPU** (Phase 2) — run the Ascend NPU connectors inside the MP worker runtime so the vLLM-Ascend process itself drives KV store/load against the MP cache server; merged in #4763 
- [ ] **3. LMCache-driven transfer on NPU** (Phase 2) — let the MP cache server drive transfers into engine-registered NPU buffers: NPU device context, pinned host memory shared across processes, and the host fallback path;
- [ ] **4. csrc / kernel integration** (Phase 3) — move the MP block-transfer kernels from LMCache-Ascend `new_kernels/` into main-repo `csrc/` with CMake/pybind wiring guarded by `BUILD_WITH_ASCEND`, keeping other platforms' builds unaffected.
- [ ] **5. CI** (Phase 3) — port the self-hosted 910B3 MP workflow into main-repo CI with unit + e2e coverage, plus Ascend MP deployment docs. 


## 评论 (1)

### github-actions[bot] · 2026-09-08

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
