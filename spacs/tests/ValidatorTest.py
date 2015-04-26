import unittest
import Validator

class ValidatorTest(unittest.TestCase):
    def test_email_valid_inputs(self):
        self.assertTrue(Validator.is_email("email@example.com"))
        self.assertTrue(Validator.is_email("firstname.lastname@example.com"))
        self.assertTrue(Validator.is_email("email@subdomain.example.com"))
        self.assertTrue(Validator.is_email("firstname+lastname@example.com"))
        self.assertTrue(Validator.is_email("email@123.123.123.123"))
        self.assertTrue(Validator.is_email("email@[123.123.123.123]"))
        self.assertTrue(Validator.is_email("1234567890@example.com"))
        self.assertTrue(Validator.is_email("email@example-one.com"))
        self.assertTrue(Validator.is_email("_______@example.com"))
        self.assertTrue(Validator.is_email("email@example.name"))
        self.assertTrue(Validator.is_email("email@example.museum"))
        self.assertTrue(Validator.is_email("email@example.co.jp"))
        self.assertTrue(Validator.is_email("firstname-lastname@example.com"))
    
    def test_email_invalid_inputs(self):
        self.assertFalse(Validator.is_email("plainaddress"))
        self.assertFalse(Validator.is_email("#@%^%#$@#$@#.com"))
        self.assertFalse(Validator.is_email("@example.com"))
        self.assertFalse(Validator.is_email("Joe Smith <email@example.com>"))
        self.assertFalse(Validator.is_email("email.example.com"))
        self.assertFalse(Validator.is_email("email@example@example.com"))
        self.assertFalse(Validator.is_email(".email@example.com"))
        self.assertFalse(Validator.is_email("email.@example.com"))
        self.assertFalse(Validator.is_email("email..email@example.com"))
        self.assertFalse(Validator.is_email("?????@example.com"))
        self.assertFalse(Validator.is_email("email@example.com (Joe Smith)"))
        self.assertFalse(Validator.is_email("email@example"))
        self.assertFalse(Validator.is_email("email@-example.com"))
        self.assertFalse(Validator.is_email("email@example.web"))
        self.assertFalse(Validator.is_email("email@111.222.333.44444"))
        self.assertFalse(Validator.is_email("email@example..com"))
        self.assertFalse(Validator.is_email("Abc..123@example.com"))

if __name__ == '__main__':
    unittest.main()