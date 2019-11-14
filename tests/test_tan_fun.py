'''import unittest class to enable all the functionality to test the cases'''
import unittest
from unittest import TestCase
from src.cal import tan_func


class TestTan(TestCase):
    """class to test the use case"""

    def test_tan_fun_pos(self):
        """function to test against negative input"""
        self.assertEqual(tan_func.tan_fun(90), -1.995200412)

    def test_tan_fun_neg(self):
        """function to test against positive input"""
        self.assertEqual(tan_func.tan_fun(-90), 1.995200412)

    def test_tan_fun_zero(self):
        """function to test against zero input"""
        self.assertEqual(tan_func.tan_fun(0), 0.0)

    def test_tan_fun(self):
        """function to test against random input"""
        self.assertEqual(tan_func.tan_fun(56), -0.611273688)


if __name__ == '__main__':
    unittest.main()
