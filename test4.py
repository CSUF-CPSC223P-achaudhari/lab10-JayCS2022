import unittest
import io
import sys
from unittest.mock import patch


from bots import *

class Test04_FIVE_ITEMS(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 *** FUNCTION CALL: cart = bot_clerk(['103','108','102','110','106']) *** EXPECT: cart = [['108', '3 Ring Binder'],['102', 'Pencils'],['106', 'Staples'],['103', 'Pens'],['110', 'Notepad']] ***
        """
        cart = bot_clerk(['103','108','102','110','106'])
        self.assertEqual(cart, [['108', '3 Ring Binder'],['102', 'Pencils'],['106', 'Staples'],['103', 'Pens'],['110', 'Notepad']])
        print()

if __name__ == '__main__':
    with open('test.txt', "w") as f:
        runner = unittest.TextTestRunner(f)
        unittest.main(testRunner=runner)
