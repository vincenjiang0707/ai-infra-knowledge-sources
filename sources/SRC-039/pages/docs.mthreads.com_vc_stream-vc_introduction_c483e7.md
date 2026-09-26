source: https://docs.mthreads.com/vc/stream-vc/introduction

# 流式音色转换WebSocket API

## 使用说明[](https://docs.mthreads.com#使用说明)

基于websocket的流式音色转换接口。

### 目录[](https://docs.mthreads.com#目录)

## 使用要求[](https://docs.mthreads.com#使用要求)

| 项目 | 要求 |
|---|---|
| 发送格式 | 当发送音频数据时采用二进制格式，其他采用文本格式发送json数据 |
| 响应格式 | 当接收音频数据时采用二进制格式，其他采用文本格式返回json数据 |
| 输入音频数据属性 | 仅支持采样率16k，16bit，单通道PCM数据 |
| 输入音频格式 | PCM（无压缩的PCM或WAV音频流） 音频需满足采样率16k、位长16bit、单声道；其他格式需满足采样率16k、单声道 |
| 数据发送 | 建议音频流每1000ms发送一次，每次发送1000ms的数据。发送间隔必须严格等于发送的数据量。如果发送间隔大于发送的数据量，可能会导致流式结果的卡顿 建立请求后，数据发送间隔不能超过10s。若长时间为发送数据（超过10s），服务会返回错误消息并结束识别 如果用户发送数据过快，可能导致引擎出现过载错误 |

## 服务地址与鉴权方式[](https://docs.mthreads.com#服务地址与鉴权方式)

**外网访问地址：** `wss://aibook-api.mthreads.com:32314/api/v1/streaming_vc`


**鉴权方式:**

在URL中使用鉴权token:

`wss://aibook-api.mthreads.com:32314/api/v1/streaming_vc?token=${your_token}`




注意:访问令牌（Access Token）请联系我们获取。联系方式：[meng.cai@mthreads.com],[ye.wang@mthreads.com]

## 交互流程[](https://docs.mthreads.com#交互流程)

## 发送请求[](https://docs.mthreads.com#发送请求)

### 开始转换[](https://docs.mthreads.com#开始转换)

开始转换时，首先以json格式传输相关配置。

| 参数 | 类型 | 层级 | 必填 | 说明 |
|---|---|---|---|---|
| type | String | 1 | 是 | 消息类型，开始转换时需使用"StartConversion" |
| payload | Dict | 1 | 是 | 指定输入输出音频格式 |
| voice | String | 2 | 是 | 目标音色名称，可用名称见"说话人列表"部分 |
| input_info | Dict | 2 | 是 | 输入音频相关参数 |
| sample_rate | Integer | 3 | 是 | 输入音频采样率，仅支持16000 |
| channels | Integer | 3 | 是 | 输入音频通道数，仅支持1 |
| bits | Integer | 3 | 是 | 输入音频位长，仅支持16 |
| audio_encoding | String | 3 | 是 | 输入音频编码格式，仅支持pcm |
| output_info | Dict | 2 | 是 | 输出音频相关参数 |
| sample_rate | Integer | 3 | 是 | 输出音频采样率，仅支持48000 |
| channels | Integer | 3 | 是 | 输出音频通道数，仅支持1 |
| bits | Integer | 3 | 是 | 输出音频位长，仅支持16 |
| audio_encoding | String | 3 | 是 | 输出音频编码格式，仅支持pcm |

**示例：**

`{`

"type":"StartConversion",

"payload":{

"voice":"xiaoling",

"input_info":{

"sample_rate":16000,

"channels":1,

"bits":16,

"audio_encoding":"pcm"

},

"output_info":{

"sample_rate":48000,

"channels":1,

"bits":16,

"audio_encoding":"pcm"

}

}

}



### 发送数据[](https://docs.mthreads.com#发送数据)

发送二进制音频数据

### 结束转换[](https://docs.mthreads.com#结束转换)

结束转换时，将type设置为"StopConversion"

| 参数 | 类型 | 层级 | 必填 | 说明 |
|---|---|---|---|---|
| type | String | 1 | 是 | 消息类型，结束转换时需使用"StopConversion" |

**示例：**

`{`

"type":"StopConversion"

}



## 返回信息[](https://docs.mthreads.com#返回信息)

### 转换正常开始[](https://docs.mthreads.com#转换正常开始)

发送"开始转换"的请求后，如果服务正常开始，则返回"转换正常开始"的响应。响应采用json编码，说明如下：

| 参数 | 类型 | 说明 |
|---|---|---|
| type | String | 消息类型，此时为："ConversionStarted" |
| task_id | String | 用于记录本次会话的任务ID |
| status | Integer | 状态码 |
| status_text | String | 状态消息 |

**示例：**

`{`

"type":"ConversionStarted",

"task_id":"task_id",

"status":1000,

"status_text":"success"

}



### 返回转换后的数据[](https://docs.mthreads.com#返回转换后的数据)

返回二进制音频数据

### 转换正常结束[](https://docs.mthreads.com#转换正常结束)

转换结束后返回响应中type为"ConversionCompleted"

| 参数 | 类型 | 说明 |
|---|---|---|
| type | String | 消息类型，此时为："ConversionCompleted" |
| task_id | String | 用于记录本次会话的任务ID |
| status | Integer | 状态码 |
| status_text | String | 状态消息 |

**示例：**

`{`

"type":"ConversionCompleted",

"task_id":"task_id",

"status":1000,

"status_text":"success"

}



### 转换错误[](https://docs.mthreads.com#转换错误)

若转换过程中发生错误，则返回type为"Error"的响应

**示例：**

`{`

"type":"Error",

"task_id":"task_id",

"status":3002,

"status_text":"service timeout"

}



## 支持音色[](https://docs.mthreads.com#支持音色)

| 音色名称 | 性别 | 参数值 |
|---|---|---|
| 晓凌 | 女 | xiaoling |

## 状态码[](https://docs.mthreads.com#状态码)

| 状态码 | 状态文本 | 说明 |
|---|---|---|
| 1000 | success! | 成功 |
| 1001 | queueing | 排队中 |
| 1002 | running | 识别中 |
| 2001 | appid doesn't exist! | appid不存在 |
| 2002 | authorization failed. | 鉴权失败 |
| 2003 | too many requests | 并发数量过多 |
| 2004 | service overload | 数据发送过快，服务超负荷 |
| 3001 | service is busy | 服务器忙 |
| 3002 | service timeout | 服务处理超时 |
| 3003 | client is disconnected | 未完成前客户端主动断开 |
| 3004 | error occured during processing | 识别过程中发生错误 |
| 3005 | cannot find the taskid | 任务过期，或taskid不存在 |
| 4001 | unknown parameter is given. | 输入了未知/不支持的参数 |
| 4002 | given value is invalid | 参数值非法 |
| 4003 | request invalid | 请求消息格式错误 |
| 4004 | fail to read the audio | 音频解码失败 |
| 4005 | unsupported audio format | 音频格式不支持 |
| 4006 | audio too large | 音频文件过大 |
| 4007 | audio too long | 音频时长过长 |
| 4008 | fail to download the audio file | 文件下载失败 |
| 4009 | data timeout | 发送数据超时，等待下一包太久，导致识别结束 |
| 4010 | url is invalid | URL非法 |
| 4011 | callback url is invalid | callback URL非法 |
| 4012 | fail to check content-length | content-length 检查失败 |
| 4013 | fail to check md5 | 音频md5校验失败 |
| 4014 | fail to upload audio data | 文件上传失败或超时 |
| 4015 | duplicated upload done detected | 重复发送UploadDone |
| 4016 | duplicated start detected | 未按照规定的交互流程发送请求 |
| 5001 | unsupported voice | 不支持音色 |

## 示例代码[](https://docs.mthreads.com#示例代码)

请参考：[https://github.com/yiliu-mt/mtvc_examples/blob/master/streaming_vc/python/streaming_demo.py](https://github.com/yiliu-mt/mtvc_examples/blob/master/streaming_vc/python/streaming_demo.py)