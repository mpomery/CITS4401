import re

"""
Returns true of input is an email address
"""
def is_email(email):
    regex = re.compile("^[a-z0-9+_-.]+@([a-z0-9+_-]+\.)+[a-z]+$", re.IGNORECASE)
    return bool(regex.match(email))