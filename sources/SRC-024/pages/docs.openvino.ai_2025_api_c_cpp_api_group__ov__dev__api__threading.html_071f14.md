source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__dev__api__threading.html
lastmod: 

# Group Threading utilities[#](https://docs.openvino.ai#group-threading-utilities)

-
*group*Threading utilities Threading API providing task executors for asynchronous operations.

Typedefs

-
using Task = std::function<void()>
[#](https://docs.openvino.ai#_CPPv44Task) OpenVINO Task Executor can use any copyable callable without parameters and output as a task. It would be wrapped into std::function object.


-
class ImmediateExecutor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[threading](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threadingE)::[ITaskExecutor](https://docs.openvino.ai#_CPPv4N2ov9threading13ITaskExecutorE)[#](https://docs.openvino.ai#_CPPv4N2ov9threading17ImmediateExecutorE) *#include <immediate_executor.hpp>*Task executor implementation that just run tasks in current thread during calling of

[run()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_immediate_executor_1a2517a367fd9ea064e5d92ce9a1b7b5dd)method.Public Types

-
using Ptr = std::shared_ptr<
[ImmediateExecutor](https://docs.openvino.ai/classov_1_1threading_1_1_immediate_executor.html#_CPPv4N2ov9threading17ImmediateExecutorE)>[#](https://docs.openvino.ai#_CPPv4N2ov9threading17ImmediateExecutor3PtrE) A shared pointer to a

[ImmediateExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_immediate_executor)object.

-
using Ptr = std::shared_ptr<

-
class CPUStreamsExecutor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[threading](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threadingE)::[IStreamsExecutor](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutorE)[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutorE) *#include <cpu_streams_executor.hpp>*CPU Streams executor implementation. The executor splits the CPU into groups of threads, that can be pinned to cores or NUMA nodes. It uses custom threads to pull tasks from single queue.

Public Types

-
using Ptr = std::shared_ptr<
[CPUStreamsExecutor](https://docs.openvino.ai/classov_1_1threading_1_1_c_p_u_streams_executor.html#_CPPv4N2ov9threading18CPUStreamsExecutorE)>[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor3PtrE) A shared pointer to a

[CPUStreamsExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_c_p_u_streams_executor)object.

Public Functions

-
explicit CPUStreamsExecutor(const Config &config)
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor18CPUStreamsExecutorERK6Config) Constructor.

- Parameters:
**config**– Stream executor parameters


-
~CPUStreamsExecutor() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutorD0Ev) A class destructor.


-
virtual void run(
[Task](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threading4TaskE)task) override[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor3runE4Task) Execute ov::Task inside task executor context.

- Parameters:
**task**– A task to start


-
virtual void execute(
[Task](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threading4TaskE)task) override[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor7executeE4Task) Execute the task in the current thread using streams executor configuration and constraints.

- Parameters:
**task**– A task to start


-
virtual int get_stream_id() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor13get_stream_idEv) Return the index of current stream.

- Returns:
An index of current stream. Or throw exceptions if called not from stream thread



-
virtual int get_streams_num() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor15get_streams_numEv) Return the total number of streams.

- Returns:
The total number of streams.



-
virtual int get_numa_node_id() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor16get_numa_node_idEv) Return the id of current NUMA

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)Return 0 when current stream cross some NUMA Nodes.- Returns:
`ID`

of current NUMA[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node), or throws exceptions if called not from stream thread


-
virtual int get_socket_id() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor13get_socket_idEv) Return the id of current socket Return 0 when current stream cross some sockets.

- Returns:
`ID`

of current socket, or throws exceptions if called not from stream thread


-
virtual std::vector<int> get_rank() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor8get_rankEv) Return the rank of current stream Return {} when current stream has no rank.

- Returns:
Rank array, or throws exceptions if called not from stream thread



-
virtual void cpu_reset() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor9cpu_resetEv) Reset cpu map table when user set enable_cpu_reservation = true.


-
using Ptr = std::shared_ptr<

-
interface ExecutorManager
[#](https://docs.openvino.ai#_CPPv4N2ov9threading15ExecutorManagerE) *#include <executor_manager.hpp>*Interface for tasks execution manager. This is global point for getting task executor objects by string id. It’s necessary in multiple asynchronous requests for having unique executors to avoid oversubscription. E.g. There 2 task executors for CPU device: one - in FPGA, another - in OneDNN. Parallel execution both of them leads to not optimal CPU usage. More efficient to run the corresponding tasks one by one via single executor.

Public Functions

-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[threading](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threadingE)::[ITaskExecutor](https://docs.openvino.ai#_CPPv4N2ov9threading13ITaskExecutorE)> get_executor(const std::string &id) = 0[#](https://docs.openvino.ai#_CPPv4N2ov9threading15ExecutorManager12get_executorERKNSt6stringE) Returns executor by unique identificator.

- Parameters:
**id**– An unique identificator of device (Usually string representation of TargetDevice)- Returns:
A shared pointer to existing or newly

[ITaskExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_i_task_executor)


-
virtual std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[threading](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threadingE)::[IStreamsExecutor](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutorE)> get_idle_cpu_streams_executor(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[threading](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threadingE)::[IStreamsExecutor](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutorE)::[Config](https://docs.openvino.ai/structov_1_1threading_1_1_i_streams_executor_1_1_config.html#_CPPv4N2ov9threading16IStreamsExecutor6ConfigE)&config) = 0[#](https://docs.openvino.ai#_CPPv4N2ov9threading15ExecutorManager29get_idle_cpu_streams_executorERKN2ov9threading16IStreamsExecutor6ConfigE) Returns idle cpu streams executor.

- Parameters:
**config**– Streams executor config- Returns:
pointer to streams executor config



-
virtual void set_property(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties) = 0[#](https://docs.openvino.ai#_CPPv4N2ov9threading15ExecutorManager12set_propertyERKN2ov6AnyMapE) Allows to configure executor manager.

- Parameters:
**properties**– map with configuration


-
virtual std::shared_ptr<

-
interface IStreamsExecutor : public virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[threading](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threadingE)::[ITaskExecutor](https://docs.openvino.ai#_CPPv4N2ov9threading13ITaskExecutorE)[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutorE) *#include <istreams_executor.hpp>*Interface for Streams Task Executor. This executor groups worker threads into so-called

`streams`

.**CPU**The executor executes all parallel tasks using threads from one stream. With proper pinning settings it should reduce cache misses for memory bound workloads.

**NUMA**On NUMA hosts GetNumaNodeId() method can be used to define the NUMA node of current stream


Subclassed by

[ov::threading::CPUStreamsExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_c_p_u_streams_executor)Public Types

-
using Ptr = std::shared_ptr<
[IStreamsExecutor](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutorE)>[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor3PtrE) A shared pointer to

[IStreamsExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_i_streams_executor)interface

Public Functions

-
~IStreamsExecutor() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutorD0Ev) A virtual destructor.


-
virtual int get_stream_id() = 0
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor13get_stream_idEv) Return the index of current stream.

- Returns:
An index of current stream. Or throw exceptions if called not from stream thread



-
virtual int get_streams_num() = 0
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor15get_streams_numEv) Return the total number of streams.

- Returns:
The total number of streams.



-
virtual int get_numa_node_id() = 0
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor16get_numa_node_idEv) Return the id of current NUMA

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)Return 0 when current stream cross some NUMA Nodes.- Returns:
`ID`

of current NUMA[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node), or throws exceptions if called not from stream thread


-
virtual int get_socket_id() = 0
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor13get_socket_idEv) Return the id of current socket Return 0 when current stream cross some sockets.

- Returns:
`ID`

of current socket, or throws exceptions if called not from stream thread


-
virtual std::vector<int> get_rank() = 0
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor8get_rankEv) Return the rank of current stream Return {} when current stream has no rank.

- Returns:
Rank array, or throws exceptions if called not from stream thread



-
virtual void cpu_reset() = 0
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor9cpu_resetEv) Reset cpu map table when user set enable_cpu_reservation = true.


-
struct Config
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6ConfigE) *#include <istreams_executor.hpp>*Defines

[IStreamsExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_i_streams_executor)configuration.Public Types

-
enum class StreamsMode
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config11StreamsModeE) This enum contains definition of each sub streams mode, indicating the main stream situation.

*Values:*-
enumerator SUB_STREAMS_NULL
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config11StreamsMode16SUB_STREAMS_NULLE) Do not create sub streams.


-
enumerator SUB_STREAMS_FOR_SOCKET
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config11StreamsMode22SUB_STREAMS_FOR_SOCKETE) Create sub streams for multiple sockets in main stream.


-
enumerator LATENCY
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config11StreamsMode7LATENCYE) latency mode


-
enumerator THROUGHPUT
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config11StreamsMode10THROUGHPUTE) throughput mode


-
enumerator SUB_STREAMS_NULL

Public Functions

-
inline Config(std::string name = "StreamsExecutor", int streams = 1, int threads_per_stream = 0,
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[hint](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hintE)::[SchedulingCoreType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hint18SchedulingCoreTypeE)thread_preferred_core_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[hint](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hintE)::[SchedulingCoreType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hint18SchedulingCoreTypeE)::[ANY_CORE](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hint18SchedulingCoreType8ANY_COREE), bool cpu_reservation = false, bool cpu_pinning = false, bool cores_limit = true, std::vector<std::vector<int>> streams_info_table = {}, std::vector<int> rank = {}, bool add_lock = true)[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config6ConfigENSt6stringEiiN2ov4hint18SchedulingCoreTypeEbbbNSt6vectorINSt6vectorIiEEEENSt6vectorIiEEb) A constructor with arguments.

- Parameters:
**name**–**[in]**The executor name**streams**–**[in]****threads_per_stream**–**[in]****thread_preferred_core_type**–**[in]****cpu_reservation**–**[in]****cpu_pinning**–**[in]****streams_info_table**–**[in]****rank**–**[in]**



-
void set_property(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties)[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config12set_propertyERKN2ov6AnyMapE) Sets configuration.

- Parameters:
**properties**– map of properties


-
enum class StreamsMode

-
struct MessageInfo
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor11MessageInfoE) *#include <istreams_executor.hpp>*


-
interface ITaskExecutor
[#](https://docs.openvino.ai#_CPPv4N2ov9threading13ITaskExecutorE) *#include <itask_executor.hpp>*Interface for Task Executor. OpenVINO uses

`ov::ITaskExecutor`

interface to run all asynchronous internal tasks. Different implementations of task executors can be used for different purposes:To improve cache locality of memory bound CPU tasks some executors can limit task’s affinity and maximum concurrency.

The executor with one worker thread can be used to serialize access to acceleration device.

Immediate task executor can be used to satisfy

`ov::ITaskExecutor`

interface restrictions but run tasks in current thread.

## Synchronization

[#](https://docs.openvino.ai#classov_1_1threading_1_1_i_task_executor_1Synchronization)It is

`ov::ITaskExecutor`

user responsibility to wait for task execution completion. The`c++11`

standard way to wait task completion is to use`std::packaged_task`

or`std::promise`

with`std::future`

. Here is an example of how to use`std::promise`

to wait task completion and process task’s exceptions:// std::promise is move only object so to satisfy copy callable constraint we use std::shared_ptr auto promise = std::make_shared<std::promise<void>>(); // When the promise is created we can get std::future to wait the result auto future = promise->get_future(); // Rather simple task ov::threading::Task task = [] { std::cout << "Some Output" << std::endl; }; // Create an executor ov::threading::ITaskExecutor::Ptr taskExecutor = std::make_shared<ov::threading::CPUStreamsExecutor>(ov::threading::IStreamsExecutor::Config{}); if (taskExecutor == nullptr) { // ProcessError(e); return; } // We capture the task and the promise. When the task is executed in the task executor context // we munually call std::promise::set_value() method taskExecutor->run([task, promise] { std::exception_ptr currentException; try { task(); } catch(...) { // If there is some exceptions store the pointer to current exception currentException = std::current_exception(); } if (nullptr == currentException) { promise->set_value(); // <-- If there is no problems just call std::promise::set_value() } else { promise->set_exception(currentException); // <-- If there is an exception forward it to std::future object } }); // To wait the task completion we call std::future::wait method future.wait(); // The current thread will be blocked here and wait when std::promise::set_value() // or std::promise::set_exception() method will be called. // If the future store the exception it will be rethrown in std::future::get method try { future.get(); } catch(std::exception& /*e*/) { // ProcessError(e); }

Note

Implementation should guaranty thread safety of all methods

Subclassed by

[ov::threading::IStreamsExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_i_streams_executor),[ov::threading::ImmediateExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_immediate_executor)Public Types

-
using Ptr = std::shared_ptr<
[ITaskExecutor](https://docs.openvino.ai#_CPPv4N2ov9threading13ITaskExecutorE)>[#](https://docs.openvino.ai#_CPPv4N2ov9threading13ITaskExecutor3PtrE) A shared pointer to

[ITaskExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_i_task_executor)interface

Public Functions

-
virtual ~ITaskExecutor() = default
[#](https://docs.openvino.ai#_CPPv4N2ov9threading13ITaskExecutorD0Ev) Destroys the object.


-
virtual void run(
[Task](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threading4TaskE)task) = 0[#](https://docs.openvino.ai#_CPPv4N2ov9threading13ITaskExecutor3runE4Task) Execute ov::Task inside task executor context.

- Parameters:
**task**– A task to start


-
virtual void run_and_wait(const std::vector<
[Task](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threading4TaskE)> &tasks)[#](https://docs.openvino.ai#_CPPv4N2ov9threading13ITaskExecutor12run_and_waitERKNSt6vectorI4TaskEE) Execute all of the tasks and waits for its completion. Default

[run_and_wait()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_i_task_executor_1ab57b26fc04ed25b75785a23ed44466eb)method implementation uses[run()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_i_task_executor_1ae5d26041256ec8018f18ae3783f75c32)pure virtual method and higher level synchronization primitives from STL. The task is wrapped into std::packaged_task which returns std::future. std::packaged_task will call the task and signal to std::future that the task is finished or the exception is thrown from task Than std::future is used to wait for task execution completion and task exception extraction.Note

[run_and_wait()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_i_task_executor_1ab57b26fc04ed25b75785a23ed44466eb)does not copy or capture tasks!- Parameters:
**tasks**– A vector of tasks to execute



-
using Task = std::function<void()>