import unittest
import io
import sys
from unittest.mock import patch


from bots import *

class Test05_TEN_ITEMS(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test05 *** FUNCTION CALL: cart = bot_clerk(['106','102','108','109','103','101','110','104','107','105']) *** EXPECT: cart = [['108', '3 Ring Binder'], ['102', 'Pencils'], ['101', 'Notebook Paper'], ['106', 'Staples'], ['109', 'Printer Paper'], ['110', 'Notepad'], ['105', 'Paper Clips'], ['103', 'Pens'], ['104', 'Graph Paper'], ['107', 'Stapler']] ***
        """
        cart = bot_clerk(['106','102','108','109','103','101','110','104','107','105'])
        self.assertEqual(cart, [['108', '3 Ring Binder'], ['102', 'Pencils'], ['101', 'Notebook Paper'], ['106', 'Staples'], ['109', 'Printer Paper'], ['110', 'Notepad'], ['105', 'Paper Clips'], ['103', 'Pens'], ['104', 'Graph Paper'], ['107', 'Stapler']])
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
