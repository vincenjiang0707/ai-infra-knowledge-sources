# [Issue #250] ValueError: `llm_cfg` `mm_projector_cfg` `vision_tower_cfg` not found in the config.

source: https://github.com/mit-han-lab/llm-awq/issues/250
state: open | updated: 2025-02-21T16:27:42Z
labels: 

## 正文

Dear author，I downloaded the files in https://huggingface.co/liuhaotian/llava-v1.5-7b/tree/main and ran the llava_example.sh to try to run the AWQ search. However, I encountered the problem of 

> ValueError: `llm_cfg` `mm_projector_cfg` `vision_tower_cfg` not found in the config.

The official LLaVA config indeeed doesn't have `llm_cfg` and `mm_projector_cfg`,how should I properly deal with it?I tried to use the files in https://huggingface.co/llava-hf/llava-1.5-7b-hf/tree/main ,but it doesn't have the necessary configs neither. Many thanks!

## 评论 (2)

### cyzhang39 · 2025-02-21

same issue, any solutions?

### Wotoosh · 2025-02-21

> same issue, any solutions?

I didn‘t solve it yet , since I encountered another problem in life, but I did find that it seems to match the architecture of vila like the one in  https://huggingface.co/Efficient-Large-Model/VILA1.5-13b/tree/main, hope it helps!
