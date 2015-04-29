class Authentication(object):
    
    def __init__(self):
        self.__id = -1
        self.__username = str()
        self.__password = str()
        self.user_type = int()
    
    def is_password(self, password):
        return self.__password == password
    
    @property
    def id(self):
        return self.__id
    
    @property
    def username(self):
        return self.__username
    
    @property
    def password(self):
        return self.__password
    
    @property
    def user_type(self):
        return self.__user_type
    
    @id.setter
    def id(self, id):
        self.__id = id
    
    @username.setter
    def username(self, username):
        self.__username = str.lower(str(username))
    
    @password.setter
    def password(self, password):
        self.__password = password
    
    @user_type.setter
    def user_type(self, user_type):
        self.__user_type = user_type

