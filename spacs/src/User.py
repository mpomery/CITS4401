import Validator

def User(Object):
    
    
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
        return self.id
    
    @property
    def title(self):
        return self.title
    
    @property
    def name(self):
        return self.name
    
    @property
    def address(self):
        return self.address
    
    @property
    def email_address(self):
        return self.email_address
    
    @property
    def phone_number(self):
        return self.phone_number
    
    @property
    def mobile_number(self):
        return self.mobile_number
    
    @id.setter
    def id(self):
        self.id
    
    @property
    def title(self):
        self.title
    
    @property
    def name(self):
        self.name
    
    @property
    def address(self):
        self.address
    
    @property
    def email_address(self):
        self.email_address
    
    @property
    def phone_number(self):
        self.phone_number
    
    @property
    def mobile_number(self):
        self.mobile_number