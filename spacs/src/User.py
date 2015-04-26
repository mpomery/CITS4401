import Validator

class User(Object):
    
    
    def __init__(self, id=None, title=None, name=None, address=None, email_address=None,
            phone_number=None, mobile_number=None):
        self.__id = id
        self.__title = title
        self.__name = name
        self.__address = address
        self.__email_address = email_address
        self.__mobile_number = mobile_number
        self.__phone_number = phone_number
    
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
        if not Validator.is_email(email_address):
            raise ValueError("Email Address is Invalid")
        self.__email_address = email_address
    
    @phone_number.setter
    def phone_number(self, phone_number):
        if not Validator.is_phone_number(phone_number):
            raise ValueError("Phone Number is not valid")
        self.__phone_number = phone_number
    
    @mobile_number.setter
    def mobile_number(self, mobile_number):
        if not Validator.is_phone_number(mobile_number):
            raise ValueError("Phone Number is not valid")
        self.__mobile_number = mobile_number

class Administrator(User):
    pass

class PoolShop(User):
    pass

class PoolOwner(User):
    pass