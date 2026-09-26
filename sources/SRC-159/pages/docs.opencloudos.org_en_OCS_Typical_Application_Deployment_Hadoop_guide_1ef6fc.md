source: https://docs.opencloudos.org/en/OCS/Typical_Application_Deployment/Hadoop_guide/

# Hadoop使用指南

Apache™ Hadoop® 项目开发用于可靠、可扩展的分布式计算的开源软件。 Apache Hadoop 软件库是一个框架，允许使用简单的编程模型跨计算机集群分布式处理大型数据集。 它旨在从单个服务器扩展到数千台机器，每台机器都提供本地计算和存储。 该库本身旨在检测和处理应用层的故障，而不是依靠硬件来提供高可用性，因此可以在计算机集群之上提供高可用性服务，而每台计算机都可能容易出现故障。

## 架构支持

3.3.4及之后的版本官方支持aarch64

## 运行依赖

必备依赖：

```
dnf install java-headless openssh-client
```


## 下载及解压

https://dlcdn.apache.org/hadoop/common/ 例如https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz src.tar.gz为源码包，tar.gz为预编译包，一般下载预编译包即可 示例命令：

```
wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz
tar axvf hadoop-3.3.4.tar.gz
```


## 运行测试

```
cd hadoop-3.3.4
export JAVA_HOME=/usr/lib/jvm/jre-11/
bin/hadoop
```


## 单节点测试

```
mkdir input
cp etc/hadoop/*.xml input
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.4.jar grep input output 'dfs[a-z.]+'
cat output/*
```


## 分布式测试

请参考官方文档https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html