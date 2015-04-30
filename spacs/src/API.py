import json
import LogHandler
import User
import TransactionBean

#TODO: Remove Magic Strings

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
    return {"error": "not_implimented"}

"""
Called if input JSON is invalid
"""
def invalid_data(data, parameter):
    LogHandler.log_warning("Malformed Data Received")
    return {"error": "invalid_data"}

"""
Called if user is not authed
"""
def not_authed(data, parameter):
    LogHandler.log_warning("User is not authed")
    return {"error": "not_authed"}

"""
Called if API method does not exist
"""
def bad_call(data, parameter):
    LogHandler.log_warning("API Method does not exist")
    return {"error": "bad_call"}

"""
Called if the user is trying to authenticate for the first time
"""
def auth_login(data, parameter):
    username = str(data["username"])
    password = str(data["password"])
    LogHandler.log_info(str(username) + " is logging in")
    #tb = TransactionBean.AuthenticationBean()
    #auth = tb.get_object({"username": username, "password": password})
    #if auth != None and auth.is_authed:
    return {"error": "success"}
    #else:
    #    return {"error": "failure"}

"""
Called if the user is trying to log out of the system
"""
def auth_logout(data, parameter):
    username = data["username"]
    LogHandler.log_info(str(username) + " is logging out")
    return {"error": "success"}

"""
Adds an administrator to the system
"""
def administrator_add(data, parameter):
    user = auth(data)
    if user == None:
        return """{"ERROR":"Not Authenticated"}"""
    
    newadmin = TransactionBean.Administrator()
    
    


