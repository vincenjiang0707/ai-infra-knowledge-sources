# [Issue #504] OpenAI backend validation fails with 401 Unauthorized when API key authentication is required

source: https://github.com/vllm-project/guidellm/issues/504
state: closed | updated: 2026-06-24T18:12:07Z
labels: 

## 正文

**Describe the bug**
The OpenAI backend's validate() method fails when connecting to OpenAI-compatible API endpoints that require authentication on their health check endpoints. The validation request to the /health endpoint does not include the Authorization header, causing a 401 Unauthorized error even when a valid API key is provided.

**Expected behavior**
When using --backend-type openai_http with a valid API key, the backend validation should successfully authenticate against the remote server's health endpoint.

**Actual behavior**
httpx.HTTPStatusError: Client error '401 Unauthorized' for url 'https://my-server/health'
RuntimeError: Backend validation request failed. Could not connect to the server or validate the backend

**Environment**
Include all relevant environment information:
`guidellm version: 0.4.0`
`Python 3.12.12`

**To Reproduce**
Exact steps to reproduce the behavior:

1. Set environment variables for the key and base url (GUIDELLM__OPENAI__API_KEY, BASE_URL)
2. Run the benchmark

```
guidellm benchmark run \
  --target "$BASE_URL" \ 
  --backend-type openai_http \
  --model "model" \
  --rate-type constant --rate 1 \
  --max-requests 10 \
  --data 'prompt_tokens=256,output_tokens=128'
```

**Additional Context**
Refer to #491 


## 评论 (8)

### arno4000 · 2025-12-09

I have currently exactly the same issue.

### sjmonson · 2025-12-11

Sorry, support for `GUIDELLM__OPENAI__API_KEY` was accidentally wiped out in v0.4.0. Assuming you don't need multi-modal you can switch to v0.3.1 and it should work. Will be fixed after #491.

### marcherr89 · 2026-04-17

Are there any plans to reactivate the environment variable GUIDELLM__OPENAI_API_KEY? In the current version (0.6.0), it does not work in the image. Unfortunately, using GUIDELLM_BACKEND_KWARGS is not a viable option for me, because I would first have to adapt the format.

### lfreinag · 2026-05-25

I had the same issue here but I just used the --backend-kwargs as documented here: https://github.com/vllm-project/guidellm/blob/main/docs/guides/backends.md#api-key-configuration

Note that: 

> The API key is used to set the Authorization: Bearer {api_key} header in HTTP requests to the backend server.

So you should be able to use:  `--backend-kwargs "{\"api_key\": \"$GUIDELLM__OPENAI_API_KEY\"}" \`. This worked for me at least 😄 Hope it helps someone or you @marcherr89. 


### lfreinag · 2026-05-25

Or you could also define more headers with for example:

```
--backend-kwargs '{\
    "api_key": "token1",\
    "validate_backend": false,\ #no /health in the API
    "extras": {\
      "headers": {\
        "application_unique_id": "test",\
        "other_info": "other",\
        "Content-Type": "application/json"\
      }\
    }}'
```
 

### marcherr89 · 2026-06-02

@lfreinag 
As I mentioned, this is not a viable approach for me, since my API key is stored in a secret and I run the Guidllm container image as a job. Therefore, when passing parameters via the GUIDELLM_BACKEND_KWARGS environment variable, I cannot subsequently format the API key or add additional parameters to the dictionary.

### sjmonson · 2026-06-02

Would `API_KEY=xyz` and `--backend-kwargs "{\"api_key\": \"$API_KEY\"}"` work? As part of #724 I'll be attempting to make nested ENV vars work which should solve this in the future.

### sjmonson · 2026-06-24

To clarify why this is closed: you can now use `GUIDELLM__SPEC__BACKEND__API_KEY=xyz` to set the API key. The first release this will appear in will be v0.7.0.
