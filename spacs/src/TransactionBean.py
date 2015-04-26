import sqlite3
import LogHandler
import User
import PoolTestingUnit


"""
Transaction Beans Simplify Reading and writing from the database
They should inherit code from the top TransactionBean object and make minimal changes to
point themselves at the right table
"""
class TransactionBean(object):
    
    tablename = __name__
    
    """
    Loads an object out of the database and into an an object
    """
    def __init__(self, id=None):
        LogHandler.log_warning("")
        if id == None:
            # Return an empty object
            return
        con = None
        try:
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            
            cur.execute('SELECT SQLITE_VERSION()')
        except sqlite3.Error, e:
                LogHandler.log_error("Database Issue: %s" % e.args[0])
        finally:
            if con:
                con.close()
    
    """
    Saves any changes to the object back to the database
    """
    def commit(self):
        
        pass
    
    """
    Cancels any changes to the object
    """
    def rollback(self):
        pass


class UserBean(TransactionBean):
    pass

class AdministratorBean(UserBean):
    pass

class PoolShopBean(UserBean):
    pass

class PoolOwnerBean(UserBean):
    pass

class PoolTestingUnitBean(TransactionBean):
    pass