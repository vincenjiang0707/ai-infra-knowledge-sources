# [Issue #2638] An error occurs when aibrix calls the model,   gateway_rsp_body.go: "{\\\"error\\\":{\\\"code\\\":null,\\\"message\\\":\\\"malformed JSON in SSE stream\\\",\\\"param\\\":null,\\\"type\\\":\\\"api_error\\\"}}\"}"

source: https://github.com/vllm-project/aibrix/issues/2638
state: closed | updated: 2026-09-13T17:31:01Z
labels: 

## 正文

### 🐛 Describe the bug

An error occurs when aibrix calls the model, 

In the `HandleResponseBody` function in `pkg\plugins\gateway\gateway_rsp_body.go`:

```go
if !gjson.ValidBytes(jsonBytes) {
    complete = true
    return generateErrorResponse(
        envoyTypePb.StatusCode_InternalServerError,
        []*configPb.HeaderValueOption{{Header: &configPb.HeaderValue{
            Key: HeaderErrorStreaming, RawValue: []byte("true"),
        }}},
        "malformed JSON in SSE stream", "", ""), complete
}
```


HandleResponseBody is Envoy external processing (ext_proc) plugin callback. The request data received here is split by TCP, not complete data. Why is there a mandatory check for the data to be complete JSON format in the method mentioned above? I think it should be judged after being spliced completely.


### Steps to Reproduce

1. aibrix 0.5.0
2. deploy deepseek-v4-flash-0731 model
3. invoke model (stream=True)

### Expected behavior

1 ouput complete data

### Environment

1. aibrix 0.5.0

## 评论 (4)

### varungup90 · 2026-08-31

@XiaozanZhang  can you please upgrade to latest release and try

### XiaozanZhang · 2026-09-01

@varungup90 hi, I read the code of the latest version 0.7.0, regarding this part of the exception-related code, there is no difference from 0.5.0.I think it still needs to be fixed and resolved.

### varungup90 · 2026-09-01

@XiaozanZhang We run this model in production and it works fine. Code deployed in our internal production cluster is closer to main branch.

can you try once to use build from main branch or you can use this test build `aibrix-public-release-cn-beijing.cr.volces.com/aibrix/gateway-plugins:v0.8.0-vke-test`

### varungup90 · 2026-09-13

feel free to re-open the issue if still present
