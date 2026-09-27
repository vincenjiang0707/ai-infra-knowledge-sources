# [Issue #4558] [Bug] Qwen3.6-27B-AWQ out of memory with TurboMind engine on V100

source: https://github.com/InternLM/lmdeploy/issues/4558
state: open | updated: 2026-05-07T06:26:07Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

I've download QuantTrio/Qwen3.6-27B-AWQ, and run it with last lmdeloy version(0.12.3), after turbomind convert completed, it's coredump with a cuda oom error, even after I limit max_context_token_num to 2048.

```
ls -lh Qwen3.6-27B-AWQ
rwxrwxrwx 1 xxx xxx 122 Apr 28 10:16 Qwen3.6-27B-AWQ -> /data/xxx/.cache/huggingface/hub/models--QuantTrio--Qwen3.6-27B-AWQ/snapshots/9b507bdc9afafb87b7898700cc2a591aa6639461/
```

run it with lmdeploy 0.12.3
```
lmdeploy --version0.12.3

nvidia-smi | egrep -e "Default| Driver"
| NVIDIA-SMI 575.57.08              Driver Version: 575.57.08      CUDA Version: 12.9     |
| N/A   40C    P0             36W /  250W |   32004MiB /  32768MiB |      0%      Default |
| N/A   35C    P0             24W /  250W |       0MiB /  32768MiB |      0%      Default |
| N/A   49C    P0             39W /  250W |   30418MiB /  32768MiB |      0%      Default |
| N/A   55C    P0             48W /  250W |   30418MiB /  32768MiB |      0%      Default |

```

core dump with out of memory
```
CUDA_VISIBLE_DEVICES=1 lmdeploy serve api_server QuantTrio/Qwen3.6-27B-AWQ
Fetching 25 files: 100%|████████████████████████████████████████| 25/25 [00:00<00:00, 5991.86it/s]
Download complete: : 0.00B [00:00, ?B/s]                                   | 0/25 [00:00<?, ?it/s]
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!
[TM][WARNING] [TM] `max_context_token_num` is not set, default to 262144.
2026-04-28 10:59:12,438 - lmdeploy - WARNING - turbomind.py:246 - get 1197 model params
[TM][ERROR] CUDA runtime error: out of memory /lmdeploy/src/turbomind/core/allocator.cc:49        
Aborted (core dumped)
```

limit to 2048 context, still core dump, just after the convert is completed
```
CUDA_VISIBLE_DEVICES=1 lmdeploy serve api_server ./Qwen3.6-27B-AWQ --max-concurrent-requests 1 --session-len 2048
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!
[TM][WARNING] [TM] `max_context_token_num` is not set, default to 2048.
2026-04-28 11:01:38,266 - lmdeploy - WARNING - turbomind.py:246 - get 1197 model params
Convert to turbomind format:  100%|██████████████████████████████  | 64/64 [00:18<00:01,  3.60it/s]
[TM][ERROR] CUDA runtime error: out of memory /lmdeploy/src/turbomind/core/allocator.cc:49        
Aborted (core dumped)
```


### Reproduction

limit to 2048 context, still core dump, just after the convert is completed
```
CUDA_VISIBLE_DEVICES=1 lmdeploy serve api_server QuantTrio/Qwen3.6-27B-AWQ --max-concurrent-requests 1 --session-len 2048
```


### Environment

```Shell
sys.platform: linux
Python: 3.12.12 (main, Feb  3 2026, 22:51:04) [Clang 21.1.4 ]
CUDA available: True
MUSA available: False
numpy_random_seed: 2147483648
GPU 0,1,2,3: Tesla V100-PCIE-32GB
CUDA_HOME: /usr/local/cuda
NVCC: Cuda compilation tools, release 12.9, V12.9.86
GCC: cc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0
PyTorch: 2.10.0+cu128
PyTorch compiling details: PyTorch built with:
  - GCC 13.3
  - C++ Version: 201703
  - Intel(R) oneAPI Math Kernel Library Version 2024.2-Product Build 20240605 for Intel(R) 64 architecture applications
  - Intel(R) MKL-DNN v3.7.1 (Git Hash 8d263e693366ef8db40acc569cc7d8edf644556d)
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - LAPACK is enabled (usually provided by MKL)
  - NNPACK is enabled
  - CPU capability usage: AVX2
  - CUDA Runtime 12.8
  - NVCC architecture flags: -gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_80,code=sm_80;-gencode;arch=compute_86,code=sm_86;-gencode;arch=compute_90,code=sm_90;-gencode;arch=compute_100,code=sm_100;-gencode;arch=compute_120,code=sm_120
  - CuDNN 91.0.2  (built against CUDA 12.9)
  - Magma 2.6.1
  - Build settings: BLAS_INFO=mkl, BUILD_TYPE=Release, COMMIT_SHA=449b1768410104d3ed79d3bcfe4ba1d65c7f22c0, CUDA_VERSION=12.8, CUDNN_VERSION=9.10.2, CXX_COMPILER=/opt/rh/gcc-toolset-13/root/usr/bin/c++, CXX_FLAGS= -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_KINETO -DLIBKINETO_NOROCTRACER -DLIBKINETO_NOXPUPTI=ON -DUSE_FBGEMM -DUSE_FBGEMM_GENAI -DUSE_PYTORCH_QNNPACK -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -DC10_NODEPRECATED -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=range-loop-construct -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-unknown-pragmas -Wno-unused-parameter -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wsuggest-override -Wno-psabi -Wno-error=old-style-cast -faligned-new -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-dangling-reference -Wno-error=dangling-reference -Wno-stringop-overflow, LAPACK_INFO=mkl, PERF_WITH_AVX=1, PERF_WITH_AVX2=1, TORCH_VERSION=2.10.0, USE_CUDA=ON, USE_CUDNN=ON, USE_CUSPARSELT=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_GLOO=ON, USE_MKL=ON, USE_MKLDNN=ON, USE_MPI=OFF, USE_NCCL=1, USE_NNPACK=ON, USE_OPENMP=ON, USE_ROCM=OFF, USE_ROCM_KERNEL_ASSERT=OFF, USE_XCCL=OFF, USE_XPU=OFF, 

TorchVision: 0.25.0+cu128
LMDeploy: 0.12.3+
transformers: 5.6.2
fastapi: 0.136.1
pydantic: 2.13.3
triton: 3.6.0
NVIDIA Topology: 
	GPU0	GPU1	GPU2	GPU3	CPU Affinity	NUMA Affinity	GPU NUMA ID
GPU0	 X 	PIX	PHB	PHB	0-13,28-41	0		N/A
GPU1	PIX	 X 	PHB	PHB	0-13,28-41	0		N/A
GPU2	PHB	PHB	 X 	PIX	0-13,28-41	0		N/A
GPU3	PHB	PHB	PIX	 X 	0-13,28-41	0		N/A

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks
```

### Error traceback

```Shell

```

## 评论 (3)

### lvhan028 · 2026-04-29

Can you try "--max-batch-size 8"?

### bash99 · 2026-05-06

> Can you try "--max-batch-size 8"?

Yes, it works, but which tool-call parser should I use?

I run it with 
```
CUDA_VISIBLE_DEVICES=1 lmdeploy serve api_server $MODEL --model-name $MODEL_NAME \
        --server-port 27878 --enable-prefix-caching --allow-terminate-by-client \        --max-concurrent-requests 8 --max-batch-size 8 --session-len 25600 --cache-max-entry-count 0.9 \
        --tool-call-parser qwen --reasoning-parser qwen-qwq
```

And test it with same api is ok, but test it with tool call, 
```python
def build_calculator_tools():
    """Return the calculator tool schema used by the tests."""
    return [
        {
            "type": "function",
            "function": {
                "name": "calculate",
                "description": "Calculate a math expression",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "Math expression like '2+3*5'"
                        }
                    },
                    "required": ["expression"]
                }
            }
        }
    ]

def test_tool_use(model_id, chat_url, headers):
    payload = {
        "model": model_id,
        "messages": [{"role": "user", "content": "Calculate 15+27"}],
        "tools": build_calculator_tools()
    }

    try:
        req = request.Request(
            chat_url,
            data=json.dumps(payload).encode(),
            headers=headers,
            method="POST"
        )

        with request.urlopen(req) as res:
            response = json.loads(res.read().decode())
            print(f"{response}")
    except error.HTTPError as e:
        body = e.read().decode()
        print(body)
```

I got a error
```
2026-05-06 14:42:39,070 - lmdeploy - ERROR - api_server.py:662 - Failed to parse Thinking Process:
1.  **Identify the user's request:** The user wants to calculate the sum of 15 and 27.
2.  **Select the appropriate tool:** The `calculate` tool is available for math expressions.
3.  **Formulate the tool call:**                                                                  
    *   Tool: `calculate`                                                                         
    *   Parameter `expression`: "15+27"                                                           
4.  **Execute the tool call:** (Mental simulation of tool execution) 15 + 27 = 42.
5.  **Formulate the final response:** State the result clearly. I will call the tool first.
*Self-Correction/Refinement:* I have the `calculate` tool, so I should use it as instructed.

Tool Call: `calculate(expression="15+27")`
Result: 42
Response: 42. (Or a full sentence)
I will proceed with the tool call.
</think>

<tool_call>
<function=calculate>
<parameter=expression>
15+27     
</parameter>                                     
</function>                                      
</tool_call>. Exception: Expecting value: line 2 column 1 (char 1).
```

### bash99 · 2026-05-07

> Can you try "--max-batch-size 8"?

BTW, how to enable mtp in turbomind engine?
like this repo [hampsonw/Qwen3.6-27B-AWQ-BF16-INT4-mtp-bf16](https://huggingface.co/hampsonw/Qwen3.6-27B-AWQ-BF16-INT4-mtp-bf16) 
