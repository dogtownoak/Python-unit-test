""" unit tests for math_functions """

import unittest
from functions import math_functions

class KnowledgeBase(unittest.TestCase):
    """ unit test class for math_funcitons) """

    # Testing Area of Circle
    # 
    def test_area_of_circle_10_radius(self):
        """ area_of_circle(10) """
        # Captue the results of the function
        result = math_functions.area_of_circle(10)
        # Check for exptected output
        expected = 314.1592653589793
        self.assertEqual(expected, result)

        # Test area_of_circle() pi * r**2
    def test_area_of_circle_2_radius(self):
        """ area_of_circle(2) """
        # Captue the results of the function
        result = math_functions.area_of_circle(2)
        # Check for exptected output
        expected = 12.566370614359172
        self.assertEqual(expected, result)

        # Test area_of_circle() pi * r**2
    def test_area_of_circle_neg_radius(self):
        """ area_of_circle(-5) """
        # Captue the results of the function
        result = math_functions.area_of_circle(-5)
        # Check for exptected output
        expected = None
        self.assertEqual(expected, result)

        # Test area_of_circle() pi * r**2
    def test_area_of_circle_zero_radius(self):
        """ area_of_circle(0) """
        # Captue the results of the function
        result = math_functions.area_of_circle(0)
        # Check for exptected output
        expected = None
        self.assertEqual(expected, result)

    #
    # Testing Surface Area of Cube
    #
    # Test surface_area_of_cube() 6 * side ** 2
    def test_surface_area_of_cube_6(self):
        """ surface_area_of_cube(6)"""
        # Captue the results of the function
        result = math_functions.surface_area_of_cube(6)
        # Check for exptected output
        expected = 216
        self.assertEqual(expected, result)

    # Test surface_area_of_cube() 6 * side ** 2
    def test_surface_area_of_cube_half(self):
        """ surface_area_of_cube(0.5)"""
        # Captue the results of the function
        result = math_functions.surface_area_of_cube(0.5)
        # Check for exptected output
        expected = 1.5
        self.assertEqual(expected, result)

    # Test surface_area_of_cube() 6 * side ** 2
    def test_surface_area_of_cube_neg(self):
        """ surface_area_of_cube(-5)"""
        # Captue the results of the function
        result = math_functions.surface_area_of_cube(-5)
        # Check for exptected output
        expected = None
        self.assertEqual(expected, result)

    # Test surface_area_of_cube() 6 * side ** 2
    def test_surface_area_of_cube_zero(self):
        """ surface_area_of_cube(0)"""
        # Captue the results of the function
        result = math_functions.surface_area_of_cube(0)
        # Check for exptected output
        expected = None
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
