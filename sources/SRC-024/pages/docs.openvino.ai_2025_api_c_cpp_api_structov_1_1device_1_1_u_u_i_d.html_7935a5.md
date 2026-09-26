source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1device_1_1_u_u_i_d.html
lastmod: 

# Struct ov::device::UUID[#](https://docs.openvino.ai#struct-ov-device-uuid)

-
struct UUID
[#](https://docs.openvino.ai#_CPPv4N2ov6device4UUIDE) Structure which defines format of

[UUID](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1device_1_1_u_u_i_d).Public Members

-
std::array<uint8_t,
[MAX_UUID_SIZE](https://docs.openvino.ai#_CPPv4N2ov6device4UUID13MAX_UUID_SIZEE)> uuid[#](https://docs.openvino.ai#_CPPv4N2ov6device4UUID4uuidE) Array with uuid for a device.


Public Static Attributes

-
static const uint64_t MAX_UUID_SIZE = 16
[#](https://docs.openvino.ai#_CPPv4N2ov6device4UUID13MAX_UUID_SIZEE) Max size of uuid array (128 bits)


-
std::array<uint8_t,