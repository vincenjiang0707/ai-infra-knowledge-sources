# [Issue #1433] TEST04 takes reciprocal of scores for SingleStream/MultiStream

source: https://github.com/mlcommons/inference/issues/1433
state: closed | updated: 2026-05-12T00:39:46Z
labels: Stale

## 正文

It is rather peculiar and confusing that for TEST04 ([only applicable to ResNet50](https://github.com/mlcommons/inference/issues/1350)), the comparisons for [SingleStream](https://github.com/mlcommons/inference/blob/master/compliance/nvidia/TEST04/verify_performance.py#L55) and [MultiStream](https://github.com/mlcommons/inference/blob/master/compliance/nvidia/TEST04/verify_performance.py#L61) are performed on score reciprocals (more precisely, `1e9 / float(score)`) rather than on scores directly like for TEST01 and TEST05 e.g.:

- SingleStream:
```
resnet50/singlestream/TEST04/verify_performance.txt:Verifying performance.
resnet50/singlestream/TEST04/verify_performance.txt-reference score = 1569.1221859754996
resnet50/singlestream/TEST04/verify_performance.txt-test score = 1571.568441019822
resnet50/singlestream/TEST04/verify_performance.txt-TEST PASS
--
resnet50/singlestream/TEST05/verify_performance.txt:Verifying performance.
resnet50/singlestream/TEST05/verify_performance.txt-reference score = 637299
resnet50/singlestream/TEST05/verify_performance.txt-test score = 638180
resnet50/singlestream/TEST05/verify_performance.txt-TEST PASS
--
resnet50/singlestream/TEST01/verify_performance.txt:Verifying performance.
resnet50/singlestream/TEST01/verify_performance.txt-reference score = 637299
resnet50/singlestream/TEST01/verify_performance.txt-test score = 638024
resnet50/singlestream/TEST01/verify_performance.txt-TEST PASS
```

- MultiStream:
```
resnet50/multistream/TEST04/verify_performance.txt:Verifying performance.
resnet50/multistream/TEST04/verify_performance.txt-reference score = 460.6963794332237
resnet50/multistream/TEST04/verify_performance.txt-test score = 469.96500640562306
resnet50/multistream/TEST04/verify_performance.txt-TEST PASS
--
resnet50/multistream/TEST05/verify_performance.txt:Verifying performance.
resnet50/multistream/TEST05/verify_performance.txt-reference score = 2170627
resnet50/multistream/TEST05/verify_performance.txt-test score = 2216725
resnet50/multistream/TEST05/verify_performance.txt-TEST PASS
--
resnet50/multistream/TEST01/verify_performance.txt:Verifying performance.
resnet50/multistream/TEST01/verify_performance.txt-reference score = 2170627
resnet50/multistream/TEST01/verify_performance.txt-test score = 2184797
resnet50/multistream/TEST01/verify_performance.txt-TEST PASS
```


## 评论 (1)

### github-actions[bot] · 2026-05-12

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
