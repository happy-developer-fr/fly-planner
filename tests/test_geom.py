from flyplanner.geom import Point, distance


def test_distance_1():
    assert distance(Point(0, 0), Point(0, 1)).__eq__(1.0)


def test_distance_2():
    assert distance(Point(0, 0), Point(0, 2)).__eq__(2.0)
    assert distance(Point(0, 0), Point(0, 2)).__eq__(2.0)
