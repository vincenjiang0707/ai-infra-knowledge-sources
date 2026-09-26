# [Issue #2987] Artifact downloading future improvement suggestions

source: https://github.com/flashinfer-ai/flashinfer/issues/2987
state: open | updated: 2026-09-19T17:50:37Z
labels: priority: should have (P1)

## 正文

Context:

#2903 fixed artifact runner header placements so they get picked up correctly by flashinfer-cubin packaging. this is critical for running in air-gapped environments. However before this change, it would flag cached artifact inconsistency upon branch switching as an error, the new approach initially does not, then adopted ensure_symlink() was added at module gen() function to ensure it is always consistent, addressing the issue flagged during the review. Looking back, it was too risky of a change to do in the hot fix, and i should have deferred that review comment. The existing race condition tests did not catch the specific error.

#2979 fixes a race condition introduced by #2903 from ensure_symlink by adding filelock

Future clean-up action items:

 1. Eliminate symlinks: Pass versioned artifact path directly as -I nvcc flag, use relative #include paths in .cu
  files. The -I flag naturally becomes part of the JIT cache key via extra_cuda_cflags, so version changes trigger
  recompilation automatically. Removes symlinks, race conditions, lock file debris, and stale cache issues in one
  change.
  2. Sentinel-based download coordination with optional locking: Add lock=True parameter to download_file and
  ensure_symlink so they remain safe by default for external/direct callers. Inside the sentinel pattern, one outer
  lock coordinates all workers — the inner functions are called with lock=False since the outer lock already provides
  exclusion. This avoids redundant per-file lock acquisition while keeping the public API foolproof. The sentinel
  approach is used in build_and_load() as well and it is a cleaner paradigm.
  3. Clean up .lock files from packaging: Exclude *.lock via pyproject.toml exclude-package-data, or rely on fix (2)
  producing fewer lock files during the packaging build.

Wider context: This chain of issues started from a planned artifacts re-org to pull in runner headers for them to be updated consistently wrt the cubins. This is critical for the correct execution of the cubins. This part of the code in general, is more prone to critical failures, lying at the intersection of varied packaging and parallel execution environment, thus it needs to be treated with more diligence in the future. Specifically TP sanity test with the flashinfer-cubin package shall be tested without networking in nightly testing to catch similar issues in the future. this is a progress underway.

## 评论 (2)

### 0z5a · 2026-09-19

Hi @aleozlx , I’d like to take cleanup item (1) here: eliminate the artifact-header symlinks and pass the versioned artifact include path directly through the JIT/NVCC include flags.

### 0z5a · 2026-09-19

Cleanup item (1) from this issue is implemented and tested in #5343 (base `dc04f50c9aa3eabcdaa5feb0934edb3d85e9529a`).

What it does: each trtllm-gen export link now lives under a versioned root `GEN_SRC_DIR/trtllm_export/<module>/<artifact sha256>`, that root is the first `-I`, and the same artifact hash is folded into the JIT build directory, so two artifact versions can no longer shadow each other and the architecture-filtered `flashinferMetaInfo.h` still wins over a same-named header in the raw artifact. The version tag is the artifact's existing content hash — no second global version state. `ensure_symlink` / `verify_symlinked_headers` are reused unchanged, so removing the convention path removes no integrity check, and the artifact's raw `include/` stays off the include path. Space-containing include dirs are now quoted; space-free ones emit byte-identical flags.

Measured on an L20 (SM89, torch 2.13, CUDA 12.8) — all CPU/JIT path resolution, no GPU kernel involved:

```
python -m pytest tests/jit/test_trtllm_gen_artifact_include.py \
                 tests/jit/test_trtllm_gen_metainfo.py \
                 tests/jit/test_jit_cpp_ext.py tests/test_artifacts.py -q
# 66 passed
```

Covered: same-version identity stability, different-version build identity, generate(A)+generate(B) then compile with no last-writer-wins, filtered-vs-raw same-named header resolution, concurrent same-version and concurrent different-version workers sharing a cache, a worker killed just before the atomic rename, missing/checksum-error artifacts failing loudly, spaces in paths, read-only install dir plus writable cache, and a preset artifact with the network blocked.

Not covered here: item (2) downloader coordination and item (3) sentinel scheduling are untouched, and the SM90/SM100 modules were not executed on their real runners (no such device available) — the generation and filtering logic is covered on CPU, the kernels are unchanged.

