source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__layout__cpp__api.html
lastmod: 

# Group Layout[#](https://docs.openvino.ai#group-layout)

-
*group*Layout OpenVINO

[Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)API to work and configure layouts for[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)inputs or outputsFunctions

- OPENVINO_API bool has_batch (const Layout &layout)
Checks if layout has ‘batch’ dimension.


- OPENVINO_API std::int64_t batch_idx (const Layout &layout)
Returns ‘batch’ dimension index.

- Throws:
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AssertFailure](https://docs.openvino.ai/classov_1_1_assert_failure.html#_CPPv4N2ov13AssertFailureE)– if dimension doesn’t exist.


- OPENVINO_API bool has_channels (const Layout &layout)
Checks if layout has ‘channels’ dimension.

- Throws:
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AssertFailure](https://docs.openvino.ai/classov_1_1_assert_failure.html#_CPPv4N2ov13AssertFailureE)– if dimension doesn’t exist.


- OPENVINO_API std::int64_t channels_idx (const Layout &layout)
Returns ‘channels’ dimension index.

- Throws:
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AssertFailure](https://docs.openvino.ai/classov_1_1_assert_failure.html#_CPPv4N2ov13AssertFailureE)– if dimension doesn’t exist.


- OPENVINO_API bool has_depth (const Layout &layout)
Checks if layout has ‘depth’ dimension.


- OPENVINO_API std::int64_t depth_idx (const Layout &layout)
Returns ‘depth’ dimension index.

- Throws:
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AssertFailure](https://docs.openvino.ai/classov_1_1_assert_failure.html#_CPPv4N2ov13AssertFailureE)– if dimension doesn’t exist.


- OPENVINO_API bool has_height (const Layout &layout)
Checks if layout has ‘height’ dimension.


- OPENVINO_API std::int64_t height_idx (const Layout &layout)
Returns ‘height’ dimension index.

- Throws:
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AssertFailure](https://docs.openvino.ai/classov_1_1_assert_failure.html#_CPPv4N2ov13AssertFailureE)– if dimension doesn’t exist.


- OPENVINO_API bool has_width (const Layout &layout)
Checks if layout has ‘width’ dimension.


- OPENVINO_API std::int64_t width_idx (const Layout &layout)
Returns ‘width’ dimension index.

- Throws:
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AssertFailure](https://docs.openvino.ai/classov_1_1_assert_failure.html#_CPPv4N2ov13AssertFailureE)– if dimension doesn’t exist.


- OPENVINO_API void set_layout (ov::Output< ov::Node > output, const ov::Layout &layout)
Sets

[Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)of port.

- OPENVINO_API ov::Layout get_layout (const ov::Output< ov::Node > &output)
Gets

[Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)of port.- Returns:
layout from port and empty layout in other case



- OPENVINO_API ov::Layout get_layout (const ov::Output< const ov::Node > &output)
Gets

[Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)of port.- Returns:
layout from port and empty layout in other case



-
class Layout
*#include <layout.hpp>*[ov::Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)represents the text information of tensor’s dimensions/axes. E.g. layout`NCHW`

means that 4D tensor`{-1, 3, 480, 640}`

will have:0:

`N = -1`

: batch dimension is dynamic1:

`C = 3`

: number of channels is ‘3’2:

`H = 480`

: image height is 4803:

`W = 640`

: image width is 640

Examples:


can be specified for:[ov::Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)Preprocessing purposes. E.g.

To apply normalization (means/scales) it is usually required to set ‘C’ dimension in a layout.

To resize the image to specified width/height it is needed to set ‘H’ and ‘W’ dimensions in a layout

To transpose image - source and target layout can be set (see


)[ov::preprocess::PreProcessSteps::convert_layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1preprocess_1_1_pre_process_steps_1a0f65fdadca32e90f5ef3a323b640b978)

To set/get model’s batch (see


/[ov::get_batch](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1a07e004b4295ab71df7a23accb362486b)[ov::set_batch](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1a3314e2ff91fcc9ffec05b1a77c37862b)) it is required in general to specify ‘N’ dimension in layout for appropriate inputs

Refer also to


namespace for various additional helper functions of[ov::layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1layout)[ov::Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)Public Functions

-
Layout()
Constructs a dynamic

[Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)with no layout information.

-
inline Layout(const char *layoutStr)
Constructs a

[Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)with static or dynamic layout information based on string representation.- Parameters:
**layoutStr**– The string used to construct[Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout)from. The string representation can be in the following form:can define order and meaning for dimensions “NCHW”

partial layout specialization:

”NC?” defines 3 dimensional layout, first two NC, 3rd one is not defined

”N…C” defines layout with dynamic rank where 1st dimension is N, last one is C

”NC…” defines layout with dynamic rank where first two are NC, others are not defined


only order of dimensions “adbc” (0312)

Advanced syntax can be used for multi-character names like “[N,C,H,W,…,CustomName]”




-
bool operator==(const
[Layout](https://docs.openvino.ai/classov_1_1_layout.html#_CPPv4N2ov6LayoutE)&rhs) const Comparison operator (equal)


-
bool operator!=(const
[Layout](https://docs.openvino.ai/classov_1_1_layout.html#_CPPv4N2ov6LayoutE)&rhs) const Comparison operator (not equal)


-
bool has_name(const std::string &dimensionName) const
Checks if dimension with specified name is in layout.

- Returns:
`true`

if layout has information about dimension index with a given name


-
std::int64_t get_index_by_name(const std::string &dimensionName) const
Gets index of dimension with a specified name.

- Throws:
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AssertFailure](https://docs.openvino.ai/classov_1_1_assert_failure.html#_CPPv4N2ov13AssertFailureE)– if dimension name is not found in a layout- Returns:
Index of given dimension name



-
std::string to_string() const
String representation of

[Layout](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout).

-
inline bool empty() const
Returns ‘true’ if layout has no information, i.e. equals to

[Layout()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_layout_1a5f1c0a4db337e976786c1b24775541db)

Public Static Functions

-
static
[Layout](https://docs.openvino.ai/classov_1_1_layout.html#_CPPv4N2ov6LayoutE)scalar() Constructs layout representing scalar.