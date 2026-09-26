# [Issue #64] libtorch_npu和opencv一块使用报错

source: https://github.com/Ascend/pytorch/issues/64
state: open | updated: 2025-07-04T01:30:48Z
labels: 

## 正文

### **使用opencv读取视频和图像数据，用libtorch和libtorch_npu进行推理，报错。但是单独使用opencv没有任何问题，证明不是opencv的问题。并且使用libtorch和opencv在别的板子上也没有任何问题。最终推断只能是libtorch_npu的问题了。完整的报错信息如下:**

```
/usr/bin/cmake -S/home/HwHiAiUser/Macro/CProject/SPSG -B/home/HwHiAiUser/Macro/CProject/SPSG/build --check-build-system CMakeFiles/Makefile.cmake 0
/usr/bin/cmake -E cmake_progress_start /home/HwHiAiUser/Macro/CProject/SPSG/build/CMakeFiles /home/HwHiAiUser/Macro/CProject/SPSG/build//CMakeFiles/progress.marks
make  -f CMakeFiles/Makefile2 all
make[1]: Entering directory '/home/HwHiAiUser/Macro/CProject/SPSG/build'
make  -f CMakeFiles/spsg_lib.dir/build.make CMakeFiles/spsg_lib.dir/depend
make[2]: Entering directory '/home/HwHiAiUser/Macro/CProject/SPSG/build'
cd /home/HwHiAiUser/Macro/CProject/SPSG/build && /usr/bin/cmake -E cmake_depends "Unix Makefiles" /home/HwHiAiUser/Macro/CProject/SPSG /home/HwHiAiUser/Macro/CProject/SPSG /home/HwHiAiUser/Macro/CProject/SPSG/build /home/HwHiAiUser/Macro/CProject/SPSG/build /home/HwHiAiUser/Macro/CProject/SPSG/build/CMakeFiles/spsg_lib.dir/DependInfo.cmake --color=
make[2]: Leaving directory '/home/HwHiAiUser/Macro/CProject/SPSG/build'
make  -f CMakeFiles/spsg_lib.dir/build.make CMakeFiles/spsg_lib.dir/build
make[2]: Entering directory '/home/HwHiAiUser/Macro/CProject/SPSG/build'
[ 20%] Building CXX object CMakeFiles/spsg_lib.dir/src/SuperGlue.cpp.o
/usr/bin/c++ -DENABLE_GPU=1 -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -Dspsg_lib_EXPORTS -I/home/HwHiAiUser/Macro/pytorch/libtorch_npu/include -I/home/HwHiAiUser/Macro/CProject/SPSG -I/home/HwHiAiUser/Macro/CProject/SPSG/include -isystem /home/HwHiAiUser/Macro/opencv/build/install/include/opencv4 -isystem /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/include -isystem /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/include/torch/csrc/api/include -D_GLIBCXX_USE_CXX11_ABI=0 -O3 -g -fPIC -DENABLE_DEBUG=1 -D_GLIBCXX_USE_CXX11_ABI=0 -MD -MT CMakeFiles/spsg_lib.dir/src/SuperGlue.cpp.o -MF CMakeFiles/spsg_lib.dir/src/SuperGlue.cpp.o.d -o CMakeFiles/spsg_lib.dir/src/SuperGlue.cpp.o -c /home/HwHiAiUser/Macro/CProject/SPSG/src/SuperGlue.cpp
[ 40%] Building CXX object CMakeFiles/spsg_lib.dir/src/SuperPoint.cpp.o
/usr/bin/c++ -DENABLE_GPU=1 -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -Dspsg_lib_EXPORTS -I/home/HwHiAiUser/Macro/pytorch/libtorch_npu/include -I/home/HwHiAiUser/Macro/CProject/SPSG -I/home/HwHiAiUser/Macro/CProject/SPSG/include -isystem /home/HwHiAiUser/Macro/opencv/build/install/include/opencv4 -isystem /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/include -isystem /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/include/torch/csrc/api/include -D_GLIBCXX_USE_CXX11_ABI=0 -O3 -g -fPIC -DENABLE_DEBUG=1 -D_GLIBCXX_USE_CXX11_ABI=0 -MD -MT CMakeFiles/spsg_lib.dir/src/SuperPoint.cpp.o -MF CMakeFiles/spsg_lib.dir/src/SuperPoint.cpp.o.d -o CMakeFiles/spsg_lib.dir/src/SuperPoint.cpp.o -c /home/HwHiAiUser/Macro/CProject/SPSG/src/SuperPoint.cpp
[ 60%] Linking CXX shared library ../lib/libspsg_lib.so
/usr/bin/cmake -E cmake_link_script CMakeFiles/spsg_lib.dir/link.txt --verbose=1
/usr/bin/c++ -fPIC  -D_GLIBCXX_USE_CXX11_ABI=0 -O3 -g -shared -Wl,-soname,libspsg_lib.so -o ../lib/libspsg_lib.so CMakeFiles/spsg_lib.dir/src/SuperGlue.cpp.o CMakeFiles/spsg_lib.dir/src/SuperPoint.cpp.o   -L/home/HwHiAiUser/.local/lib/python3.9/site-packages/torch.libs  -L/home/HwHiAiUser/Macro/opencv/build/install/lib  -Wl,-rpath,/home/HwHiAiUser/.local/lib/python3.9/site-packages/torch.libs:/home/HwHiAiUser/Macro/opencv/build/install/lib:/home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib:/home/HwHiAiUser/Macro/pytorch/libtorch_npu/lib /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_gapi.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_highgui.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_ml.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_objdetect.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_photo.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_stitching.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_video.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_videoio.so.4.12.0 /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libtorch.so /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libc10.so /home/HwHiAiUser/Macro/pytorch/libtorch_npu/lib/libtorch_npu.so /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_imgcodecs.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_dnn.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_calib3d.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_features2d.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_flann.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_imgproc.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_core.so.4.12.0 -Wl,--no-as-needed,"/home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libtorch_cpu.so" -Wl,--as-needed /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libc10.so -Wl,--no-as-needed,"/home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libtorch.so" -Wl,--as-needed 
make[2]: Leaving directory '/home/HwHiAiUser/Macro/CProject/SPSG/build'
[ 60%] Built target spsg_lib
make  -f CMakeFiles/test_npu.dir/build.make CMakeFiles/test_npu.dir/depend
make[2]: Entering directory '/home/HwHiAiUser/Macro/CProject/SPSG/build'
cd /home/HwHiAiUser/Macro/CProject/SPSG/build && /usr/bin/cmake -E cmake_depends "Unix Makefiles" /home/HwHiAiUser/Macro/CProject/SPSG /home/HwHiAiUser/Macro/CProject/SPSG /home/HwHiAiUser/Macro/CProject/SPSG/build /home/HwHiAiUser/Macro/CProject/SPSG/build /home/HwHiAiUser/Macro/CProject/SPSG/build/CMakeFiles/test_npu.dir/DependInfo.cmake --color=
make[2]: Leaving directory '/home/HwHiAiUser/Macro/CProject/SPSG/build'
make  -f CMakeFiles/test_npu.dir/build.make CMakeFiles/test_npu.dir/build
make[2]: Entering directory '/home/HwHiAiUser/Macro/CProject/SPSG/build'
[ 80%] Building CXX object CMakeFiles/test_npu.dir/spsg.cpp.o
/usr/bin/c++ -DENABLE_GPU=1 -DUSE_C10D_GLOO -DUSE_DISTRIBUTED -DUSE_RPC -DUSE_TENSORPIPE -I/home/HwHiAiUser/Macro/pytorch/libtorch_npu/include -I/home/HwHiAiUser/Macro/CProject/SPSG -I/home/HwHiAiUser/Macro/CProject/SPSG/include -isystem /home/HwHiAiUser/Macro/opencv/build/install/include/opencv4 -isystem /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/include -isystem /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/include/torch/csrc/api/include -D_GLIBCXX_USE_CXX11_ABI=0 -O3 -g -DENABLE_DEBUG=1 -D_GLIBCXX_USE_CXX11_ABI=0 -MD -MT CMakeFiles/test_npu.dir/spsg.cpp.o -MF CMakeFiles/test_npu.dir/spsg.cpp.o.d -o CMakeFiles/test_npu.dir/spsg.cpp.o -c /home/HwHiAiUser/Macro/CProject/SPSG/spsg.cpp
/home/HwHiAiUser/Macro/CProject/SPSG/spsg.cpp: In function ‘int main(int, char**)’:
/home/HwHiAiUser/Macro/CProject/SPSG/spsg.cpp:59:15: warning: ISO C++ forbids converting a string constant to ‘char*’ [-Wwrite-strings]
   59 |     argv[1] = "../models/superpoint_model.pt";
      |               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/HwHiAiUser/Macro/CProject/SPSG/spsg.cpp:60:15: warning: ISO C++ forbids converting a string constant to ‘char*’ [-Wwrite-strings]
   60 |     argv[2] = "../models/superglue_model.pt";
      |               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/home/HwHiAiUser/Macro/CProject/SPSG/spsg.cpp:61:15: warning: ISO C++ forbids converting a string constant to ‘char*’ [-Wwrite-strings]
   61 |     argv[3] = "../images/map.jpg";
      |               ^~~~~~~~~~~~~~~~~~~
/home/HwHiAiUser/Macro/CProject/SPSG/spsg.cpp:62:15: warning: ISO C++ forbids converting a string constant to ‘char*’ [-Wwrite-strings]
   62 |     argv[4] = "../images/005_DBC_20200922_P4R_10HZ.MP4";
      |               ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
[100%] Linking CXX executable ../bin/test_npu
/usr/bin/cmake -E cmake_link_script CMakeFiles/test_npu.dir/link.txt --verbose=1
/usr/bin/c++  -D_GLIBCXX_USE_CXX11_ABI=0 -O3 -g CMakeFiles/test_npu.dir/spsg.cpp.o -o ../bin/test_npu   -L/home/HwHiAiUser/.local/lib/python3.9/site-packages/torch.libs  -L/home/HwHiAiUser/Macro/opencv/build/install/lib  -Wl,-rpath,/home/HwHiAiUser/.local/lib/python3.9/site-packages/torch.libs:/home/HwHiAiUser/Macro/opencv/build/install/lib:/home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib:/home/HwHiAiUser/Macro/pytorch/libtorch_npu/lib:/home/HwHiAiUser/Macro/CProject/SPSG/lib /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libc10.so /home/HwHiAiUser/Macro/pytorch/libtorch_npu/lib/libtorch_npu.so ../lib/libspsg_lib.so /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_gapi.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_highgui.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_ml.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_objdetect.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_photo.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_stitching.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_video.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_calib3d.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_dnn.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_features2d.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_flann.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_videoio.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_imgcodecs.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_imgproc.so.4.12.0 /home/HwHiAiUser/Macro/opencv/build/install/lib/libopencv_core.so.4.12.0 /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libtorch.so -Wl,--no-as-needed,"/home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libtorch_cpu.so" -Wl,--as-needed /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libc10.so -Wl,--no-as-needed,"/home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libtorch.so" -Wl,--as-needed /home/HwHiAiUser/.local/lib/python3.9/site-packages/torch/lib/libc10.so /home/HwHiAiUser/Macro/pytorch/libtorch_npu/lib/libtorch_npu.so 
/usr/bin/ld: CMakeFiles/test_npu.dir/spsg.cpp.o: in function `cv::Mat::elemSize() const':
/home/HwHiAiUser/Macro/opencv/build/install/include/opencv4/opencv2/core/mat.inl.hpp:670: undefined reference to `cv::error(int, std::string const&, char const*, char const*, int)'
/usr/bin/ld: CMakeFiles/test_npu.dir/spsg.cpp.o: in function `cv::MatConstIterator::MatConstIterator(cv::Mat const*)':
/home/HwHiAiUser/Macro/opencv/build/install/include/opencv4/opencv2/core/mat.inl.hpp:2277: undefined reference to `cv::error(int, std::string const&, char const*, char const*, int)'
/usr/bin/ld: CMakeFiles/test_npu.dir/spsg.cpp.o: in function `cv::MatCommaInitializer_<float>& cv::MatCommaInitializer_<float>::operator,<double>(double)':
/home/HwHiAiUser/Macro/opencv/build/install/include/opencv4/opencv2/core/mat.inl.hpp:2982: undefined reference to `cv::error(int, std::string const&, char const*, char const*, int)'
/usr/bin/ld: CMakeFiles/test_npu.dir/spsg.cpp.o: in function `cv::Mat::elemSize() const':
/home/HwHiAiUser/Macro/opencv/build/install/include/opencv4/opencv2/core/mat.inl.hpp:670: undefined reference to `cv::error(int, std::string const&, char const*, char const*, int)'
/usr/bin/ld: CMakeFiles/test_npu.dir/spsg.cpp.o: in function `cv::MatConstIterator_<float> cv::Mat::end<float>() const':
/home/HwHiAiUser/Macro/opencv/build/install/include/opencv4/opencv2/core/mat.inl.hpp:1034: undefined reference to `cv::error(int, std::string const&, char const*, char const*, int)'
/usr/bin/ld: CMakeFiles/test_npu.dir/spsg.cpp.o:/home/HwHiAiUser/Macro/opencv/build/install/include/opencv4/opencv2/core/mat.inl.hpp:2277: more undefined references to `cv::error(int, std::string const&, char const*, char const*, int)' follow
/usr/bin/ld: CMakeFiles/test_npu.dir/spsg.cpp.o: in function `main':
/home/HwHiAiUser/Macro/CProject/SPSG/spsg.cpp:89: undefined reference to `cv::imread(std::string const&, int)'
/usr/bin/ld: /home/HwHiAiUser/Macro/CProject/SPSG/spsg.cpp:94: undefined reference to `cv::VideoCapture::VideoCapture(std::string const&, int)'
/usr/bin/ld: /home/HwHiAiUser/Macro/CProject/SPSG/spsg.cpp:143: undefined reference to `cv::imshow(std::string const&, cv::_InputArray const&)'
/usr/bin/ld: CMakeFiles/test_npu.dir/spsg.cpp.o: in function `cv::MatSize::operator()() const':
/home/HwHiAiUser/Macro/opencv/build/install/include/opencv4/opencv2/core/mat.inl.hpp:1198: undefined reference to `cv::error(int, std::string const&, char const*, char const*, int)'
/usr/bin/ld: /home/HwHiAiUser/Macro/opencv/build/install/include/opencv4/opencv2/core/mat.inl.hpp:1198: undefined reference to `cv::error(int, std::string const&, char const*, char const*, int)'
collect2: error: ld returned 1 exit status
make[2]: *** [CMakeFiles/test_npu.dir/build.make:122: ../bin/test_npu] Error 1
make[2]: Leaving directory '/home/HwHiAiUser/Macro/CProject/SPSG/build'
make[1]: *** [CMakeFiles/Makefile2:114: CMakeFiles/test_npu.dir/all] Error 2
make[1]: Leaving directory '/home/HwHiAiUser/Macro/CProject/SPSG/build'
make: *** [Makefile:94: all] Error 2
```


**尝试了很多方法，也尝试了定义-D_GLIBCXX_USE_CXX11_ABI=0重新编译opencv还是没用。我看这个pytorch里面给的libtorch_npu例子给的也很简单，就是单独使用libtorch_npu的，并没有结合opencv使用的例子，请问这个问题是不是libtorch_npu固有的？**

## 评论 (2)

### kalcohol · 2025-05-06

我不是华为的员工，只是恰好看到了你的问题；看起来是链接时少链接了 opencv 的库，cv::imshow 是 highgui.so cv::VideoCapture 似乎是 videoio.so
适当修改 cmake 试试吧
也可能是链接顺序不对，opencv 常有的问题；此时还可以试试用链接组：`-Wl,--start-group -lopencv_imgcodecs -lopencv_imgproc -lopencv_core -ldl -lm -lpthread -lrt -llibjpeg-turbo -llibwebp -llibpng -llibtiff -llibopenjp2 -lzlib -Wl,--end-group` 类似这种写法

### yunyiyun · 2025-07-04

这个问题大概率是ABI版本的问题，你不使用libtorch_npu仅仅使用libtorch应该也是会报错的；
如果要避免该报错，请使用abi=1的libtorch和配套的libtorch_npu或者咨询opencv是否支持abi=0
可参考
https://gitee.com/ascend/pytorch/issues/IBYU8A?from=project-issue&search_text=opencv
