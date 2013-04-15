#!/usr/bin/env python
# coding: utf8
import logging
from logging.handlers import TimedRotatingFileHandler

logger = None
log_name = "db.logger"
file_name = "db.log"


def init_logger():
    global logger, log_name
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    # set rotate log files
    file_handler = TimedRotatingFileHandler(file_name, 'S', 1, 3)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.suffix = "%Y-%m-%d_%H-%M-%S"
    file_handler.setFormatter(formatter)  
    logger.addHandler(file_handler)


def get_logger():
    global logger
    if not logger:
        init_logger()
    return logger
