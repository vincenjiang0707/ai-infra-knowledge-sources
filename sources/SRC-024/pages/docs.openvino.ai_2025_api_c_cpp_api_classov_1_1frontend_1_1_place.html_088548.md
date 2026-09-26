source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_place.html
lastmod: 

# Class ov::frontend::Place[#](https://docs.openvino.ai#class-ov-frontend-place)

-
class Place
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend5PlaceE) An interface for identifying a place in a graph and iterate over it; can refer to an operation node, tensor, port etc.

[Place](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_place)can refer to[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor),[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)Edge,[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)Port, Operation,[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)Port,[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)Edge[Tensor A] | | [Input Edge] | V ------------------- [ [Input Port 0] ] [ ] [ Operation A ] [ ] [ [Output Port 0] ] ------------------- | | [Output Edge] | V [Tensor B] | | [Input Edge] | V ------------------- [ [Input Port 0] ] [ ] [ Operation B ] [ ] [ [Output Port 0] ] ------------------- | | [Output Edge] | V [Tensor C]

Note

Each front end implementation provides specialization of this interface to represent a place in a model graph. Various methods in the front end classes accept and retrieve instances of

[Place](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_place)to point to particular node part which should be modified or satisfies some criteria. For example, this class is used to report model inputs and outputs, for searching operations and tensors by name, for setting shape etc.Public Functions

-
virtual std::vector<std::string> get_names() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place9get_namesEv) All associated names (synonyms) that identify this place in the graph in a framework specific way.

- Returns:
A vector of strings each representing a name that identifies this place in the graph. Can be empty if there are no names associated with this place or name cannot be attached.



-
virtual std::vector<Ptr> get_consuming_operations() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place24get_consuming_operationsEv) Returns references to all operation nodes that consume data from this place.

Note

It can be called for any kind of graph place searching for the first consuming operations. It is optional if place has only one output port

- Returns:
A vector with all operation node references that consumes data from this place



-
virtual std::vector<Ptr> get_consuming_operations(int output_port_index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place24get_consuming_operationsEi) Returns references to all operation nodes that consume data from this place for specified output port.

Note

It can be called for any kind of graph place searching for the first consuming operations.

- Parameters:
**output_port_index**– If place is an operational node it specifies which output port should be considered.- Returns:
A vector with all operation node references that consumes data from this place



-
virtual std::vector<Ptr> get_consuming_operations(const std::string &outputName) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place24get_consuming_operationsERKNSt6stringE) Returns references to all operation nodes that consume data from this place for specified output port.

Note

It can be called for any kind of graph place searching for the first consuming operations.

- Parameters:
**outputName**– If a given place is itself an operation node, this specifies name of output port group- Returns:
A vector with all operation node references that consumes data from this place



-
virtual std::vector<Ptr> get_consuming_operations(const std::string &outputName, int outputPortIndex) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place24get_consuming_operationsERKNSt6stringEi) Returns references to all operation nodes that consume data from this place for specified output port.

Note

It can be called for any kind of graph place searching for the first consuming operations.

- Parameters:
**outputName**– If a given place is itself an operation node, this specifies name of output port group, each group can have multiple ports**outputPortIndex**– If place is an operational node it specifies which output port should be considered.

- Returns:
A vector with all operation node references that consumes data from this place



-
virtual Ptr get_target_tensor() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place17get_target_tensorEv) Returns a tensor place that gets data from this place; applicable for operations, output ports and output edges which have only one output port.

- Returns:
A tensor place which hold the resulting value for this place



-
virtual Ptr get_target_tensor(const std::string &outputName) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place17get_target_tensorERKNSt6stringE) Returns a tensor place that gets data from this place; applicable for operations.

- Parameters:
**outputName**– Name of output port group- Returns:
A tensor place which hold the resulting value for this place



-
virtual Ptr get_target_tensor(const std::string &outputName, int outputPortIndex) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place17get_target_tensorERKNSt6stringEi) Returns a tensor place that gets data from this place; applicable for operations.

- Parameters:
**outputName**– Name of output port group, each group can have multiple ports**outputPortIndex**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)port index if the current place is an operation node and has multiple output ports

- Returns:
A tensor place which hold the resulting value for this place



-
virtual Ptr get_target_tensor(int output_port_index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place17get_target_tensorEi) Returns a tensor place that gets data from this place; applicable for operations.

- Parameters:
**output_port_index**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)port index if the current place is an operation node and has multiple output ports- Returns:
A tensor place which hold the resulting value for this place



-
virtual Ptr get_source_tensor() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place17get_source_tensorEv) Returns a tensor place that supplies data for this place; applicable for operations, input ports and input edges which have only one input port.

- Returns:
A tensor place which supplies data for this place



-
virtual Ptr get_source_tensor(int input_port_index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place17get_source_tensorEi) Returns a tensor place that supplies data for this place; applicable for operations.

- Parameters:
**input_port_index**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)port index for operational nodes.- Returns:
A tensor place which supplies data for this place



-
virtual Ptr get_source_tensor(const std::string &inputName) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place17get_source_tensorERKNSt6stringE) Returns a tensor place that supplies data for this place; applicable for operations.

- Parameters:
**inputName**– Name of input port group- Returns:
A tensor place which supplies data for this place



-
virtual Ptr get_source_tensor(const std::string &inputName, int inputPortIndex) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place17get_source_tensorERKNSt6stringEi) Returns a tensor place that supplies data for this place; applicable for operations.

- Parameters:
**inputName**– If a given place is itself an operation node, this specifies name of output port group, each group can have multiple ports**inputPortIndex**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)port index for operational nodes.

- Returns:
A tensor place which supplies data for this place



-
virtual Ptr get_producing_operation() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place23get_producing_operationEv) Get an operation node place that immediately produces data for this place; applicable if place has only one input port.

- Returns:
An operation place that produces data for this place



-
virtual Ptr get_producing_operation(int input_port_index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place23get_producing_operationEi) Get an operation node place that immediately produces data for this place.

- Parameters:
**input_port_index**– If a given place is itself an operation node, this specifies a port index- Returns:
An operation place that produces data for this place



-
virtual Ptr get_producing_operation(const std::string &inputName) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place23get_producing_operationERKNSt6stringE) Get an operation node place that immediately produces data for this place.

- Parameters:
**inputName**– If a given place is itself an operation node, this specifies name of output port group- Returns:
An operation place that produces data for this place



-
virtual Ptr get_producing_operation(const std::string &inputName, int inputPortIndex) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place23get_producing_operationERKNSt6stringEi) Get an operation node place that immediately produces data for this place.

- Parameters:
**inputName**– If a given place is itself an operation node, this specifies name of output port group, each group can have multiple ports**inputPortIndex**– If a given place is itself an operation node, this specifies a port index

- Returns:
An operation place that produces data for this place



-
virtual Ptr get_producing_port() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place18get_producing_portEv) Returns a port that produces data for this place.


-
virtual Ptr get_input_port() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place14get_input_portEv) For operation node returns reference to an input port; applicable if operation node has only one input port.

- Returns:
[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)port place or nullptr if not exists


-
virtual Ptr get_input_port(int input_port_index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place14get_input_portEi) For operation node returns reference to an input port with specified index.

- Parameters:
**input_port_index**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)port index- Returns:
Appropriate input port place or nullptr if not exists



-
virtual Ptr get_input_port(const std::string &input_name) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place14get_input_portERKNSt6stringE) For operation node returns reference to an input port with specified name; applicable if port group has only one input port.

- Parameters:
**input_name**– Name of port group- Returns:
Appropriate input port place or nullptr if not exists



-
virtual Ptr get_input_port(const std::string &input_name, int input_port_index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place14get_input_portERKNSt6stringEi) For operation node returns reference to an input port with specified name and index.

- Parameters:
**input_name**– Name of port group, each group can have multiple ports**input_port_index**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)port index in a group

- Returns:
Appropriate input port place or nullptr if not exists



-
virtual Ptr get_output_port() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place15get_output_portEv) For operation node returns reference to an output port; applicable for operations with only one output port.

- Returns:
Appropriate output port place or nullptr if not exists



-
virtual Ptr get_output_port(int output_port_index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place15get_output_portEi) For operation node returns reference to an output port with specified index.

- Parameters:
**output_port_index**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)port index- Returns:
Appropriate output port place or nullptr if not exists



-
virtual Ptr get_output_port(const std::string &output_name) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place15get_output_portERKNSt6stringE) For operation node returns reference to an output port with specified name; applicable if port group has only one output port.

- Parameters:
**output_name**– Name of output port group- Returns:
Appropriate output port place or nullptr if not exists



-
virtual Ptr get_output_port(const std::string &output_name, int output_port_index) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place15get_output_portERKNSt6stringEi) For operation node returns reference to an output port with specified name and index.

- Parameters:
**output_name**– Name of output port group, each group can have multiple ports**output_port_index**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)port index

- Returns:
Appropriate output port place or nullptr if not exists



-
virtual std::vector<
[Place](https://docs.openvino.ai#_CPPv4N2ov8frontend5PlaceE)::Ptr> get_consuming_ports() const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place19get_consuming_portsEv) Returns all input ports that consume data flows through this place.


-
virtual bool is_input() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place8is_inputEv) Returns true if this place is input for a model.


-
virtual bool is_output() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place9is_outputEv) Returns true if this place is output for a model.


-
virtual bool is_equal(const Ptr &another) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place8is_equalERK3Ptr) Returns true if another place is the same as this place.

- Parameters:
**another**– Another place object


-
virtual bool is_equal_data(const Ptr &another) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend5Place13is_equal_dataERK3Ptr) Returns true if another place points to the same data.

Note

The same data means all places on path: output port -> output edge -> tensor -> input edge -> input port.

- Parameters:
**another**– Another place object


-
virtual std::vector<std::string> get_names() const