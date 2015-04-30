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
        
    def test_edit_user(self):
        test_username1 = "Hrid"
        test_password1 = "lurzard"
        test_username2 = "BOb"
        test_password2 = "alob"
        new_user = AuthUser.CreateAdministrator()
        new_user.auth_info.username = test_username1
        new_user.auth_info.password = test_password1
        new_user.create()
        id = new_user.id
        
        edit = AuthUser.EditAdministrator(id)
        self.assertNotEqual(None, edit.auth_info)
        
        edit.auth_info.username = test_username2
        edit.auth_info.password = test_password2
        
        edit.save()
        
        authattempt = AuthUser.AuthAdministrator(test_username2, test_password2)
        self.assertTrue(authattempt.is_authed)
        self.assertEqual(authattempt.id, id)

if __name__ == '__main__':
    unittest.main()