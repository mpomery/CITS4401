import sqlite3
import LogHandler
import User
import PoolTestingUnit
import inspect


"""
Transaction Beans Simplify Reading and writing from the database
They should inherit code from the top TransactionBean object and make minimal changes to
point themselves at the right table
"""
class TransactionBean(object):
    obj = None
    
    """
    Loads an object out of the database and into an an object
    """
    def __init__(self, id=None):
        LogHandler.log_warning("Loading Bean: " + str(self.__class__.__name__))
        LogHandler.log_warning("Loading Bean: " + str(self.__class__.obj))
        LogHandler.log_warning("Loading Bean: " + str(self.__class__.obj.__name__))
        # Creating a new object, so return an empty one
        # Get the objects properties
        properties = [prop for prop in dir(self.__class__.obj) if isinstance(getattr(self.__class__.obj, prop), property)]
        print("Properties")
        for p in properties:
            print(str(p))
        print("End Properties")
        
        if id == None:
            self.object = self.__class__.obj()
            return
        
        con = None
        
        try:
            # read the object from the database
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            
            #TODO: Read * from self.__class__.__name__ table
            #TODO: Put read data into an object
            
            self.object = self.__class__.obj(id)
            #in vars(self.__class__.obj).iteritems():
            
            cur.execute('SELECT SQLITE_VERSION()')
        except sqlite3.Error, e:
                LogHandler.log_error("Database Issue: %s" % e.args[0])
        finally:
            if con:
                con.close()
    
    """
    Get the object(s) the bean has loaded
    """
    def get_object(self):
        return self.object
    
    """
    Saves any changes to the object back to the database, returns its id
    """
    def commit(self, msg=None):
        properties = [prop for prop in dir(self.__class__.obj) if isinstance(getattr(self.__class__.obj, prop), property)]
        for p in properties:
            print (str(p) + ": " + str(getattr(self.object, p)))
        #TODO: Save object back into database
        pass
    
    """
    Cancels any changes to the object
    """
    def rollback(self, msg=None):
        pass


class UserBean(TransactionBean):
    obj = User.User

class AdministratorBean(UserBean):
    pass

class PoolShopBean(UserBean):
    pass

class PoolOwnerBean(UserBean):
    pass

class PoolTestingUnitBean(TransactionBean):
    pass