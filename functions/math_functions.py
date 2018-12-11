""" module math_functions """

import math
PI = math.pi

def area_of_circle(radius):
    """ determines the area of a circle with a 'radius' input """
    radius2 = radius**2
    area = radius2 * PI
    return radius


# def surface_area_of_cube(side):
#     """ determines the surface area of a cube with a 'side' input """
#     surfaceArea = 6 * side
#     return side

