source: https://docs.opencloudos.org/OC9/cloud/Import-OpenCloudOS9-to-Ali-Cloud/

# 导入镜像到阿里云

### 1. 创建存储桶

- 首先进入阿里云对象存储 OSS
- 选择进入管理控制台
- 然后选择创建 Bucket
- 创建名为 opencloudos 的 Bucket（可按需自定义其他配置，避免不必要的计费）
- 创建成功如下图所示：

### 2. 上传 OpenCloudOS 9.2 qcow2 镜像

- 上传镜像
- 上传成功后拷贝文件 URL 备用

### 3. 导入镜像

- 搜索并点击云服务器 ECS
- 点击镜像
- 点击导入镜像
- 粘贴 URL 并设置镜像名称
- 等待导入完成

### 4. 切换至导入的系统

- 返回云服务器 ECS 并选择一个实例，停止该实例
- 实例停止后，选择更换操作系统
- 选择更换操作系统方式
- 选择自定义镜像并创建密钥对
- 创建密钥对并保存
- 确认后等待实例启动

### 5. 连接云服务器

- 通过 Workbench 远程连接
- 登录成功显示（用户名、密码均为 opencloudos）
- 通过 VNC 远程连接
- 登录成功显示（用户名、密码均为 opencloudos）