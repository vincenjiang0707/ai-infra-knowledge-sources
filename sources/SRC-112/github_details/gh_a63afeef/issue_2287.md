# [Issue #2287] 请问是否有长序列的比较维度？

source: https://github.com/SemiAnalysisAI/InferenceX/issues/2287
state: open | updated: 2026-08-01T14:20:57Z
labels: 

## 正文

得益于kvcache，现在的大模型多倾向于 long-kvcache + short-in + long-out，
请问是否有长序列的比较维度？（面向 coding / long thinking 等新需求）

For example, 1K/64K ..

目前的throughput指标被 long-in 污染较为严重，导致漂亮的统计指标与实际output体验有很大gap

## 评论 (12)

### dawenxi-007 · 2026-07-21

Yes, agreed. 

Moreover, it would be great if there is any document to give the updated details of each benchmark and explain the change list. For example, I noticed that the 1K/1K is deprecated but not sure why; Also, I am not sure what "Agentic Traces" benchmark means. 

If there is any discussion/forum that is helpful to understand better on these benchmark items, I would be interested in joining.

### ghostplant · 2026-07-21

I don't know why they turn to drop a lot of long-out evaluation, maybe it's bad for selling NVIDIA GPUs (since **NVIDIA GPUs are the most expensive choice in decoding**)?

It is sad that only the numbers look impressive, but customers become frustrated when actually deploying services.

### Oseltamivir · 2026-07-22

Hello @ghostplant @dawenxi-007  👋 

谢谢对 InferenceX 的关注

AMD、NVIDIA 等在内的所有提交方一致同意，我们已弃用1k/1k和1k/8k 单轮这类测试，转而采用更贴近实际应用场景的 “长上下文多轮对话 + KV Cache 命中率 + Agentic Coding（智能体编程” 基准测试方案，该方案即将发布。这似乎与建议的“长 KV-cache 前缀 + 非缓存前缀 + 输出”模式相契合。https://inferencex.semianalysis.com/datasets/cc-traces-weka-062126

由于 GPU 资源有限且排队时间较长，我们无法对所有场景进行基准测试；如果您愿意提供 GPU 算力支持，我们将非常乐意考虑增加更多测试场景。

我们的 Agentic Coding 基准测试是与 WEKA、vLLM 维护者、AMD、NVIDIA 以及多家 AI 实验室合作开发的。

欢迎与我们通话交流，可以随时留下邮箱地址。

### Oseltamivir · 2026-07-22

它包括很多真正的 Claude code converstaion，我们用了个 reverse proxy来收集的。打个比方：https://inferencex.semianalysis.com/datasets/cc-traces-weka-062126/conversations/5b6e131844fbcb4a57f8cf516831dc679004

会包容Compaction，sub-agent，kv cache 的影响。

<img width="1187" height="502" alt="Image" src="https://github.com/user-attachments/assets/13677ac9-767a-49ad-be88-d9fd31eb5c5f" />

<img width="1244" height="235" alt="Image" src="https://github.com/user-attachments/assets/7c13dd64-26e4-4356-89a9-0fa8ab8c247d" />

### Oseltamivir · 2026-07-22

@ghostplant 请问1k/64k有什么现实中的例子吗？

### ghostplant · 2026-07-22

1K/64K Example: Wring a single HTML file to implement the game of aircraft.

We have our own in-house Inference other than vLLM/Sglang/TRTLLM. Does InferenceX accept these 3 engines only?

### dawenxi-007 · 2026-07-22

> Hello [@ghostplant](https://github.com/ghostplant) [@dawenxi-007](https://github.com/dawenxi-007) 👋
> 
> 谢谢对 InferenceX 的关注
> 
> AMD、NVIDIA 等在内的所有提交方一致同意，我们已弃用1k/1k和1k/8k 单轮这类测试，转而采用更贴近实际应用场景的 “长上下文多轮对话 + KV Cache 命中率 + Agentic Coding（智能体编程” 基准测试方案，该方案即将发布。这似乎与建议的“长 KV-cache 前缀 + 非缓存前缀 + 输出”模式相契合。https://inferencex.semianalysis.com/datasets/cc-traces-weka-062126
> 
> 由于 GPU 资源有限且排队时间较长，我们无法对所有场景进行基准测试；如果您愿意提供 GPU 算力支持，我们将非常乐意考虑增加更多测试场景。
> 
> 我们的 Agentic Coding 基准测试是与 WEKA、vLLM 维护者、AMD、NVIDIA 以及多家 AI 实验室合作开发的。
> 
> 欢迎与我们通话交流，可以随时留下邮箱地址。

@Oseltamivir phicolzhang@gmail.com
可以交流一下吗？我们对InferenceX的benchmark比较感兴趣。

### ghostplant · 2026-07-23

> 它包括很多真正的 Claude code converstaion，我们用了个 reverse proxy来收集的。打个比方：https://inferencex.semianalysis.com/datasets/cc-traces-weka-062126/conversations/5b6e131844fbcb4a57f8cf516831dc679004
> 
> 会包容Compaction，sub-agent，kv cache 的影响。
> 
> <img alt="Image" width="1187" height="502" src="https://private-user-images.githubusercontent.com/58582368/624956654-13677ac9-767a-49ad-be88-d9fd31eb5c5f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODQ3ODU5OTksIm5iZiI6MTc4NDc4NTY5OSwicGF0aCI6Ii81ODU4MjM2OC82MjQ5NTY2NTQtMTM2NzdhYzktNzY3YS00OWFkLWJlODgtZDlmZDMxZWI1YzVmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA3MjMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNzIzVDA1NDgxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWYyYTI5YmMyODRiMzFiZTRhMmNlNjhmZTJiNjllMmNiZDcyNDMyNmYwMzQzNTA5ODZhYmY0M2EyM2I3NjhhYmMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.CDd3P-A4uNgRrtXfcwCqCT1mDJZkdLf0vmfHX76WbHA"> <img alt="Image" width="1244" height="235" src="https://private-user-images.githubusercontent.com/58582368/624956837-7c13dd64-26e4-4356-89a9-0fa8ab8c247d.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3ODQ3ODU5OTksIm5iZiI6MTc4NDc4NTY5OSwicGF0aCI6Ii81ODU4MjM2OC82MjQ5NTY4MzctN2MxM2RkNjQtMjZlNC00MzU2LTg5YTktMGZhOGFiOGMyNDdkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA3MjMlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNzIzVDA1NDgxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNjMjhkNGJiOTA0ZDU4ZmYyM2YwODAzNWQwOGQyMzFmM2QzZmJhOWU0NWNkYzA1OTU2M2YxNDY5YThjODc3YTYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.tN5W8xEoDqE1VZ2XeWvpVzxoh3QxrDM832mpyGYq70o">

Why is the output size so short? Is it a coding task, or have you disabled thinking effort?

### Oseltamivir · 2026-07-27

> We have our own in-house Inference other than vLLM/Sglang/TRTLLM. Does InferenceX accept these 3 engines only?

We can't host too many due to engineering time + cluster time, we picked the ones driving most of production tokens.

---

> [phicolzhang@gmail.com](mailto:phicolzhang@gmail.com) 可以交流一下吗？我们对InferenceX的benchmark比较感兴趣。

请问你和ghostplant属于MSRA吗？

---

> Why is the output size so short? Is it a coding task, or have you disabled thinking effort? 

Output per turn are low cause a "turn" here is a single model request in the agentic loop, not the whole task.

[OR reports](https://openrouter.ai/state-of-ai#rising-adoption-of-tool-calling) that the share of Anthropic-API requests ending in a tool call climbed from under 5% to over 15% at Nov 2025 and that agentic requests burn ~15× more tokens than human chat: a shift from single-turn completion toward multi-step, tool-integrated loops. These number are likely far higher today, with the shift from chatbots to agents.

Production coding agents doesn't reply with one long message. it runs hundreds of turns and the majority are tool-call steps: read a file, grep, run tests, make a small edit. Each of which emits only brief reasoning plus a compact tool payload (Edit sends just the changed lines, not whole files).

The same is now true of consumer chat, where models use tools (search, code, retrieval) constantly and only emit a long, from-scratch response when a user explicitly asks them to write something whole, is comparatively rare. A full paragraph of generated output per turn is an exception.

### dawenxi-007 · 2026-07-27

> > We have our own in-house Inference other than vLLM/Sglang/TRTLLM. Does InferenceX accept these 3 engines only?
> 
> We can't host too many due to engineering time + cluster time, we picked the ones driving most of production tokens.
> 
> > [phicolzhang@gmail.com](mailto:phicolzhang@gmail.com) 可以交流一下吗？我们对InferenceX的benchmark比较感兴趣。
> 
> 请问你和ghostplant属于MSRA吗？
> 
> > Why is the output size so short? Is it a coding task, or have you disabled thinking effort?
> 
> Output per turn are low cause a "turn" here is a single model request in the agentic loop, not the whole task.
> 
> [OR reports](https://openrouter.ai/state-of-ai#rising-adoption-of-tool-calling) that the share of Anthropic-API requests ending in a tool call climbed from under 5% to over 15% at Nov 2025 and that agentic requests burn ~15× more tokens than human chat: a shift from single-turn completion toward multi-step, tool-integrated loops. These number are likely far higher today, with the shift from chatbots to agents.
> 
> Production coding agents doesn't reply with one long message. it runs hundreds of turns and the majority are tool-call steps: read a file, grep, run tests, make a small edit. Each of which emits only brief reasoning plus a compact tool payload (Edit sends just the changed lines, not whole files).
> 
> The same is now true of consumer chat, where models use tools (search, code, retrieval) constantly and only emit a long, from-scratch response when a user explicitly asks them to write something whole, is comparatively rare. A full paragraph of generated output per turn is an exception.



> > We have our own in-house Inference other than vLLM/Sglang/TRTLLM. Does InferenceX accept these 3 engines only?
> 
> We can't host too many due to engineering time + cluster time, we picked the ones driving most of production tokens.
> 
> > [phicolzhang@gmail.com](mailto:phicolzhang@gmail.com) 可以交流一下吗？我们对InferenceX的benchmark比较感兴趣。
> 
> 请问你和ghostplant属于MSRA吗？

> 不是。我们lab有time-sharing的NVL72 access和一些其他服务器。可以做一些benchmark。



### dawenxi-007 · 2026-07-28

@ghostplant @Oseltamivir, 当前benchmark里面的Agentic Traces基准，有没有文档给出详细的定义？非常confusing。

### Oseltamivir · 2026-08-01

@dawenxi-007 
> 当前benchmark里面的Agentic Traces基准，有没有文档给出详细的定义？非常confusing。

我们现在还在调，e.g. #2415。但这个月内稳定后应该会写张 article 

