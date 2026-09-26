source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityInstantaneousMetric.html

# 7.49. CUpti_ActivityInstantaneousMetric[#](https://docs.nvidia.com#cupti-activityinstantaneousmetric)

-
struct CUpti_ActivityInstantaneousMetric
[#](https://docs.nvidia.com#_CPPv433CUpti_ActivityInstantaneousMetric) The activity record for an instantaneous CUPTI metric.

This activity record represents the collection of a CUPTI metric value (CUPTI_ACTIVITY_KIND_METRIC) at a particular instance. This activity record kind is not produced by the activity API but is included for completeness and ease-of-use. Profiler frameworks built on top of CUPTI that collect metric data may choose to use this type to store the collected metric data.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityInstantaneousMetric4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_INSTANTANEOUS_METRIC.


-
CUpti_MetricID id
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityInstantaneousMetric2idE) The metric ID.


-
CUpti_MetricValue value
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityInstantaneousMetric5valueE) The metric value.


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityInstantaneousMetric9timestampE) The timestamp at which metric is sampled.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityInstantaneousMetric8deviceIdE) The device id.


-
uint8_t flags
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityInstantaneousMetric5flagsE) The properties of this metric.

See also


-
uint8_t pad[3]
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityInstantaneousMetric3padE) Undefined.

reserved for internal use


-