# PiroQ

> A Heroku-like execution environment, with a focus on Raspberry Pi support


[![Latest Version on PyPI](https://img.shields.io/pypi/v/piroq.svg)](https://pypi.python.org/pypi/piroq/)
[![Supported Implementations](https://img.shields.io/pypi/pyversions/piroq.svg)](https://pypi.python.org/pypi/piroq/)
[![Build Status](https://secure.travis-ci.org/christophevg/piroq.svg?branch=master)](http://travis-ci.org/christophevg/piroq)
[![Documentation Status](https://readthedocs.org/projects/piroq/badge/?version=latest)](https://piroq.readthedocs.io/en/latest/?badge=latest)
[![Coverage Status](https://coveralls.io/repos/github/christophevg/piroq/badge.svg?branch=master)](https://coveralls.io/github/christophevg/piroq?branch=master)
[![Built with PyPi Template](https://img.shields.io/badge/PyPi_Template-v0.0.6-blue.svg)](https://github.com/christophevg/pypi-template)

```eval_rst
.. warning:: **Work in Progress** - I've only just started working on this and I'm literally exploring my own code as I write it ;-) So until this warning is removed, I wouldn't trust myself using this ;-) Do play with it, but remember things can and will change overnight.
```

## Rationale

For some time now, I've been settling on Python as my preferred general-purpose language,  with its vast amount of very nice modules and frameworks. Along with Python, I really like Heroku as an incredible simple deployment target. Besides Heroku, I also heavily use Raspberry Pi nodes. Most of the time the same code runs on Heroku and on a Pi, so I ended up with a quest to make deployment on a Pi as identical to the experience on Heroku. Hence PiroQ - pronounced "ku" at the end - wonder why ;-)

## Philosophy

The design goals for PiroQ:

1. Make it as simple, lightweight,... as possible.
2. Make it work out of the box with as minimal installation steps as possible.
3. Make it work with as little configuration as possible, aka prefer conventions over configuration.

Basically I want to achieve the following experience:

```bash
$ mkdir -p /opt/piroq/apps
$ cd /opt/piroq/apps
$ git clone [your project's origin repository]
$ pip install piroq
$ piroq
```

... and have the project up & running and updated & restarted with every push to the origins repository.

## Contents

* [What's in the Box](whats-in-the-box.md)
* [Getting Started](getting-started.md)
* [Contributing](contributing.md)
