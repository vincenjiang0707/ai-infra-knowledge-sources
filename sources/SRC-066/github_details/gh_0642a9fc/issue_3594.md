# [Issue #3594] [BUG] CuTe DSL 4.8 dev regresses SM80 SDPA backward compilation (NVVM constraint 'n')

source: https://github.com/NVIDIA/cutlass/issues/3594
state: closed | updated: 2026-09-22T06:43:14Z
labels: bug, ? - Needs Triage, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

Describe the bug:
A cuDNN Frontend FROST SDPA backward case that compiles and runs
successfully with nvidia-cutlass-dsl 4.7.0 consistently fails during
NVVM compilation with 4.8.0 dev public wheel. This blocks the cuDNN
Frontend CUTLASS 4.8 SM80 FROST SDPA lane.

Steps to reproduce:
1. Check out NVIDIA/cudnn-frontend at:
   4af0c9f645cf41a3547c638f9eec0c2861ff7aa3
2. Install nvidia-cutlass-dsl[cu13]==4.8.0.dev0 from the 4.8 dev wheel channel.
3. Run:

CUDNN_FRONTEND_ENABLE_FROST_ENGINES=1 \
CUDNN_TEST_NO_ISOLATION=1 \
pytest -q -s \
'test/python/test_mhas_v2.py::test_sdpa_random_bwd_L0[test468]'

Observed error:
NVVM_ERROR_COMPILATION:
constraint 'n' expects an integer constant expression

Expected behavior:
The case should compile and pass as it does with CuTe DSL 4.7.0.

Environment:
- Bare metal NVIDIA A100-PCIE-40GB, sm80
- CUDA 13.4
- Driver 595.58.03
- Python 3.12.3
- PyTorch 2.14.0a0+4fdf77b940.nv26.08
- cuDNN 9.27.0

Impact:
An FE-side workaround would require changing accumulator materialization
in a hot kernel and may increase register pressure. Please address this
compiler regression before CUTLASS 4.8 GA.


## 评论 (1)

### brandon-yujie-sun · 2026-09-22

@YangXu1990uiuc this is fixed in 4.8
