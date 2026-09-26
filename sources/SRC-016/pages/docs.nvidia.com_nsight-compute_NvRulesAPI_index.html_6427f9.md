source: https://docs.nvidia.com/nsight-compute/NvRulesAPI/index.html

# 3. NvRules API[#](https://docs.nvidia.com#module-NvRules)

-
*class*NvRules.IAction[#](https://docs.nvidia.com#NvRules.IAction) Bases:

`object`

The

represents a profile result such as a CUDA kernel in a single range or a range itself in range-based profiling, for which zero or more metrics were collected.`IAction`

-
__iter__()
[#](https://docs.nvidia.com#NvRules.IAction.__iter__)

-
__len__()
[#](https://docs.nvidia.com#NvRules.IAction.__len__)

-
name(
**args*)[#](https://docs.nvidia.com#NvRules.IAction.name) Get the name of the result the

object represents.`IAction`

- Parameters:
**name_base**(, optional) – The desired name base. Defaults to`int`

.`NameBase_FUNCTION`

- Returns:
The name of the result (potentially in a specific name base).

- Return type:


-
nvtx_state()
[#](https://docs.nvidia.com#NvRules.IAction.nvtx_state) Get the NVTX state associated with this action.

- Returns:
The associated

or`INvtxState`

if no state is associated.`None`

- Return type:


-
ptx_by_pc(
*address*)[#](https://docs.nvidia.com#NvRules.IAction.ptx_by_pc) Get the PTX associated with an address.


-
sass_by_pc(
*address*)[#](https://docs.nvidia.com#NvRules.IAction.sass_by_pc) Get the SASS associated with an address.


-
source_files()
[#](https://docs.nvidia.com#NvRules.IAction.source_files) Get the source files associated with this action along with their content.

If content is not available for a file (e.g. because it hadn’t been imported into the report), the file name will map to an empty string.


-
source_info(
*address*)[#](https://docs.nvidia.com#NvRules.IAction.source_info) Get the source info for a function address within this action.

Addresses are commonly obtained as correlation IDs of source-correlated metrics.


-
__iter__()

-
*class*NvRules.IContext[#](https://docs.nvidia.com#NvRules.IContext) Bases:

`IBaseContext`

The

class is the top-level object representing an open report.`IContext`

It can be created by calling the

`load_report`

function.-
__getitem__(
*key*)[#](https://docs.nvidia.com#NvRules.IContext.__getitem__) Get one or more

objects by index or by slice.`IRange`

Returns:

|`IRange`

of`tuple`

: An`IRange`

object or a`IRange`

of`tuple`

objects.`IRange`

- Raises:
– If**IndexError**`key`

is out of range for the.`IContext`




-
__iter__()
[#](https://docs.nvidia.com#NvRules.IContext.__iter__)

-
__len__()
[#](https://docs.nvidia.com#NvRules.IContext.__len__)

-
controller()
[#](https://docs.nvidia.com#NvRules.IContext.controller) Get the controller object.

- Returns:
The controller object.

- Return type:


-
num_ranges()
[#](https://docs.nvidia.com#NvRules.IContext.num_ranges)

-
__getitem__(

-
*class*NvRules.IController[#](https://docs.nvidia.com#NvRules.IController) Bases:

`object`

Controller interface.

The controller can be used to interact with the tool runtime, e.g., to signal the tools to propose a follow-up rule.

-
get_message_vault()
[#](https://docs.nvidia.com#NvRules.IController.get_message_vault) Get an

object that can be used for message passing between rules.`IMessageVault`

- Returns:


-
get_message_vault()

-
*class*NvRules.IEvaluator[#](https://docs.nvidia.com#NvRules.IEvaluator) Bases:

`IBaseContext`

Evaluator interface.

The evaluator is used during rule setup to pass information about rule dependencies to the tool. For most cases, its Python wrapper functions

and`require_metrics`

should be used instead for convenience.`require_rules`


-
*class*NvRules.IFrontend[#](https://docs.nvidia.com#NvRules.IFrontend) Bases:

`object`

The frontend is responsible for relaying messages and results to the caller via user interfaces, logs or output files.

- Deprecated Attributes and Their Replacement:
MarkerKind_SASS -

`MarkerKind.SASS`

MarkerKind_SOURCE -

`MarkerKind.SOURCE`

MsgType_MSG_NONE -

`MsgType.NONE`

MsgType_MSG_OK -

`MsgType.OK`

MsgType_MSG_OPTIMIZATION -

`MsgType.OPTIMIZATION`

MsgType_MSG_WARNING -

`MsgType.WARNING`

MsgType_MSG_ERROR -

`MsgType.ERROR`


-
SpeedupType_LOCAL
[#](https://docs.nvidia.com#NvRules.IFrontend.SpeedupType_LOCAL) The proportional increase in efficiency of the hardware usage when viewing the performance problem in isolation.

- Type:


- focus_metric(
*message_id*,*metric_name*,*metric_value*,*severity*,*info*,Create a rule focus metric message.

Issues a focus metric message to the frontend, e.g. to indicate a key metric that triggered the rule output.

- Parameters:
**message_id**() – The prior message to associate with.`int`

**metric_name**() – Name of the focus metric.`str`

**metric_value**() – Value of the focus metric.`float`

**severity**() – Indicates the impact orseverity on the result.`int`

**info**() – Descriptive string for further information, e.g., the calculation leading to this metric being focused.`str`


- Returns:
- Return type:


[#](https://docs.nvidia.com#NvRules.IFrontend.focus_metric)-
generate_table(
*message_id*,*header*,*data*,*config=None*)[#](https://docs.nvidia.com#NvRules.IFrontend.generate_table) Generate a table in the frontend.

This function attaches a table to the pre-existing rule message given by message_id. It can be called multiple times to attach multiple tables to the same message.

The table can be customized by passing a dict to the config parameter. The table can contain a title, description, a column to sort by, and a global styling. Additionally, the table can have per-column configurations, which can specify a header tooltip, relative column width, and styling for the header and data cells.

This is an example of a valid config dict:

config = { "title": "My table title", "description": "Short description of the table", "sort_by": { "column": "MyColumn", # specify column by name or index "order": "ascending", # in ascending order (default) }, "per_column_configs": { # overwrites global styling for individual columns "MyColumn": { # can use column name or index "tooltip": "Explanation of MyColumn", # tooltip for the header "relative_width": 0.5, # relative width of the column "style": { "header": {"bold": True}, "data": {"italic": True}, } }, }, }

- Parameters:
**message_id**() – The message to which to attach the table to.*int***data**(*list**[**list**[**int**|**float**|**str**|**Any**]**]*) –The table data in row-major format. Any refers to any type that implements __str__. Each column must only have elements of the same type, and all columns must have the same length.

- class:str values may contain substrings with the following special link formats:
@url:<hypertext>:<external link>@ - To add a external link for a hypertext.

@sass:<address>:<hypertext>@ - To add a link to the hypertext to open the SASS address line on the Source page.

@source:<file name>:<line number>:<hypertext>@ - To add a link to the hypertext to open the source file at the specified line number on the Source page.

@section:<section identifier>:<hypertext>@ - To add a link to the hypertext to jump to the respective section.



**config**(*dict**[**str**,**Any**]**|**None*) – Configuration options for the table. Defaults to None.

- Raises:
– If types of elements within a column are mixed.**TypeError**– If columns have different lengths, or len(header) does not match the number of columns in data.**ValueError**



-
load_chart_from_file(
*filename*)[#](https://docs.nvidia.com#NvRules.IFrontend.load_chart_from_file) Load a ProfilerSection google protocol buffer chart from a file.

- Parameters:
**filename**() – The file name.`str`



-
message(
**args*)[#](https://docs.nvidia.com#NvRules.IFrontend.message) Issues a message to the frontend.

- Parameters:
**type**(, optional) – The message type.`int`

**str**() –`str`

The message content.

- The message may contain substrings with the following special link formats:
@url:<hypertext>:<external link>@ - To add a external link for a hypertext.

@sass:<address>:<text>@ - To add a SASS address to the cell.

@source:<file name>:<line number>:<hypertext>@ - To add a link to the hypertext to open the source file at the specified line number on the Source page.

@section:<section identifier>:<hypertext>@ - To add a link to the hypertext to jump to the respective section.



**name**(, optional) – The name of the message.`str`


- Returns:
A message ID that is unique in this rule invocation.

- Return type:


-
receive_dict_from_parent(
*parent_id*)[#](https://docs.nvidia.com#NvRules.IFrontend.receive_dict_from_parent) Receive a dictionary from a parent rule.

Receive a dictionary of type dict[str,float] sent using

. If the parent id does not represent a pre-specified parent rule of this rule, or in case the parent rule has not been executed, an empty dict will be returned.`IFrontend.send_dict_to_children`


-
send_dict_to_children(
*dict*)[#](https://docs.nvidia.com#NvRules.IFrontend.send_dict_to_children) Send a dictionary to all child rules.

Sends a Python dictionary of type dict[str,float] to all rules that specify this rule as a parent rule. Child rules can retrieve the message using

. In case this function is called repeatedly, the dict is updated accordingly, thereby adding new key-value pairs, and overwriting values of pre-existing keys.`IFrontend.receive_dict_from_parent`

- Parameters:
**dict**() – The dictionary to send.`dict`



-
source_marker(
**args*)[#](https://docs.nvidia.com#NvRules.IFrontend.source_marker) Create a rule source marker.


-
speedup(
*message_id*,*type*,*estimated_speedup*)[#](https://docs.nvidia.com#NvRules.IFrontend.speedup) Rule estimated speedup message.

Issues an estimated speedup associated with a message to the frontend.

- Parameters:
**message_id**() – ID of the existing message.`int`

**type**() – The SpeedupType. If GLOBAL, it indicates what proportional decrease in workload runtime could potentially be achieved, when following the guidelines of the rule. If LOCAL, it indicates what increase in the efficiency of the hardware usage within the context of the performance problem could be achieved.`int`


- Returns:
- Return type:



-
*class*NvRules.IMessageVault[#](https://docs.nvidia.com#NvRules.IMessageVault) Bases:

`object`

Passes messages between rules.

-
Get(
*ruleId*)[#](https://docs.nvidia.com#NvRules.IMessageVault.Get) Retrieve the message associated with a rule from the vault.

In case the rule is unknown, an empty message is returned.


-
Put(
*ruleId*,*message*)[#](https://docs.nvidia.com#NvRules.IMessageVault.Put) Commit a message associated with a rule to the vault.

In case multiple messages associated with the same rule are committed, the messages are merged, in such a way that new key-value pairs are added, and values of pre-existing keys are updated.


-
Get(

-
*class*NvRules.IMetric[#](https://docs.nvidia.com#NvRules.IMetric) Bases:

`object`

Represents a single, named metric. An

can carry one value or multiple ones if it is an instanced metric.`IMetric`

-
MetricSubtype_PEAK_SUSTAINED_ACTIVE_PER_SECOND
[#](https://docs.nvidia.com#NvRules.IMetric.MetricSubtype_PEAK_SUSTAINED_ACTIVE_PER_SECOND) Metric subtype for peak sustained active per-second metrics.

- Type:


-
MetricSubtype_PEAK_SUSTAINED_ELAPSED_PER_SECOND
[#](https://docs.nvidia.com#NvRules.IMetric.MetricSubtype_PEAK_SUSTAINED_ELAPSED_PER_SECOND) Metric subtype for peak sustained elapsed per-second metrics.

- Type:


-
MetricSubtype_PCT_OF_PEAK_SUSTAINED_ACTIVE
[#](https://docs.nvidia.com#NvRules.IMetric.MetricSubtype_PCT_OF_PEAK_SUSTAINED_ACTIVE) Metric subtype for percentage of peak sustained active metrics.

- Type:


-
MetricSubtype_PCT_OF_PEAK_SUSTAINED_ELAPSED
[#](https://docs.nvidia.com#NvRules.IMetric.MetricSubtype_PCT_OF_PEAK_SUSTAINED_ELAPSED) Metric subtype for percentage of peak sustained elapsed metrics.

- Type:


-
correlation_ids()
[#](https://docs.nvidia.com#NvRules.IMetric.correlation_ids) Get a metric object for this metric’s instance value’s correlation IDs.

Returns a new

representing the correlation IDs for the metric’s instance values. Use`IMetric`

to check if this metric has correlation IDs for its instance values. Correlation IDs are used to associate instance values with the instance their value represents. In the returned new metric object, the correlation IDs are that object’s instance values.`IMetric.has_correlation_ids`

If the metric does not have any correlation IDs, this function will return

.`None`


-
has_correlation_ids()
[#](https://docs.nvidia.com#NvRules.IMetric.has_correlation_ids) Check if the metric has correlation IDs.


-
has_value(
**args*)[#](https://docs.nvidia.com#NvRules.IMetric.has_value) Check if the metric or metric instance has a value.


-
kind(
**args*)[#](https://docs.nvidia.com#NvRules.IMetric.kind) Get the metric or metric instance value kind.


-
num_instances()
[#](https://docs.nvidia.com#NvRules.IMetric.num_instances) Get the number of instance values for this metric.

Not all metrics have instance values. If a metric has instance values, it may also have

matching these instance values.`IMetric.correlation_ids`

- Returns:
The number of instances for this metric.

- Return type:


-
rollup_operation()
[#](https://docs.nvidia.com#NvRules.IMetric.rollup_operation) Get the type of rollup operation for this metric.

- Returns:
The rollup operation type.

- Return type:


-
MetricSubtype_PEAK_SUSTAINED_ACTIVE_PER_SECOND

-
*class*NvRules.IMutableMetric[#](https://docs.nvidia.com#NvRules.IMutableMetric) Bases:

`IMetric`

Represents a single, named mutable metric. An

can carry one value or multiple ones if it is an instanced metric. In comparison to`IMutableMetric`

,`IMetric`

can be modified by assigning it a new value and/or instance values. The metric kind is determined by the assigned value(s).`IMutableMetric`

-
mutable_correlation_ids()
[#](https://docs.nvidia.com#NvRules.IMutableMetric.mutable_correlation_ids) Get a mutable metric object for this metric’s instance value’s correlation IDs.

Returns a new

representing the correlation IDs for the metric’s instance values. Correlation IDs are used to associate instance values with the instance their value represents. In the returned new metric object, the correlation IDs are that object’s instance values.`IMutableMetric`

- Returns:
The new

object representing the correlation IDs for this metric’s instance values.`IMutableMetric`

- Return type:


-
mutable_correlation_ids()

-
*class*NvRules.INvtxDomainInfo[#](https://docs.nvidia.com#NvRules.INvtxDomainInfo) Bases:

`object`

Represents a single NVTX domain of the NVTX state, including all ranges associated with this domain.

-
__str__()
[#](https://docs.nvidia.com#NvRules.INvtxDomainInfo.__str__) Get a human-readable representation of this

.`INvtxDomainInfo`

- Returns:
The name of the

.`INvtxDomainInfo`

- Return type:


-
name()
[#](https://docs.nvidia.com#NvRules.INvtxDomainInfo.name) Get a human-readable representation of this

.`INvtxDomainInfo`

- Returns:
The name of the

.`INvtxDomainInfo`

- Return type:


-
push_pop_range(
*idx*)[#](https://docs.nvidia.com#NvRules.INvtxDomainInfo.push_pop_range) Get a push/pop range object by index.

The index is identical to the range’s order on the call stack.

- Returns:
The requested

or`INvtxRange`

if the index is out of range.`None`

- Return type:


-
push_pop_ranges()
[#](https://docs.nvidia.com#NvRules.INvtxDomainInfo.push_pop_ranges) Get a sorted list of push/pop range names.

Get the sorted list of stacked push/pop range names in this domain, associated with the current

.`INvtxState`


-
start_end_range(
*idx*)[#](https://docs.nvidia.com#NvRules.INvtxDomainInfo.start_end_range) Get a start/end range object by index.

- Returns:
The requested

or`INvtxRange`

if the index is out of range.`None`

- Return type:


-
start_end_ranges()
[#](https://docs.nvidia.com#NvRules.INvtxDomainInfo.start_end_ranges) Get a sorted list of start/end range names.

Get the sorted list of start/end range names in this domain, associated with the current

.`INvtxState`


-
__str__()

-
*class*NvRules.INvtxRange[#](https://docs.nvidia.com#NvRules.INvtxRange) Bases:

`object`

Represents a single NVTX Push/Pop or Start/End range.

-
category()
[#](https://docs.nvidia.com#NvRules.INvtxRange.category) Get the category attribute value.

- Returns:
The category attribute value. If

returns`INvtxRange.has_attributes`

, this will return`False`

`0`

.- Return type:


-
color()
[#](https://docs.nvidia.com#NvRules.INvtxRange.color) Get the color attribute value.

- Returns:
The color attribute value. If

returns`INvtxRange.has_attributes`

, this will return`False`

`0`

.- Return type:


-
has_attributes()
[#](https://docs.nvidia.com#NvRules.INvtxRange.has_attributes) Check if range has event attributes.


-
message()
[#](https://docs.nvidia.com#NvRules.INvtxRange.message) Get the message attribute value.

- Returns:
The message attribute value. If

returns`INvtxRange.has_attributes`

, this will return the empty string.`False`

- Return type:


-
category()

-
*class*NvRules.INvtxState[#](https://docs.nvidia.com#NvRules.INvtxState) Bases:

`object`

Represents the NVTX (Nvidia Tools Extensions) state associated with a single

.`IAction`

-
__getitem__(
*key*)[#](https://docs.nvidia.com#NvRules.INvtxState.__getitem__) Get an

object by ID.`INvtxDomainInfo`

- Parameters:
**key**() – The ID of the`int`

object.`INvtxDomainInfo`

- Returns:
An

object.`INvtxDomainInfo`

- Return type:
- Raises:


-
__iter__()
[#](https://docs.nvidia.com#NvRules.INvtxState.__iter__) Get an

[iterator](https://docs.python.org/3/glossary.html#term-iterator)over theobjects of this`INvtxDomainInfo`

.`INvtxState`

- Returns:
An

[iterator](https://docs.python.org/3/glossary.html#term-iterator)over theobjects.`INvtxDomainInfo`

- Return type:


-
__len__()
[#](https://docs.nvidia.com#NvRules.INvtxState.__len__) Get the number of

objects of this`INvtxDomainInfo`

.`INvtxState`

- Returns:
The number of

objects.`INvtxDomainInfo`

- Return type:


-
domain_by_id(
*id*)[#](https://docs.nvidia.com#NvRules.INvtxState.domain_by_id) Get a

object by ID.`INvtxDomainInfo`

Use

to retrieve the list of valid domain IDs.`INvtxState.domains`

- Parameters:
**id**() – The ID of the request domain.`int`

- Returns:
The requested

object.`INvtxDomainInfo`

- Return type:


-
__getitem__(

-
*class*NvRules.IRange[#](https://docs.nvidia.com#NvRules.IRange) Bases:

`object`

Represents a serial, ordered stream of execution, such as a CUDA stream. It holds one or more actions that were logically executing in this range.

-
__getitem__(
*key*)[#](https://docs.nvidia.com#NvRules.IRange.__getitem__)

-
__len__()
[#](https://docs.nvidia.com#NvRules.IRange.__len__) Get the number of

objects in this`IAction`

.`IRange`

- Returns:
The number of class:IAction objects.

- Return type:


-
actions_by_nvtx(
*includes*,*excludes*)[#](https://docs.nvidia.com#NvRules.IRange.actions_by_nvtx) Get a set of indices to IAction objects by their NVTX state. The state is defined using a series of

*includes*and*excludes*.

-
__getitem__(

-
*class*NvRules.MarkerKind[#](https://docs.nvidia.com#NvRules.MarkerKind) Bases:

`IntEnum`

Enum representing the kind of a source marker.

-
SASS
[#](https://docs.nvidia.com#NvRules.MarkerKind.SASS) The marker will be associated with a SASS instruction.


-
SOURCE
[#](https://docs.nvidia.com#NvRules.MarkerKind.SOURCE) The marker will be associated with a Source line.


-
NONE
[#](https://docs.nvidia.com#NvRules.MarkerKind.NONE) No specific kind of marker.


-
__new__(
*value*)[#](https://docs.nvidia.com#NvRules.MarkerKind.__new__)

-
SASS

-
*class*NvRules.MsgType[#](https://docs.nvidia.com#NvRules.MsgType) Bases:

`IntEnum`

Enum representing the type of the message.

-
NONE
[#](https://docs.nvidia.com#NvRules.MsgType.NONE) No specific type for this message.


-
OK
[#](https://docs.nvidia.com#NvRules.MsgType.OK) The message is informative.


-
OPTIMIZATION
[#](https://docs.nvidia.com#NvRules.MsgType.OPTIMIZATION) The message represents a suggestion for performance optimization.


-
WARNING
[#](https://docs.nvidia.com#NvRules.MsgType.WARNING) The message represents a warning or fixable issue.


-
ERROR
[#](https://docs.nvidia.com#NvRules.MsgType.ERROR) The message represents an error, potentially in executing the rule.


-
__new__(
*value*)[#](https://docs.nvidia.com#NvRules.MsgType.__new__)

-
NONE

-
NvRules.get_evaluator(
*h*)[#](https://docs.nvidia.com#NvRules.get_evaluator) Return the

object from the context handle.`IEvaluator`

- Parameters:
**h**() – The context handle.`int`

- Returns:
The evaluator object.

- Return type:


-
NvRules.get_version(
*h*)[#](https://docs.nvidia.com#NvRules.get_version) Get version number of this interface.


-
NvRules.require_metrics(
*handle*,*metrics*)[#](https://docs.nvidia.com#NvRules.require_metrics) Convenience wrapper for

.`NvRules.IEvaluator.require_metric`

- Parameters:
**handle**() – The context handle, obtained from`int`

.`get_context`

**metrics**() – List of metric names.`list`




-
NvRules.require_rules(
*handle*,*rules*)[#](https://docs.nvidia.com#NvRules.require_rules) Convenience wrapper for

.`NvRules.IEvaluator.require_rule`

- Parameters:
**handle**() – The context handle, obtained from`int`

.`get_context`

**rules**() – List of rule identifiers.`list`




Notices

Notices

ALL NVIDIA DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESSED, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES OF NONINFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE.

Information furnished is believed to be accurate and reliable. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication of otherwise under any patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all other information previously supplied. NVIDIA Corporation products are not authorized as critical components in life support devices or systems without express written approval of NVIDIA Corporation.

Trademarks

NVIDIA and the NVIDIA logo are trademarks or registered trademarks of NVIDIA Corporation in the U.S. and other countries. Other company and product names may be trademarks of the respective companies with which they are associated.