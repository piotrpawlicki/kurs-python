from geometric_figures import *

def menu():
    while True:
        circles = float(input("Enter number of circle rooms: "))
        squares = float(input("Enter number of square rooms: "))
        rectangles = float(input("Enter number of rectangle rooms: "))
        triangles = float(input("Enter number of triangle rooms: "))
        if circles == 0 and squares == 0 and rectangles == 0 and triangles == 0:
            break
        break
    return circles, squares, rectangles, triangles
def main():
    circles, squares, rectangles, triangles = menu()

    while circles > 0:
        total_circle_area = 0
        radius = float(input("Enter the radius of the circle room: "))
        print(f'The area of the circle room, is:  {calc_circle_area(radius)} square meters')
        total_circle_area += calc_circle_area(radius)
        circles -= 1
    while squares > 0:
        total_square_area = 0
        side = float(input("Enter the side of the square room: "))
        print(f'The area of the square room, is: {calc_square_area(side)} square meters')
        total_square_area += calc_square_area(side)
        squares -= 1
    while rectangles > 0:
        total_rectangle_area = 0
        length = float(input("Enter the length of the rectangle room: "))
        width = float(input("Enter the width of the rectangle room: "))
        print(f'The area of the rectangle room, is:  {calc_rectangle_area(length, width)} square meters')
        total_rectangle_area += calc_rectangle_area(length, width)
        rectangles -= 1
    while triangles > 0:
        total_triangle_area = 0
        base = float(input("Enter the base of the triangle room: "))
        height = float(input("Enter the height of the triangle room: "))
        print(f' The area of the triangle room, is:  {calc_triangle_area(base, height)} square meters')
        total_triangle_area += calc_triangle_area(base, height)
        triangles -= 1

    print(f'The total area of the rooms is: {total_circle_area+total_square_area+total_rectangle_area+total_triangle_area} square meters')
    print()

main()