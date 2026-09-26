# [Issue #5418] [Issue]: DeepSeek R1 MXFP4 core dumps due to compiler hazard after #5061 (0200ada1a)

source: https://github.com/ROCm/aiter/issues/5418
state: closed | updated: 2026-09-24T17:05:37Z
labels: bug, Triton/Gluon

## 正文

### Problem Description

gemm_afp4wfp4 tuned config added in #5061 (0200ada1a) triggers GPU memory fault in DeepSeek-R1 MXFP4 (compiler hazard in global_load_async_to_lds path)

### Operating System

Ubuntu 24.04.3 LTS

### CPU

AMD Eng Sample 100-000001046-04

### GPU

MI455 (A0)

### ROCm Version

ROCM 10.1

### Installation Method

Python wheels

### Installed ROCm Packages / Versions

<details>
<summary>Installed ROCm packages / versions</summary>

```
accelerate==1.15.0
agent-detector==2.0.0
aiofiles==25.1.0
aiohappyeyeballs==2.7.1
aiohttp==3.14.3
aiosignal==1.4.0
-e git+https://github.com/ROCm/aiter.git@0200ada1aa4cc7fe47aa14abd4677b35105b1553#egg=amd_aiter
amd-quark==0.12.post1
amd-torch-device-gfx1250==2.11.0+rocm10.1.0a20260811.bkc.20260820
amd_mori @ file:///install/amd_mori-1.0.0-cp312-cp312-linux_x86_64.whl#sha256=2231d9413d6a9aa7ed41879420c9dc020adabe8f80de24d984ba3f96447f2133
annotated-doc==0.0.5
annotated-types==0.8.0
anthropic==1.4.0
anyio==4.15.1
apache-tvm-ffi==0.1.10
astor==0.8.1
attrs==26.1.0
azure-core==1.41.0
azure-identity==1.25.3
azure-storage-blob==12.30.1
blake3==1.0.9
blinker==1.9.0
boto3==1.43.91
botocore==1.43.91
cachetools==7.1.8
cbor2==6.1.4
certifi==2026.7.22
cffi==2.1.1
charset-normalizer==3.5.1
click==8.5.0
cloudpickle==3.1.2
cmake==3.31.10
colorama==0.4.6
compressed-tensors==0.17.0
conch-triton-kernels==1.2.1
cryptography==50.0.1
Cython==3.3.0
datasets==5.0.1
depyf==0.20.0
detect-installer==0.2.1
dill==0.4.1
dnspython==2.8.0
docstring_parser==0.18.0
einops==0.8.2
email-validator==2.3.0
evaluate==0.4.6
fastapi==0.136.3
fastapi-cli==0.0.32
fastapi-cloud-cli==0.25.0
fastar==0.12.0
fastsafetensors==0.4.0
filelock==3.32.6
flash_attn @ file:///install/flash_attn-2.8.3-py3-none-any.whl#sha256=4b779dcd819233a31056a9e0d3a179ad8aad34890831d03986328c1540f35ebe
Flask==3.1.3
flydsl==0.3.2
frozenlist==1.8.0
fsspec==2026.6.0
google-api-core==2.36.0
google-auth==2.58.0
google-cloud-core==2.7.0
google-cloud-storage==3.14.1
google-crc32c==1.8.0
google-resumable-media==2.10.2
googleapis-common-protos==1.75.3
grpcio==1.78.0
grpcio-reflection==1.78.0
h11==0.16.0
h2==4.4.1
hf-xet==1.6.0
hiredis==3.4.1
hpack==4.2.0
httpcore==1.0.9
httpcore2==2.12.0
httptools==0.8.0
httpx==0.28.1
httpx2==2.12.0
huggingface_hub==1.31.0
humanize==4.16.0
Hypercorn==0.18.0
hyperframe==6.1.0
idna==3.19
ijson==3.5.1
iniconfig==2.3.0
interegular==0.3.3
isodate==0.7.2
itsdangerous==2.2.0
Jinja2==3.1.6
jiter==0.16.0
jmespath==1.1.0
joblib==1.6.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
lark==1.2.2
libnacl==2.1.0
llguidance==1.7.6
llvmlite==0.47.0
lm-format-enforcer==0.11.3
loguru==0.7.3
markdown-it-py==4.2.0
MarkupSafe==3.0.3
mcp==2.2.0
mcp-types==2.2.0
mdurl==0.1.2
mistral_common==1.11.7
ml_dtypes==0.6.0
model-hosting-container-standards==0.1.16
mpmath==1.3.0
msal==1.38.0
msal-extensions==1.3.1
msgpack==1.2.2
msgspec==0.21.1
multidict==6.8.0
multiprocess==0.70.19
narwhals==2.26.0
networkx==3.6.1
ninja==1.13.2
numba==0.65.0
numpy==2.3.5
onnx==1.22.0
onnx-ir==1.0.0
onnxscript==0.7.2
onnxslim==0.1.96
openai==3.11.0
openai-harmony==0.0.8
opencv-python-headless==5.0.0.93
opentelemetry-api==1.44.0
opentelemetry-exporter-otlp==1.44.0
opentelemetry-exporter-otlp-proto-common==1.44.0
opentelemetry-exporter-otlp-proto-grpc==1.44.0
opentelemetry-exporter-otlp-proto-http==1.44.0
opentelemetry-proto==1.44.0
opentelemetry-sdk==1.44.0
opentelemetry-semantic-conventions==0.65b0
opentelemetry-semantic-conventions-ai==0.5.1
outlines_core==0.2.14
packaging==26.3
pandas==3.0.5
partial-json-parser==0.2.1.1.post7
peft==0.20.0
pillow==12.3.0
plotly==7.0.0
pluggy==1.6.0
priority==2.0.0
prometheus-fastapi-instrumentator==8.1.0
prometheus_client==0.26.0
propcache==0.5.2
proto-plus==1.28.4
protobuf==6.33.6
psutil==7.2.2
py-cpuinfo==9.0.0
pyarrow==25.0.1
pyasn1==0.6.4
pyasn1_modules==0.4.2
pybase64==1.5.0
pybind11==3.1.0
pycountry==26.2.16
pycparser==3.0
pydantic==2.13.5
pydantic-extra-types==2.11.1
pydantic-settings==2.15.0
pydantic_core==2.46.5
Pygments==2.21.0
PyJWT==2.13.0
pytest==9.1.1
pytest-asyncio==1.4.0
python-dateutil==2.9.0.post0
python-dotenv==1.2.3
python-json-logger==4.2.0
python-multipart==0.0.32
PyYAML==6.0.3
pyzmq==27.2.0
Quart==0.22.0
redis==8.1.0
referencing==0.37.0
regex==2026.9.10
requests==2.34.2
rich==15.0.0
rich-toolkit==0.20.5
rignore==0.8.1
rixl @ file:///rixl_install/rixl-1.1.0-cp312-cp312-manylinux_2_39_x86_64.whl
rocm==10.1.0a20260811+bkc.20260820
rocm-bootstrap==0.2.0
rocm-sdk-core==10.1.0a20260811+bkc.20260820
rocm-sdk-devel==10.1.0a20260811+bkc.20260820
rocm-sdk-device-gfx1250==10.1.0a20260811+bkc.20260820
rocm-sdk-libraries==10.1.0a20260811+bkc.20260820
rpds-py==2026.6.3
runai-model-streamer==0.15.7
runai-model-streamer-azure==0.15.7
runai-model-streamer-gcs==0.15.7
runai-model-streamer-s3==0.15.7
s3transfer==0.19.2
safetensors==0.8.0
scipy==1.18.1
semantic-version==2.10.0
sentencepiece==0.2.2
sentry-sdk==2.69.1
setproctitle==1.3.7
setuptools==79.0.1
setuptools-rust==1.13.0
setuptools-scm==10.2.3
shellingham==1.5.4
six==1.17.0
sniffio==1.3.1
sse-starlette==3.4.11
starlette==1.6.0
supervisor==4.3.0
sympy==1.14.0
tensorizer==2.10.1
tiktoken==0.14.0
tilelang==0.1.10
timm==1.0.29
tokenizers==0.23.2
torch==2.11.0+rocm10.1.0a20260811.bkc.20260820
torch_c_dlpack_ext==0.1.5
torchaudio==2.11.0+rocm10.1.0a20260811.bkc.20260820
torchvision==0.26.0+rocm10.1.0a20260811.bkc.20260820
tqdm==4.70.0
transformers==5.17.0
triton @ file:///app/triton
truststore==0.10.4
typer==0.27.2
typing-inspection==0.4.4
typing_extensions==4.16.0
urllib3==2.7.0
uvicorn==0.52.4
uvloop==0.22.1
vcs-versioning==2.3.4
vllm @ file:///install/vllm-0.9.2rc2.dev13074+g5887cf8ac.rocm101-cp312-cp312-linux_x86_64.whl
watchfiles==1.2.0
websockets==17.1
Werkzeug==3.1.8
wheel==0.48.0
wsproto==1.3.2
xgrammar==0.2.6
xxhash==4.0.1
yarl==1.24.5
z3-solver==4.15.4.0
zstandard==0.25.0

libamdhip64-5/now 5.7.1-3 amd64 [installed,local]
libdrm-amdgpu1/now 2.4.125-1ubuntu0.1~24.04.2 amd64 [installed,local]
```

</details>


### ROCm Component

_No response_

### Steps to Reproduce

Pull this image: rocm/vllm-dev:nightly_455_wip_main_torch__0910_b231 to have the testing environment described above.

To repro you can run /app/vllm_smoketest.sh --dsr1 inside the image. This vllm serve for DeepSeek-R1-0528-MXFP4 crashes the engine core during warmup with HSA_STATUS_ERROR_MEMORY_FAULT / illegal memory access. Git bisect on aiter points to 0200ada1a "[Triton/Gluon] Consolidate and reorganize ops/triton utils (#5061)"

For a standalone reproducer see attached afp4_repro.py, DSR1 shared-expert down_proj shape N=7168, K=2048, M=16/32, HIP_VISIBLE_DEVICES=1

[afp4_repro.py](https://github.com/user-attachments/files/32077815/afp4_repro.py)


### (Optional for Linux users) Output of rocminfo --support

<details>
<summary>rocminfo --support output</summary>

```
Paste output here
```

</details>


### Additional Information

_No response_

## 评论 (3)

### JadenMathias · 2026-09-11

Additional reproducer:

```#!/usr/bin/env python3
# gfx1250: aiter Triton _gemm_afp4wfp4_kernel clobbers the address VGPRs of an
# in-flight global_load_async_to_lds_b128 (the s_wait_alu depctr_vm_vsrc(0) fence
# is emitted one instruction too late), so the load fetches from an address built
# out of e8m0 scale bytes.  Needs K-major scales and K=2048 at BLOCK_SIZE_K=1024.
# Workaround: TRITON_HIP_USE_ASYNC_COPY=0
import torch
from aiter.ops.triton._triton_kernels.gemm.basic.gemm_afp4wfp4 import _gemm_afp4wfp4_kernel

M, N, K = 32, 32, 2048
KP, u8, dev = K // 2, torch.uint8, "cuda"

x  = torch.randint(0, 256, (M, KP), dtype=u8, device=dev)        # A  (M, K//2)
w  = torch.randint(0, 256, (N, KP), dtype=u8, device=dev).T      # B  (K//2, N)
y  = torch.empty((M, N), dtype=torch.bfloat16, device=dev)       # C  (M, N)
xs = torch.randint(0x76, 0x7B, (K // 32, M), dtype=u8, device=dev).T   # K-major e8m0 scales
ws = torch.randint(0x76, 0x7B, (K // 32, N), dtype=u8, device=dev).T   # K-major e8m0 scales

_gemm_afp4wfp4_kernel[(M // 32) * (N // 32),](
    x, w, y, xs, ws, M, N, KP,
    x.stride(0), x.stride(1), w.stride(0), w.stride(1),
    0, y.stride(0), y.stride(1),
    xs.stride(0), xs.stride(1), ws.stride(0), ws.stride(1),
    BLOCK_SIZE_M=32, BLOCK_SIZE_N=32, BLOCK_SIZE_K=1024, GROUP_SIZE_M=4,
    NUM_KSPLIT=1, SPLITK_BLOCK_SIZE=2 * KP, num_warps=4, num_stages=3,
    waves_per_eu=1, matrix_instr_nonkdim=16, cache_modifier=".cg",
)

# Faults here: "Memory access fault by GPU node-2 ... on address 0x777700787000"
# -> SIGABRT + GPU core dump written to the cwd as gpucore.<pid>.gpu
torch.cuda.synchronize()
print("no fault")
 ```

### JadenMathias · 2026-09-11

A Workaround for this issue is to set: `TRITON_HIP_USE_ASYNC_COPY=0`

### Boss2002n · 2026-09-24

Works on Latest AITER and upstream triton, tested on a B0 machine 
