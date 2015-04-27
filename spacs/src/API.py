import json
import LogHandler
import User
import TransactionBean

"""
Authentication information should be passed in at the start of the JSON
Return the current user object or None if not authed
"""
def is_authed(data):
    return User.User()

"""
Called for things that haven't been programmed yet
"""
def not_implimented(data, parameter):
    LogHandler.log_warning("API Method not implemented")

"""
Called if input JSON is invalid
"""
def invalid_data(data, parameter):
    LogHandler.log_warning("Malformed Data Received")

"""
Called if API method does not exist
"""
def bad_call(data, parameter):
    LogHandler.log_warning("API Method does not exist")

"""
Called if the user is trying to authenticate for the first time
"""
def auth_login(data, parameter):
    LogHandler.log_warning("User trying to authenticate")
    return

"""
Called if the user is trying to log out of the system
"""
def auth_logout(data, parameter):
    LogHandler.log_warning("User Logging Out")
    return

"""
Adds an administrator to the system
"""
def administrator_add(data, parameter):
    user = auth(data)
    if user == None:
        return """{"ERROR":"Not Authenticated"}"""
    
    newadmin = TransactionBean.Administrator()
    
    


