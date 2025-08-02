#https://github.com/dmertis/lab10-DD-FM
#Partner 1: Demetri Delerme
#Partner 2: Frank Maronas

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(7, 5), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(5,2), 10)
        self.assertEqual(mul(-2,4), -8)
        self.assertEqual(mul(-3,-7), 21)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,8), 4.0)
        self.assertEqual(div(-2,10), -5.0)
        self.assertEqual(div(-1, -3),3.0)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertEqual(logarithm(1, 10), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 1)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0,5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4), 5.0)
        self.assertEqual(hypotenuse(-3,4), 5.0)
        self.assertEqual(hypotenuse(-6,-8), 10.0)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(25), 5)
    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()