source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/metrics/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.metrics`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics)

Classes:

-
–[KVConnectorLogging](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorLogging) -
–[KVConnectorProm](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorProm)Support for registering per-connector Prometheus metrics, and

-
–[KVConnectorPromMetrics](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorPromMetrics)A base class for per-connector Prometheus metric registration

-
–[KVConnectorStats](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats)Base class for KV Connector Stats, a container for transfer performance


##

`KVConnectorLogging`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorLogging)

Methods:

-
–[log](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorLogging.log)Log transfer metrics periodically, similar to throughput logging.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`


###

`log(log_fn=logger.info)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorLogging.log)

Log transfer metrics periodically, similar to throughput logging.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`


##

`KVConnectorProm`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorProm)

Support for registering per-connector Prometheus metrics, and recording transfer statistics to those metrics. Uses KVConnectorBase.build_prom_metrics().

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`


##

`KVConnectorPromMetrics`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorPromMetrics)

A base class for per-connector Prometheus metric registration and recording.

Methods:

-
–[observe](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorPromMetrics.observe)Record the supplied transfer statistics to Prometheus metrics. These


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`


###

`observe(transfer_stats_data, engine_idx=0)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorPromMetrics.observe)

Record the supplied transfer statistics to Prometheus metrics. These statistics are engine-specific, and should be recorded to a metric with the appropriate 'engine' label. These metric instances can be created using the create_metric_per_engine() helper method.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`


##

`KVConnectorStats`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats)

Base class for KV Connector Stats, a container for transfer performance metrics or otherwise important telemetry from the connector. All sub-classes need to be serializable as stats are sent from worker to logger process.

Methods:

-
–[aggregate](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.aggregate)Aggregate stats with another

`KVConnectorStats`

object. -
–[is_empty](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.is_empty)Return True if the stats are empty.

-
–[reduce](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.reduce)Reduce the observations collected during a time interval to one or

-
–[reset](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.reset)Reset the stats, clear the state.

-
–[to_dict](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.to_dict)Return the serializable connector stats payload.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/metrics.py`


###

`aggregate(other)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.aggregate)

###

`is_empty()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.is_empty)

###

`reduce()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats.reduce)

Reduce the observations collected during a time interval to one or more representative values (eg avg/median/sum of the series). This is meant to be called by the logger to produce a summary of the stats for the last time interval.