import unittest
from title import juft_son
class JuftTest(unittest.TestCase):
    def test_juft(self):
        self.assertTrue(juft_son(4))
    def test_false(self):
        self.assertFalse(juft_son(7))
unittest.main()