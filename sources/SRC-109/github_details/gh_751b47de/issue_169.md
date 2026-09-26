# [Issue #169] Input file when profiling

source: https://github.com/triton-inference-server/perf_analyzer/issues/169
state: closed | updated: 2024-11-14T18:19:14Z
labels: question

## 正文

I want to make a profile with genai-perf, using my custom dataset, using the "--input-file".
My **inputs.json** is formatted as following:
`{"text": "my text"}\n{"text": "another text"}`
I then execute the command: 
```
genai-perf profile \
            -m my_model_name \
            --service-kind openai \
            --backend vllm \
            --endpoint v1/chat/completions \
            --endpoint-type chat \
            --input-file /workspace/inputs.json \
            --streaming \
            --generate-plots \
            --output-tokens-mean 500 \
            --output-tokens-stddev 0 \
            --concurrency 2 \
            --measurement-interval 10000 \
            --profile-export-file exported_file.json \
            --url ip:port \
            -- -H "Authorization: Bearer myapikey" -H "Accept: text/event-stream"
```

Then inside the artifacts folder, an inputs.json file is created, with the following: 
`{
  "data": [
    {
      "payload": [
        {
          "messages": [],
          "model": "my_model_name",
          "stream": true,
          "max_tokens": 500
        }
      ]
    },
    {
      "payload": [
        {
          "messages": [],
          "model": "my_model_name",
          "stream": true,
          "max_tokens": 500
        }
      ]
    }
  ]`.
As you can see the messages field is empty, so the result is the following: 
```
Failed to retrieve results from inference request.
Thread [0] had error: OpenAI response returns HTTP code 400

Thread [1] had error: OpenAI response returns HTTP code 400.
```
Which is the correct format of the file submitted with **--input-file**?
**SOLUTION:**
The correct format of the inputs.json file:
`{"text_input": "my text"}\n{"text_input": "another text"}`

## 评论 (1)

### the-david-oy · 2024-11-07

Thanks for opening this issue and sharing the solution! The main branch has been updated to allow both text and text_input as a part of a larger refactor that cleaned up disparities between how input files worked across endpoints. This additional flexibility will be included in the next release. If you are not building off the main branch, I recommend following the documentation for the branch you are on.

Our beta is moving toward stability, and we plan to have full stability (full backwards compatibility) for our GA release.
