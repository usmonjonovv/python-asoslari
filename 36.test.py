import unittest
from highest import Kattasi
class HighestTest(unittest.TestCase):
    def test_high(self):
        self.assertEqual(Kattasi(7,5,4),"Ro'yxatdagi eng katta son: 7")
unittest.main()