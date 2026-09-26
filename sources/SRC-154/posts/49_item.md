# item

source: https://news.ycombinator.com/item?id=49795600

> After another half-an-hour I found that my malloc function always returned the same address!!! Wow! An unexpected bug in my operating system. When the memory space is full, the malloc routine simply fails to return a NULL pointer.

don't you love it when your investigation finds bugs in completely unrelated part of the system?

how does a debug file output 8GB+? Is it running for minutes/hours? Or is it in a format that uses a lot of rich text? I would assume a text file in hex or unicode wouldn't use very much.. Is there a way to create intervals of log files so they have a cap on the size?

It is a simple debugger log in the transputer emulator (enabled by compilation option) which outputs each instruction executed so far, around 70 bytes per line displaying the 3 registers, the stack pointer, the instruction pointer, and the disassembled instruction.

The emulated C compiler processed a whole file ccvars.c before getting stuck in ccinter.c (this is the 5gb mark, approximately 78 millions of instructions executed). I stopped the process as soon as I saw it was stuck, but the emulator is fast, and I got extra 3 gb in the log. All this happened in less than two minutes.

Another reminder of how easy it is to forget how ridiculously fast computers are these days (especially when you're like me and not writing stuff close to the metal for your day job).

In terms of latency... well... we also could do a lot better there, but as I understand it, even if you do your best to cut away as much software bloat as possible, the latency "floor" seems to be higher than in the old days[0]. And the many layers of abstraction that is the average software stack don't help. Like, I'm doing my best to keep a web-app snappy, but there's only so much you can squeeze out of a browser.

reply
