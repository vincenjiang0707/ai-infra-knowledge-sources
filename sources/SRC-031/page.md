# MindIE 调优

source: https://www.hiascend.com/document/detail/zh/mindie/230/mindiellm/llmdev/mindie_llm0526.html

# 服务化接口介绍

#### 场景说明

Server提供EndPoint模块对推理服务化协议和接口封装，兼容Triton/OpenAI/TGI/vLLM等第三方框架接口。使用单节点安装模式安装Server之后，用户使用客户端（Linux curl命令，Postman工具等）发送HTTP/HTTPS请求，即可调用EndPoint提供的接口。

HTTP协议存在安全风险，建议您使用HTTPS安全协议。

#### EndPoint RESTful接口使用说明

HTTP/HTTPS请求的URL的IP地址和端口号在config.json中进行配置，详情请参见[ServerConfig参数说明](https://www.hiascend.com/mindie_service0285.html#ZH-CN_TOPIC_0000002501059508__zh-cn_topic_0000002108800077_section6101152962011)。

- 以Linux curl工具发送generate请求，URL请求格式如下：
- 操作类型：
**POST** **URL：http***[**s]*://*{ip}:{port}***/generate**

- 操作类型：
- 未开启HTTPS，发送推理请求：
curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{ "inputs": "My name is Olivier and I", "parameters": { "details": true, "do_sample": true, "repetition_penalty": 1.1, "return_full_text": false, "seed": null, "temperature": 1, "top_p": 0.99 } }' http://

*{ip}:{port}*/generate - HTTPS双向认证的请求方式示例：
curl --location --request POST 'https://

*{ip}:{port}*/generate' \ --header 'Content-Type: application/json' \ --cacert*/home/runs/static_conf/ca/ca.pem*\ --cert*/home/runs/static_conf/cert/client.pem*\ --key*/home/runs/static_conf/cert/client.key.pem*\ --data-raw '{ "inputs": "My name is Olivier and I", "parameters": { "best_of": 1, "decoder_input_details": false, "details": false, "do_sample": true, "max_new_tokens": 20, "repetition_penalty": 2, "return_full_text": false, "seed": 12, "temperature": 0.1, "top_k": 1, "top_p": 0.9, "truncate": 1024 } }'- --cacert：验签证书文件路径。
- ca.pem：Server的验签证书/根证书。
- --cert：客户端证书文件路径。
- client.pem：客户端证书。
- --key：客户端私钥文件路径。
- client.key.pem：客户端证书私钥（未加密，建议采用加密密钥）。

请用户根据实际情况对相应参数进行修改。


API |
接口类型 |
URL |
说明 |
支持框架 |
|---|---|---|---|---|
Server Live |
GET |
/v2/health/live |
检查服务器是否在线。 |
Triton |
Server Ready |
GET |
/v2/health/ready |
检查服务器是否准备就绪。 |
Triton |
Model Ready |
GET |
/v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]/ready |
检查模型是否准备就绪。 |
Triton |
health |
GET |
/health |
服务健康检查。 |
|
查询TGI EndPoint信息 |
GET |
/info |
查询TGI EndPoint信息。 |
TGI |
Slot统计 |
GET |
/v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]/getSlotCount |
参考Triton格式，自定义的Slot统计信息查询接口。 |
原生 |
健康探针接口 |
GET |
/health/timed[-${TIMEOUT}] |
检查推理流程是否正常。 |
原生 |
优雅退出接口 |
GET |
/stopService |
实现整个服务的优雅退出。调用该接口时，会等待服务中正在执行和等待的所有请求完成，并关闭服务，等待时所有推理接口将不可用。 |
原生 |
静态配置采集接口 |
GET |
/v1/config |
采集静态配置。 |
原生 |
动态状态采集接口 |
GET |
/v1/status |
采集动态状态。 |
原生 |
指定实例身份接口 |
POST |
/v1/role/${role} |
指定实例身份。 |
原生 |
动态状态采集接口 |
GET |
/v2/status |
采集动态状态。 |
原生 |
指定实例身份接口 |
POST |
/v2/role/${role} |
指定实例身份。 |
原生 |
服务指标接口（JSON格式） |
GET |
/metrics-json |
获取推理服务过程中请求的TTFT（Time To First Token）、TBT（Time Between Tokens）的动态平均值（默认近1000个请求的平均值），正在执行请求数、正在等待请求数量、剩余NPUblock数量。 |
原生 |
服务管控指标查询接口（普罗格式） |
GET |
/metrics |
查询推理服务化的相关服务管控指标 |
原生 |
动态加载lora接口 |
POST |
/v1/load_lora_adapter |
动态加载lora |
OpenAI |
动态卸载lora接口 |
POST |
/v1/unload_lora_adapter |
动态卸载lora |
OpenAI |

API |
接口类型 |
URL |
说明 |
支持框架 |
|---|---|---|---|---|
models列表 |
GET |
/v1/models |
列举当前可用模型列表。 |
OpenAI |
model详情 |
GET |
/v1/models/{model} |
查询模型信息。 |
OpenAI |
服务元数据查询 |
GET |
/v2 |
获取服务元数据。 |
Triton |
模型元数据查询 |
GET |
/v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}] |
查询模型元数据信息。 |
Triton |
查询模型配置 |
GET |
/v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]/config |
查询模型配置。 |
Triton |

API |
接口类型 |
URL |
说明 |
支持框架 |
|---|---|---|---|---|
推理任务 |
POST |
/ |
TGI推理接口，stream==false返回文本推理结果，stream==true返回流式推理结果。 |
TGI |
POST |
/generate |
TGI和vLLM的推理接口，通过请求参数来区分是哪种服务的接口。 |
|
|
POST |
/generate_stream |
TGI流式推理接口，使用Server-Sent Events格式返回结果。 |
TGI |
|
POST |
/v1/chat/completions |
OpenAI文本/流式推理接口。 |
OpenAI |
|
POST |
/v1/completions |
vLLM兼容OpenAI文本/流式推理接口。 |
OpenAI |
|
POST |
/infer |
原生推理接口，支持文本/流式返回结果。 |
原生 |
|
POST |
/infer_token |
原生推理接口，实现token输入的文本/流式推理。 |
原生 |
|
POST |
/v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]/infer |
Triton的token推理接口。 |
Triton |
|
POST |
/v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]/stopInfer |
参考Triton接口定义，提供提前终止请求接口。 |
原生 |
|
POST |
/v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]/generate |
Triton文本推理接口。 |
Triton |
|
POST |
/v2/models/${MODEL_NAME}[/versions/${MODEL_VERSION}]/generate_stream |
Triton流式推理接口。 |
Triton |
|
POST |
/v1/tokenizer |
计算token数量。 |
原生 |
|
GET |
/dresult |
调度器与D实例间，存在一个长连接，D实例每推理出一个结果，就通过该长连接响应给调度器。 |
PD分离相关 |

- ${MODEL_NAME}字段指定需要查询的模型名称。
- [/versions/${MODEL_VERSION}]字段暂不支持，不传递。

**父主题：**

[在线服务化](https://www.hiascend.com/mindie_llm0519.html)


# 概述

Prefill&Decode混合服务部署（简称：PD混合服务部署），指单个MindIE LLM的服务既能处理Prefill阶段又能处理Decode阶段的推理任务。该部署方式通常适用于时延不敏感的场景。

目前支持PD混部单机服务部署和PD混部多机服务部署：

- PD混部单机服务部署：Server运行在单个服务器上，适用于单个服务器部署模型的场景。
- PD混部多机服务部署：Server运行在多个独立的机器上，适用于多个服务器部署模型的场景。

**父主题：**

[PD混合服务部署](https://www.hiascend.com/mindie_llm0521.html)


# ATB Models纯模型使用

#### 前提条件

已在环境上安装CANN、PyTorch、Torch-NPU和ATB Models，详情请参见《[MindIE安装指南](https://www.hiascend.com/document/detail/zh/mindie/230/envdeployment/instg/mindie_instg_0001.html)》。

本次样例参考以下安装路径进行：

安装ATB Models并初始化ATB Models环境变量。模型仓库set_env.sh脚本中有初始化“${ATB_SPEED_HOME_PATH}”环境变量的操作，所以source模型仓库中set_env.sh脚本时会同时初始化“${ATB_SPEED_HOME_PATH}”环境变量。

#### 约束

- 使用ATB Models进行推理，模型初始化失败时，模型初始化过程中用户自定义修改导致的失败，需要手动结束进程。
- 使用ATB Models进行推理，权重路径及文件的权限需保证其他用户无写权限。

#### README文档解读

当前ATB Models包含三类Readme文档指导您执行推理流程，了解模型支持特性以及提供基础的调测和问题定位手段。

**图1**ATB Models Readme文档关系示意图

文档名称 |
作用 |
内容 |
|---|---|---|
“${ATB_SPEED_HOME_PATH}/README.md” |
为ATB Models所有文档的总入口。 |
|
“${ATB_SPEED_HOME_PATH}/examples/models/{模型名称}/README.md” |
为ATB Models每个模型各自的文档，例如：“${ATB_SPEED_HOME_PATH}/examples/models/llama/README.md”中为LLaMA模型的文档，其中涵盖了LLaMA系列和LLaMA2系列模型的介绍和运行指导。 |
|
“${ATB_SPEED_HOME_PATH}/examples/README.md” |
汇总了对于公共能力和接口的介绍。 |
|

#### 使用示例

下面以LLaMA3-8B模型为例，展示对话推理以及性能测试的执行步骤。

- 配置环境变量。
1 2 3 4 5 6

# 配置CANN环境，默认安装在/usr/local目录下 source /usr/local/Ascend/cann/set_env.sh # 配置加速库环境 source /usr/local/Ascend/nnal/atb/set_env.sh # 配置模型仓库环境变量 source /usr/local/Ascend/atb-models/set_env.sh

- 准备模型权重：可从Hugging Face官网直接下载，将下载的权重保存在“/data/Llama-3-8b”。
- 执行如下命令，修改权重文件权限。
chmod -R 755 /data/Llama-3-8b

- （可选）当前ATB Models推理仅支持加载safetensor格式的权重文件。若下载的权重文件是safetensor格式文件，则无需进行权重转换，若下载的权重文件是bin格式文件，则需要按照如下方式进行转换。
1 2 3 4

# 进入ATB Models 所在路径 cd ${ATB_SPEED_HOME_PATH} # 执行脚本生成safetensor格式的权重 python examples/convert/convert_weights.py --model_path /data/Llama-3-8b

输出结果会保存在bin格式的权重文件同目录下。

- 测试对话推理。
1 2

cd ${ATB_SPEED_HOME_PATH} bash examples/models/llama/run_pa.sh /data/Llama-3-8b

如上命令调用的run_pa.sh脚本是对run_pa.py脚本的封装，默认推理内容为"What's deep learning?"，batch size为1，可以通过

[6](https://www.hiascend.com#ZH-CN_TOPIC_0000002500899618__li436715716254)修改推理内容。 [自定义推理内容。]- 用户可以通过以下方式直接调用run_pa.py脚本，通过传入参数的方式自定义推理内容及推理方式。
[例如：使用/data/Llama-3-8b路径下的权重，使用8卡推理"What's deep learning?"和"Hello World."，推理时batch size为2。]1 2 3 4

# 指定当前机器上可用的逻辑NPU核心，多个核心间使用逗号相连 export ASCEND_RT_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 # 执行推理 torchrun --nproc_per_node 8 --master_port 20030 -m examples.run_pa --model_path /data/Llama-3-8b --input_texts "What's deep learning?" "Hello World." --max_batch_size 2

说明环境变量说明见

[环境变量说明](https://www.hiascend.com/mindie_llm0416.html)。 - 用户可以通过传入Token id的方式进行推理。
[新建一个py脚本（如test.py）用于生成Token id：]from transformers import AutoTokenizer tokenizer = AutoTokenizer.from_pretrained( pretrained_model_name_or_path="{

*tokenizer所在的文件夹路径*}", use_fast=False, padding_side='left', trust_remote_code="{*用户输入的trust_remote_code值*}") inputs = tokenizer("What's deep learning?", return_tensors="pt") token_id = inputs.data["input_ids"] print(token_id)执行如下命令，生成Token id：

python

*test*.py执行如下命令进行推理，如下以生成的第一个推理内容对应的Token id为"1,15043,2787"，第二个推理内容对应的Token id为"1,306,626,2691"为例，其中推理内容间以空格分开。# 执行推理 torchrun --nproc_per_node 8 --master_port 20030 -m examples.run_pa --model_path /data/Llama-3-8b --input_ids 1,15043,2787 1,306,626,2691 --max_batch_size 2


**表2**run_pa.py脚本参数说明参数名称

是否为必选

类型

默认值

描述

--model_path

是

string

""

模型权重路径。

该路径会进行安全校验，必须使用绝对路径，且和执行推理用户的属组和权限保持一致。

--input_texts

否

string

"What's deep learning?"

推理文本或推理文本路径，多条推理文本间使用空格分割。

--input_ids

否

string

None

推理文本经过模型分词器处理后得到的token id列表，多条推理请求间使用空格分割，单个推理请求内每个token使用逗号隔开。

--input_file

否

string

None

仅支持jsonl格式文件，每一行必须为List[Dict]格式的按时间顺序排序的对话数据，每个Dict字典中需要至少包含"role"和"content"两个字段。

--input_dict

否

parse_list_of_json

None

推理文本以及对应的adapter名称。格式形如：'[{"prompt": "A robe takes 2 bolts of blue fiber and half that much white fiber. How many bolts in total does it take?", "adapter": "adapter1"}, {"prompt": "What is deep learning?", "adapter": "base"}]'

--max_prefill_batch_size

否

int或者None

None

模型推理最大Prefill Batch Size。

--max_position_embeddings

否

int或者None

None

模型可接受的最大上下文长度。当此值为None时，则从模型权重文件中读取。

--max_input_length

否

int

1024

推理文本最大token数。

--max_output_length

否

int

20

推理结果最大token数。

--max_prefill_tokens

否

int

-1

模型Prefill推理阶段最大可接受的token数。若输入为-1，则max_prefill_tokens = max_batch_size * (max_input_length + max_output_length)

--max_batch_size

否

int

1

模型推理最大batch size。

--block_size

否

int

128

KV Cache分块存储，每块存储的最大token数，默认为128。

--chat_template

否

string或者None

None

对话模型的prompt模板。

--ignore_eos

否

bool

store_true

当推理结果中遇到eos token（句子结束标识符）时，是否结束推理。若传入此参数，则忽略eos token。

--is_chat_model

否

bool

store_true

是否支持对话模式。若传入此参数，则进入对话模式。

--is_embedding_model

否

bool

store_true

是否为embedding类模型。默认为因果推断类模型，若传入此参数，则为embedding类模型。

--load_tokenizer

否

bool

True

是否加载tokenizer。若传入False，则必须传入input_ids参数，且推理输出为token id。

--enable_atb_torch

否

bool

store_true

是否使用Python组图。默认使用C++组图，若传入此参数，则使用Python组图。

--kw_args

否

string

""

扩展参数，支持用户通过扩展参数进行功能扩展。

--trust_remote_code

否

bool

store_true

是否信任模型权重路径下的自定义代码文件。默认不执行。若传入此参数，则transformers会执行用户权重路径下的自定义代码文件，这些代码文件的功能的安全性需由用户保证，请提前做好安全性检查。

--dp

否

int

-1

数据并行数，默认不进行数据并行。

--tp

否

int

-1

整网张量并行数，若值为“-1”，默认张量并行数为worldSize值。

--sp

否

int

-1

序列并行数，默认不进行序列并行。若开启序列并行数，一般与张量并行数保持一致。

--cp

否

int

-1

文本并行数，默认不进行文本并行。

--moe_tp

否

int

-1

稀疏模型MoE模块中的张量并行数，默认等于“tp”数。若同时配置“tp”参数，则“moe_tp”参数优先级高于“tp”参数。

--moe_ep

否

int

-1

稀疏模型MoE模块中的专家并行数，默认无专家并行。

--lora_modules

否

string

None

定义需要加载的Lora权重名以及对应的Lora权重路径。例如：'{"adapter1": "/path/to/lora1", "adapter2": "/path/to/lora2"}'。默认不加载Lora权重。

--max_loras

否

int

0

LoRA场景中，定义最多可存储的LoRA数量。动态LoRA场景下必须配置，静态LoRA场景中可以不配置。若传入数值过大，由于预留了过多权重空间，会出现out_of_memory报错信息，例如: "RuntimeError: NPU out of memory. Tried to allocate xxx GiB."

--max_lora_rank

否

int

0

动态加载卸载LoRA场景中，定义最大LoRA秩。动态LoRA场景下必须配置，静态LoRA场景中可以不配置。若传入数值过大，由于预留了过多权重空间，会出现out_of_memory报错信息，例如: "RuntimeError: NPU out of memory. Tried to allocate xxx GiB."

说明此章节中的run_pa.py脚本用于纯模型快速测试，脚本中未增加强校验，出现异常情况时，会直接抛出异常信息。例如：

- input_texts、input_ids、input_file、input_dict参数包含推理内容，程序进行数据处理的时间和传入数据量成正比。同时这些输入会被转换成token id搬运至NPU，传入数据量过大可能会导致这些NPU tensor占用显存过大，而出现由out of memory导致的报错信息，例如："req: xx input length: xx is too long, max_prefill_tokens: xx"等报错信息。
- chat_template参数可以使用两种形式输入：模板文本或模板文件的路径。当以模板文本输入时，若文本长度过大，可能会导致运行缓慢。
- 脚本会基于max_batch_size、max_input_length、max_output_length、max_prefill_batch_size和max_prefill_tokens等参数申请推理输入及KV Cache，若用户传入数值过大，会出现由out of memory导致的报错信息，例如："RuntimeError: NPU out of memory. Tried to allocate xxx GiB."。
- 脚本会基于max_position_embeddings参数，申请旋转位置编码和attention mask等NPU tensor，若用户传入数值过大，会出现由out of memory导致的报错信息，例如："RuntimeError: NPU out of memory. Tried to allocate xxx GiB."。
- block_size参数若小于张量并行场景下每张卡实际分到的注意力头个数，会出现由shape不匹配导致的报错（"Setup fail, enable log: export ASDOPS_LOG_LEVEL=ERROR, export ASDOPS_LOG_TO_STDOUT=1 to find the first error. For more details, see the MindIE official document."），需开启日志查看详细信息。

- 用户可以通过以下方式直接调用run_pa.py脚本，通过传入参数的方式自定义推理内容及推理方式。
- 测试性能。开启ATB_LLM_BENCHMARK_ENABLE环境变量后，将统计模型首Token、增量Token及端到端推理时延。
# 环境变量开启方式 export ATB_LLM_BENCHMARK_ENABLE=1 # 启动推理方式见步骤4、步骤5

耗时结果会显示在终端中，并保存在./benchmark_result/benchmark.csv文件里。

说明性能测试后，可使用msprof工具，进行性能数据采集和性能数据分析，达到性能调优目的。msprof工具的使用可参见《性能调优工具》的“

[msprof命令行工具](https://www.hiascend.com/document/detail/zh/mindstudio/700/T&ITools/Profiling/atlasprofiling_16_0010.html)”章节。

**父主题：**

[离线推理](https://www.hiascend.com/mindie_llm0525.html)


# ATB Models服务化使用

#### 前提条件

已在环境上安装CANN、PyTorch、Torch-NPU、ATB Models、MindIE LLM和MindIE Motor，详情请参见《[MindIE安装指南](https://www.hiascend.com/document/detail/zh/mindie/230/envdeployment/instg/mindie_instg_0001.html)》。

#### 使用实例

- 设置环境变量。
若安装路径为默认路径，可以运行以下命令初始化各组件环境变量。

1 2 3 4 5 6 7 8 9

# 配置CANN环境，默认安装在/usr/local目录下 source /usr/local/Ascend/cann/set_env.sh # 配置加速库环境 source /usr/local/Ascend/nnal/atb/set_env.sh # 配置模型仓库环境变量 source /usr/local/Ascend/atb-models/set_env.sh # MindIE source /usr/local/Ascend/mindie/latest/mindie-llm/set_env.sh source /usr/local/Ascend/mindie/latest/mindie-service/set_env.sh

- 启动服务化并发送请求。
MindIE服务化使用方法请参考《MindIE Motor开发指南》中的“快速入门 >

[启动服务](https://www.hiascend.com/document/detail/zh/mindie/230/mindiemotor/motordev/mindie_service0004.html)”章节。服务化参数配置请参考[配置参数说明（服务化）](https://www.hiascend.com/mindie_service0285.html)。服务化配置中默认使用ATB Models作为模型后端。

1 2 3

vim /usr/local/Ascend/mindie/latest/mindie-service/conf/config.json # ModelDeployConfig.ModelConfig.backendType字段默认值为"atb" "backendType": "atb"

服务化API接口请参考《MindIE Motor开发指南》中的“

[服务化接口](https://www.hiascend.com/document/detail/zh/mindie/230/mindiemotor/motordev/mindie_service0256.html)”章节。用户可使用HTTPS客户端（Linux curl命令，Postman工具等）发送HTTPS请求，此处以Linux curl命令为例进行说明。重开一个窗口，使用以下命令发送请求。

curl -H "Accept: application/json" -H "Content-type: application/json" -X POST --cacert {Server

*服务端证书的验签证书/根证书路径*} --cert {*客户端证书文件路径*} --key {*客户端证书私钥路径*} -d '{"inputs": "hi","stream":false}' https://{ip}:{port}/generate

**父主题：**

[离线推理](https://www.hiascend.com/mindie_llm0525.html)


# MindSpore Models服务化使用

MindIE LLM不仅支持ATB Models，同时支持MindSpore作为框架后端，MindSpore Models覆盖MindFormers社区下的开源模型，模型列表和使用方式参考[MindSpore Transformers](https://gitee.com/mindspore/mindformers/tree/master/)。

#### 前提条件

- 已在环境上安装CANN，详情请参见《
[MindIE安装指南](https://www.hiascend.com/document/detail/zh/mindie/230/envdeployment/instg/mindie_instg_0001.html)》。 - 已在环境上安装MindSpore和MindFormers，详情请参见
[MindFormers官方安装指南](https://www.mindspore.cn/mindformers/docs/zh-CN/r1.5.0/quick_start/install.html)。

#### 权重转换

执行推理前，需将权重格式转为MindFormers所使用的格式（ckpt格式）。MindFormers提供了统一的权重转换工具，请参考[权重格式转换](https://www.mindspore.cn/mindformers/docs/zh-CN/r1.5.0/function/weight_conversion.html)。

mf_model └── qwen2_5_72b ├── config.json # 模型json配置文件 ├── vocab.json # 模型vocab文件，hf上对应模型下载 ├── merges.txt # 模型merges文件，hf上对应模型下载 ├── predict_qwen2_5_72b.yaml # 模型yaml配置文件 ├── qwen2_5_tokenizer.py # 模型tokenizer文件，从mindformers仓中research目录下找到对应模型复制 └── qwen2_5_72b_ckpt_dir # 模型分布式权重文件夹

权重转换之后，需要进行权重切分。请参考[MindFormer Qwen2.5](https://gitee.com/mindspore/mindformers/blob/r1.6.0/research/qwen2_5/README.md)的“多卡推理”进行权重切分，切分后生成“qwen2_5_72b_ckpt_dir”文件夹。

predict_qwen2_5_72b.yaml需要关注以下配置：

load_checkpoint: '/mf_model/qwen2_5_72b/qwen2_5_72b_ckpt_dir' # 为存放模型分布式权重文件夹路径 use_parallel: True auto_trans_ckpt: False # 是否开启自动权重转换，离线切分设置为False parallel_config: data_parallel: 1 model_parallel: 4 # 多卡推理配置模型切分，一般与使用卡数一致 pipeline_parallel: 1 processor: tokenizer: vocab_file: "/mf_model/qwen2_5_72b/vocab.json" # vocab文件路径 merges_file: "/mf_model/qwen2_5_72b/merges.txt" # merges文件路径

模型的config.json文件可以使用save_pretrained接口生成，示例如下：

1 2 3 4 | from mindformers import AutoConfig model_config = AutoConfig.from_pretrained("/mf_model/qwen2_5_72b/predict_qwen2_5_72b.yaml") model_config.save_pretrained(save_directory="./json/qwen2_5_72b/", save_json=True) |

#### 使用实例

运行MindSpore Models需配合服务化使用。

- 设置环境变量。
若安装路径为默认路径，可以运行以下命令初始化各组件环境变量。

`# Ascend source /usr/local/Ascend/cann/set_env.sh # MindIE source /usr/local/Ascend/mindie/latest/mindie-llm/set_env.sh source /usr/local/Ascend/mindie/latest/mindie-service/set_env.sh # MindSpore export LCAL_IF_PORT=8129 # 组网配置 export MS_SCHED_HOST=127.0.0.1 # scheduler节点ip地址 export MS_SCHED_PORT=8090 # scheduler节点服务端口`

说明若机器上有其他卡已启动MindIE，需要注意MS_SCHED_PORT参数是否冲突。若日志打印中该参数报错，替换为其他端口号重新尝试即可。

- 启动服务化并发送请求。
MindIE服务化使用方法请参考《MindIE Motor开发指南》中的“快速入门 >

[启动服务](https://www.hiascend.com/document/detail/zh/mindie/230/mindiemotor/motordev/mindie_service0004.html)”章节，服务化参数配置请参考[配置参数说明（服务化）](https://www.hiascend.com/mindie_service0285.html)。若要启用MindSpore Models作为模型后端，服务化配置中需将ModelDeployConfig.ModelConfig.backendType字段设置为"ms"。

`vim /usr/local/Ascend/mindie/latest/mindie-service/conf/config.json # 修改ModelDeployConfig.ModelConfig.backendType "backendType": "ms"`

服务化API接口请参考《MindIE Motor开发指南》中的“

[服务化接口](https://www.hiascend.com/document/detail/zh/mindie/230/mindiemotor/motordev/mindie_service0256.html)”章节。用户可使用HTTPS客户端（Linux curl命令，Postman工具等）发送HTTPS请求，此处以Linux curl命令为例进行说明。重开一个窗口，使用以下命令发送请求。

`curl -H "Accept: application/json" -H "Content-type: application/json" -X POST --cacert {Server`

*服务端证书的验签证书/根证书路径*} --cert {*客户端证书文件路径*} --key {*客户端证书私钥路径*} -d '{"inputs": "I love Beijing, because","stream": false}' https://{ip}:{port}/generate须知MindSpore场景下，请求体中的seed字段限制在[0, 2^32)范围内，若超过则按照默认值seed = 0设置。


**父主题：**

[离线推理](https://www.hiascend.com/mindie_llm0525.html)


# 性能调优

可通过开启CPU高性能模式、透明大页和jemalloc优化来提升性能，这三种方式相互独立，可以开启其中一个或多个。

192核服务器在处理低并发长序列任务时，易发CPU高负载，致使CPU成为系统瓶颈，并引发TPOP性能波动与劣化。建议参照本章节中的方式进行优化。

#### 开启CPU高性能模式和透明大页

在裸机中执行以下命令开启CPU高性能模式和透明大页，开启后可提升性能。

- 开启CPU高性能模式，在相同时延约束下，TPS会有约3%的提升。
`cpupower -c all frequency-set -g performance`


- 开启透明大页，多次实验的吞吐率结果会更稳定。
`echo always > /sys/kernel/mm/transparent_hugepage/enabled`

说明服务化进程可能与模型执行进程抢占CPU资源，导致性能时延波动；可以在启动服务时将服务化进程手动绑核至CPU奇数核，以减少CPU抢占影响，降低性能波动，具体方法如下所示。

- 使用
**lscpu**命令查看系统CPU配置情况。`lscpu`

CPU相关配置回显信息如下所示：

`NUMA: NUMA node(s): 8 NUMA node0 CPU(s): 0-23 NUMA node1 CPU(s): 24-47 NUMA node2 CPU(s): 48-71 NUMA node3 CPU(s): 72-95 NUMA node4 CPU(s): 96-119 NUMA node5 CPU(s): 120-143 NUMA node6 CPU(s): 144-167 NUMA node7 CPU(s): 168-191`

- 使用
**taskset -c**命令将服务化进程绑核至CPU奇数核并启动。`taskset -c $cpus ./bin/mindieservice_daemon`

$cpus：为CPU配置回显信息中node1、node3、node5或node7的值。


- 使用

#### 开启jemalloc优化

jemalloc优化需要用户自行编译jemalloc动态链接库，并在脚本里引入编译好的动态链接库，具体步骤如下。

- 单击
[链接](https://github.com/jemalloc/jemalloc)下载jemalloc源码，并参考INSTALL.md文件编译安装。 - 拉起服务前，将jemalloc动态链接库引入环境，执行如下命令。
export LD_PRELOAD="

*{$path_to_lib}*/libjemalloc.so:$LD_PRELOAD"其中path_to_lib为libjemalloc.so所在路径。



# 特性列表

MindIE LLM支持的特性包括基础特性、长序列特性、调度特性、加速特性和交互特性。

#### 基础特性

基础特性如[表1](https://www.hiascend.com#ZH-CN_TOPIC_0000002500899398__table1834873673210)所示。

#### 长序列特性

长序列特性如[表2](https://www.hiascend.com#ZH-CN_TOPIC_0000002500899398__table795410285193)所示。

特性 |
说明 |
|---|---|
Context Parallel |
通过将长序列在上下文维度进行切分，分配到不同设备并行处理，减少首token响应时间，其特性介绍详情请参见 |
Sequence Parallel |
通过对KV Cache进行切分，使得每个sprank保存的KV Cache各不相同，达到节省显存，支持长序列的功能，其特性介绍详情请参见 |

#### 调度特性

调度特性如[表3](https://www.hiascend.com#ZH-CN_TOPIC_0000002500899398__table28683917196)所示。

#### 加速特性

加速特性如[表4](https://www.hiascend.com#ZH-CN_TOPIC_0000002500899398__table85751656171918)所示。

特性 |
说明 |
|---|---|
Micro Batch |
批处理过程中，将数据切分为更小粒度的多个batch运行，使得硬件资源得以充分利用，以提高推理吞吐。其特性介绍详情请参见 |
Buffer Response |
通过配置Prefill阶段和Decode阶段的SLO期望时延，可达到平衡两者时延，使其在都不超时的情况下，收益最大化的目的。其特性介绍详情请参见 |
并行解码 |
利用算力优势弥补访存带宽受限的影响，提升算力利用率。其特性介绍详情请参见 |
MTP |
在推理过程中，模型不仅预测下一个token，而且会同时预测多个token，从而显著提升模型生成速度。其特性介绍详情请参见 |
Prefix Cache |
复用跨session的重复token序列对应的KV Cache，减少一部分前缀token的KV Cache计算时间，从而减少Prefill的时间。其特性介绍详情请参见 |
KV Cache池化 |
支持将DRAM甚至SSD等更大容量的存储介质纳入前缀缓存池，从而突破片上内存的容量限制。该特性有效提升了Prefix Cache的命中率，显著降低大模型推理的成本。其特性介绍详情请参见 |

#### 交互特性

交互特性如[表5](https://www.hiascend.com#ZH-CN_TOPIC_0000002500899398__table1026817512013)所示。

特性 |
说明 |
|---|---|
Function Call |
支持Function Call函数调用，使大模型具备使用工具能力。其特性介绍详情请参见 |
思考解析 |
对大模型的输出内容进行结构化解析，将思考过程和输出结果进行分离。其特性介绍详情请参见 |

**父主题：**

[特性介绍](https://www.hiascend.com/mindie_llm0277.html)


# 特性叠加

本章节提供DeepSeek模型和Qwen模型的特性叠加说明。

：表示全部支持

：表示部分支持

：表示不支持

#### DeepSeek模型

DeepSeek模型支持的特性叠加情况如下所示。

[1]：MTP和CP叠加：PD分离场景时，仅P节点支持；PD混部场景只支持CP和MTP=1的叠加。

[2]：MTP和SP叠加：PD分离场景时，仅P节点支持；PD混部场景只支持CP和MTP=1的叠加。

#### Qwen模型

Qwen模型支持的特性叠加情况如下所示。

[1]：仅Qwen3系列支持思考解析。

[2]：仅Qwen2.5和Qwen3系列支持Function Call。

[3]：仅Qwen2和Qwen2.5系列支持Prefix Cache。

**父主题：**

[特性介绍](https://www.hiascend.com/mindie_llm0277.html)


# 前提条件

已在环境上安装CANN、ATB Models和msModelSlim，详情请参见《[MindIE安装指南](https://www.hiascend.com/document/detail/zh/mindie/230/envdeployment/instg/mindie_instg_0001.html)》。

本次样例参考以下安装路径进行：

安装ATB Models并初始化ATB Models环境变量。模型仓库set_env.sh脚本中有初始化“${ATB_SPEED_HOME_PATH}”环境变量的操作，所以source模型仓库中set_env.sh脚本时会同时初始化“${ATB_SPEED_HOME_PATH}”环境变量。

ATB Models公共能力支持以下量化方式：

- W8A8
- W4A8混合量化
- W8A16
- W8A8SC稀疏量化
- W16A16SC稀疏量化
- KV Cache int8
- FA3量化
- Anti-Outlier离群值处理
- Attention量化
- PDMIX量化

每个模型具体支持的量化方式不同，请参考${ATB_SPEED_HOME_PATH}/examples/models/路径下模型Readme文件中的特性支持矩阵。

量化特性支持量化回退，即模型中部分权重不做量化，使用原始的浮点权重进行MatMul计算，支持Linear级别的量化回退。量化回退可以提升量化权重的精度。每个模型不同量化方式下的量化回退配置可能都不相同，请参考各模型生成量化权重脚本中的配置。

以LLaMA为例，在${ATB_SPEED_HOME_PATH}/examples/models/llama/generate_quant_weight.sh中定义了不同量化方式下的回退层。在W8A16量化场景下，不设置回退层（默认回退lmhead），其他量化场景下，将layer中的down层全部回退。

1 2 3 4 5 6 7 8 | get_down_proj_disable_name() { local num_layer=$1 local disable_names="" for ((i=0; i<$num_layer; i++)); do disable_names="$disable_names model.layers.$i.mlp.down_proj" done echo "$disable_names" } |

**父主题：**

[量化](https://www.hiascend.com/mindie_llm0278.html)


# 量化脚本说明

MindIE LLM中提供统一的脚本${ATB_SPEED_HOME_PATH}/examples/convert/model_slim/quantifier.py供用户生成量化权重。

#### 使用说明

由于不同模型量化特性参数配置不同，模型基于公共脚本编写各自的量化脚本。具体使用方式见模型readme文件（${ATB_SPEED_HOME_PATH}/examples/models/{模型名称}/README.md）。

不同量化方式下的参数配置方法见后续章节。

#### 参数说明

详情可参考《msModelSlim工具》的“[介绍](https://gitcode.com/Ascend/msit/tree/master/msmodelslim)”章节。

参数名称 |
是否为必选 |
类型 |
默认值 |
描述 |
|---|---|---|---|---|
--save_directory |
是 |
string |
- |
量化权重保存路径。 |
--part_file_size |
否 |
int |
None |
量化权重保存文件切分大小，单位GB，默认不切分。 |
--calib_texts |
否 |
string |
None |
量化时的校准数据，多条数据间使用空格分割。 说明：
脚本基于calib_texts进行推理，若用户传入数值过大，会出现由out of memory导致的报错信息。 |
--calib_file |
否 |
string |
${ATB_SPEED_HOME_PATH}/examples/convert/model_slim/teacher_qualification.jsonl |
包含校准数据的文件。 |
--w_bit |
否 |
int |
8 |
权重量化bit。
|
--a_bit |
否 |
int |
8 |
激活值量化bit。 可选值为8和16。
|
--disable_names |
否 |
string |
None |
需排除量化的节点名称，即手动回退的量化层名称。如精度太差，推荐回退量化敏感层，如分类层、输入层、检测head层等。 |
--device_type |
否 |
string |
"cpu" |
量化时的硬件类型，仅支持"cpu"或"npu"。 |
--fraction |
否 |
float |
0.01 |
稀疏量化精度控制。 |
--act_method |
否 |
int |
1 |
激活值量化方法，仅支持1或2或3。
|
--co_sparse |
否 |
bool |
False |
是否开启稀疏量化功能。 大模型稀疏量化场景下，优先使用lowbit稀疏量化功能，开启lowbit稀疏量化后，co_sparse参数自动失效。 |
--anti_method |
否 |
string |
"" |
离群值抑制算法，默认不开启。
|
--disable_level |
否 |
string |
"L0" |
自动回退等级。
|
--do_smooth |
否 |
bool |
False |
是否开启smooth功能。启用do_smooth功能后，平滑激活值。默认为"False"，不开启smooth功能。 |
--use_sigma |
否 |
bool |
False |
是否启动sigma功能。启用use_sigma功能后，可根据正态分布数值特点进行异常值保护。默认为"False"，不开启sigma功能。 |
--use_reduce_quant |
否 |
bool |
False |
是否使用lccl reduce量化功能，默认不开启。 |
--tp_size |
否 |
int |
1 |
lccl reduce量化时需要用到的卡数，默认为1。 |
--sigma_factor |
否 |
float |
3.0 |
启用sigma功能后sigma_factor的值，用于限制异常值的保护范围。默认为3.0，取值范围为[3.0, 4.0]。 |
--is_lowbit |
否 |
bool |
False |
是否开启lowbit量化功能。 默认为"False"，不开启lowbit量化功能。 |
--mm_tensor |
否 |
bool |
True |
选择进行per-channel量化或per-tensor量化。
|
--w_sym |
否 |
bool |
True |
权重量化是否为对称量化，默认开启对称量化。 |
--use_kvcache_quant |
否 |
bool |
False |
是否使用KV Cache量化功能，默认不开启KV Cache量化功能。 |
--use_fa_quant |
否 |
bool |
False |
是否使用Attention量化功能，默认不开启Attention量化功能。 |
--fa_amp |
否 |
int |
0 |
Attention量化的自动回退层数，以整个Attention为单位进行回退。 默认值为0。 |
--open_outlier |
否 |
bool |
True |
是否开启权重异常值划分。
|
--group_size |
否 |
int |
64 |
per_group量化中group的大小。 默认值为64，支持配置为64或128。 |
--is_dynamic |
否 |
bool |
False |
是否开启per token量化，当前仅W8A8支持per token量化。
|
--input_ids_name |
否 |
string |
"input_ids" |
tokenize后input_ids对应的键名。 |
--attention_mask_name |
否 |
string |
"attention_mask" |
tokenize后attention_mask对应的键名。 |
--tokenizer_args |
否 |
符合json格式的string |
"{}" |
对校准数据集做tokenize时可额外配置的参数。 例如：'{"padding_side":"left","pad_token":"!"}' |
--disable_last_linear |
否 |
bool |
True |
是否禁用最后一层全连接层量化，默认为True，即禁用。 |
--trust_remote_code |
否 |
bool |
store_true |
是否信任模型权重路径下的自定义代码文件。默认不执行。若传入此参数，则transformers会执行用户权重路径下的自定义代码文件，这些代码文件的功能的安全性需由用户保证，请提前做好安全性检查。 |

calib_texts参数包含校准数据，量化校准时间和传入数据量成正比。当使用NPU进行量化时，输入会被转换成token id搬运至NPU，传入数据量过大可能会导致NPU tensor占用显存过大，而出现由out of memory导致的报错信息。

**父主题：**

[量化](https://www.hiascend.com/mindie_llm0278.html)


# msModelSlim工具生成量化权重

请参考[量化权重生成代码样例](https://gitcode.com/Ascend/msit/blob/master/msmodelslim/docs/案例集/量化及稀疏量化场景导入代码样例.md)。

#### 限制与约束

- Atlas 300I Duo 推理卡场景时，msModelSlim工具仅支持单卡单芯量化。
- msModelSlim工具不支持多机量化。

**父主题：**

[量化](https://www.hiascend.com/mindie_llm0278.html)


# 量化精度调优

量化精度调优策略是结合ModelSlim量化工具和精度测试工具precision tool进行精度验证和调优开展。大模型经过量化后精度损失大，可以参考如下精度调优策略进行调整。具体内容可以参考下面的链接：

- W8A8量化精度调优请参考
[W8A8量化精度调优策略](https://gitcode.com/Ascend/msit/blob/master/msmodelslim/docs/案例集/w8a8精度调优策略.md)。 - W8A16量化精度调优请参考
[W8A16精度调优策略](https://gitcode.com/Ascend/msit/blob/master/msmodelslim/docs/案例集/w8a16精度调优策略.md)。 - 稀疏量化精度调优请参考
[稀疏量化精度调试案例](https://gitcode.com/Ascend/msit/blob/master/msmodelslim/docs/案例集/稀疏量化精度调试案例.md)。 - FA量化精度调优请参考
[FA量化使用说明](https://gitcode.com/Ascend/msit/blob/master/msmodelslim/docs/功能指南/脚本量化与其他功能/pytorch/llm_ptq/FA量化使用说明.md#fa3精度调优)。

**父主题：**

[量化](https://www.hiascend.com/mindie_llm0278.html)


# W8A8

#### 简介

此量化方式对权重和激活值均进行量化，将高位浮点数转为8 bit，减少模型权重的体积。使用int8格式的数据进行计算，可以减少MatMul算子计算量，以提升推理性能。

量化后权重目录结构：

├─ config.json ├─ configuration.json ├─ generation_config.json ├─ quant_model_description.json ├─ quant_model_weight_w8a8.safetensors └─ tokenizer.json

- 量化输出包含：权重文件quant_model_weight_w8a8.safetensors和权重描述文件quant_model_description.json。
- 目录中的其余文件为推理时所需的配置文件，不同模型略有差异。

以下展示了量化后权重描述文件quant_model_description.json中的部分内容：

1 2 3 4 5 6 7 |
{ "model.layers.0.self_attn.q_proj.weight": "W8A8", "model.layers.0.self_attn.q_proj.input_scale": "W8A8", "model.layers.0.self_attn.q_proj.input_offset": "W8A8", "model.layers.0.self_attn.q_proj.quant_bias": "W8A8", "model.layers.0.self_attn.q_proj.deq_scale": "W8A8" } |

量化后的MatMul权重新增input_scale、input_offset、quant_bias和deq_scale。其中input_scale和input_offset用于对激活值进行量化。MatMul使用量化后的激活值和量化权重进行计算。quant_bias和deq_scale用于对MatMul的计算结果进行反量化。

**图1**量化权重推理时流程

此量化方式支持量化float16或bfloat16类型的原始权重。

|
Tensor信息 |
weight |
input_scale |
input_offset |
quant_bias |
deq_scale |
|---|---|---|---|---|---|
|
dtype |
int8 |
float16 |
float16 |
int32 |
int64 |
|
shape |
[n, k] |
[1] |
[1] |
[n] |
[n] |

|
Tensor信息 |
weight |
input_scale |
input_offset |
quant_bias |
deq_scale |
|---|---|---|---|---|---|
|
dtype |
int8 |
bfloat16 |
bfloat16 |
int32 |
float32 |
|
shape |
[n, k] |
[1] |
[1] |
[n] |
[n] |

#### 生成权重

- 请参见
[msModelSlim工具](https://gitcode.com/Ascend/msit/blob/master/msmodelslim/docs/安装指南.md)，安装**msModelSlim**工具。 - 使用msModelSlim工具生成量化权重。
[以Qwen2-7B为例，安装msModelSlim工具后，可以使用如下命令快速生成一份W8A8量化权重：]msmodelslim quant --model_path {浮点权重路径} --save_path {W8A8量化权重路径} --device npu --model_type Qwen2-7B --quant_type w8a8 --trust_remote_code True


上述命令是msModelSlim工具的一个最佳实践，如需了解更多量化参数配置，请参考msModelSlim工具文档。

#### 执行推理

以Qwen2-7B-W8A8为例，您可以使用以下指令执行对话测试，推理内容为"What's deep learning?"，最长输出20个token。

1 2 |
cd ${ATB_SPEED_HOME_PATH} torchrun --master_port 12350 -m examples.run_pa --model_path {w8a8量化权重路径} |

**父主题：**

[量化](https://www.hiascend.com/mindie_llm0278.html)
