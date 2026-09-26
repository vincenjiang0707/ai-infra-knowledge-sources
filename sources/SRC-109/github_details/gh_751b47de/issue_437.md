# [Issue #437] genai-perf returns only few fields in the table, not all

source: https://github.com/triton-inference-server/perf_analyzer/issues/437
state: closed | updated: 2025-08-18T10:32:19Z
labels: 

## 正文

I deployed in Kubernetes a pod for genai-perf using the below 

     containers:
      - name: genai-perf
        image: nvcr.io/nvidia/tritonserver:24.06-py3-sdk
        command: ["/bin/sh", "-c"]
        args:
          - |
            pip3 install sentencepiece && \
            sleep infinity

I then accessed the pod (kubectl exec -it) and executed the below command successfully and files created in /artifacts

genai-perf -m meta/llama3-8b-instruct --service-kind openai --url http://<nim-llm-service>:8000 --endpoint-type chat

The only issue is that I cannot see all the metrics in the table though: just latency, num output/input token:

                                                      LLM Metrics
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃            Statistic ┃           avg ┃           min ┃           max ┃           p99 ┃           p90 ┃           p75 ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ Request latency (ns) │ 4,110,623,430 │ 2,272,022,940 │ 5,252,536,691 │ 5,217,352,175 │ 4,900,691,530 │ 4,626,917,531 │
│     Num output token │           331 │           189 │           414 │           412 │           392 │           376 │
│      Num input token │           550 │           550 │           550 │           550 │           550 │           550 │
└──────────────────────┴───────────────┴───────────────┴───────────────┴───────────────┴─────
──────────┴───────────────┘

I would expect to get 
-Time to first token
-Inter token latency
and other mentioned in the description.



## 评论 (1)

### antonios-nokia · 2025-08-18

I used a newer image (25.01) and added --streaming in the command, it worked
