# [Issue #1488] Is it possible to allow resubmission from previous round?

source: https://github.com/mlcommons/inference/issues/1488
state: closed | updated: 2026-05-12T00:39:40Z
labels: Stale

## 正文

Would be nice to allow submitters to reuse logs from previous round. Currently its not possible because loadgen hashes are not backward compatible. 

FYI: MLCommons Training allows to reuse logs. 

## 评论 (5)

### rakshithvasudev · 2023-08-25

The key is to make sure old loadgen seed is not optimized. So if this feature is added, the checker should ensure there is no perf improvement.

### arjunsuresh · 2023-09-03

There is a downside to this that the submitted inference results may not be the `latest` on a system. Can you please share the plus points of this ask?

Training runs are really time-consuming and they even allow to change the results after the submission. In inference, most scenarios run within 10 minutes. Also, for the 4.0 round, we can discuss reducing the `min_query_count` for the offline scenario which can further lower the run times for slower running models.

### rakshithvasudev · 2023-09-12

Agreed, you're correct.  The point of this resubmission is not to exactly have the latest scores; but to make a resubmission as is. Not higher or lower performance. This would serve some usecases:

- Allows to make a submission, in the event that the engineering resources such as systems or engineers are blocked with other work and they still want to make an official MLPerf submission. 
- Allows to resubmit to preview systems to closed (with code on the latest round, if they didn't submit it first time and without rerunning the benchmarks because of the above mentioned constraints, this way their previous preview results don't have to get invalidated) 
- Enables the comparison of systems in the newest round with both old and new systems. While one can compare with the previous round by referring to the earlier table, integrating this information into the latest round facilitates an easier comparison. This is particularly beneficial for users unfamiliar with the MLPerf results table, as they might overlook details from the prior round.
 
If not being latest is a concern, the system description helps to give an overview of the system. That could also explain system is having possibly an old software and hardware. I'd also suspect that most submitters in general wouldn't want to submit older results anyway if there are no constraints.  

This approach atleast offers a placement for an older system on the latest results table without redoing a lot of work in the event there is no new hardware or software. 

With training, results are only allowed to be resubmitted if there is a convergence HP borrowing event. There are no other cases where results are allowed to be updated, and it has to be for the same system (no new systems can be added after deadline). Training is also as stringent as Inference when it comes to changing the results, the only exception is HP borrowing is allowed. 

Although inference runs don't take as much time as training, submitting all the benchmarks can still be time consuming. Especially when there are challenges with system access, etc. Allowing users the option to resubmit provides flexibility and accounts for this potential time constraint.

### arjunsuresh · 2023-09-19

Thank you @rakshithvasudev for detailing all the points. 

I strongly support this point: "Allows to resubmit to preview systems to closed " and it makes sense to allow reuse of older seeds when preview submissions are submitted as available in the next round. In fact this was done in 3.1 round for dlrmv1. However this was done only to satisfy the preview submission criteria and did not make it to the 3.1 results table. We should discuss this in the WG meetings.

### github-actions[bot] · 2026-05-12

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
