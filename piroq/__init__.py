__version__ = "0.0.2"

import os
from dotenv import load_dotenv
import logging

# read environment from .env file

load_dotenv(".env")

# setup logging: formatting and console logger

logger = logging.getLogger()

formatter = logging.Formatter(
  "[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s",
  "%Y-%m-%d %H:%M:%S %z"
)

if len(logger.handlers) > 0:
  logger.handlers[0].setFormatter(formatter)
else:
  consoleHandler = logging.StreamHandler()
  consoleHandler.setFormatter(formatter)
  logger.addHandler(consoleHandler)

LOG_LEVEL = os.environ.get("LOG_LEVEL") or "INFO"
logger.setLevel(logging.getLevelName(LOG_LEVEL))
