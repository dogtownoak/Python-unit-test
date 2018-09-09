""" module math_functions """

import math

def area_of_circle(radius):
    """ determines the area of a circle with a 'radius' input """
    return None if radius <= 0 else math.pi * radius ** 2

def surface_area_of_cube(side):
    """ determines the surface area of a cube with a 'side' input """
    return None if side <= 0 else 6 * side ** 2
