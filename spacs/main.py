import LogHandler
import Scheduler
import WebServer
import thread

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

"""
Start all Subsystems
"""
def start_threads():
    LogHandler.log_info("Starting Scheduler Thread")
    thread.start_new_thread(Scheduler.start, ())
    LogHandler.log_info("Starting WebServer Thread")
    thread.start_new_thread(WebServer.start, ())

"""
Stop all subsystems cleanly
"""
def clean_up_threads():
    pass

"""
Check the Health of all Subsystems
"""
def health_check():
    pass

def main():
    read_config()
    configure_logging()
    LogHandler.log_info("Starting Server")
    start_threads()
    while True:
        try:
            
            pass
        except KeyboardInterrupt:
            LogHandler.log_info("Killed by signal")
            LogHandler.log_warning("SPACS Server stopped")
            clean_up_threads()
            break
        except:
            LogHandler.log_exception()

if __name__=='__main__':
    main()

