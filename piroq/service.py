import os
import time
import logging

from servicefactory import Service

from piroq.app import Runner

APPS_ROOT = os.environ.get("APPS_ROOT") or "/opt/piroq/apps"

class Manager(Service.base):

  def __init__(self):
    self.apps = {}
    logging.info("managing apps from {0}".format(APPS_ROOT))

  def loop(self):
    self.check_apps()
    self.check_for_updates()
    time.sleep(5)

  def check_apps(self):
    _, dirs, _ = next(os.walk(APPS_ROOT))
    # detect new apps
    for dir in dirs:
      if not dir in self.apps:
        self.apps[dir] = Runner(os.path.join(APPS_ROOT, dir)).run()
    # detect removed apps
    for dir in list(self.apps):
      if not dir in dirs:
        self.apps[dir].stop()
        self.apps.pop(dir)

  def check_for_updates(self):
    for name in self.apps:
      self.apps[name].check()

  def finalize(self):
    logging.info("terminating all apps")
    for name in self.apps:
      self.apps[name].stop()
