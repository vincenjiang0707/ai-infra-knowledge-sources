source: https://docs.mthreads.com/tts/stream-tts/introduction

# 流式语音合成WebSocket API

## 目录[](https://docs.mthreads.com#目录)

## 接口地址：[](https://docs.mthreads.com#接口地址)

**外网访问地址:**

`wss://aibook-api.mthreads.com:32414/api/v2/tts/stream_generate`




注意:访问令牌（Access Token）请联系我们获取。联系方式：[meng.cai@mthreads.com],[ye.wang@mthreads.com]

## TTS 音色列表[](https://docs.mthreads.com#tts音色列表)

体验demo：[https://voice.mthreads.com/](https://voice.mthreads.com/)

| 音色 | voice_name | 性别 | 备��注 |
|---|---|---|---|
| 程小可 | AIBC006_llm | 女 | 大模型音色 |
| 程小清 | AIBF004_llm | 女 | 大模型音色 |
| 程小新 | AIBF105_llm | 女 | 大模型音色 |
| 程小艾 | AIBF111_llm | 女 | 大模型音色 |
| 程小曲 | AIBF001_llm | 女 | 大模型音色 |
| 程小园 | AIBF002_llm | 女 | 大模型音色 |
| 程小苏 | AIBF003_llm | 女 | 大模型音色 |
| 程小迪 | AIBM107_llm | 男 | 大模型音色 |
| 程小春 | AIBM115_llm | 男 | 大模型音色 |
| 程小虎 | AIBM101_llm | 男 | 大模型音色 |
| 程小帅 | AIBM103_llm | 男 | 大模型音色 |
| 晓凌 | LYG1004_llm | 女 | 大模型音色 |
| 穆莎 | SSB3001_llm | 女 | 大模型音色 |
| 米塔 | SSB3002_llm | 女 | 大模型音色 |
| 晓柒 | LYG3001_llm | 男 | 大模型音色 |
| BabyX | WSH0001_llm | 男 | 大模型音色 |
| BoyTen | WSH0002_llm | 男 | 大模型音色 |
| 程小可(lite) | AIBC006 | 女 | |
| 程小曲(lite) | AIBF001 | 女 | |
| 小美(lite) | NYS0001 | 女 | |
| 小雅(lite) | NYS0002 | 女 | |
| 穆莎(lite) | SSB3001 | 女 | |
| 米塔(lite) | SSB3002 | 女 | |
| 晓凌(lite) | LYG1004 | 女 | |
| 晓柒(lite) | LYG3001 | 男 | |
| BabyX(lite) | babyx | 男 | |
| BoyTen(lite) | boyten | 男 |

## 接口说明[](https://docs.mthreads.com#接口说明)

### 单句流式合成[](https://docs.mthreads.com#单句流式合成)

#### 使用说明[](https://docs.mthreads.com#使用说明)

client单次发送请求信息，server流式返回一到多条返回返回信息

#### 注意事项：[](https://docs.mthreads.com#注意事项)

-
支持SSML输入

-
websocket单次连接仅支持单次合成(返回时间戳为连续数值)，若需要合成多次，则需要多次建立连接


#### 交互流程[](https://docs.mthreads.com#交互流程)

### 流式文本合成：文本大模型实时生成场景[](https://docs.mthreads.com#流式文本合成文本大模型实时生成场景)

#### 使用说明[](https://docs.mthreads.com#使用说明-1)

流式文本语音合成基于文本持续输入的应用场景进行测试，该接口可以面向大语言模型逐字输入的场景持续输出合成音频，极大地提升了交互体验，减少了用户等待时间，又能同时兼顾在连续文本输入中合成语音效果的上下文连贯性、韵律风格一致性。

#### 注意事项[](https://docs.mthreads.com#注意事项-1)

-
不支持SSML输入

-
websocket单次连接仅支持单次合成(返回时间戳为连续数值)，如果需要重置时间戳，需要重新建立连接

-
在调用上游就已经确定了全部文本时不建议使用本接口：由于流式文本接口需要维护额外的文本缓冲，整体合成时延会略高于单向流式合成


#### 交互流程[](https://docs.mthreads.com#交互流程-1)

## 基础参数说明[](https://docs.mthreads.com#基础参数说明)

### 发送请求[](https://docs.mthreads.com#发送请求)

#### 字段说明[](https://docs.mthreads.com#字段说明)

参数 | 类型 | 层级 | 必须 | 默认值 | 说明 |
|---|---|---|---|---|---|
| access_token | String | 1 | ✓ | 目前未生效，填写默认值：default_token | |
| cluster | String | 1 | ✓ | 当前请求使用的算法集群，不同集群支持不同音色，mt_tts / mt_llm_tts | |
| input | Dict | 1 | ✓ | 内容相关配置 | |
| text | String | 2 | ✓ | 待合成文本，文本内容必须采用UTF-8编码，长度不超过300个字符（英文字母之间需要添加空格）。 | |
| text_type | String | 2 | plain | plain / ssml, 默认为plain | |
| enable_subtitle | Boolean | 2 | false | 开启字级别时间戳。(开启之后大模型音色首包latency会变高) | |
| enable_phoneme_timestamp | Boolean | 2 | false | 开启音素级别时间戳。(开启之后大模型音色首包latency会变高) | |
| voice_config | Dict | 1 | ✓ | 音色相关配置 | |
| voice_name | String | 2 | ✓ | ||
| audio_config | Dict | 1 | 音频��相关配置 | ||
| speed_ratio | Float | 2 | 1 | 语速，[0.2,3]，默认为1，通常保留一位小数即可（大模型音色不支持） | |
| volume_ratio | Float | 2 | 1 | 音量，[0.1, 3]，默认为1，通常保留一位小数即可（大模型音色不支持） | |
| pitch_ratio | Float | 2 | 1 | 音高，[0.1, 3]，默认为1，通常保留一位小数即可（大模型音色不支持） |

#### 请求示例[](https://docs.mthreads.com#请求示例)

`{`

"access_token": "XXXXX",

"cluster": "mt_tts",

"input": {

"text": "摩尔线程语音合成",

"text_type": "plain",

"enable_subtitle": true,

"enable_phoneme_timestamp": true

},

"voice_config": {

"voice_name": "LYG1004",

"emotion": "happy",

"language": "cn"

},

"audio_config": {

"encoding": "pcm",

"sample_rate": 22050,

"compression_rate": 1,

"bits": 16,

"channel": 1,

"speed_ratio": 1.0,

"volume_ratio": 1.0,

"pitch_ratio": 1.0

}

}



### 返回信息[](https://docs.mthreads.com#返回信息)

#### 字段说明[](https://docs.mthreads.com#字段说明-1)

| 字段 | 含义 | 层级 | 格式 | 备注 |
|---|---|---|---|---|
| task_id | 当前session的id | 1 | string | 服务端随机生成 |
| status | 请求状态码 | 1 | int | 错误码，参考下方说明 |
| status_text | 请求状态信息 | 1 | string | 错误信息 |
| is_final | 请求音频是否合成完成 | 1 | boolean | 在流式版本中用到 |
| data | 合成音频 | 1 | string | 返回的音频数据，base64 编码 |
| addition | 额外信息 | 1 | string | 额外信息父节点 |
| duration | 音频时长 | 2 | int | 返回音频的长度，单位ms |
| subtitles | 字幕/时间戳信息 | 2 | List | 包含字级别和音素级别的时间戳信息，以字级别时间戳为单元的列表 |

#### 状态码[](https://docs.mthreads.com#状态码)

| 错误码 | 含义 | 举例 | 建议处理 |
|---|---|---|---|
| 1000 | 请求正确 | 正常合成 | 正常处理 |
| 2000 | 请求参数无效 | 请求参数缺失必需字段 / 字段值无效 | 检查调用逻辑 |
| 2001 | 无效文本 | 参数有误或者文本为空、文本与语种不匹配、文本只含标点 | 检查参数 |
| 2002 | 输入配置错误 | 无效文本类型/在文本流式场景下用ssml | 检查input参数 |
| 2003 | 音色配置错误 | 选择的音色不存在/音色使用错误 | 检查voice_config参数 |
| 2004 | 音频配置错误 | 无效音频类型指定 | 检查audio_config参数 |
| 2005 | 集群配置错误 | 无效集群指定 | 检查cluster参数 |
| 3000 | 服务内部错误 | 服务/网络/资源异常 | 重试 |

#### 返回示例[](https://docs.mthreads.com#返回示例)

`{`

"task_id": "XXXX",

"status": 1000,

"status_text": "Success",

"is_final": true,

"audio": "base64 encoded binary data",

"addition": {

"duration": 400,

"subtitles": [

{ "start_msec": 100, "end_msec": 200, "text": "今" },

{ "start_msec": 200, "end_msec": 400, "text": "天" }

],

"phoneme_timestamps": [

{ "start_msec": 100, "end_msec": 150, "text": "j" },

{ "start_msec": 150, "end_msec": 200, "text": "in1" },

{ "start_msec": 200, "end_msec": 300, "text": "t" },

{ "start_msec": 300, "end_msec": 400, "text": "ian1" }

]

}

}



## 流式参数说明[](https://docs.mthreads.com#流式参数说明)

### 字段说明[](https://docs.mthreads.com#字段说明-2)

参数 | 类型 | 层级 | 必须 | 默认值 | 说明 |
|---|---|---|---|---|---|
| is_final | Boolean | 1 | true | 当前请求是否完成上传文本 |

### 调用示例[](https://docs.mthreads.com#调用示例)

#### 单句流式[](https://docs.mthreads.com#单句流式)

`# 请求返回`

{

"task_id": "XXXX",

"status": 1000,

"status_text": "Success",

"is_final": false,

"audio": "音频数据(摩尔线程)base64 encoded binary data",

"addition": {

"duration": 899,

"subtitles":[]

}

}

{

"task_id": "XXXX",

"status": 1000,

"status_text": "Success",

"is_final": true,

"audio": "音频数据(语音合成)base64 encoded binary data",

"addition": {

"duration": 800,

"subtitles":[]

}

}



#### 流式文本流式[](https://docs.mthreads.com#流式文本流式)

`# 发第一个请求（初始请求需要包含所有meta，后续请求可以只包含文本信息）`

{

"access_token": "XXXXX",

"model": "mt_tts"

"input": {

"text": "摩尔线",

"text_type": "plain",

"enable_subtitle": true,

"enable_phoneme_timestamp": true

},

"voice_config": {

"voice_name": "LYG1004",

"emotion": "happy",

"language": "cn"

},

"audio_config": {

"audio_encoding": "pcm",

"sample_rate": 22050,

"compression_rate": 1,

"bits": 16,

"channel": 1,

"speed_ratio": 1.0,

"volume_ratio": 1.0,

"pitch_ratio": 1.0

},

"is_final": false,

}

# 发送第2个文本片段

{

"input": {

"text": "程",

},

"is_final": false

}

# 此时可能收到第1个音频片段

{

"task_id": "XXXX",

"status": 1000,

"status_text": "Success",

"is_final": false,

"audio": "音频数据(摩尔线程)base64 encoded binary data",

"addition": {

"duration": 899,

"subtitles":[]

}

}

# 发送第3个文本片段

{

"input": {

"text": "语音",

},

"is_final": false,

}

# 发送第4个文本片段

{

"input": {

"text": "合成",

},

"is_final": true,

}

# 此时收到第2个音频片段

{

"task_id": "XXXX",

"status": 1000,

"status_text": "Success",

"is_final": false,

"audio": "音频数据(语音)base64 encoded binary data",

"addition": {

"duration": 203,

"subtitles":[]

}

}

# 此时收到最后一个音频片段

{

"task_id": "XXXX",

"status": 1000,

"status_text": "Success",

"is_final": true,

"audio": "音频数据(合成)base64 encoded binary data",

"addition": {

"duration": 203,

"subtitles":[]

}

}

# 断开连接



## 调用示例[](https://docs.mthreads.com#调用示例-1)

### 准备client相关依赖[](https://docs.mthreads.com#准备client相关依赖)

`- python>=3.8`

- pip install -i https://pypi.tuna.tsinghua.edu.cn/simple websockets scipy numpy

- MT_DEVELOPER_API_ACCESS_TOKEN="XXXX" 请联系业务人员获取



### client代码[](https://docs.mthreads.com#client代码)

`import argparse`

import asyncio

import base64

import json

import os


import numpy as np

import websockets

from scipy.io import wavfile


MT_DEVELOPER_API_ACCESS_TOKEN = os.environ.get("MT_DEVELOPER_API_ACCESS_TOKEN", "")

if MT_DEVELOPER_API_ACCESS_TOKEN:

print(f"MT_DEVELOPER_API_ACCESS_TOKEN: {MT_DEVELOPER_API_ACCESS_TOKEN}")



def dump_wav(wav, sample_rate, basename, path="/tmp"):

if not os.path.exists(path):

os.makedirs(path)

filename = os.path.join(path, "{}.wav".format(basename))

print("dump synthesized audio [{}]s to path {}".format(wav.shape[0] / sample_rate, filename))

wavfile.write(filename, sample_rate, wav)

return filename



def get_json_request(text, **kwargs):

json_message = {

"cluster": kwargs.get("cluster", None),

"is_final": kwargs.get("is_final", False),

"input": {

"text": text,

"text_type": kwargs.get("text_type", "plain"),

"enable_subtitle": kwargs.get("enable_subtitle", False),

"enable_phoneme_timestamp": kwargs.get("enable_phoneme_timestamp", False),


},

"voice_config": {

"voice_name": kwargs.get("voice_name", None)

},

"audio_config": {

"speed_ratio": kwargs.get("speed_ratio", None)

}

}

print("发送请求message：{}".format(json_message))

return json_message



async def message_receiving_iterator(websocket):

while True:

try:

message = await websocket.recv()

data = json.loads(message)

yield data

if data.get("audio"):

data["audio"] = "...音频内容..."

print("收到响应message：{}".format(data))

if data.get('is_final', False):

break

except websockets.exceptions.ConnectionClosed:

print("Connection closed")

break



async def generate_ws_request_iter(text, is_final=True, **kwargs):

yield get_json_request(text, is_final=is_final, **kwargs)



async def generate_ws_request_stream_iter(text_stream_list, mock_request_interval=0, **kwargs):

voice = kwargs.pop("voice", None)

for i, text in enumerate(text_stream_list):

yield get_json_request(text, voice_name=voice if i == 0 else None,

is_final=True if i == len(text_stream_list) - 1 else False, **kwargs)

if mock_request_interval > 0:

print("发送请求文本片段{}：{}，模拟暂停{}秒".format(i + 1, text, mock_request_interval))

await asyncio.sleep(1)



async def request_sending_handler(websocket, request_iterator):

async for request in request_iterator:

await websocket.send(json.dumps(request))



async def text_sending_handler(websocket, text_stream_list, voice=None, text_type="plain",

enable_subtitle=False, enable_phoneme_timestamp=False,

speed_ratio=None, mock_request_interval=0, cluster=None):

for i, text in enumerate(text_stream_list):

request_json = json.dumps(get_json_request(

text, voice_name=voice if i == 0 else None,

text_type=text_type,

is_final=True if i == len(text_stream_list) - 1 else False,

enable_subtitle=enable_subtitle,

enable_phoneme_timestamp=enable_phoneme_timestamp,

speed_ratio=speed_ratio,

cluster=cluster,

), ensure_ascii=False)

await websocket.send(

request_json

)

if mock_request_interval > 0:

print("send: {}, wait {}s".format(request_json, mock_request_interval))

await asyncio.sleep(mock_request_interval)



async def streaming_synthesize_by_request_iter(address, request_iterator, access_token=MT_DEVELOPER_API_ACCESS_TOKEN):

async with websockets.connect(

address, max_size=1_000_000_000, extra_headers={"Authorization": f'Bearer {access_token}'}

) as websocket:

response_iter = message_receiving_iterator(websocket)

sending_task = asyncio.create_task(

request_sending_handler(websocket, request_iterator))

async for message in response_iter:

yield message

await sending_task



async def simple_streaming_synthesize(address, text, voice=None, text_type="plain", speed_ratio=1.0,

enable_subtitle=False, enable_phoneme_timestamp=False, cluster=None,

access_token=MT_DEVELOPER_API_ACCESS_TOKEN):

text_stream_list = text

mock_request_interval = 1

if isinstance(text, str):

text_stream_list = [text]

mock_request_interval = 0

async with websockets.connect(address, max_size=1_000_000_000,

extra_headers={"Authorization": f'Bearer {access_token}'}) as websocket:

response_iter = message_receiving_iterator(websocket)

sending_task = asyncio.create_task(

text_sending_handler(websocket, text_stream_list,

voice=voice, text_type=text_type, speed_ratio=speed_ratio,

enable_subtitle=enable_subtitle, enable_phoneme_timestamp=enable_phoneme_timestamp,

cluster=cluster, mock_request_interval=mock_request_interval))

async for message in response_iter:

yield message

await sending_task



def parse_audio_data_from_response(resp: dict):

audio_b64 = resp["audio"]

audio_bytes = base64.b64decode(audio_b64)

audio_data = np.frombuffer(audio_bytes, dtype=np.int16)

return audio_data



def stringify_linguistic_meta_list(meta_list):

return "|".join(

["{}({}->{}|final:{})".format(meta['text'], meta['start_msec'], meta['end_msec'], meta.get("is_final", False))

for meta in meta_list])



if __name__ == "__main__":

parser = argparse.ArgumentParser()

parser.add_argument("--address", type=str, default='ws://localhost:55302/api/v2/tts/stream_generate',

help="grpc service address")

parser.add_argument("--mode", type=str, default="unary",

help="streaming mode ('bidi' or 'unary')")

parser.add_argument("--voice", type=str, default="LYG1004",

help="voice name for tts service")

parser.add_argument("--text", type=str, default="轻轻的，我走了，正如我轻轻的来",

help="text to synthesize")

parser.add_argument("--text_stream", type=str, default="轻轻的|||我走了。|||正如|||我轻轻|||的来",

help="mock text stream for bidirectional synthesis, "

"text_stream should be a string separated by a |||")

parser.add_argument("--text_type", type=str, default="plain",

help="text type for request text (plain or ssml).")

parser.add_argument("--cluster", type=str, default="",

help="cluster for the voice.")

parser.add_argument("--speed_ratio", type=float, default=1.0,

help="requested speaking speed ratio to synthesize, 1.0 is the default speed.")

parser.add_argument("--output_fpath", type=str, default="./gRPCClient.wav",

help="fpath to dump wav")

parser.add_argument("--enable_subtitle", type=lambda s: s.lower() == "true", default="true")

parser.add_argument("--enable_phoneme_timestamp", type=lambda s: s.lower() == "true", default="true")

args = parser.parse_args()



async def synthesize():

text = args.text

if args.mode == "bidi":

assert args.text_stream.strip()

text = args.text_stream.split("|||")

print("输入文本: {}".format(text))


audio_chunks = []

audio_chunk_metas = []

async for response in simple_streaming_synthesize(address=args.address, text=text, text_type=args.text_type,

voice=args.voice, speed_ratio=args.speed_ratio,

cluster=args.cluster,

enable_subtitle=args.enable_subtitle,

enable_phoneme_timestamp=args.enable_phoneme_timestamp):

if response["status"] != 1000:

print("收到错误码：", response["status"])

print("收到错误信息：", response["status_text"])

exit(1)

is_final = response.get("is_final", False)

audio_chunks.append(parse_audio_data_from_response(response))

audio_chunk_metas.append(response["addition"])

print(f"收到第一句音频，{response['addition']['duration']}毫秒, is_final: [{is_final}]")

print(f"收到第一句音频对应字幕，[{stringify_linguistic_meta_list(response['addition']['subtitles'])}]")

print(

f"收到第一句音频对应音素时间戳，[{stringify_linguistic_meta_list(response['addition']['phoneme_timestamps'])}]")

return audio_chunks



audio_chunks = asyncio.run(synthesize())


audio_data = np.concatenate(audio_chunks)

output_base_name = os.path.basename(args.output_fpath).replace(".wav", "")

output_dir = os.path.dirname(args.output_fpath)

dump_wav(audio_data, 22050, output_base_name, path=output_dir)



## 单向流式[](https://docs.mthreads.com#单向流式)

`PYTHONPATH=. MT_DEVELOPER_API_ACCESS_TOKEN="XXXXX" python ws_client.py --voice AIBC006_llm `

--address ws://10.1.33.4:32414/api/v2/tts/stream_generate --enable_subtitle false --enable_phoneme_timestamp false --text "你好，我是穆莎，��你的AI朋友，有什么问题就尽管找我吧。"


MT_DEVELOPER_API_ACCESS_TOKEN: XXXXX

输入文本: 你好，我是穆莎，你的AI朋友，有什么问题就尽管找我吧。

发送请求message：{'cluster': '', 'is_final': True, 'input': {'text': '你好，我是穆莎，你的AI朋友，有什么问题就尽管找我吧。', 'text_type': 'plain', 'enable_subtitle': False, 'enable_phoneme_timestamp': False}, 'voice_config': {'audio_config': {'speed_ratio': 1.0}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，372毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 372, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第�一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，186毫秒, is_final: [True]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': 'ded5709880d14d0f9b0ecfac32b15d2b', 'status': 1000, 'status_text': 'Success.', 'is_final': True, 'audio': '...音频内容...', 'addition': {'duration': 186, 'subtitles': [], 'phoneme_timestamps': []}}

dump synthesized audio [6.408707482993197]s to path ./gRPCClient.wav




PYTHONPATH=. MT_DEVELOPER_API_ACCESS_TOKEN="XXXXX" python ws_client.py --voice AIBC006_llm

--address ws://10.1.33.4:32414/api/v2/tts/stream_generate --enable_subtitle true --enable_phoneme_timestamp true --text "你好，我是穆莎，你的AI朋友，有什么问题就尽管找我吧。"


输入文本: 你好，我是穆莎，你的AI朋友，有什么问题就尽管找我吧。

发送请求message：{'cluster': '', 'is_final': True, 'input': {'text': '你好，我是穆莎，你的AI朋友，有什么问题就尽管找我吧。', 'text_type': 'plain', 'enable_subtitle': True, 'enable_phoneme_timestamp': True}, 'voice_config': {'vodio_config': {'speed_ratio': 1.0}}

收到第一句音频，604毫秒, is_final: [False]

收到第一句音频对应字幕，[你(507->603|final:False)]

收到第一句音频对应音素时间戳，[n(507->552|final:False)|i2(552->603|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 604, 'subtitles': [{'text': '你', 'start_msec': msec': 603, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'n', 'start_msec': 507, 'end_msec': 552, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'i2', 'start_msec': 552, 'end_msec': 603, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，557毫秒, is_final: [False]

收到第一句音频对应字幕，[好，(0->557|final:False)]

收到第一句音频对应音素时间戳，[h(0->268|final:False)|ao3(268->557|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 557, 'subtitles': [{'text': '好，', 'start_msec'sec': 557, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'h', 'start_msec': 0, 'end_msec': 268, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'ao3', 'start_msec': 268, 'end_msec': 557, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，186毫秒, is_final: [False]

收到第一句音频对应字幕，[我(0->185|final:False)]

收到第一句音频对应音素时间戳，[^(0->45|final:False)|uo3(45->185|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 186, 'subtitles': [{'text': '我', 'start_msec': ec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': '^', 'start_msec': 0, 'end_msec': 45, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'uo3', 'start_msec': 45, 'end_msec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，93毫秒, is_final: [False]

收到第一句音频对应字幕，[是(0->92|final:False)]

收到第一句音频对应音素时间戳，[sh(0->18|final:False)|iii4(18->92|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 93, 'subtitles': [{'text': '是', 'start_msec': 0c': 92, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'sh', 'start_msec': 0, 'end_msec': 18, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'iii4', 'start_msec': 18, 'end_msec': 92, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，232毫秒, is_final: [False]

收到第一句音频对应字幕，[穆(0->231|final:False)]

收到第一句音频对应音素时间戳，[m(0->113|final:False)|u4(113->231|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 232, 'subtitles': [{'text': '穆', 'start_msec': ec': 231, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'm', 'start_msec': 0, 'end_msec': 113, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'u4', 'start_msec': 113, 'end_msec': 231, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，278毫秒, is_final: [False]

收到第一句音频对应字幕，[莎，(0->278|final:False)]

收到第一句音频对应音素时间戳，[sh(0->66|final:False)|a1(66->278|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 278, 'subtitles': [{'text': '莎，', 'start_msec'sec': 278, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'sh', 'start_msec': 0, 'end_msec': 66, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'a1', 'start_msec': 66, 'end_msec': 278, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，511毫秒, is_final: [False]

收到第一句音频对应字幕，[你(0->510|final:False)]

收到第一句音频对应音素时间戳，[n(0->105|final:False)|i3(105->510|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 511, 'subtitles': [{'text': '你', 'start_msec': ec': 510, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'n', 'start_msec': 0, 'end_msec': 105, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'i3', 'start_msec': 105, 'end_msec': 510, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，168毫秒, is_final: [False]

收到第一句音频对应字幕，[的(0->168|final:False)]

收到第一句音频对应音素时间戳，[d(0->22|final:False)|e5(22->168|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 168, 'subtitles': [{'text': '的', 'start_msec': ec': 168, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'd', 'start_msec': 0, 'end_msec': 22, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'e5', 'start_msec': 22, 'end_msec': 168, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，343毫秒, is_final: [False]

收到第一句音频对应字幕，[AI(53->342|final:False)]

收到第一句音频对应音素时间戳，[EY1(53->215|final:False)|AY1(215->342|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 343, 'subtitles': [{'text': 'AI', 'start_msec': msec': 342, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'EY1', 'start_msec': 53, 'end_msec': 215, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'AY1', 'start_msec': 215, 'end_msec': 342, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，186毫秒, is_final: [False]

收到第一句音频对应字幕，[朋(0->185|final:False)]

收到第一句音频对应音素时间戳，[p(0->92|final:False)|eng2(92->185|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 186, 'subtitles': [{'text': '朋', 'start_msec': ec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'p', 'start_msec': 0, 'end_msec': 92, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'eng2', 'start_msec': 92, 'end_msec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，511毫秒, is_final: [False]

收到第一句音频对应字幕，[友，(0->207|final:False)]

收到第一句音频对应音素时间戳，[^(0->36|final:False)|iou5(36->207|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 511, 'subtitles': [{'text': '友，', 'start_msec'sec': 207, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': '^', 'start_msec': 0, 'end_msec': 36, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'iou5', 'start_msec': 36, 'end_msec': 207, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，557毫秒, is_final: [False]

收到第一句音频对应字幕，[有(507->557|final:False)]

收到第一句音频对应音素时间戳，[^(507->530|final:False)|iou3(530->557|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 557, 'subtitles': [{'text': '有', 'start_msec': msec': 557, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': '^', 'start_msec': 507, 'end_msec': 530, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'iou3', 'start_msec': 530, 'end_msec': 557, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，186毫秒, is_final: [False]

收到第一句音频对应字幕，[什(0->185|final:False)]

收到第一句音频对应音素时间戳，[sh(0->99|final:False)|en2(99->185|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 186, 'subtitles': [{'text': '什', 'start_msec': ec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'sh', 'start_msec': 0, 'end_msec': 99, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'en2', 'start_msec': 99, 'end_msec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，186毫秒, is_final: [False]

收到第一句音频对应字幕，[么(0->186|final:False)]

收到第一句音频对应音素时间戳，[m(0->24|final:False)|e5(24->186|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 186, 'subtitles': [{'text': '么', 'start_msec': ec': 186, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'm', 'start_msec': 0, 'end_msec': 24, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'e5', 'start_msec': 24, 'end_msec': 186, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，186毫秒, is_final: [False]

收到第一句音频对应字幕，[问(0->185|final:False)]

收到第一句音频对应音素时间戳，[^(0->86|final:False)|uen4(86->185|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 186, 'subtitles': [{'text': '问', 'start_msec': ec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': '^', 'start_msec': 0, 'end_msec': 86, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'uen4', 'start_msec': 86, 'end_msec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，185毫秒, is_final: [False]

收到第一句音频对应字幕，[题(0->185|final:False)]

收到第一句音频对应音素时间戳，[t(0->83|final:False)|i2(83->185|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 185, 'subtitles': [{'text': '题', 'start_msec': ec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 't', 'start_msec': 0, 'end_msec': 83, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'i2', 'start_msec': 83, 'end_msec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，186毫秒, is_final: [False]

收到第一句音频对应字幕，[就(0->185|final:False)]

收到第一句音频对应音素时间戳，[j(0->38|final:False)|iou4(38->185|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 186, 'subtitles': [{'text': '就', 'start_msec': ec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'j', 'start_msec': 0, 'end_msec': 38, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'iou4', 'start_msec': 38, 'end_msec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，139毫秒, is_final: [False]

收到第一句音频对应字幕，[尽(0->139|final:False)]

收到第一句音频对应音素时间戳，[j(0->69|final:False)|in2(69->139|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 139, 'subtitles': [{'text': '尽', 'start_msec': ec': 139, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'j', 'start_msec': 0, 'end_msec': 69, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'in2', 'start_msec': 69, 'end_msec': 139, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，186毫秒, is_final: [False]

收到第一句音频对应字幕，[管(0->185|final:False)]

收到第一句音频对应音素时间戳，[g(0->29|final:False)|uan2(29->185|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 186, 'subtitles': [{'text': '管', 'start_msec': ec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'g', 'start_msec': 0, 'end_msec': 29, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'uan2', 'start_msec': 29, 'end_msec': 185, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，186毫秒, is_final: [False]

收到第一句音频对应字幕，[找(0->186|final:False)]

收到第一句音频对应音素时间戳，[zh(0->96|final:False)|ao2(96->186|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 186, 'subtitles': [{'text': '找', 'start_msec': ec': 186, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': 'zh', 'start_msec': 0, 'end_msec': 96, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'ao2', 'start_msec': 96, 'end_msec': 186, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，139毫秒, is_final: [False]

收到第一句音频对应字幕，[我(0->139|final:False)]

收到第一句音频对应音素时间戳，[^(0->18|final:False)|uo3(18->139|final:False)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 139, 'subtitles': [{'text': '我', 'start_msec': ec': 139, 'level': 'UNKNOWN', 'children': [], 'is_final': False}], 'phoneme_timestamps': [{'text': '^', 'start_msec': 0, 'end_msec': 18, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'uo3', 'start_msec': 18, 'end_msec': 139, 'level': 'UNKNOWN', 'children': [], 'is_final': False}]}}

收到第一句音频，465毫秒, is_final: [True]

收到第一句音频对应字幕，[吧。(0->173|final:True)]

收到第一句音频对应音素时间戳，[b(0->28|final:False)|a5(28->173|final:True)]

收到响应message：{'task_id': 'ec4947abd1024af2ba07994adbeb0418', 'status': 1000, 'status_text': 'Success.', 'is_final': True, 'audio': '...音频内容...', 'addition': {'duration': 465, 'subtitles': [{'text': '吧。', 'start_msec':ec': 173, 'level': 'UNKNOWN', 'children': [], 'is_final': True}], 'phoneme_timestamps': [{'text': 'b', 'start_msec': 0, 'end_msec': 28, 'level': 'UNKNOWN', 'children': [], 'is_final': False}, {'text': 'a5', 'start_msec': 28, 'end_msec': 173, 'level': 'UNKNOWN', 'children': [], 'is_final': True}]}}

dump synthesized audio [6.2693877551020405]s to path ./gRPCClient.wav



## 文本流式[](https://docs.mthreads.com#文本流式)

`(TTS-FastSpeech) ➜ temp git:(main) ✗ PYTHONPATH=. MT_DEVELOPER_API_ACCESS_TOKEN="XXXX" python ws_client.py --mode bidi --voice AIBC006_llm `

--address ws://10.1.33.4:32414/api/v2/tts/stream_generate --enable_subtitle false --enable_phoneme_timestamp false --text_stream "你好，|||我是|||穆|||莎，你的|||AI|||朋友。有什|||么问题|||就尽管|||找我吧。"



MT_DEVELOPER_API_ACCESS_TOKEN: XXX

输入文本: ['你好，', '我是', '穆', '莎，你的', 'AI', '朋友。有什', '么问题', '就尽管', '找我吧。']

发送请求message：{'cluster': '', 'is_final': False, 'input': {'text': '你好，', 'text_type': 'plain', 'enable_subtitle': False, 'enable_phoneme_timestamp': False}, 'voice_config': {'voice_name': 'AIBC006_llm'}, 'audio_config': ratio': 1.0}}

send: {"cluster": "", "is_final": false, "input": {"text": "你好，", "text_type": "plain", "enable_subtitle": false, "enable_phoneme_timestamp": false}, "voice_config": {"voice_name": "AIBC006_llm"}, "audio_config": {"speed_rat: 1.0}}, wait 1s

发送请求message：{'cluster': '', 'is_final': False, 'input': {'text': '我是', 'text_type': 'plain', 'enable_subtitle': False, 'enable_phoneme_timestamp': False}, 'voice_config': {'voice_name': None}, 'audio_config': {'speed_rat0}}

send: {"cluster": "", "is_final": false, "input": {"text": "我是", "text_type": "plain", "enable_subtitle": false, "enable_phoneme_timestamp": false}, "voice_config": {"voice_name": null}, "audio_config": {"speed_ratio": 1.0}},ait 1s

发送请求message：{'cluster': '', 'is_final': False, 'input': {'text': '穆', 'text_type': 'plain', 'enable_subtitle': False, 'enable_phoneme_timestamp': False}, 'voice_config': {'voice_name': None}, 'audio_config': {'speed_ratio}}

send: {"cluster": "", "is_final": false, "input": {"text": "穆", "text_type": "plain", "enable_subtitle": false, "enable_phoneme_timestamp": false}, "voice_config": {"voice_name": null}, "audio_config": {"speed_ratio": 1.0}}, wit 1s

发送请求message：{'cluster': '', 'is_final': False, 'input': {'text': '莎，你的', 'text_type': 'plain', 'enable_subtitle': False, 'enable_phoneme_timestamp': False}, 'voice_config': {'voice_name': None}, 'audio_config': {'speed1.0}}

send: {"cluster": "", "is_final": false, "input": {"text": "莎，你的", "text_type": "plain", "enable_subtitle": false, "enable_phoneme_timestamp": false}, "voice_config": {"voice_name": null}, "audio_config": {"speed_ratio": 1. wait 1s

发送请求message：{'cluster': '', 'is_final': False, 'input': {'text': 'AI', 'text_type': 'plain', 'enable_subtitle': False, 'enable_phoneme_timestamp': False}, 'voice_config': {'voice_name': None}, 'audio_config': {'speed_ratio0}}

send: {"cluster": "", "is_final": false, "input": {"text": "AI", "text_type": "plain", "enable_subtitle": false, "enable_phoneme_timestamp": false}, "voice_config": {"voice_name": null}, "audio_config": {"speed_ratio": 1.0}}, wait 1s

发送请求message：{'cluster': '', 'is_final': False, 'input': {'text': '朋友。有什', 'text_type': 'plain', 'enable_subtitle': False, 'enable_phoneme_timestamp': False}, 'voice_config': {'voice_name': None}, 'audio_config': {'spe 1.0}}

send: {"cluster": "", "is_final": false, "input": {"text": "朋友。有什", "text_type": "plain", "enable_subtitle": false, "enable_phoneme_timestamp": false}, "voice_config": {"voice_name": null}, "audio_config": {"speed_ratio": , wait 1s

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': '9394cdab19ae4a0a93e23d1d978c0eca', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': '9394cdab19ae4a0a93e23d1d978c0eca', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

发送请求message：{'cluster': '', 'is_final': False, 'input': {'text': '么问题', 'text_type': 'plain', 'enable_subtitle': False, 'enable_phoneme_timestamp': False}, 'voice_config': {'voice_name': None}, 'audio_config': {'speed_r.0}}

send: {"cluster": "", "is_final": false, "input": {"text": "么问题", "text_type": "plain", "enable_subtitle": false, "enable_phoneme_timestamp": false}, "voice_config": {"voice_name": null}, "audio_config": {"speed_ratio": 1.0}wait 1s

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': '9394cdab19ae4a0a93e23d1d978c0eca', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': '9394cdab19ae4a0a93e23d1d978c0eca', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

发送请求message：{'cluster': '', 'is_final': False, 'input': {'text': '就尽管', 'text_type': 'plain', 'enable_subtitle': False, 'enable_phoneme_timestamp': False}, 'voice_config': {'voice_name': None}, 'audio_config': {'speed_r.0}}

send: {"cluster": "", "is_final": false, "input": {"text": "就尽管", "text_type": "plain", "enable_subtitle": false, "enable_phoneme_timestamp": false}, "voice_config": {"voice_name": null}, "audio_config": {"speed_ratio": 1.0}wait 1s

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': '9394cdab19ae4a0a93e23d1d978c0eca', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，232毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': '9394cdab19ae4a0a93e23d1d978c0eca', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 232, 'subtitles': [], 'phoneme_timestamps': []}}

发送请求message：{'cluster': '', 'is_final': True, 'input': {'text': '找我吧。', 'text_type': 'plain', 'enable_subtitle': False, 'enable_phoneme_timestamp': False}, 'voice_config': {'voice_name': None}, 'audio_config': {'speed_.0}}

send: {"cluster": "", "is_final": true, "input": {"text": "找我吧。", "text_type": "plain", "enable_subtitle": false, "enable_phoneme_timestamp": false}, "voice_config": {"voice_name": null}, "audio_config": {"speed_ratio": 1.0wait 1s

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': '9394cdab19ae4a0a93e23d1d978c0eca', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': '9394cdab19ae4a0a93e23d1d978c0eca', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，650毫秒, is_final: [False]

收到第一句音频对应字幕，[]

收到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': '9394cdab19ae4a0a93e23d1d978c0eca', 'status': 1000, 'status_text': 'Success.', 'is_final': False, 'audio': '...音频内容...', 'addition': {'duration': 650, 'subtitles': [], 'phoneme_timestamps': []}}

收到第一句音频，604毫秒, is_final: [True]

收到第一句音频对应字幕，[]

收�到第一句音频对应音素时间戳，[]

收到响应message：{'task_id': '9394cdab19ae4a0a93e23d1d978c0eca', 'status': 1000, 'status_text': 'Success.', 'is_final': True, 'audio': '...音频内容...', 'addition': {'duration': 604, 'subtitles': [], 'phoneme_timestamps': []}}

dump synthesized audio [6.03718820861678]s to path ./gRPCClient.wav