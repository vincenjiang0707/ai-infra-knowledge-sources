# [Issue #4536] [Bug] 咱们v0.12.3-cu128版本镜像支持 “--tool-call-parser glm47”参数吗？

source: https://github.com/InternLM/lmdeploy/issues/4536
state: closed | updated: 2026-04-18T14:56:40Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

咱们v0.12.3-cu128版本镜像支持 “--tool-call-parser glm47”参数吗？但是文档里现已经说支持了啊，是我的哪个地方配置的不对吗？我看到你们文档里写的也都是加的这个--tool-call-parser

# Using GLM-4.7-Flash model on HuggingFace
lmdeploy serve api_server THUDM/glm4-7b-flash --tool-call-parser glm47 --tp 2

# Using a locally converted TurboMind model
lmdeploy serve api_server /path/to/glm47_turbomind --tool-call-parser glm47 --tp 4

**### 我看到在lmdeploy/serve/openai/.tool_parser的_init_.py中完全没有添加对glm的支持？是这个glm4_parser.py（Glm47ToolParser）接口还有bug吗？

__all__ = [
    'Internlm2ToolParser',
    'Qwen2d5ToolParser',
    'Qwen3ToolParser',
    'Qwen3CoderToolParser',
    'ToolParser',
    'ToolParserManager',
    'Llama3JsonToolParser',
]**




######################################################################################



2026-04-18 08:56:04,190 - lmdeploy - INFO - async_engine.py:195 - enable metrics, with dp: 1 dp_rank: 0
Traceback (most recent call last):
  File "/opt/py3/bin/lmdeploy", line 6, in <module>
NCCL version 2.29.7+cuda12.9
    sys.exit(run())
             ^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/cli/entrypoint.py", line 39, in run
    args.run(args)
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/cli/serve.py", line 284, in api_server
    run_api_server(
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/serve/openai/api_server.py", line 1505, in serve
    set_parsers(reasoning_parser, tool_call_parser)
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/serve/openai/api_server.py", line 1348, in set_parsers
    raise ValueError(
ValueError: The reasoning parser glm47 is not in the parser list: dict_keys(['internlm', 'intern-s1', 'llama3', 'qwen2d5', 'qwen', 'qwen3', 'qwen3coder'])


### Reproduction

使用openmmlab/lmdeploy:v0.12.3-cu12.8版本镜像 

设置     
      --communicator nccl
      --tool-call-parser glm47
      --backend turbomind

启动的时候就提上上面错误，但是我看到

我已经创建了基于 vLLM/SGLang 标准格式的 GLM-4.7 工具调用解析器。

## 🚀 快速开始

### 1. 启动 API 服务器

```bash
lmdeploy serve api_server THUDM/glm4-7b-flash \
    --tp 2 \
    --tool-call-parser glm47


### Environment

```Shell
ubuntu 2204
```

### Error traceback

```Shell
2026-04-18 08:56:04,190 - lmdeploy - INFO - async_engine.py:195 - enable metrics, with dp: 1 dp_rank: 0
Traceback (most recent call last):
  File "/opt/py3/bin/lmdeploy", line 6, in <module>
NCCL version 2.29.7+cuda12.9
    sys.exit(run())
             ^^^^^
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/cli/entrypoint.py", line 39, in run
    args.run(args)
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/cli/serve.py", line 284, in api_server
    run_api_server(
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/serve/openai/api_server.py", line 1505, in serve
    set_parsers(reasoning_parser, tool_call_parser)
  File "/opt/py3/lib/python3.12/site-packages/lmdeploy/serve/openai/api_server.py", line 1348, in set_parsers
    raise ValueError(
ValueError: The reasoning parser glm47 is not in the parser list: dict_keys(['internlm', 'intern-s1', 'llama3', 'qwen2d5', 'qwen', 'qwen3', 'qwen3coder'])
```

## 评论 (3)

### lvhan028 · 2026-04-18

ValueError: The reasoning parser glm47 is not in the parser list: dict_keys(['internlm', 'intern-s1', 'llama3', 'qwen2d5', 'qwen', 'qwen3', 'qwen3coder'])
这个list中列出来的是支持的 reasoning parser。
如果有哪个文档中说明支持了 glm47，麻烦告知文档名

### simonjhy · 2026-04-18

我是看到GLM4_PARSER_SUMMARY.md里说的，我还以为开始支持了呢，如果还不支持那我就关了这个issue。

### lvhan028 · 2026-04-18

LMDeploy中没有 GLM4_PARSER_SUMMARY.md
