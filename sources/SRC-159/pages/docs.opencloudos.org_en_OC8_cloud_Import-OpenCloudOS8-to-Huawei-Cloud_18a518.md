source: https://docs.opencloudos.org/en/OC8/cloud/Import-OpenCloudOS8-to-Huawei-Cloud/

# 导入镜像到华为云

### 1. 创建存储桶

- 首先进入华为云对象存储服务 OBS
- 然后选择右上方创建桶
- 创建名为 opencloudos 的存储桶（可按需自定义其他配置，避免不必要的计费）

### 2. 上传 OpenCloudOS 8.8 qcow2 镜像

### 3. 创建私有对象

- 在镜像服务中选择导入私有镜像
- 提交配置
- 导入成功

### 4. 切换至私有系统

- 返回云服务器 ECS 选择切换操作系统
- 选择上述创建的私有对象，设置 root 用户密码
- 选择同意切换系统
- 至此，OpenCloudOS 8.8 已导入成功

### 5. 连接云服务器

- 在远程连接中选择 vnc 登录
- 登录成功