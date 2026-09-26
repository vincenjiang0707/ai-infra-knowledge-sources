source: https://docs.mthreads.com/alphacore/alphacore-doc-online/VeraFiber/VeraFiber_releasenote

# VeraFiber版本信息发布

# AlphaCore Beta 15.3.2

## VeraFiber 1.25.2[](https://docs.mthreads.com#verafiber-1252)

#### Daily 2026 04.09[](https://docs.mthreads.com#daily-2026-0409)

**VeraPipeline for Houdini**[](https://docs.mthreads.com#verapipeline-for-houdini)

- 新增Vera_AutoPostResloveIntersection 后处理穿插修正节点

**Bug修复**[](https://docs.mthreads.com#bug修复)

- 修复Friction计算nan问题
- 修复pin约束未勾选match animation 任继承动画问题

**详情**[](https://docs.mthreads.com#详情)

- 新增Vera_AutoPostResloveIntersection 后处理穿插修正节点：如下图，该节点目前可用于修复简模单片模型两两之间的穿插问题. 通过提高Iteration迭代参数或者控制Effectdis参数改变修正强度来解除穿插。

**注：当前节点不能对自穿插和高模多层效果作出正确修正处理。**

- 修复Friction计算P属性计算nan导致模型消失问题
- 修复pin约束未勾选match animation任然使用动画问题，未勾选使用第一帧位置信息

# AlphaCore Beta 15.3.1

## VeraFiber 1.25.1[](https://docs.mthreads.com#verafiber-1251)

#### Daily 2026 03.25[](https://docs.mthreads.com#daily-2026-0325)

**Bug修复**[](https://docs.mthreads.com#bug修复-1)

- 修复stitch约束导致的布料跳动问题
- 修复pin约束未勾选MatchAnimation且同时开启VelocityBlend参数导致的计算崩溃问题

**详情**[](https://docs.mthreads.com#详情-1)

- 布料在存在stitch约束时，可能因为自碰撞导致布料莫名跳动，影响效果。（如图中左边效果）在该版本修复了该问题，去除了跳动，效果更稳定。（如图中右边效果）

- 用户在使用pin约束时，若未勾选MatchAnimation但同时开启VelocityBlend参数会导致解算文件崩溃，该版本修复了该问题，能够正常模拟。

# AlphaCore Beta 15.3.0

## VeraFiber 1.25.0[](https://docs.mthreads.com#verafiber-1250)

#### Daily 2026 03.10[](https://docs.mthreads.com#daily-2026-0310)

**Bug修复**[](https://docs.mthreads.com#bug修复-2)

- 修复动画旋转时毛发扭曲问题

**详情**[](https://docs.mthreads.com#详情-2)

在动画有旋转动作时，毛发pin住的点orient属性不会动态更新，导致毛发的扭曲方向和动画不一致，在该版本修复了该问题。

修复后，模拟结果和vellum保持一致。

# AlphaCore Beta 15.2.8

## VeraFiber 1.24.8[](https://docs.mthreads.com#verafiber-1248)

#### Daily 2026 02.05[](https://docs.mthreads.com#daily-2026-0205)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features)

- 摩檫力分区控制

**VeraPipeline for Houdini**[](https://docs.mthreads.com#verapipeline-for-houdini-1)

- 增加Hair生长面输出框架

**Bug修复**[](https://docs.mthreads.com#bug修复-3)

- 修复动态约束K帧

**详情**[](https://docs.mthreads.com#详情-3)

**摩檫力分区控制**

- 当前版本支持在布料上添加friction属性来区分控制摩檫力大小.如下图，给红色区域赋予属性 "friction = 10",显示给定红色摩檫力区域摩檫力较大未发生明显滑落。 · 无friction属性时，摩檫力默认使用解算器参数面板 Force> Cloth > Static Threadshould 的数值。 · 存在friction，friction=0区域使用面板参数值，friction≠0 区域使用自定义值。 · 注： friction属性仅在ResloveFriction 下起效， NonFriction 下无法使用该特性。

**增加Hair生长面输出框架**
2. 在xgen毛发曲线解算模板中，增加生长面 abc输出节点

**修复动态约束K帧**

- �修复Vera_ConstraintProperty 节点的 Stiffness ，Velcoity Blend ， Remove 参数失效bug， 可正常K帧控制约束强度变化. 注： 其他参数暂未修复

# AlphaCore Beta 15.2.7

## VeraFiber 1.24.7[](https://docs.mthreads.com#verafiber-1247)

#### Daily 2026 01.20[](https://docs.mthreads.com#daily-2026-0120)

**Bug修复**[](https://docs.mthreads.com#bug修复-4)

- 修复毛发碰撞厚度问题

**详情**[](https://docs.mthreads.com#详情-4)

**修复毛发碰撞厚度问题**

- 旧版毛发碰撞pscale算法会导致毛发紧贴碰撞体。Vera1.24.7对毛发碰撞厚度和自碰撞厚度进行了区分修正，保证毛发与碰撞体之间的厚度正确。

# AlphaCore Beta 15.2.6

## VeraFiber 1.24.6[](https://docs.mthreads.com#verafiber-1246)

#### Daily 2026 01.13[](https://docs.mthreads.com#daily-2026-0113)

**Bug修复**[](https://docs.mthreads.com#bug修复-5)

- 修复毛发碰撞精度不足问题
- 修复解算器Attach，Stitch显示错误

**详情**[](https://docs.mthreads.com#详情-5)

**修复毛发碰撞精度不足问题**

- 增加毛发解算过程碰撞收敛的循环次数，提高毛发的碰撞精度。解算器内部节点 AxOP_SolidCORE 增加Resolve Iteration参数可以控制迭代次数（默认参数为2）。

**修复解算器Attach，Stitch显示错误**

- 修复解算器勾选Visualization > Attach时出现的呲面问题
- 修复解算器勾选Visualization > Stitch时,约束类型 @type=stitch stitch约束不显示问题

# AlphaCore Beta 15.2.5

## VeraFiber 1.24.5[](https://docs.mthreads.com#verafiber-1245)

#### Daily 2026 01.07[](https://docs.mthreads.com#daily-2026-0107)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-1)

- 修复毛发碰撞精度不足问题

**Bug修复**[](https://docs.mthreads.com#bug修复-6)

- 修复GPUBlockCompiler效果不一致问题

**详情**[](https://docs.mthreads.com#详情-6)

**异步加载**

1.新增Async UpdateSim 开关，默认勾选异步加载功能,解算当前帧同时可读取下一帧解算数据，从而优化解算器整体解算速度。开关在VeraFiberSolver > Advance > Async UpdateSim 可启动/关闭。

**GPUBlockCompiler效果不一致问题**

- 修复GPUBlockCompiler 加速过程中速度更新错误，原始动画速度被覆盖导致解算出现强阻力的异常效果.如下图，在Vera1.24.4版本中使用GPUBlockCompiler 导致红色布料下落缓慢，具有较强阻尼感。Vera1.24.5版本两者动态基本一致。

注：使用GPUBlockCompiler加速，解算会与不使用该功能存在轻微差异

**已知问题**[](https://docs.mthreads.com#已知问题)

- 开启Async UpdateSim 异步加载开关，�在多个解算器串行计算时会100%崩溃。 如：VeraFiberSolver1先计算布料,结果给到VeraFiberSolver2 作为碰撞体，此时第二个解算器在开启异步情况下会发生崩溃

# AlphaCore Beta 15.2.4

## VeraFiber 1.24.4[](https://docs.mthreads.com#verafiber-1244)

#### Daily 2025 12.25[](https://docs.mthreads.com#daily-2025-1225)

**Bug修复**[](https://docs.mthreads.com#bug修复-7)

- 修复GPUBlockCompiler导致的毛发抖动问题

**详情**[](https://docs.mthreads.com#详情-7)

**修复GPUBlockCompiler导致的毛发抖动问题**

- 由于毛发边存在接近平行的情况，导致GPUBlockCompiler加速过程中的局部坐标系构建不稳定，相关位置计算错误引发抖动。

# AlphaCore Beta 15.2.3

## VeraFiber 1.24.3[](https://docs.mthreads.com#verafiber-1243)

#### Daily 2025 11.17[](https://docs.mthreads.com#daily-2025-1117)

**Bug修复**[](https://docs.mthreads.com#bug修复-8)

- 修复VeraDeformer包裹P属性nan问题
- 修复VeraFiber 毛发计算P属性nan问题
- 修复VeraFiberSolver Self Collision开关关闭无法取消毛发碰撞问题

**详情**[](https://docs.mthreads.com#详情-8)

**修复VeraDeformer包裹P属性nan问题**

- VeraDefomer 自Vera1.24.1升级后存在包裹导致P属性nan的问题，导致部分模型包裹后无法正常显示，当前版本修复该问题

**修复VeraFiber 毛发计算P属性nan问题**

- 当前版本修复了因毛发曲线点过近导致的计算nan的问题

**修复VeraFiberSolver self collision开关关闭无法取消毛发碰撞问题**

- Vera1.24.2版本VeraFiberSolver Self Collision开关关闭无法取消自碰撞，该问题已在当前版本修复

# VeraFiber版本信息发布

# AlphaCore Beta 15.2.2

## VeraFiber 1.24.2[](https://docs.mthreads.com#verafiber-1242)

#### Daily 2025 09.09[](https://docs.mthreads.com#daily-2025-0909)

**VeraPipeline for Houdini**[](https://docs.mthreads.com#verapipeline-for-houdini-2)

- Vera_Deformer WarpMappingType： 提供两种驱动方式，分别支持高模包裹简模和简模包裹高模 （內部发版）

**详情**[](https://docs.mthreads.com#详情-9)

Vera_Deformer WarpMappingType：1. AssetList Affect Warp-Mes（cloth deformer） ：通过高模包裹简模，获得携带动画的简模. 2. Warp-Mesh Affect AssetList: 通过简模包裹驱动高模

# AlphaCore Beta 15.2.1

## VeraFiber 1.24.1[](https://docs.mthreads.com#verafiber-1241)

#### Daily 2025 08.28[](https://docs.mthreads.com#daily-2025-0828)

**VeraPipeline for Houdini**[](https://docs.mthreads.com#verapipeline-for-houdini-3)

- Vera_Deformer GPU包裹（內部发版）

**详情**[](https://docs.mthreads.com#详情-10)

Vera_Deformer GPU包裹：1. 优点是合并了包裹内容，提升了包裹速度，简化VeraPipeline 包裹结构图。 2. 定义包裹新的DeformerGraph图输出：simMesh（简模），解算simMesh, renderMesh(高模)。可以在CFX-GUN 产品（开发中）获取到这些数据对解算效果进行最终毛发布料快速修型修穿。

# AlphaCore Beta 15.2.0

## VeraFiber 1.24.0[](https://docs.mthreads.com#verafiber-1240)

#### Daily 2025 07.30[](https://docs.mthreads.com#daily-2025-0730)

**Bug修复**[](https://docs.mthreads.com#bug修复-9)

- 修复disableself,disableexternal属性不支持取消自碰撞和碰撞问题
- 修复各约束参数为零时解算器P N v属性计算nan问题
- 修复GPU Block Compiler 不支持vel blend问题

**详情**[](https://docs.mthreads.com#详情-11)

**disableself disableexternal**

**如图上：** 1. Vera1.24.0增加了disableself取消自碰撞,disableexternal取消碰撞体�碰撞功能。
图左Vera1.23.3在黄色选区点属性disableself=1 disableexternal=1 设置下任然发生碰撞和自碰撞；同设置下图右Vera1.24.0黄色选区的碰撞与自碰撞已被取消。

**P N v属性计算nan**

- 修复Attach/Stitch Compression Stiffness等于0造成的计算nan
- 修复ShapeMatch Stiffness等于0造成的计算nan

**GPU Block Compiler 支持vel blend**

**如图上：** 1. Vera1.24.0修复GPU Block Compiler不支持Pin约束Velocity Blend问题（携带动画布料使用Pin约束跟随情况）。图上Vera1.24.0版本在使用GPU Block Compiler 任然可以使布料跟随，图下Vera1.23.3版本布料始终停留在原地。

**已知问题**[](https://docs.mthreads.com#已知问题-1)

- Reset Simluation 按钮功能未修复：出现显存访问报错无法通过Reset Simluation刷新解算器时，需关闭重启工程文件
- Reference Frame 功能未修复
- License 不支持服务器部署
- Attach/stitch silder 功能不支持
- Plastic 功能不支持
- Weld Constraint 功能不支持
- 解算器约束可视化存在错误
- 毛发解算器Orient属性输出不正确，WireDeformer曲线包裹模型bug待修复

**近期计划**[](https://docs.mthreads.com#近期计划)

- 提升解算器整体稳定性
- 升级license部署方案

# AlphaCore Beta 15.1.3

## VeraFiber 1.23.3[](https://docs.mthreads.com#verafiber-1233)

#### Daily 2025 07.18[](https://docs.mthreads.com#daily-2025-0718)

**Bug修复**[](https://docs.mthreads.com#bug修复-10)

- 修复重叠点，点过近导致的解算器P N v属性计算nan
- 修复Vera1.23解算无碰撞体输入勾选碰撞体显示报错

# AlphaCore Beta 15.1.2

## VeraFiber 1.23.2[](https://docs.mthreads.com#verafiber-1232)

#### Daily 2025 07.03[](https://docs.mthreads.com#daily-2025-0703)

**VeraPipeline for Houdini**[](https://docs.mthreads.com#verapipeline-for-houdini-4)

- simMesh renderMesh静帧
- GPU Block Compiler Toggle 创建GPU加速模板

#### 安装包[](https://docs.mthreads.com#安装包)

- Linux 平台安装程序升级

**详情**[](https://docs.mthreads.com#详情-12)

**simMesh renderMesh静帧**[](https://docs.mthreads.com#simmesh-rendermesh静帧)

**如图上：** 1. VeraPipeline在simMesh,renderMesh第一第二输入端口默认加上timeshift节点，定格在 **$FSTART**初始帧，避免USDImport或者Alembic节点每帧读取网络硬盘数据数据过慢。

**GPU Block Compiler Toggle**[](https://docs.mthreads.com#gpu-block-compiler-toggle)

**如图上：布料模板创建** 1. VeraPipeline UI界面增加GPU Block Compiler 勾选选项。2.在勾选时创建布料模板时，会在约束之前的**clothProcess NULL**节点创建**AlphaCore_GPU_block_compiler_begin**节点作为加速编译功能的起点；3.在**VeraFiberSolver**节点之后创建**AlpahCore_GPU_block_compiler_end**节点作为加速编译的终点。

**如��图上：毛发模板创建** 与布料创建原则保持一致，GPU Block Compiler节点组包含约束和解算器。

#### Linux 平台安装程序升级[](https://docs.mthreads.com#linux-平台安装程序升级)

- 安装包Linux CUDA 增加20.0.547版本安装。详情参考本页文档
**安装指导>2 Linux>2.1 脚本自动安装**安装方式

# AlphaCore Beta 15.1.1

## VeraFiber 1.23.1[](https://docs.mthreads.com#verafiber-1231)

#### Daily 2025 06.24[](https://docs.mthreads.com#daily-2025-0624)

**Bug修复**[](https://docs.mthreads.com#bug修复-11)

- 修复毛发碰撞失效问题
- 修复license配置错误发送404报错问题
- 修复HDA参数链接错误造成的异步加载性能下降问题

# AlphaCore Beta 15.1

## VeraFiber 1.23.0[](https://docs.mthreads.com#verafiber-1230)

#### Daily 2025 06.23[](https://docs.mthreads.com#daily-2025-0623)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-2)

**异步性能加速（GPUBlockComplier/HoudiniHDK 计算异步处理）：**解算器解算效率提升**碰撞效果优化：**新增AutoDisbleCollision功能，大幅优化布料粘连，布料穿插问题**显存优化：**当前版本优化了同一文件多解算器显存异常占用问题**License升级：**替换后台服务器增加license服务稳定性**MUSA性能优化：**优化摩尔MUSA驱动环境下解算器速度**安装包升级：**安装包文件层级结构修改升级，产品之间做结构性拆分

**VeraPipeline for Houdini**[](https://docs.mthreads.com#verapipeline-for-houdini-5)

**VeraWireDeformer：**新增orient曲线包裹工具修复曲线包裹曲线扭转问题

**详情**[](https://docs.mthreads.com#详情-13)

**异步性能加速（GPUBlockComplier/HoudiniHDK 计算异步处理）**

**如图上：** 1. Vera1.23增加计算异步处理特性，可以解算当前帧同时及时获取下帧解算数据，相对Vera1.22有效减少10%-50%因数据读取造成是解算耗时。

**如图上：** 2. Vera1.23增加GPU Block Compiler特性加速毛发布料解算。已毛发为例，毛发通常需要使用大量pin constraint 来完成每一帧的动态跟随；但每一帧重复属性更新会大幅降低解算器的解算效率。Vera1.23通过增加**GPU Constraint BlockCompiler**节点组**AlphaCore_GPU_block_compile_begin**/**AlphaCore_GPU_block_compile_end**属性**P**进行编译。解算平均速度相对vellum提升3倍,相对vera1.22平均提升1.7倍（常规角色毛发解算24FPS左右）。

**碰撞效果优化**

**如图上：** 1. Vera1.23增加AutoDiableCollision碰撞特性，可以标记并忽略部分穿插布料碰撞计算，大幅提升碰撞品质。

**显存优化：**

**如图上：** 1. 记录Vera1.22版本与VeraFiber1.23同一Hip文件存在多个解算器显存使用情况。Vera1.22同时存在四个解算器是消耗9G显存，相同情况下Vera1.23仅占用4.7G。大幅优化同一文件多开解算器导致的显存爆满问题,避免显存溢出造成的解算性能下降。

**License升级：**

**如图上：** 1. Vera1.23优化了License部署方式，由 **$HFS/AlphaCore**修改为 **$HOME/houdiniX.Y/AlphaCore**；移除旧版对于axServerConfig.json依赖。2. 同时后台license做服务器切换升级提高体验稳定性。

**MUSA性能优化**

- 优化排序算法，提升MUSA环境下10%解算速度

**安装包升级：**

- 安装方式：
- 双击
**AxHoudiniPluginsSetup.exe** - 选择需要安装Houdini版本
- 关闭Houdini,点击
**Setup**安装

- 双击
- 安装内容：
- 拷贝mt文件夹中所有资产至
**$HOME/** - 自动配置目标
**houdini.env**环境变量。 - 注：不会对原有文档下/otls,/hda 文件夹做覆盖或者删除，存在旧版资产需及时清理避免冲突。

- 拷贝mt文件夹中所有资产至

- 安装包结构变化
- 产品：mt文件夹将包含
**FilmWorks**，**AlphaCore**两款产品；同时AlphaCore包含**Catayst**，**VeraFiber**两款子产品。 - 结构规范： 如上图，产品文件夹下统一存放
**/hda**,**/script**,**/toolbar**资产；HDA不在做版本区分管理，dso多版本统一存放与`/mt/AlphaCore/Utility/dso/xx.x.xxx`

文件夹中 - 公用资产：对于
**VeraFiber**,**Catalyst**子产品存在公用资产统一存储与`/mt/AlphaCore/Utility`

- 取消结构：包体不在按以Houdini版本做文件夹存放hda和otls资产。如:删除了
**/19.5.303/hda**,**/19.5.303/otls**

- 产品：mt文件夹将包含

**VeraWireDeformer**

曲线包裹工具升级,修复曲线包裹模型扭转问题，包裹速度和稳定性相对旧版Vera_CurveDeformer均有大幅优化

**Bug修复**[](https://docs.mthreads.com#bug修复-12)

- 修复VeraFiberSolver 参数PBD-Iteration,PBD-SmoothIteration 为0时,解算陷入卡死问题
- 修复VeraPipeline 布料毛发模板先后创建会导致后者创建失败问题
- 修复上游数据dirty，或者主动 restSimulation 导致的显存泄漏问题
- 修复SolidCORE 显存再分配策略导致CPU逻辑死循环问题
- 修复同一文件内多解算器造成的显存爆炸问题

**注意事项**[](https://docs.mthreads.com#注意事项)

**新旧版本解算器冲突及解决方案**

**冲突**：在使用Vera1.23HDA资产打开旧版本工程文件时，会导致解算器面板Dev->SystemIntrinsic->IsAniClothPinPropNmae 无法正确加载python通道，造成pin约束相关的计算错误**解决方案**：如下图通过`Ctrl+鼠标中键`

点击面板IsAniClothPinPropName,紫色显示后即为正确设置。 注：上游若使用pin约束，则该面板根据使用的pin类型自动填入**gluetoanimation**或者**pintoanimation**信息

**手动安装包配置相关问题**

- 手动配置安装包：需要指认houdini.env文件
**HOUDINI_PATH**至目标产品文件夹下

`# mt config start`

MTPATH = C:/Users/xianjun.zhu/Documents/houdini19.5/mt/AlphaCore

HOUDINI_PATH = $MTPATH/Catalyst;$MTPATH/Utility;$MTPATH/VeraFiber;&

# mt config end



- 拷贝dll: 将
`/mt/AlphaCore/Utility/dso/<houdini ver>`

下dll文件拷贝至`/mt/AlphaCore/Utility/dso`

，可以保证**HOUDINI_PATH**中**$MTPATH/Utility**可以正确识别到dll

**近期计划**[](https://docs.mthreads.com#近期计划-1)

- 提升解算器整体稳定性

# AlphaCore Beta 14.4

## VeraFiber 1.22.4[](https://docs.mthreads.com#verafiber-1224)

#### Daily 2025 5.19[](https://docs.mthreads.com#daily-2025-519)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-3)

**版本适配：**新增Houdini 20.5.522版本适配

# AlphaCore Beta 14.3

## VeraFiber 1.22.3[](https://docs.mthreads.com#verafiber-1223)

#### Daily 2025 3.20[](https://docs.mthreads.com#daily-2025-320)

**VeraPipeline for Houdini**[](https://docs.mthreads.com#verapipeline-for-houdini-6)

**VeraPipeline工具优化升级：**当前版本优化了毛发模板自动创建框架逻辑

**详情**[](https://docs.mthreads.com#详情-14)

**VeraPipeline**[](https://docs.mthreads.com#verapipeline)

- 优化毛发选择参数暴露，进一步方便解算毛发筛选
- 优化Vera_GradientCurve 渐变跟随，psale设置
- 优化空间缩放逻辑
- 剔除模板重叠节点

# AlphaCore Beta 14.2

## VeraFiber 1.22.2[](https://docs.mthreads.com#verafiber-1222)

#### Daily 2025 3.10[](https://docs.mthreads.com#daily-2025-310)

**VeraPipeline for Houdini**[](https://docs.mthreads.com#verapipeline-for-houdini-7)

**VeraPipeline工具优化升级：**当前版本优化了模板框架逻辑

**详情**[](https://docs.mthreads.com#详情-15)

**VeraPipeline**[](https://docs.mthreads.com#verapipeline-1)

- 优化毛发模板与布料模板节点冲突
- 优化布料模板Vera_AssetLayerMatch选择功能
- 优化布料模板Vera_RenderAssetSelect高模重复筛选
- 增加模板点序排序功能
- 增加Extracttransform Tpose位置修复预设
- 修复毛发模板class属性缺失，remesh timeshift定帧，vera_Deform cloth ani节点生成错误问题

# AlphaCore Beta 14.1

## VeraFiber 1.22.1[](https://docs.mthreads.com#verafiber-1221)

#### Daily 2024 12.26[](https://docs.mthreads.com#daily-2024-1226)

**VeraPipeline for Houdini**[](https://docs.mthreads.com#verapipeline-for-houdini-8)

**VeraPipeline工具优化升级：**当前版本优化了模板自动创建框架逻辑，并且增加了部分节点初始化设置

**详情**[](https://docs.mthreads.com#详情-16)

**VeraPipeline**[](https://docs.mthreads.com#verapipeline-2)

- Vera_AssetLayerMatch简模包裹映射结束后增加remesh可自行重拓扑解算片
- 增加paintColor可自行在碰撞体上绘制颜色属性作为自动修穿插功能的遮罩贴图
- Vera_SimMeshDoctor：关闭节点打印
- 设置vellumconstraint节点默认mass：0.001,bendstiffness：0.001
- 设置attachconstraint节点作用区域根据mask>0.1表达式自动筛选attach 范围
- 自动创建模板ABC导出节点和USD导出节点

# AlphaCore Beta 14

## VeraFiber 1.22[](https://docs.mthreads.com#verafiber-122)

#### Daily 2024 12.19[](https://docs.mthreads.com#daily-2024-1219)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-4)

**碰撞品质提升：**当前版本对穿插问题进行了优化，提升了碰撞品质**新增Attach Tangent Stiffness功能支持：**当前版本开始支持Attach约束类型下设置的TangentStiffness功能

**详情**[](https://docs.mthreads.com#详情-17)

**宽阶段**

**如图（上）：** 角色在运动过程中因部分穿插未被检测到，造成布料大面积的穿插。如图左，旧版Vera存在碰撞检测遗漏问题，导致手臂、裙帘都出现了大面积穿插现象。图右新版修复该问题，大幅提升了该类问题碰撞品质。

**Tangent Stiffness**

**如图（上）：** 本次更新支持了VellumConstraint Attach 约束的Tangent Stiffness 功能。具体效果如上图，开启TangentStiffness的绿色布料可以保持Attach约束位置不发生滑动，未开启的红色布料相对与约束的参考位置向下发生了滑动。该功能可以用来模拟角色腰带，裙子等需要固定在身体上的效果。

**近期计划**[](https://docs.mthreads.com#近期计划-2)

- 进一步提高碰撞品质

# AlphaCore Beta 13

## VeraFiber 1.21[](https://docs.mthreads.com#verafiber-121)

#### Daily 2024 11.29[](https://docs.mthreads.com#daily-2024-1129)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-5)

**解算器新增Hair模块计算：**当前版本开始支持Hair类型数据解算。**碰撞模块算法更新：**新增DynamicPscale计算，在解算过程中，根据布料压缩程度实现对厚度的自适应调整，减少布料在极端压缩情况下产生的穿插与抖动

**详情**[](https://docs.mthreads.com#详情-18)

**Hair解算效果对比**

**如图上** 记录了VeraFiber解算器与Vellum解算器的Hair解算效果。场景中分别测试对比了Hair有碰撞和无碰撞时一阶与二阶的效果，计算结果基本一致。

**DynamicPscale效果对比**

**如图上** 这是一个极限挤压多层布料解空间的测试场景。vellum布料在挤压碰撞后，因为解空间过小，多层布料间产生了穿插。VeraFiber解算器新增DynamicPscale计算后，会根据解空间大小，动态调整Pscale大小，改善了多层布料间的穿插。

**Bug修复**[](https://docs.mthreads.com#bug修复-13)

- 修复使用DisableCollision属性取消碰撞失效的问题。
- 修复碰撞模块BVH Update Structure错误问题
- 修复Hair解算中Pin约束Stop模式失效问题

**近期计划**[](https://docs.mthreads.com#近期计划-3)

- 进一步提高碰撞品质

# AlphaCore Beta 12

## VeraFiber 1.20[](https://docs.mthreads.com#verafiber-120)

#### Daily 2024 11.14[](https://docs.mthreads.com#daily-2024-1114)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-6)

-
**新增Velocity Blend功能支持：**当前版本开始支持Attach与Pin约束类型下设置的Velocity Blend功能。 -
**Vellum Reference Frame节点兼容：**当前版本开始支持在VeraFiberSolver解算器上游使用Vellum Reference Frame节点。 -
**新增碰撞体摩擦力：**解算器面板Friction模块下新增碰撞体摩擦力参数，支持对碰撞体的摩擦力强度进行调节。 -
**新增Velocity Damping功能：**解算器面板Force模块下新增Velocity Damping参数，支持对速度阻尼强度的调节。 -
**新增Vera AutoCollisionFree 节点：**新增自动修穿插节点，支持动态解除封闭模型的自穿插，构建解算空间

**Experiment Feature**[](https://docs.mthreads.com#experiment-feature)

**新增 SubCollision Marching 技术：**当前版本开始，解算器新增SubCollision Marching功能，该功能开启后可以优化快速运动镜头中布料的碰撞结果，减少穿插的产生。

**Bug修复**[](https://docs.mthreads.com#bug修复-14)

- 修复Pin约束选中的区域自碰撞失效问题
- 修复Pin约束下Orientation Pin Type类型切换导致的约束失效问题
- 修复CollisionResolve模块在有摩擦力的情况下可能存在数值爆炸的问题

**详情**[](https://docs.mthreads.com#详情-19)

**Velocity Blend功能**

**如图（上）：** 场景中的布料使用Attach约束连接到拥有摆动动画的角色身体上，当启用Attach约束上的Velocity Blend功能，布料解算时的速度会和Attach约束目标（角色身体）的速度做融合。未开启该功能时，布料解算后的速度较大，摆动幅度比较明显。开启该功能后，布料的速度受角色身体动画速度影响变小，摆动幅度也随之变小。

**如图（上）：** 测试场景中，画面左侧是一个拥有左右摆动动画的Box模型，右侧是进行解算的布料（Grid）模型。在未使用Vellum Reference Frame节点时，布料解算在无其他外力作用的情况下是自然垂落状态。当画面左侧的Box模型作为Vellum Reference Frame节点的第三输入端，启用Vellum Reference Frame功能后，布料解算的动态在无其他外力作用的情况下，是随着Box模型的动画进行左右摆动的。

**碰撞体摩擦力**

**如图（上）：** 这是一个物体滑落的测试场景，在解算物体摩擦力强度一致的情况下，画面右侧的碰撞体摩擦力高于画面左侧，所以物体滑落程度小于左侧的布料。

**如图（上）：** 这是一个布料自由落体的测试场景，黄色的线段长度表示当前布料运动速度的大小。从黄色速度线的长度显示上可以看到，当Velocity Damping值越大，速度线的长度越短，速度也就越小。所以Velocity Damping为0时，布料在20帧处可以落至地面。当Velocity Damping值为0.3时，布料在20帧处还处于下降状态。

**如图（上）：** 这是角色在动态运动时的穿插动画，图中红色标记区域表示节点自动查询到的穿插位置。标记区域在合理参数迭代下解除自穿插，并且每帧随动画的改变自动修正穿插位置，同时尽量保证无穿插区域保持动画原始动态。此外该节点支持Houdini 属性Cd作为Mask遮罩，黑色区域将不在参与穿插修正。

**如图（上）：** 场景中的模型动画在一帧内产生了较大的位移，在未开启SubCollision Marching功能时，布料上存在多处穿插，开启SubCollision Marching功能后，布料的穿插效果得到改善。

**如图（上）：** 红色显示的是Pin约束选中的布料区域。修复前，该区域无自碰撞修正，修复后拥有正确的自碰撞修正效果。

**近期计划**[](https://docs.mthreads.com#近期计划-4)

- 优化解算效率
- 新增Hair毛发功能
- 新增TangentStiffness功能
- 进一步提高碰撞品质
- DynamicPscale：在解算过程中，根据布料压缩程度实现对厚度的自适应调整，减少布料在极端压缩情况下的抖动

# AlphaCore Beta 11.2

## VeraFiber 1.19[](https://docs.mthreads.com#verafiber-119)

#### Daily 2024 7.29[](https://docs.mthreads.com#daily-2024-729)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-7)

-
**新增显存释放按钮**：VeraFiberSolver解算器面板新增Clean Device Memory按钮，点击后可以释放当前解算器占用的显存。有多个Houdini文件开启时，未解算文件的解算器依然会有显存占用，可以使用当前功能实现显存释放。 -
**新增显存复用功能**：在旧版本VeraFiber中，当同一文件存在多个解算器时，无论该解算器是否触发计算，都会占用显存。优化后，创建多个 Solver ，显存不会成倍增长。 -
**新增用户帮助文档**：提供用户帮助文档，包含基础案例101教学，高级案例教学，材料力学。 -
**解算器效率提升：****碰撞检测优化：**对碰撞检测模块Kernel进行优化，提高计算运行效率。**Simgraph节点图连接优化**：优化了VeraFiberSolver解算器的节点图连接方式，消除了SubStep运行时存在的气泡间隔。提高了解算器的运行效率。


**详情**[](https://docs.mthreads.com#详情-20)

**新增按钮**

| Example Name | Frames | Primitives | Parameter | vellum | VeraFiber 1.18 | VeraFiber 1.19 |
|---|---|---|---|---|---|---|
| Sit Dowm | 130 | 26w Triangles 220368 + 43270 (Cloth&body) | 300 Tieration 10 Collision Passes 30 Post Collision Passes | 3 substep : 20min | 3 substep : 6min49s | 3 substep : 4min36s |

**效率测试**：**GPU RTX 3060****CPU i7-11700**

**近期计划**[](https://docs.mthreads.com#近期计划-5)

- 优化显存占用
- 新增FEM

# AlphaCore Beta 11.0

## VeraFiber 1.18[](https://docs.mthreads.com#verafiber-118)

#### Daily 2024 7.1[](https://docs.mthreads.com#daily-2024-71)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-8)

-
**解算效率提升**：优化了stich约束的染色方式，通过减少异常颜色数量提高解算效率。 -
**碰撞修正算法优化**：加快CollisionResolve计算的收敛速度。减少因为修正次数不足引起的布料穿插。

**Bug修复**[](https://docs.mthreads.com#bug修复-15)

- 修复Shape Match约束导致计算速度下降的问题
- 修复Shape Match约束与Pin约束同时使用时，Pin约束失效的问题

**详情**[](https://docs.mthreads.com#详情-21)

**解算效率测试**：GPU RTX 3060

| Example Name | Frames | Primitives | Parameter | VeraFiber 1.17 | VeraFiber 1.18 |
|---|---|---|---|---|---|
| Sit Down | 130 | 26 w Triangles 220,368 + 43,270 ( Cloth & Body ) | 300 Iterations 10 Collision Passes 30 Post Collision Paases | 3 substep : 8min31s | 3 substep : 6min49s |

**Shape Match约束解算效率测试**：GPU RTX 3060

| Example Name | Primitives | Parameter | VeraFiber 1.17 | VeraFiber 1.18 | |
|---|---|---|---|---|---|
| Sphere | 4400 Triangles | Default Paramater | 2 substep : 单帧耗时：0.45秒(2.2FPS） | 2 substep : 单帧耗时： 0.12秒(8.2FPS） |

**近期计划**[](https://docs.mthreads.com#近期计划-6)

- 显存管理优化
- 新增用户文档

# AlphaCore Beta 10.0

## VeraFiber 1.17[](https://docs.mthreads.com#verafiber-117)

#### Daily 2024 5.23[](https://docs.mthreads.com#daily-2024-523)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-9)

-
**碰撞检测模块性能优化****1.**VV类型碰撞检测算法改进：提高了布料与碰撞体之间点对点(Vertex-Vertex)类型检测的运行效率。**2.**优化了Post Collision模块的计算逻辑，提高运行效率。 -
**ShockPropagationScale参数设置优化**

**详情**[](https://docs.mthreads.com#详情-22)

性能测试 Example

GPU RTX 3060

| Example Name | Frames | Primitives | Parameter | VeraFiber 1.16 | VeraFiber 1.17 | Houdini 19.5 Vellum |
|---|---|---|---|---|---|---|
| Sit Down | 130 | 26 w Triangles 220,368 + 43,270 ( Cloth & Body ) | 300 Iterations 10 Collision Passes 30 Post Collision Paases | 3 substep : 11min 8 substep : 26min | 3 substep : 8min8 substep : 19min | 3 substep : 17min 8 substep : 40min |

**近期计划**[](https://docs.mthreads.com#近期计划-7)

- 显存优化
- 性能优化

# AlphaCore Beta 9.1

## VeraFiber 1.16.2[](https://docs.mthreads.com#verafiber-1162)

#### Daily 2024 5.17[](https://docs.mthreads.com#daily-2024-517)

**Bug修复**[](https://docs.mthreads.com#bug修复-16)

**VeraPipeline Vera_CurveDeformer**：修复曲线包裹模型发生的扭转问题。

# AlphaCore Beta 9.0.1.A

## VeraFiber 1.16.1[](https://docs.mthreads.com#verafiber-1161)

#### Daily 2024 5.8[](https://docs.mthreads.com#daily-2024-58)

**Bug修复**[](https://docs.mthreads.com#bug修复-17)

**VeraPipeline Vera_Deformer**：修复节点包裹后法线更新错误问题。

# AlphaCore Beta 8.0.1

## VeraFiber 1.16[](https://docs.mthreads.com#verafiber-116)

#### Daily 2024 4.30[](https://docs.mthreads.com#daily-2024-430)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-10)

**解算器新增Body Volume Collision Build功能**：改进了布料与封闭躯体的碰撞方式，功能开启后可以减少布料与角色碰撞体之间的穿插。

**详情**[](https://docs.mthreads.com#详情-23)

**如图上** 测试镜头为一段大位移动画，左侧是关闭Body Volume Collision Build功能的效果，右侧是开启后的效果，布料与碰撞体之间的穿插得到了改善。

**Bug修复**[](https://docs.mthreads.com#bug修复-18)

**Pin约束**：修复Pin约束在Stop模式下，勾选Match Animation项，布料未跟随动画的问题。**shockPropagation参数**：修复参数值过大时，布料会在无外力作用下产生大面积抖动的问题。**碰撞检测模块**：修复动画位移距离过大时，布料碰撞检测出现区域遗漏的问题。

**近期计划**[](https://docs.mthreads.com#近期计划-8)

- 解算器运行效率提升。

# AlphaCore Beta 8.0.2

## VeraFiber 1.15.2[](https://docs.mthreads.com#verafiber-1152)

#### Daily 2024 2.5[](https://docs.mthreads.com#daily-2024-25)

**VeraFiber Houdini Plugin 版本支持**[](https://docs.mthreads.com#verafiber-houdini-plugin-版本支持)

**Windows平台**：新增Houdini 20.0.547版本解�算器。

**近期计划**[](https://docs.mthreads.com#近期计划-9)

- 提高碰撞修正品质，减少穿插。
- 解算器运行效率提升。

# AlphaCore Beta 8.0.1

## VeraFiber 1.15.1[](https://docs.mthreads.com#verafiber-1151)

#### Daily 2024 2.4[](https://docs.mthreads.com#daily-2024-24)

**Bug修复**[](https://docs.mthreads.com#bug修复-19)

- 修复大动态镜头中，布料部分区域碰撞失效，产生穿透的问题。
- 修复个别计算场景中，由于碰撞修正不足而导致穿插的问题。

**近期计划**[](https://docs.mthreads.com#近期计划-10)

- 提高碰撞修正品质，减少穿插。
- 解算器运行效率提升。

# AlphaCore Beta 8.0

## VeraFiber 1.15[](https://docs.mthreads.com#verafiber-115)

#### Daily 2024 1.26[](https://docs.mthreads.com#daily-2024-126)

**VeraFiber Plugin新增 Features**[](https://docs.mthreads.com#verafiber-plugin新增-features-11)

-
**碰撞修正算法改进**- 全新的碰撞修正内核，提供满足能量守恒的穿插修正方法， 抖动现象大幅减少。
- 新增 VV,VE 碰撞接触类型 ：支持布料与碰撞体之间的点对点
**(Vertex-Vertex)**和点对边**(Vertex-Edge)**碰撞。减少复杂布料模型在解算时的穿插现象。

-
**计算确定性支持**：在解算器参数设置不变的情况下，每次解算都能得到同样的计算结果。 -
**摩擦力计算效果改进**: 修复了解算器摩擦力参数过大时，布料产生抖动的问题。

**Bug修复**[](https://docs.mthreads.com#bug修复-20)

- 修复了解算器WindScale参数K帧失效问题。

**详情**[](https://docs.mthreads.com#详情-24)

**碰撞修正算法改进**

**如图（上）** 这是一个多层布料降落堆积的测试，布料完成堆积状态后应该趋于静止。旧版的布料解算器，在落地后长时间内仍存在随机性的抖动现象，从图中能看到许多长短不一的黄色速度线（**上**）。新版本的布料解算器，可以在布料落地堆积的过程中，快速稳定下来（**下**）。

-
**新增 VV / VE 碰撞接触类型**新版VeraFiber解算器，新增了碰撞接触的类型支持。新增了点对点

**(Vertex-Vertex)**和点对边**(Vertex-Edge)**的碰撞接触类型支持，可以提升布料解算状态的稳定性

**如图（上）** 当前实验设置布料为自由落体，并最终悬挂在球体障碍物上。旧版解算器的仿真结果，最终在无任何外力作用的悬挂状态下，仍产生了向某个方向上的飞起错误（**上**）。而新版本的解算器可以保持最终悬挂状态的稳定（**下**）。

-
**计算确定性支持**旧版VeraFiber解算器，在调用GPU版本时，同文件参数下，每次计算都会得到不同的结果。新版解算器，提供了计算确定性支持。


**如图（上）** 在不改变解算器参数的前提下，进行两次计算。旧版解算器，第一次计算 **(白色模型)** 与第二次计算 **(红色线框)** 的最终计算结果存在较大差异（**上**）。新版解算器每次计算都可以得到完全一样的效果（**右**）。

**近期计�划**[](https://docs.mthreads.com#近期计划-11)

- 提高碰撞修正品质，减少穿插。
- 解算器运行效率提升。

# AlphaCore Beta 7.1.1

## VeraFiber 1.14.1[](https://docs.mthreads.com#verafiber-1141)

#### Daily 2023 12.4[](https://docs.mthreads.com#daily-2023-124)

**Bug修复**[](https://docs.mthreads.com#bug修复-21)

`001`

修复 Smooth Iteration 中，由于ARAP（Triangle Stretch）约束更新遗漏，所导致的 stitch 约束在距离过小，接近布料厚度叠加时范围时，产生的碰撞爆炸问题。

**如图（上）** 功能修复前，**在无任何外力，无任何碰撞作用的纯重力悬挂状态下**，大衣口袋位置仍然**凭空出现了拉扯异常**，该错误修复后，凭空出现的拉扯异常消失。
`002`

修复了 Houdini 工程文件在修改 FPS 工程设置后，导致解算器读取的场景动画混乱，解算结果无法对齐原始输入动画的错误。

#### 近期计划[](https://docs.mthreads.com#近期计划-12)

`001`

新增 SubCollision Marching 技术，优化快速运动动画的碰撞结果

`002`

新增显存开销过大时的Solver过载保护机制

`003`

Activation-EE：EE 计算性能优化

`004`

AxOP ParticleWind 风场可视化

`005`

减缓碰撞抖动

# AlphaCore Beta 7.1

## VeraFiber 1.14[](https://docs.mthreads.com#verafiber-114)

#### Daily 2023 11.23[](https://docs.mthreads.com#daily-2023-1123)

**VeraPipeline for Houdini 新增 Features**[](https://docs.mthreads.com#verapipeline-for-houdini-新增-features)

-
**新增破碎重叠模型修复工具组 (MakeClothLayer)**

**Vera SplitClothLayer 节点**提供一系列全自动的布料破面修补，及分层方法，修复因材质分区过于复杂导致的模型破碎重叠问题。


**如图（上）** 使用 VeraPipeline 提供的 MakeClothLayer 节点组，可以全自动的修复由于特殊材质处理导致的解算模型破损问题，直接使用渲染模型进行解算，省去手动制作 SimCloth 解算模型的制作步骤

**Vera MakeClothLayer 节点**

在全自动破面修补，分层方案不能满��足需求的情况下，MakeClothLayer 节点提供了一套 **半自动** 的解算模型及曲线生成方案，并支持自定义SimCloth解算模型的手动导入匹配。

**如图（上）** MakeCLothLayer 节点提供了复杂模型对应解算模型的五种生成或者匹配方式。使用默认的None将模型直接视为解算模型，Mesh将生成适配当前模型的解算模型，Line和LineLab3d生成适配当前模型的曲线，Custom允许导入外部自定义解算模型作为解算对象。

**Vera WrapClothLayer 节点**

配合 Makeclothlayer 工具所生成的解算模型的专用定制包裹器，避免对原始的破碎重叠面进行手动包裹处理

**如图（上）** WrapCLothLayer 根据上游节点组提供的解算模型信息可以提取对应的渲染模型，节省手动选取复杂渲染模型时间

#### 近期计划[](https://docs.mthreads.com#近期计划-13)

`001`

新增 SubCollision Marching 技术，优化快速运动动画的碰撞结果

`002`

新增显存开销过大时的Solver过载保护机制

`003`

Activation-EE：EE 计算性能优化

`004`

AxOP ParticleWind 风场可视化

`005`

减缓碰撞抖动

# AlphaCore Beta 7.0

## VeraFiber 1.13[](https://docs.mthreads.com#verafiber-113)

#### Daily 2023 11.17[](https://docs.mthreads.com#daily-2023-1117)

**VeraFiber Houdini Plugin 新增 Features**[](https://docs.mthreads.com#verafiber-houdini-plugin-新增-features)

- 新增 ARAP 材料力学模型支持：当前版本开始支持 Vellum Constraint 节点设置里的 Triangle Stretch 类型约束
- 改善BDF2积分器计算效果：修复 BDF2 积分器在参与快速碰撞反应时的积分能量不守恒现象。

**如图（上）** 在有快速碰撞响应，且布料精度极高的时候，BDF2 积分器会产生能量不守恒的积分现象（中），这个错误已在新版本中得到修正（右）

# AlphaCore Beta 6.3

## VeraFiber 1.12[](https://docs.mthreads.com#verafiber-112)

#### Daily 2023 11.7[](https://docs.mthreads.com#daily-2023-117)

**Bug 修复**[](https://docs.mthreads.com#bug-修复)

`001`

材料计算准确度提高： 修复 stiffness 量级在 1e-7 1e-8 并且材料密度极��低（mass 1e-5以下）的情况下 bend constraint 的计算失败问题

`002`

优化 GroundCollision 碰撞摩擦力计算方式，修复先前 Solver 开启 GroundCollision 后，由于摩擦力计算失败导致的摩擦力作用效果不足，不明显等问题

`003`

修复 SOP SimGraph 节点在输入不存在 ComputeBuffer 之后进行回读导致 Crash 的 bug

`004`

修复 SimLoop 算子 RateControl 中，在多节点路径设置时的静态分析错误问题。

#### 详情[](https://docs.mthreads.com#详情-25)

**如图（上）** 从当前版本开始，使用同样参数的 Bend Constraint 设置，VeraFiber **（红）** 和 Vellum **（绿）** 可以计算出几乎一样的效果

#### 近期计划[](https://docs.mthreads.com#近期计划-14)

`001`

ARAP 材料模型支持

`002`

新增 SubCollision Marching 技术，优化快速运动动画的碰撞结果

`003`

新增显存开销过大时的Solver过载保护机制

`004`

提供 MakeClothLayer 功能正式版

`005`

Activation-EE：EE 计算性能优化

`006`

AxOP ParticleWind 风场可视化

# AlphaCore Beta 6.2

## VeraFiber 1.11[](https://docs.mthreads.com#verafiber-111)

#### Daily 2023 10.31[](https://docs.mthreads.com#daily-2023-1031)

#### VeraPipeline for Houdini 新增 Features[](https://docs.mthreads.com#verapipeline-for-houdini-新增-features-1)

`001`

新增 Vera Makeclothlayer 节点组：修复因材质分区过于复杂，而导致的模型破碎及重面问题。该节点可以根据初始FBX模型中所提供的材质信息，解析渲染模型并生成可以用于解算的解算模型。

**如图（上）** 使用 VeraPipeline 提供的 MakeClothLayer 节点组，可以修复由于特殊材质处理导致的解算模型破损问题，直接使用渲染模型进行解算，省去手动制作 SimCloth 解算模型的制作步骤

# AlphaCore Beta 6.1

## VeraFiber 1.10[](https://docs.mthreads.com#verafiber-110)

#### Daily 2023 10.23[](https://docs.mthreads.com#daily-2023-1023)

**VeraFiber Houdini Plugin 新增 Features**[](https://docs.mthreads.com#verafiber-houdini-plugin-新增-features-1)

`001`

DOP 模块数据接口全新升级（SimDataInterface），提供对 Houdini DOP Force 类型节点的兼容，以及动态Group信息读取

`002`

DOP 节点计算兼容性提高，修复 Houdini POP Wind 节点计算结果和 Houdini POP 计算不一致的错误，支持外部 Group 数据传递

`003`

支持自定义 Debug 数据 Loadback Visualization

`004`

Ground Collision 增加摩擦力支持

`005`

四边面模型输入下的风阻计算错误优化

`006`

提供 Houdini Vellum 相似的 Exponential 阻尼计算

`007`

Stiffness Dropoff DOP 版本支持

`008`

Vera Constraint Property 节点计算失效修复

`009`

BDF2 二阶积分器缺失功能对齐，现为Solver的默认积分器类型

**Bug 修复**[](https://docs.mthreads.com#bug-修复-1)

`001`

修复了解算器输入不完备导致的各类 Houdini Crash Bug

`002`

修复由于设计不当，造成的 SubStep 子步计算中所有 DOP 节点的计算失败错误

`003`

修复 DOP 版本 VeraFiber Self-Collision 勾选失效错误

`004`

优化 DOP 自定义速度编辑的回调流程，提高数值稳定性减少由于用户对速度过度编辑带来的不稳定抖动现象

#### 详情[](https://docs.mthreads.com#详情-26)

-
**提高 Houdini DOP 节点计算兼容性**新版本 VeraFiber 完善了 Houdini DOP 节点计算支持，修复了 DOP DataInterface 的对接错误，可最大程度保证 DOP 节点在 Houdini DOP中和 VeraFiber 中��有同样的计算作用效果


**如图（上）** 同样参数的 POP Wind 节点添加在 Vellum 和 VeraFiber 内部，使用 3 的 Substep 进行计算推进，在关闭碰撞（忽略碰撞计算对形态的影响）的情况下，VeraFiber **（实体模型）** 和 Vellum **（红色线框）** 可以计算出几乎一样的效果

**如图（上）** 新版本也修复了 Houdini 原生 DOP 节点在 VeraFiber DOP 计算图中的外部 Group 组信息丢失问题

-
**Stiffness Dropoff DOP 版本**新版本VeraFiber 提供了对 vellumConstraint节点上 SitffnessDropoff参数设置的兼容，用来动态修改约束的stiffness强度。例如，通过设置bend参数的SitffnessDropoff值，可以实现在计算过程中物体的弯曲程度的控制。#### 示例1

[](https://docs.mthreads.com#示例1)

**如图（上）：** Decresasing 衰减模式下，只要计算约束的当前帧的角度值大于设定的dropoff角度阈值，就会发生坍塌。红色区域sitiffness强度会被修改为0或是设置的Minsitffness.

#### 示例2[](https://docs.mthreads.com#示例2)

**如图（上）：** Bend Dropoff开启的布料��在弯曲角度大的位置会降低bend stiifness的强度，会更容易保住褶皱。并且通过设置MinStiffness的值，可以控制褶皱处的尖锐程度。

#### 近期计划[](https://docs.mthreads.com#近期计划-15)

`001`

材料计算准确性，在关闭碰撞处理的情况下，可以计算出和 Vellum 完全一样的材料表现效果

`002`

进一步提高碰撞品质，可以在计算过程中增强材料大褶皱和小褶皱的对比

`003`

进一步优化性能，速度有再提高一倍的可能性

#### 已知问题[](https://docs.mthreads.com#已知问题-2)

`001`

目前一个 VeraFiber Solver 默认会创建 2G 的显存池用于碰撞修正的临时数据存储，在一个 Hip 文件中创建多个 VeraFiber Solver 可能会导致 Houdini Crash，该问题将在下一个版本中修复

# AlphaCore Beta 6.0

## VeraFiber 1.9[](https://docs.mthreads.com#verafiber-19)

#### Daily 2023 10.8[](https://docs.mthreads.com#daily-2023-108)

**VeraFiber Houdini Plugin 新增 Features**[](https://docs.mthreads.com#verafiber-houdini-plugin-新增-features-2)

`001`

全新的摩擦力模型

`002`

Collision Resolve品质改进，优化布料与物体碰撞修正过程中产生的不必要计算错误

`003`

修复 Stitch Constraint 计算bug

`004`

新增Sitffness Drop off (SOP Version Plugin Only)

`005`

提供 DOP 版本 VeraFiber **(Experimental)** ，支持 DOP 节点的数据回调，可以使用 各种 DOP 节点参与VeraFiber的解算，包括但不限于 POPWind， SOP Solver ，VEX，VOP 等常用 Houdini DOP 节点

#### 详情[](https://docs.mthreads.com#详情-27)

**全新的摩擦力模型**

**如图（上）：** VeraFiber 1.9 使用了全新的摩擦力模型，相比过去 1.8，男孩的衣服可以受到更精准的摩擦力作用紧贴肩膀不滑落。此处对比了 经过完整的 120 帧镜头动画之后，新版本的VeraFiber 男孩外衣仍旧可以保持原始T-pose状态，而在先前的1.8老版本中，镜头动画仅运行了不到 30 帧，外衣则就由于摩擦力计算失效而完全脱落

**Collision Resolve品质改进**

**如图（上）：** 改进了Collision Resolve 内核的权重计算方式，在与高速旋转物体的碰撞测试对比中，整个Collision Passes 的计算品质明显由于老版本的解算结果

**Stitch Constraint 计算错误修复**

修复了由于传参错误导致的 Stitch Constraint 强度失效问题

**DOP 版本 VeraFiber**

使用 DOP 的节点网络对整个 VeraFiber 的GPU计算调度进行了实现，并允许在VeraFiber的GPU计算过程中回调使用 DOP 和 SOP 的节点参与解算过程，实现更复杂的效果调解控制

**如图（上）：** 新版本的 VeraFiber DOP 版本可以继续使用 Houdini 自带的 POP Wind 风场节点，对 POP Wind 的 Noise 参数进行调整，Noise 效果也会直附加到 VeraFiber 的计算结果上

#### 近期计划[](https://docs.mthreads.com#近期计划-16)

`001`

进一步提高碰撞品质，可以在计算过程中增强材料大褶皱和小褶皱的对比
`002`

进一步优化性能，速度有再提高一倍的可能性
`003`

提供更多的 DOP 数据接口 （Position，Group etc Data Interface）

#### 已知问题[](https://docs.mthreads.com#已知问题-3)

`001`

DOP 数据接口暂时不支持 Position 和 Group 数据，将在后续版本提供接口
`002`

当前版本 DOP Solver 仅支持缓存 Point Cloud，不携带 Topology 信息
`003`

摩擦力强度相比 Houdini Vellum 整体作用效果偏弱，在使用VeraFiber的时候考虑使用更高强度的摩擦力系数

# AlphaCore Beta 5.3.1

## VeraFiber 1.8.1[](https://docs.mthreads.com#verafiber-181)

#### Daily 2023 8.15[](https://docs.mthreads.com#daily-2023-815)

**VeraFiber Houdini Plugin**[](https://docs.mthreads.com#verafiber--houdini-plugin)

`001`

修复 VeraFiber Houdini SOP Plugin 节点参数 Key 帧失效bug。除 Substep参数以外，其余参数均支持动画曲线设置调整。

# AlphaCore Beta 5.3

## VeraFiber 1.8[](https://docs.mthreads.com#verafiber-18)

#### Daily 2023 8.14[](https://docs.mthreads.com#daily-2023-814)

**VeraFiber Houdini Plugin 新增 Features**[](https://docs.mthreads.com#verafiber--houdini-plugin-新增-features)

`001`

提供和Vellum Constraint Property 功能类似的 VeraConstraint Property ��节点， 新增 Constraint Breaking 功能以及 Constraint Property 节点，可在解算过程中动态控制Constraint的属性以及断状态，当前版本为实验版本，我们将在 VeraFiber Beta 1.9 的版本中提供该功能的正式版本

`002`

修复曲线包裹的翻转bug，避免极端情况下曲线包裹模型出现扭转问题。`003`

优化 AniPin 过重场景负载，解算器 CacheInput 功能增加对 AniPin 数据的缓存

#### 其它[](https://docs.mthreads.com#其它)

- 改进用户体验 HDA Cache Input 功能自动回调 ReloadCache 按钮，无需2次点击

#### 近期计划[](https://docs.mthreads.com#近期计划-17)

- 持续优化碰撞检测品质，我们开发了一套对碰撞检测品质定量评估的方法，会使用该方法加快碰撞处理模块的迭代速度
- 进一步优化性能，目标相比于 VeraFiber 1.7 再提速 50% 以上
- 优化碰撞处理品质，修复碰撞检测中的假阳性存在修正导致碰撞求解爆炸的bug
- VeraFiber Houdini 插件即将支持 DOP 模式

# AlphaCore Beta 5.2

## VeraFiber 1.7[](https://docs.mthreads.com#verafiber-17)

#### Daily 2023 8.3[](https://docs.mthreads.com#daily-2023-83)

**VeraFiber 新增 Features**[](https://docs.mthreads.com#verafiber-新增-features)

`001`

优化 Collision Resolve 失败产生的数值爆炸问题。包括 AniPin 约束状态分析错误，假阳性约束剔除错误，等多处计算错误。`002`

优化了 ShockPropagation 计算错误导致的弱 Stiffness Attach (stiffness < 100) 约束的过度拉伸现象`003`

优化了风阻计算失效错误`004`

修复了DisableCollision 计算失效 bug`005`

VeraPipeline 新增毛发中心线提取 HDA

#### 详细信息[](https://docs.mthreads.com#详细信息)

**Collision Resolve**

**如图（上）** VeraFiber 1.7 版本针对角色动画在短时间内产生的大幅位移进行了多处碰撞计算优化，相对于 VeraFiber 1.6 减少了 90 % 以上的数值爆炸现象。

**WindDrag 风阻**

风阻是布料仿真中非常重要的一个特性，在现实世界中，布料受到的空气阻尼十分复杂，但在计算机世界的虚拟环境中通常是一个真空状态。所以在虚拟世界中如何模拟布料受到的空气阻尼，是布料仿真领域的一个难点

**如图（上）** 这里我们对布料进行简单的自由落体测试，测试中布料会因下落过程中受到空气阻尼而减缓下落速度。在老版本的 VeraFiber 中，存在风阻计算失败的问题 **（左）**，布料由于空气阻尼积分错误而下降过快，这会导致在复杂case中，布料难以模拟出轻柔的漂浮感，新版本的 VeraFiber 修复了这一 bug **（右）**

**VeraPipeline 毛发中心线提取更新**

**如图（上）** VeraPipeline 工具包 **Vera CenterLine** 节点更新，提供2种新的基于曲面的中心线提取方式（1）UV映射提取（2）四边面提取，输入曲面模型，输出曲线信息，范例文件 `example/Vera_CenterLine.Sample.hip`


#### 近期计划[](https://docs.mthreads.com#近期计划-18)

- 进一步优化碰撞处理计算品质

# AlphaCore Beta 4.0

## VeraFiber 1.6[](https://docs.mthreads.com#verafiber-16)

#### Daily 2023 7.20[](https://docs.mthreads.com#daily-2023-720)

#### AlphaCore 核心模块[](https://docs.mthreads.com#alphacore-核心模块)

-
**稳定性提高**-
新增错误监测模块： 新版本的 SimWorld 会对每一步计算结果进行错误信息监听，一旦检测到 Runtime 运行时错误，则迅速进行抛出异常处理，及时终止存在异常的计算，引擎稳定性相比老版本有重大提升

-
新增 SimGraph 仿真图： 完善节点操作，产品级开发全面采用 SimGraph，解耦模块（SimOP），生成单元测试


-
-
**Linux MUSA**- 集成 MUSA Toolchain muThrust 工具包，实现各类型空间加速结构（AccelTree）的 MT GPU 高性能运行

-
**Houdini Interface**- 新增 Runtime ERROR 错误信息节点同步功能


**如图（上）** 从当前版本后，AlphaCore 引擎内部所有 ERROR 信息同步至 Houdini 节点，准确描述定位问题，改善Houdini插件用户体验
2. 提供多 Houdini 版本插件发布:

- Houdini 19.5.303 (python3)
- Houdini 19.0.720 (python2)

**VeraFiber Houdini Plugin 新增Features**[](https://docs.mthreads.com#verafiber-houdini-plugin-新增features)

`001`

计算性能进一步优化，包括 ConstraintOptimization Kernel Launch 参数优化，Collision Resolve 初始化逻辑优化，Collision Detection L1 Cache 缓存命中率优化，BVHTree 构建确定性bug修复。整体优化幅，相对于 VeraFiber 1.5 度达��到**50%**以上

GPU RTX 3060

| Example Name | Frames | Primitives | Parameter | VeraFiber 1.5 | VeraFiber 1.6 | Houdini 19.5 Vellum |
|---|---|---|---|---|---|---|
| Walking | 100 | 15.3 w Triangles 90,001 + 63,452 ( Cloth & Body ) | 100 Iterations 10 Collision Passes 3 Post Collision Paases | 2 substep : 62s 4 substep : 110s | 2 substep : 39s4 substep : 64s | 2 substep : 132s 4 substep : 201s |

#### Bug 修复[](https://docs.mthreads.com#bug-修复-2)

`001`

碰撞检测准确度提高：修复了 RTriangle 在宽阶段计算过程中的剔除错误，减少了 Contact 的遗漏现象`002`

Pin约束动画跟随bug修复：修复了 AniPin 在 Substep 计算过程中由于 PrdP 插值错误导致的跟随失效错误`003`

修复了 Collision Detection Solver 的 EnableCollision 参数链接失效导致的，在关闭 Collision Detection 计算时导致的引擎 Crash bug`004`

Collision Passes 碰撞处理管线忽略质量为 0 顶点（边界条件）`005`

对 BVHTree 在构建 Hierarchy 结构时产生的确定性（Deterministic） bug 进行了修复

#### 已知问题[](https://docs.mthreads.com#已知问题-4)

`001`

ParamBlockArray 功能缺少开发者文档，不支持参数初始化以及 LogSimParameter 打印
`002`

风场节点当前版本处于禁用状态，将在 1.7 版本中重新开启

#### 近期计划[](https://docs.mthreads.com#近期计划-19)

- SOP 可编程计算管线开放：可实现在 VeraFiber 的计算过程中对 Houdini Node 的回调，如：在Substep推进的过程中，通过SOP Attribute Blur节点实现对顶点速度的圆滑处理，或使用Houdini的VOP，VEX等编程方式进行复杂效果调节
- 碰撞检测 Collision Resolve 品质进一步改进，减少穿插，抖动
- 修复 ShockPropagation 参与 Attach 约束求解导致的过度拉伸
- Wind 风阻错误修正
- MaxAcceleration 积分错误修正
- BDF2 积分器快速摩擦力支持
- 修复材料最大厚度计算错误导致的Collision Detection 结果假阳性过重错误

# AlphaCore Beta 3.5

## VeraFiber 1.5[](https://docs.mthreads.com#verafiber-15)

#### Daily 2023 5.10[](https://docs.mthreads.com#daily-2023-510)

**VeraFiber Houdini Plugin 新增Features**[](https://docs.mthreads.com#verafiber-houdini-plugin-新增features-1)

`001`

新增 ShapeMatching 布料刚体耦合计算支持`002`

场景解析速度优化：不存在的系统即为最稳定的系统，因此我们删除掉了HDA中所有时序相关的属性获取（Attach，Pin，Collider 的 PrevP），可以降低一半的场景解析时间`003`

新增 Point2Primitive (Stitch) 类型约束支持，支持布料之间的顶点 - 面约束绑定，和顶点 - 边约束绑定`004`

Houdini SOP 插件端获取并显示 AlphaCore 内核运行状态和报错信息，包括解算错误，显存运行开销，simOP计算开销统计，GPU型号`005`

新增 PBDJacobiSmooth Iteration 迭代支持，对GS 收敛不均匀的问题进行圆滑后处理`006`

新增 MaxGPUMemory 参数限制解算器的显存计算开销，当计算消耗超过该阈值时，解算器将通过前端界面提示内核运行错误信息，该参数默认大小是4G。经过多方面实验，该大小可以在**动画躯体数据无明显穿插和穿透的情况下**，满足80~100万面多层布料的正常解算（更多关于动画数据`穿插`

和`穿透`

方面的介绍请参考`VeraPipeline`

CFX角色布料仿真行业标准白皮书）`007`

所有Constraint 的 Stiffness 增加对 Compress Stiffness 的支持`008`

提供 Max Acceleration 最大加速度限定功能（**仅ImplicitEuler积分器**）

#### Bug 修复[](https://docs.mthreads.com#bug-修复-3)

`001`

修复了由于显存优化带来的 IsPinPoint 属性未分配显存就计算，最终导致引擎Crash bug`002`

修复了任意模型（非法模型）输入到解算器 Constraint 接口导致的解算器 Crash bug`003`

修复了 Attach Constraint 由于质量倒数计算错误导致的 Attach Constraint 拉伸过度的 bug`004`

修复了 HDA Dev 面板各类中间计算结果保存失效的bug，优化并减少Debug数据导出分类

**开发者工具**[](https://docs.mthreads.com#开发者工具)

`001`

AlphaCore Visual Debug Tools 提供完整的 Collision Passes Visual Debug解决方案，包括所有 Collision Detection 和 Collision Resolve 类型 simOP 计算过程的可视化

#### 文档资料[](https://docs.mthreads.com#文档资料)

`houdini/examples/VeraFiber/StitchConstraint.hip`

演示了对Vellum Stitch Constant的支持
`houdini/examples/VeraFiber/ShapeMatching.hip`

演示了对Vellum ShapeMatching 类型Constraint 的支持

#### 详细信息[](https://docs.mthreads.com#详细信息-1)

**Point2Primitive (Stitch) Constraint**

Point2Primitive (Stitch) 类型约束提供了不同精度布料之间的缝合和联动，可支持 **Point2Edge**（点-边），**Point2Triangle**（点-三角形），**Point2Quad**（点 - 四边形）的缝合和联动。约束设置方面，可以直接读取 Houdini Vellum Constraint 节点所生成的 Stitch类型约束数据并进行计算

**ShapeMatching 布料刚体交互支持**

增加GPU布料刚体交互支持，Houdini 插件版本可直接读取 Vellum Constraint 的 Shape Matching 类型约束进行求解计算

**Jacobi Smoother**

新版本 VeraFiber 在SolverType为XPBD的模式下，提供 JacobiSmooth Iteration 作为后处理迭代，以解决默认 Gauss–Seidel 迭代过程中收敛不均匀的问题。如图（上）在开启Jacobi Smooth 之后得到的更光滑的收敛效果，该参数默认为每 substep 10 次。

**Compress Stiffness 支持**

新版本的VeraFiber，对有关材料拉伸控制相关的约束（如：Attach，Distance，TriangleARAP 等）都增加了对CompressStiffness属性（压缩刚度，抗压缩）的支持。如图（上）所示，Attach 约束的 CompressStiffness（抗压缩）强度和 Stiffness（抗拉伸）强度不一样，随着AttachGeometry的翻转，布料受重力从被支撑的状翻转到被拉伸的状态，Attach Constraint 所体现出的强度也完全不一样

**Attach Constraint 支持顶点质量（Point Mass）**

新版本的Attach Constraint 支持了顶点质量属性，旧版本的Attach约束在Stiffness一样的情况下，所有的材料约束强度都一样的Bug。如图（上）所示，蓝色线条的为Attach Constraint 约束，约束强度均为 100 ，曲面黑白渐变代表了顶点质量大小，越白代表了顶点质量越大，在新版本中，质量越大的质点（越重的材料）将计算过程中越难被Attach 约束束缚

**GPU Info 计算状态查询**

Houdini Plugin 增加GPU运行状态信息保存至 Solver Detail Attribute，回放计算时可以查询当前帧的计算硬件开销状况

#### 近期计划[](https://docs.mthreads.com#近期计划-20)

`001`

Stiffness Dropoff`002`

Post Detangle`003`

SOP 可编程管线开放：支持 SOP 节点参与解算，可使用自定义 SOP 节点组，如：VEX ，VOP参与VeraFiber的计算处理

# AlphaCore Beta 3.4

## VeraFiber 1.4[](https://docs.mthreads.com#verafiber-14)

#### Daily 2023 4.21[](https://docs.mthreads.com#daily-2023-421)

**VeraFiber Houdini Plugin 新增Features**[](https://docs.mthreads.com#verafiber-houdini-plugin-新增features-2)

`001`

重构碰撞检测内核，全新碰撞检测内核：AlphaCore CollisionDetection SimOP ，模块化碰撞检测设计，使复杂场景碰撞检测显存开销降低**50%**,碰撞内核速度提速**1~3**倍，解算器整体提速**43% ~ 50%**`002`

完善CollisionDebug流程，详见`ENGINE_ReleaseNote.md`

`003`

Attachment Geometry 输出和回放速度进一步优化，对于复杂场景的Attach Geometry 回放速度可以由3FPS 提速至 24 FPS，提升解算器的 AttachGeometry IO 读取性能

**VeraPipeline 更新**[](https://docs.mthreads.com#verapipeline--更新)

`001`

VeraPipeline 主节点 新增SimRayRender功能，通过path属性规则，自动创建建模（SimAsset）到高模（RenderAsset）映射节点组。`002`

毛发Pipeline模板录屏：提供最新毛发Pipeline教学录屏`003`

GradientCurve.hda：新增支持Pscale在曲线解算设置可视化和ramp调节

**用户体验改进**[](https://docs.mthreads.com#用户体验改进)

`001`

VeraFiber SOP HDA 新增版本信息提示

**开发者工具**[](https://docs.mthreads.com#开发者工具-1)

`001`

AlphaCore Geometry IO 升级类型兼容，新增对于Int8，Int64的数据对接，新增AlphaCore System Properties 对接包括但不限于：Contact类型Buffer，BVHNode，AABB类型Buffer的Houdini可视化

**Bug 修复**[](https://docs.mthreads.com#bug-修复-4)

`001`

修复了 VeraFiber 在复杂场景中 Contact 数量过导致的 Crash bug`002`

修复 Vera Pipeline 布料模板生成时，mask属性未自动匹配到 attach 节点的强度上的 bug

**近期计划**[](https://docs.mthreads.com#近期计划-21)

`001`

新增ShapeMatching布料刚体耦合计算支持`002`

新增 Stiffness Dropoff`003`

新增 Stitch 类型约束支持`004`

允许Houdini插件端获取硬件内核运行数据，包括显存开销，显卡型号

**详情**[](https://docs.mthreads.com#详情-28)

**1.4 性能测试 Example**[](https://docs.mthreads.com#14-性能测试-example)

GPU RTX 3060

| Example Name | Frames | Primitives | Parameter | VeraFiber 1.3 | VeraFiber 1.4 | Houdini 19.5 Vellum |
|---|---|---|---|---|---|---|
| Kicking | 120 | 12.3 w Triangles 61,798 + 62,730 ( Cloth & Body ) | 100 Iterations 4 Collision Passes 3 Post Collision Paases | 2 substep : 161 4 substep : 263s | 2 substep : 74s4 substep : 132s | 2 substep : 184s 4 substep : 212s |

# AlphaCore Beta 3.3.1

## VeraFiber 1.3.1[](https://docs.mthreads.com#verafiber-131)

#### Daily 2023 4.12[](https://docs.mthreads.com#daily-2023-412)

#### Bug 修复[](https://docs.mthreads.com#bug-修复-5)

`001`

修复了在Release版本中，Kernel Logger申请显存过大导致解算器Crash，效率陡降的bug`002`

修复了Houdini 插件端，日志输出路径被第一个创建的VeraFiber节点锁死的bug`003`

修复了AXC文件格式，无法解析特殊数据类型Property导致引擎 Crash 的bug。

# AlphaCore Beta 3.3

## VeraFiber 1.3[](https://docs.mthreads.com#verafiber-13)

#### Daily 2023 4.10[](https://docs.mthreads.com#daily-2023-410)

**Houdini Plugin 新增Features**[](https://docs.mthreads.com#houdini-plugin-新增features)

-
`001`

改进 VeraFiber 场景解析速度和解算速度：Attachment Geometry 解析速度比Beta 1.2 版本**提速15倍**,在对场景Cache input的时候，可以大幅缩短缓存输出时间，对于简单的角色场景，甚至可以做到无需缓存。解算速度相比上一个版本Beta 1.2 提速**20%**，相比相比 Beta 1.1 提速超过**30%**以上 -
`002`

全方位支持 Pin 约束，包括了Vellum Constraint 中 Pin to Animation 参数组的全套参数，和Pin类型约束 -
`003`

VeraPipeline 提供毛发流程自动节点创建功能，包括：自动毛发Rig节点创建，中心线提取等功能模块 -
`004`

提供快速摩擦力计算功能

**用户体验改进**[](https://docs.mthreads.com#用户体验改进-1)

`001`

修复框选VeraFiber 解算器状态时，解算器仍然处于解算状态的bug，该问题解决后，可以实现拖动时间轴滑块在viewport显示动画表演的状态下，对解算器参数进行key帧处理。`002`

暴露 Sim Cache 缓存池大小设置，并对缓存回放进行深度优化，默认缓存池大小为 5G,对于相同资产的计算结果缓存的时间帧长度是Vellum的3倍以上`003`

提供Houdini packed Geometry 安全检查，如果强行输入未 unpack 的geometry，VeraFiber Solver 将提示报错信息

#### Bug 修复[](https://docs.mthreads.com#bug-修复-6)

`001`

修复了**ctxNormal**属性记录错误的bug，老版本的**ctxNormal**属性记录每一次 CollisionResolve 的修正幅度（1次CollisionResolve包含了多次迭代），而新版本的**ctxNormal**记录的是一个Substep内所有的 CollisionResolve 修正幅度，这样会导致做单次CollisionPasses Visualization的时候，**ctxNormal**的幅度并不能代表当前单次CollisionPasses的修正情况

**其它**[](https://docs.mthreads.com#其它-1)

`001`

增加 Debug CheckPoint :`beforceConstraintProjection`

和`afterConstraintProjection`


**已知问题**[](https://docs.mthreads.com#已知问题-5)

- 当前版本AniPin会参与碰撞

**详细信息**[](https://docs.mthreads.com#详细信息-2)

- 快速摩擦力算法

提供

**近期计划**[](https://docs.mthreads.com#近期计划-22)

`001`

SOP 可编程管线开放：支持 SOP 节点参与解算，可使用自定义 SOP 节点组，如：VEX ，VOP参与VeraFiber的计算处理`002`

提供 Max Acceleration 最大加速度限定功能`003`

增加动画缓存非线性变速预处理节点

# AlphaCore Beta 3.2

## VeraFiber 1.2[](https://docs.mthreads.com#verafiber-12)

#### Daily 2023 3.16[](https://docs.mthreads.com#daily-2023-316)

**新增Features**[](https://docs.mthreads.com#新增features)

`001`

改进 Solver Collision Resolve 效率，在效果不变的情况下可以提速15%~20%`002`

开放节点操作功能，提供风场控制，及可视化相关节点`003`

VeraFiber SOP HDA �节点提供重力可视化 Handle`004`

全新的风场控制模块（持续迭代升级）`005`

新增 DisableCollision 属性，忽略自定义区域碰撞碰撞检测

#### 详细信息[](https://docs.mthreads.com#详细信息-3)

- 节点操作支持

当前版本开放了VeraFiber SOP HDA 解算器内部的节点操作支持，在VeraFiber SOP Plugin 内部添加AlphaCore节点组实现自定义变成控制

#### 文档资料[](https://docs.mthreads.com#文档资料-1)

`houdini/examples/VeraFiber/DisableCollision.hip`

演示通过设置DisableCollision属性忽略三角形碰撞
`houdini/examples/VeraFiber/WindOperator.hip`

演示全新的风场和可视化功能操作

#### 近期计划[](https://docs.mthreads.com#近期计划-23)

- 性能持续优化
- Post Detangle，在已经发生穿插的区域，通过全局穿插分析，进行穿模后处理修正
- ARAP 材料力学约束，和Pin 类型约束的全面适配
- 摩擦力支持

# AlphaCore Beta 3.1

## VeraFiber 1.1[](https://docs.mthreads.com#verafiber-11)

#### Daily 2023 2.28[](https://docs.mthreads.com#daily-2023-228)

**新增Features**[](https://docs.mthreads.com#新增features-1)

`001`

改进 HDA 缓存播放效率（使用Input Cache的情况下 20万面角色可以达到 120 FPS 以上的回放速度）`002`

新增 Shock Propagation 功能支持`003`

VeraPipeline 改进升级`004`

新增 Cache Scene Input 功能，可以在VeraFiber上对几个input的Geometry序列进行（.bgeo）缓存操作

**修复bug**[](https://docs.mthreads.com#修复bug)

`005`

修复了 Collider 输入点数为0的Geometry时候 solver crash的问题`006`

修复了输入的 ClothAsset 在解算过程中顶点数量发生变化时候的 solver crash问题。（例如：在解算过程中对上游节点进行了subdivision，remesh等改变拓扑的误操作，该问题出现概率较低）`007`

修复了HDA中SIM Cache 起始帧为 1 的bug`008`

修复了VeraFiber Houdini SOP Solver 上 GroundPosition 设置失效的bug

**其它**[](https://docs.mthreads.com#其它-2)

`009`

完善 VeraFiber Houdini Plugin Runtime运行日志管理`010`

修改 Houdini HDK 接口 Geometry H2A 的内存分配方式（批量PrimitiveCopy），大幅优化了复杂布料模拟（20w 三角形以上资产）的第一帧初始化时间

**详细信息**[](https://docs.mthreads.com#详细信息-4)

- 新增功能 Shock Propagation

VeraFiber Solver 解算器面板新增 Shock Propagation Scale 参数，该参数用于调节布料在碰撞过程中产生拉伸的修正幅度。在布料和障碍物的碰撞过程中，解算器会根据该参数的大小优先修正碰撞区域的顶点拉伸错误

- 新增功能 一键 Cache Scene Input

VeraFiber Solver Houdini HDA 增加一键输出Input缓存功能，通过该功能将所有输入解算器的 Geometry 序列在解算前缓存到了硬盘上，确保解算器可以满负运行，无前置计算（Houdini cook）等待时间

点击 Save To Disk (Attach & Collider)按钮缓存输入，完成缓存输出后，需要点击 Reload Cache 按钮，否则有可能提示 `Error: [VeraFiber ERROR] Input Coliider Point Number ERROR`

，该报错说明VeraFiber HDA Input的 Collision Object 的顶点数，和从硬盘上读取到已缓存 Geometry 的顶点数不同，属于正常错误提示

- VeraPipeline 改进升级
- VeraPipeline 优化input,anicache采用一个端口，更根据renderAsset 的path 信息split AniCloth和Anibody信息
- unpack和convert发生在每一个包裹之后，保证remesh 解算模型修改方便和包裹和后续pin约束加入
- 修复AniCloth 和 Anibody的包裹错误，并且留有手动操作的余地


**下一个版本计划**[](https://docs.mthreads.com#下一个版本计划)

- 开放节点操作，和全新的风场可视化系统

# AlphaCore Beta 3.0

## VeraFiber 1.0[](https://docs.mthreads.com#verafiber-10)

#### Daily 2023 2.17[](https://docs.mthreads.com#daily-2023-217)

#### 工具组件[](https://docs.mthreads.com#工具组件)

`001`

Houdini 原生插件，可以在Houdini中直接链接Vellum Constraint节点组进行GPU布料解算`002`

Unreal 接口，可以将Houdini 中边界好的Vera Asset布料解算资产导入至Unreal引擎进行解算，和动画替换`003`

VeraPipeline 模块，提供基于 Houdini 的角色布料毛发解算流程节点的自动创建

#### 文档资料[](https://docs.mthreads.com#文档资料-2)

`001`

20分钟完整教学录像 + 范例文件`houdini/examples/VeraFiber/Vera_Dress.Sample.hip`

（VeraFiber for Houdini 101）`002`

VeraFiber 用户手册

#### Feature List[](https://docs.mthreads.com#feature-list)

##### Constraint Dynamics 约束动力学[](https://docs.mthreads.com#constraint-dynamics-约束动力学)

- 提供基于Constraint Dynamics的布料毛发模拟效果。支持基于XPBD数值计算方法的 Distance，Bend（Strain Base Dynamic），Attach，Hair（BendTwist，Orientation）的约束动力学求解。
- 提供布料空气动力学功能，可以通过风阻系数设置，实现布料在空气中模拟产生自然的摆动的效果。
- 提供Gauss-Seidel，Jacobi（Smooth Iteration）2种求解方法的混合方案

##### Collision Respond 碰撞反应[](https://docs.mthreads.com#collision-respond-碰撞反应)

- 支持基于GPU的快速碰撞检测方法，速度是Houdini Vellum的 4倍以上，随着计算面数的提高，加速比更加明显
- 支持 Shock Propagation 方法，最大程度�保证布料不和躯体碰撞物产生穿插

##### Houdini Interface[](https://docs.mthreads.com#houdini-interface)

- 支持Houdini SOP Vellum Constraint 数据对接，可使用Vellum节点组进行约束构建，并用 VeraFiber SOP Plugin 读取约束信息进行布料毛发仿真
- 支持Houdini SIM Cache 功能，支持解算缓存的内存实时播放

#### 已知问题[](https://docs.mthreads.com#已知问题-6)

- Houdini 接口IO开销较大，目前Houdini Plugin 版本VeraFiber 运行速度小于 AlphaCore 独立程序（大约慢了50%），待后续版本完善Houdini接口性能
- 目前不支持 Vellum Constraint 系列的 pin 类型约束
- 暂时不开放节点编辑操作，和VOP计算图调用模块
- 多层布料容易在手肘，腋下极端挤压的过程中产生穿插，后续会推出应对腋下手肘压缩时防止穿模的特殊处理模块
- 由于准备时间有限，提供的教学录像背景噪音较大，演示范例较为简单，会再后续二次彩排录制更流畅版本

#### 软硬件要求[](https://docs.mthreads.com#软硬件要求)

- nVIDIA GTX 1080 以上 GPU ，CUDA 驱动 11.5 以上版本
- Houdini 19.5.303

#### 近期计划[](https://docs.mthreads.com#近期计划-24)

- 性能优化，目标下一个大版本提速一倍
- 进一步解决碰撞穿插问题，使用更好的碰撞求解线性系统
- ARAP 材料力学约束，和Pin 类型约束的全面适配
- 开放节点操作，和全新的风场可视化系统

# AlphaCore Beta 2.2

## Vera Pipeline Beta 1.0[](https://docs.mthreads.com#vera-pipeline-beta-10)

#### Daily 2022 11.18[](https://docs.mthreads.com#daily-2022-1118)

提供 Vera Pipeline 一键 Houdini CFX 流程搭建工具包

如图（上）：使用该工具包可以在Houdini 中全自动搭建 CFX 角色动画解算制作流程。

#### VeraPipeline_v1.mp4[](https://docs.mthreads.com#verapipeline_v1mp4)

相关更详细资料，可以阅读帮助文档`doc/VeraPipeline.md`

，和额外提供的example 范例教学录像：`VeraPipeline_v1.mp4`