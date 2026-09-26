source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_low_latency2.html
lastmod: 

# Class ov::pass::LowLatency2[#](https://docs.openvino.ai#class-ov-pass-lowlatency2)

-
class LowLatency2 : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass11LowLatency2E) The transformation finds all TensorIterator/Loop layers in the network, processes all back edges that describe a connection between Result and Parameter of the TensorIterator/Loop bodies,and inserts ReadValue and Assign layers at the input and output corresponding to this back edge. Supported platform: CPU.

The example below describes the changes made by the transformation [] - TensorIterator body () - new layer BE - back-edge

before applying the transformation: -> input1[BE_1 -> Parameter -> Layers … -> Result -> BE_1 ]output1->

after applying the transformation: ->(ReadValue)-> input1[BE_1 ->Parameter->Layers …->Result->BE_1]output1 ->(Assign) \ ->… After applying the transformation, the resulting network can be inferred step by step, the states will store between inferences.