import unittest
import TransactionBean
import LogHandler

class TransactionBeanTest(unittest.TestCase):
    
    def test_basic_create_commit(self):
        LogHandler.log_error("STARTING: test_basic_create_commit")
        testname = "Hagrid"
        tb = TransactionBean.UserBean()
        user = tb.create_object()
        user.name = testname
        id = user.id
        tb.save()
        tb.commit()
        tb = TransactionBean.UserBean()
        user = tb.get_object({"id": id})
        self.assertEquals(testname, user.name)
    
    def test_basic_create_rollback(self):
        LogHandler.log_error("STARTING: test_basic_create_commit")
        testname = "Hagrid"
        tb = TransactionBean.UserBean()
        user = tb.create_object()
        user.name = testname
        id = user.id
        tb.save()
        tb.rollback()
        tb = TransactionBean.UserBean()
        user = tb.get_object({"id": id})
        self.assertEquals(user, None)
    
    def test_basic_create_update(self):
        LogHandler.log_error("STARTING: test_basic_create_commit")
        testname1 = "Hagrid"
        testname2 = "Harry"
        tb = TransactionBean.UserBean()
        user = tb.create_object()
        user.name = testname1
        id = user.id
        tb.save()
        tb.commit()
        
        tb = TransactionBean.UserBean()
        user = tb.get_object({"id": id})
        user.name = testname2
        tb.save()
        tb.commit()
        
        tb = TransactionBean.UserBean()
        user = tb.get_object({"id": id})
        
        self.assertEquals(testname2, user.name)
    
    def test_nonexistant_user(self):
        LogHandler.log_error("STARTING: test_basic_create_commit")
        tb = TransactionBean.UserBean()
        user = tb.get_object({"id": -1})
        self.assertEquals(None, user)
    
    def test_create_user(self):
        LogHandler.log_error("STARTING: test_basic_create_commit")
        # Test Insert Variables
        title = "Mr"
        name = "Mitchell Pomery"
        address = "4/36 Abba St, Beta, Charlie 6512"
        email_address = "aaa@aaaa.cas"
        mobile_number = "0123456789"
        phone_number = "9876543210"
        
        # Create a new bean
        tb = TransactionBean.UserBean()
        user = tb.create_object()
        # Update Info
        id = user.id
        user.title = title
        user.name = name
        user.address = address
        user.email_address = email_address
        user.mobile_number = mobile_number
        user.phone_number = phone_number
        
        tb.save()
        tb.commit()
        tb.close()
        
        # Load the user again
        tb = TransactionBean.UserBean()
        user = tb.get_object({"id": id})
        
        #Check the values are right
        self.assertEqual(user.title, title)
        self.assertEqual(user.name, name)
        self.assertEqual(user.address, address)
        self.assertEqual(user.email_address, email_address)
        self.assertEqual(user.mobile_number, mobile_number)
        self.assertEqual(user.phone_number, phone_number)
    
    def test_edit_user(self):
        LogHandler.log_error("STARTING: test_basic_create_commit")
        # Test Insert Variables
        title = "Mr"
        name = "Mitchell Pomery"
        address = "4/36 Abba St, Beta, Charlie 6512"
        email_address = "aaa@aaaa.cas"
        mobile_number = "0123456789"
        phone_number = "9876543210"
        
        title2 = "Miss"
        name2 = "Abagail Storm"
        address2 = "1/36 Abba St, Beta, Charlie 1337"
        email_address2 = "bb@a.co"
        mobile_number2 = "3214569870"
        phone_number2 = "1236547890"
        
        # Create a new bean
        tb = TransactionBean.UserBean()
        user = tb.create_object()
        # Update Info
        id = user.id
        user.title = title
        user.name = name
        user.address = address
        user.email_address = email_address
        user.mobile_number = mobile_number
        user.phone_number = phone_number
        # Save Info
        tb.save()
        tb.commit()
        tb.close()
        
        # Load the user again
        tb = TransactionBean.UserBean()
        user = tb.get_object({"id": id})
        # Update Info
        user.title = title2
        user.name = name2
        user.address = address2
        user.email_address = email_address2
        user.mobile_number = mobile_number2
        user.phone_number = phone_number2
        
        tb.save()
        tb.commit()
        tb.close()
        
        # Load the user again
        tb = TransactionBean.UserBean()
        user = tb.get_object({"id": id})
        #Check the values are right
        self.assertEqual(user.title, title2)
        self.assertEqual(user.name, name2)
        self.assertEqual(user.address, address2)
        self.assertEqual(user.email_address, email_address2)
        self.assertEqual(user.mobile_number, mobile_number2)
        self.assertEqual(user.phone_number, phone_number2)
    
    def test_edit_administrator(self):
        LogHandler.log_error("STARTING: test_basic_create_commit")
        # Test Insert Variables
        title = "Mr"
        name = "Mitchell Pomery"
        address = "4/36 Abba St, Beta, Charlie 6512"
        email_address = "aaa@aaaa.cas"
        mobile_number = "0123456789"
        phone_number = "9876543210"
        
        title2 = "Miss"
        name2 = "Abagail Storm"
        address2 = "1/36 Abba St, Beta, Charlie 1337"
        email_address2 = "bb@a.co"
        mobile_number2 = "3214569870"
        phone_number2 = "1236547890"
        
        # Create a new bean
        tb = TransactionBean.AdministratorBean()
        user = tb.create_object()
        # Update Info
        id = user.id
        user.title = title
        user.name = name
        user.address = address
        user.email_address = email_address
        user.mobile_number = mobile_number
        user.phone_number = phone_number
        # Save Info
        tb.save()
        tb.commit()
        tb.close()
        
        # Load the user again
        tb = TransactionBean.AdministratorBean()
        user = tb.get_object({"id": id})
        # Update Info
        user.title = title2
        user.name = name2
        user.address = address2
        user.email_address = email_address2
        user.mobile_number = mobile_number2
        user.phone_number = phone_number2
        
        tb.save()
        tb.commit()
        tb.close()
        
        # Load the user again
        tb = TransactionBean.AdministratorBean()
        user = tb.get_object({"id": id})
        #Check the values are right
        self.assertEqual(user.title, title2)
        self.assertEqual(user.name, name2)
        self.assertEqual(user.address, address2)
        self.assertEqual(user.email_address, email_address2)
        self.assertEqual(user.mobile_number, mobile_number2)
        self.assertEqual(user.phone_number, phone_number2)
    
    def test_create_administrator(self):
        LogHandler.log_error("STARTING: test_basic_create_commit")
        # Test Insert Variables
        title = "Mr"
        name = "Mitchell Pomery"
        address = "4/36 Abba St, Beta, Charlie 6512"
        email_address = "aaa@aaaa.cas"
        mobile_number = "0123456789"
        phone_number = "9876543210"
        
        # Create a new bean
        tb = TransactionBean.AdministratorBean()
        user = tb.create_object()
        # Update Info
        id = user.id
        user.title = title
        user.name = name
        user.address = address
        user.email_address = email_address
        user.mobile_number = mobile_number
        user.phone_number = phone_number
        # Save Info
        tb.save()
        tb.commit()
        tb.close()
        
        
        # Load the user again
        tb = TransactionBean.AdministratorBean()
        user = tb.get_object({"id": id})
        
        #Check the values are right
        self.assertEqual(user.title, title)
        self.assertEqual(user.name, name)
        self.assertEqual(user.address, address)
        self.assertEqual(user.email_address, email_address)
        self.assertEqual(user.mobile_number, mobile_number)
        self.assertEqual(user.phone_number, phone_number)

if __name__ == '__main__':
    unittest.main()

