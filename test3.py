import unittest
import io
import sys
from unittest.mock import patch


from bots import *

class Test03_THREE_ITEMS(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** FUNCTION CALL: cart = bot_clerk(['106','109','102']) *** EXPECT: cart = [['109', 'Printer Paper'], ['102', 'Pencils'], ['106', 'Staples']] ***
        """
        cart = bot_clerk(['106','109','102'])
        self.assertEqual(cart, [['109', 'Printer Paper'], ['102', 'Pencils'], ['106', 'Staples']])
        print()


if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
