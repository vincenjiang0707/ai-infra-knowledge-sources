source: https://docs.nvidia.com/cupti/api/group__CUPTI__CLOCK__CONTROL__API.html

# 6.4. CUPTI Clock Control API[#](https://docs.nvidia.com#cupti-clock-control-api)

Functions and types to lock GPU clock frequencies for deterministic profiling.

## 6.4.1. Enumerations[#](https://docs.nvidia.com#enumerations)

[CUpti_ClockControl_Mode](https://docs.nvidia.com#group__cupti__clock__control__api_1ga630e8650f9afda4fdabf27642cc03309)Clock control modes.

[CUpti_ClockControl_Status](https://docs.nvidia.com#group__cupti__clock__control__api_1gabc9d58809e7cebb9f4cd3020440c9a55)Device clock-control status.


## 6.4.2. Functions[#](https://docs.nvidia.com#functions)

- CUptiResult
[cuptiClockControlGetStatus](https://docs.nvidia.com#group__cupti__clock__control__api_1gae044dd7c83a5f3ac8692bdfb60108a82)(CUcontext ctx, CUpti_ClockControl_Status *pStatus) Query the device-global GPU clock-control status.

- CUptiResult
[cuptiClockControlLock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga9d6db516fc0da9e3a1cb53cfbedefdb7)(CUcontext ctx, CUpti_ClockControl_Mode mode) Lock GPU clocks to the requested frequency.

- CUptiResult
[cuptiClockControlUnlock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga426501dd3513cab51a77a6d93e0fc42d)(void) Unlock GPU clocks previously locked via

[cuptiClockControlLock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga9d6db516fc0da9e3a1cb53cfbedefdb7).

## 6.4.3. Enumerations[#](https://docs.nvidia.com#id1)

-
enum CUpti_ClockControl_Mode
[#](https://docs.nvidia.com#_CPPv423CUpti_ClockControl_Mode) Clock control modes.

Determines the frequency to which GPU clocks are pinned for a profiling session. Locking clocks produces reproducible metric values across kernel launches and replay passes.

Clock locking is device-global — affects all contexts on the GPU. It is not supported on platforms where the underlying driver clock-control operation is unavailable, such as MIG-partitioned devices.

To skip clock locking entirely, simply do not call

[cuptiClockControlLock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga9d6db516fc0da9e3a1cb53cfbedefdb7). Numeric values start at 1 so that an uninitialized / zero-valued[CUpti_ClockControl_Mode](https://docs.nvidia.com#group__cupti__clock__control__api_1ga630e8650f9afda4fdabf27642cc03309)is rejected with[CUPTI_ERROR_INVALID_PARAMETER](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#group__cupti__result__api_1gga8c54bf95108e67d858f37fcf76c88714ad4dc6d34f22e4adc9b129df68b7bae63)rather than silently locking clocks.**Since**CUDA 13.4


*Values:*-
enumerator CUPTI_CLOCK_CONTROL_MODE_BASE
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ClockControl_Mode29CUPTI_CLOCK_CONTROL_MODE_BASEE) Lock GPU clocks to the base (rated TDP) frequency.

Exact clock domains that are pinned may depend on the driver and board configuration.


-
enumerator CUPTI_CLOCK_CONTROL_MODE_BOOST
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ClockControl_Mode30CUPTI_CLOCK_CONTROL_MODE_BOOSTE) Lock GPU clocks to the boost frequency.

Returns an error if boost locking is not supported by the driver or platform — no automatic fallback to base. Clients that want a fallback can retry with

[CUPTI_CLOCK_CONTROL_MODE_BASE](https://docs.nvidia.com#group__cupti__clock__control__api_1gga630e8650f9afda4fdabf27642cc03309a9486c938284bc9b4650c02177fc4816d)on error.

-
enumerator CUPTI_CLOCK_CONTROL_MODE_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N23CUpti_ClockControl_Mode34CUPTI_CLOCK_CONTROL_MODE_FORCE_INTE)


-
enum CUpti_ClockControl_Status
[#](https://docs.nvidia.com#_CPPv425CUpti_ClockControl_Status) Device clock-control status.

This status describes the device-global clock-control state reported by the driver for the GPU associated with a CUDA context. It does not describe CUPTI ownership. For example,

[CUPTI_CLOCK_CONTROL_STATUS_LOCKED](https://docs.nvidia.com#group__cupti__clock__control__api_1ggabc9d58809e7cebb9f4cd3020440c9a55a7e62f47e18d4d3f5ce97336cec0a7e7e)can be returned for a lock created by CUPTI, by another profiling tool, or by an administrator through an external mechanism such as nvidia-smi.Tools can query this state before calling

[cuptiClockControlLock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga9d6db516fc0da9e3a1cb53cfbedefdb7)to make an informed policy decision. A common use case is MIG: CUPTI cannot create a new clock lock on MIG-partitioned devices, but a tool may still choose to run if this API reports that clocks are already externally locked.A status of

[CUPTI_CLOCK_CONTROL_STATUS_UNLOCKED](https://docs.nvidia.com#group__cupti__clock__control__api_1ggabc9d58809e7cebb9f4cd3020440c9a55aba82e9d19bfec6a6762bb3a13de78bd4)only means the driver currently reports no explicit clock lock. It does not guarantee fixed, deterministic, or non-boosting clocks.**Since**CUDA 13.4


*Values:*-
enumerator CUPTI_CLOCK_CONTROL_STATUS_UNLOCKED
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ClockControl_Status35CUPTI_CLOCK_CONTROL_STATUS_UNLOCKEDE) The driver reports no explicit clock lock for this device.


-
enumerator CUPTI_CLOCK_CONTROL_STATUS_LOCKED
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ClockControl_Status33CUPTI_CLOCK_CONTROL_STATUS_LOCKEDE) The driver reports that clocks are locked to a fixed level.

This may be a CUPTI-owned lock or an externally-created lock.


-
enumerator CUPTI_CLOCK_CONTROL_STATUS_LOCKED_TO_FLOOR
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ClockControl_Status42CUPTI_CLOCK_CONTROL_STATUS_LOCKED_TO_FLOORE) The driver reports that clocks are locked to a floor/minimum level.


-
enumerator CUPTI_CLOCK_CONTROL_STATUS_BOOST_ENABLED
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ClockControl_Status40CUPTI_CLOCK_CONTROL_STATUS_BOOST_ENABLEDE) The driver reports that boost behavior is enabled by clock control.


-
enumerator CUPTI_CLOCK_CONTROL_STATUS_BOOST_DISABLED
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ClockControl_Status41CUPTI_CLOCK_CONTROL_STATUS_BOOST_DISABLEDE) The driver reports that boost behavior is disabled by clock control.


-
enumerator CUPTI_CLOCK_CONTROL_STATUS_FORCE_INT
[#](https://docs.nvidia.com#_CPPv4N25CUpti_ClockControl_Status36CUPTI_CLOCK_CONTROL_STATUS_FORCE_INTE)


## 6.4.4. Functions[#](https://docs.nvidia.com#id2)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiClockControlGetStatus( *CUcontext ctx*,,[CUpti_ClockControl_Status](https://docs.nvidia.com#_CPPv425CUpti_ClockControl_Status)*pStatusQuery the device-global GPU clock-control status.

Queries the driver for the current clock-control state of the GPU associated with

`ctx`

and stores the result in`pStatus`

. The returned status is device-global: it applies to the GPU, not just to`ctx`

, and it can reflect locks created outside CUPTI.This API does not create, take ownership of, release, or otherwise modify any clock lock. It only reports the current driver-visible state. In particular, receiving

[CUPTI_CLOCK_CONTROL_STATUS_LOCKED](https://docs.nvidia.com#group__cupti__clock__control__api_1ggabc9d58809e7cebb9f4cd3020440c9a55a7e62f47e18d4d3f5ce97336cec0a7e7e)does not imply that a later[cuptiClockControlUnlock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga426501dd3513cab51a77a6d93e0fc42d)call will release the lock; unlock only releases locks that were created by[cuptiClockControlLock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga9d6db516fc0da9e3a1cb53cfbedefdb7)in this process.If the query fails,

`pStatus`

is not modified. Failures can happen on platforms where clock-control state is unavailable or access is restricted.**Since**CUDA 13.4


- Parameters:
**ctx**– A valid CUDA context on the device whose clock status should be queried.**pStatus**– Returns the device clock-control status.

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– ctx is NULL or pStatus is NULL**CUPTI_ERROR_UNKNOWN**– An unspecified error occurred, preventing the query.



[#](https://docs.nvidia.com#_CPPv426cuptiClockControlGetStatus9CUcontextP25CUpti_ClockControl_Status)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiClockControlLock( *CUcontext ctx*,,[CUpti_ClockControl_Mode](https://docs.nvidia.com#_CPPv423CUpti_ClockControl_Mode)modeLock GPU clocks to the requested frequency.

Lock GPU clocks to a fixed level (base/rated-TDP or boost) so profiling sessions collect deterministic metrics. Clocks remain locked until

[cuptiClockControlUnlock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga426501dd3513cab51a77a6d93e0fc42d)is called. If the process exits beforehand, clocks are not automatically unlocked.Intended to be called BEFORE the profiling session is enabled (e.g., before

[cuptiRangeProfilerEnable](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#group__cupti__range__profiler__api_1ga7ea8fd4160643df21e66c2242d044010)), and matched with a call to[cuptiClockControlUnlock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga426501dd3513cab51a77a6d93e0fc42d)AFTER the session is disabled.Only one lock can be active at a time per process; calling this API again while a lock is active is a no-op that returns

[CUPTI_SUCCESS](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#group__cupti__result__api_1gga8c54bf95108e67d858f37fcf76c88714a60bd0257372573920d9bb2c802ce3b71). Before attempting a new lock, CUPTI queries the device status. If clocks are already locked before this API is called, CUPTI leaves the existing lock untouched and returns[CUPTI_SUCCESS](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#group__cupti__result__api_1gga8c54bf95108e67d858f37fcf76c88714a60bd0257372573920d9bb2c802ce3b71)without taking ownership of that lock. This external-lock check is performed before CUPTI rejects platforms where it cannot create a new lock, such as MIG-partitioned devices.To skip clock locking entirely, do not call this API — passing an uninitialized or zero-valued mode returns

[CUPTI_ERROR_INVALID_PARAMETER](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#group__cupti__result__api_1gga8c54bf95108e67d858f37fcf76c88714ad4dc6d34f22e4adc9b129df68b7bae63).**Since**CUDA 13.4


- Parameters:
**ctx**– A valid CUDA context on the device whose clocks should be locked.**mode**– Clock control mode (see[CUpti_ClockControl_Mode](https://docs.nvidia.com#group__cupti__clock__control__api_1ga630e8650f9afda4fdabf27642cc03309)).

- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_INVALID_PARAMETER**– ctx is NULL or mode is not a valid enum value**CUPTI_ERROR_NOT_SUPPORTED**– Device does not support clock control**CUPTI_ERROR_INSUFFICIENT_PRIVILEGES**– BOOST mode failed — typically requires elevated privileges**CUPTI_ERROR_UNKNOWN**– An unspecified error occurred, preventing the lock.



[#](https://docs.nvidia.com#_CPPv421cuptiClockControlLock9CUcontext23CUpti_ClockControl_Mode)

-
[CUptiResult](https://docs.nvidia.com/group__CUPTI__RESULT__API.html#_CPPv411CUptiResult)cuptiClockControlUnlock(*void*)[#](https://docs.nvidia.com#_CPPv423cuptiClockControlUnlockv) Unlock GPU clocks previously locked via

[cuptiClockControlLock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga9d6db516fc0da9e3a1cb53cfbedefdb7).Releases any clock lock created by CUPTI in this process. No-op if no lock is currently held. Safe to call even without a matching lock (e.g., as a defensive cleanup). This API does not release a pre-existing external lock that was observed by

[cuptiClockControlLock](https://docs.nvidia.com#group__cupti__clock__control__api_1ga9d6db516fc0da9e3a1cb53cfbedefdb7).Intended to be called AFTER the profiling session is disabled (e.g., after

[cuptiRangeProfilerDisable](https://docs.nvidia.com/group__CUPTI__RANGE__PROFILER__API.html#group__cupti__range__profiler__api_1ga062be4b9c43eec450718b2d01ceda582)).**Since**CUDA 13.4


- Return values:
**CUPTI_SUCCESS**–**CUPTI_ERROR_UNKNOWN**– An unspecified error occurred, preventing the unlock.