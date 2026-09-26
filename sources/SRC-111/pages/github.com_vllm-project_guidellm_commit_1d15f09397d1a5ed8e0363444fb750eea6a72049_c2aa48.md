source: https://github.com/vllm-project/guidellm/commit/1d15f09397d1a5ed8e0363444fb750eea6a72049

|
`5` | `5` | from guidellm.benchmark.schemas.accumulator import (
|
`6` | `6` | GenerativeRequestsAccumulator,
|
`7` | `7` | )
|
`8` |
| `-`from guidellm.schemas import GenerativeRequestStats, RequestInfo, UsageMetrics |
| `8` | `+`from guidellm.schemas import ( |
| `9` | `+` GenerationRequest, |
| `10` | `+` GenerationResponse, |
| `11` | `+` GenerativeRequestStats, |
| `12` | `+` RequestInfo, |
| `13` | `+` UsageMetrics, |
| `14` | `+`) |
`9` | `15` |
|
`10` | `16` |
|
`11` | `17` | def _make_stats(
|
@@ -86,6 +92,62 @@ def test_clears_request_args(self):
|
`86` | `92` | assert stats.output == "answer"
|
`87` | `93` | assert stats.reasoning_output == "thinking..."
|
`88` | `94` |
|
| `95` | `+` |
| `96` | `+`class TestReservoirSampling: |
| `97` | `+` """Tests for bounded request-data retention during reservoir sampling.""" |
| `98` | `+` |
| `99` | `+` @pytest.mark.regression |
| `100` | `+` def test_clears_request_data_when_new_request_is_not_sampled(self, monkeypatch): |
| `101` | `+` """A rejected reservoir candidate must not retain heavyweight data. |
| `102` | `+`
|
| `103` | `+` ## WRITTEN BY AI ## |
| `104` | `+` """ |
| `105` | `+` accumulator = GenerativeRequestsAccumulator(sample_size=1) |
| `106` | `+` |
| `107` | `+` first_request = GenerationRequest(request_id="req-1") |
| `108` | `+` first_response = GenerationResponse( |
| `109` | `+` request_id="req-1", |
| `110` | `+` request_args="args-1", |
| `111` | `+` text="output-1", |
| `112` | `+` reasoning_text="reasoning-1", |
| `113` | `+` ) |
| `114` | `+` first_info = RequestInfo(request_id="req-1", status="completed") |
| `115` | `+` first_info.timings.request_start = 0.0 |
| `116` | `+` first_info.timings.request_end = 1.0 |
| `117` | `+` first_info.timings.resolve_end = 1.0 |
| `118` | `+` accumulator.update_estimate( |
| `119` | `+` first_response, |
| `120` | `+` first_request, |
| `121` | `+` first_info, |
| `122` | `+` prefer_response_metrics=True, |
| `123` | `+` ) |
| `124` | `+` |
| `125` | `+` monkeypatch.setattr("random.random", lambda: 1.0) |
| `126` | `+` second_request = GenerationRequest(request_id="req-2") |
| `127` | `+` second_response = GenerationResponse( |
| `128` | `+` request_id="req-2", |
| `129` | `+` request_args="args-2", |
| `130` | `+` text="output-2", |
| `131` | `+` reasoning_text="reasoning-2", |
| `132` | `+` ) |
| `133` | `+` second_info = RequestInfo(request_id="req-2", status="completed") |
| `134` | `+` second_info.timings.request_start = 1.0 |
| `135` | `+` second_info.timings.request_end = 2.0 |
| `136` | `+` second_info.timings.resolve_end = 2.0 |
| `137` | `+` accumulator.update_estimate( |
| `138` | `+` second_response, |
| `139` | `+` second_request, |
| `140` | `+` second_info, |
| `141` | `+` prefer_response_metrics=True, |
| `142` | `+` ) |
| `143` | `+` |
| `144` | `+` assert accumulator.samples == [0] |
| `145` | `+` assert accumulator.requests_stats[0].request_args == "args-1" |
| `146` | `+` assert accumulator.requests_stats[0].output == "output-1" |
| `147` | `+` assert accumulator.requests_stats[1].request_args is None |
| `148` | `+` assert accumulator.requests_stats[1].output is None |
| `149` | `+` assert accumulator.requests_stats[1].reasoning_output is None |
| `150` | `+` |
`89` | `151` | @pytest.mark.smoke
|
`90` | `152` | def test_clears_both(self):
|
`91` | `153` | """
|
|
## 0 commit comments