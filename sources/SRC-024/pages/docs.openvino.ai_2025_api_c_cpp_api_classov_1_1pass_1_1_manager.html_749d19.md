source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_manager.html
lastmod: 

# Class ov::pass::Manager[#](https://docs.openvino.ai#class-ov-pass-manager)

-
class Manager
[#](https://docs.openvino.ai#_CPPv4N2ov4pass7ManagerE) [Manager](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_manager)class allows to manage transformation passes.Public Functions

-
explicit Manager(const
[PassConfig](https://docs.openvino.ai/classov_1_1pass_1_1_pass_config.html#_CPPv4N2ov4pass10PassConfigE)&pass_config, std::string name = "UnnamedManager")[#](https://docs.openvino.ai#_CPPv4N2ov4pass7Manager7ManagerERK10PassConfigNSt6stringE) Construct

[Manager](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_manager)with a copied[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)instance; it will not share[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)as in the constructor above.

Register given transformation class type to execution list Example below show the basic usage of

[pass::Manager](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_manager).For some purposes transformation can be registered and disabled by default.pass::Manager manager; manager.register_pass<MyTransformation>(/* transformation constructor args *‍/); manager.run_passes(f);

manager.register_pass<MyTransformation, false>();

- Returns:
shared_ptr to the transformation instance



Runs registered transformations on a given model.

- Parameters:
**model**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)model- Returns:
Returns true if the model was changed by transformations, false otherwise.



-
void set_per_pass_validation(bool new_state)
[#](https://docs.openvino.ai#_CPPv4N2ov4pass7Manager23set_per_pass_validationEb) Set flag to enable/disable running

[Validate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_validate)pass after executing each registered pass.- Parameters:
**new_state**– Value “true” enables[Validate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_validate)pass run; “false”, otherwise


-
inline std::shared_ptr<
[PassConfig](https://docs.openvino.ai/classov_1_1pass_1_1_pass_config.html#_CPPv4N2ov4pass10PassConfigE)> get_pass_config()[#](https://docs.openvino.ai#_CPPv4N2ov4pass7Manager15get_pass_configEv) - Returns:
[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)shared object. This object is used for transformations pipeline configuration. This object allows to disable/enable transformations execution, set callback to particular transformation. For more details see[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)class.


-
explicit Manager(const