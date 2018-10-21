# PiroQ

Turns a Raspberry Pi in a Heroku-like execution environment

## Work in Progress Warning ;-)

I've only just started working on this and I'm literally exploring my own code as I write it ;-) So until this warning is removed, I wouldn't trust myself using this ;-) Do play with it, but remember things can and will change overnight.

## Rationale

For some time now, I've been settling on Python as my preferred general-purpose language,  with its vast amount of very nice modules and frameworks. Along with Python, I really like Heroku as an incredible simple deployment target. Besides Heroku, I also heavily use Raspberry Pi nodes. Most of the time the same code runs on Heroku and on a Pi, so I ended up with a quest to make deployment on a Pi as identical to the experience on Heroku. Hence PiroQ - pronounced "ku" at the end - wonder why ;-)

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

At its core, PiroQ is a wrapper around [Honcho](https://github.com/nickstenning/honcho), a Python port of [Foreman](https://github.com/ddollar/foreman), which enables running applications from a Procfile. So that's [where I started](https://github.com/nickstenning/honcho/issues/208) ;-)

At first I created a basic local Honcho wrapper, which allowed me to get access to the return code of the honcho Manager. But soon more roadblocks emerged and simply rewriting parts locally didn't really work anymore.

I wanted to turn PiroQ into a service and allow it to run multiple instances of applications in parallel. Here I bumped into a first roadblock. The Honcho Manager, deals with system signals it receives. This doesn't play well with threads. So I had to lift this up to the start command level, and that included turning Honcho into a class, to be able to track multiple instances with different Managers... A this point, I started to work on a fork of Honcho, which hopefully will finds in way back upstream.

So to run the following code, for now, you need a clone of [my fork](https://github.com/christophevg/honcho.git) as a sibling to a PiroQ cloned repository and checkout the `api` branch. Then from the PiroQ clone issue the following commands:

```bash
$ virtualenv venv
$ . ./venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) falcon:piroq xtof$ PYTHONPATH=.:../honcho python piroq
looping...
looping...
```

At this point, the PiroQ service is looping and printing `looping...` every 5 seconds. The service is created using my [servicefactory module](https://github.com/christophevg/py-servicefactory), which makes the creation of a service with a REST API to access it a breeze.

Now from a different terminal issue:

```bash
curl http://localhost:1234/start -X POST -d '"."' -H "Content-Type: application/json"
```

Back in the PiroQ terminal we see that the `/start` command is given to Honcho and the Procfile is executed.

```bash
2018-10-21 21:53:07 [31593] [INFO] starting app from: .
21:53:07 system   | count5.1 started (pid=31597)
21:53:07 system   | count2.1 started (pid=31598)
21:53:07 count2.1 | 1
21:53:07 count5.1 | 1
21:53:08 count5.1 | 2
21:53:08 count2.1 | 2
21:53:09 count5.1 | 3
21:53:09 system   | count2.1 stopped (rc=128)
21:53:09 system   | sending SIGTERM to count5.1 (pid 31597)
21:53:09 system   | count5.1 stopped (rc=-15)
looping...
^C2018-10-21 21:53:12 [31593] [INFO] shutdown requested
2018-10-21 21:53:12 [31593] [INFO] finalizing...
21:53:12 system   | SIGTERM received
```

> Issuing multiple curl commands will result in multiple instances of the Procfile to be executed.

More to come...
