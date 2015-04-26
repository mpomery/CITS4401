import unittest
import Validator

class ValidatorTest(unittest.TestCase):
    def test_email_valid_inputs(self):
        emails = ["email@example.com",
                "firstname.lastname@example.com",
                "email@subdomain.example.com",
                "firstname+lastname@example.com",
                "email@123.123.123.123",
                "email@[123.123.123.123]",
                "1234567890@example.com",
                "email@example-one.com",
                "_______@example.com",
                "email@example.name",
                "email@example.museum",
                "email@example.co.jp",
                "firstname-lastname@example.com"
        ]
        failed = []
        for email in emails:
            if not Validator.is_email(email):
                failed.append(email)
        if len(failed) > 0:
            self.fail("Failed to Validate: " + str(failed))
    
    def test_email_invalid_inputs(self):
        emails = ["plainaddress",
                "#@%^%#$@#$@#.com",
                "@example.com",
                "Joe Smith <email@example.com>",
                "email.example.com",
                "email@example@example.com",
                ".email@example.com",
                "email.@example.com",
                "email..email@example.com",
                "?????@example.com",
                "email@example.com (Joe Smith)",
                "email@example",
                "email@-example.com",
                "email@example.web",
                "email@111.222.333.44444",
                "email@example..com",
                "Abc..123@example.com",
        ]
        failed = []
        for email in emails:
            if not Validator.is_email(email):
                failed.append(email)
        if len(failed) > 0:
            self.fail("Accidentally Validated: " + str(failed))

if __name__ == '__main__':
    unittest.main()