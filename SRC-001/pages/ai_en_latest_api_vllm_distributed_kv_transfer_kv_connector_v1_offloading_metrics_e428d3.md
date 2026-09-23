source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics)

Classes:

-
–[OffloadPromMetrics](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadPromMetrics) -
–[OffloadingConnectorStats](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadingConnectorStats)Offloading connector stats use flat metric names as keys.


##

`OffloadPromMetrics`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadPromMetrics)

Bases: [KVConnectorPromMetrics](https://docs.vllm.ai/metrics/#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorPromMetrics)

Methods:

-
–[observe](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadPromMetrics.observe)Observe transfer statistics.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`


|
|

###

`observe(transfer_stats_data, engine_idx=0)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadPromMetrics.observe)

Observe transfer statistics.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`


##

`OffloadingConnectorStats`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadingConnectorStats)

Bases: [KVConnectorStats](https://docs.vllm.ai/metrics/#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats)

Offloading connector stats use flat metric names as keys.

The `data`

dict is structured using `_StatsKey`

/ `_MetricType`

::

```
{
_StatsKey.TYPES: {name: _MetricType.*, ...},
_StatsKey.DATA: {name: {labelvalues: value, ...}, ...},
}
```


This structure is self-describing: it survives IPC serialization without needing the full `OffloadingMetricMetadata`

objects on the receiving side.

Counter values are aggregated by summing per-label-tuple, gauge values use the latest snapshot per-label-tuple, and histogram values are lists of observed samples per-label-tuple. Unlabeled metrics use `()`

as their labelvalues tuple.

Methods:

-
–[increase_counter](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadingConnectorStats.increase_counter)Increase a counter on the stats payload.

-
–[observe_histogram](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadingConnectorStats.observe_histogram)Record a histogram observation on the stats payload.

-
–[reduce](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadingConnectorStats.reduce)Reduce the observations collected during a time interval to one or

-
–[set_gauge](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadingConnectorStats.set_gauge)Set a gauge snapshot on the stats payload.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`


|
|

###

`increase_counter(counter_name, counter_increase_value=1, labelvalues=())`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadingConnectorStats.increase_counter)

Increase a counter on the stats payload.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`


###

`observe_histogram(histogram_name, histogram_value, labelvalues=())`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadingConnectorStats.observe_histogram)

Record a histogram observation on the stats payload.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`


###

`reduce()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadingConnectorStats.reduce)

Reduce the observations collected during a time interval to one or more representative values (eg avg/median/sum of the series). This is meant to be called by the logger to produce a summary of the stats for the last time interval.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`


###

`set_gauge(gauge_name, gauge_value, labelvalues=())`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics.OffloadingConnectorStats.set_gauge)

Set a gauge snapshot on the stats payload.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`


##

`_ConnectorMetricName`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics._ConnectorMetricName)

Connector-side metrics emitted by scheduler-side offloading code.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`


##

`_MetricType`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics._MetricType)

##

`_StatsKey`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics._StatsKey)

Top-level keys in the serialized stats dict.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`


##

`_TransferMetricName`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics._TransferMetricName)

Flat metric names for GPU↔offload-medium transfer operations.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/offloading/metrics.py`


##

`_TransferType`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.offloading.metrics._TransferType)

Transfer direction labels for deprecated CPU offload metrics.