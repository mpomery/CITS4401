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
    id_property = ""
    properties = []
    fixed = {}
    obj = None
    table = None
    
    """
    Connects to the database
    """
    def __init__(self):
        if self.__class__.table == None:
            self.__class__.table = self.__class__.obj.__name__
        self.connection = None
        self.cursor = None
        
        # Connect to the database
        try:
            LogHandler.log_info("Database: Open(" + str(self.__class__.__name__) + ")")
            self.con = sqlite3.connect('database.db')
            self.cur = self.con.cursor()
        except sqlite3.Error, e:
            LogHandler.log_error("Database: Exception: %s" % e.args[0])
    
    #TODO: Make this a property somehow
    """
    Create a new object in the database and return it (with its id set)
    """
    def create_object(self):
        LogHandler.log_info("Database: Create(" + str(self.__class__.__name__) + ")")
        new_object = self.__class__.obj()
        self.objects = [new_object]
        
        valuestring = "?, " * (len(self.__class__.properties) + len(self.__class__.fixed))
        valuestring = valuestring[0:-2]
        fields = ""
        values = []
        
        for property in self.__class__.properties:
            fields += str(property) + ", "
            values.append(getattr(new_object, property))
        
        for key, val in self.__class__.fixed.iteritems():
            fields += str(key) + ", "
            values.append(val)
        fields = fields[0:-2]
        
        query = "INSERT INTO " + self.__class__.table + " (" + fields + \
                ") VALUES (" + valuestring + ");"
        new_object
        try:
            LogHandler.log_info("Database: Create(" + str(self.__class__.__name__) + "): Query:" + query)
            LogHandler.log_info("Database: Create(" + str(self.__class__.__name__) + "): Values:" + str(values))
            self.cur.execute(query, values)
            returnid = self.cur.lastrowid
            setattr(new_object, str(self.__class__.id_property), returnid)
        except sqlite3.Error, e:
            LogHandler.log_error("Database: Exception: %s" % e.args[0])
        
        return new_object
    
    #TODO: Make this a property somehow
    """
    Get the first object found using the search terms
    """
    def get_object(self, searchterms = None):
        self.objects = self.get_objects(searchterms, 1, None)
        if self.objects == None:
            return None
        else:
            return self.objects[0]
    
    #TODO: Make this a property somehow
    """
    Get a list of objects found using the search terms
    """
    def get_objects(self, searchterms = None, limit = None, start = None):
        selecting = ""
        for porperty in self.__class__.properties:
            selecting += porperty + ", "
        selecting = selecting[0:-2]
        
        search = ""
        if searchterms != None:
            for key, val in searchterms.iteritems():
                search += "AND " + str(key) + "=" + str(val) + " "
            search = search[4:]
        else:
            search = "1==1"
        
        limiter = ""
        for key, val in self.__class__.fixed.iteritems():
            limiter += "AND " + str(key) + "=" + str(val) + " "
        
        # Read record from table
        selectquery = "SELECT " + selecting + " FROM " + self.__class__.table + \
                " WHERE " + search + " " +  limiter + ";"
        data = None
        try:
            LogHandler.log_info("Database: Select(" + str(self.__class__.__name__) + "): "+ selectquery)
            self.cur.execute(selectquery)
            data = self.cur.fetchall()
        except sqlite3.Error, e:
            LogHandler.log_error("Database: Exception: %s" % e.args[0])
        
        if data == None or len(data) == 0:
            return None
        else:
            self.objects = []
            for i in range(len(data)):
                new = self.__class__.obj()
                for j in range(len(self.__class__.properties)):
                    p = self.__class__.properties[j]
                    v = data[i][j]
                    try:
                        setattr(new, str(p), v)
                    except ValueError, ve:
                        LogHandler.log_error("Database: Select: Exception: %s" % ve.args[0])
                for key, val in searchterms.iteritems():
                    setattr(new, str(key), val)
                self.objects.append(new)
        return self.objects
    
    """
    Close the transaction. Doesn't save any changes not committed
    """
    def close(self, msg=None):
        try:
            LogHandler.log_info("Database: Close(" + str(self.__class__.__name__) + "): " + str(msg))
            self.con.close()
        except sqlite3.Error, e:
            LogHandler.log_error("Database: Exception: %s" % e.args[0])
    
    """
    Put changes back into the database
    """
    def save(self, msg=None):
        valuestring = "?, " * (len(self.__class__.properties) + len(self.__class__.fixed))
        valuestring = valuestring[0:-2]
        
        LogHandler.log_info("Database: Save(" + str(self.__class__.__name__) + "): ")
        for object in self.objects:
            fields = ""
            values = []
            
            for property in self.__class__.properties:
                fields += str(property) + "=?, "
                values.append(getattr(object, property))
            
            for key, val in self.__class__.fixed.iteritems():
                fields += str(key) + ", "
                values.append(val)
            fields = fields[0:-2]
            values.append(getattr(object, self.__class__.id_property))
            
            query = "UPDATE " + self.__class__.table + " SET " + fields + " WHERE " +\
                    str(self.__class__.id_property)+ "=?;"
            try:
                LogHandler.log_info("Database: Save(" + str(self.__class__.__name__) + "): "+ query)
                self.cur.execute(query, values)
                data = self.cur.fetchall()
            except sqlite3.Error, e:
                LogHandler.log_error("Database: Exception: %s" % e.args[0])
        pass
    
    """
    Commits any saved changes to the database
    """
    def commit(self, msg=None):
        try:
            LogHandler.log_info("Database: Commit(" + str(self.__class__.__name__) + "): " + str(msg))
            self.con.commit()
        except sqlite3.Error, e:
            LogHandler.log_error("Database: Exception: %s" % e.args[0])
    
    """
    Cancels any changes made to the database since the last commit
    """
    def rollback(self, msg=None):
        try:
            self.con.rollback()
        except sqlite3.Error, e:
            LogHandler.log_error("Database: Exception: %s" % e.args[0])

class UserBean(TransactionBean):
    id_property = "id"
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