source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__dev__profiling.html
lastmod: 

# Group ITT profiling utilities[#](https://docs.openvino.ai#group-itt-profiling-utilities)

-
*group*ITT profiling utilities Configurable macro wrappers for ITT profiling.

Defines

-
OV_ITT_DOMAIN(...)
[#](https://docs.openvino.ai#c.OV_ITT_DOMAIN) Declare domain with a given name.

- Parameters:
**domainName**– [in] Known at compile time name of module or library (the domain name).**domainDisplayName**– [in] Domain name used as the ITT counter name and displayed in Intel VTune. Parameter is optional.



-
OV_ITT_SCOPE(group, ...)
[#](https://docs.openvino.ai#c.OV_ITT_SCOPE) Annotate section of code till scope exit to be profiled using known

`handle`

or`taskName`

as section id.In case if handle or taskName absent, the current function name is used.

Note

Implements a task scope

- Parameters:
**group**– [in] ITT counter group name used for enabling/disabling at compile time.**domainName**– [in] Known at compile time name of module or library (the domain name).**handleOrTaskName**– [in] The annotation name or handle for section of code. Parameter is optional.



-
OV_ITT_SCOPED_TASK(...)
[#](https://docs.openvino.ai#c.OV_ITT_SCOPED_TASK) Annotate section of code till scope exit to be profiled using known

`handle`

or`taskName`

as section id.In case if handle or taskName absent, the current function name is used.

Note

Implements a task scope

- Parameters:
**domainName**– [in] Known at compile time name of module or library (the domain name).**handleOrTaskName**– [in] The annotation name or handle for section of code. Parameter is optional.



-
OV_ITT_SCOPED_TASK_BASE(...)
[#](https://docs.openvino.ai#c.OV_ITT_SCOPED_TASK_BASE) Annotate section of code till scope exit for BASE/FULL modes regardless of profiling filter groups.

In case if handle or taskName absent, the current function name is used.

- Parameters:
**domain**– [in] Known at compile time name of module or library (the domain name).**handleOrTaskName**– [in] The annotation name or handle for section of code. Parameter is optional.



-
OV_ITT_SCOPED_REGION_BASE(...)
[#](https://docs.openvino.ai#c.OV_ITT_SCOPED_REGION_BASE) Annotate region of code till scope exit for BASE/FULL modes regardless of profiling filter groups.

In case if handle or regionName absent, the current function name is used.

Note

Implements a region scope (single-active per thread; tasks started within the region attach as children).

- Parameters:
**domain**– [in] Known at compile time name of module or library (the domain name).**handleOrRegionName**– [in] The annotation name or handle for section of code. Parameter is optional.



-
OV_ITT_SCOPED_REGION(group, ...)
[#](https://docs.openvino.ai#c.OV_ITT_SCOPED_REGION) Annotate region of code till scope exit to be profiled using known

`handle`

or`regionName`

as section id.In case if handle or regionName absent, the current function name is used.

- Parameters:
**group**– [in] ITT counter group name used for enabling/disabling at compile time.**domainName**– [in] Known at compile time name of module or library (the domain name).**handleOrRegionName**– [in] The annotation name or handle for section of code. Parameter is optional.



-
OV_ITT_TASK_CHAIN(...)
[#](https://docs.openvino.ai#c.OV_ITT_TASK_CHAIN) Begins the sequrence of an annotated sections of code using

`prefix`

and`taskName`

as section id.In case if prefix absent, the current function name is used, if taskName absent, the first chain index is used, i.e 1.

In case if prefix absent, the current function name is used, if taskName absent, the first chain index is used, i.e 1.

- Parameters:
**group**– [in] ITT counter group name used for enabling/disabling at compile time.**chainId**– [in] The tasks chain identifier.**domainName**– [in] Known at compile time name of module or library (the domain name).**prefix**– [in] The task chain name prefix. The task name starts with this prefix. Parameter is optional.**taskName**– [in] The annotation name for section of code. Parameter is optional.**chainId**– [in] The tasks chain identifier.**domainName**– [in] Known at compile time name of module or library (the domain name).**prefix**– [in] The task chain name prefix. The task name starts with this prefix. Parameter is optional.**taskName**– [in] The annotation name for section of code. Parameter is optional.



-
OV_ITT_SCOPE_NEXT(group, ...)
[#](https://docs.openvino.ai#c.OV_ITT_SCOPE_NEXT) Inserts new annotated section of code to tasks chain using

`taskName`

as section id.If taskName is missing, the current chain index is used.

- Parameters:
**group**– [in] ITT counter group name used for enabling/disabling at compile time.**chainId**– [in] The tasks chain identifier.**taskOrTaskName**– [in] The annotation name or handle for section of code. Parameter is optional.



-
OV_ITT_SCOPE_SKIP(group, chainId)
[#](https://docs.openvino.ai#c.OV_ITT_SCOPE_SKIP) Skips the remaining task scope.

- Parameters:
**group**– [in] ITT counter group name used for enabling/disabling at compile time.**chainId**– [in] The tasks chain identifier.



-
OV_ITT_TASK_NEXT(...)
[#](https://docs.openvino.ai#c.OV_ITT_TASK_NEXT) Inserts new annotated section of code to tasks chain using

`taskName`

as section id.If taskName is missing, the current chain index is used.

- Parameters:
**chainId**– [in] The tasks chain identifier.**taskOrTaskName**– [in] The annotation name or handle for section of code. Parameter is optional.



-
OV_ITT_TASK_SKIP(chainId)
[#](https://docs.openvino.ai#c.OV_ITT_TASK_SKIP) Skips the remaining task scope.

- Parameters:
**chainId**– [in] The tasks chain identifier.



-
OV_ITT_REGION_BEGIN(group, domain, handleOrRegionName)
[#](https://docs.openvino.ai#c.OV_ITT_REGION_BEGIN) Begin a region of code to be profiled using known

`handle`

or`regionName`

as section id.- Parameters:
**group**– [in] ITT counter group name used for enabling/disabling at compile time.**domain**– [in] Known at compile time name of module or library (the domain name).**handleOrRegionName**– [in] The annotation name or handle for section of code.



-
OV_ITT_REGION_END(group, domain, handleOrRegionName)
[#](https://docs.openvino.ai#c.OV_ITT_REGION_END) End a region of code to be profiled using known

`handle`

or`regionName`

as section id.- Parameters:
**group**– [in] ITT counter group name used for enabling/disabling at compile time.**domain**– [in] Known at compile time name of module or library (the domain name).**handleOrRegionName**– [in] The annotation name or handle for section of code.



Typedefs

Functions

-
inline void threadName(const char *name)
[#](https://docs.openvino.ai#_CPPv410threadNamePKc) Set thread name using a char string.

- Parameters:
**name**– [in] The thread name


-
template<
[domain_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8domain_tE)(*domain)()>

class ScopedTask[#](https://docs.openvino.ai#_CPPv4I_PF8domain_tvEEN8openvino3itt10ScopedTaskE) *#include <itt.hpp>*Used to annotate section of code which would be named at runtime.

Note

Uses ITT task begin/end. If a region is active on the current thread, tasks started within it are recorded as its children.

- Template Parameters:
**The**–`domain`

parameter is domain type which shoud be defined with[OV_ITT_DOMAIN()](https://docs.openvino.ai#group__ov__dev__profiling_1ga83ad6f539c8e1aef944160e37fcfcb4d)macro.

Public Functions

-
inline ScopedTask(
[handle_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8handle_tE)taskHandle) noexcept[#](https://docs.openvino.ai#_CPPv4N8openvino3itt10ScopedTask10ScopedTaskE8handle_t) Construct

[ScopedTask](https://docs.openvino.ai/structopenvino_1_1itt_1_1_scoped_task.html#structopenvino_1_1itt_1_1_scoped_task)with defined annotation handle.

-
inline ~ScopedTask() noexcept
[#](https://docs.openvino.ai#_CPPv4N8openvino3itt10ScopedTaskD0Ev) The

[ScopedTask](https://docs.openvino.ai/structopenvino_1_1itt_1_1_scoped_task.html#structopenvino_1_1itt_1_1_scoped_task)destructor closes or ends the task scope.


-
template<
[domain_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8domain_tE)(*domain)()>

class ScopedRegion[#](https://docs.openvino.ai#_CPPv4I_PF8domain_tvEEN8openvino3itt12ScopedRegionE) *#include <itt.hpp>*Used to annotate region of code which would be named at runtime using RAII.

Note

Uses ITT region begin/end. At most one region is active per thread; tasks started while a region is active attach to it as their parent.

- Template Parameters:
**The**–`domain`

parameter is domain type which shoud be defined with[OV_ITT_DOMAIN()](https://docs.openvino.ai#group__ov__dev__profiling_1ga83ad6f539c8e1aef944160e37fcfcb4d)macro.

Public Functions

-
inline ScopedRegion(
[handle_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8handle_tE)handle) noexcept[#](https://docs.openvino.ai#_CPPv4N8openvino3itt12ScopedRegion12ScopedRegionE8handle_t) Construct

[ScopedRegion](https://docs.openvino.ai/structopenvino_1_1itt_1_1_scoped_region.html#structopenvino_1_1itt_1_1_scoped_region)with defined annotation handle.

-
inline ~ScopedRegion() noexcept
[#](https://docs.openvino.ai#_CPPv4N8openvino3itt12ScopedRegionD0Ev) The

[ScopedRegion](https://docs.openvino.ai/structopenvino_1_1itt_1_1_scoped_region.html#structopenvino_1_1itt_1_1_scoped_region)destructor closes or ends the region scope.


-
template<
[domain_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8domain_tE)(*domain)()>

class TaskChain[#](https://docs.openvino.ai#_CPPv4I_PF8domain_tvEEN8openvino3itt9TaskChainE) *#include <itt.hpp>*Used to annotate a sequence of sections of code which would be named at runtime.

- Template Parameters:
**The**–`domain`

parameter is domain type which shoud be defined with[OV_ITT_DOMAIN()](https://docs.openvino.ai#group__ov__dev__profiling_1ga83ad6f539c8e1aef944160e37fcfcb4d)macro.


-
namespace openvino
[#](https://docs.openvino.ai#_CPPv48openvino) openvino namespace

-
namespace cc
[#](https://docs.openvino.ai#_CPPv4N8openvino2ccE) -
template<typename Key, typename T>

class Factory[#](https://docs.openvino.ai#_CPPv4I00EN8openvino2cc7FactoryE)

-
template<typename Key, typename T, typename ...Args>

class Factory<[Key](https://docs.openvino.ai#_CPPv4I00DpEN8openvino2cc7FactoryI3KeyF1TDp4ArgsEEE),[T](https://docs.openvino.ai#_CPPv4I00DpEN8openvino2cc7FactoryI3KeyF1TDp4ArgsEEE)([Args](https://docs.openvino.ai#_CPPv4I00DpEN8openvino2cc7FactoryI3KeyF1TDp4ArgsEEE)...)>[#](https://docs.openvino.ai#_CPPv4I00DpEN8openvino2cc7FactoryI3KeyF1TDp4ArgsEEE) *#include <factory.h>*

-
namespace internal
[#](https://docs.openvino.ai#_CPPv4N8openvino2cc8internalE) Functions

-
template<typename T, typename C>
[case_wrapper](https://docs.openvino.ai#_CPPv4I00EN8openvino2cc8internal12case_wrapperE)<[C](https://docs.openvino.ai#_CPPv4I00EN8openvino2cc8internal17make_case_wrapperE12case_wrapperI1C1TERR1C),[T](https://docs.openvino.ai#_CPPv4I00EN8openvino2cc8internal17make_case_wrapperE12case_wrapperI1C1TERR1C)> make_case_wrapper([C](https://docs.openvino.ai#_CPPv4I00EN8openvino2cc8internal17make_case_wrapperE12case_wrapperI1C1TERR1C)&&val)[#](https://docs.openvino.ai#_CPPv4I00EN8openvino2cc8internal17make_case_wrapperE12case_wrapperI1C1TERR1C)

-
template<typename C, typename T>

struct case_wrapper[#](https://docs.openvino.ai#_CPPv4I00EN8openvino2cc8internal12case_wrapperE) *#include <selective_build.h>*

-
template<typename T, typename C>

-
template<typename Key, typename T>

-
namespace itt
[#](https://docs.openvino.ai#_CPPv4N8openvino3ittE) Typedefs

Functions

-
inline void threadName(const char *name)
[#](https://docs.openvino.ai#_CPPv4N8openvino3itt10threadNameEPKc) Set thread name using a char string.

- Parameters:
**name**– [in] The thread name


-
inline void threadName(const std::string &name)
[#](https://docs.openvino.ai#_CPPv4N8openvino3itt10threadNameERKNSt6stringE)

-
struct domain_
[#](https://docs.openvino.ai#_CPPv4N8openvino3itt7domain_E) *#include <itt.hpp>*

-
struct handle_
[#](https://docs.openvino.ai#_CPPv4N8openvino3itt7handle_E) *#include <itt.hpp>*

-
template<
[domain_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8domain_tE)(*domain)()>

class ScopedRegion *#include <itt.hpp>*Used to annotate region of code which would be named at runtime using RAII.

Note

Uses ITT region begin/end. At most one region is active per thread; tasks started while a region is active attach to it as their parent.

- Template Parameters:
**The**–`domain`

parameter is domain type which shoud be defined with[OV_ITT_DOMAIN()](https://docs.openvino.ai#group__ov__dev__profiling_1ga83ad6f539c8e1aef944160e37fcfcb4d)macro.

Public Functions

-
inline ScopedRegion(
[handle_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8handle_tE)handle) noexcept Construct

[ScopedRegion](https://docs.openvino.ai/structopenvino_1_1itt_1_1_scoped_region.html#structopenvino_1_1itt_1_1_scoped_region)with defined annotation handle.

-
inline ~ScopedRegion() noexcept
The

[ScopedRegion](https://docs.openvino.ai/structopenvino_1_1itt_1_1_scoped_region.html#structopenvino_1_1itt_1_1_scoped_region)destructor closes or ends the region scope.


-
template<
[domain_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8domain_tE)(*domain)()>

class ScopedTask *#include <itt.hpp>*Used to annotate section of code which would be named at runtime.

Note

Uses ITT task begin/end. If a region is active on the current thread, tasks started within it are recorded as its children.

- Template Parameters:
**The**–`domain`

parameter is domain type which shoud be defined with[OV_ITT_DOMAIN()](https://docs.openvino.ai#group__ov__dev__profiling_1ga83ad6f539c8e1aef944160e37fcfcb4d)macro.

Public Functions

-
inline ScopedTask(
[handle_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8handle_tE)taskHandle) noexcept Construct

[ScopedTask](https://docs.openvino.ai/structopenvino_1_1itt_1_1_scoped_task.html#structopenvino_1_1itt_1_1_scoped_task)with defined annotation handle.

-
inline ~ScopedTask() noexcept
The

[ScopedTask](https://docs.openvino.ai/structopenvino_1_1itt_1_1_scoped_task.html#structopenvino_1_1itt_1_1_scoped_task)destructor closes or ends the task scope.


-
template<
[domain_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8domain_tE)(*domain)()>

class TaskChain *#include <itt.hpp>*Used to annotate a sequence of sections of code which would be named at runtime.

- Template Parameters:
**The**–`domain`

parameter is domain type which shoud be defined with[OV_ITT_DOMAIN()](https://docs.openvino.ai#group__ov__dev__profiling_1ga83ad6f539c8e1aef944160e37fcfcb4d)macro.

Public Functions

-
inline TaskChain(
[handle_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8handle_tE)taskHandle, std::string &&prefix) noexcept Construct

[TaskChain](https://docs.openvino.ai/classopenvino_1_1itt_1_1_task_chain.html#classopenvino_1_1itt_1_1_task_chain)with defined annotation handle.

-
inline ~TaskChain() noexcept
The

[TaskChain](https://docs.openvino.ai/classopenvino_1_1itt_1_1_task_chain.html#classopenvino_1_1itt_1_1_task_chain)destructor closes or ends the task scope.

-
inline void next(
[handle_t](https://docs.openvino.ai#_CPPv4N8openvino3itt8handle_tE)taskHandle) Ends the previous task from the chain and starts a new one with the given annotation handle.



-
inline void threadName(const char *name)

-
namespace cc

-
OV_ITT_DOMAIN(...)