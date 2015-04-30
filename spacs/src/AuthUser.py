import User
import TransactionBean
import Authentication


class AuthUser(object):

    def __init__(self, username, password):
        self.__authentication = None
        self.__user = None
        self.__level = None
        self.__is_authed = False
        
        
        authbean = TransactionBean.AuthenticationBean()
        self.__authentication = authbean.get_object({"username": str.lower(username), "password": password})
        authbean.close()
        
        if self.__authentication != None:
            userbean = self.__class__.bean()
            self.__user = userbean.get_object({"id": self.__authentication.id})
            userbean.close()
            if self.user_info != None:
                self.__is_authed = True
                self.__level = getattr(User.UserTypes, str.upper(str(self.__user.__class__.__name__)))
    
    @property
    def user_info(self):
        return self.__user
        
    @property
    def auth_info(self):
        return self.__authentication
        
    @property
    def is_authed(self):
        return self.__is_authed
        
    @property
    def username(self):
        return self.__authentication.username
    
    @property
    def id(self):
        return self.__user.id
        
    @property
    def level(self):
        return self.__level

class AuthAdministrator(AuthUser):
    bean = TransactionBean.AdministratorBean
    userclass = User.Administrator

class AuthPoolShopAdmin(AuthUser):
    userclass = User.PoolShopAdmin
    bean = TransactionBean.PoolShopAdminBean

class AuthPoolOwner(AuthUser):
    userclass = User.PoolOwner
    bean = TransactionBean.PoolOwnerBean

"""
WARNING: This class has a couple opf hacks implimented to get around SQLites lack of multithreading
"""
class CreateUser(object):
    #TODO: Disallow multiple users with same username
    userclass = User.User
    bean = TransactionBean.UserBean
    
    def __init__(self):
        self.__authentication = Authentication.Authentication()
        self.__user = self.__class__.userclass()
    
    @property
    def user_info(self):
        return self.__user
        
    @property
    def auth_info(self):
        return self.__authentication
    
    @property
    def id(self):
        return self.__user.id
        
    def create(self):
        authbean = TransactionBean.AuthenticationBean()
        auth = authbean.create_object()
        for property in TransactionBean.AuthenticationBean.properties:
            if str(property) != "id":
                try:
                    setattr(auth, str(property), getattr(self.__authentication, str(property)))
                except:
                    pass
        authbean.save()
        authbean.commit()
        authbean.close()
        
        userbean = self.__class__.bean()
        user = userbean.create_object()
        self.__user.id = user.id
        for property in userbean.properties:
            if str(property) != "id":
                try:
                    setattr(user, str(property), getattr(self.__user, str(property)))
                except:
                    pass
        userbean.save()
        userbean.commit()
        userbean.close()

class CreateAdministrator(CreateUser):
    userclass = User.Administrator
    bean = TransactionBean.AdministratorBean

class CreatePoolShopAdmin(CreateUser):
    userclass = User.PoolShopAdmin
    bean = TransactionBean.PoolShopAdminBean

class CreatePoolOwner(CreateUser):
    userclass = User.PoolOwner
    bean = TransactionBean.PoolOwnerBean

class EditUser(object):
    userclass = User.User
    bean = TransactionBean.UserBean
    
    def __init__(self, userid):
        self.__authentication = None
        self.__user = None
        self.__level = None
        self.__id = userid
        self.__is_authed = False
        
        authbean = TransactionBean.AuthenticationBean()
        self.__authentication = authbean.get_object({"id": userid})
        authbean.close()
        
        if self.__authentication != None:
            userbean = self.__class__.bean()
            self.__user = userbean.get_object({"id": self.__authentication.id})
            userbean.close()
            if self.user_info != None:
                self.__is_authed = True
                self.__level = getattr(User.UserTypes, str.upper(str(self.__user.__class__.__name__)))
    
    @property
    def user_info(self):
        return self.__user
        
    @property
    def auth_info(self):
        return self.__authentication
    
    @property
    def id(self):
        return self.__id
        
    def save(self):
        authbean = TransactionBean.AuthenticationBean()
        auth = authbean.get_object({"id": self.__id})
        for property in TransactionBean.AuthenticationBean.properties:
            if str(property) != "id":
                try:
                    setattr(auth, str(property), getattr(self.__authentication, str(property)))
                except:
                    pass
        authbean.save()
        authbean.commit()
        authbean.close()
        
        userbean = self.__class__.bean()
        user = userbean.get_object({"id": self.__id})
        for property in userbean.properties:
            if str(property) != "id":
                try:
                    setattr(user, str(property), getattr(self.__user, str(property)))
                except:
                    pass
        userbean.save()
        userbean.commit()
        userbean.close()

class EditAdministrator(EditUser):
    userclass = User.Administrator
    bean = TransactionBean.AdministratorBean

class EditPoolShopAdmin(EditUser):
    userclass = User.PoolShopAdmin
    bean = TransactionBean.PoolShopAdminBean

class EditPoolOwner(EditUser):
    userclass = User.PoolOwner
    bean = TransactionBean.PoolOwnerBean
