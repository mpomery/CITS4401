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
        tb = TransactionBean.AdministratorBean(id)
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

