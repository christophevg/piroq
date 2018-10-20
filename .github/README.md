# PiroQ

Turns a Raspberry Pi in a Heroku-like execution environment

## Work in Progress Warning ;-)

I've only just started working on this and I'm literally exploring my own code as I write it ;-) So until this warning is removed, I wouldn't trust myself using this ;-) Do play with it, but remember things can and will change overnight.

## Rationale

For some time now, I've been settling on Python as my preferred general-purpose language, along with its vast amount of very nice modules and frameworks. Along with Python, I really like Heroku as an incredible simple deployment target. Besides Heroku, I also heavily use Raspberry Pi nodes. Most of the time the same code runs on Heroku and on a Pi, so I ended up with a quest to make deployment on a Pi as identical to the experience on Heroku. Hence PiroQ - pronounced like (He)roku ;-)

## Philosophy

The design goals for PiroQ:

1. Make it as simple, lightweight,... as possible
2. Make it work out of the box with as minimal installation steps as possible
3. Make it work with as little configuration as possible

Basically I want to achieve the following experience:

```bash
$ pip install piroq
$ mkdir -p /opt/piroq/apps
$ cd /opt/piroq/apps
$ git clone [your project]
```

## The story so far

At its core, PiroQ is a wrapper around [honcho](https://github.com/nickstenning/honcho), a Python port of [foreman](https://github.com/ddollar/foreman), which enables running applications from a Profile. So that's [where I started](https://github.com/nickstenning/honcho/issues/208) ;-)

For now, I've created a local honcho wrapper, which allows me to get access to the return code of the honcho Manager:

```bash
$ virtualenv venv
$ . ./venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ PYTHONPATH=. python piroq
12:09:34 system   | count5.1 started (pid=7568)
12:09:34 system   | count2.1 started (pid=7569)
12:09:34 count5.1 | 1
12:09:34 count2.1 | 1
12:09:35 count5.1 | 2
12:09:35 count2.1 | 2
12:09:36 count5.1 | 3
12:09:36 system   | count2.1 stopped (rc=128)
12:09:36 system   | sending SIGTERM to count5.1 (pid 7568)
12:09:36 system   | count5.1 stopped (rc=-15)
honcho ended with 128
```

Next up: turning PiroQ into a service and add application management commands...
