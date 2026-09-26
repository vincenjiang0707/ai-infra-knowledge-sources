# [Issue #1302] 部分数据集评测实际结果比官方低很多（在差值为30%的情况下，无法复现/接近官方数据）

source: https://github.com/modelscope/evalscope/issues/1302
state: closed | updated: 2026-07-08T06:15:37Z
labels: 

## 正文


## 问题描述
最近在使用evalscope评测的时候，有一些疑惑：实际测试出来结果比官方公布的低很多，不清楚是什么原因？

请简要描述您遇到的问题。
无法复现官方的测试数据

## EvalScope 版本（必填）
evalscope 0.0.0_dev
(git pull https://github.com/modelscope/evalscope.git)之后自行在本地编译的，2026_0416那天pull的代码


## 执行的代码或指令
evalscope eval \
    --model deepseek-ai/DeepSeek-V3.1-Terminus \
    --api-url ####### \
    --api-key ################ \
    --datasets hle \
    --judge-model-args '{"model_id": "gpt-4.1-mini", "api_url": "#########", "api_key": "############3"}' \
    --dataset-args '{"hle": {"extra_params": {"include_multi_modal": false}}}'

## 运行环境

- 操作系统：
- Python版本：py312



## 评论 (18)

### twilighgt · 2026-04-20

自行测试出来的结果显示：<img width="1003" height="343" alt="Image" src="https://github.com/user-attachments/assets/de10c47b-df25-4fb6-b78f-1054e172b95b" />

官方提供的结果显示：<img width="637" height="279" alt="Image" src="https://github.com/user-attachments/assets/261e0393-7e03-4014-a9fd-047b13e1cbb3" />

### twilighgt · 2026-04-20

evalscope给了一些可能的结果异常排查方向：[https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html#id6](结果异常与问题排查)
尝试增加了以下两个参数：
--dataset-args '{"hle": {"extra_params": {"include_multi_modal": false}}, "ifeval": {"filters": {"remove_until": "</think>"}}}' \
--generation-config '{"max_tokens": 32000, "temperature": 0.0}' \
并且将裁判模型换成gpt-5.1-chat
依旧无法复现官方的测试结果，跑出来数据很低

### Yunnglin · 2026-04-20

@twilighgt 使用可视化工具看下模型每个样本的输出结果是否正常：https://evalscope.readthedocs.io/zh-cn/latest/get_started/visualization.html

### twilighgt · 2026-04-21

@Yunnglin 由于HLE用例实在太多，我抽样查看了几个，暂时未发现误判的情况；但当我使用aime25评测kimi-k2.5这个模型的时候，我又遇到了同样的问题，
我测出来的数据为56.67，但官方公布数据为96；
<img width="772" height="149" alt="Image" src="https://github.com/user-attachments/assets/8f4e1932-944c-4fc3-bdf7-d7f7cb13f7b0" />
并且我已经按照kimi-k2.5论文中所展示的参数配置，依旧无法复现/接近这个数值。
<img width="1796" height="272" alt="Image" src="https://github.com/user-attachments/assets/1dcee3ce-66e0-42ca-be83-099e3f10fe43" />

当我使用可视化工具查看的时候，我发现了一个问题，aime25中有一道计算七边形的题目：其正确结果是588；我在时候可视化查看的时候，发现这道题判定失败，
generated下方空白，初步怀疑max_tokens设置的问题，导致输出被截断。
<img width="1708" height="992" alt="Image" src="https://github.com/user-attachments/assets/3bb34f9f-1be1-4add-9c6b-5bbaeb465584" />
但是当我查看aime25_default.jsonl文件的时候，我发现这道题目实际上模型回答正确了。
完整的日志如下所示：
`{"index": 4, "model": "moonshotai/kimi-k2.5", "model_output": {"id": "e5ecd40d-d516-4290-b648-9761d3755be8", "model": "moonshotai/kimi-k2.5", "choices": [{"message": {"id": "a2ab21e8", "content": "**I need to find the area of heptagon AFNBCEM given information about points on triangle ABC.**\n\n## Setting Up Coordinates\n\nLet me place A at the origin with AB along the x-axis.\n- A = (0, 0)\n- D = (4, 0) (since AD = 4)\n- E = (20, 0) (since DE = 16, so AE = 20)\n- B = (28, 0) (since EB = 8, so AB = 28)\n\nLet C = (c_x, c_y) for some c_y > 0.\n\n## Finding Points on AC\n\nPoints F and G are on AC with AF = 13, FG = 52, GC = 26, so AG = 65 and AC = 91.\n\nThe ratio AF/AC = 13/91 = 1/7, and AG/AC = 65/91 = 5/7.\n\nSo F = (c_x/7, c_y/7) and G = (5c_x/7, 5c_y/7).\n\n## Finding M and N\n\n- M is reflection of D through F: F is midpoint of DM, so M = 2F - D = (2c_x/7 - 4, 2c_y/7)\n- N is reflection of G through E: E is midpoint of GN, so N = 2E - G = (40 - 5c_x/7, -5c_y/7)\n\n## Using the Area of Quadrilateral DEGF\n\nArea of DEGF = 288. The vertices in order are D, E, G, F.\n\nUsing the shoelace formula with D=(4,0), E=(20,0), G=(5c_x/7, 5c_y/7), F=(c_x/7, c_y/7):\n\nArea = ½|x_D(y_E - y_G) + x_E(y_G - y_F) + x_G(y_F - y_D) + x_F(y_D - y_E)|\n= ½|4(0 - 5c_y/7) + 20(5c_y/7 - c_y/7) + (5c_x/7)(c_y/7 - 0) + (c_x/7)(0 - 0)|\n= ½|-20c_y/7 + 20·4c_y/7 + 5c_xc_y/49|\n= ½|-20c_y/7 + 80c_y/7 + 5c_xc_y/49|\n= ½|60c_y/7 + 5c_xc_y/49|\n= ½|c_y/49 · (420 + 5c_x)|\n\nSince area is positive: ½ · (c_y/49)|420 + 5c_x| = 288\n\nSo c_y|420 + 5c_x| = 28224, meaning c_y|84 + c_x| = 5644.8... \n\nLet me recheck: 288 × 98 = 28224. And 28224/5 = 5644.8. \n\nActually: ½ · (c_y/49) · 5|84 + c_x| = 288, so 5c_y|84+c_x| = 28224.\n\nSo c_y|84 + c_x| = 28224/5 = 5644.8. This is messy. Let me recheck.\n\nActually: 60c_y/7 = 420c_y/49. So we have (420c_y + 5c_xc_y)/49 = (5c_y(84+c_x))/49.\n\nSo ½ · 5c_y(84+c_x)/49 = 288, giving 5c_y(84+c_x) = 28224, so c_y(84+c_x) = 5644.8.\n\nHmm, let me recheck: 28224/5 = 5644.8. But let me verify 28224 = 288 × 98? No, 288 × 98 = 28224. Yes.\n\nWait: 5c_y(84+c_x) = 28224. So c_y(84+c_x) = 5644.8 = 28224/5.\n\nLet me try: 28224 = 16 × 1764 = 16 × 4 × 441 = 64 × 441 = 64 × 21². And 5644.8 = 28224/5.\n\nActually, let me recheck my area calculation. D=(4,0), E=(20,0), G=(5c_x/7, 5c_y/7), F=(c_x/7, c_y/7).\n\nShoelace: 4·0 + 20·(5c_y/7) + (5c_x/7)·(c_y/7) + (c_x/7)·0 - [0·20 + 0·(5c_x/7) + (5c_y/7)·(c_x/7) + (c_y/7)·4]\n= 100c_y/7 + 5c_xc_y/49 - 5c_xc_y/49 - 4c_y/7\n= 96c_y/7\n\nSo area = ½ · |96c_y/7| = 48c_y/7 = 288.\n\nThus c_y = 288 × 7/48 = 6 × 7 = 42.\n\n## Finding c_x\n\nFrom c_y(84 + c_x) = 5644.8... wait I need to recheck. Actually with correct area: 48c_y/7 = 288, so c_y = 42.\n\nNow I need another condition. Actually I already used the area condition. Let me recheck if I need c_x.\n\nActually for the heptagon area, I need c_x. Let me recheck: I got area = 48c_y/7, which doesn't depend on c_x! \n\nSo c_y = 42, and c_x is free? That seems odd. Let me recheck the shoelace once more.\n\nGoing around D→E→G→F→D:\n- x: 4, 20, 5c_x/7, c_x/7\n- y: 0, 0, 5c_y/7, c_y/7\n\nSum1 = 4·0 + 20·(5c_y/7) + (5c_x/7)·(c_y/7) + (c_x/7)·0 = 100c_y/7 + 5c_xc_y/49\nSum2 = 0·20 + 0·(5c_x/7) + (5c_y/7)·(c_x/7) + (c_y/7)·4 = 5c_xc_y/49 + 4c_y/7\n\nSum1 - Sum2 = 100c_y/7 - 4c_y/7 = 96c_y/7. ✓\n\nSo c_y = 42, and c_x can be anything (as long as the geometry is valid). \n\n## Computing the Heptagon Area\n\nThe heptagon is AFNBCEM with vertices in order: A, F, N, B, C, E, M.\n\nPoints:\n- A = (0, 0)\n- F = (c_x/7, 6)  [since c_y/7 = 6]\n- N = (40 - 5c_x/7, -30)  [since -5c_y/7 = -30]\n- B = (28, 0)\n- C = (c_x, 42)\n- E = (20, 0)\n- M = (2c_x/7 - 4, 12)  [since 2c_y/7 = 12]\n\nShoelace formula. Let u = c_x/7, so c_x = 7u.\n\n- A = (0, 0)\n- F = (u, 6)\n- N = (40 - 5u, -30)\n- B = (28, 0)\n- C = (7u, 42)\n- E = (20, 0)\n- M = (2u - 4, 12)\n\nSum of x_i y_{i+1}:\n- A→F: 0·6 = 0\n- F→N: u·(-30) = -30u\n- N→B: (40-5u)·0 = 0\n- B→C: 28·42 = 1176\n- C→E: 7u·0 = 0\n- E→M: 20·12 = 240\n- M→A: (2u-4)·0 = 0\n\nSum1 = 1416 - 30u\n\nSum of y_i x_{i+1}:\n- A→F: 0·u = 0\n- F→N: 6·(40-5u) = 240 - 30u\n- N→B: (-30)·28 = -840\n- B→C: 0·7u = 0\n- C→E: 42·20 = 840\n- E→M: 0·(2u-4) = 0\n- M→A: 12·0 = 0\n\nSum2 = 240 - 30u - 840 + 840 = 240 - 30u\n\nArea = ½|Sum1 - Sum2| = ½|1416 - 30u - 240 + 30u| = ½|1176| = 588\n\nThe u terms cancel!\n\n\\boxed{588}", "source": "generate", "metadata": null, "internal": null, "role": "assistant", "tool_calls": null, "model": "moonshotai/kimi-k2.5"}, "stop_reason": "stop", "logprobs": null}], "usage": {"input_tokens": 189, "output_tokens": 2109, "total_tokens": 2298, "input_tokens_cache_write": null, "input_tokens_cache_read": 0, "reasoning_tokens": 0}, "time": null, "metadata": null, "error": null}, "messages": [{"id": "a2ab21e8", "content": "I need to find the area of heptagon AFNBCEM given information about points on triangle ABC.\n\n## Setting Up Coordinates\n\nLet me place A at the origin with AB along the x-axis.\n- A = (0, 0)\n- D = (4, 0) (since AD = 4)\n- E = (20, 0) (since DE = 16, so AE = 20)\n- B = (28, 0) (since EB = 8, so AB = 28)\n\nLet C = (c_x, c_y) for some c_y > 0.\n\n## Finding Points on AC\n\nPoints F and G are on AC with AF = 13, FG = 52, GC = 26, so AG = 65 and AC = 91.\n\nThe ratio AF/AC = 13/91 = 1/7, and AG/AC = 65/91 = 5/7.\n\nSo F = (c_x/7, c_y/7) and G = (5c_x/7, 5c_y/7).\n\n## Finding M and N\n\n- M is reflection of D through F: F is midpoint of DM, so M = 2F - D = (2c_x/7 - 4, 2c_y/7)\n- N is reflection of G through E: E is midpoint of GN, so N = 2E - G = (40 - 5c_x/7, -5c_y/7)\n\n## Using the Area of Quadrilateral DEGF\n\nArea of DEGF = 288. The vertices in order are D, E, G, F.\n\nUsing the shoelace formula with D=(4,0), E=(20,0), G=(5c_x/7, 5c_y/7), F=(c_x/7, c_y/7):\n\nArea = ½|x_D(y_E - y_G) + x_E(y_G - y_F) + x_G(y_F - y_D) + x_F(y_D - y_E)|\n= ½|4(0 - 5c_y/7) + 20(5c_y/7 - c_y/7) + (5c_x/7)(c_y/7 - 0) + (c_x/7)(0 - 0)|\n= ½|-20c_y/7 + 20·4c_y/7 + 5c_xc_y/49|\n= ½|-20c_y/7 + 80c_y/7 + 5c_xc_y/49|\n= ½|60c_y/7 + 5c_xc_y/49|\n= ½|c_y/49 · (420 + 5c_x)|\n\nSince area is positive: ½ · (c_y/49)|420 + 5c_x| = 288\n\nSo c_y|420 + 5c_x| = 28224, meaning c_y|84 + c_x| = 5644.8... \n\nLet me recheck: 288 × 98 = 28224. And 28224/5 = 5644.8. \n\nActually: ½ · (c_y/49) · 5|84 + c_x| = 288, so 5c_y|84+c_x| = 28224.\n\nSo c_y|84 + c_x| = 28224/5 = 5644.8. This is messy. Let me recheck.\n\nActually: 60c_y/7 = 420c_y/49. So we have (420c_y + 5c_xc_y)/49 = (5c_y(84+c_x))/49.\n\nSo ½ · 5c_y(84+c_x)/49 = 288, giving 5c_y(84+c_x) = 28224, so c_y(84+c_x) = 5644.8.\n\nHmm, let me recheck: 28224/5 = 5644.8. But let me verify 28224 = 288 × 98? No, 288 × 98 = 28224. Yes.\n\nWait: 5c_y(84+c_x) = 28224. So c_y(84+c_x) = 5644.8 = 28224/5.\n\nLet me try: 28224 = 16 × 1764 = 16 × 4 × 441 = 64 × 441 = 64 × 21². And 5644.8 = 28224/5.\n\nActually, let me recheck my area calculation. D=(4,0), E=(20,0), G=(5c_x/7, 5c_y/7), F=(c_x/7, c_y/7).\n\nShoelace: 4·0 + 20·(5c_y/7) + (5c_x/7)·(c_y/7) + (c_x/7)·0 - [0·20 + 0·(5c_x/7) + (5c_y/7)·(c_x/7) + (c_y/7)·4]\n= 100c_y/7 + 5c_xc_y/49 - 5c_xc_y/49 - 4c_y/7\n= 96c_y/7\n\nSo area = ½ · |96c_y/7| = 48c_y/7 = 288.\n\nThus c_y = 288 × 7/48 = 6 × 7 = 42.\n\n## Finding c_x\n\nFrom c_y(84 + c_x) = 5644.8... wait I need to recheck. Actually with correct area: 48c_y/7 = 288, so c_y = 42.\n\nNow I need another condition. Actually I already used the area condition. Let me recheck if I need c_x.\n\nActually for the heptagon area, I need c_x. Let me recheck: I got area = 48c_y/7, which doesn't depend on c_x! \n\nSo c_y = 42, and c_x is free? That seems odd. Let me recheck the shoelace once more.\n\nGoing around D→E→G→F→D:\n- x: 4, 20, 5c_x/7, c_x/7\n- y: 0, 0, 5c_y/7, c_y/7\n\nSum1 = 4·0 + 20·(5c_y/7) + (5c_x/7)·(c_y/7) + (c_x/7)·0 = 100c_y/7 + 5c_xc_y/49\nSum2 = 0·20 + 0·(5c_x/7) + (5c_y/7)·(c_x/7) + (c_y/7)·4 = 5c_xc_y/49 + 4c_y/7\n\nSum1 - Sum2 = 100c_y/7 - 4c_y/7 = 96c_y/7. ✓\n\nSo c_y = 42, and c_x can be anything (as long as the geometry is valid). \n\n## Computing the Heptagon Area\n\nThe heptagon is AFNBCEM with vertices in order: A, F, N, B, C, E, M.\n\nPoints:\n- A = (0, 0)\n- F = (c_x/7, 6)  [since c_y/7 = 6]\n- N = (40 - 5c_x/7, -30)  [since -5c_y/7 = -30]\n- B = (28, 0)\n- C = (c_x, 42)\n- E = (20, 0)\n- M = (2c_x/7 - 4, 12)  [since 2c_y/7 = 12]\n\nShoelace formula. Let u = c_x/7, so c_x = 7u.\n\n- A = (0, 0)\n- F = (u, 6)\n- N = (40 - 5u, -30)\n- B = (28, 0)\n- C = (7u, 42)\n- E = (20, 0)\n- M = (2u - 4, 12)\n\nSum of x_i y_{i+1}:\n- A→F: 0·6 = 0\n- F→N: u·(-30) = -30u\n- N→B: (40-5u)·0 = 0\n- B→C: 28·42 = 1176\n- C→E: 7u·0 = 0\n- E→M: 20·12 = 240\n- M→A: (2u-4)·0 = 0\n\nSum1 = 1416 - 30u\n\nSum of y_i x_{i+1}:\n- A→F: 0·u = 0\n- F→N: 6·(40-5u) = 240 - 30u\n- N→B: (-30)·28 = -840\n- B→C: 0·7u = 0\n- C→E: 42·20 = 840\n- E→M: 0·(2u-4) = 0\n- M→A: 12·0 = 0\n\nSum2 = 240 - 30u - 840 + 840 = 240 - 30u\n\nArea = ½|Sum1 - Sum2| = ½|1416 - 30u - 240 + 30u| = ½|1176| = 588\n\nThe u terms cancel!\n\n\\boxed{588}", "source": "generate", "metadata": null, "internal": null, "role": "assistant", "tool_calls": null, "model": "moonshotai/kimi-k2.5"}], "metadata": {}}`

### Yunnglin · 2026-04-21

使用aime25评测kimi-k2.5 设置了 repeat 参数吗，完整运行参数是什么

### twilighgt · 2026-04-21

@Yunnglin 设置了，完整命令：
evalscope eval \
    --model moonshotai/kimi-k2.5 \
    --api-url ############## \
    --api-key ##############3 \
    --repeats 4 \
    --datasets aime25 \
    --generation-config '{"temperature": 1.0, "top_p": 0.95, "max_tokens": 32768}'

此外我查看了具体代码：

<img width="718" height="200" alt="Image" src="https://github.com/user-attachments/assets/bda87ed5-eaa7-4918-abb5-ca9df109d3f1" />

<img width="502" height="357" alt="Image" src="https://github.com/user-attachments/assets/e8bc3fb4-36e3-40d9-9261-bdd037b5f704" />



Kimi在jsonl里的原始输出片段：...\\boxed{588}----实际代码并没有等效的正则提取？我不太确定

### Yunnglin · 2026-04-21

@twilighgt 你可以配置 --judge-strategy llm_recall 和 --judge-model-args ... 来使用judge model进行兜底，方便的话可以上传一下整个output/2026xxx目录，排查一下问题

### twilighgt · 2026-04-21

@Yunnglin 好的，我使用judge再继续尝试下，以下是整个日志文件：

[20260420_143108.zip](https://github.com/user-attachments/files/26924874/20260420_143108.zip)

是否可以正常打开

### Yunnglin · 2026-04-23

> [@Yunnglin](https://github.com/Yunnglin) 设置了，完整命令： evalscope eval --model moonshotai/kimi-k2.5 --api-url ############## --api-key #############[#3](https://github.com/modelscope/evalscope/pull/3) --repeats 4 --datasets aime25 --generation-config '{"temperature": 1.0, "top_p": 0.95, "max_tokens": 32768}'
> 
> 此外我查看了具体代码：
> 
> <img alt="Image" width="718" height="200" src="https://private-user-images.githubusercontent.com/93211030/581228427-bda87ed5-eaa7-4918-abb5-ca9df109d3f1.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY5MTkzODUsIm5iZiI6MTc3NjkxOTA4NSwicGF0aCI6Ii85MzIxMTAzMC81ODEyMjg0MjctYmRhODdlZDUtZWFhNy00OTE4LWFiYjUtY2E5ZGYxMDlkM2YxLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MjMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDIzVDA0MzgwNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTNhNjY2NmY1MzdmN2IzOGUxZWRlZDZiOTczNTE4OTRmM2MzMzRmNTMzZjljYjA4MzBjZjg4ZGZhMGYwNWRjNzUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.s28_31b-P8umDR_9ffP8OoRtP1O8lk-CCZmO4SN1JXg"> <img alt="Image" width="502" height="357" src="https://private-user-images.githubusercontent.com/93211030/581227560-e8bc3fb4-36e3-40d9-9261-bdd037b5f704.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY5MTkzODUsIm5iZiI6MTc3NjkxOTA4NSwicGF0aCI6Ii85MzIxMTAzMC81ODEyMjc1NjAtZThiYzNmYjQtMzZlMy00MGQ5LTkyNjEtYmRkMDM3YjVmNzA0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MjMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDIzVDA0MzgwNVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWI4ZTNiMGUxOGZmY2Y2OTBjNzU0NzYzOTAwOWU1YjZlMzNkOWNjMDNlZThiNWY0OTQ3OGZmYWU5NGM4Nzk4ZjkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.URHRaVseR5y9cJUpugXUdkabKH0sx5R8y7g4Qm7A2N8">
> Kimi在jsonl里的原始输出片段：...\boxed{588}----实际代码并没有等效的正则提取？我不太确定

看了下这个样本，是reasoning过长截断，导致正文为空，是符合预期的，可以查看prediction中的第6条

### twilighgt · 2026-04-23

@Yunnglin 好的，感谢。此外，我配置了 --judge-strategy llm_recall 和 --judge-model-args ... 来进行兜底，
<img width="1015" height="146" alt="Image" src="https://github.com/user-attachments/assets/86d8f4af-d46b-44a3-89c3-8bf5f8d08c08" />
官方（95.8），evalscope工具跑出来56.67，进行查看之后并未误判。最近kimi-k2.6也出来了，所以我也顺道评测了kimi-k2.6在aime26上的表现，发现仍有差距，官方声称：96.4；我这边测试：76.67，已对齐指标：
<img width="1146" height="310" alt="Image" src="https://github.com/user-attachments/assets/ff5c91b8-1283-443c-b26d-ee654dba9b67" />
<img width="1680" height="326" alt="Image" src="https://github.com/user-attachments/assets/24007523-5090-4cc2-ad67-0a010f9a63a4" />

所以我怀疑这种情况：模型的能力是否和供应商也有关？是否还能其他可能的因素

### Yunnglin · 2026-04-23

- “模型的能力是否和供应商也有关”，这个是确定的，不然也不会有这个工具 https://github.com/MoonshotAI/K2-Vendor-Verifier
- 看了下官方推荐配置是这样的，最大token是否能支持到262k：

<img width="1802" height="788" alt="Image" src="https://github.com/user-attachments/assets/04bdcfd0-77d2-40a9-9ad4-4c353ca6ed09" />

### twilighgt · 2026-04-27

@Yunnglin aime这个测试集不需要这么大的token支持，我设置了32k，其输出也没有被截断，我查看了每道题目的输出，我发现fail的题目确实是模型答错了，这个随机性实在太高了。此外我通过使用K2VV https://github.com/MoonshotAI/K2-Vendor-Verifier 这个工具摸底了一把供应商（测试集只公布了50%，我在此基础上进行测试），其表现还可以（准确率在95.26%，召回率在86%，计算出来tool_call_f1=91.1%，官方认为tool_call_f1为80%（K2 0905 Evaluation Results）上是合理的）
所以，我尝试自己写了一个简单的脚本进行测试，其测试结果如下：虽和官方还有一些差距，但计算差值缩小了。
<img width="588" height="262" alt="Image" src="https://github.com/user-attachments/assets/ac5a39dd-c3b5-4e91-9e33-b808dba1aa3e" />
其部分代码如下所示：
<img width="1283" height="822" alt="Image" src="https://github.com/user-attachments/assets/6104da7a-666c-43a4-a94c-62c448ecc2da" />
===================================================================================
还有第二个小问题，HlE这个测试集，为何可视化的时候，红框部分显示的都是一样，都是Same as Generated，无论这道题错误还是正确，为何不直接显示捕获到的结果呢？我查看其他测试集发现这部分是获取到的结果。
<img width="1251" height="553" alt="Image" src="https://github.com/user-attachments/assets/683770a9-4b73-4b91-88dd-f218da070a6e" />
下图为gpqa_diamond测试集：
<img width="1178" height="562" alt="Image" src="https://github.com/user-attachments/assets/6b427321-c51a-494a-bed0-42fcdde6d149" />


### Yunnglin · 2026-04-27

1. AIME 系列的数据样本较少，一个题目的正误就是3.3%的差距，一般需要repeat多次计算平均值
2. HLE需要用judge model来判断正误，没有内置的answer extract，这些题目的输出自由度很高，无法写规则来判断

### twilighgt · 2026-04-28

@Yunnglin 好的，非常感谢。我想问下此工具是否考虑过丢包的情况？我在使用kimi-k2.6跑aime2026这个数据集，我当前的完整命令：
<img width="941" height="207" alt="Image" src="https://github.com/user-attachments/assets/ec611d1e-9cdf-4b50-be39-d85a428a78b2" />
当我发现在数据传输过大的时候，会产生丢包的现象：比如说查看任务对应时间节点：
```
Apr 28, 2026 @ 01:45:41.767 请求进入
Apr 28, 2026 @ 02:02:08.252 任务完成状态码200（我的任务已经完成了）
```
但是：注意下图有一个“incomplete chunked read” ；
<img width="1280" height="295" alt="Image" src="https://github.com/user-attachments/assets/0e0da584-9f3b-42b3-aebd-75e783920388" />
<img width="1912" height="150" alt="Image" src="https://github.com/user-attachments/assets/17488ad0-8239-494b-8e6f-f7130bf1cfeb" />

65这一行，大概在120k-150k的tokens之间：
<img width="1682" height="256" alt="Image" src="https://github.com/user-attachments/assets/a4c94165-c2af-4691-b169-4a68e5ab9a2e" />
目前的重试机制，我查看是针对api请求失败的，像这种由于网络抖动+丢包，继而导致连接关闭，这种情况是否有规避方案？


### Yunnglin · 2026-04-29

请问是否开启了stream模式进行流式传输

### twilighgt · 2026-04-29

@Yunnglin 是的，开启了。为了避免在执行测试的时候由于长时间无响应导致的连接超时，比如说这样，不停的重试直到挂掉：`2026-04-27 23:10:39,255 - openai._base_client - INFO: Retrying request to /chat/completions in 0.950291 seconds240 [20:06<13:40:50, 209.58s/it] `

### Yunnglin · 2026-05-13

@twilighgt incomplete chunked read 这种情况建议配置 ignore_errors 参数跳过出错的样本，在streaming 模式下重试的话成本较高，相当于这条样本重新推理一遍

### Yunnglin · 2026-07-08

这类“无法复现官方 / paper 分数”的问题，通常需要先对齐评测口径、采样参数和运行环境。当前信息还不足以判断为 EvalScope 框架侧 bug，先关闭该 issue；如果后续能提供最小可复现证据，欢迎 reopen 继续跟进。

建议按下面顺序排查：

1. **上传完整 `outputs/<timestamp>/`**
   - 至少包含 `configs/`、`predictions/`、`reports/`；
   - 如涉及 judge / agent / terminal-bench，请一并提供 `reviews/`、`trials/`、`agent/trajectory.json`、verifier 日志。

2. **先定位差异来源**
   - 模型原始输出错误：优先检查模型服务、采样参数、prompt 或官方口径；
   - 模型输出正确但 `extracted_prediction` 错：可能是答案提取问题；
   - 提取正确但 score 错：可能是 metric / judge / aggregation 配置问题；
   - 大量 error / timeout：先排查运行环境，再比较分数。

3. **对齐官方评测口径**
   请确认 prompt、system prompt、chat template、temperature、top_p、top_k、max_tokens、repeats、pass@k / vote@k / mean aggregation、judge model、benchmark 版本和 subset 都与官方一致。

4. **小样本集需要多次重复**
   AIME 等小样本 benchmark 单题就会带来几个百分点波动，建议使用 `repeats` 多次采样，并明确聚合方式。

5. **Agent / terminal-bench 类任务先查环境**
   请确认 Docker、容器网络、GitHub/PyPI/apt 访问、`timeout_multiplier` 等配置正常。环境不稳定时，总分通常不具备可比性。

6. **如需继续定位**
   请提供“模型输出正确但 EvalScope 提取或评分错误”的具体样本编号和完整 outputs，我们会继续排查。

