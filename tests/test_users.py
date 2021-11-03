import unittest
from user import add_user

class TestUsers(unittest.TestCase):

    def test_add_user(self):
        self.assertEqual(add_user('JR'), True)
        self.assertEqual(add_user(66), False)