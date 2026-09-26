source: https://docs.nvidia.com/cupti/api/structCUpti__SubscriberParams.html

# 7.232. CUpti_SubscriberParams[#](https://docs.nvidia.com#cupti-subscriberparams)

-
struct CUpti_SubscriberParams
[#](https://docs.nvidia.com#_CPPv422CUpti_SubscriberParams) Params for cuptiSubscribe_v2.

Public Members

-
size_t structSize
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SubscriberParams10structSizeE) Size of the data structure.

CUPTI client should set the size of the structure. It will be used in CUPTI to check what fields are available in the structure. Used to preserve backward compatibility.


-
const char *subscriberName
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SubscriberParams14subscriberNameE) Name given to the subscriber.

The subscriber name need not include the “CUPTI” prefix, as the CUPTI library automatically adds it as “CUPTI for <subscriberName>”. Can be NULL. An internal copy is created. Size must not exceed CUPTI_SUBSCRIBER_NAME_MAX_LEN to avoid truncation.


-
char *oldSubscriberName
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SubscriberParams17oldSubscriberNameE) In case of multiple subscribers not allowed, and a CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED return code, the name of the incompatible tool or the existing CUPTI subscriber will be written to this location.

Size should be greater than or equal to CUPTI_OLD_SUBSCRIBER_NAME_MIN_LEN to avoid truncation. Can be NULL. If multiple subscribers are allowed, this will be the name of the first subscriber, but CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED will not be returned.


-
size_t oldSubscriberSize
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SubscriberParams17oldSubscriberSizeE) Size of oldSubscriberName.

Minimum size should be CUPTI_OLD_SUBSCRIBER_NAME_MIN_LEN to avoid truncation.


-
uint8_t allowMultipleSubscribers
[#](https://docs.nvidia.com#_CPPv4N22CUpti_SubscriberParams24allowMultipleSubscribersE) Request to allow multiple subscribers.

If 0, requesting to disallow multiple subscribers. If 1, requesting to allow multiple subscribers. Note that cuptiSubscribe_v2 will return CUPTI_ERROR_MULTIPLE_SUBSCRIBERS_NOT_SUPPORTED if the request cannot be fulfilled. Note that support is currently only for CUPTI shared library and not for CUPTI static library, but static library will be supported in future releases.


-
size_t structSize