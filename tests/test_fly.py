import pytest

from flyplanner.fly import Fly
from flyplanner.geom import Point


@pytest.fixture
def fly_three_points():
    take_off_point = Point(0, 0)
    middle_point = Point(0, 1)
    landing_point = Point(0, 3)
    return Fly([take_off_point, middle_point, landing_point])


@pytest.fixture
def fly_four_points():
    take_off_point = Point(0, 0)
    middle_point = Point(0, 2)
    middle_point2 = Point(2, 2)
    landing_point = Point(2, 4)
    return Fly([take_off_point, middle_point, middle_point2, landing_point])


def test_take_off_point(fly_three_points):
    assert fly_three_points.take_off_point().__eq__(Point(0, 0))


def test_landing_point(fly_three_points):
    assert fly_three_points.landing_point().__eq__(Point(0, 3))


def test_fly_length(fly_four_points):
    assert 6.0 == fly_four_points.fly_length()
