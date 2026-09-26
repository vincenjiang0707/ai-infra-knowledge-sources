source: https://docs.mthreads.com/sglang-musa-m1000/version-20260830/sglang-musa-m1000-doc-online/faq

# 常见问题（FAQ）

## 如何确认 SGLang 是否安装成功[](https://docs.mthreads.com#如何确认-sglang-是否安装成功)

执行以下命令：

`pip list | grep sglang`



如果输出中包含 `sglang`

和 `sglang-kernel`

，说明相关 Python 包已经安装到当前环境。

## 编译 SGLang 后 Torch 相关包被刷新怎么办[](https://docs.mthreads.com#编译-sglang-后-torch-相关包被刷新怎么办)

SGLang Python 包编译过程中可能会刷新 Torch 相关包。请重新安装发布包中指定版本的依赖：

`pip install torch-2.9.0-cp310-cp310-linux_aarch64.whl`

pip install torch_musa-2.9.0-cp310-cp310-linux_aarch64.whl

pip install torchvision-0.22.1+e98278b-cp310-cp310-linux_aarch64.whl

pip install torchaudio-2.9.0+eaa9e4e-cp310-cp310-linux_aarch64.whl

pip install triton-3.2.0-cp310-cp310-linux_aarch64.whl



## 如何查看 MUSA 环境是否正常[](https://docs.mthreads.com#如何查看-musa-环境是否正常)

执行 `musaInfo`

，正常输出设备信息即表示 MUSA 环境可用。

如果提示找不到命令，执行：

`export PATH=/usr/local/musa/bin:${PATH}`

export LD_LIBRARY_PATH=/usr/local/musa/lib:${LD_LIBRARY_PATH}

musaInfo



如果加了 PATH 后仍然找不到 `musaInfo`

，说明 MUSA SDK 可能未正确安装，需要重新安装 MUSA SDK。

## 如何验证 Torch MUSA 是否可用[](https://docs.mthreads.com#如何验证-torch-musa-是否可用)

`python3 -c "import torch;import torch_musa;print(torch.musa.is_available())"`



输出 `true`

表示 Torch MUSA 环境可用。

## 启动时提示 CXXABI_1.3.15 not found 怎么办[](https://docs.mthreads.com#启动时提示-cxxabi_1315-not-found-怎么办)

如果启动服务时出现如下报错：

`ImportError: /usr/lib/aarch64-linux-gnu/libstdc++.so.6: version `CXXABI_1.3.15' not found`



可以在启动命令前将当前 Conda 环境的库路径加入 `LD_LIBRARY_PATH`

：

`export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH`



该报错通常是因为系统默认加载了 `/usr/lib/aarch64-linux-gnu/libstdc++.so.6`

，但该版本不包含运行时依赖所需的 `CXXABI_1.3.15`

。将 `$CONDA_PREFIX/lib`

放到 `LD_LIBRARY_PATH`

最前面之后，程序会优先使用当前 Conda 环境中的 `libstdc++.so.6`

，从而避免因系统库版本较低导致的导入失败。

## 服务启动后如何确认接口可用[](https://docs.mthreads.com#服务启动后如何确认接口可用)

执行：

`curl http://127.0.0.1:30000/v1/models`



如果可以返回模型列表，说明服务已经正常启动并暴露 OpenAI 兼容接口。

## OOM (Out of Memory)[](https://docs.mthreads.com#oom-out-of-memory)

-
如果 SGLang 启动时发生 OOM，可以尝试增加

`--mem-fraction-static`

，或更换更小的模型后重新启动服务。 -
尝试清除缓存


`sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"`