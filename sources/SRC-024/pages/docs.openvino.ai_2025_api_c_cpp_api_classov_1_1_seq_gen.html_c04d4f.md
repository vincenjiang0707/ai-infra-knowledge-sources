source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_seq_gen.html
lastmod: 

# Class ov::SeqGen[#](https://docs.openvino.ai#class-ov-seqgen)

-
template<class T, Direction D = Direction::FORWARD>

class SeqGen[#](https://docs.openvino.ai#_CPPv4I0_9DirectionEN2ov6SeqGenE) Infinite generator of sequence increasing values.

Start value can be specified.

- Template Parameters:
**T**– Type of sequence values (must support`++`

or ‘—’ operators).