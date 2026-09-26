# item

source: https://news.ycombinator.com/item?id=49799306

Once upon a time I had to figure out an issue where I forgot a `return` statement at the end of a non-`void` function, so the C++ compiler happily omitted both RETs for some reason and let the program go straight into illegal instructions. That was fun to debug (not fun, I practically had to single-step through the entire program) because every time this happened the debugger was incredibly confused about what the fuck was going on and nothing made any sense.

Another issue that happened in the same project is that for some reason whenever I compiled it with a regular C++ compiler, field writes were disappearing into the abyss. I think I actually never figured that out because it was literally the same object at the same memory address, there were no other threads and yet when a subroutine returned after writing the field, the write disappeared?? The strangest thing is that Emscripten's C++-to-WASM cross-compiler worked perfectly fine with the exact same routines. I wonder if the compiler I used simply had fuckass issues, it was an oldish (by modern standards) Apple clang from like probably macOS 10.14 or so.

reply
