source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1device_1_1_l_u_i_d.html
lastmod: 

# Struct ov::device::LUID[#](https://docs.openvino.ai#struct-ov-device-luid)

-
struct LUID
[#](https://docs.openvino.ai#_CPPv4N2ov6device4LUIDE) Structure which defines format of

[LUID](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1device_1_1_l_u_i_d).Public Members

-
std::array<uint8_t,
[MAX_LUID_SIZE](https://docs.openvino.ai#_CPPv4N2ov6device4LUID13MAX_LUID_SIZEE)> luid[#](https://docs.openvino.ai#_CPPv4N2ov6device4LUID4luidE) Array with luid for a device.


Public Static Attributes

-
static const uint64_t MAX_LUID_SIZE = 8
[#](https://docs.openvino.ai#_CPPv4N2ov6device4LUID13MAX_LUID_SIZEE) Max size of luid array (64 bits)


-
std::array<uint8_t,