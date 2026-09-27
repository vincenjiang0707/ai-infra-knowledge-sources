# [Issue #4256] [feat][MP] Support separate cache key by user through lmcache tags

source: https://github.com/LMCache/LMCache/issues/4256
state: open | updated: 2026-09-27T01:55:58Z
labels: stale

## 正文

**Label**
Please label your issue with "new feature" and any other relevant labels so that it can easily be easily categorized under [LMCache Onboarding](https://github.com/LMCache/LMCache/issues/1882)

**Is your feature request related to a problem? Please describe.**

In our case, we should to separate cache data by user field，then I add tags: OrderedDict for the extention

How to use:
add user field to kv_transfer_params

```shell
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
    "model": "deepseek-r1",
    "messages": [
        {
            "role": "user",
            "content": "Hello, how are you?"
        }
    ],
    "max_tokens": 1000,
    "temperature": 0,
    "top_p": 0.95,
    "stream": true,
    "stream_options": {
         "include_usage": true
    },
    "kv_transfer_params":{
            "user":"example_user_id"
        }
    }'
```

This feature has been land to in-process mode by https://github.com/LMCache/LMCache/pull/1200 , now we need to port it to mp mode.

**Describe the solution you'd like**
A clear and concise description of what you want to happen.

**Describe alternatives you've considered**
A clear and concise description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.


## 评论 (3)

### maobaolong · 2026-07-27

@ApostaC Issue has been created, we can use this issue to track.

### maobaolong · 2026-07-28

https://github.com/LMCache/LMCache/pull/4280 This is a draft PR.

### github-actions[bot] · 2026-09-27

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.
