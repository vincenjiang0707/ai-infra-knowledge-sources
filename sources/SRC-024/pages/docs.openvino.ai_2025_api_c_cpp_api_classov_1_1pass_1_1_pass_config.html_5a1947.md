source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_pass_config.html
lastmod: 

# Class ov::pass::PassConfig[#](https://docs.openvino.ai#class-ov-pass-passconfig)

-
class PassConfig
[#](https://docs.openvino.ai#_CPPv4N2ov4pass10PassConfigE) Class representing a transformations config that is used for disabling/enabling transformations registered inside

[pass::Manager](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_manager)and also allows to set callback for all transformations or for particular transformation.When

[pass::Manager](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_manager)is created all passes registered inside this manager including nested passes will share the same instance of[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)class. To work with this class first you need to get shared instance of this class by calling manager.get_pass_config() method. Then you will be able to disable/enable passes based on transformations type_info. For example:Sometimes it is needed to call transformation inside other transformation manually. And for that case before running transformation you need manually check that this pass is not disabled and then you need to set currentpass::Manager manager; manager.register_pass<CommonOptimizations>(); auto pass_config = manager.get_pass_config(); pass_config->disable<ConvertGELU>(); // this will disable nested pass inside // CommonOptimizations pipeline manager.run_passes(f);

[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)instance to this transformation. For example:Following this logic inside your transformations you will guaranty that transformations will be executed in a right way.// Inside MatcherPass callback or inside FunctionPass run_on_function() method // you need to call get_pass_config() method to get shared instance of PassConfig auto pass_config = get_pass_config(); // Before running nested transformation you need to check is it disabled or not if (!pass_config->is_disabled<ConvertGELU>()) { auto pass = ConvertGELU(); pass->set_pass_config(pass_config); pass.apply(node); }

Public Functions

-
PassConfig()
[#](https://docs.openvino.ai#_CPPv4N2ov4pass10PassConfig10PassConfigEv) Default constructor.


-
void disable(const
[DiscreteTypeInfo](https://docs.openvino.ai/structov_1_1_discrete_type_info.html#_CPPv4N2ov16DiscreteTypeInfoE)&type_info)[#](https://docs.openvino.ai#_CPPv4N2ov4pass10PassConfig7disableERK16DiscreteTypeInfo) Disable transformation by its type_info.

- Parameters:
**type_info**– Transformation type_info


-
template<class T>

inline void disable()[#](https://docs.openvino.ai#_CPPv4I0EN2ov4pass10PassConfig7disableEvv) Disable transformation by its class type (based on type_info)


-
void enable(const
[DiscreteTypeInfo](https://docs.openvino.ai/structov_1_1_discrete_type_info.html#_CPPv4N2ov16DiscreteTypeInfoE)&type_info)[#](https://docs.openvino.ai#_CPPv4N2ov4pass10PassConfig6enableERK16DiscreteTypeInfo) Enable transformation by its type_info.

- Parameters:
**type_info**– Transformation type_info


-
template<class T>

inline void enable()[#](https://docs.openvino.ai#_CPPv4I0EN2ov4pass10PassConfig6enableEvv) Enable transformation by its class type (based on type_info)


-
inline void set_callback(const
[param_callback](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass14param_callbackE)&callback)[#](https://docs.openvino.ai#_CPPv4N2ov4pass10PassConfig12set_callbackERK14param_callback) Set callback for all kind of transformations.


-
template<typename T, class ...Args>

inline void set_callback(const[param_callback](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass14param_callbackE)&callback)[#](https://docs.openvino.ai#_CPPv4I0DpEN2ov4pass10PassConfig12set_callbackEvRK14param_callback) Set callback for particular transformation class types.

Example below show how to set callback for one or multiple passes using this method.

Note that inside transformations you must provide code that work with this callback. See example below:pass_config->set_callback<ov::pass::ConvertBatchToSpace, ov::pass::ConvertSpaceToBatch>( [](const_node_ptr &node) -> bool { // Disable transformations for cases when input shape rank is not equal to 4 const auto input_shape_rank = node->get_output_partial_shape(0).rank().get_length(); if (input_shape_rank != 4) { return false; } return true; });

if (transformation_callback(node)) { return false; // exit from transformation }


-
[param_callback](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass14param_callbackE)get_callback(const[DiscreteTypeInfo](https://docs.openvino.ai/structov_1_1_discrete_type_info.html#_CPPv4N2ov16DiscreteTypeInfoE)&type_info) const[#](https://docs.openvino.ai#_CPPv4NK2ov4pass10PassConfig12get_callbackERK16DiscreteTypeInfo) Get callback for given transformation type_info.

In case if callback wasn’t set for given transformation type then global callback will be returned. But if even global callback wasn’t set then default callback will be returned.

- Parameters:
**type_info**– Transformation type_info


-
template<class T>

inline[param_callback](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass14param_callbackE)get_callback() const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov4pass10PassConfig12get_callbackE14param_callbackv) Get callback for given transformation class type.

- Returns:
callback lambda function



-
inline bool is_disabled(const
[DiscreteTypeInfo](https://docs.openvino.ai/structov_1_1_discrete_type_info.html#_CPPv4N2ov16DiscreteTypeInfoE)&type_info) const[#](https://docs.openvino.ai#_CPPv4NK2ov4pass10PassConfig11is_disabledERK16DiscreteTypeInfo) Check either transformation type is disabled or not.

- Parameters:
**type_info**– Transformation type_info- Returns:
true if transformation type was disabled and false otherwise



-
template<class T>

inline bool is_disabled() const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov4pass10PassConfig11is_disabledEbv) Check either transformation class type is disabled or not.

- Returns:
true if transformation type was disabled and false otherwise



-
inline bool is_enabled(const
[DiscreteTypeInfo](https://docs.openvino.ai/structov_1_1_discrete_type_info.html#_CPPv4N2ov16DiscreteTypeInfoE)&type_info) const[#](https://docs.openvino.ai#_CPPv4NK2ov4pass10PassConfig10is_enabledERK16DiscreteTypeInfo) Check either transformation type is force enabled or not.

- Parameters:
**type_info**– Transformation type_info- Returns:
true if transformation type was force enabled and false otherwise



-
template<class T>

inline bool is_enabled() const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov4pass10PassConfig10is_enabledEbv) Check either transformation class type is force enabled or not.

- Returns:
true if transformation type was force enabled and false otherwise



-
PassConfig()