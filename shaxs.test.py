import unittest
from shaxs import Shaxs
class ShaxsTest(unittest.TestCase):
    def setUp(self):
        ism = 'ali'
        familiya = 'usmonjonov'
        passport = 'AA000'
        tyil = 2009
        self.user1 = Shaxs(ism,familiya,passport,tyil)

    def test_create(self):
        self.assertIsNotNone(self.user1.ism)
        self.assertIsNotNone(self.user1.familiya)
        self.assertIsNotNone(self.user1.passport)
        self.assertIsNotNone(self.user1.tyil)
unittest.main()