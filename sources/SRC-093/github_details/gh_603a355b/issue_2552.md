# [Issue #2552] active_jobs has some stale job information which maybe done

source: https://github.com/vllm-project/aibrix/issues/2552
state: open | updated: 2026-08-23T07:28:48Z
labels: 

## 正文

### 🚀 Feature Description and Motivation

1. no job id or name..
2. lots of jobs are checked/refreshed within 1s. 

This is probably the reason job can not be scheduled. 


```
 2026-08-12 05:53:14,568 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  2026-08-12 05:53:14,569 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  2026-08-12 05:53:14,570 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  2026-08-12 05:53:14,571 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  2026-08-12 05:53:14,572 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  2026-08-12 05:53:14,573 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  2026-08-12 05:53:14,574 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  2026-08-12 05:53:14,575 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  2026-08-12 05:53:14,576 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  2026-08-12 05:53:14,577 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  2026-08-12 05:53:14,578 - batch_manager.py:593 - job_updated_handler - WARNING - {"old_category": "_in_progress_jobs", "new_category": "_done_jobs", "event": "Job is not in old category, ignore updating", "logger": "aibrix.batch.batch_manager", "level": "warning", "timestamp": "2026-08-12 05:53:14 UTC"}
  ^C
```

### Use Case

observability/job scheduling

### Proposed Solution

_No response_

## 评论 (1)

### Chenyiax · 2026-08-23

I looked into this and found a possible race in the refresh loop.
Refresh may capture an unfinished job while scanning pages. If the job finishes before the scan returns, refresh can put the old snapshot back into _monitored_job_snapshots. The Manager then rejects it because the job is already done, so the same update is retried every second.
I can reproduce the warning locally. The fix should be small, and I can submit a PR with a regression test.
