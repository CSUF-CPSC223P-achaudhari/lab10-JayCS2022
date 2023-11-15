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

class Test02_ONE_ITEM(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test02 *** FUNCTION CALL: cart = bot_clerk(['104']) *** EXPECT: cart = [['104', 'Graph Paper']] ***
        """
        cart = bot_clerk(['104'])
        self.assertEqual(cart, [['104', 'Graph Paper']])
        print()

class Test03_THREE_ITEMS(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test03 *** FUNCTION CALL: cart = bot_clerk(['106','109','102']) *** EXPECT: cart = [['109', 'Printer Paper'], ['102', 'Pencils'], ['106', 'Staples']] ***
        """
        cart = bot_clerk(['106','109','102'])
        self.assertEqual(cart, [['109', 'Printer Paper'], ['102', 'Pencils'], ['106', 'Staples']])
        print()

class Test04_FIVE_ITEMS(unittest.TestCase):
    def test_list_int(self):
        """
        *** Test04 *** FUNCTION CALL: cart = bot_clerk(['103','108','102','110','106']) *** EXPECT: cart = [['108', '3 Ring Binder'],['102', 'Pencils'],['106', 'Staples'],['103', 'Pens'],['110', 'Notepad']] ***
        """
        cart = bot_clerk(['103','108','102','110','106'])
        self.assertEqual(cart, [['108', '3 Ring Binder'],['102', 'Pencils'],['106', 'Staples'],['103', 'Pens'],['110', 'Notepad']])
        print()

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