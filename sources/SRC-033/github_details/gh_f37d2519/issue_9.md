# [Issue #9] dynamic_batch处理的时间问题

source: https://github.com/Ascend/samples/issues/9
state: closed | updated: 2022-12-23T08:57:35Z
labels: 

## 正文

我在参考\python\level2_simple_inference\1_classification\googlenet_imagenet_dynamic_batch样例进行动态batch输入测试时发现，假设batch为1，8，16，无论我选择哪个batch，forward的时间都是差不多平均15ms左右一张图（例如耗时=15ms*batch的输入图片数量），好像batch是串行处理并不是并行处理，处理采用的是_execute_with_dynamic_batch_size这个算子，请问动态batch输入是选择这个算子还是其他算子呢，batch处理是并行还是串行呢？
![image](https://user-images.githubusercontent.com/109121546/208339064-c3dc1ec0-8750-4a3d-8d99-8f39e20da29f.png)
![image](https://user-images.githubusercontent.com/109121546/208339168-8ab91c9f-b9b8-47b4-b426-7436b238ac0e.png)
![image](https://user-images.githubusercontent.com/109121546/208339190-b1e3fb8f-4319-4ba4-809c-6ba80a4e9ea1.png)


## 评论 (7)

### ascendhuawei · 2022-12-19

Hi, 
Batch model inference is kind of 'parallel processing'. So, you should be able to see benefit of using multiple-batch.
As I tested, for this example, the inference time of batch 1, 2, 4, 8 are actually very close on Ascend910, i.e., increasing batch size does not increase the total model execution time.

But, the available benefit also depends on the SoC capability, as well as the software stack. and the benefit is only for the model inference part, not including pre or post processing.

So, I will suggest:
1. double check your timer code, only timing the model inference part
2. try latest CANN version and see any difference
3. if still not difference, you could try deeper profiling the model execution (check our documentation). It could be possible that, the SoC you are using (I guess Ascend310) might be already fully utilized even running One batch. In that case, even increasing batch size, you might not see obvious performance benefit.

### RRRRRayyyyy · 2022-12-20

soc=Ascend310，cann version is 5.1.RC1
然后我将模型进行了两种测试，测试时间都只计算了execute的整体时间，not including pre or post processing。图片处理方式参考的samples样例，如下图
![image](https://user-images.githubusercontent.com/109121546/208567773-992bb7d3-d3d3-480c-877d-7a7f7785b966.png)
第一种是固定batch输入转换的om模型，input_shape="images:12,3,640,640" or input_shape="images:8,3,640,640" ,
![image](https://user-images.githubusercontent.com/109121546/208567860-ee739757-6bd6-41e7-ada6-9c3400fec93d.png)
测试结果
![image](https://user-images.githubusercontent.com/109121546/208568176-14789beb-db0b-4a69-b2e4-c1bdcc9ed83b.png)
依然是整体运行时间随着batch增大而增大。
第二种使用动态batch时间，模型转换设置参数input_shape="images:-1,3,640,640" --dynamic_batch_size="1,8,12" 
![image](https://user-images.githubusercontent.com/109121546/208568292-1f2fff77-13d1-46ee-a56b-b86cdfc791d8.png)
测试时间和前面也是一样的。参考了文档和教程，请问我是哪里还存在问题呢？

### ascendhuawei · 2022-12-20

代码应该没有问题，multi-batch本来就不一定能够有收益，可以参考这个issue
https://gitee.com/ascend/samples/issues/I4IJYN?from=project-issue

### RRRRRayyyyy · 2022-12-20

也就是使用dynamic或者multi-batch，时间上是线性增加，并没有想要的并行结果那种收益是吗？

### ascendhuawei · 2022-12-20

就目前这个模型，是这样的。
总的来说，multi-batch有收益的前提是single-batch性能有比较大的富余；同时跟模型结构也有关系；
就某个模型而言，multi-batch能否有收益，以及怎样调整才能有收益，这并不trivial,需要去profiling和实验。

### RRRRRayyyyy · 2022-12-20

好的，请问目前是否有测试，哪些模型在dynamic或者mutil-batch的使用上可以有类似“并行处理”的时间收益呢？

### ascendhuawei · 2022-12-20

这个公开的信息里应该是没有的
