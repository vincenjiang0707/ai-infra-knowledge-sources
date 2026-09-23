source: https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/demo

# Demo

使能 demo 功能时，该工具可以以 docker 容器方式一键拉起内置 AI demo。拉起 demo 过程中，工具会自动检测并安装必须的依赖包，避免用户依次手动安装依赖。demo 功能非常实用，建议用户关注 demo 的使用方法以及 demo 模块的更新。 demo 的使用方式如下：

`sudo musa-deploy --demo <DemoType>[==Version] [--task <TaskName>] [参数...]`



当前支持的 **DemoType** 有：

| DemoType | CPU | OS | GPU | Version | Intruction |
|---|---|---|---|---|---|
| torch_musa | Intel | Ubuntu | S80 X300 S4000 | 1.3.0 | 提供基础 torch_musa 容器环境（详看：
|

[MTT-vLLM用户服务指南](https://docs.mthreads.com/mtt/mtt-doc-online/)）0.8.4

[https://docs.mthreads.com/vllm-musa/vllm-musa-doc-online/intro/](https://docs.mthreads.com/vllm-musa/vllm-musa-doc-online/intro/))X300

[基于Ollama框架的 DeepSeek-R1 蒸馏版模型推理](https://blog.mthreads.com/blog/AI/2025-02-17-deepseek/)）### 1. docker 参数支持[](https://docs.mthreads.com#1-docker-参数支持)

使用 musa-deploy 工具拉起容器时，支持灵活配置 Docker 参数，以满足不同场景需求。支持方式分为两类：

#### 1.1 常用参数直通支持[](https://docs.mthreads.com#11-常用参数直通支持)

musa-deploy 直接支持一系列常用的 docker run 参数，调用方式与原始 Docker 命令保持一致，包括：--name, -v, --pid, --network, --port, -w。
👉 [Docker run 官方参数说明](https://docs.docker.com/engine/containers/run/)

**示例**：通过以下命令拉起名为 torch_musa_test 的容器，并挂载本地目录、配置网络与 PID 命名空间：

`sudo musa-deploy --demo torch_musa --name torch_musa_test -v /home/ggn:/home/ggn --network host --pid host `



#### 1.2 其他参数透传支持[](https://docs.mthreads.com#12-其他参数透传支持)

对于未被 musa-deploy 明确支持的 Docker 参数，可通过 --docker-para=`<docker参数>`

形式传入，原样附加到最终的容器启动命令中，便于高级自定义。

**示例**：仅启用第 2,3,4,5,6 张 MUSA 卡运行 vllm_musa 容器：

`sudo musa-deploy --demo vllm_musa --docker-para="-e MUSA_VISIBLE_DEVICES=2,3,4,5,6"`



📝 提示：执行过程中，完整的 docker run 命令会显示在终端，方便你查看或进一步定制。


### 2. torch_musa/kuae Demo[](https://docs.mthreads.com#2-torch_musakuae-demo)

| demo | task |
|---|---|
| torch_musa kuae | [缺省] train_cifar10 |

注：


- 若当前机器未安装 driver，工具将自动下载并安装对应版本的 driver。驱动安装后需重启机器，重启完成后可重复执行上一次
`musa-deploy`

命令来拉起demo；- 若当前已安装 driver，但和 demo 要求的版本不匹配，程序将自动退出。可在命令中增加
`-f/--force`

参数强制更新驱动，或者手动卸载现有 driver 后重新执行命令;- 当 task 缺省时，会基于 torch_musa/kuae 镜像启动一个基础容器，不执行任务;
- 当 task 指定为
`train_cifar10`

，会拉起容器并启动训练`CIFAR-10`

任务。

示例命令以及示例执行截图如下：

`sudo musa-deploy --demo torch_musa --task train_cifar10`



### 3. vLLM Demo[](https://docs.mthreads.com#3-vllm-demo)

#### 3.1 参数说明[](https://docs.mthreads.com#31-参数说明)

| 参数 | 类型 | 是否必填 | 说明 |
|---|---|---|---|
`--task` | 模型名 | 否 | 指定要运行的模型名(小写全称)，如：qwen2.5-0.5b-instruct，deepseek-r1-distill-llama-70b，deepseek-r1-distill-qwen-32b，支持模型列表：
|

`--model`

`--converted-model`

`--tensor-patallel-size`

/`--tp-size`

`--webui`


`--task`

参数是其他参数生效的前提，必须优先指定；- 若未指定
`--model`

和`--converted-model`

参数，将默认在线下载模型至容器内。若挂载了宿主机目录（通过`-v`

），模型将保存至宿主机指定目录。

`sudo musa-deploy --demo vllm[==version] \`

--task <model_name> \

[--model <origin_model_path>] \

[--converted-model <converted_model_path>] \

[--image <image_name>] \

[--tensor-parallel-size|--tp-size <gpu_nums>] \

[--webui]



示例命令以及示例截图如下。示例代码中没有指定模型路径，工具会在容器中自动下载模型文件，并转换成 MTT 推理引擎识别的文件格式。对于模型文件比较大的模型，建议用户提前下载好，通过参数指定好模型路径。

`musa-deploy --demo vllm --task qwen2.5-0.5b-instruct`



### 4. vllm_musa Demo[](https://docs.mthreads.com#4-vllm_musa-demo)

通过 musa-deploy 工具，用户可以一键部署基于 vllm_musa 实现的大模型推理服务。

**命令格式**：

`sudo musa-deploy --demo vllm_musa[==version] \`

[--model <model_path> \

[-a="<vllm_args>"] \

[--webui]] \

[-f] \

[other_args]



#### 4.1 参数说明[](https://docs.mthreads.com#41-参数说明)

| 参数 | 类型 | 是否必填 | 说明 |
|---|---|---|---|
`--task` | 固定值 | 否 | 当前仅支持 single，表示单节点推理服务部署 |
`--model` | 路径 | 否 | 模型文件路径，仅支持加载本地离线模型（路径会自动映射到容器中） |
`-a` , `--extra-args` | 字符串 | 否 | 传递给 `vllm serve` 的额外 CLI 参数, 如 `-a="-tp 8 -pp 1"` (注意 )`=` 不可省略 |
`--webui` | \ | 否 | 启用基于 Gradio 的 Web UI，容器网络自动设置为 host 模式 |
`-f` , `--force` | \ | 否 | 当demo要求的驱动版本不匹配时，加上此参数可以自动更新驱动，否则退出 demo 构建（更新驱动会重启机器，重启完之后重新执行命令） |

#### 4.2 快速启动示例[](https://docs.mthreads.com#42-快速启动示例)

以下命令将部署基于 QwQ-32B 模型的 8 卡 vLLM 推理服务，并启动 Web UI 界面：

`sudo musa-deploy --demo vllm_musa --name qwq_32b_vllm --task single --model /data/models/Qwen/QwQ-32B/ -a="-tp 8" --webui`



更多示例，参见：[vllm_musa 快速部署大模型推理服务示例](https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/integrated_machine_deploy_vllm_musa)

### 5. ollama Demo[](https://docs.mthreads.com#5-ollama-demo)

使用示例：

`sudo musa-deploy --demo ollama -f`



暂不支持

`task`

功能