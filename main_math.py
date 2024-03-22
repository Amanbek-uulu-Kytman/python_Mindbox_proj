import math


class ShapeCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_triangle_area(self, side_a, side_b, side_c):
        s = (side_a + side_b + side_c) / 2
        return math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

    def is_right_triangle(self, side_a, side_b, side_c):
        sides = [side_a, side_b, side_c]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2

