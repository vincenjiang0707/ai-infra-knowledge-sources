source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityInstantaneousMetricInstance.html

# 7.50. CUpti_ActivityInstantaneousMetricInstance[#](https://docs.nvidia.com#cupti-activityinstantaneousmetricinstance)

-
struct CUpti_ActivityInstantaneousMetricInstance
[#](https://docs.nvidia.com#_CPPv441CUpti_ActivityInstantaneousMetricInstance) The instantaneous activity record for a CUPTI metric with instance information.

This activity record represents a CUPTI metric value for a specific metric domain instance (CUPTI_ACTIVITY_KIND_METRIC_INSTANCE) sampled at a particular time. This activity record kind is not produced by the activity API but is included for completeness and ease-of-use. Profiler frameworks built on top of CUPTI that collect metric data may choose to use this type to store the collected metric data. This activity record should be used when metric domain instance information needs to be associated with the metric.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityInstantaneousMetricInstance4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_INSTANTANEOUS_METRIC_INSTANCE.


-
CUpti_MetricID id
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityInstantaneousMetricInstance2idE) The metric ID.


-
CUpti_MetricValue value
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityInstantaneousMetricInstance5valueE) The metric value.


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityInstantaneousMetricInstance9timestampE) The timestamp at which metric is sampled.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityInstantaneousMetricInstance8deviceIdE) The device id.


-
uint8_t flags
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityInstantaneousMetricInstance5flagsE) The properties of this metric.

See also


-
uint8_t instance
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityInstantaneousMetricInstance8instanceE) The metric domain instance.


-
uint8_t pad[2]
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityInstantaneousMetricInstance3padE) Undefined.

reserved for internal use


-