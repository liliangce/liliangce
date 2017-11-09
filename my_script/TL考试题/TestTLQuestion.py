# /usr/bin/evn python
# coding:utf-8

import unittest
from TLQuestion import TotalPrice


class TestTLQuestion(unittest.TestCase):
    """测试最低价格"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_total_price_1(self):
        self.assertEqual(TotalPrice(2, 2, 2, 1, 1).total_price(), 51.2, 'test total_price fail')

    def test_total_price_2(self):
        self.assertEqual(TotalPrice(1, 2).total_price(), 23.2, 'test total_price fail')

    def test_total_price_3(self):
        self.assertEqual(TotalPrice(3, 1, 2).total_price(), 44.8, 'test total_price fail')

if __name__=="__main__":
    unittest.main()
