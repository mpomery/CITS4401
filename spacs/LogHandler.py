import sys
from traceback import format_tb
import logging

LogFormat = "AAAA"

def log_exception():
    # Catch Everything, log it and restart
    (exc_type, exc_value, exc_traceback) = sys.exc_info()
    tb = format_tb(exc_traceback, 20)
    logmessage = "Unhandled " + str(exc_type) + " exception\r\n" + \
            "Message: " + str(exc_value) + "\r\n"
    for event in tb:
        logmessage += "Traceback:\r\n"
        for line in event.split("\n"):
                logmessage += "    " + line + "\r\n"
    logmessage += "This message should be considered a bug in the SPACS Server.\r\n"
    logging.critical(logmessage)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message):
    logging.error(message)

def log_critical(message):
    logging.critical(message)

def log_debug(message):
    logging.debug(message)

