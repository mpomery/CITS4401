import unittest
import API

class ValidatorTest(unittest.TestCase):
    
    def test_auth_logout(self):
        ret = API.auth_logout({"username": "AAAA", "password": "aaaa"}, "")
        self.assertEquals(ret, {"error": "success"})
    
    def test_auth_login_success(self):
        pass
        
    def test_auth_login_fail(self):
        ret = API.auth_login({"username": "AAAA", "password": "aaaa"}, "")
        self.assertEquals(ret, {"error": "failure"})
    
    def test_auth_login_fail(self):
        ret = API.auth_login({"username": "AAAA", "password": "aaaa"}, "")
        self.assertEquals(ret, {"error": "failure"})

if __name__ == '__main__':
    unittest.main()