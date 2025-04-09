#https://github.com/Man-Kai-Andrew-Ho/Lab10-AH-OC
#Partner 1 : Andrew Ho
#Partner 2 : Oscar Cao
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(3,1),2)
        self.assertEqual(subtract(1,3), -2)
        self.assertEqual(subtract(-1,-2), 1)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,3), 9)
        self.assertEqual(mul(30, -10), -300)
        self.assertEqual(mul(100, 100), 10000)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(-3, 100), -33.333333333)
        self.assertEqual(div(5, 10000), 2000)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
         # call division function inside, example:
         with self.assertRaises(ZeroDivisionError):
              div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 1000), 2.999999999)
        self.assertEqual(logarithm(2, 8),3)
        self.assertEqual(logarithm(2, 4), 2)


    def test_log_invalid_base(self): # 1 assertion
    #    # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(1,10)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(5,10), 11.180339887498949)
        self.assertEqual(hypotenuse(3,4), 5)
        self.assertAlmostEqual(hypotenuse(100, 123), 158.52129195)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(1), 1)
        self.assertAlmostEqual(square_root(1000), 31.6227766)
        self.assertEqual(square_root(10000), 100)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()