source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_progress_reporter_extension.html
lastmod: 

# Class ov::frontend::ProgressReporterExtension[#](https://docs.openvino.ai#class-ov-frontend-progressreporterextension)

-
class ProgressReporterExtension : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Extension](https://docs.openvino.ai/classov_1_1_extension.html#_CPPv4N2ov9ExtensionE)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend25ProgressReporterExtensionE) Public Types

-
using progress_notifier_callback = std::function<void(float, unsigned int, unsigned int)>
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend25ProgressReporterExtension26progress_notifier_callbackE) A progress reporting callback signature. A FunctionObject that matches this signature should be passed to the constructor of this extension. The extension will then invoke this as a callback each time the progress needs to be reported. The callback itself is responsible for consuming the reported values.

- Param progress:
A float value in the range [0.0, 1.0] indicating the total progress of an operation.

- Param total_steps:
The total number of steps that a given instance of this extension is tracking

- Param completed_completed:
The current number of completed steps (out of the total number of steps to take)



Public Functions

-
inline ProgressReporterExtension()
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend25ProgressReporterExtension25ProgressReporterExtensionEv) The default constructor which creates a reporter that doesn’t report progress.


-
void report_progress(float progress, unsigned int total_steps, unsigned int completed_steps) const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend25ProgressReporterExtension15report_progressEfjj) The main method of this extension used to report the progress. This method forwards its arguments to the callback stored in this class.

- Parameters:
**progress**– A float value in the range [0.0, 1.0] indicating the total progress of an operation.**total_steps**– The total number of steps that a given instance of this extension is tracking**completed_steps**– The current number of completed steps (out of the total number of steps to take)



-
using progress_notifier_callback = std::function<void(float, unsigned int, unsigned int)>