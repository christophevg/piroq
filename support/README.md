To have PiroQ running as a daemon on a Raspberry Pi, issue the following
commands:

```bash
$ sudo cp piroq.service /lib/systemd/system/
$ sudo systemctl enable piroq
$ sudo systemctl start piroq
```
