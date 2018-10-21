import time
import json
import signal
import logging
from threading import Thread

from servicefactory import Service

from honcho import Honcho

@Service.API.endpoint(port=1234)
class Manager(Service.base):

  def __init__(self):
    self.honchos = []

  def loop(self):
    print("looping...")
    time.sleep(5)

  def finalize(self):
    logging.info("finalizing...")
    for honcho in self.honchos:
      honcho.handle_signal(signal.SIGTERM)

  @Service.API.handle("start")
  def handle_start(self, arg):
    app = json.loads(arg)
    logging.info("starting app from: {0}".format(app))
    honcho = Honcho(app_root=app, handle_signals=False)
    self.honchos.append(honcho)
    thread = Thread(target=honcho.start)
    thread.start()
    time.sleep(0.1)
