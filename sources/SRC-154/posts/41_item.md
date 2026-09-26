# item

source: https://news.ycombinator.com/item?id=49824864

There are roughly 3 ways to give a KVM guest a GPU.

1) VFIO passthrough: host binds entire GPU to guest as PCI device, which only allows one VM to use the GPU, thus you sacrifice your host display too (unless you fallback to integrated graphics on cpu etc). Strongest isolation because host kernel module driver not involved.

2) virtio-gpu: guest sees paravirtual GPU and loads virgl/venus mesa driver which serializes graphics API calls and replays them on the host driver. This allows multiple VMs to use the GPU, but performance overhead can be significant, and guests can’t practically leverage lower level primitives eg NVENC without paying price of CPU readback.

3) virtio-nvgpu (this repo): guest loads standard NVIDIA user mode driver (closed source), a fake /dev/nvidia* kernel module copies ioctl bytes + handle onto queue for host kernel mode driver to execute. This also allows multiple VMs to use a GPU, but is near native speed due to low overhead. Unfortunately the tradeoff is this project has the weakest isolation, eg every guest ioctl is forwarded to the host by default, the VMM holds read/write FDs, no seccomp/caps/allowlist. With respect to There is basically no GPU related security measures here, the exposure is the same as running multiple processes using the GPU with no VM. Only caveat is these guests can’t drive a physical display, so there is some restriction of surface area but it feels incidental rather than intentional in this case.

Anyways this is a tough problem OP, I don’t want to discourage you.

Without hardware/driver support for isolation (MIG) on consumer grade NVIDIA GPUs, it won’t be possible to solve this properly for a long time.

Also a factor is that NVIDIA has no open Mesa driver to support a native context approach (guest owns GPU command buffers, host maps them) like we have for AMD/Intel.

If I remember correctly, the idea is that you have a physical GPU and you split its memory (with, eventually, time-budget) to create multiple virtual GPUs, which can then be associated with a KVM guest and use by it

A week or so ago when I stumbled on this he at least seemed to be clear about the potential security implications, which gave me pause. But it doesn't seem any worse than just running software on your main OS which is what most people do. Sure, it's DoA for a hypervisor in a data center but that isn't the only use case out there.

What kinds of things can a guest running undesirably applications (viruses, malware, LLM escaping a sandbox, etc) get up to with shared GPU access?

What is the state of virtio-gpu these days? I have a system76 "pang14" (Ryzen 7 7840U laptop), is that a valid option for me to have a VM with 3d acceleration? I'm fine with having some overhead if it is better than the current software GPU.

I'm more interested how this would effect providing VM graphics with migrations between hosts.

The dream would be put the user OS in a VM in a lab, and then be able to suspend and resume seamlessly if you need to push it to a new workstation, with locally accelerated graphics available.

Amazing project! But man, that README is just a textbook example of LLM word salad. It's wild how these tools are so incredibly capable at many things, but their writing sticks out like a sore thumb

The percentage-overhead comparison is pretty choice nonsense. It has only percentages to try and "explain" that overheads don't matter if the system is slow anyhow.

A fair comparison would be this project vs virtio.

Virtio? what virtio? virtio native drm native context, is that what you mean? We actually use it in nesbox[1] for AMD/Intel cards.

Venus is the only one we could directly compare to, as it is the only one that supports Nvidia GPUs. vDRM works only on AMD/Intel GPUs and has a similar performance (~98% baremetal performance) to virtio-nvgpu.

Claude is much worse for having a distinctive style you can spot from a mile away. I’ve found GPT-6 to not suffer from this or it’s insanely verbose markdown salad.

LLMs are pretty good at translation, they're just pretty awful at generating natural-sounding English prose from scratch. In my opinion, probably the best solution is to simply write the README in your native tongue and use an LLM to translate it.

All good friend! I'm as guilty as anyone. It's a super cool project though.

Now that I have you on the hook, is there any benefit to this over virtio for a single KVM passthrough situation? I previously ran a proxmox based gaming PC setup (docs here: https://github.com/mtrudel/rabble/tree/4d9329f3dd0fb09123a8f...), and was lucky enough that the GPU passthrough part of that build 'just worked'. I'd started down a path of trying to share the GPU between VMs based on a naive 'one VM owns it at a time' setup, but never really got it off the ground.

The benefit is that you do not have a limit to how many VMs you can run at the same time. However, virtio-nvgpu has no Windows support as of yet, please check back in a while :)

You should check out Nestri [1], another project we are working on, that helps you do exactly that. It helps run multiple gaming sessions for you and your friends on the same GPU, without anyone meddling in the other person's session. Everyone gets to stream their game to whatever desktop or device they want. It is still a work-in-progress though.

it's not just literary authorship, it's pretty easy to spot LLM driven programming paradigms too, especially if you look at the test suites of a given package.

I am very sceptical about this. I have some experience in GPU virtualization and passthrough with Nvidia GPUs and they are really not designed to be able to share them with multiple guests/host without Nvidia's blessing (licenced drivers).

Yes they are not... we run the Nvidia drivers unmodified. Only thing we have done is make the guest driver think it's running on the host, talking to the host's GPU kernel.

It works really well with a ~2% performance penalty. Nvproxy by google/gvisor has been doing this for years.

You should try running it yourself and see how it goes :D

So you can share the GPU between multiple VMs? I can have 4 VMs simultaneously do work on the GPU?

And each one would have its own Nvidia driver? How do they not interfere with each other? I mean I am by no means an expert in GPU architecture or anything similar, but I thought the problems with sharing a GPU come from the differences between GPU vs CPU architecture. On the other hand, multiple processes on a host can run on the same GPU, but that is all using the same kernel. I am just very confused.

This has been a thing for AMD, Intel, and Qualcomm GPUs for a few years now. Search for "DRM native context".
The only difference here is that you had to use mesa drivers before and now someone made it work with the Nvidia drivers.

On a laptop, I never got a working setup where I could attach/detach a modern nvidia card from host linux. So something that can do without is better.
But intel SRIOV is a thing as well, which should be the secure alternative.

Fair point, we still have a long way to go in terms of security AND being suitable for everyday use.

However, nvgpu is meant to be used in PCI passthrough in scenarios where you would want to run and share your GPU across multiple KVM guests, or you don't want to detach the GPU from the host, and plug it into the VM you are running... you know, that little dance you do everytime you want to game inside a VM.

I recently did a similar thing with cgroups2 and lxc

Its an proxmox host with local lxc drm passtrough for monitor + udev perhiperals, then cgroup the nvidia cuda api to other stream lxcs. this way i can play on my local node and friends can play on my pc remotely without anyone hogging the gpu fully.

Edit: nvproxy is mentioned as the "direct inspiration" in the readme without mention of how this is different or why it doesn't use nvproxy as a backend.

We borrowed a lot of the architectural design from nvproxy, then built it to support graphical workloads. Plus it is reusable in such a way you can hot plug it into any microVM, cloud-hypervisor, maybe even Firecracker

Why not use normal GPU passthrough? I don't see how you can use this to share a GPU between multiple VMs, so what is the benefit of using this software over normal GPU passthrough with vfio-pci drivers?

With normal passthrough, your host loses access to the gpu, no? So you need to have two gpus, one for the host and one for the guest. Correct me, if I am wrong, but this should make the host fully operational on a single gpu and still let vm guests have headless access to the host gpu.

Nesbox is just an underlying part of a broader (but early) kit to allow a system to stream multiple remote desktops at once.
https://github.com/nestrilabs/nestri

1) VFIO passthrough: host binds entire GPU to guest as PCI device, which only allows one VM to use the GPU, thus you sacrifice your host display too (unless you fallback to integrated graphics on cpu etc). Strongest isolation because host kernel module driver not involved.

2) virtio-gpu: guest sees paravirtual GPU and loads virgl/venus mesa driver which serializes graphics API calls and replays them on the host driver. This allows multiple VMs to use the GPU, but performance overhead can be significant, and guests can’t practically leverage lower level primitives eg NVENC without paying price of CPU readback.

3) virtio-nvgpu (this repo): guest loads standard NVIDIA user mode driver (closed source), a fake /dev/nvidia* kernel module copies ioctl bytes + handle onto queue for host kernel mode driver to execute. This also allows multiple VMs to use a GPU, but is near native speed due to low overhead. Unfortunately the tradeoff is this project has the weakest isolation, eg every guest ioctl is forwarded to the host by default, the VMM holds read/write FDs, no seccomp/caps/allowlist. With respect to There is basically no GPU related security measures here, the exposure is the same as running multiple processes using the GPU with no VM. Only caveat is these guests can’t drive a physical display, so there is some restriction of surface area but it feels incidental rather than intentional in this case.

Anyways this is a tough problem OP, I don’t want to discourage you.

Without hardware/driver support for isolation (MIG) on consumer grade NVIDIA GPUs, it won’t be possible to solve this properly for a long time.

Also a factor is that NVIDIA has no open Mesa driver to support a native context approach (guest owns GPU command buffers, host maps them) like we have for AMD/Intel.

reply
