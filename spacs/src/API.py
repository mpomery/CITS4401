import json
import LogHandler
import User
import AuthUser
import TransactionBean

#TODO: Remove Magic Strings

"""
Called for things that haven't been programmed yet
"""
def not_implimented(data, parameter, user):
    LogHandler.log_warning("API Method not implemented")
    return {"error": "not_implimented"}

"""
Called if input JSON is invalid
"""
def invalid_data(data, parameter, user):
    LogHandler.log_warning("Malformed Data Received")
    return {"error": "invalid_data"}

"""
Called if user is not authed
"""
def not_authed(data, parameter, user):
    LogHandler.log_warning("User is not authed")
    return {"error": "not_authed"}

"""
Called if API method does not exist
"""
def bad_call(data, parameter, user):
    LogHandler.log_warning("API Method does not exist")
    return {"error": "bad_call"}

"""
Called if the user is trying to authenticate for the first time
"""
def auth_login(data, parameter, user):
    username = str(data["username"])
    password = str(data["password"])
    LogHandler.log_info(str(username) + " is logging in")
    tb = TransactionBean.AuthenticationBean()
    auth = tb.get_object({"username": username, "password": password})
    if auth != None and auth.is_authed:
        return {"error": "success"}, auth.user_info
    else:
        return {"error": "failure"}

"""
Called if the user is trying to log out of the system
"""
def auth_logout(data, parameter, user):
    username = data["username"]
    LogHandler.log_info(str(username) + " is logging out")
    return {"error": "success"}

"""
Adds a USER to the system
"""
def user_add(data, parameter, au):
    for property in TransactionBean.UserBean.properties:
        try:
            print("Setting UserBean" + str(property) + " To " + data["user"][str(property)])
            setattr(au.user_info, str(property), data["user"][str(property)])
        except ValueError, ve:
            LogHandler.log_warning("Value Error: " + str(ve[0]))
    
    for property in TransactionBean.AuthenticationBean.properties:
        try:
            print("Setting AuthenticationBean" + str(property) + " To " + data["auth"][str(property)])
            setattr(au.auth_info, str(property), data["auth"][str(property)])
        except ValueError, ve:
            LogHandler.log_warning("Value Error: " + str(ve[0]))
    au.create()
    id = au.id
    return {"error": "success", "id": id}

"""
Adds an Administrator to the system
"""
def administrator_add(data, parameter, user):
    return user_add(data, parameter, AuthUser.CreateAdministrator())

"""
Adds a Pool Shop Admin to the system
"""
def psa_add(data, parameter, user):
    return user_add(data, parameter, AuthUser.CreatePoolShopAdmin())

"""
Adds a Pool Owner to the system
"""
def po_add(data, parameter, user):
    return user_add(data, parameter, AuthUser.CreatePoolOwner())

"""
Edit a USER in the system
"""
def user_edit(data, parameter, au):
    for property in TransactionBean.UserBean.properties:
        try:
            print("Setting UserBean" + str(property) + " To " + data["user"][str(property)])
            setattr(au.user_info, str(property), data["user"][str(property)])
        except ValueError, ve:
            LogHandler.log_warning("Value Error: " + str(ve[0]))
    
    for property in TransactionBean.AuthenticationBean.properties:
        try:
            print("Setting AuthenticationBean" + str(property) + " To " + data["auth"][str(property)])
            setattr(au.auth_info, str(property), data["auth"][str(property)])
        except ValueError, ve:
            LogHandler.log_warning("Value Error: " + str(ve[0]))
    au.save()
    id = au.id
    return {"error": "success", "id": id}

"""
Edits an Administrator in the system
"""
def administrator_edit(data, parameter, user):
    return user_edit(data, parameter, AuthUser.EditAdministrator(data["user"]["id"]))

"""
Edits a Pool Shop Admin in the system
"""
def psa_edit(data, parameter, user):
    return user_edit(data, parameter, AuthUser.EditPoolShopAdmin(data["user"]["id"]))

"""
Edits a Pool Shop Owner in the system
"""
def po_edit(data, parameter, user):
    return user_edit(data, parameter, AuthUser.EditPoolOwner(data["user"]["id"]))

