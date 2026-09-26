# [Issue #751] Why the acceptance rate of eagle3 is so low?

source: https://github.com/vllm-project/speculators/issues/751
state: open | updated: 2026-07-10T11:38:52Z
labels: 

## 正文

eg: 
https://github.com/vllm-project/speculators/blob/main/examples/train/eagle3_qwen3_8b_sharegpt_online_5k.sh


On the trainning set data of 5k size.

<img width="1106" height="372" alt="Image" src="https://github.com/user-attachments/assets/4cfe309c-b842-4a69-8f1b-b80dcdce3f45" />

the acceptance rate of eagle3 is much lower than mtp and much lower than the paper stats. 

<img width="1660" height="1150" alt="Image" src="https://github.com/user-attachments/assets/2496ecfe-416d-4ada-af8d-584c5bdf8def" />

Is this reasonable?

## 评论 (2)

### fynnsu · 2026-07-09

Yes, https://github.com/vllm-project/speculators/blob/main/examples/train/eagle3_qwen3_8b_sharegpt_online_5k.sh and the other examples are intended as beginner friendly scripts to get users familiar with how to run the code. We also have tutorials that go alongside these scripts [here](https://docs.vllm.ai/projects/speculators/en/latest/user_guide/tutorials/). 

That's why they only use a small dataset, because they're just intended to show how to run all the steps. In reality to train a good speculator from scratch, we typically run with a lot more data (e.g. 500k samples for 2-3 epochs). There are also some other steps like [Response regeneration](https://docs.vllm.ai/projects/speculators/en/latest/user_guide/tutorials/response_regeneration/) that are often used to improve model performance further.

### xsank · 2026-07-10

@fynnsu thanks for your reply, we have found that when the data reaches tens of thousands, the acceptance rate will increase significantly. we will observe at what order of magnitude the acceptance rate begins to converge approximately.
