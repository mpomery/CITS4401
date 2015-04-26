import LogHandler

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
            LogHandler.log_info("Killed by signal")
            LogHandler.log_warning("SPACS Server stopped")
            break
        except:
            LogHandler.log_exception()

if __name__=='__main__':
    read_config()
    configure_logging()
    LogHandler.log_info("Starting Server")
    main()

