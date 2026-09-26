source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityConfidentialComputeRotation.html

# 7.10. CUpti_ActivityConfidentialComputeRotation[#](https://docs.nvidia.com#cupti-activityconfidentialcomputerotation)

-
struct CUpti_ActivityConfidentialComputeRotation
[#](https://docs.nvidia.com#_CPPv441CUpti_ActivityConfidentialComputeRotation) Event related to confidential compute encryption rotation.

This structure gives timestamps for stages of encryption rotation

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityConfidentialComputeRotation4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_CONFIDENTIAL_COMPUTE_ROTATION.


-
[CUpti_ConfidentialComputeRotationEventType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv442CUpti_ConfidentialComputeRotationEventType)eventType[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityConfidentialComputeRotation9eventTypeE) Type of event

[CUpti_ConfidentialComputeRotationEventType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga2453dc66ae13b07775b53dbd2481e142).

-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityConfidentialComputeRotation8deviceIdE) Device ID.


-
uint32_t contextId
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityConfidentialComputeRotation9contextIdE) Context ID.


-
uint32_t channelId
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityConfidentialComputeRotation9channelIdE) Channel ID.


-
[CUpti_ChannelType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv417CUpti_ChannelType)channelType[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityConfidentialComputeRotation11channelTypeE) Channel Type

[CUpti_ChannelType](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1gabc1dae9c4f50bae5a0068ec0e8dd2cdd).

-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N41CUpti_ActivityConfidentialComputeRotation9timestampE) Timestamp in ns.


-