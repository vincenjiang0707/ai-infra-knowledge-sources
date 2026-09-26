source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityDeviceAttribute.html

# 7.24. CUpti_ActivityDeviceAttribute[#](https://docs.nvidia.com#cupti-activitydeviceattribute)

-
struct CUpti_ActivityDeviceAttribute
[#](https://docs.nvidia.com#_CPPv429CUpti_ActivityDeviceAttribute) The activity record for a device attribute.

This activity record represents information about a GPU device: either a CUpti_DeviceAttribute or CUdevice_attribute value (CUPTI_ACTIVITY_KIND_DEVICE_ATTRIBUTE).

Public Members

-
[CUpti_ActivityKind](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityKind)kind[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityDeviceAttribute4kindE) The activity record kind, must be CUPTI_ACTIVITY_KIND_DEVICE_ATTRIBUTE.


-
[CUpti_ActivityFlag](https://docs.nvidia.com/group__CUPTI__ACTIVITY__API.html#_CPPv418CUpti_ActivityFlag)flags[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityDeviceAttribute5flagsE) The flags associated with the device.

See also


-
uint32_t deviceId
[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityDeviceAttribute8deviceIdE) The ID of the device that this attribute applies to.


-
union
[CUpti_ActivityDeviceAttribute](https://docs.nvidia.com#_CPPv429CUpti_ActivityDeviceAttribute)::[anonymous] attribute[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityDeviceAttribute9attributeE) The attribute, either a CUpti_DeviceAttribute or CUdevice_attribute.

Flag CUPTI_ACTIVITY_FLAG_DEVICE_ATTRIBUTE_CUDEVICE is used to indicate what kind of attribute this is. If CUPTI_ACTIVITY_FLAG_DEVICE_ATTRIBUTE_CUDEVICE is 1 then CUdevice_attribute field is value, otherwise CUpti_DeviceAttribute field is valid.


-
union
[CUpti_ActivityDeviceAttribute](https://docs.nvidia.com#_CPPv429CUpti_ActivityDeviceAttribute)::[anonymous] value[#](https://docs.nvidia.com#_CPPv4N29CUpti_ActivityDeviceAttribute5valueE) The value for the attribute.

See CUpti_DeviceAttribute and CUdevice_attribute for the type of the value for a given attribute.


-