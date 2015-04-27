import sqlite3
import LogHandler
import User
import PoolTestingUnit
import inspect

"""
Avoid using this
"""
def get_properties():
    return [prop for prop in dir(self.__class__.obj) if isinstance(getattr(self.__class__.obj, prop), property)]


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
    Provide an empty dictionary to search for everything
    """
    def __init__(self, searchterms = None):
        # Creating a new object, so return an empty one
        #print("RUNNING")
        self.insert = False
        if searchterms == None:
            self.insert = True
            self.object = self.__class__.obj()
            return
        
        if self.__class__.table == None:
            self.__class__.table = self.__class__.obj.__name__
        
        selecting = ""
        for porperty in self.__class__.properties:
            selecting += porperty + ", "
        selecting = selecting[0:-2]
        
        search = ""
        for key, val in searchterms.iteritems():
            search += "AND " + str(key) + "=" + str(val) + " "
        search = search[4:]
        
        limiter = ""
        for key, val in self.__class__.fixed.iteritems():
            limiter += "AND " + str(key) + "=" + str(val) + " "
        
        # Read record from table
        selectquery = "SELECT " + selecting + " FROM " + self.__class__.table + \
                " WHERE " + search + " " +  limiter + ";"
        
        
        con = None
        try:
            # read the object from the database
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute(selectquery)
            data = cur.fetchall()
            # Put read data into an object
            if len(data) == 0:
                self.object = None
            else:
                self.object = []
                for i in range(len(data)):
                    new = self.__class__.obj()
                    for j in range(len(self.__class__.properties)):
                        p = self.__class__.properties[j]
                        v = data[i][j]
                        #print("AA: " + str(p) + ":" + str(v))
                        setattr(new, str(p), v)
                    for key, val in searchterms.iteritems():
                        setattr(new, str(key), val)
                    self.object.append(new)
                if len(self.object) == 1:
                    self.object = self.object[0]
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
        
        if self.__class__.table == None:
            self.__class__.table = self.__class__.obj.__name__
        
        if self.insert:
            valuestring = "?, " * (len(self.__class__.properties) + len(self.__class__.fixed))
            valuestring = valuestring[0:-2]
            fields = ""
            values = []
            for property in self.__class__.properties:
                fields += str(property) + ", "
                values.append(getattr(self.object, property))
            for key, val in self.__class__.fixed.iteritems():
                fields += str(key) + ", "
                values.append(val)
            fields = fields[0:-2]
            query = "INSERT INTO " + self.__class__.table + " (" + fields + \
                    ") VALUES (" + valuestring + ");"
        else:
            query = ""
        
        #print("QUERY: " + str(query))
        #print("PROPERTIES: " + str(tuple(values)))
        
        try:
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            cur.execute(query, values)
            returnid = cur.lastrowid
            #print("RID: " + str(returnid))
            cur.close()
            con.commit()
        except sqlite3.Error, e:
                LogHandler.log_error("Database Issue: %s" % e.args[0])
        finally:
            if con:
                con.close()
        return returnid
        return 1
    
    """
    Cancels any changes to the object
    """
    def rollback(self, msg=None):
        pass


class UserBean(TransactionBean):
    properties = [ "address",
            "email_address",
            "mobile_number",
            "name",
            "phone_number",
            "title"
        ]
    fixed = {}
    obj = User.User
    table = "User"

class AdministratorBean(UserBean):
    fixed = {"level": 9}

class PoolShopBean(UserBean):
    fixed = {"level": 7}

class PoolOwnerBean(UserBean):
    fixed = {"level": 1}

class PoolTestingUnitBean(TransactionBean):
    pass