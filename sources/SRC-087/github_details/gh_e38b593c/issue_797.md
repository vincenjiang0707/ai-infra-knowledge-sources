# [Issue #797] [Bug]: DFlash training performs worse on Qwen3.5 than on Qwen3

source: https://github.com/vllm-project/speculators/issues/797
state: open | updated: 2026-07-29T02:42:27Z
labels: bug

## 正文

### Your current environment

Please provide the following information about your environment if applicable:

- vLLM
- Speculators 0.6.0
- CUDA
- PyTorch 2.8.0
- Transformers 5.5.0
- Hardware
- Model


### 🐛 Describe the bug

Speculators version: 0.6.0.
When training DFlash with the same corpus, questions, and training scripts, Qwen3.5‑4B performs worse than Qwen3‑4B during the training phase. This can be clearly observed from the TensorBoard statistics.
Is this due to inherent differences between the models, or is it an issue with Speculators?
Below are the data plots for both models during training.

<img width="401" height="425" alt="Image" src="https://github.com/user-attachments/assets/9c781b3f-59ac-4238-b3ac-39f63d9f6d93" />
<img width="401" height="427" alt="Image" src="https://github.com/user-attachments/assets/b3b9e182-0059-46b8-9281-eb9052f5c5d8" />
<img width="398" height="430" alt="Image" src="https://github.com/user-attachments/assets/fa79ea46-e843-4931-9e72-8262f59fc8d6" />

train scripts:
python scripts/train.py --verifier-name-or-path /llm/model/Qwen3-4B-Instruct-2507 --data-path ./output/dflash_qwen3_4b_medium_10k --hidden-states-path ./output/dflash_qwen3_4b_medium_10k/hidden_states --save-path ./output/dflash_qwen3_4b_medium_10k/checkpoints --speculator-type dflash --block-size 8 --num-layers 5 --target-layer-ids 2 10 18 26 34 --epochs 30 --lr 5e-4 --total-seq-len 8192 --on-missing raise --seed 42 --draft-arch qwen3 --scheduler-type cosine --max-anchors 512 --prefetch-factor 2 --num-workers 8 --logger tensorboard --run-name dflash_qwen3_4b_medium_10k --log-freq 4
python scripts/train.py --verifier-name-or-path /llm/model/Qwen3.5-4B --data-path ./output/dflash_qwen3_5_4b_medium_10k --hidden-states-path ./output/dflash_qwen3_5_4b_medium_10k/hidden_states_new --save-path ./output/dflash_qwen3_5_4b_medium_10k_new_1/checkpoints --speculator-type dflash --block-size 8 --num-layers 5 --target-layer-ids 2 9 16 23 30 --epochs 30 --lr 5e-4 --total-seq-len 8192 --on-missing raise --seed 42 --draft-arch qwen3 --scheduler-type cosine --max-anchors 512 --prefetch-factor 2 --num-workers 8 --logger tensorboard --run-name dflash_qwen3_5_4b_medium_10k_new_1 --log-freq 4 

## 评论 (10)

### imargulis · 2026-07-16

Hello @chenfengt .
Could you please expand a bit on the context behind the expected behavior (I presume you'd expect similar learning dynamics) ?
After all, it's a different model (I mean draft model) the hidden dimension is different as well as intermediate, so I would not expect
to see the same dynamics, correct me if I'm wrong.

### chenfengt · 2026-07-17

> Hello [@chenfengt](https://github.com/chenfengt) . Could you please expand a bit on the context behind the expected behavior (I presume you'd expect similar learning dynamics) ? After all, it's a different model (I mean draft model) the hidden dimension is different as well as intermediate, so I would not expect to see the same dynamics, correct me if I'm wrong.

I was expecting similar learning behavior because I looked at the evaluation results of the z-lab Qwen3.5-4B-DFlash model. With block=8, it achieves an average acceptance length of over 3. However, when I train the draft model using the Speculators framework, I'm nowhere near that level.
One indication is that the first-token acceptance rate on the training set stays around 0.75, which already suggests that the draft model is not learning as expected.
Initially, I suspected that the issue might be related to my training corpus or training scripts. I'm using a Chinese medical QA dataset. However, when I use exactly the same corpus and training scripts to train Qwen3-4B, the results are significantly better—the acceptance rate increases steadily during training, and the overall learning trend looks much healthier.
That's why I'm wondering whether this behavior is simply due to architectural differences between Qwen3-4B and Qwen3.5-4B, or whether there might be some compatibility issue or limitation when training Qwen3.5-4B with the Speculators framework.

### Xuejinggg · 2026-07-17

Hello, could I ask what GPUs you used for training Qwen3.5? A800?
I’ve been trying to train Qwen3.5-27B on A800 with TP=2 and TP=4 respectively, but I keep running into CUDA out-of-memory errors，which is weird.  I’d appreciate it if you could share your training experience with me.

### chenfengt · 2026-07-17

> Hello, could I ask what GPUs you used for training Qwen3.5? A800? I’ve been trying to train Qwen3.5-27B on A800 with TP=2 and TP=4 respectively, but I keep running into CUDA out-of-memory errors，which is weird. I’d appreciate it if you could share your training experience with me.

I am training Qwen3.5‑4B. You can try reducing total-seq-len or max-anchors to see if that helps.

### Xuejinggg · 2026-07-17

> m training Qwen3.5‑4B. You can try reducing total-seq-len or max-anchors to see if that helps.

Thanks, but we encountered this issue at Step 2: Launch vLLM server in the background.

### chenfengt · 2026-07-17

> > m training Qwen3.5‑4B. You can try reducing total-seq-len or max-anchors to see if that helps.
> 
> Thanks, but we encountered this issue at Step 2: Launch vLLM server in the background.

Ah，I misunderstood your question.I just used the default launch_vllm.py script in examples. and I didn't hit any OOM at Step 2

### fynnsu · 2026-07-20

@chenfengt Could you try running using the latest version from the main branch of speculators. We've recently landed some things that we expect should help with Qwen 3.5 (https://github.com/vllm-project/speculators/pull/733).

Let me know if that helps!

### fynnsu · 2026-07-20

@Xuejinggg if you're hitting OOMs when launching vllm, you can try adjusting `--gpu-memory-utilization` or `--max-model-len`, those can sometimes be good knobs to tune. 

### chenfengt · 2026-07-22

> [@chenfengt](https://github.com/chenfengt) Could you try running using the latest version from the main branch of speculators. We've recently landed some things that we expect should help with Qwen 3.5 ([#733](https://github.com/vllm-project/speculators/pull/733)).
> 
> Let me know if that helps!

Thanks! I'll give a try in the next few days

### chenfengt · 2026-07-29

@fynnsu I tried the latest main branch, and the training results on Qwen 3.5 are definitely better now. Thanks!

<img width="405" height="431" alt="Image" src="https://github.com/user-attachments/assets/ef094a52-11e9-45d1-934d-3fa07164d85d" />
<img width="399" height="430" alt="Image" src="https://github.com/user-attachments/assets/848d5aa2-e765-458d-b830-30ab7495c9af" />
