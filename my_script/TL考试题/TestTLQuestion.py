# /usr/bin/evn python
# coding:utf-8

import unittest
from TLQuestion import *


class TestTLQuestion(unittest.TestCase):
    """测试最低价格"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_lowest_price_1(self):
        self.assertEqual(TLQuestion(2,2,2,1,1).lowest_price(), 51.6, 'test lowest_price fail')

    def test_lowest_price_2(self):
        self.assertEqual(TLQuestion(book_one=1, book_two=2).lowest_price(), 23.2, 'test lowest_price fail')

    def test_lowest_price_3(self):
        self.assertEqual(TLQuestion(book_one=3, book_two=1, book_three=2).lowest_price(), 44.8, 'test lowest_price fail')
if __name__=="__main__":
    unittest.main()