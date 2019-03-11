import os  
import time
import logging
from threading import Thread

from procfile_manager import Procfile, Manager

class Runner(object):
  def __init__(self, path):
    self.path = path
    self.manager = None
    f = os.path.join(path, "Procfile.piroq")
    if not os.path.isfile(f):
      f = os.path.join(path, "Procfile")
    if os.path.isfile(f):
      self.manager = Manager(Procfile(f))
    else:
      logging.warn("no Procfile detected in {0}".format(self.path))

  def run(self):
    if self.manager is None: return self
    thread = Thread(target=self.manager.run, kwargs=dict(blocking=False))
    thread.start()
    time.sleep(0.1) # else the thread doestn't start properly ?!
    return self

  def stop(self):
    self.manager.stop()
    return self
