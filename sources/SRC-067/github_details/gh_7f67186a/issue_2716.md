# [Issue #2716] Unexpected E4M3 accuracy deficit in FA4 SM100 FP8 forward relative to E5M2 and CPU quantization emulation

source: https://github.com/Dao-AILab/flash-attention/issues/2716
state: closed | updated: 2026-07-19T23:16:13Z
labels: 

## 正文

### Summary

Using `flash-attn-4` CuTe `_flash_attn_fwd` with explicit `q_descale`, `k_descale`, and `v_descale` on one NVIDIA B200, E4M3 produces consistently higher error than E5M2 for the tested GQA geometry.

A standalone NumPy emulation of the quantization pipeline predicts the opposite ordering: under the same scaling, E4M3 should have roughly half the quantization error of E5M2. The emulated E5M2 result matches the GPU result within 0.1–1.3% across all five tested configurations, while the emulated E4M3 result is 54.9–68.5% below the GPU error. This isolates an unexplained E4M3-specific excess error, but does not establish the failing instruction or transformation.

### Environment

- `flash-attn-4 == 4.0.0b22`
- `nvidia-cutlass-dsl == 4.6.0.dev0`
- `torch == 2.13.0+cu130`
- GPU: 1× NVIDIA B200 (SM100)
- Driver: `580.95.05`
- CUDA: `13.0`
- Entry point: `flash_attn.cute.interface._flash_attn_fwd`
- Input formats: `torch.float8_e4m3fn` and `torch.float8_e5m2`
- Explicit `q_descale`, `k_descale`, `v_descale`, shape `(batch, num_kv_heads)`, `float32`
- Geometry: `batch=2`, `num_heads=32`, `num_kv_heads=2`, `head_dim=128` (GQA 16:1)
- Seed: `0`

### GPU observations

All values below are `rel_l2` against an FP32 `softmax(QKᵀ/√d)·V` reference.

| seq_len | softmax | E4M3 | E5M2 | E4M3/E5M2 |
|---:|---|---:|---:|---:|
| 256 | uniform | 0.114825 | 0.101554 | 1.131 |
| 1024 | uniform | 0.163994 | 0.104824 | 1.564 |
| 4096 | uniform | 0.170582 | 0.106446 | 1.603 |
| 1024 | peaked (`q×8`) | 0.318663 | 0.235719 | 1.352 |
| 4096 | peaked (`q×8`) | 0.336852 | 0.250965 | 1.342 |

BF16 calibration for the same path was approximately `rel_l2=0.0023`, and the private `_flash_attn_fwd` BF16 result matched the public BF16 path exactly in the calibration case.

### CPU quantization emulation

The standalone NumPy model implements:

- IEEE round-to-nearest-even;
- E4M3FN / E5M2 subnormals and saturation;
- the same per-`(batch, kv_head)` amax scaling used by the GPU probe;
- the kernel's `max_offset=8` P scaling (`P` represented as `P×256` before FP8 conversion);
- GQA repeat and FP32 attention reference;
- A/B/C/D decomposition for P-only, V-only, P×V, and full Q/K/V→P×V quantization.

Full-pipeline emulation (`D`) versus GPU:

| config | emu E4M3 | GPU E4M3 | emu E5M2 | GPU E5M2 |
|---|---:|---:|---:|---:|
| s256 uniform | 0.051764 | 0.114825 | 0.102826 | 0.101554 |
| s1024 uniform | 0.052783 | 0.163994 | 0.104771 | 0.104824 |
| s4096 uniform | 0.053658 | 0.170582 | 0.106352 | 0.106446 |
| s1024 peaked | 0.119297 | 0.318663 | 0.235007 | 0.235719 |
| s4096 peaked | 0.126008 | 0.336852 | 0.252964 | 0.250965 |

The E5M2 GPU values closely track the quantization-only model. E4M3 shows a substantial additional error that the same arithmetic model does not reproduce.

### Interpretation

The E5M2 agreement makes shared operand preparation and accumulation explanations less likely. The evidence narrows suspicion toward an E4M3-specific stage, including the P-matrix conversion in `apply_exp2_convert`, but it does **not** establish the failing instruction or transformation.

### Questions

1. Is E4M3 a supported and numerically validated input/P format for the current SM100 FA4 forward path, or is E5M2 the intended FP8 mode?
2. Is this E4M3-specific excess error known or expected for `4.0.0b22`?
3. Has the P-cast/scaling path changed in a newer build that we should test?
4. Is there a recommended additional scaling or offset for E4M3 P conversion on SM100?

### Reproducer structure

We have three self-contained scripts and immutable JSON outputs:

- Run 13: direct `_flash_attn_fwd` BF16 calibration plus E4M3/E5M2 comparison;
- Run 14: sequence-length and softmax-shape sweep;
- Run 15: CPU-only NumPy quantization emulation with preregistered A/B/C/D checks.

Each GPU script checks for B200/SM100, records package versions and the exact callable signature, uses fixed seed/geometry, and refuses to overwrite its result JSON. The CPU script includes 12 FP8 format self-tests before running the emulation. I can post the complete scripts and raw JSON in follow-up comments if that is preferable to a large issue body.

### Artifact hashes

```text
a6ceee96f3be76242a890a7d2e68c787b854550b39f6f3d2774b980b37bd8fab  probe_fa4_b200_run13.py
8ff53695eaa5e9ef9057904056806c024e91afc0e008c9bdb319633b59942279  probe_result_run13.json
ee767c7cd79cec0bf51733498e223bd211f3b59b4a4b0ab09b0306b2f8a8b61b  probe_fa4_b200_run14.py
0add838a52ec7a3217feb5e4f13c7dba661fb225ef21fad5f63ea04bec8e5511  probe_result_run14.json
a24e6178dabb9604d29c7af1825c421594bfca38a1d6bc4c839f2e266b273024  probe_fp8_pcast_local_run15.py
9dacfaf9b13633269857f6ebc0b4d285e0915da6c7316c2a8022bbe4175cab18  probe_result_run15.json
```

## 评论 (6)

### Johnsonms · 2026-07-18

Will take a look at it

### yunweili3 · 2026-07-19

# Response
@GoblinFlash Could you please verify my fix?

> Is E4M3 a supported and numerically validated input/P format for the current SM100 FA4 forward path, or is E5M2 the intended FP8 mode?

Neither was validated — both were treated identically by accident, not by design. In flash_attn/cute/flash_fwd_sm100.py (pre-fix), the P-scaling constant was gated only on bit-width, not dtype:

max_offset = 8 if cutlass.const_expr(self.q_dtype.width == 8) else 0

e4m3 and e5m2 are both 8-bit, so they silently shared one constant tuned (via rescale_threshold=4, added later in commit cbbab83/related tuning work) without re-checking it against e4m3's much lower saturation ceiling (448 vs. e5m2's 57344). Stronger evidence: in tests/cute/test_flash_attn.py:99-100, the fp8 dtype is commented out of the default test parametrize —

@pytest.mark.parametrize("dtype", [torch.float16, torch.bfloat16, torch.float8_e4m3fn])
@pytest.mark.parametrize("dtype", [torch.bfloat16])

— meaning e4m3 has never run in this suite's normal sweep. I ran it anyway on main with the issue's own geometry and got the same ~1.13–1.60× excess error the reporter saw. So: e4m3 was accepted by the API but not numerically validated; e5m2 wasn't specially "intended" either, it just happened not to saturate.

> Is this E4M3-specific excess error known or expected for 4.0.0b22?

No — it was an unrecognized bug until this report. Evidence: #2716 is the only issue on it, with a single collaborator comment ("Will take a look at it," no acknowledgment of a known limitation). No CHANGELOG/release-notes entry, no related closed issue, and the constant in question hadn't been touched with fp8-format-awareness in git history (git log on flash_fwd_sm100.py shows tuning commits like cbbab83 "Tune FP8 causal hd128 ex2_emu_freq," but nothing addressing e4m3-specific saturation). It's also worth noting flash-attn-4's version (4.0.0b22) is a setuptools-scm-derived string, not a published PyPI release (pip index versions flash-attn-4 → "No matching distribution found") — so this was almost certainly a from-source/nightly build, not a version anyone had separately validated against.

> Has the P-cast/scaling path changed in a newer build that we should test?

No. origin/main is currently at the same commit the PR is based on (77aacb6) — git log 77aacb6..origin/main -- flash_attn/cute/flash_fwd_sm100.py retur to that file since. The only change tothis path anywhere is PR #2717 itself, which is still open, unmerged, 0 reviews (gh pr view 2717 --json
state,mergeable,mergedAt,reviews → "statviews":[]). So there is no newer build totest — #2717 (unmerged) is the fix to test.

> Is there a recommended additional scaling or offset for E4M3 P conversion on SM100?

Yes, and it's derived, not guessed: keep rescale_threshold=4 (the perf-optimization that lets the row-mstale) and require max_offset + rescale_ dtype. That gives max_offset=4 for e4m3fn (worst case 2^(4+4)=256 ≤ 448) vs. the existing 8 for e5m2 (2^12=4096 ≤ 57344). I verified this isn't jtheoretical — I reproduced the bug on macal script on the PR branch: e4m3 errorflipped from ~1.3–1.6× worse than e5m2 to a consistent ~0.50–0.51× of e5m2 (i.e., ~2× better, matching quantization theory), and 12 real cases h_attn_output suite passed againstreference on the PR branch. Diff is in flash_attn/cute/flash_fwd_sm100.py, both the softmax warp (max_offset) and correction warp (max_offset/max_offsonsistent per your earlier PR review.



### GoblinFlash · 2026-07-19

## Correction and full independent verification of PR #2717

This comment replaces an earlier verification note that incorrectly characterized the CuTeDSL failure as shape-dependent. Further isolation work (Runs 20–21) showed that conclusion was wrong.

### 1. Correction: the compile failure is process-context-dependent, not shape-dependent

Using the byte-exact PR-head kernel (`20177d738cf1285dcedc84523bbf504008a58405`, kernel SHA-256 `857fc862f421b1b285b52ca5491e7c8412c58ff2db2f289594995ca7fd5e2843`):

- calling the kernel inside our long-lived serverless orchestrator process consistently produced `DSLRuntimeError: Unable to convert dynamic Boolean value to bool at compile time`;
- calling the identical installed file from a freshly spawned `python` subprocess compiled and ran successfully;
- this reproduced across BF16, E4M3, and E5M2 entry paths;
- the base revision `77aacb68d194ba9af1010eda5eac3e7c0df8e6f6` did not fail in either context.

The same in-process failure also occurred with two semantically equivalent respellings of the new selection logic, so the nested conditional-expression form is not established as the trigger. The exact CuTeDSL root cause remains unproven.

Therefore, I withdraw the earlier claim that PR #2717 introduces a mainstream-shape compilation regression. The failure is real in our rich host-process context, but it is not demonstrated to be a numerical-kernel or shape regression caused by the PR. This may still matter for serving stacks that compile from long-lived worker processes, so it appears worth root-causing separately.

### 2. Exact PR-head numerical verification on B200

The byte-exact PR head was run successfully from a clean subprocess on:

- NVIDIA B200 / SM100
- driver `580.95.05`
- CUDA 13.0
- PyTorch `2.13.0+cu130`
- `flash-attn-4==4.0.0b22`
- `nvidia-cutlass-dsl==4.6.0.dev0`

Test geometry family:

- `batch=2`
- `num_heads=32`
- `num_kv_heads=2`
- `head_dim=128`
- non-causal
- fixed seed
- per-`(batch, kv_head)` descales through `_flash_attn_fwd`
- rel-L2 against an FP32 reference

| config `(seq_len, alpha)` | base E4M3 | **PR E4M3** | E5M2 (unchanged) | PR E4M3/E5M2 | PR / CPU prediction |
|---|---:|---:|---:|---:|---:|
| `(256, 1)` | 0.114825 | **0.051621** | 0.101554 | 0.508 | 0.997 |
| `(1024, 1)` | 0.163994 | **0.053000** | 0.104824 | 0.506 | 1.004 |
| `(4096, 1)` | 0.170582 | **0.053306** | 0.106446 | 0.501 | 0.993 |
| `(1024, 8)` | 0.318663 | **0.120804** | 0.235719 | 0.512 | 1.013 |
| `(4096, 8)` | 0.336923 | **0.128270** | 0.251026 | 0.511 | 1.002 |

Results:

- E4M3 lands within approximately **-0.7% to +1.3%** of the quantization-only CPU emulation from #2716 in all five cases.
- E4M3/E5M2 is **0.501–0.512**, matching the expected approximately 0.50–0.51 ratio.
- E5M2 and BF16 are unchanged versus base to the reported precision in every tested configuration.
- In the direct-cast/no-descale harness, E4M3/E5M2 is **0.502–0.505**; in the peaked case E4M3 error drops from about `0.301` to `0.013` (approximately 23x improvement).

### Conclusion

For the independently tested B200/SM100 geometry family, the dtype-aware `max_offset=4` change does exactly what the PR claims: it removes the E4M3-specific saturation excess and restores the expected E4M3 advantage over E5M2 without changing BF16 or E5M2 results.

This confirms the numerical fix for the tested scope. It is not a claim of universal correctness across every SM100 configuration.

The remaining separate concern is the process-context-dependent CuTeDSL compilation failure observed only inside a long-lived rich host process; the same byte-exact PR head compiles and runs correctly in a fresh subprocess.

Result artifact SHA-256:

- Run 20: `add5567d9aca5ccc9f78e0bae6695ef25bc116fb984578d85e84f7676e0a381d`
- Run 21: `46ec3dfb231fdfa80cf00bd57a0bc6507323d38707e56d45d241873409147c41`

Full scripts and JSON results are available on request.

### yunweili3 · 2026-07-19

@GoblinFlash 

After checking in with the CUTLASS repo, it is clear that this issue isn't related on the side of FlashAttention in any way, but instead to CUTLASS, so there is no immediate issue that can be attributed to FlashAttention here. 

### GoblinFlash · 2026-07-19

Thanks — this explains the process-context behavior we observed and cleanly separates it from the numerical fix in #2717.

Subscribed to NVIDIA/cutlass#3395 and #3396. From our side, the numerical verification of #2717 remains valid for the tested B200 geometry family.

Great work, guys — really appreciate the quick root-cause analysis and upstream handoff.

### Johnsonms · 2026-07-19

Thanks @GoblinFlash and @yunweili3 
