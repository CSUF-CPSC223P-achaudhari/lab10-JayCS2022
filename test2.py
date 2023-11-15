import unittest
import io
import sys
from unittest.mock import patch


from bots import *

class Test02_ONE_ITEM(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** FUNCTION CALL: cart = bot_clerk(['104']) *** EXPECT: cart = [['104', 'Graph Paper']] ***
        """
        cart = bot_clerk(['104'])
        self.assertEqual(cart, [['104', 'Graph Paper']])
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
