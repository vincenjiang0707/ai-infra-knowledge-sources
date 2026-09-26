source: https://github.com/vllm-project/guidellm/discussions/312

# use guidellm to test vllm benchmark (with litellm proxy), failed #312

[Answered](https://github.com#discussioncomment-14366033)by

[mubashir1osmani](https://github.com/mubashir1osmani)

[liyuerich](https://github.com/liyuerich)asked this question in

[User Support](https://github.com/vllm-project/guidellm/discussions/categories/user-support)

|
try to use guidellm to test vllm benchmark (with litellm proxy), failed 1 setup vllm service 2 setup litellm proxy litellm_config.yaml
litellm --config config.yaml --port 4000 3 use curl to access vllm service and litellm proxy directly , both works fine. 4 run guidellm , failed guidellm benchmark --target "
|

[mubashir1osmani](https://github.com/mubashir1osmani)

Sep 10, 2025

## Replies: 9 comments 1 reply

|
try to ask RunLLM, the answer is not helpful. |

|
Hi |

|
get detailed debug logs from litellm
|

|
not sure where "max_completion_tokens" comes from? all the request setup , there is no "max_completion_tokens" . |

|
litellm supports max_completion_tokens - try adding |

[sjmonson](https://github.com/sjmonson)

|
Yeah due to this mess we have to emit both See also |

|
curl to litellm with different parameter, get error: curl curl |

|
refer this doc to setup config.yaml to ignore the parameters, still get the same error. |

litellm supports max_completion_tokens - try adding

`litellm.drop_params=True`

ref: https://docs.litellm.ai/docs/completion/input