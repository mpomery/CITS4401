class PoolTestingUnit(object):
    
    def __init__(self, id=None):
        self.__id = id
        self.__length = None
        self.__width = None
        self.__depth = None
        self.__above_ground = False
        self.__material = str()
    
    @property
    def id(self):
        return self.__id
    
    @property
    def length(self):
        return self.__length
    
    @property
    def width(self):
        return self.__width
    
    @property
    def depth(self):
        return self.__depth
    
    @property
    def volume(self):
        return self.__volume
    
    @property
    def above_ground(self):
        return self.__above_ground
    
    @property
    def material(self):
        return self.__material
    
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