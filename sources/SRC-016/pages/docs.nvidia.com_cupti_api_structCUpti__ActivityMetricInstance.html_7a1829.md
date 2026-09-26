source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityMetricInstance.html

# 7.96. CUpti_ActivityMetricInstance[#](https://docs.nvidia.com#cupti-activitymetricinstance)

-
struct CUpti_ActivityMetricInstance
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityMetricInstance) The activity record for a CUPTI metric with instance information.

This activity record represents a CUPTI metric value for a specific metric domain instance (CUPTI_ACTIVITY_KIND_METRIC_INSTANCE). This activity record kind is not produced by the activity API but is included for completeness and ease-of-use. Profile frameworks built on top of CUPTI that collect metric data may choose to use this type to store the collected metric data. This activity record should be used when metric domain instance information needs to be associated with the metric.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMetricInstance4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_METRIC_INSTANCE.


-
CUpti_MetricID id
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMetricInstance2idE) The metric ID.


-
CUpti_MetricValue value
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMetricInstance5valueE) The metric value.


-
uint32_t instance
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMetricInstance8instanceE) The metric domain instance.


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMetricInstance13correlationIdE) The correlation ID of the metric.

Use of this ID is user-defined, but typically this ID value will equal the correlation ID of the kernel for which the metric was gathered.


-
uint8_t flags
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMetricInstance5flagsE) The properties of this metric.

See also


-
uint8_t pad[7]
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityMetricInstance3padE) Undefined.

Reserved for internal use.


-