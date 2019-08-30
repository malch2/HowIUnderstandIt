# https://www.youtube.com/watch?v=1Lfv5tUGsn8

import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius>=0
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi*(2.1**2))
    
    def test_values(self):
        # Test to see how imporper inputs are handled
        self.assertRaises(ValueError, circle_area, -2)
    
    def test_type(self):
        # Type error when input is not a real number
        self.assertRaises(TypeError, circle_area, 3+5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")