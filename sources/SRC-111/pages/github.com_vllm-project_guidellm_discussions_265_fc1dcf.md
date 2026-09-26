source: https://github.com/vllm-project/guidellm/discussions/265

# I want to disable thinking for thinking models in load testing #265

[Answered](https://github.com#discussioncomment-14036048)by

[sjmonson](https://github.com/sjmonson)

[psydok](https://github.com/psydok)asked this question in

[User Support](https://github.com/vllm-project/guidellm/discussions/categories/user-support)

|
How do I do this when testing the load through guidellm? |

[sjmonson](https://github.com/sjmonson)

Aug 7, 2025

## Replies: 3 comments 4 replies

|
You can specify extra request parameters using the |

[psydok](https://github.com/psydok)

|
I want to run test through docker. Can you tell me how it would be correct to pass these values through environment variables? Would it be right to do it this way? And how can this be done through env? ```
sudo docker run \
--rm -it \
-v "./data/guidellm:/results:rw" \
-e GUIDELLM_TARGET=http://localhost:8000 \
-e GUIDELLM_MODEL=Qwen/Qwen3-30B-A3B \
-e GUIDELLM_PROCESSOR=Qwen/Qwen3-30B-A3B \
-e GUIDELLM_RANDOM_SEED=2025 \
-e GUIDELLM_RATE_TYPE=concurrent -e GUIDELLM_RATE=1,3,5,8 \
-e GUIDELLM_MAX_SECONDS=300 \
-e GUIDELLM_DATA="prompt_tokens=4096,output_tokens=512" \
-e GUIDELLM__PREFERRED_ROUTE="chat_completions" \
-e GUIDELLM__REQUEST_HTTP2=0 \
ghcr.io/vllm-project/guidellm:latest -- --backend-args='{"extra_body":{"chat_template_kwargs":{"enable_thinking":false}}}'
``` |

|
The above did not work. I tried passing it like this: Thank you very much! |

You can specify extra request parameters using the

`extra_body`

backend arg:`--backend-args='{"extra_body":{"chat_template_kwargs":{"enable_thinking":false}}}'`