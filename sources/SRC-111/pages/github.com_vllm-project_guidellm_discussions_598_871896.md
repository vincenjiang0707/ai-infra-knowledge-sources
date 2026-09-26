source: https://github.com/vllm-project/guidellm/discussions/598

# Temp and topp #598

[Answered](https://github.com#discussioncomment-15827693)by

[sjmonson](https://github.com/sjmonson)

[martin1tab](https://github.com/martin1tab)asked this question in

[User Support](https://github.com/vllm-project/guidellm/discussions/categories/user-support)

[Temp and topp](https://github.com#top)#598

|
Hello, how can I pass the temp and top_k parameters to a benchmark run? |

Answered by

[sjmonson](https://github.com/sjmonson)Feb 16, 2026
## Replies: 1 comment

|
For GuideLLM v0.5.3: |

0 replies

Answer selected by

For GuideLLM v0.5.3:

`--request-formatter-kwargs '{"extras": {"body": {"temperature": 0.7}}}'`

For main (v0.6.0):

`--backend-kwargs '{"extras": {"body": {"temperature": 0.7}}}'`