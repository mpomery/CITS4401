import sys
from traceback import format_tb
import logging

"""
Read configuration file for application
"""
def read_config():
    pass

"""
Set up logging for the entire SPACS system
"""
def configure_logging():
    pass

def main():
    
    while True:
        try:
            pass
        except KeyboardInterrupt:
            logging.info("Killed by signal, cleaning up")
            logging.warning("SPACS Server stopped")
            break
        except:
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

if __name__=='__main__':
    read_config()
    configure_logging()
    main()

    