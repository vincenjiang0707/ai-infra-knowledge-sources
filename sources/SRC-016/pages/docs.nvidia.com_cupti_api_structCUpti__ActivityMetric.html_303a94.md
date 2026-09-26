source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMetric.html

# 7.95. CUpti_ActivityMetric[#](https://docs.nvidia.com#cupti-activitymetric)

-
struct CUpti_ActivityMetric
[#](https://docs.nvidia.com#_CPPv420CUpti_ActivityMetric) The activity record for a CUPTI metric.

This activity record represents the collection of a CUPTI metric value (CUPTI_ACTIVITY_KIND_METRIC). This activity record kind is not produced by the activity API but is included for completeness and ease-of-use. Profile frameworks built on top of CUPTI that collect metric data may choose to use this type to store the collected metric data.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMetric4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_METRIC.


-
CUpti_MetricID id
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMetric2idE) The metric ID.


-
CUpti_MetricValue value
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMetric5valueE) The metric value.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMetric13correlationIdE) The correlation ID of the metric.

Use of this ID is user-defined, but typically this ID value will equal the correlation ID of the kernel for which the metric was gathered.


-
uint8_t flags
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMetric5flagsE) The properties of this metric.

See also


-
uint8_t pad[3]
[#](https://docs.nvidia.com#_CPPv4N20CUpti_ActivityMetric3padE) Undefined.

Reserved for internal use.


-