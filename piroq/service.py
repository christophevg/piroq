import os
import time
import logging
import json

from git import Repo, Remote
logging.getLogger("git.cmd").setLevel(logging.WARNING)

from servicefactory import Service

from piroq.app import Runner

APPS_ROOT     = os.environ.get("APPS_ROOT") or "/opt/piroq/apps"
AUTO_DEPLOY   = os.environ.get("AUTO_DEPLOY") in [ "yes", "YES", "y", "true", "TRUE" ]
if AUTO_DEPLOY: logging.info("auto deploying is enabled")
LOOP_INTERVAL = os.environ.get("LOOP_INTERVAL") or 5

@Service.API.endpoint(port=56565)
class Manager(Service.base):

  def __init__(self):
    self.apps = {}
    logging.info("managing apps from {0}".format(APPS_ROOT))

  def loop(self):
    self.check_apps()
    if AUTO_DEPLOY: self.check_for_updates()
    time.sleep(LOOP_INTERVAL)

  def check_apps(self):
    _, dirs, _ = next(os.walk(APPS_ROOT))
    # detect new apps
    for dir in dirs:
      if not dir in self.apps:
        self.start(dir)
    # detect removed apps
    for dir in list(self.apps):
      if not dir in dirs:
        self.apps[dir].stop()
        self.apps.pop(dir)

  def check_for_updates(self):
    for name in self.apps:
      self.update(name)

  @Service.API.handle("update")
  def update(self, name):
    try: name = json.loads(name)
    except: pass
    try:
      repo = Repo(self.apps[name].path)
      before = repo.head.object.hexsha
      origin = Remote(repo, 'origin')
      origin.pull(rebase=True)
      after = repo.head.object.hexsha
      if after != before:
        logging.info("repository of app {0} was updated {1}->{2}".format(
          name, before, after)
        )
        self.restart(name)
      return "ok"
    except Exception as e:
      logging.error("git operation failed: {0}".format(str(e)))
      return "not ok"

  @Service.API.handle("start")
  def start(self, name):
    try: name = json.loads(name)
    except: pass
    logging.info("starting app {0}".format(name))
    self.apps[name] = Runner(os.path.join(APPS_ROOT, name)).run()

  @Service.API.handle("stop")
  def stop(self, name):
    try: name = json.loads(name)
    except: pass
    if name in self.apps:
      logging.info("stopping app {0}".format(name))
      self.apps[name].stop()
    else:
      logging.warn("unknown app {0}".format(name))

  @Service.API.handle("restart")
  def restart(self, name):
    try: name = json.loads(name)
    except: pass
    self.stop(name)
    self.start(name)

  def finalize(self):
    logging.info("terminating all apps")
    for name in self.apps:
      self.stop(name)
    logging.info("done")
