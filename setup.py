import os
import re
import setuptools

NAME             = "piroq"
AUTHOR           = "Christophe VG"
AUTHOR_EMAIL     = "contact@christophe.vg"
DESCRIPTION      = "PiroQ: Turns a Raspberry Pi into a Heroku-like execution environment."
LICENSE          = "MIT"
KEYWORDS         = "framework cloud raspberrypi procfile"
URL              = "https://github.com/christophevg/" + NAME
README           = ".github/README.md"
CLASSIFIERS      = [
  "Environment :: Console",
  "Development Status :: 4 - Beta",
  "Intended Audience :: Developers",
  "Intended Audience :: System Administrators",
  "Topic :: Software Development",
  "License :: OSI Approved :: MIT License",
  "Programming Language :: Python",
  "Programming Language :: Python :: 2.7",
  "Programming Language :: Python :: 3.7",
]
INSTALL_REQUIRES = [
  "python-dotenv",
  "servicefactory",
  "procfile-manager",
  "GitPython"
]
ENTRY_POINTS = {
  "console_scripts": [
    "piroq=piroq.command:main"
  ]
}
SCRIPTS = []

HERE = os.path.dirname(__file__)

def read(file):
  with open(os.path.join(HERE, file), "r") as fh:
    return fh.read()

VERSION = re.search(
  r'__version__ = [\'"]([^\'"]*)[\'"]',
  read(NAME.replace("-", "_") + "/__init__.py")
).group(1)

LONG_DESCRIPTION = read(README)

if __name__ == "__main__":
  setuptools.setup(name=NAME,
        version=VERSION,
        packages=setuptools.find_packages(),
        author=AUTHOR,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        license=LICENSE,
        keywords=KEYWORDS,
        url=URL,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        entry_points=ENTRY_POINTS,
        scripts=SCRIPTS)
