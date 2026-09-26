source: https://docs.openvino.ai/2025/about-openvino/performance-benchmarks/generative-ai-performance.html
lastmod: 

# Most Efficient Large Language Models for AI PC[#](https://docs.openvino.ai#most-efficient-large-language-models-for-ai-pc)

This page is regularly updated to help you identify the best-performing LLMs on the Intel® Core™ Ultra processor family and AI PCs. The current data is as of OpenVINO 2025.3, 3 September 2025.

The tables below list the key performance indicators for inference on built-in GPUs.

Topology | Precision | Input Size | 1st latency (ms) | 2nd latency (ms) | max rss memory | 2nd token per sec |
|---|---|---|---|---|---|---|
gemma-2b-it | INT4-MIXED | 32 | 55.3 | 30 | 3315.5 | 33.33 |
gemma-2b-it | INT4-MIXED | 1024 | 272 | 30.8 | 3106.4 | 32.47 |
stable-zephyr-3b-dpo | INT8-CW | 32 | 53.2 | 33.1 | 4303.3 | 30.21 |
dolly-v2-3b | INT4-MIXED | 32 | 147.5 | 35.7 | 3304.3 | 28.01 |
stable-zephyr-3b-dpo | INT8-CW | 1024 | 322.1 | 35.8 | 4605 | 27.93 |
phi-2 | INT4-MIXED | 32 | 130.3 | 36.6 | 3251.2 | 27.32 |
stable-zephyr-3b-dpo | INT4-MIXED | 32 | 131.9 | 38.5 | 3282.8 | 25.97 |
dolly-v2-3b | INT4-MIXED | 1024 | 503.3 | 38.7 | 3672.2 | 25.84 |
phi-3-mini-4k-instruct | INT4-MIXED | 32 | 95 | 39 | 3638.7 | 25.64 |
phi-2 | INT4-MIXED | 1024 | 473.2 | 39.8 | 3553.1 | 25.13 |
gemma-2b-it | INT8-CW | 32 | 56.6 | 40.4 | 3711.3 | 24.75 |
stable-zephyr-3b-dpo | INT4-MIXED | 1024 | 458.7 | 41.6 | 3558.9 | 24.04 |
gemma-2b-it | INT8-CW | 1024 | 236.5 | 41.9 | 3732.8 | 23.87 |
phi-3-mini-4k-instruct | INT4-MIXED | 1024 | 574 | 42.5 | 4161.3 | 23.53 |
stablelm-3b-4e1t | INT4-MIXED | 32 | 125.5 | 43 | 3363.8 | 23.26 |
dolly-v2-3b | INT8-CW | 32 | 105.8 | 43.7 | 4273.8 | 22.88 |
phi-2 | INT8-CW | 32 | 113.5 | 44.3 | 4174.4 | 22.57 |
stablelm-3b-4e1t | INT8-CW | 32 | 102.6 | 46.2 | 4300.8 | 21.65 |
stablelm-3b-4e1t | INT4-MIXED | 1024 | 412.2 | 47.2 | 3620.4 | 21.19 |
dolly-v2-3b | INT8-CW | 1024 | 428.4 | 47.9 | 4617.3 | 20.88 |
phi-2 | INT8-CW | 1024 | 398.4 | 48.1 | 4480.6 | 20.79 |
flan-t5-xxl | INT4-MIXED | 33 | 92.1 | 48.3 | 13700.3 | 20.70 |
chatglm3-6b | INT4-MIXED | 32 | 79.3 | 49 | 4991.2 | 20.41 |
gpt-j-6b | INT4-MIXED | 32 | 140.4 | 49.2 | 5042.7 | 20.33 |
stablelm-3b-4e1t | INT8-CW | 1024 | 407.3 | 49.4 | 4600.8 | 20.24 |
chatglm3-6b | INT4-MIXED | 1024 | 795.6 | 50.6 | 4623.4 | 19.76 |
gpt-j-6b | INT4-MIXED | 1024 | 722 | 52.7 | 6260.2 | 18.98 |
flan-t5-xxl | INT4-MIXED | 1139 | 261.1 | 53.9 | 15237.8 | 18.55 |
phi-3-mini-4k-instruct | INT8-CW | 32 | 80 | 56.7 | 5305.6 | 17.64 |
phi-3-mini-4k-instruct | INT8-CW | 1024 | 524 | 60.4 | 5629.9 | 16.56 |
chatglm3-6b | INT8-CW | 32 | 88.6 | 67.9 | 7536.3 | 14.73 |
chatglm3-6b | INT8-CW | 1024 | 479.2 | 69.8 | 7330.4 | 14.33 |
gpt-j-6b | INT8-CW | 32 | 99.5 | 71 | 7422.3 | 14.08 |
falcon-7b-instruct | INT4-MIXED | 32 | 113.6 | 71.5 | 5295.8 | 13.99 |
falcon-7b-instruct | INT4-MIXED | 1024 | 943.5 | 73 | 5040.6 | 13.70 |
gpt-j-6b | INT8-CW | 1024 | 557.3 | 75 | 8734.2 | 13.33 |
baichuan2-7b-chat | INT4-MIXED | 32 | 152.7 | 75.5 | 6518.7 | 13.25 |
mistral-7b-v0.1 | INT4-MIXED | 32 | 137.3 | 77.6 | 5731.8 | 12.89 |
baichuan2-7b-chat | INT4-MIXED | 1024 | 1583.3 | 79.1 | 7189.8 | 12.64 |
mistral-7b-v0.1 | INT4-MIXED | 1024 | 732.1 | 79.3 | 5595.9 | 12.61 |
zephyr-7b-beta | INT4-MIXED | 32 | 118.5 | 80.4 | 5987 | 12.44 |
zephyr-7b-beta | INT4-MIXED | 1024 | 724.4 | 82.4 | 5829.6 | 12.14 |
gemma-2b-it | FP16 | 32 | 91.4 | 83.1 | 6021.3 | 12.03 |
gemma-7b-it | INT4-MIXED | 32 | 127.6 | 83.7 | 6323.6 | 11.95 |
gemma-2b-it | FP16 | 1024 | 395.4 | 83.8 | 6137.8 | 11.93 |
dolly-v2-3b | FP16 | 32 | 105.6 | 86 | 6710.9 | 11.63 |
phi-2 | FP16 | 32 | 111.3 | 86.3 | 6934.2 | 11.59 |
gemma-7b-it | INT4-MIXED | 1024 | 1112.1 | 86.8 | 6894.6 | 11.52 |
stable-zephyr-3b-dpo | FP16 | 32 | 145.3 | 90.2 | 6954 | 11.09 |
dolly-v2-3b | FP16 | 1024 | 602 | 90.8 | 7525.8 | 11.01 |
phi-2 | FP16 | 1024 | 600.2 | 92 | 7523.2 | 10.87 |
stablelm-3b-4e1t | FP16 | 32 | 119.4 | 92.1 | 6861.9 | 10.86 |
qwen-7b-chat | INT4-MIXED | 32 | 133.3 | 93.7 | 7386.6 | 10.67 |
stable-zephyr-3b-dpo | FP16 | 1024 | 604.7 | 94.5 | 7539.5 | 10.58 |
stablelm-3b-4e1t | FP16 | 1024 | 610.1 | 96.2 | 7450.4 | 10.40 |
qwen-7b-chat | INT4-MIXED | 1024 | 736.9 | 98.1 | 7898 | 10.19 |

Topology | Precision | Input Size | 1st latency (ms) | 2nd latency (ms) | max rss memory | 2nd token per sec |
|---|---|---|---|---|---|---|
gemma-2b-it | INT4-MIXED | 32 | 28.6 | 17.7 | 3378 | 56.50 |
dolly-v2-3b | INT4-MIXED | 32 | 53.6 | 18.5 | 3424.4 | 54.05 |
gemma-2b-it | INT4-MIXED | 1024 | 196.7 | 18.6 | 3390.2 | 53.76 |
dolly-v2-3b | INT4-MIXED | 1024 | 392.5 | 21 | 3844.7 | 47.62 |
gemma-2b-it | INT8-CW | 32 | 35 | 28.3 | 3749.2 | 35.34 |
gemma-2b-it | INT8-CW | 1024 | 187.5 | 29.2 | 3893.1 | 34.25 |
dolly-v2-3b | INT8-CW | 32 | 49.8 | 30.9 | 4453 | 32.36 |
dolly-v2-3b | INT8-CW | 1024 | 363.7 | 33 | 4904.5 | 30.30 |
chatglm3-6b | INT4-MIXED | 32 | 49 | 33.9 | 5220.1 | 29.50 |
flan-t5-xxl | INT4-MIXED | 33 | 61.6 | 34.9 | 13722.1 | 28.65 |
chatglm3-6b | INT4-MIXED | 1024 | 465.7 | 36 | 5222.1 | 27.78 |
flan-t5-xxl | INT4-MIXED | 1139 | 223.5 | 39.1 | 15435.4 | 25.58 |
gpt-j-6b | INT4-MIXED | 32 | 72.4 | 39.6 | 5314 | 25.25 |
gpt-j-6b | INT4-MIXED | 1024 | 563.9 | 43.7 | 6473.2 | 22.88 |
zephyr-7b-beta | INT4-MIXED | 32 | 67 | 48.9 | 6141.4 | 20.45 |
baichuan2-7b-chat | INT4-MIXED | 32 | 65.7 | 50 | 6553.6 | 20.00 |
zephyr-7b-beta | INT4-MIXED | 1024 | 461 | 51.6 | 6114.5 | 19.38 |
baichuan2-7b-chat | INT4-MIXED | 1024 | 1605.2 | 54.4 | 7411.5 | 18.38 |
qwen-7b-chat | INT4-MIXED | 32 | 77.7 | 58.6 | 7451.7 | 17.06 |
gemma-2b-it | FP16 | 32 | 66.9 | 62.4 | 6240 | 16.03 |
gemma-2b-it | FP16 | 1024 | 242 | 63 | 6373.7 | 15.87 |
qwen-7b-chat | INT4-MIXED | 1024 | 476.6 | 63 | 8100.3 | 15.87 |
dolly-v2-3b | FP16 | 32 | 66 | 65.1 | 6938 | 15.36 |
chatglm3-6b | INT8-CW | 32 | 78.6 | 66.2 | 7591.9 | 15.11 |
chatglm3-6b | INT8-CW | 1024 | 430.1 | 68.6 | 7526.1 | 14.58 |
dolly-v2-3b | FP16 | 1024 | 433.2 | 68.8 | 7754 | 14.53 |
gpt-j-6b | INT8-CW | 32 | 85.9 | 75.1 | 7469.5 | 13.32 |
gpt-j-6b | INT8-CW | 1024 | 562.3 | 79.1 | 8937 | 12.64 |

Topology | Precision | Input Size | 1st latency (ms) | 2nd latency (ms) | max rss memory | 2nd token per sec |
|---|---|---|---|---|---|---|
dolly-v2-3b | INT4-MIXED | 32 | 70.8 | 23.6 | 3580.5 | 42.37 |
gemma-2b-it | INT4-MIXED | 32 | 58.8 | 24 | 4086.6 | 41.67 |
phi-2 | INT4-MIXED | 32 | 67.9 | 24.1 | 3782.8 | 41.49 |
gemma-2b-it | INT4-MIXED | 1024 | 712.9 | 24.8 | 4186.5 | 40.32 |
gemma-2b-it | INT4-MIXED | 4096 | 3135.2 | 25.3 | 4931.5 | 39.53 |
stable-zephyr-3b-dpo | INT4-MIXED | 32 | 76.3 | 25.4 | 3810.1 | 39.37 |
gemma-2b-it | INT4-MIXED | 2048 | 1440 | 25.5 | 4250 | 39.22 |
dolly-v2-3b | INT4-MIXED | 1024 | 1068.1 | 26.4 | 4119.8 | 37.88 |
phi-2 | INT4-MIXED | 1024 | 1043 | 27 | 4328.3 | 37.04 |
stablelm-3b-4e1t | INT4-MIXED | 32 | 68.5 | 27.9 | 3439.8 | 35.84 |
stable-zephyr-3b-dpo | INT4-MIXED | 1024 | 1051.4 | 28.3 | 4325.2 | 35.34 |
stable-zephyr-3b-dpo | INT4-MIXED | 2076 | 2677.9 | 31.1 | 4992.6 | 32.15 |
stablelm-3b-4e1t | INT4-MIXED | 1024 | 1057.3 | 31.1 | 4182.4 | 32.15 |
phi-3-mini-4k-instruct | INT4-MIXED | 32 | 94.5 | 32.3 | 4263.6 | 30.96 |
stablelm-3b-4e1t | INT4-MIXED | 2048 | 2564 | 33.7 | 5129.6 | 29.67 |
phi-3-mini-4k-instruct | INT4-MIXED | 1024 | 1366 | 35.9 | 4642.7 | 27.86 |
phi-3-mini-4k-instruct | INT4-MIXED | 2048 | 3183 | 38.9 | 5685.2 | 25.71 |
stable-zephyr-3b-dpo | INT8-CW | 32 | 84.6 | 39.2 | 4402.8 | 25.51 |
stablelm-3b-4e1t | INT4-MIXED | 4096 | 6621.6 | 39.2 | 7302 | 25.51 |
stablelm-3b-4e1t | INT8-CW | 32 | 82.9 | 39.3 | 4315.5 | 25.45 |
gemma-2b-it | INT8-CW | 32 | 85.4 | 39.5 | 4886.5 | 25.32 |
phi-2 | INT8-CW | 32 | 95 | 40.1 | 4447.6 | 24.94 |
gemma-2b-it | INT8-CW | 1024 | 791.5 | 40.2 | 4847.7 | 24.88 |
dolly-v2-3b | INT8-CW | 32 | 93.6 | 40.4 | 4614.8 | 24.75 |
gemma-2b-it | INT8-CW | 4096 | 3371.3 | 40.6 | 5799.9 | 24.63 |
gemma-2b-it | INT8-CW | 2048 | 1594.2 | 40.9 | 5115.9 | 24.45 |
stable-zephyr-3b-dpo | INT8-CW | 1024 | 1177.2 | 42.1 | 5124.4 | 23.75 |
stablelm-3b-4e1t | INT8-CW | 1024 | 1174.4 | 42.3 | 5037 | 23.64 |
phi-2 | INT8-CW | 1024 | 1145.9 | 43 | 5183.6 | 23.26 |
dolly-v2-3b | INT8-CW | 1024 | 1171.3 | 43.3 | 5172.3 | 23.09 |
stable-zephyr-3b-dpo | INT8-CW | 2076 | 4070 | 44.8 | 5927.9 | 22.32 |
stablelm-3b-4e1t | INT8-CW | 2048 | 2797.1 | 44.8 | 5950 | 22.32 |
phi-3-mini-4k-instruct | INT4-MIXED | 4096 | 8047.2 | 45.1 | 8019.5 | 22.17 |
gpt-j-6b | INT4-MIXED | 32 | 136 | 48.1 | 5306.2 | 20.79 |
flan-t5-xxl | INT4-MIXED | 33 | 79.3 | 48.2 | 14071 | 20.75 |
chatglm3-6b | INT4-MIXED | 32 | 147.4 | 48.7 | 5063.6 | 20.53 |
chatglm3-6b | INT4-MIXED | 1024 | 1877.2 | 50.1 | 5267.6 | 19.96 |
stablelm-3b-4e1t | INT8-CW | 4096 | 7094.2 | 50.1 | 8047.9 | 19.96 |
chatglm3-6b | INT4-MIXED | 2048 | 4009.4 | 51.4 | 5677 | 19.46 |
chatglm3-6b | INT4-MIXED | 4096 | 8779.6 | 51.5 | 7111.5 | 19.42 |
flan-t5-xxl | INT4-MIXED | 1139 | 376.5 | 52 | 15851.9 | 19.23 |
gpt-j-6b | INT4-MIXED | 1024 | 2112.5 | 52.2 | 6915.4 | 19.16 |
phi-3-mini-4k-instruct | INT8-CW | 32 | 101.5 | 53 | 5272.3 | 18.87 |
falcon-7b-instruct | INT4-MIXED | 32 | 172.6 | 55.7 | 5732.4 | 17.95 |
gpt-j-6b | INT4-MIXED | 2048 | 4759.6 | 56.2 | 9203.4 | 17.79 |
phi-3-mini-4k-instruct | INT8-CW | 1024 | 1556.7 | 56.4 | 6118 | 17.73 |
flan-t5-xxl | INT4-MIXED | 2048 | 664 | 56.7 | 20616.4 | 17.64 |
falcon-7b-instruct | INT4-MIXED | 1024 | 2316 | 57.1 | 6052.5 | 17.51 |
phi-3-mini-4k-instruct | INT8-CW | 2048 | 3593.9 | 59.3 | 7165.8 | 16.86 |
mistral-7b-v0.1 | INT4-MIXED | 32 | 180 | 61 | 5781.8 | 16.39 |
mistral-7b-v0.1 | INT4-MIXED | 1024 | 2311.4 | 63.2 | 6227 | 15.82 |
mistral-7b-v0.1 | INT4-MIXED | 2048 | 4931.2 | 65.2 | 6883.6 | 15.34 |
phi-3-mini-4k-instruct | INT8-CW | 4096 | 8851 | 65.4 | 9741.2 | 15.29 |
zephyr-7b-beta | INT4-MIXED | 32 | 172 | 65.7 | 6387.4 | 15.22 |
mistral-7b-v0.1 | INT4-MIXED | 4096 | 10822.1 | 66.1 | 8790.2 | 15.13 |
baichuan2-7b-chat | INT4-MIXED | 32 | 155.4 | 66.7 | 6847.8 | 14.99 |
flan-t5-xxl | INT4-MIXED | 4096 | 1368.2 | 67.5 | 30669.4 | 14.81 |
zephyr-7b-beta | INT4-MIXED | 1024 | 2313.7 | 67.8 | 6530.2 | 14.75 |
gemma-7b-it | INT4-MIXED | 32 | 231.5 | 68.8 | 7265.1 | 14.53 |
gemma-2b-it | FP16 | 32 | 91.8 | 69.1 | 7829.9 | 14.47 |
gemma-2b-it | FP16 | 1024 | 1398.2 | 69.9 | 7656.5 | 14.31 |
gemma-2b-it | FP16 | 2048 | 2977.5 | 70.7 | 7982.2 | 14.14 |
baichuan2-7b-chat | INT4-MIXED | 1024 | 2771.3 | 71 | 7753.8 | 14.08 |
phi-2 | FP16 | 32 | 99.8 | 71.1 | 7066.5 | 14.06 |
gemma-2b-it | FP16 | 4096 | 6309.8 | 71.2 | 8607.5 | 14.04 |
stable-zephyr-3b-dpo | FP16 | 32 | 94.7 | 71.3 | 7072.5 | 14.03 |
stablelm-3b-4e1t | FP16 | 32 | 94.5 | 71.3 | 6980.7 | 14.03 |
dolly-v2-3b | FP16 | 32 | 98.8 | 71.6 | 7211 | 13.97 |
gemma-7b-it | INT4-MIXED | 1024 | 2832 | 72.8 | 8247.3 | 13.74 |
baichuan2-7b-chat | INT4-MIXED | 2048 | 5351.1 | 75.1 | 9136.2 | 13.32 |
phi-2 | FP16 | 1024 | 1376.9 | 75.7 | 8097.9 | 13.21 |
stable-zephyr-3b-dpo | FP16 | 1024 | 1375.4 | 75.8 | 8106.4 | 13.19 |
stablelm-3b-4e1t | FP16 | 1024 | 1382.8 | 75.8 | 8020.3 | 13.19 |
dolly-v2-3b | FP16 | 1024 | 1405.3 | 76.3 | 8093.4 | 13.11 |
qwen-7b-chat | INT4-MIXED | 32 | 145.9 | 76.4 | 7648.4 | 13.09 |
gemma-7b-it | INT4-MIXED | 2048 | 6079.5 | 77 | 9493.9 | 12.99 |
stablelm-3b-4e1t | FP16 | 2048 | 3170.1 | 80.3 | 9339.1 | 12.45 |
stable-zephyr-3b-dpo | FP16 | 2076 | 9419.9 | 80.4 | 9101 | 12.44 |
qwen-7b-chat | INT4-MIXED | 1024 | 2405.7 | 80.7 | 8483.9 | 12.39 |
gpt-j-6b | INT8-CW | 32 | 142.1 | 81.9 | 7614 | 12.21 |
baichuan2-7b-chat | INT4-MIXED | 3968 | 12508.6 | 83.2 | 9938 | 12.02 |
flan-t5-xxl | INT8-CW | 33 | 123.9 | 83.2 | 23446.4 | 12.02 |
gemma-7b-it | INT4-MIXED | 4096 | 14292.9 | 84.9 | 11672.5 | 11.78 |
qwen-7b-chat | INT4-MIXED | 2048 | 5429.1 | 85.2 | 9822.4 | 11.74 |
chatglm3-6b | INT8-CW | 32 | 143 | 85.4 | 7618.1 | 11.71 |
gpt-j-6b | INT8-CW | 1024 | 2307.9 | 86.1 | 9248.2 | 11.61 |
chatglm3-6b | INT8-CW | 1024 | 2472.9 | 86.8 | 7824.2 | 11.52 |
flan-t5-xxl | INT8-CW | 1139 | 471 | 86.8 | 25692.8 | 11.52 |
chatglm3-6b | INT8-CW | 2048 | 5232.6 | 88 | 8354.6 | 11.36 |
chatglm3-6b | INT8-CW | 4096 | 11328.1 | 88.1 | 9675.8 | 11.35 |
stablelm-3b-4e1t | FP16 | 4096 | 7736.9 | 89.1 | 12203.8 | 11.22 |
gpt-j-6b | INT8-CW | 2048 | 5140 | 90.2 | 11542.2 | 11.09 |
flan-t5-xxl | INT8-CW | 2048 | 804.4 | 91.4 | 30371.1 | 10.94 |
falcon-7b-instruct | INT8-CW | 32 | 171.9 | 93.7 | 8415.5 | 10.67 |
qwen-7b-chat | INT4-MIXED | 4096 | 13230.6 | 93.7 | 12824.2 | 10.67 |
falcon-7b-instruct | INT8-CW | 1024 | 2564.1 | 95.1 | 8741.2 | 10.52 |
phi-3-mini-4k-instruct | FP16 | 32 | 121.4 | 98.8 | 9057.3 | 10.12 |
baichuan2-7b-chat | INT8-CW | 32 | 152 | 99.3 | 9002 | 10.07 |

All models listed here were tested with the following parameters:

Framework: PyTorch

Beam: 1

Batch size: 1