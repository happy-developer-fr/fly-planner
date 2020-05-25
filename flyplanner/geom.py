import math


class Point:
    def __init__(self, x_coord: int, y_coord: int):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def get_x(self) -> int:
        return self.x_coord

    def get_y(self) -> int:
        return self.y_coord


def distance(a_point: Point, b_point: Point):
    return math.sqrt(
        math.pow(b_point.x_coord - a_point.x_coord, 2)
        + math.pow(b_point.y_coord - a_point.y_coord, 2)
    )
