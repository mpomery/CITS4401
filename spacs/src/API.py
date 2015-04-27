import LogHandler

def not_implimented(data, parameter):
    LogHandler.log_warning("API Method not impimented")

def bad_call(data, parameter):
    LogHandler.log_warning("API Method does not exist")