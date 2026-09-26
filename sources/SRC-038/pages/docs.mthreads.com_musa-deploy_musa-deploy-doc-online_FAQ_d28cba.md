source: https://docs.mthreads.com/musa-deploy/musa-deploy-doc-online/FAQ

# FAQ

## 常见问题[](https://docs.mthreads.com#常见问题)

-
如果安装 musa-deploy 包时报网络错误，如下图所示，该如何解决？


可尝试通过指定 pip 清华源来解决，解决方法：sudo pip install musa-deploy -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple -
在部署多机 musa 基础环境时，如何判断基础 musa 环境部署是否正常？


需要关注输出 log，如下图： 如果某台服务器对应的 log 中，没有包含类似`docker exec -it musa_deploy_vllm_musa_base`

的日志，说明这台服务器可能部署 musa 基础环境异常，需要登陆这台服务，手动使用 musa-deploy 工具检查原因并部署 musa 环境。 -
多机部署满血版 deepseek 时，如何查看各个 task 状态？


常用的查看命令如下所示。注意，如果是单机部署，下面这些查看命令是不需要的。# 在主节点执行，即hostfile第一行ip对应的服务器执行# 查看docker swarm集群包含哪些节点docker node ls# 查看docker swarm集群启动task的状态docker service ls# 查看docker swarm集群中指定task的启动参数等信息，‘deepseek-r1-671b_task2’可以从'docker service ls'查看到docker service inspect deepseek-r1-671b_task2# 查看docker swarm集群中指定task对应容器的状态docker service ps --no-trunc deepseek-r1-671b_task2 -
多机部署满血版 deepseek 时，执行

`sudo musa-deploy-ansible --hostfile hostfile --init-cluster`

初始化集群失败，如下图所示： 请执行`sudo musa-deploy-ansible --hostfile hostfile --reset-cluster`

清除集群配置之后再初始化集群 -
多机部署满血版 deepseek 时，拉起 4/5 机推理服务失败，如下图所示： 没有初始化集群，对应执行

`docker node ls`

没有集群节点信息。 请执行`sudo musa-deploy-ansible --hostfile hostfile --init-cluster`

再尝试重新拉起推理服务。 -
多机部署满血版 deepseek 时，拉起推理服务没有报错，但是查看集群服务, 有些副本（replicas）运行异常： 如上图所示，可以进一步定位某个服务的任务运行状态（失败原因通常在任务里）：

docker service ps deepseek-r1-671b_task1可以看出，是由于目录映射配置错误，导致副本未能成功运行。具体来说，宿主机上并不存在

`/mnt/data/vllm`

目录，而推理服务的启动命令中使用了该路径进行映射，这是人为制造的异常场景，用于演示。

目前，启动推理服务时不会自动校验容器参数的合法性。因此，即便日志未报错，若通过`docker service ls`

发现副本运行失败，往往是启动参数配置错误，重点排查 -v（挂载目录）和 --model-path（容器内模型路径）等关键参数。 -
多机部署满血版 deepseek 时，初始化集群失败 执行

`sudo musa-deploy-ansible --hostfile hostfile --init-cluster`

失败，报错如图： 检验每台节点的`/etc/docker/daemon.json`

配置，将`"live-restore": true`

更改为`"live-restore": false`

。保存并退出后，执行`sudo systemctl restart docker`

重启 docker 服务。 -
拉起 torch_musa 容器时，执行

`sudo musa-deploy --demo torch_musa -f`

失败，检查发现驱动加载失败，报错如图： 请先执行`sudo musa-deploy -u driver`

卸载加载失败的驱动，再执行`sudo musa-deploy --demo torch_musa`

，执行过程会安装对应驱动并提示重启，请输入`y`

重启，重新连接后再执行上一条命令。