# [Issue #659] DFlash train do not support MM!!!

source: https://github.com/vllm-project/speculators/issues/659
state: closed | updated: 2026-07-13T07:29:14Z
labels: 

## 正文

My train dataset is MM data

{
   "images": [],
   "system": "",
   "conversations": []
}

val_metrics.json

{"loss_epoch": 0.055430415494879114, "full_acc_epoch": 0.8921938772083632, "position_1_acc_epoch": 0.9333426497179864, "position_2_acc_epoch": 0.9084640020613753, "position_3_acc_epoch": 0.8972993950354843, "position_4_acc_epoch": 0.8900179479239685, "position_5_acc_epoch": 0.8816816581237188, "position_6_acc_epoch": 0.8718744566500382, "position_7_acc_epoch": 0.8612913956776911}

infer draft model: accpet only 8%!


## 评论 (1)

### shanjiaz · 2026-06-25

@chizhanyuefeng Thanks for reaching out! Could you provide more details? Which model are you targeting and how much data is your model trained on? Which vLLM version did you test the model for? Would be happy to help! 
