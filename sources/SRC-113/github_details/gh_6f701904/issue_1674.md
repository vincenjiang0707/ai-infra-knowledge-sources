# [Issue #1674] 【GPT-J】checkpoint.zip download Incompletely

source: https://github.com/mlcommons/inference/issues/1674
state: closed | updated: 2026-05-05T00:38:32Z
labels: Stale

## 正文

i download checkpoint.zip :
wget https://cloud.mlcommons.org/index.php/s/QAZ2oM94MkFtbQx/download --output-document checkpoint.zip
but with error pytorch checkpoint file cannot load
when i unzip checkpoint.zip,i found it lacks pytorch_model-00002-of-00003.bin this file.
So i download pytorch_model.bin form Huggingface;
according pytorch_model.bin.index.json,i split pytorch_model.bin to get this file: pytorch_model-00002-of-00003.bin
but i run:
python3 main.py --scenario=Offline --model-path=./model/ --dataset-path=./data/cnn_eval.json --max_examples=16
it raise ValueError: Trying to set a tensor of shape torch.Size([50400, 4096]) in "weight" (which has shape torch.Size([50401, 4096])), this look incorrect.
can @mlcommons-bot help me?

## 评论 (2)

### nathanwasson · 2024-04-09

It sounds like you're using old download instructions.
Try the new download instructions [here](https://github.com/mlcommons/inference/tree/master/language/gpt-j#download-gpt-j-model). 

### github-actions[bot] · 2026-05-05

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
