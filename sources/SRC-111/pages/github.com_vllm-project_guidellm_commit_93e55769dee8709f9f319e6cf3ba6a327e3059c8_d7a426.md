source: https://github.com/vllm-project/guidellm/commit/93e55769dee8709f9f319e6cf3ba6a327e3059c8

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

Expose requeue delay from datasets (#871 Cont.) (#876)

## Summary
Continuation of PR #871.
## Details
- Add `requeue_delay_column` to the column mapper
- Add `synthetic_text` dataset support for requeue delay
- Add basic tests in `test_synthetic.py`
## Test Plan
- `tox`
## Related Issues
- Resolves#871
---
- [x] "I certify that all code in this PR is my own, except as noted below."
## Use of AI
- [ ] Includes code generated or substantially modified by an AI agent
- [ ] Includes tests generated or substantially modified by an AI agent
> NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`](https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md) file.
---
# git log
commit 254da7a
Author: Samuel Monson <smonson@redhat.com>
Date: Mon Jun 29 14:45:28 2026 -0400
Fix interface between data and scheduler
The scheduler has no concept of a GenerationRequest so move the request
settings out as a separate object in a tuple.
Signed-off-by: Samuel Monson <smonson@redhat.com>
commit e69d65e
Author: Samuel Monson <smonson@redhat.com>
Date: Mon Jun 29 15:48:32 2026 -0400
Move requeue delay to request settings
Signed-off-by: Samuel Monson <smonson@redhat.com>
commit a12e135
Author: Samuel Monson <smonson@redhat.com>
Date: Mon Jun 29 16:19:12 2026 -0400
Fixup Tests
Generated-by: claude-code Opus 4.6
Signed-off-by: Samuel Monson <smonson@redhat.com>
commit 8732459
Author: SkiHatDuckie <SkiHatDuckie@gmail.com>
Date: Wed Jul 1 14:56:34 2026 -0400
Add requeue_delay_column to column mapper
Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>
commit f600d71
Author: SkiHatDuckie <SkiHatDuckie@gmail.com>
Date: Wed Jul 1 15:26:06 2026 -0400
synthetic text dataset support for requeue delay
Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>
commit a24430b
Author: SkiHatDuckie <SkiHatDuckie@gmail.com>
Date: Wed Jul 1 16:25:51 2026 -0400
Add basic tests
Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>
commit 0a1a2a5
Author: Samuel Monson <smonson@redhat.com>
Date: Wed Jul 1 17:44:40 2026 -0400
Don't clear request_info after _process_next_request
Signed-off-by: Samuel Monson <smonson@redhat.com>
commit 97a6076
Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
Date: Thu Jul 2 15:18:32 2026 -0400
Rework random number generation logic
Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
commit 738257b
Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
Date: Thu Jul 2 15:20:55 2026 -0400
Rework random number generation logic x2
Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
commit 6a2dea3
Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
Date: Thu Jul 2 15:29:52 2026 -0400
fix: Call correct random generator
Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
commit 25048e9
Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
Date: Thu Jul 2 15:33:36 2026 -0400
Don't round in FloatRangeSampler
Co-authored-by: Samuel Monson <smonson@irbash.net>
Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
commit 8b68f67
Author: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
Date: Thu Jul 2 15:38:09 2026 -0400
Set minimum val of calc_min to 0.0 instead of 1
Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>
---------
Co-authored-by: Samuel Monson <smonson@irbash.net>
Generated-by: claude-code Opus 4.6
Signed-off-by: Samuel Monson <smonson@redhat.com>
Signed-off-by: SkiHatDuckie <SkiHatDuckie@gmail.com>
Signed-off-by: SkiHatDuckie <63932363+SkiHatDuckie@users.noreply.github.com>

## 0 commit comments