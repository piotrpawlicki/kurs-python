import math

def calc_triangle_area(base, height):
    return base * height / 2

def calc_rectangle_area(width, height):
    return width * height

def calc_circle_area(radius):
    return math.pi * radius * radius

def calc_square_area(side):
    return side * side

if  __name__ == '__main__':
    print(calc_triangle_area(10, 20))
    print(calc_rectangle_area(10, 20))
    print(calc_circle_area(10))
    print(calc_square_area(10))
