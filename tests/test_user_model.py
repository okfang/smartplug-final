import unittest

from  myapp.models import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User('fang', 'abc')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User('fang', 'abc')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User('fang', 'abc')
        self.assertTrue(u.verify_password('abc'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User('dong', '123')
        u2 = User('fang' , '123')
        self.assertTrue(u.password_hash != u2.password_hash)