source: https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/integrated_machine_deploy

# DeepSeek 一体机部署-单机部署

本节介绍利用**musa-deploy**工具在单台服务器快速部署大模型推理服务的步骤。单机大模型推理服务是基于摩尔线程推出的[vLLM-MTT](https://docs.mthreads.com/mtt/mtt-doc-online/)产品部署的，详细的产品��介绍以及部署步骤请参考[vLLM-MTT](https://docs.mthreads.com/mtt/mtt-doc-online/)页面。

阅读本章节前，建议用户先仔细阅读前面[demo](https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/user_guide/demo)章节。

## 启动命令[](https://docs.mthreads.com#启动命令)

用户可以通过执行以下命令快速启动：

`sudo musa-deploy --demo vllm --task <model_name> [其他参数]`



更多参数含义讲解，参看

[demo]章节

当前支持的部分热门模型及其 Tensor Parallel 配置示例如下：

| Model | Tensor Parallel Size |
|---|---|
| deepSeek-r1-distill-qwen-1.5b | 1 |
| deepseek-r1-distill-llama-70b | 4 8 |
| deepSeek-r1-distill-qwen-32b | 2 4 |

注：


- 上表仅列举部分模型示例，可支持的完整模型列表参看
[vllm-demo]中`--task`

参数讲解。

## 常用命令示例[](https://docs.mthreads.com#常用命令示例)

### 1. 支持在线下载模型[](https://docs.mthreads.com#1-支持在线下载模型)

如果本地没有模型，工具会自动下载模型，并存放到目录映射的宿主机目录，若无 `-v`

映射，会下载到容器 `/musa_depeloy_xxx`

目录下。

如果模型文件较大，建议用户提前下载好，通过`-v`

映射到容器内。

`sudo musa-deploy --demo vllm --task deepSeek-r1-distill-qwen-1.5B -v /data/mtt:/data/mtt`



### 2. 支持模型权重自动转换[](https://docs.mthreads.com#2-支持模型权重自动转换)

从 modelscope 或者 huggingface 下载的原始模型权重，需要经过模型文件格式转换，才能被[vLLM-MTT](https://docs.mthreads.com/mtt/mtt-doc-online/) 读取来进行推理服务。**musa-deploy** 工具在拉起服务时可以自动完成模型文件格式转换。用户通过`--model`

指定原始模型路径即可，工具会自动将该路径映射进容器内部。

`sudo musa-deploy --demo vllm --task deepSeek-r1-distill-qwen-1.5B --model /mnt/cephfs/deepSeek-r1-distill-qwen-1.5B/ `



### 3. 支持直接指定格式转换后的权重模型[](https://docs.mthreads.com#3-支持直接指定格式转换后的权重模型)

如果本地已经存在权重格式转化后的模型文件，那么可以通过`--converted-model`

参数指定转换后的模型文件路径，指定后工具会跳过模型转换，直接开始部署推理服务。

`sudo musa-deploy --demo vllm --task deepSeek-r1-distill-qwen-1.5B --converted-model /mnt/cephfs/deepSeek-r1-distill-qwen-1.5B-tp1-converted/ `



### 4. 支持指定 Tensor Parallel Size 参数[](https://docs.mthreads.com#4-支持指定-tensor-parallel-size-参数)

可以指定模型推理服务用��到的 GPU 卡数。若未指定，则默认为上面支持列表中的最大值。建议用户在部署时手动指定该参数。

`sudo musa-deploy --demo vllm --task deepSeek-r1-distill-qwen-32b --model /mnt/cephfs/deepseek-r1-distill-qwen-32b --tensor-parallel-size 2`



注：


`--tensor-parallel-size`

参数会作用于模型转化过程，如果指定为 2, 会自动生成权重转化后模型路径:`/mnt/cephfs/deepseek-r1-distill-qwen-32b-tp2-converted`

，该路径只能用于 2 卡推理。故参数`--tensor-parallel-size`

和`--converted-model`

不能同时指定；- 模型默认按照 0 -> 8 号的顺序占用 GPU 卡，故可以先用命令
`mthreads-gmi`

查看当前机器 GPUs 使用情况。

### 5. 支持启动 Web UI 前端界面[](https://docs.mthreads.com#5-支持启动-web-ui-前端界面)

`sudo musa-deploy --demo vllm --task deepseek-r1-distill-qwen-32b --model /mnt/cephfs/deepseek-r1-distill-qwen-32b --tensor-parallel-size 2 --webui`



后端服务开启后会给出一个 URL, 在浏览器中打开，示例效果如下：