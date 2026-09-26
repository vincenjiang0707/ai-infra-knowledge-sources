source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_l_s_t_m_states_broadcast.html
lastmod: 

Class ov::pass::LSTMStatesBroadcast# class LSTMStatesBroadcast : public ov::pass::ModelPass# In case LSTMCell has constant initial hidden and cell state with single batch size we make them broadcast-able by batch.