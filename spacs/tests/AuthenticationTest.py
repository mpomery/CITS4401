import unittest
import Authentication
import AuthUser
from User import UserTypes
import TransactionBean

class AthenticationTest(unittest.TestCase):
    
    def test_create_user(self):
        test_username = "Hagrid"
        test_password = "urawizard"
        new_user = AuthUser.CreateAdministrator()
        new_user.auth_info.username = test_username
        new_user.auth_info.password = test_password
        new_user.create()
        authattempt = AuthUser.AuthAdministrator(test_username, test_password)
        self.assertTrue(authattempt.is_authed)

if __name__ == '__main__':
    unittest.main()