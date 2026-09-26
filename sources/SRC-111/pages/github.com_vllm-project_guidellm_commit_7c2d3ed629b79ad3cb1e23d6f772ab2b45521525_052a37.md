source: https://github.com/vllm-project/guidellm/commit/7c2d3ed629b79ad3cb1e23d6f772ab2b45521525

|
`13` | `13` | GenerativeMetrics,
|
`14` | `14` | GenerativeMetricsSummary,
|
`15` | `15` | GenerativeToolCallMetricsSummary,
|
| `16` | `+` SchedulerMetrics, |
`16` | `17` | )
|
`17` | `18` | from guidellm.scheduler import (
|
`18` | `19` | AsyncConstantStrategy,
|
| `20` | `+` SchedulerState, |
`19` | `21` | SchedulingStrategy,
|
`20` | `22` | ThroughputStrategy,
|
`21` | `23` | )
|
`22` | `24` | from guidellm.schemas import (
|
| `25` | `+` GenerationRequest, |
| `26` | `+` GenerationResponse, |
`23` | `27` | GenerativeRequestStats,
|
`24` | `28` | RequestInfo,
|
`25` | `29` | RequestTimings,
|
@@ -279,6 +283,76 @@ def _make_accumulator(
|
`279` | `283` | return accumulator
|
`280` | `284` |
|
`281` | `285` |
|
| `286` | `+`@pytest.mark.regression |
| `287` | `+`def test_scheduler_metrics_exclude_requests_cancelled_before_dispatch(): |
| `288` | `+` """ |
| `289` | `+` Compiled scheduler counts exclude requests cancelled while still queued. |
| `290` | `+`
|
| `291` | `+` ## WRITTEN BY AI ## |
| `292` | `+` """ |
| `293` | `+` accumulator = _make_accumulator([], SCHEDULE_BASE_TIME, SCHEDULE_BASE_TIME + 1.0) |
| `294` | `+` cancelled_state = SchedulerState( |
| `295` | `+` start_time=SCHEDULE_BASE_TIME, |
| `296` | `+` end_time=SCHEDULE_BASE_TIME + 1.0, |
| `297` | `+` start_requests_time=SCHEDULE_BASE_TIME, |
| `298` | `+` end_processing_time=SCHEDULE_BASE_TIME + 1.0, |
| `299` | `+` created_requests=1, |
| `300` | `+` queued_requests=1, |
| `301` | `+` processed_requests=1, |
| `302` | `+` cancelled_requests=1, |
| `303` | `+` ) |
| `304` | `+` info = RequestInfo( |
| `305` | `+` request_id="cancelled-queued", |
| `306` | `+` status="cancelled", |
| `307` | `+` timings=RequestTimings( |
| `308` | `+` queued=SCHEDULE_BASE_TIME, |
| `309` | `+` dequeued=SCHEDULE_BASE_TIME + 0.5, |
| `310` | `+` resolve_end=SCHEDULE_BASE_TIME + 1.0, |
| `311` | `+` finalized=SCHEDULE_BASE_TIME + 1.0, |
| `312` | `+` ), |
| `313` | `+` ) |
| `314` | `+` |
| `315` | `+` accumulator.update_estimate( |
| `316` | `+` response=None, |
| `317` | `+` request=GenerationRequest(request_id=info.request_id), |
| `318` | `+` info=info, |
| `319` | `+` scheduler_state=cancelled_state, |
| `320` | `+` ) |
| `321` | `+` completed_request = GenerationRequest(request_id="completed") |
| `322` | `+` completed_info = RequestInfo( |
| `323` | `+` request_id=completed_request.request_id, |
| `324` | `+` status="completed", |
| `325` | `+` timings=RequestTimings( |
| `326` | `+` queued=SCHEDULE_BASE_TIME, |
| `327` | `+` dequeued=SCHEDULE_BASE_TIME + 0.1, |
| `328` | `+` resolve_start=SCHEDULE_BASE_TIME + 0.2, |
| `329` | `+` request_start=SCHEDULE_BASE_TIME + 0.2, |
| `330` | `+` request_end=SCHEDULE_BASE_TIME + 0.8, |
| `331` | `+` resolve_end=SCHEDULE_BASE_TIME + 0.9, |
| `332` | `+` finalized=SCHEDULE_BASE_TIME + 1.0, |
| `333` | `+` ), |
| `334` | `+` ) |
| `335` | `+` final_state = cancelled_state.model_copy( |
| `336` | `+` update={"successful_requests": 1, "cancelled_requests": 1} |
| `337` | `+` ) |
| `338` | `+` accumulator.update_estimate( |
| `339` | `+` response=GenerationResponse( |
| `340` | `+` request_id=completed_request.request_id, |
| `341` | `+` request_args=None, |
| `342` | `+` ), |
| `343` | `+` request=completed_request, |
| `344` | `+` info=completed_info, |
| `345` | `+` scheduler_state=final_state, |
| `346` | `+` ) |
| `347` | `+` |
| `348` | `+` metrics = SchedulerMetrics.compile(accumulator, final_state) |
| `349` | `+` |
| `350` | `+` assert metrics.requests_made.successful == 1 |
| `351` | `+` assert metrics.requests_made.errored == 0 |
| `352` | `+` assert metrics.requests_made.incomplete == 0 |
| `353` | `+` assert metrics.requests_made.total == 1 |
| `354` | `+` |
| `355` | `+` |
`282` | `356` | class TestScheduleRelativeMetrics:
|
`283` | `357` | """
|
`284` | `358` | Verify the schedule-relative distributions added alongside request_latency.
|
|
## 0 commit comments