source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/metrics/
lastmod: 2026-09-24

#

`vllm.distributed.ec_transfer.ec_connector.metrics`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics)

Classes:

-
–[ECConnectorLogging](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorLogging) -
–[ECConnectorProm](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorProm)Support for registering per-connector Prometheus metrics, and

-
–[ECConnectorPromMetrics](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorPromMetrics)A base class for per-connector Prometheus metric registration

-
–[ECConnectorStats](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorStats)Base class for EC Connector Stats, a container for transfer performance


##

`ECConnectorLogging`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorLogging)

Methods:

-
–[log](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorLogging.log)Log transfer metrics periodically, similar to throughput logging


## Source code in `vllm/distributed/ec_transfer/ec_connector/metrics.py`


###

`log(log_fn=logger.info)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorLogging.log)

Log transfer metrics periodically, similar to throughput logging

## Source code in `vllm/distributed/ec_transfer/ec_connector/metrics.py`


##

`ECConnectorProm`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorProm)

Support for registering per-connector Prometheus metrics, and recording transfer statistics to those metrics. Uses ECConnectorBase.build_prom_metrics().

## Source code in `vllm/distributed/ec_transfer/ec_connector/metrics.py`


##

`ECConnectorPromMetrics`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorPromMetrics)

A base class for per-connector Prometheus metric registration and recording.

Methods:

-
–[observe](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorPromMetrics.observe)Record the supplied transfer statistics to Prometheus metrics. These


## Source code in `vllm/distributed/ec_transfer/ec_connector/metrics.py`


###

`observe(transfer_stats_data, engine_idx=0)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorPromMetrics.observe)

Record the supplied transfer statistics to Prometheus metrics. These statistics are engine-specific, and should be recorded to a metric with the appropriate 'engine' label. These metric instances can be created using the create_metric_per_engine() helper method.

## Source code in `vllm/distributed/ec_transfer/ec_connector/metrics.py`


##

`ECConnectorStats`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorStats)

Base class for EC Connector Stats, a container for transfer performance metrics or otherwise important telemetry from the connector. All sub-classes need to be serializable as stats are sent from worker to logger process.

Methods:

-
–[aggregate](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorStats.aggregate)Aggregate stats with another

`ECConnectorStats`

object. -
–[is_empty](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorStats.is_empty)Return True if the stats are empty.

-
–[reduce](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorStats.reduce)Reduce the observations collected during a time interval to one or

-
–[reset](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorStats.reset)Reset the stats, clear the state.


## Source code in `vllm/distributed/ec_transfer/ec_connector/metrics.py`


###

`aggregate(other)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorStats.aggregate)

###

`is_empty()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorStats.is_empty)

###

`reduce()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.metrics.ECConnectorStats.reduce)

Reduce the observations collected during a time interval to one or more representative values (eg avg/median/sum of the series). This is meant to be called by the logger to produce a summary of the stats for the last time interval.