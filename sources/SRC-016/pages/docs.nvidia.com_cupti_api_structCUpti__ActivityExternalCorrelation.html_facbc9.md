source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityExternalCorrelation.html

# 7.33. CUpti_ActivityExternalCorrelation[#](https://docs.nvidia.com#cupti-activityexternalcorrelation)

-
struct CUpti_ActivityExternalCorrelation
[#](https://docs.nvidia.com#_CPPv433CUpti_ActivityExternalCorrelation) The activity record for correlation with external records.

This activity record correlates native CUDA records (e.g. CUDA Driver API, kernels, memcpys, …) with records from external APIs such as OpenACC. (CUPTI_ACTIVITY_KIND_EXTERNAL_CORRELATION).

See also

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityExternalCorrelation4kindE) The kind of this activity.


-
[CUpti_ExternalCorrelationKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv429CUpti_ExternalCorrelationKind)externalKind[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityExternalCorrelation12externalKindE) The kind of external API this record correlated to.


-
uint64_t externalId
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityExternalCorrelation10externalIdE) The correlation ID of the associated non-CUDA API record.

The exact field in the associated external record depends on that record’s activity kind (

See also


-
uint32_t correlationId
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityExternalCorrelation13correlationIdE) The correlation ID of the associated CUDA driver or runtime API record.


-
uint32_t reserved
[#](https://docs.nvidia.com#_CPPv4N33CUpti_ActivityExternalCorrelation8reservedE) Undefined.

Reserved for internal use.


-