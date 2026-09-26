# [Issue #9259] can not deregister UcpMemory immediately

source: https://github.com/openucx/ucx/issues/9259
state: closed | updated: 2026-01-16T02:08:37Z
labels: Bug

## 正文

### Describe the bug
I am using ucx 1.14.1 to build my application. However, I am unable to immediately deregister memory using `UcpMemory.deregister()`. Instead, the UcpMemory is deregistered when the application finishes executing.

For example, when i run the following code, which register UcpMemory and then deregister it, the output is :
```
before memory map: 2: mlx5_bond_0: pd 4 cq 9 qp 5 cm_id 0 mr 5 ctx 1 
after memory map: 2: mlx5_bond_0: pd 4 cq 9 qp 5 cm_id 0 mr 6 ctx 1 
after close: 2: mlx5_bond_0: pd 4 cq 9 qp 5 cm_id 0 mr 6 ctx 1 
```
the num of mr is still 6 after `ucpMemory.deregister()`.

Once the program is finished, i noticed that the UcpMemory is deregistered:
```
[root@ecs ~]# rdma res show
2: mlx5_bond_0: pd 3 cq 3 qp 3 cm_id 0 mr 0 ctx 0 
```

```java
public class Test extends CommunicationDemo{
    public static void main(String[] args) throws InterruptedException, IOException {
        initializeArguments(args);
        createContextAndWorker();

        System.out.println("before memory map: "+showRDMAResources());
        UcpMemory ucpMemory = context.memoryMap(
                new UcpMemMapParams()
                        .allocate()
                        .setLength(1029392));
        System.out.println("after memory map: "+showRDMAResources());
        ucpMemory.deregister();
        System.out.println("after close: "+showRDMAResources());


        Thread.sleep(3 * 60 * 1000);
        closeResources();
    }

    public static String showRDMAResources() {
        String line = null;
        try {
            Process process = Runtime.getRuntime().exec("rdma res show");

            process.waitFor();

            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            line = reader.readLine();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return line;
    }
}
```


## 评论 (1)

### yosefe · 2023-07-31

UCX caches memory registrations until the memory is released (by munmap/madvise/..) or until ucp_context is destroyed.
This behavior amortized the cost of memory registrations during runtime.
In version 1.14.1, it's possible to limit the number of memory registrations using these variables:
```
$ ucx_info -fc |grep IB_RCACHE_MAX -B 6
#
# Maximal number of regions in the registration cache
#
# syntax:    unsigned long: <number>, "inf", or "auto"
# inherits:  UCX_RCACHE_MAX_REGIONS
#
UCX_IB_RCACHE_MAX_REGIONS=inf
--
#
# Maximal total size of registration cache regions
#
# syntax:    memory units: <number>[b|kb|mb|gb], "inf", or "auto"
# inherits:  UCX_RCACHE_MAX_SIZE
#
UCX_IB_RCACHE_MAX_SIZE=inf
```
