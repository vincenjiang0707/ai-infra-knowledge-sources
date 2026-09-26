source: https://github.com/vllm-project/guidellm/discussions/520

# How to test a multimodal model？ #520

|
Hi team, I just learned about GuideLLM recently, and I tried to use a custom dataset to test a multimodal model(Qwen2.5-VL-3B-Instruct), but I found that the request sent was Incorrect. My dataset looks like: `{"image": "/path/text.jpeg", "text": "What do you see happening in this image?\n<image>"}` And the generated request body looks like: ```
{
"messages": [
{
"role": "user",
"content": [{"type": "text", "text": "What do you see happening in this image?\\n<image>'"}]
},
{
"role": "user",
"content": [{"type": "image_url", "image_url": "data:image/jpeg;basexxxxxx"}]
}]
}
``` But the request body expected to be generated looks like: ```
{
"messages": [
{
"role": "user",
"content": [
{"type": "text", "text": "What do you see happening in this image?\\n<image>'"},
{"type": "image_url", "image_url": "data:image/jpeg;basexxxxxx"}]
}]
}
``` My command looks like: ```
guidellm benchmark run \
--target http://xxxx \
--data /path/dataset.json \
--request-type chat_completions \
--profile constant \
--rate 1 \
--max-seconds 20
``` I'm not sure if I'm using it the wrong way, and I'm really looking forward to your support, Thanks. |

Answered by

Sorry, I lost track of this because I thought it was an issue. This was a regression on our side. See #594 and #595.