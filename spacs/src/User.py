import Validator


class UserTypes(object):
    USER = -1
    ADMINISTRATOR = 9
    POOLSHOPADMIN = 7
    POOLOWNER = 1

class User(object):
    
    def __init__(self, id=None):
        self.__id = id
        self.__title = str()
        self.__name = str()
        self.__address = str()
        self.__email_address = str()
        self.__mobile_number = str()
        self.__phone_number = str()
        self.__user_type = getattr(UserTypes, str.upper(self.__class__.__name__))
    
    @property
    def id(self):
        return self.__id
    
    @property
    def title(self):
        return self.__title
    
    @property
    def name(self):
        return self.__name
    
    @property
    def address(self):
        return self.__address
    
    @property
    def email_address(self):
        return self.__email_address
    
    @property
    def phone_number(self):
        return self.__phone_number
    
    @property
    def mobile_number(self):
        return self.__mobile_number
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @title.setter
    def title(self, title):
        self.__title = title
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @address.setter
    def address(self, address):
        self.__address = address
    
    @email_address.setter
    def email_address(self, email_address):
        self.__email_address = email_address
        if not Validator.is_email(email_address):
            raise ValueError("Email Address is Invalid")
    
    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number
        if not Validator.is_phone_number(phone_number):
            raise ValueError("Phone Number is not valid")
    
    @mobile_number.setter
    def mobile_number(self, mobile_number):
        self.__mobile_number = mobile_number
        if not Validator.is_phone_number(mobile_number):
            raise ValueError("Phone Number is not valid")

class Administrator(User):
    pass

class PoolShopAdmin(User):
    pass

class PoolOwner(User):
    pass