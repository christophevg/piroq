# Getting Started

Let's give PiroQ a spin, shall we?

```bash
$ pip install piroq
$ mkdir apps
$ APPS_ROOT=apps piroq
[2019-03-15 22:01:14 +0100] [94481] [INFO] managing apps from apps
```

Let's create an app... Just keep PiroQ running, so from a separate terminal:

```bash
$ cd apps
$ mkdir hello
```

And PiroQ will report...

```bash
[2019-03-15 21:46:48 +0100] [79455] [WARNING] no Procfile (Procfile) found in apps/hello
[2019-03-15 21:46:48 +0100] [79455] [ERROR] manager was not initialized, probably no Procfile loaded?
```

Okay, makes sense... the `hello` folder is empty. Let's create a `Procfile` that dumps the current date to a file:

```
$ cd hello
$ echo 'hello: while true; do date >> log.txt; sleep 1; done' > Procfile
```

Now within a few seconds, you will see that PiroQ has picked up de `Procfile` and has started all (one in this case) processes:

```bash
[2019-03-15 21:47:08 +0100] [79455] [INFO] starting app hello
[2019-03-15 21:47:08 +0100] [79455] [INFO] started all processes from apps/hello/Procfile
```

And we can validate it:

```bash
$ tail -3 log.txt 
Fri Mar 15 21:49:20 CET 2019
Fri Mar 15 21:49:21 CET 2019
Fri Mar 15 21:49:22 CET 2019
```

Don't forget to terminate PiroQ:

```bash
^C[2019-03-15 21:52:32 +0100] [79455] [INFO] shutdown requested
[2019-03-15 21:52:32 +0100] [79455] [INFO] terminating all apps
[2019-03-15 21:52:32 +0100] [79455] [INFO] stopping app hello
[2019-03-15 21:52:32 +0100] [79455] [INFO] stopped all processes from apps/hello/Procfile
```
