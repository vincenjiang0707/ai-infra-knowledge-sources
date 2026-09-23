# [Issue #4329] [Bug] 基于https://github.com/InternLM/lmdeploy/pull/4320 构建Docker Image，启动GLM-4.7-Flash依然报错

source: https://github.com/InternLM/lmdeploy/issues/4329
state: closed | updated: 2026-08-05T03:35:41Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

我使用最新版代码，包含了https://github.com/InternLM/lmdeploy/pull/4320 的修改，在本地构建了Docker image，但是启动的时候依然报下面的错误。这里面除了需要升级transformer之外，还有哪些地方需要在Dockerfile中需要更新？

You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
2026-02-06 03:02:50,837 - lmdeploy - WARNING - transformers.py:22 - LMDeploy requires transformers version: [4.33.0 ~ 4.57.3], but found version: 4.57.6
2026-02-06 03:02:50,842 - lmdeploy - ERROR - base.py:55 - ValueError: The checkpoint you are trying to load has model type glm4_moe_lite but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

### Reproduction

在lmdeploy中的源码目录中，使用docker目录下的默认Dockerfile执行构建本地的docker image，然后加在glm-4.7

### Environment

```Shell
ubuntu 22.04
glm-4.7-flash
```

### Error traceback

```Shell
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
2026-02-06 03:02:50,837 - lmdeploy - WARNING - transformers.py:22 - LMDeploy requires transformers version: [4.33.0 ~ 4.57.3], but found version: 4.57.6
2026-02-06 03:02:50,842 - lmdeploy - ERROR - base.py:55 - ValueError: The checkpoint you are trying to load has model type glm4_moe_lite but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.
```

## 评论 (9)

### windreamer · 2026-02-06

因为只有 transformers >= 5.0 才支持 glm-4.7-flash 所以您需要升级到 transformers 5.0

注意：当前最新的 release 版本 v0.12.0 不支持  transformers 5.0，但是 main 分支 包含了 #4303 和 #4320  ，所以已经可以在 PytorchEngine 实验性支持  transformers 5.0

### simonjhy · 2026-02-06

但是我已经是基于main分子来构建，而且我在Dockerfile的最后，我还加上了
RUN python3 -m pip install --upgrade git+https://github.com/huggingface/transformers.git

但是还是不生效， 提示

2026-02-06 07:31:09,578 - lmdeploy - WARNING - tokenizer.py:89 - The current version of `transformers` is transformers==4.57.6, which is lower than the required version transformers==5.0.0rc0. Please upgrade to the required version.
The tokenizer you are loading from '/models/GLM-4.7-Flash' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
2026-02-06 07:31:23,620 - lmdeploy - WARNING - transformers.py:22 - LMDeploy requires transformers version: [4.33.0 ~ 4.57.3], but found version: 4.57.6
2026-02-06 07:31:23,624 - lmdeploy - ERROR - base.py:55 - ValueError: The checkpoint you are trying to load has model type `glm4_moe_lite` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git`
2026-02-06 07:31:23,624 - lmdeploy - ERROR - base.py:56 - <transformers> check failed!
Load model config with transformers==4.57.6 failed. Please make sure model can be loaded with transformers API.



### simonjhy · 2026-02-06

我是需要在install.sh中来安装这个transformer吗？


### windreamer · 2026-02-06

你可以试试这样修改：

```diff
diff --git a/requirements/runtime_cuda.txt b/requirements/runtime_cuda.txt
index c55b6646..03376695 100644
--- a/requirements/runtime_cuda.txt
+++ b/requirements/runtime_cuda.txt
@@ -23,7 +23,7 @@ shortuuid
 tiktoken
 torch<=2.8.0,>=2.0.0
 torchvision<=0.23.0,>=0.15.0
-transformers<5.0.0
+transformers
 triton<=3.4.0,>=3.0.0; sys_platform == "linux" and "aarch64" not in platform_machine and "arm" not in platform_machine
 uvicorn
 xgrammar
```

安装 lmdeploy 后 用 `lmdeploy check_env` 来检查 lmdeploy 环境是不是正确，其中应该会显示lmdeploy 看到的 transformers 版本

### simonjhy · 2026-02-09

咱们官方的基于turbomind加速的版本什么时候能推出，期待啊

### simonjhy · 2026-02-09

我今天使用了官方刚刚发布不的最新额docker image，依然不支持glm-4.7-flash的模型


soft@AI:/data/ai/dockers/composes/glm-4.7-flash-lmdeploy$ docker logs -f lmdeploy-glm-4.7-1
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
2026-02-09 13:57:56,777 - lmdeploy - WARNING - archs.py:45 - Fallback to pytorch engine because `/models/GLM-4.7-Flash` not supported by turbomind engine.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
The tokenizer you are loading from '/models/GLM-4.7-Flash' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
The tokenizer you are loading from '/models/GLM-4.7-Flash' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
2026-02-09 13:58:19,068 - lmdeploy - WARNING - tokenizer.py:89 - The current version of `transformers` is transformers==4.57.6, which is lower than the required version transformers==5.0.0rc0. Please upgrade to the required version.
The tokenizer you are loading from '/models/GLM-4.7-Flash' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
The argument `trust_remote_code` is to be used with Auto classes. It has no effect here and is ignored.
You are using a model of type glm4_moe_lite to instantiate a model of type . This is not supported for all configurations of models and can yield errors.
2026-02-09 13:59:17,105 - lmdeploy - WARNING - transformers.py:22 - LMDeploy requires transformers version: [4.33.0 ~ 4.57.3], but found version: 4.57.6
2026-02-09 13:59:17,123 - lmdeploy - ERROR - base.py:55 - ValueError: The checkpoint you are trying to load has model type `glm4_moe_lite` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git`
2026-02-09 13:59:17,124 - lmdeploy - ERROR - base.py:56 - <transformers> check failed!
Load model config with transformers==4.57.6 failed. Please make sure model can be loaded with transformers API.

### 470335075 · 2026-02-09

最新额docker image，依然不支持glm-4.7-flash的模型，我刚试完

### simonjhy · 2026-03-10

非常感谢提供的glm-4.7的加速引擎!!!!!!

但是实际使用的时候发现了一些问题
1）
我在测试的时候发现日志中提示
2026-03-09 07:57:19,727 - lmdeploy - ERROR - turbomind.py:764 - internal error. status_code 6
2026-03-09 07:57:19,727 - lmdeploy - ERROR - async_engine.py:519 - session 88 finished, ResponseType.INPUT_LENGTH_ERROR, reason "error"

这个是什么错误？需要设置什么参数来控制的吗?

2）
这个glm-4.7在vllm中使用时候的下面这些参数
--tool-call-parser glm47
--reasoning-parser glm45
--enable-auto-tool-choice \

在lmdeploy加载的时候需要使用什么参数？这两个在lmdeploy中如何调用

3）
而且我在运行的时候，总是出现[TM][WARNING] [ProcessInferRequests] [2] total sequence length (12817 + 183791) exceeds session_len (42880), max_new_tokens is truncated to 30063，我如何配置才能避免生成的token不被truncated

4）
另外在opencode和claudecode中使用这个lmdeploy加载的glm-4.7-flash，均出现无法识别模型的情况，但是通过web接口访问时候没有问题。应该是需要的某些api接口lmdeploy中无法提供，导致识别不出来相应的模型

恳请指导：如何解决在本地部署的问题

### lvhan028 · 2026-03-22

1）表示输入长度已经超过了 session_len 或者引擎 token 容量的上界
2）glm4.7 的 reasoning parser、tool call parser 还没有加
3）调低 session_len。运行命令可以增加 --log-level INFO 能看到引擎输出的 token 容量最大值
4）接入opencode、claudecode 的方式我们还没有学习过
