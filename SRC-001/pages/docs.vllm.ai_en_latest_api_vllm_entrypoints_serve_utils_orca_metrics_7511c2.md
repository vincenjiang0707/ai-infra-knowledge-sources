source: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/serve/utils/orca_metrics/
lastmod: 2026-09-23

#

`vllm.entrypoints.serve.utils.orca_metrics`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics)

Utility functions that create ORCA endpoint load report response headers.

Functions:

-
–[create_orca_header](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics.create_orca_header)Creates ORCA headers named 'endpoint-load-metrics' in the specified format

-
–[get_named_metrics_from_prometheus](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics.get_named_metrics_from_prometheus)Collects current metrics from Prometheus and returns some of them

-
–[metrics_header](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics.metrics_header)Creates ORCA headers named 'endpoint-load-metrics' in the specified format.


##

`create_orca_header(metrics_format, named_metrics)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics.create_orca_header)

Creates ORCA headers named 'endpoint-load-metrics' in the specified format and adds custom metrics to named_metrics. ORCA headers format description: https://docs.google.com/document/d/1C1ybMmDKJIVlrbOLbywhu9iRYo4rilR-cT50OTtOFTs/edit?tab=t.0 ORCA proto https://github.com/cncf/xds/blob/main/xds/data/orca/v3/orca_load_report.proto

Parameters:

-

(`metrics_format`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics.create_orca_header(metrics_format))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The format of the header ('TEXT', 'JSON').

-

(`named_metrics`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics.create_orca_header(named_metrics))`List[Tuple[`

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str),[float](https://docs.python.org/3/builtins/functions.html#float)]]List of tuples with metric names and their corresponding double values.


Returns: - Optional[Mapping[str,str]]: A dictionary with header key as 'endpoint-load-metrics' and values as the ORCA header strings with format prefix and data in with named_metrics in.

## Source code in `vllm/entrypoints/serve/utils/orca_metrics.py`


##

`get_named_metrics_from_prometheus()`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics.get_named_metrics_from_prometheus)

Collects current metrics from Prometheus and returns some of them in the form of the `named_metrics`

list for `create_orca_header()`

.

#### Parameters[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics.get_named_metrics_from_prometheus--parameters)

- None

#### Returns[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics.get_named_metrics_from_prometheus--returns)

- list[tuple[str, float]]: List of tuples of metric names and their values.

## Source code in `vllm/entrypoints/serve/utils/orca_metrics.py`


##

`metrics_header(metrics_format)`

[¶](https://docs.vllm.ai#vllm.entrypoints.serve.utils.orca_metrics.metrics_header)

Creates ORCA headers named 'endpoint-load-metrics' in the specified format. Metrics are collected from Prometheus using `get_named_metrics_from_prometheus()`

.

ORCA headers format description: https://docs.google.com/document/d/1C1ybMmDKJIVlrbOLbywhu9iRYo4rilR-cT50OTtOFTs/edit?tab=t.0 ORCA proto https://github.com/cncf/xds/blob/main/xds/data/orca/v3/orca_load_report.proto

Parameters:

Returns: - Optional[Mapping[str,str]]: A dictionary with header key as 'endpoint-load-metrics' and values as the ORCA header strings with format prefix and data in with named_metrics in.