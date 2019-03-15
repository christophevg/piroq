import os  
import time
import logging
from threading import Thread
from dotenv import load_dotenv, dotenv_values

from procfile_manager import Procfile, Manager

class Runner(object):
  def __init__(self, path):
    self.path    = path
    self.manager = None
    self.running = False

  def load(self):
    if not self.manager is None: return self
    try:
      env = dotenv_values(dotenv_path=os.path.join(self.path, ".env"))
      procfile = env["PROCFILE"]
    except KeyError:
      procfile = "Procfile"
    f = os.path.join(self.path, procfile)
    if os.path.isfile(f):
      self.manager = Manager(Procfile(f))
    else:
      logging.warn("no Procfile ({0}) found in {1}".format(procfile, self.path))
    return self

  def run(self):
    self.load()
    if self.manager is None:
      logging.error("manager was not initialized, probably no Procfile loaded?")
      return None
    thread = Thread(
      target=self.manager.run,
      kwargs=dict(
        blocking=False,
        cwd=self.path
      )
    )
    thread.start()
    time.sleep(0.1) # else the thread doestn't start properly ?!
    self.running = True
    return self

  def stop(self):
    if self.running:
      self.manager.stop()
      self.running = False
    return self
