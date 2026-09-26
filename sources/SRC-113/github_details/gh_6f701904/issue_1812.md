# [Issue #1812] Submission checker results for SingleStream using 97-percentile results instead of 90-percentile results

source: https://github.com/mlcommons/inference/issues/1812
state: closed | updated: 2026-07-27T00:37:01Z
labels: Stale

## 正文

@pgmpablo157321 
One of our submission results for singlestream was having wrong result showing in the final table. It should be showing 90-perc latency, but actually showing 97-perc latency.
![image](https://github.com/user-attachments/assets/bcdc1d35-7cfb-46d1-a274-86b65fbcb95c)
![image](https://github.com/user-attachments/assets/350add63-3787-4067-b686-32f2c487cb4d)



## 评论 (2)

### arjunsuresh · 2024-07-26

@nvzhihanj Its an unexpected error. Is it happening for all the models? Also we have early stopping result right?

### github-actions[bot] · 2026-07-27

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
