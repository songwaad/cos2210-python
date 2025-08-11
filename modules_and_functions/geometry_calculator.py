# geometry_calculator.py

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return 3.14 * radius ** 2

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def rhombus_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def ellipes_area(semi_major_axis, semi_minor_axis):
    return 3.14 * semi_major_axis * semi_minor_axis