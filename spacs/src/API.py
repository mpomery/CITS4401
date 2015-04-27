import json
import LogHandler

def not_implimented(data, parameter):
    LogHandler.log_warning("API Method not impimented")

def invalid_data(data, parameter):
    LogHandler.log_warning("Malformed Data Received")

def bad_call(data, parameter):
    LogHandler.log_warning("API Method does not exist")

def auth_login(data, parameter):
    LogHandler.log_warning("User trying to authenticate")
    return

