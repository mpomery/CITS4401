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
        # Creating a new object, so return an empty one
        if id == None:
            self.object = self.__class__.obj()
            return
        
        
        # Get the objects properties
        properties = [prop for prop in dir(self.__class__.obj) if isinstance(getattr(self.__class__.obj, prop), property)]
        print("Properties")
        columns = []
        columnsstring = ""
        
        for p in properties:
            columnsstring += str(p) + ", "
            columns.append(str(p))
        columnsstring = columnsstring[0:-2]

        print("End Properties")
        
        con = None
        try:
            # read the object from the database
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            table = self.__class__.obj.__name__
            #TODO: Read * from self.__class__.__name__ table
            query = "SELECT " + columnsstring + " FROM " + table + " WHERE id=" + str(id) + ";"
            print(query)
            cur.execute(query)
            data = cur.fetchone()
            
            #TODO: Put read data into an object]
            self.object = self.__class__.obj(id)
            for i in range(len(columns)):
                p = columns[i]
                v = data[i]
                setattr(self.object, p, v)
            
            cur.close()
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
        returnid = None
        try:
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            table = self.__class__.obj.__name__
            properties = [prop for prop in dir(self.__class__.obj) if isinstance(getattr(self.__class__.obj, prop), property)]
            columns = ""
            values = []
            for p in properties:
                columns += str(p) + ", "
                values.append(getattr(self.object, p))
            columns = columns[0:-2]
            valuestring = ("?, " * len(values))[0:-2]
            print(columns)
            print(valuestring)
            print(values)
            query = "INSERT INTO " + table + " (" + columns + ") VALUES (" + valuestring + ");"
            
            print(query)
            print(str(tuple(values)))
            cur.execute(query, tuple(values))
            returnid = cur.lastrowid
            cur.close()
            con.commit()
        except sqlite3.Error, e:
                LogHandler.log_error("Database Issue: %s" % e.args[0])
        finally:
            if con:
                con.close()
        return returnid
    
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