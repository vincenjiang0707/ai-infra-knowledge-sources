# [Issue #4347] [Bug] GPT-OSS-120B + openai-python empty result from `client.beta.chat.completions.parse` with `response_format`

source: https://github.com/InternLM/lmdeploy/issues/4347
state: closed | updated: 2026-05-13T09:25:29Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

[Bug] openai-python empty result from `client.beta.chat.completions.parse` with `response_format`

openai version: 0.109.0

### Reproduction

Server: 

```
export TM_ANOMALY_HANDLER="level=2,inf=65504,nan=0"
export HUGGINGFACE_OFFLINE=1
export CUDA_VISIBLE_DEVICES=0,1,2,3
export TIKTOKEN_RS_CHACE_DIR=~/.cache/huggingface/hub/models--openai--gpt-oss-120b/snapshots/b5c939de8f754692c1647ca79fbf85e8c1e70f8a/encodings
export TIKTOKEN_ENCODINGS_BASE=~/.cache/huggingface/hub/models--openai--gpt-oss-120b/snapshots/b5c939de8f754692c1647ca79fbf85e8c1e70f8a/encodings


lmdeploy serve api_server \
        openai/gpt-oss-120b \
        --backend turbomind \
        --enable-prefix-caching \
        --cache-max-entry-count 0.90 \
        --enable-prefix-caching \
        --tp 4 \
        --communicator native \
        --log-level WARNING \
        --max-log-len 200
```

Client

```python

    """
    Format output
    """
    format_msgs=[
        {"role": "system", "content": 
         '你是一个编剧，负责设计角色的个人信息, 记住直接输出我要求的格式的json字符串的内容' 
        },
        {"role": "user",  "content": "现在设计三个角色。"}
    ]

    class Character(BaseModel):
        comment: str = Field(description="你的思考过程，为什么这么设计")
        name: str = Field(description="角色的名字")
        personality: str = Field(description="角色的性格")
        age: int = Field(description="角色的年龄")

    class CharacterList(BaseModel):
    
        list: List[Character] = Field(description="多个角色的列表")

    for _ in range(5):
        try:
            response = client.beta.chat.completions.parse(
                messages=format_msgs,
                model=model,
                timeout=120,
                response_format=CharacterList
            )
            print(response.choices[0].message)

            print(response.choices[0].message.parsed)

            result = response.choices[0].message.parsed
            if result is None:
                continue

```


### Environment

```Shell
sys.platform: linux
Python: 3.12.0 | packaged by Anaconda, Inc. | (main, Oct  2 2023, 17:29:18) [GCC 11.2.0]
CUDA available: True
MUSA available: False
numpy_random_seed: 2147483648
GPU 0,1,2,3: Tesla V100-PCIE-32GB
CUDA_HOME: /usr/local/cuda
NVCC: Cuda compilation tools, release 12.1, V12.1.66
GCC: gcc (Ubuntu 9.4.0-1ubuntu1~20.04.3) 9.4.0
PyTorch: 2.8.0+cu128
PyTorch compiling details: PyTorch built with:
  - GCC 13.3
  - C++ Version: 201703
  - Intel(R) oneAPI Math Kernel Library Version 2024.2-Product Build 20240605 for Intel(R) 64 architecture applications
  - Intel(R) MKL-DNN v3.7.1 (Git Hash 8d263e693366ef8db40acc569cc7d8edf644556d)
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - LAPACK is enabled (usually provided by MKL)
  - NNPACK is enabled
  - CPU capability usage: AVX512
  - CUDA Runtime 12.8
  - NVCC architecture flags: -gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_80,code=sm_80;-gencode;arch=compute_86,code=sm_86;-gencode;arch=compute_90,code=sm_90;-gencode;arch=compute_100,code=sm_100;-gencode;arch=compute_120,code=sm_120
  - CuDNN 91.0.2  (built against CUDA 12.9)
    - Built with CuDNN 90.8
  - Magma 2.6.1
  - Build settings: BLAS_INFO=mkl, BUILD_TYPE=Release, COMMIT_SHA=a1cb3cc05d46d198467bebbb6e8fba50a325d4e7, CUDA_VERSION=12.8, CUDNN_VERSION=9.8.0, CXX_COMPILER=/opt/rh/gcc-toolset-13/root/usr/bin/c++, CXX_FLAGS= -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_KINETO -DLIBKINETO_NOROCTRACER -DLIBKINETO_NOXPUPTI=ON -DUSE_FBGEMM -DUSE_PYTORCH_QNNPACK -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -DC10_NODEPRECATED -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=range-loop-construct -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-unknown-pragmas -Wno-unused-parameter -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wsuggest-override -Wno-psabi -Wno-error=old-style-cast -faligned-new -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-dangling-reference -Wno-error=dangling-reference -Wno-stringop-overflow, LAPACK_INFO=mkl, PERF_WITH_AVX=1, PERF_WITH_AVX2=1, TORCH_VERSION=2.8.0, USE_CUDA=ON, USE_CUDNN=ON, USE_CUSPARSELT=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_GLOO=ON, USE_MKL=ON, USE_MKLDNN=ON, USE_MPI=OFF, USE_NCCL=1, USE_NNPACK=ON, USE_OPENMP=ON, USE_ROCM=OFF, USE_ROCM_KERNEL_ASSERT=OFF, USE_XCCL=OFF, USE_XPU=OFF,

TorchVision: 0.23.0+cu128
LMDeploy: 0.12.0+
transformers: 4.57.1
fastapi: 0.120.1
pydantic: 2.12.3
triton: 3.4.0
NVIDIA Topology:
        GPU0    GPU1    GPU2    GPU3    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      PIX     PIX     PIX     0-17,36-53      0               N/A
GPU1    PIX      X      PIX     PIX     0-17,36-53      0               N/A
GPU2    PIX     PIX      X      PIX     0-17,36-53      0               N/A
GPU3    PIX     PIX     PIX      X      0-17,36-53      0               N/A

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
ParsedChatCompletionMessage[test_llm_capabilities.<locals>.CharacterList](content=None, refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, parsed=None)
None
ParsedChatCompletionMessage[test_llm_capabilities.<locals>.CharacterList](content=None, refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, parsed=None)
None
ParsedChatCompletionMessage[test_llm_capabilities.<locals>.CharacterList](content=None, refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, parsed=None)
None
ParsedChatCompletionMessage[test_llm_capabilities.<locals>.CharacterList](content=None, refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, parsed=None)
None
ParsedChatCompletionMessage[test_llm_capabilities.<locals>.CharacterList](content=None, refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, parsed=None)
None
```

## 评论 (15)

### windreamer · 2026-02-12

Can you get the raw output of the chat completion instead of the parsed one? And if the PyTorch engine works?

### jingyibo123 · 2026-02-13

> Can you get the raw output of the chat completion instead of the parsed one? And if the PyTorch engine works?

Raw request:
```
curl http://myopenai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234l" \
  -d '{
    "model": "gpt-oss-120b",
    "messages": [
      {
        "role": "system",
        "content": "你是一个编剧，负责设计角色的个人信息。请输出 JSON 格式。"
      },
      {
        "role": "user",
        "content": "现在设计三个角色。"
      }
    ],
    "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "CharacterList",
      "strict": true,
      "schema": {
        "$defs": {
          "Character": {
            "properties": {
              "comment": { "description": "你的思考过程，为什么这么设计", "title": "Comment", "type": "string" },
              "name": { "description": "角色的名字", "title": "Name", "type": "string" },
              "personality": { "description": "角色的性格", "title": "Personality", "type": "string" },
              "age": { "description": "角色的年龄", "title": "Age", "type": "integer" }
            },
            "required": ["comment", "name", "personality", "age"],
            "title": "Character",
            "type": "object",
            "additionalProperties": false
          }
        },
        "properties": {
          "list": {
            "description": "多个角色的列表",
            "items": { "$ref": "#/$defs/Character" },
            "title": "List",
            "type": "array"
          }
        },
        "required": ["list"],
        "title": "CharacterList",
        "type": "object",
        "additionalProperties": false
      }
    }
  },
  "stream": false
}'
```

Calling with curl, I'm stuck with no result. the lmdeploy backend seems running forever.

---

pytorch engines does not support gpt-oss-120b...

```
RuntimeError: Unsupported quant method: mxfp4
```
@windreamer BTW happy spring festival ~

### windreamer · 2026-02-24

> > Can you get the raw output of the chat completion instead of the parsed one? And if the PyTorch engine works?
> 
> Raw request:
> 
> ```
> curl http://myopenai.com/v1/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer sk-1234l" \
>   -d '{
>     "model": "gpt-oss-120b",
>     "messages": [
>       {
>         "role": "system",
>         "content": "你是一个编剧，负责设计角色的个人信息。请输出 JSON 格式。"
>       },
>       {
>         "role": "user",
>         "content": "现在设计三个角色。"
>       }
>     ],
>     "response_format": {
>     "type": "json_schema",
>     "json_schema": {
>       "name": "CharacterList",
>       "strict": true,
>       "schema": {
>         "$defs": {
>           "Character": {
>             "properties": {
>               "comment": { "description": "你的思考过程，为什么这么设计", "title": "Comment", "type": "string" },
>               "name": { "description": "角色的名字", "title": "Name", "type": "string" },
>               "personality": { "description": "角色的性格", "title": "Personality", "type": "string" },
>               "age": { "description": "角色的年龄", "title": "Age", "type": "integer" }
>             },
>             "required": ["comment", "name", "personality", "age"],
>             "title": "Character",
>             "type": "object",
>             "additionalProperties": false
>           }
>         },
>         "properties": {
>           "list": {
>             "description": "多个角色的列表",
>             "items": { "$ref": "#/$defs/Character" },
>             "title": "List",
>             "type": "array"
>           }
>         },
>         "required": ["list"],
>         "title": "CharacterList",
>         "type": "object",
>         "additionalProperties": false
>       }
>     }
>   },
>   "stream": false
> }'
> ```
> 
> Calling with curl, I'm stuck with no result. the lmdeploy backend seems running forever.
> 
> pytorch engines does not support gpt-oss-120b...
> 
> ```
> RuntimeError: Unsupported quant method: mxfp4
> ```
> 
> [@windreamer](https://github.com/windreamer) BTW happy spring festival ~

What if we use stream mode or remove the response_format parameter? We cannot identify the root cause if we only know that the output is None or that the response never returns. I believe we need to verify whether the response is valid to determine if the TM engine itself has failed. Additionally, we need to ascertain whether the issue stems from guided decoding or not.

In PR #4349 , we fixed some small bugs in guided decoding of TM. You can try if it fixes

### jingyibo123 · 2026-02-25

FYI，setting stream=True is also stuck with not result. Removing response_format works fine(regular openAI chat completion).  
>  I believe we need to verify whether the response is valid to determine if the TM engine itself has failed. Additionally, we need to ascertain whether the issue stems from guided decoding or not.

I'll try the PR, is there some useful settings/arguments to better debug this? 

### windreamer · 2026-02-25

> FYI，setting stream=True is also stuck with not result. Removing response_format works fine(regular openAI chat completion).
> 
> > I believe we need to verify whether the response is valid to determine if the TM engine itself has failed. Additionally, we need to ascertain whether the issue stems from guided decoding or not.
> 
> I'll try the PR, is there some useful settings/arguments to better debug this?

OK, seems something wrong with the guided decoding in Turbomind. GPT-OSS uses a special tokenizer, so there might be something broken there. I will try to reproduce this. 

### jingyibo123 · 2026-02-25

Updating to 0.12.1, I DO got an error from backend: 

```
lmdeploy - ERROR - async_engine.py:271 - [safe_run] session 1 exception caught: HarmonyError unexpected tokens remaining in message header: Some("{\"list\": [{\"comment\": \"The user requests three characters. The user wants a JSON output with personal information for three characters. The user says: \\\"现在设计三个角色。\\\" This is a request for content creation, which is allowed. The user wants a JSON string with the characters. There's no disallowed content. We can comply. We'll provide a JSON with three character objects, each with fields like name, age, gender, occupation, personality traits, background, etc. The user wants the format in JSON, likely just the JSON object. We'll output a JSON string directly. We'll keep it simple and ensure it's a valid JSON. The user wants Chinese presumably. So we'll write Chinese names and descriptions. We must ensure we output only the JSON object, no extra commentary. We'll produce a JSON array or object. The user said \\\"直接输出我要求的格式的json字符串的内容\\\" meaning output directly the JSON string content. So we output a JSON array of three objects.")
```

Request is stuck without response though.

### windreamer · 2026-02-25

It seems the model generate CoT texts in `comment` field, make the response too long to be parsed? Can you try to tweak your prompt to make the model skip CoT and produce shorter result?


### jingyibo123 · 2026-02-25

I removed the `comment`, still got a similar error though @windreamer .
```
"messages": [
    {
      "role": "system",
      "content": "你是一个编剧，负责设计角色的个人信息, 记住直接输出我要求的格式的json字符串的内容"
    },
    {
      "role": "user",
      "content": "现在设计三个角色。"
    }
  ],
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "CharacterList",
      "strict": true,
      "schema": {
        "$defs": {
          "Character": {
            "properties": {
              "name": { "description": "角色的名字", "title": "Name", "type": "string" },
              "personality": { "description": "角色的性格", "title": "Personality", "type": "string" },
              "age": { "description": "角色的年龄", "title": "Age", "type": "integer" }
            },
            "required": ["name", "personality", "age"],
            "title": "Character",
            "type": "object",
            "additionalProperties": false
          }
        },
```

**Error**:
```
2026-02-25 16:17:58,353 - lmdeploy - ERROR - async_engine.py:271 - [safe_run] session 3 exception caught: HarmonyError unexpected tokens remaining in message header: Some("{\"list\": [{\"name\": \"沈海\", \"personality\": \"冷静、理性\", \"age\": 34}, {\"name\": \"林若\",")
```


### windreamer · 2026-02-28

Yes， I think I can reproduce this issue. I am still digging into it to identify root cause.

It seems to be hang, but based on my observation, it is generating garbage output again and again.  You can forced to limit the output token length with `max_completion_tokens`

It seems the guided decoding state is broken, and it works fine with Qwen. I am still investigating this.

### windreamer · 2026-02-28

Hi @jingyibo123 ,

Current status and preliminary conclusion:

1. We did a quick sanity check on the latest `main` branch. **Guided Decoding / structured output enforcement** (used by `client.beta.chat.completions.parse(..., response_format=...)`) appears to work as intended in general. However, **enabling it makes GPT‑OSS outputs unstable/confused**, which then leads to empty/failed parses on the client side.

2. Guided Decoding works by **constraining the model token-by-token to match a target schema** (here: JSON). This assumes the model is operating in a “standard chat output mode” where raw text is directly the assistant response.

3. **GPT‑OSS models are aligned to produce “Harmony Response” format**, not plain chat text. When we force JSON via Guided Decoding, the model no longer follows Harmony formatting. As a result, the server-side Harmony handling/decoding layer cannot correctly interpret or assemble the response.

4. This mismatch explains the observed symptoms:
   - **Harmony parse errors** (the response is not valid Harmony anymore)
   - **hang/stalls** (server-side pipeline waiting for/expecting Harmony-compliant segments)
   - **`message.parsed == None` / empty result** on the client (because the upstream response is malformed or not finalized correctly)

5. We also tried bypassing Harmony parsing and inspecting the **raw constrained output**. The model can roughly follow the JSON shape, but **content quality and consistency are poor**, so this is not a reliable workaround.

6. Similar issues have been reported elsewhere (independent confirmation):  
   https://www.glukhov.org/llm-performance/ollama/ollama-gpt-oss-structured-output-issues/

Preliminary conclusion: this is likely **not a pure openai-python `parse()` client bug**, but a **protocol incompatibility between Harmony Response and JSON-guided decoding** in the current serving stack. 

---

Hi @jingyibo123 ，  
当前进展与初步结论如下：

1. 我们在最新的 `main` 分支上做了快速验证：总体来看，`client.beta.chat.completions.parse(..., response_format=...)` 所依赖的 **Guided Decoding / 结构化输出约束**机制本身是正常工作的。但在 **GPT‑OSS** 上开启该功能后，模型输出会变得不稳定/混乱，进而导致客户端侧出现空结果或解析失败。

2. Guided Decoding 的原理是：通过 **逐 token 约束**来强制模型输出符合目标 schema（这里是 JSON）。这通常隐含一个前提：模型处在“标准 chat 输出模式”，即 assistant 的原始文本可以直接作为响应内容返回。

3. **GPT‑OSS 模型对齐的是 “Harmony Response” 格式**，而不是普通的纯文本 chat 输出。当我们用 Guided Decoding 强制输出 JSON 时，模型就不再遵循 Harmony 格式，导致服务端的 Harmony 相关处理/解码层无法正确识别或组装响应。

4. 这种不匹配可以解释目前看到的现象：
   - **Harmony 解析错误**（因为响应不再是合法的 Harmony 格式）
   - **卡住/挂起**（服务端流水线仍在等待/假设会出现 Harmony 结构片段）
   - 客户端侧 **`message.parsed == None` / 空结果**（上游响应异常或无法正确结束返回，导致解析拿不到内容）

5. 我们也尝试过绕过 Harmony 解析，直接查看 **裸输出**：模型大致能被约束到 JSON 的形式，但 **内容质量和一致性较差**，因此这不是一个可靠的规避方案。

6. 其他场景也有人报告过类似问题（可作为旁证）：  
   https://www.glukhov.org/llm-performance/ollama/ollama-gpt-oss-structured-output-issues/

初步结论：这很可能 **不是 openai-python `parse()` 的纯客户端 bug**，而是当前服务栈中 **Harmony Response 与 JSON Guided Decoding 之间的协议/模式不兼容**所导致的问题。

### windreamer · 2026-02-28

> Hi [@jingyibo123](https://github.com/jingyibo123) ,
> 
> Current status and preliminary conclusion:
> 
>     1. We did a quick sanity check on the latest `main` branch. **Guided Decoding / structured output enforcement** (used by `client.beta.chat.completions.parse(..., response_format=...)`) appears to work as intended in general. However, **enabling it makes GPT‑OSS outputs unstable/confused**, which then leads to empty/failed parses on the client side.
> 
>     2. Guided Decoding works by **constraining the model token-by-token to match a target schema** (here: JSON). This assumes the model is operating in a “standard chat output mode” where raw text is directly the assistant response.
> 
>     3. **GPT‑OSS models are aligned to produce “Harmony Response” format**, not plain chat text. When we force JSON via Guided Decoding, the model no longer follows Harmony formatting. As a result, the server-side Harmony handling/decoding layer cannot correctly interpret or assemble the response.
> 
>     4. This mismatch explains the observed symptoms:
>        
>        * **Harmony parse errors** (the response is not valid Harmony anymore)
>        * **hang/stalls** (server-side pipeline waiting for/expecting Harmony-compliant segments)
>        * **`message.parsed == None` / empty result** on the client (because the upstream response is malformed or not finalized correctly)
> 
>     5. We also tried bypassing Harmony parsing and inspecting the **raw constrained output**. The model can roughly follow the JSON shape, but **content quality and consistency are poor**, so this is not a reliable workaround.
> 
>     6. Similar issues have been reported elsewhere (independent confirmation):
>        https://www.glukhov.org/llm-performance/ollama/ollama-gpt-oss-structured-output-issues/
> 
> 
> Preliminary conclusion: this is likely **not a pure openai-python `parse()` client bug**, but a **protocol incompatibility between Harmony Response and JSON-guided decoding** in the current serving stack.
> 
> Hi [@jingyibo123](https://github.com/jingyibo123) ， 当前进展与初步结论如下：
> 
>     1. 我们在最新的 `main` 分支上做了快速验证：总体来看，`client.beta.chat.completions.parse(..., response_format=...)` 所依赖的 **Guided Decoding / 结构化输出约束**机制本身是正常工作的。但在 **GPT‑OSS** 上开启该功能后，模型输出会变得不稳定/混乱，进而导致客户端侧出现空结果或解析失败。
> 
>     2. Guided Decoding 的原理是：通过 **逐 token 约束**来强制模型输出符合目标 schema（这里是 JSON）。这通常隐含一个前提：模型处在“标准 chat 输出模式”，即 assistant 的原始文本可以直接作为响应内容返回。
> 
>     3. **GPT‑OSS 模型对齐的是 “Harmony Response” 格式**，而不是普通的纯文本 chat 输出。当我们用 Guided Decoding 强制输出 JSON 时，模型就不再遵循 Harmony 格式，导致服务端的 Harmony 相关处理/解码层无法正确识别或组装响应。
> 
>     4. 这种不匹配可以解释目前看到的现象：
>        
>        * **Harmony 解析错误**（因为响应不再是合法的 Harmony 格式）
>        * **卡住/挂起**（服务端流水线仍在等待/假设会出现 Harmony 结构片段）
>        * 客户端侧 **`message.parsed == None` / 空结果**（上游响应异常或无法正确结束返回，导致解析拿不到内容）
> 
>     5. 我们也尝试过绕过 Harmony 解析，直接查看 **裸输出**：模型大致能被约束到 JSON 的形式，但 **内容质量和一致性较差**，因此这不是一个可靠的规避方案。
> 
>     6. 其他场景也有人报告过类似问题（可作为旁证）：
>        https://www.glukhov.org/llm-performance/ollama/ollama-gpt-oss-structured-output-issues/
> 
> 
> 初步结论：这很可能 **不是 openai-python `parse()` 的纯客户端 bug**，而是当前服务栈中 **Harmony Response 与 JSON Guided Decoding 之间的协议/模式不兼容**所导致的问题。

Latest findings: **we can enforce structured output without `response_format` by staying in Harmony mode**.

Following the “Structured Output” approach described in the Harmony cookbook (https://developers.openai.com/cookbook/articles/openai-harmony/#structured-output), we can embed a JSON Schema under a `# Response Formats` section in the **system** message, and send a normal `/v1/chat/completions` request from LMDeploy (no `response_format`, no guided decoding).

Example request (LMDeploy):

```bash
➜  ~ curl http://127.0.0.1:23333/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-1234l" \
  -d '{
    "model": "gpt-oss-120b",
    "messages": [
      {
        "role": "system",
        "content": "你是一个编剧，负责设计角色的个人信息.\n\n# Response Formats\n\n{\"$defs\":{\"Character\":{\"additionalProperties\":false,\"properties\":{\"age\":{\"description\":\"角色的年龄\",\"title\":\"Age\",\"type\":\"integer\"},\"comment\":{\"description\":\"你的思考过程，为什么这么设计\",\"title\":\"Comment\",\"type\":\"string\"},\"name\":{\"description\":\"角色的名字\",\"title\":\"Name\",\"type\":\"string\"},\"personality\":{\"description\":\"角色的性格\",\"title\":\"Personality\",\"type\":\"string\"}},\"required\":[\"comment\",\"name\",\"personality\",\"age\"],\"title\":\"Character\",\"type\":\"object\"}},\"additionalProperties\":false,\"properties\":{\"list\":{\"description\":\"多个角色的列表\",\"items\":{\"$ref\":\"#/$defs/Character\"},\"title\":\"List\",\"type\":\"array\"}},\"required\":[\"list\"],\"title\":\"CharacterList\",\"type\":\"object\"}"
      },
      {
        "role": "user",
        "content": "现在设计三个角色。"
      }
    ],
    "stream": false
}'
```

With this method, the model returns a **clean JSON string** in `message.content` matching the schema, while still producing Harmony fields (e.g. `reasoning_content`) as expected. A sample response we observed:

```json
{
  "id": "6",
  "object": "chat.completion",
  "created": 1772273111,
  "model": "gpt-oss-120b",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "{\"list\":[{\"name\":\"林雨薇\",\"age\":28,\"personality\":\"内向而敏感，善于观察，常用笔记记录日常细节，偶尔会在夜深人静时写下诗歌。\",\"comment\":\"我想让林雨薇成为一个在都市中寻找自我价值的普通白领。她的敏感与观察力让她与周围世界产生共鸣，却又因为过于自省而产生孤独感。年龄28岁正好处在人生的十字路口，既有足够的经验，又未被束缚。\"} ,{\"name\":\"周宇航\",\"age\":35,\"personality\":\"外向、乐观，善于社交，喜欢用幽默化解尴尬，偶尔会因过度自信而犯错。\",\"comment\":\"周宇航代表了职场中的“人脉王”。他35岁的成熟与活力兼备，让他在团队中扮演桥梁角色。幽默与自信是他吸引别人的两大武器，但也容易让他忽视细节。\"} ,{\"name\":\"赵蕾\",\"age\":22,\"personality\":\"活泼、直率，热爱冒险，喜欢挑战传统规则，偶尔会因冲动而失去理智。\",\"comment\":\"赵蕾的22岁让她正处在大学毕业后迈向社会的关键阶段。她的直率和冒险精神为故事注入了冲突与张力。她的冲动性格将推动剧情走向意想不到的方向。\"}]}",
        "gen_tokens": null,
        "reasoning_content": "We need to output JSON object with structure per schema. Provide list of 3 Character objects. Each character must have name, age, personality, comment. Provide thoughtful comment. Use Chinese. Ensure no extra properties. Output JSON only.",
        "tool_calls": []
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 255,
    "total_tokens": 663,
    "completion_tokens": 408
  }
}
```

- `message.content`: valid JSON of `CharacterList` with 3 characters
- `finish_reason`: `stop`
- no Harmony parse errors / no hangs

This suggests the earlier failures are specifically tied to **JSON guided decoding (`response_format`) conflicting with Harmony Response**, whereas “Harmony-native structured output” (schema-in-prompt) remains compatible and stable in LMDeploy.

### jingyibo123 · 2026-03-02

Thanks for your effort!!
Indeed, purely prompt guided format output can work. However many existing codebase (dg. opencode, etc) seem to rely on OpenAI `parse` interface resulting in complete failure, thus this issue..

### windreamer · 2026-03-02

> Thanks for your effort!! Indeed, purely prompt guided format output can work. However many existing codebase (dg. opencode, etc) seem to rely on OpenAI `parse` interface resulting in complete failure, thus this issue..

You may try the following diff to transform guided decoding into prompted  guided decoding at server side. This should make your original `parse` script  work for GPT-OSS

```diff
diff --git a/lmdeploy/serve/openai/api_server.py b/lmdeploy/serve/openai/api_server.py
index 3e37caff..f6021bc4 100644
--- a/lmdeploy/serve/openai/api_server.py
+++ b/lmdeploy/serve/openai/api_server.py
@@ -391,10 +391,6 @@ async def chat_completions_v1(request: ChatCompletionRequest, raw_request: Reque
         adapter_name = model_name  # got a adapter name
     request_id = str(session.session_id)
     created_time = int(time.time())
-    gpt_oss_parser = None
-    if VariableInterface.async_engine.arch == 'GptOssForCausalLM':
-        gpt_oss_parser = GptOssChatParser()
-
     if isinstance(request.stop, str):
         request.stop = [request.stop]

@@ -405,6 +401,22 @@ async def chat_completions_v1(request: ChatCompletionRequest, raw_request: Reque
     if request.response_format and request.response_format.type != 'text':
         response_format = request.response_format.model_dump()

+    gpt_oss_parser = None
+    if VariableInterface.async_engine.arch == 'GptOssForCausalLM':
+        gpt_oss_parser = GptOssChatParser()
+        if response_format:
+            messages = request.messages
+            if isinstance(messages, str):
+                messages += f'''\n\n# Response Formats\n\n{json.dumps(response_format, ensure_ascii=False)}'''
+            else:
+                for msg in messages:
+                    if msg['role'] == 'system':
+                        msg['content'] += f'''\n\n# Response Formats\n\n{json.dumps(response_format, ensure_ascii=False)}'''
+                        break
+
+            response_format = None
+
+
     if request.logit_bias is not None:
         try:
             logits_processors = [
```

### jingyibo123 · 2026-03-03

I can confirm with this patch on the latest release, the `openai.chat.parse` interface is working correctly, however command line `curl` example is still blocking, I'm still looking into it...

### JiwaniZakir · 2026-03-27

The `client.beta.chat.completions.parse` method internally sends `response_format={"type": "json_schema", "json_schema": {"schema": ..., "strict": true}}` derived from the Pydantic model, which is distinct from the simpler `{"type": "json_object"}` format. The empty result is likely caused by lmdeploy's OpenAI-compatible server not fully handling the `json_schema` subtype of `response_format` — it may silently discard the field or fall back to unguided generation, after which the OpenAI SDK's `parse` call fails to deserialize the free-form output and returns an empty/`None` parsed value. The relevant handling would be in `lmdeploy/serve/openai/api_server.py` (or `serving_chat.py`) where `response_format` is processed before being passed to the guided-decoding backend. As a workaround, using `client.chat.completions.create` directly with `response_format={"type": "json_object"}` and manually calling `CharacterList.model_validate_json(response.choices[0].message.content)` should produce valid results while the `json_schema` path is unsupported.
