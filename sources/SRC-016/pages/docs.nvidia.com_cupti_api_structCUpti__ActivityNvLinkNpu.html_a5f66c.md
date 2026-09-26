source: https://docs.nvidia.com/cupti/api/structCUpti__ActivityNvLinkNpu.html

7.104. CUpti_ActivityNvLinkNpu# struct CUpti_ActivityNvLinkNpu# NPU identifier for NVLink connections. This structure identifies an NPU by index and domain ID. Public Members uint32_t index# Index of the NPU. First index will always be zero. uint32_t domainId# Domain ID of NPU. On Linux, this can be queried using lspci.