import re

"""
Returns true of input is an email address
"""
def is_email(email):
    regex = re.compile("^.*@.*\..*")
    return bool(regex.match(email))

def is_phone_number(number):
    return True

def is_address(number):
    return True

