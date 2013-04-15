```python
#!/usr/bin/env python
# coding: utf8
import logging
from logging.handlers import TimedRotatingFileHandler

logger = None
log_name = "logger"
file_name = "db.log"


def init_logger():
    global logger, log_name
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    # set rotate log files
    file_handler = TimedRotatingFileHandler(file_name, 'D', 1, 0)
    # set logging format
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    # set rotate file suffix format
    file_handler.suffix = "%Y-%m-%d"
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def get_logger():
    global logger
    if not logger:
        init_logger()
    return logger

```
