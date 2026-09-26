# [Issue #412] How to use genai-perf with custom dataset and OpenAI compatible API?

source: https://github.com/triton-inference-server/perf_analyzer/issues/412
state: open | updated: 2025-08-28T12:56:07Z
labels: 

## 正文

Hi all,

I'm trying to run genai-perf with a custom dataset and OpenAI compatible API. I started the Triton container with:

```text
sudo docker run --rm -ti \
  -v /home/shareduser/maria-zamin:/mnt \
  -w /mnt \
  -v /home/shareduser/.cache/huggingface:/root/.cache/huggingface \
  --gpus all \
  -p 8000:8000 \
  -p 8001:8001 \
  -p 8002:8002 \
  nvcr.io/nvidia/tritonserver:25.06-trtllm-python-py3 \
  bash
```

Then, I prepared a TensorRT-LLM engine with Llama 3.2 3B Instruct, and inside the container, I used the following commands to serve the engine:

```text
cd /mnt/tensorrt-llm/server/python/openai/
pip install -r requirements.txt
 
python3 openai_frontend/main.py --model-repository /mnt/llama_ifb/ --tokenizer /mnt/models/Llama-3.2-3B-Instruct
```

If I do a curl, it's working:

<img width="727" height="448" alt="Image" src="https://github.com/user-attachments/assets/de19b409-1b79-4c03-a581-fcc794cf2fdd" />

Now I'm trying to use genai-perf with a custom JSON dataset, for example:

```text
genai-perf profile --model ensemble --tokenizer /mnt/models/Llama-3.2-3B-Instruct --endpoint-type chat --url localhost:9000 --input-file /mnt/tensorrt-llm/benchmarks/test_openai.jsonl --server-metrics-url http://15.15.83.236:9400/metrics --verbose
```

But it doesn't matter how I pass the json, it always gives me an error when parsing it. I tried all variations of this:

```json
{"model": "ensemble", "messages": [{"role": "user", "content": "Hello"}]}
```

Do you know if it's possible to use genai-perf with OpenAI compatible API for a custom dataset? If so, what should be the JSON format?

Additional note:

If I don't specify the input-file flag, I can run genai-perf. The `inputs.json` generated has the following schema. I tried using those inputs as the input file, but it didn't work as well.

```json
{
  "data": [
    {
      "payload": [
        {
          "model": "ensemble",
          "messages": [
            {
              "role": "user",
              "content": " be ingrate HORTENSIO Sir you say well and well you do conceive And since you do profess to be a suitor You must as we do gratify this gentleman To whom we all rest generally beholding TRANIO Sir I shall not be slack in sign whereof Please ye we may contrive this afternoon And quaff carouses to our mistress health And do as adversaries do in law Strive mightily but eat and drink as friends GRUMIO BIONDELLO O excellent motion Fellows lets be gone HORTENSIO The motions good indeed and be it so Petruchio I shall be your ben venuto Exeunt ACT II SCENE I Padua A room in Baptistas house Enter Katherina and Bianca BIANCA Good sister wrong me not nor wrong yourself To make a bondmaid and a slave of me That I disdain but for these other gawds Unbind my hands Ill pull them off myself Yea all my raiment to my petticoat Or what you will command me will I do So well I know my duty to my elders KATHERINA Of all thy suitors here I charge thee tell Whom thou lovst best see thou dissemble not BIANCA Believe me sister of all the men alive I never yet beheld that special face Which I could fancy more than any other KATHERINA Minion thou liest Ist not Hortensio BIANCA If you affect him sister here I swear Ill plead for you myself but you shall have him KATHERINA O then belike you fancy riches more You will have Gremio to keep you fair BIANCA Is it for him you do envy me so Nay then you jest and now I well perceive You have but jested with me all this while I prithee sister Kate untie my hands KATHERINA If that be jest then all the rest was so Strikes her Enter Baptista BAPTISTA Why how now dame Whence grows this insolence Bianca stand aside Poor girl she weeps Go ply thy needle meddle not with her For shame thou hilding of a devilish spirit Why dost thou wrong her that did neer wrong thee When did she cross thee with a bitter word KATHERINA Her silence flouts me and Ill be revengd Flies after Bianca BAPTISTA What in my sight Bianca get thee in Exit Bianca KATHERINA What will you not suffer me Nay now I see She is your treasure she must have a husband I must dance barefoot on her weddingday And for your love to her lead apes in hell Talk not to me I will go sit and weep Till I can find occasion of revenge Exit BAPTISTA Was ever gentleman thus griev"
            }
          ]
        }
      ]
    }
  ]
}
```

## 评论 (1)

### wellflat · 2025-08-28

`--input-file` is JSONL format file
```json
{"text":"your prompt here..."}
{"text":"your prompt here..."}
{"text":"your prompt here..."}
```
implementation: https://github.com/triton-inference-server/perf_analyzer/blob/bfcca04f599f363a767d4663e7d617a3d24fd93e/genai-perf/genai_perf/inputs/retrievers/file_input_retriever.py#L125
