# [Issue #69] OSError

source: https://github.com/FasterDecoding/Medusa/issues/69
state: open | updated: 2024-01-25T02:24:06Z
labels: 

## 正文

python gen_model_answer_baseline.py  --model-path /data/transformers/vicuna-7b-v1.3 --model-id vicuna-7b-v1.3-0
python gen_model_answer_medusa.py  --model-path /data/transformers/medusa_vicuna-7b-v1.3 --model-id medusa-vicuna-7b-v1.3-0
My vicuna-7b-v1.3 download comes from:https://huggingface.co/FasterDecoding/medusa-vicuna-7b-v1.3/tree/main
My medusa-vicuna-7b-v1.3 download comes from:https://huggingface.co/FasterDecoding/medusa-vicuna-7b-v1.3/tree/main
I used this command to add the local model, and then an error was reported.how can I fixed it?
![微信截图_20240117161746](https://github.com/FasterDecoding/Medusa/assets/93046554/93da5efd-0378-4bfa-acab-f801a33adfdd)


## 评论 (3)

### ctlllll · 2024-01-24

Thanks for your interest! It seems to be a network issue and may be due to the GFW. Could you please check if that's the case?

### qspang · 2024-01-24

Thank you for your reply!I have fixed that problem.Can you take a look at the question I asked here?：https://github.com/FasterDecoding/Medusa/issues/45

### ctlllll · 2024-01-25

Sorry, I haven't tried llama-chat yet, but you may find our new training env https://github.com/ctlllll/axolotl helpful. You can refer to the configs and start training with commands like `accelerate launch -m axolotl.cli.train examples/medusa/your_config.yml`.
