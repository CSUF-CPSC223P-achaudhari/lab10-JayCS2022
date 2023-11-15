import unittest
import io
import sys
from unittest.mock import patch


from bots import *

class Test01_EMPTY_ITEM(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test01 *** FUNCTION CALL:  *** EXPECT: cart = [] ***
        """
        cart = bot_clerk([])
        self.assertEqual(cart, [])
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
