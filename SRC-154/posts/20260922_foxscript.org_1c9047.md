# Microsoft killed FoxPro in 2007. Anyway, here's FoxPro revived

source: https://foxscript.org/
published: Tue, 22 Sep 2026 21:00:30 +0000

FoxDev Studio opens the projects, forms and tables you already have and runs them the way you remember: **no rewrite, no conversion, no export step**.

Point it at a folder you have not opened in years, and what is there is what you get.

Projects, forms, class libraries, menus and reports open straight from the files you already have. Nothing is migrated first, and nothing is left behind.

Forms, classes, menus and reports are edited where you expect them to be, alongside the project manager, the Command Window and a debugger that stops on your line.

Tables, indexes, memos and databases are read and written in place. What sits on disk afterwards is the same kind of file it was before.

The system calls, the automation objects and the old add-in libraries your application leans on keep working, so the parts nobody wants to touch stay untouched.

The IDE, on Visual FoxPro's own sample projects. Every picture is a real session.

Small differences are what break an old application: a number printed a column too wide, an event arriving a moment late, an error with the wrong number on it. So behaviour here is **settled by asking Visual FoxPro itself** and matching its answer, rather than by reading a reference page and hoping.

What comes out of that is a runtime written from scratch: quick to start, self-contained, and straightforward about the corners it has not reached yet.

Visual FoxPro stopped at version 9, and at 32 bits. This is the same language, rebuilt on a foundation that has not been frozen since 2007. Four pieces are what make that possible.

Visual FoxPro is a 32-bit program, and that decides more than it appears to. It is why a table stops at two gigabytes, why a memo file stops at two gigabytes, and why a big report runs out of memory on a machine with plenty to spare. The limits are signed 32-bit numbers buried in the file handling, not a licensing decision anybody made.

FoxDev Studio is **64-bit throughout**. Every file offset is 64-bit and a table is never read into memory at all, so the same `.dbf`

that used to stop dead carries on into the **hundreds of gigabytes**. One thing to know before you lean on it: a table grown past two gigabytes will not open in Visual FoxPro again. If you still work in both, that is a one-way door.

Visual FoxPro compiled your program to p-code and shipped a runtime to execute it. This is the same arrangement, made again: a compiler and a bytecode interpreter written in Rust and compiled to **WebAssembly**, so one machine runs your code wherever the application runs. The editor checks what you type through that very compiler, so what it underlines and what the runtime refuses cannot drift apart.

A running program is a fiber. When it needs something from the world outside (a message box, a modal form, the next record) it does not call out and block; it yields, the work is done while the machine is off the stack, and the answer is handed back. That is why `MESSAGEBOX()`

stops your program without freezing the window behind it, why `READ EVENTS`

waits without spinning, and why`SetFocus`

can fire `GotFocus`

, and `Init`

can run while a form is still being built, in the order FoxPro always did it.

A running form is a live tree of objects with the properties you would expect, and the interface is drawn straight from that tree by React. Each object watches only itself, so `THISFORM.lblGreeting.Caption = cMsg`

repaints one label rather than the whole form. On a dense screen that is the difference between instant and sluggish.

The same tree is what the designer edits, one step earlier. There is no second model kept in step with the first, which is the usual place a form and its designer start telling different stories.

An `.fll`

is a 32-bit image, and every process in a 64-bit application is 64-bit, so nothing inside the application itself could ever open one. Rather than tell you it is impossible, `SET LIBRARY TO`

starts a **small 32-bit process whose only job is to hold your library**, and the runtime talks to it. The calls are synchronous, because a program may call into a library halfway through an expression, and an answer that arrived later would not be an answer. It is measured against real libraries: the encryption library, FoxTools, and libraries built from Microsoft's own API samples.

Nothing 64-bit needs the bridge: `DECLARE ... DLL`

reaches a modern library in the same process, and automation objects are reached the way they always were. The old road stays open; it just is not the only one any more.

Everything you have written still means what it always meant. FoxScript only adds on top: a block you can hand to something else to run later, and a way to answer a web request from the code that already knows your business.

```
&& your old add-in libraries load just as before
SET LIBRARY TO "vfpencryption71.fll" ADDITIVE
LOCAL oServer
oServer = FoxScript.Http.CreateServer()
oServer.Get("/api/v1/customers/:id", LAMBDA(req, res)
LOCAL lnId
lnId = VAL(req.Params("id"))
SELECT * FROM customer WHERE cust_id = lnId INTO CURSOR c_cust
IF RECCOUNT("c_cust") > 0
res.Status(200).Json(FoxScript.Data.CursorToJson("c_cust"))
ELSE
res.Status(404).Json('{"error": "Not found"}')
ENDIF
USE IN c_cust
ENDLAMBDA)
oServer.Listen(8080)
READ EVENTS
```


Every line of that runs on the same runtime your forms do. The queries, the cursor and the library call are ordinary FoxPro; the lambda and the server are what FoxScript adds: no second language, no service to stand up beside it.[The keywords](https://foxscript.org/docs/foxscript) and [the HTTP API](https://foxscript.org/docs/http-api)are each written down in full.

The nightly is rebuilt from every push to main and published as a pre-release on GitHub. Unsigned, so the first launch asks you to confirm.

Each part of the product is written down, including the parts that are not there yet.

Work already mapped out, roughly in the order it is being built.