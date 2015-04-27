import unittest
import TransactionBean

class TransactionBeanTest(unittest.TestCase):
    def test_create_user(self):
        # Test Insert Variables
        title = "Mr"
        name = "Mitchell Pomery"
        address = "4/36 Abba St, Beta, Charlie 6512"
        email_address = "aaa@aaaa.cas"
        mobile_number = "0123456789"
        phone_number = "9876543210"
        
        # Create a new bean
        tb = TransactionBean.UserBean()
        user = tb.get_object()
        # Update Info
        user.title = title
        user.name = name
        user.address = address
        user.email_address = email_address
        user.mobile_number = mobile_number
        user.phone_number = phone_number
        # Save Info
        id = tb.commit()
        
        # Load the user again
        tb = TransactionBean.UserBean({"id": id})
        user = tb.get_object()
        
        #Check the values are right
        self.assertEqual(user.title, title)
        self.assertEqual(user.name, name)
        self.assertEqual(user.address, address)
        self.assertEqual(user.email_address, email_address)
        self.assertEqual(user.mobile_number, mobile_number)
        self.assertEqual(user.phone_number, phone_number)
        
    def test_edit_user(self):
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
        user = tb.get_object()
        # Update Info
        user.title = title
        user.name = name
        user.address = address
        user.email_address = email_address
        user.mobile_number = mobile_number
        user.phone_number = phone_number
        # Save Info
        id = tb.commit()
        
        # Load the user again
        tb = TransactionBean.UserBean({"id": id})
        user = tb.get_object()
        # Update Info
        user.title = title2
        user.name = name2
        user.address = address2
        user.email_address = email_address2
        user.mobile_number = mobile_number2
        user.phone_number = phone_number2
        
        # Load the user again
        tb = TransactionBean.UserBean({"id": id})
        user = tb.get_object()
        #Check the values are right
        self.assertEqual(user.title, title)
        self.assertEqual(user.name, name)
        self.assertEqual(user.address, address)
        self.assertEqual(user.email_address, email_address)
        self.assertEqual(user.mobile_number, mobile_number)
        self.assertEqual(user.phone_number, phone_number)
        
        
    def test_create_administrator(self):
        # Test Insert Variables
        title = "Mr"
        name = "Mitchell Pomery"
        address = "4/36 Abba St, Beta, Charlie 6512"
        email_address = "aaa@aaaa.cas"
        mobile_number = "0123456789"
        phone_number = "9876543210"
        
        # Create a new bean
        tb = TransactionBean.AdministratorBean()
        user = tb.get_object()
        # Update Info
        user.title = title
        user.name = name
        user.address = address
        user.email_address = email_address
        user.mobile_number = mobile_number
        user.phone_number = phone_number
        # Save Info
        id = tb.commit()
        
        # Load the user again
        tb = TransactionBean.AdministratorBean({"id": id})
        user = tb.get_object()
        
        #Check the values are right
        self.assertEqual(user.title, title)
        self.assertEqual(user.name, name)
        self.assertEqual(user.address, address)
        self.assertEqual(user.email_address, email_address)
        self.assertEqual(user.mobile_number, mobile_number)
        self.assertEqual(user.phone_number, phone_number)

if __name__ == '__main__':
    unittest.main()

