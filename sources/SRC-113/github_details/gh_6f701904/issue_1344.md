# [Issue #1344] DLRM Inference fails:KeyError

source: https://github.com/mlcommons/inference/issues/1344
state: closed | updated: 2026-05-15T00:42:51Z
labels: Stale

## 正文

Hi,
I am using the Terabyte dataset and the 12GB pre-trained model you published. I am running inference locally so I used `run_local.sh` script. I first ran the script to pre-process the dataset. It successfully pre-processed 21 days and then failed (I think due to memory limitations). Then I started pre-processing again and since the pre-processed files for the first 21st days were already there, the 3 remaining days were pre-processed. Finally I have all the 24 days pre-processed but now when I use them to run inference I get this error:
`File "$HOME/training/recommendation/dlrm/data_utils.py", line 147, in processCriteoAdData
    X_cat_t[j, k] = convertDicts[j][x]
KeyError: 1637495`
I am running in a conda virtual env with pytorch 1.10 and numpy 1.19 because it has been mentioned in other issues we'd better use those versions. The command I use for doing inference (initially used the same command for pre-processing) is this:
`./run_local.sh pytorch dlrm terabyte cpu --scenario Offline --max-ind-range=10000000 --data-sub-sample-rate=0.875 --samples-to-aggregate-quantile-file=./tools/dist_quantile.txt --max-batchsize=2048`

Can you please help with this issue?

Thanks!

## 评论 (2)

### nv-ananjappa · 2023-04-18

@pgmpablo157321 Could you help?

### github-actions[bot] · 2026-05-15

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
