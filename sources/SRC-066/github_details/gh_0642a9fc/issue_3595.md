# [Issue #3595] [BUG] CuTe DSL 4.8 dev SIGABRTs in TVM-FFI launch for SM100 ragged SDPA (4.7 passes)

source: https://github.com/NVIDIA/cutlass/issues/3595
state: closed | updated: 2026-09-22T06:43:39Z
labels: bug, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**

On SM100, the latest CuTe DSL 4.8 development wheel aborts the Python
process while launching a ragged/THD SDPA kernel through TVM-FFI.

The failure reproduces in isolation in about 8 seconds with:

- `nvidia-cutlass-dsl==4.8.0a0+20260907123000.a76982f`
- NVIDIA/cudnn-frontend at `4af0c9f645cf41a3547c638f9eec0c2861ff7aa3`
- `apache-tvm-ffi==0.1.13.post3`

The process reports:

```text
CUDA Dialect Assertion failed on CUDA error:
cudaErrorInvalidValue - invalid argument

Fatal Python error: Aborted

  File "<string>", line 3 in wrapper
  File ".../cutlass_dsl/tvm_ffi_provider.py", line 1084 in __call__
  File ".../cudnn/sdpa/fwd/api_dsl.py", line 1942 in _execute_thd
  ...
  File ".../test_mhas_v2.py", line 507 in test_sdpa_random_bwd_ragged_L0
```

This is a native abort rather than a Python exception.

**Steps to reproduce**

1. Check out cudnn-frontend:

```bash
git clone https://github.com/NVIDIA/cudnn-frontend.git
cd cudnn-frontend
git checkout 4af0c9f645cf41a3547c638f9eec0c2861ff7aa3
```

2. Install the latest 4.8 development wheel and TVM-FFI:

```bash
pip install \
  "nvidia-cutlass-dsl[cu13]==4.8.0a0+20260907123000.a76982f" \
  --extra-index-url \
  https://urm.nvidia.com/artifactory/api/pypi/nv-shared-pypi-local/simple/

pip install "apache-tvm-ffi==0.1.13.post3"
```

3. Build/install cudnn-frontend in the usual way, then run:

```bash
CUDNN_FRONTEND_ENABLE_FROST_ENGINES=1 \
pytest -vv -s \
  'test/python/test_mhas_v2.py::test_sdpa_random_bwd_ragged_L0[test370]'
```

The deterministic test configuration is:

```text
dtype:        fp16
B:            16
H:            5
S_q:          7333
S_kv:         8048
D_qk:         192
D_v:          128
alignment:    bottom-right
right_bound:  0
layout:       ragged
stats layout: head_major

seq_q:
[5252, 4398, 3528, 2933, 0, 1446, 0, 836,
 5526, 1774, 3493, 3848, 6549, 3619, 2920, 5128]

seq_kv:
[6695, 2088, 556, 7866, 5601, 2414, 6438, 5467,
 3232, 381, 6855, 1976, 2164, 6981, 1580, 1277]
```

**Expected behavior**

The kernel should launch and produce a result, or at minimum report a
recoverable Python/DSL error. The process must not abort.

The same cudnn-frontend suites complete without this abort with CuTe DSL
4.7.0.

**Regression evidence**

At identical cudnn-frontend SHAs, the 4.8 lane repeatedly aborts inside the
same call path while the 4.7.0 lane completes:

- FE `32d955d9c1057496a3284dcc9584cd48136589a4`
  - 4.8 build `20260905123000.6083892`: three SIGABRTs, eventual timeout
  - 4.7.0: completed with no worker abort
- FE `58fc746a1cfdf528d50584412ce4d1966849629f`
  - 4.8 build `20260906123000.6083892`: three SIGABRTs, eventual timeout
  - 4.7.0: completed with no worker abort

The comparison also crossed two SM100 runners and driver versions: whichever
runner used 4.8 failed, while the 4.7 job completed.

The longer history shows this is a recurring 4.8-only regression:

- Known-good 4.8 builds through `20260823210556.ac70faa`
- Identical aborts from `20260825210638.952ea40` through
  `20260831123001.b066920`
- Temporarily green with `20260901123001.7b963f4` and
  `20260902123001.54ab983`
- Regressed again with `6083892`
- Still present in the latest RC build `a76982f`

The Python `tvm_ffi_provider.py` file is identical between the temporarily
good `54ab983` build and the failing `6083892`/`a76982f` builds, so the abort
appears to originate below that Python wrapper or in generated launch code.

**Environment**

- GPU: B200, compute capability 10.0
- Driver: 595.71.05
- CUDA: 13.2
- Python: 3.12.3
- PyTorch: 2.12.0a0+5aff3928d8.nv26.05
- cuDNN backend: 9.30.0
- cuDNN Frontend: 1.29.0
- Apache TVM-FFI: 0.1.13.post3
- CuTe DSL: 4.8.0a0+20260907123000.a76982f

The nightly CI reproductions also occurred with CUDA 13.4, cuDNN 9.27,
PyTorch 2.14 nightly, and TVM-FFI 0.1.13.post3.

This is separate from the SM80 NVVM compilation regression tracked in #3594.
Both currently block validation of CuTe DSL 4.8 before GA.


## 评论 (1)

### brandon-yujie-sun · 2026-09-22

@YangXu1990uiuc this is fixed in 4.8
