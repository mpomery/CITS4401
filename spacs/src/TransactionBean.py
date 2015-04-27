import sqlite3
import LogHandler
import User
import PoolTestingUnit
import inspect


#TODO: Comment this class
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
        if self.__class__.selectquery == None or id==None:
            # Creating a new object, so return an empty one
            if id == None:
                self.object = self.__class__.obj()
                return
            
            # Get the objects properties
            properties = [prop for prop in dir(self.__class__.obj) if isinstance(getattr(self.__class__.obj, prop), property)]
            self.__class__.colums = []
            columnsstring = ""
            # Create the SQL
            for p in properties:
                columnsstring += str(p) + ", "
                self.__class__.colums.append(str(p))
            columnsstring = columnsstring[0:-2]
            
            if self.__class__.table == None:
                self.__class__.table = self.__class__.obj.__name__
            # Read record from table
            self.__class__.selectquery = "SELECT " + columnsstring + " FROM " + self.__class__.table + " WHERE id=" + str(id) + ";"
        
        print("QUERY: " + str(self.__class__.selectquery))
        
        con = None
        try:
            # read the object from the database
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute(self.__class__.selectquery)
            data = cur.fetchone()
            # Put read data into an object
            self.object = self.__class__.obj()
            print(data)
            if data != None:
                for i in range(len(self.__class__.colums)):
                    p = self.__class__.colums[i]
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
            query = "INSERT INTO " + table + " (" + columns + ") VALUES (" + valuestring + ");"
            cur.execute(query, tuple(values))
            returnid = cur.lastrowid
            print("RID: " + str(returnid))
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
    selectquery = None
    commitquery = None
    table = "User"
    
    def __init__(self, id=None):
        super(UserBean, self ).__init__(id)

class AdministratorBean(UserBean):
    def __init__(self, id=None):
        if id != None:
            self.__class__.selectquery = "SELECT address, email_address, id, mobile_number," + \
                    "name, phone_number, title FROM User WHERE id=" + str(id) + " AND level=9;"
            self.__class__.colums = ["address", "email_address", "id", "mobile_number",
                    "name", "phone_number", "title"]
        super(UserBean, self ).__init__(id)
    def commit(self):
        

class PoolShopBean(UserBean):
    pass

class PoolOwnerBean(UserBean):
    pass

class PoolTestingUnitBean(TransactionBean):
    pass