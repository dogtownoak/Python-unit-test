""" unit tests for math_functions """

import unittest
from functions import math_functions

class KnowledgeBase(unittest.TestCase):
    """ unit test class for math_funcitons) """

    def test_area_of_circle_sanity(self):
        """ area_of_circle(1) """
        # Captue the results of the function
        result = math_functions.area_of_circle(1)
        # Check for exptected output
        expected = 3.14
        self.assertEqual(expected, result)
    
    def test_surface_area_cube_sanityu2(self)
        """ area_of_


if __name__ == '__main__':
    unittest.main()
