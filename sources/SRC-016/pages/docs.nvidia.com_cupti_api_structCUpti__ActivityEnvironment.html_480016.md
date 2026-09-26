source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityEnvironment.html

# 7.26. CUpti_ActivityEnvironment[#](https://docs.nvidia.com#cupti-activityenvironment)

-
struct CUpti_ActivityEnvironment
[#](https://docs.nvidia.com#_CPPv425CUpti_ActivityEnvironment) The activity record for CUPTI environmental data.

This activity record provides CUPTI environmental data, include power, clocks, and thermals. This information is sampled at various rates and returned in this activity record. The consumer of the record needs to check the environmentKind field to figure out what kind of environmental record this is.

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityEnvironment4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_ENVIRONMENT.


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityEnvironment8deviceIdE) The ID of the device.


-
uint64_t timestamp
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityEnvironment9timestampE) The timestamp when this sample was retrieved, in ns.

A value of 0 indicates that timestamp information could not be collected for the marker.


-
[CUpti_ActivityEnvironmentKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv429CUpti_ActivityEnvironmentKind)environmentKind[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityEnvironment15environmentKindE) The kind of data reported in this record.


-
[CUpti_ActivityEnvironmentSpeed](https://docs.nvidia.com/structCUpti__ActivityEnvironmentSpeed.html#_CPPv430CUpti_ActivityEnvironmentSpeed)speed[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityEnvironment5speedE) Data returned for CUPTI_ACTIVITY_ENVIRONMENT_SPEED environment kind.


-
[CUpti_ActivityEnvironmentTemperature](https://docs.nvidia.com/structCUpti__ActivityEnvironmentTemperature.html#_CPPv436CUpti_ActivityEnvironmentTemperature)temperature[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityEnvironment11temperatureE) Data returned for CUPTI_ACTIVITY_ENVIRONMENT_TEMPERATURE environment kind.


-
[CUpti_ActivityEnvironmentPower](https://docs.nvidia.com/structCUpti__ActivityEnvironmentPower.html#_CPPv430CUpti_ActivityEnvironmentPower)power[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityEnvironment5powerE) Data returned for CUPTI_ACTIVITY_ENVIRONMENT_POWER environment kind.

The power in milliwatts consumed by GPU and associated circuitry. The power in milliwatts that will trigger power management algorithm.


-
[CUpti_ActivityEnvironmentCooling](https://docs.nvidia.com/structCUpti__ActivityEnvironmentCooling.html#_CPPv432CUpti_ActivityEnvironmentCooling)cooling[#](https://docs.nvidia.com#_CPPv4N25CUpti_ActivityEnvironment7coolingE) Data returned for CUPTI_ACTIVITY_ENVIRONMENT_COOLING environment kind.


-