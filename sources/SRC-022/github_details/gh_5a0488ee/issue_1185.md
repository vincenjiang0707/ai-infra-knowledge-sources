# [Issue #1185] Some question about the topo.xml dumped by RCCL

source: https://github.com/ROCm/rccl/issues/1185
state: closed | updated: 2024-06-25T17:39:27Z
labels: 

## 正文

Hi dear developer,
I have one question about the topo.xml dumped by RCCL, the following is the topo.xml from RCCL, and I draw a topo picture according the topo.xml

```
<system version="2">
  <cpu numaid="3" affinity="00000000,ff000000" arch="x86_64" vendor="AMD" familyid="159" modelid="2">
    <pci busid="0000:31:00.0" class="0x060400" vendor="0x1000" device="0xc010" subsystem_vendor="0x1000" subsystem_device="0xa096" link_speed="16.0 GT/s PCIe" link_width="16">
      <pci busid="0000:33:00.0" class="0x060400" vendor="0x1000" device="0xc010" subsystem_vendor="0x1000" subsystem_device="0xa096" link_speed="16.0 GT/s PCIe" link_width="16">
        <pci busid="0000:35:00.0" class="0x060400" vendor="0x1d94" device="0x23b7" subsystem_vendor="0x0000" subsystem_device="0x0000" link_speed="16.0 GT/s PCIe" link_width="16">
          <pci busid="0000:37:00.0" class="0x038000" vendor="0x1d94" device="0x55b7" subsystem_vendor="0x1d94" subsystem_device="0x55b7" link_speed="16.0 GT/s PCIe" link_width="16">
            <gpu dev="0" sm="90" gcn="21943" arch="38911" rank="0" gdr="1"/>
          </pci>
        </pci>
        <pci busid="0000:38:00.0" class="0x060400" vendor="0x1d94" device="0x23b7" subsystem_vendor="0x0000" subsystem_device="0x0000" link_speed="16.0 GT/s PCIe" link_width="16">
          <pci busid="0000:3a:00.0" class="0x038000" vendor="0x1d94" device="0x55b7" subsystem_vendor="0x1d94" subsystem_device="0x55b7" link_speed="16.0 GT/s PCIe" link_width="16">
            <gpu dev="1" sm="90" gcn="21943" arch="38911" rank="1" gdr="1"/>
          </pci>
        </pci>
      </pci>
      <pci busid="0000:3b:00.0" class="0x060400" vendor="0x1000" device="0xc010" subsystem_vendor="0x1000" subsystem_device="0xa096" link_speed="16.0 GT/s PCIe" link_width="16">
        <pci busid="0000:3d:00.0" class="0x060400" vendor="0x1d94" device="0x23b7" subsystem_vendor="0x0000" subsystem_device="0x0000" link_speed="16.0 GT/s PCIe" link_width="16">
          <pci busid="0000:3f:00.0" class="0x038000" vendor="0x1d94" device="0x55b7" subsystem_vendor="0x1d94" subsystem_device="0x55b7" link_speed="16.0 GT/s PCIe" link_width="16">
            <gpu dev="2" sm="90" gcn="21943" arch="38911" rank="2" gdr="1"/>
          </pci>
        </pci>
      </pci>
      <pci busid="0000:40:00.0" class="0x060400" vendor="0x1000" device="0xc010" subsystem_vendor="0x1000" subsystem_device="0xa096" link_speed="16.0 GT/s PCIe" link_width="16">
        <pci busid="0000:43:00.0" class="0x060400" vendor="0x1d94" device="0x23b7" subsystem_vendor="0x0000" subsystem_device="0x0000" link_speed="16.0 GT/s PCIe" link_width="16">
          <pci busid="0000:45:00.0" class="0x038000" vendor="0x1d94" device="0x55b7" subsystem_vendor="0x1d94" subsystem_device="0x55b7" link_speed="16.0 GT/s PCIe" link_width="16">
            <gpu dev="3" sm="90" gcn="21943" arch="38911" rank="3" gdr="1"/>
          </pci>
        </pci>
        <pci busid="0000:42:00.0" class="0x020000" vendor="0x15b3" device="0x1021" subsystem_vendor="0x15b3" subsystem_device="0x0022" link_speed="16.0 GT/s PCIe" link_width="16">
          <nic>
            <net name="mlx5_0" dev="0" speed="200000" port="1" latency="0.000000" guid="0x92db980003c288a0" maxconn="131072" gdr="1"/>
            <net name="mlx5_1" dev="1" speed="200000" port="2" latency="0.000000" guid="0x92db980003c288a0" maxconn="131072" gdr="1"/>
          </nic>
        </pci>
      </pci>
    </pci>
  </cpu>
  <cpu numaid="7" affinity="ff000000,00000000" arch="x86_64" vendor="AMD" familyid="159" modelid="2">
    <pci busid="0000:b1:00.0" class="0x060400" vendor="0x1000" device="0xc010" subsystem_vendor="0x1000" subsystem_device="0xa096" link_speed="16.0 GT/s PCIe" link_width="16">
      <pci busid="0000:b3:00.0" class="0x060400" vendor="0x1000" device="0xc010" subsystem_vendor="0x1000" subsystem_device="0xa096" link_speed="16.0 GT/s PCIe" link_width="16">
        <pci busid="0000:b5:00.0" class="0x060400" vendor="0x1d94" device="0x23b7" subsystem_vendor="0x0000" subsystem_device="0x0000" link_speed="16.0 GT/s PCIe" link_width="16">
          <pci busid="0000:b7:00.0" class="0x038000" vendor="0x1d94" device="0x55b7" subsystem_vendor="0x1d94" subsystem_device="0x55b7" link_speed="16.0 GT/s PCIe" link_width="16">
            <gpu dev="4" sm="90" gcn="21943" arch="38911" rank="4" gdr="1"/>
          </pci>
        </pci>
        <pci busid="0000:b8:00.0" class="0x060400" vendor="0x1d94" device="0x23b7" subsystem_vendor="0x0000" subsystem_device="0x0000" link_speed="16.0 GT/s PCIe" link_width="16">
          <pci busid="0000:ba:00.0" class="0x038000" vendor="0x1d94" device="0x55b7" subsystem_vendor="0x1d94" subsystem_device="0x55b7" link_speed="16.0 GT/s PCIe" link_width="16">
            <gpu dev="5" sm="90" gcn="21943" arch="38911" rank="5" gdr="1"/>
          </pci>
        </pci>
      </pci>
      <pci busid="0000:bb:00.0" class="0x060400" vendor="0x1000" device="0xc010" subsystem_vendor="0x1000" subsystem_device="0xa096" link_speed="16.0 GT/s PCIe" link_width="16">
        <pci busid="0000:bd:00.0" class="0x060400" vendor="0x1d94" device="0x23b7" subsystem_vendor="0x0000" subsystem_device="0x0000" link_speed="16.0 GT/s PCIe" link_width="16">
          <pci busid="0000:bf:00.0" class="0x038000" vendor="0x1d94" device="0x55b7" subsystem_vendor="0x1d94" subsystem_device="0x55b7" link_speed="16.0 GT/s PCIe" link_width="16">
            <gpu dev="6" sm="90" gcn="21943" arch="38911" rank="6" gdr="1"/>
          </pci>
        </pci>
        <pci busid="0000:c0:00.0" class="0x020000" vendor="0x15b3" device="0x1021" subsystem_vendor="0x15b3" subsystem_device="0x0022" link_speed="16.0 GT/s PCIe" link_width="16">
          <nic>
            <net name="mlx5_4" dev="4" speed="200000" port="1" latency="0.000000" guid="0xc2db980003c288a0" maxconn="131072" gdr="1"/>
            <net name="mlx5_5" dev="5" speed="200000" port="2" latency="0.000000" guid="0xc2db980003c288a0" maxconn="131072" gdr="1"/>
          </nic>
        </pci>
      </pci>
      <pci busid="0000:c1:00.0" class="0x060400" vendor="0x1000" device="0xc010" subsystem_vendor="0x1000" subsystem_device="0xa096" link_speed="16.0 GT/s PCIe" link_width="16">
        <pci busid="0000:c3:00.0" class="0x060400" vendor="0x1d94" device="0x23b7" subsystem_vendor="0x0000" subsystem_device="0x0000" link_speed="16.0 GT/s PCIe" link_width="16">
          <pci busid="0000:c5:00.0" class="0x038000" vendor="0x1d94" device="0x55b7" subsystem_vendor="0x1d94" subsystem_device="0x55b7" link_speed="16.0 GT/s PCIe" link_width="16">
            <gpu dev="7" sm="90" gcn="21943" arch="38911" rank="7" gdr="1"/>
          </pci>
        </pci>
      </pci>
    </pci>
  </cpu>
  <cpu numaid="5" affinity="0000ff00,00000000" arch="x86_64" vendor="AMD" familyid="159" modelid="2">
    <pci busid="0000:91:00.0" class="0x020000" vendor="0x15b3" device="0x1015" subsystem_vendor="0x15b3" subsystem_device="0x0102" link_speed="8.0 GT/s PCIe" link_width="8">
      <nic>
        <net name="mlx5_2" dev="2" speed="10000" port="1" latency="0.000000" guid="0xa1cd5000031f61e8" maxconn="131072" gdr="1"/>
        <net name="mlx5_3" dev="3" speed="10000" port="2" latency="0.000000" guid="0xa1cd5000031f61e8" maxconn="131072" gdr="1"/>
      </nic>
    </pci>
  </cpu>
</system>
```

![图片](https://github.com/ROCm/rccl/assets/145751038/b4a37630-d117-4da1-b750-b5edca010c0b)

My question is:
(1) The pci node colsed to the gpu node represents the GPU right? How about the other layer pci nodes? Are they represent the PCIe swithch? If so, are these PCIe switches physical or logical?
(2) From the topo.xml, can  every two GPUs use peer-to-peer with HSA_FORCE_FINE_GRAIN_PCIE=1? Suppose the CPUs are connected with XGMI.

Thank you.

## 评论 (4)

### arkhadem · 2024-06-12

How did you draw the topo picture from the xml file?

### corey-derochie-amd · 2024-06-12

@shanleo1986 I've polled the team, and this is my current understanding:

1. The pci node containing the gpu node represents the GPU. Only one gpu node should ever appear in these leaf pci nodes. As far as we are aware, the hierarchy is generated by traversing the system's device file, so the switches should *not* be logical.
2. HSA_FORCE_FINE_GRAIN_PCIE=1 is no longer needed on or after ROCm 5.7.

(I am also interested in what tool you used to create your topo picture.)

### shanleo2024 · 2024-06-13

Hi @corey-derochie-amd @arkhadem 
Thank you for your kind response, it is very useful for me.
There is no tool to creat the topo picture automatically, I just draw the picture using visio according my understanding.


### shanleo2024 · 2024-06-13

Hi @corey-derochie-amd @arkhadem 
Thank you for your kind response, it is very useful for me.
There is no tool to creat the topo picture automatically, I just draw the picture using visio according my understanding.

