source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityAutoBoostState.html

# 7.5. CUpti_ActivityAutoBoostState[#](https://docs.nvidia.com#cupti-activityautobooststate)

-
struct CUpti_ActivityAutoBoostState
[#](https://docs.nvidia.com#_CPPv428CUpti_ActivityAutoBoostState) Device auto boost state structure.

This structure defines auto boost state for a device. See function

[cuptiGetAutoBoostState](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#group__cupti__activity__api_1ga1ac1cce5ce788b9f2c679d13e982384b)Public Members

-
uint32_t enabled
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityAutoBoostState7enabledE) Returned auto boost state.

1 is returned in case auto boost is enabled, 0 otherwise


-
uint32_t pid
[#](https://docs.nvidia.com#_CPPv4N28CUpti_ActivityAutoBoostState3pidE) Id of process that has set the current boost state.

The value will be CUPTI_AUTO_BOOST_INVALID_CLIENT_PID if the user does not have the permission to query process ids or there is an error in querying the process id.


-
uint32_t enabled