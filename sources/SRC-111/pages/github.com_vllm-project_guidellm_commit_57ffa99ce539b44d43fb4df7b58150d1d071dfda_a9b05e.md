source: https://github.com/vllm-project/guidellm/commit/57ffa99ce539b44d43fb4df7b58150d1d071dfda

You signed in with another tab or window. Reload to refresh your session.You signed out in another tab or window. Reload to refresh your session.You switched accounts on another tab or window. Reload to refresh your session.Dismiss alert

The interval columns were written beside each metric and then moved to the
end of the row by matching header names, so the code that wrote a column no
longer said where it went, and any later column with a matching name would
have been moved too. They are now written by one method called after every
other column, listing only the metrics that carry intervals.
Listing them explicitly also drops the columns that could never hold a
value. Every distribution used to get Mean CI and Percentile CIs, including
time per output token, inter-token latency and the rate metrics, which never
carry an interval. On a 107 request run that took the addition from 95
columns to 27, with the 238 existing columns and every populated interval
value unchanged.
The percentile intervals are now read with model_dump rather than getattr,
and a code comment points at the metrics guide's new location under docs/en.
Assisted-by: Claude Code claude-opus-5
Signed-off-by: QHarshil <harshil_c@hotmail.com>

Copy file name to clipboardExpand all lines: docs/en/guides/metrics.md

+1-1Lines changed: 1 addition & 1 deletion

Display the source diff

Display the rich diff

Original file line number

Diff line number

Diff line change

@@ -160,7 +160,7 @@ Each summary statistic above is an estimate made from a finite number of request

160

160

161

161

Set the level with `--metrics kind=generative,confidence=0.95`. It defaults to 0.95, and `null` reports the metrics without intervals. The level is recorded once per benchmark as `config.confidence`.

162

162

163

-

The console shows the mean and the half-width of its interval together, for example `80.5 ±3.9`, and marks a percentile the sample cannot bound with `*`. The CSV appends a `Mean CI` and a `Percentile CIs` column per metric, the latter keyed by percentile, plus the confidence level. Those columns go at the end of each row so that existing column positions are unchanged.

163

+

The console shows the mean and the half-width of its interval together, for example `80.5 ±3.9`, and marks a percentile the sample cannot bound with `*`. The CSV appends a `Mean CI` and a `Percentile CIs` column for each metric that carries intervals, the latter keyed by percentile, plus the confidence level. Those columns go at the end of each row so that existing column positions are unchanged.

## 0 commit comments