source: https://github.com/vllm-project/guidellm/commit/58eb61a82ad6c359499edd7317a9dec8b783755e

File tree Expand file tree Collapse file tree


src/guidellm/benchmark/schemas

tests/unit/benchmark/schemas Expand file tree Collapse file tree Original file line number Diff line number Diff line change @@ -295,10 +295,12 @@ def _compile_metric_distributions(


`295`

`295`

status : [


`296`

`296`

( # type: ignore[misc]


`297`

`297`

metric [_TIMED_METRIC_END_TIME_INDEX ],


`298`


- float (metric [ value_index ] or 0.0 ),



`298`

+ float (val ),


`299`

`299`

)


`300`

`300`

for metric in metrics


`301`

`301`

if metric is not None



`302`

+ for val in [metric [value_index ]]



`303`

+ if val is not None


`302`

`304`

]


`303`

`305`

for status , metrics in metrics_by_status .items ()


`304`

`306`

}


@@ -313,10 +315,12 @@ def _compile_metric_distributions(


`313`

`315`

( # type: ignore[misc]


`314`

`316`

metric [_TIMED_METRIC_START_TIME_INDEX ],


`315`

`317`

metric [_TIMED_METRIC_END_TIME_INDEX ],


`316`


- float (metric [ value_index ] or 0.0 ),



`318`

+ float (val ),


`317`

`319`

)


`318`

`320`

for metric in metrics


`319`

`321`

if metric is not None



`322`

+ for val in [metric [value_index ]]



`323`

+ if val is not None


`320`

`324`

]


`321`

`325`

for status , metrics in metrics_by_status .items ()


`322`

`326`

}



Original file line number Diff line number Diff line change @@ -173,6 +173,36 @@ def test_tool_call_summary_compile_no_tool_calls(self):


`173`

`173`

assert summary .mixed_tokens .output is None


`174`

`174`



`175`

`175`




`176`

+ @pytest .mark .regression



`177`

+ def test_timed_metrics_exclude_missing_values_from_rates_and_concurrency ():



`178`

+ """



`179`

+ Missing optional values do not become zero-valued rate or concurrency events.



`180`

+



`181`

+ Mixed workloads can contain requests where a modality-specific metric does not



`182`

+ apply. Those requests must be excluded consistently from every distribution for



`183`

+ that metric, while real zero values remain valid observations.



`184`

+



`185`

+ ## WRITTEN BY AI ##



`186`

+ """



`187`

+ summary = GenerativeMetricsSummary .compile_timed_metrics (



`188`

+ successful = [



`189`

+ (1.0 , 2.0 , None , 8 ),



`190`

+ (2.0 , 3.0 , None , None ),



`191`

+ (5.0 , 6.0 , None , 8 ),



`192`

+ ],



`193`

+ incomplete = [],



`194`

+ errored = [],



`195`

+ )



`196`

+



`197`

+ assert summary is not None



`198`

+ assert summary .output is not None



`199`

+ assert summary .output_per_second is not None



`200`

+ assert summary .output_concurrency is not None



`201`

+ assert summary .output .successful .count == 2



`202`

+ assert summary .output_per_second .successful .median == pytest .approx (4.0 )



`203`

+ assert summary .output_concurrency .successful .count == 2



`204`

+



`205`

+


`176`

`206`

@pytest .mark .sanity


`177`

`207`

def test_round_trip_metrics_compile ():


`178`

`208`

"""



You can’t perform that action at this time.


## 0 commit comments