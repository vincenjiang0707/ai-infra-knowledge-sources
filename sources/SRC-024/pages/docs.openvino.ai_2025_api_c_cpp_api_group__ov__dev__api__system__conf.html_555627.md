source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__dev__api__system__conf.html
lastmod: 

# Group System configuration utilities[#](https://docs.openvino.ai#group-system-configuration-utilities)

-
*group*System configuration utilities API to get information about the system, core processor capabilities.

Functions

-
bool check_open_mp_env_vars(bool include_omp_num_threads = true)
[#](https://docs.openvino.ai#_CPPv422check_open_mp_env_varsb) Checks whether OpenMP environment variables are defined.

- Parameters:
**include_omp_num_threads**–**[in]**Indicates if the omp number threads is included- Returns:
`True`

if any OpenMP environment variable is defined,`false`

otherwise


-
std::vector<int> get_available_numa_nodes()
[#](https://docs.openvino.ai#_CPPv424get_available_numa_nodesv) Returns available CPU NUMA nodes (on Linux, and Windows [only with TBB], single node is assumed on all other OSes)

- Returns:
NUMA nodes



-
std::vector<int> get_available_cores_types()
[#](https://docs.openvino.ai#_CPPv425get_available_cores_typesv) Returns available CPU cores types (on Linux, and Windows) and ONLY with TBB, single core type is assumed otherwise.

- Returns:
Vector of core types



-
int get_number_of_cpu_cores(bool big_cores_only = false)
[#](https://docs.openvino.ai#_CPPv423get_number_of_cpu_coresb) Returns number of CPU physical cores on Linux/Windows (which is considered to be more performance friendly for servers) (on other OSes it simply relies on the original parallel API of choice, which usually uses the logical cores). call function with ‘false’ to get #phys cores of all types call function with ‘true’ to get #phys ‘Big’ cores number of ‘Little’ = ‘all’ - ‘Big’.

- Parameters:
**big_cores_only**–**[in]**Additionally limits the number of reported cores to the ‘Big’ cores only.- Returns:
Number of physical CPU cores.



-
int get_number_of_logical_cpu_cores(bool big_cores_only = false)
[#](https://docs.openvino.ai#_CPPv431get_number_of_logical_cpu_coresb) Returns number of CPU logical cores on Linux/Windows (on other OSes it simply relies on the original parallel API of choice, which uses the ‘all’ logical cores). call function with ‘false’ to get #logical cores of all types call function with ‘true’ to get #logical ‘Big’ cores number of ‘Little’ = ‘all’ - ‘Big’.

- Parameters:
**big_cores_only**–**[in]**Additionally limits the number of reported cores to the ‘Big’ cores only.- Returns:
Number of logical CPU cores.



-
int get_number_of_blocked_cores()
[#](https://docs.openvino.ai#_CPPv427get_number_of_blocked_coresv) Returns number of blocked CPU cores. Please note that this is a temporary interface for performance optimization on a specific platform. May be removed in future release.

- Returns:
Number of blocked CPU cores.



-
bool with_cpu_x86_sse42()
[#](https://docs.openvino.ai#_CPPv418with_cpu_x86_sse42v) Checks whether CPU supports SSE 4.2 capability.

- Returns:
`True`

is SSE 4.2 instructions are available,`false`

otherwise


-
bool with_cpu_neon_fp16()
[#](https://docs.openvino.ai#_CPPv418with_cpu_neon_fp16v) Checks whether CPU supports ARM NEON FP16 capability.

- Returns:
`True`

is ARM NEON FP16 instructions are available,`false`

otherwise


-
bool with_cpu_arm_dotprod()
[#](https://docs.openvino.ai#_CPPv420with_cpu_arm_dotprodv) Checks whether CPU supports ARM Dot Product capability.

- Returns:
`True`

is ARM Dot Product instructions are available,`false`

otherwise


-
bool with_cpu_arm_i8mm()
[#](https://docs.openvino.ai#_CPPv417with_cpu_arm_i8mmv) Checks whether CPU supports ARM Int8 MM capability.

- Returns:
`True`

is ARM Int8 MM instructions are available,`false`

otherwise


-
bool with_cpu_sve()
[#](https://docs.openvino.ai#_CPPv412with_cpu_svev) Checks whether CPU supports ARM SVE capability.

- Returns:
`True`

if ARM SVE instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx()
[#](https://docs.openvino.ai#_CPPv416with_cpu_x86_avxv) Checks whether CPU supports AVX capability.

- Returns:
`True`

is AVX instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx2()
[#](https://docs.openvino.ai#_CPPv417with_cpu_x86_avx2v) Checks whether CPU supports AVX2 capability.

- Returns:
`True`

is AVX2 instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx2_vnni()
[#](https://docs.openvino.ai#_CPPv422with_cpu_x86_avx2_vnniv) Checks whether CPU supports AVX2_VNNI capability.

- Returns:
`True`

is AVX2_VNNI instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx512f()
[#](https://docs.openvino.ai#_CPPv420with_cpu_x86_avx512fv) Checks whether CPU supports AVX 512 capability.

- Returns:
`True`

is AVX512F (foundation) instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx512_core()
[#](https://docs.openvino.ai#_CPPv424with_cpu_x86_avx512_corev) Checks whether CPU supports AVX 512 capability.

- Returns:
`True`

is AVX512F, AVX512BW, AVX512DQ instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx512_core_vnni()
[#](https://docs.openvino.ai#_CPPv429with_cpu_x86_avx512_core_vnniv) Checks whether CPU supports AVX 512 VNNI capability.

- Returns:
`True`

is AVX512F, AVX512BW, AVX512DQ, AVX512_VNNI instructions are available,`false`

otherwise


-
bool with_cpu_x86_bfloat16()
[#](https://docs.openvino.ai#_CPPv421with_cpu_x86_bfloat16v) Checks whether CPU supports BFloat16 capability.

- Returns:
`True`

is tAVX512_BF16 instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx512_core_fp16()
[#](https://docs.openvino.ai#_CPPv429with_cpu_x86_avx512_core_fp16v) Checks whether CPU supports fp16 capability.

- Returns:
`True`

is tAVX512_FP16 instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx512_core_amx_int8()
[#](https://docs.openvino.ai#_CPPv433with_cpu_x86_avx512_core_amx_int8v) Checks whether CPU supports AMX int8 capability.

- Returns:
`True`

is tAMX_INT8 instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx512_core_amx_bf16()
[#](https://docs.openvino.ai#_CPPv433with_cpu_x86_avx512_core_amx_bf16v) Checks whether CPU supports AMX bf16 capability.

- Returns:
`True`

is tAMX_BF16 instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx512_core_amx_fp16()
[#](https://docs.openvino.ai#_CPPv433with_cpu_x86_avx512_core_amx_fp16v) Checks whether CPU supports AMX fp16 capability.

- Returns:
`True`

is tAMX_FP16 instructions are available,`false`

otherwise


-
bool with_cpu_x86_avx512_core_amx()
[#](https://docs.openvino.ai#_CPPv428with_cpu_x86_avx512_core_amxv) Checks whether CPU supports AMX capability.

- Returns:
`True`

is tAMX_INT8 or tAMX_BF16 instructions are available,`false`

otherwise


-
int get_num_numa_nodes()
[#](https://docs.openvino.ai#_CPPv418get_num_numa_nodesv) Get number of numa nodes.

- Returns:
Number of numa nodes



-
int get_num_sockets()
[#](https://docs.openvino.ai#_CPPv415get_num_socketsv) Get number of sockets.

- Returns:
Number of sockets



-
int get_numa_node_id(int cpu_id)
[#](https://docs.openvino.ai#_CPPv416get_numa_node_idi) Get numa node id of cpu_id.

- Returns:
Numa node id



-
std::vector<std::vector<int>> get_proc_type_table()
[#](https://docs.openvino.ai#_CPPv419get_proc_type_tablev) Returns a table of number of processor types on Linux/Windows.

Processor table of one socket CPU desktop ALL_PROC | MAIN_CORE_PROC | EFFICIENT_CORE_PROC | HYPER_THREADING_PROC 32 8 16 8 // Total number of one socket


- Returns:
A table about number of CPU cores of different types defined with ColumnOfProcessorTypeTable The following are two example of processor type table.

Processor table of two socket CPUs XEON server ALL_PROC | MAIN_CORE_PROC | EFFICIENT_CORE_PROC | HYPER_THREADING_PROC 96 48 0 48 // Total number of two sockets 48 24 0 24 // Number of socket one 48 24 0 24 // Number of socket two




-
int get_current_socket_id()
[#](https://docs.openvino.ai#_CPPv421get_current_socket_idv) Returns the socket ID in cpu mapping table of the currently running thread.

- Returns:
socket ID in cpu mapping



-
int get_current_numa_node_id()
[#](https://docs.openvino.ai#_CPPv424get_current_numa_node_idv) Returns the numa node ID in cpu mapping table of the currently running thread.

- Returns:
numa node ID in cpu mapping



-
std::vector<std::vector<int>> get_org_proc_type_table()
[#](https://docs.openvino.ai#_CPPv423get_org_proc_type_tablev) Returns a table of original number of processor types without filtering other plugins occupying CPU resources. The difference from get_proc_type_table: This is used to get the configuration of current machine. For example, GPU plugin occupies all Pcores, there is only one type core in proc_type_table from

[get_proc_type_table()](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__dev__api__system__conf_1gaa8b2c3e270b1c057d23a96782b1a8004). If user wants to get the real configuration of this machine which should be got from get_org_proc_type_table.- Returns:
A table about number of CPU cores of different types defined with ColumnOfProcessorTypeTable



-
void reserve_available_cpus(const std::vector<std::vector<int>> streams_info_table, std::vector<std::vector<int>> &stream_processors, const int cpu_status = NOT_USED)
[#](https://docs.openvino.ai#_CPPv422reserve_available_cpusKNSt6vectorINSt6vectorIiEEEERNSt6vectorINSt6vectorIiEEEEKi) Get and reserve available cpu ids.

- Parameters:
**streams_info_table**–**[in]**streams information table.**stream_processors**–**[in]**processors grouped in stream which is used in core binding in cpu streams executor**cpu_status**–**[in]**set cpu status



-
void set_cpu_used(const std::vector<int> &cpu_ids, const int used)
[#](https://docs.openvino.ai#_CPPv412set_cpu_usedRKNSt6vectorIiEEKi) Set CPU_MAP_USED_FLAG of cpu_mapping.

- Parameters:
**cpu_ids**–**[in]**cpus in cpu_mapping.**used**–**[in]**update CPU_MAP_USED_FLAG of cpu_mapping with this flag bit



-
int get_org_socket_id(int socket_id)
[#](https://docs.openvino.ai#_CPPv417get_org_socket_idi) Get original socket id by current socket id, the input socket id is recalculated after filtering (like numactl), while the original socket id is the original id before filtering.

- Parameters:
**socket_id**–**[in]**socket id- Returns:
socket id



-
int get_org_numa_id(int numa_node_id)
[#](https://docs.openvino.ai#_CPPv415get_org_numa_idi) Get original numa node id by current numa node id, the input numa node id is recalculated after filtering (like numactl), while the original numa node id is the original id before filtering.

- Parameters:
**numa_node_id**–**[in]**numa node id- Returns:
numa node id



-
bool check_open_mp_env_vars(bool include_omp_num_threads = true)