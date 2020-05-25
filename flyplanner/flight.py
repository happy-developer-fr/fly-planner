from typing import List

from .geom import distance, Point


class Flight:
    def __init__(self, flight_positions: List[Point]):
        self.flight_positions = flight_positions

    def take_off_point(self) -> Point:
        return self.flight_positions[0]

    def landing_point(self) -> Point:
        return self.flight_positions[-1]

    def flight_length(self) -> float:
        dist = 0.0
        previous_point = None
        for i, val in enumerate(self.flight_positions):
            if i == 0:
                previous_point = val
            else:
                dist += distance(previous_point, val)
                previous_point = val

        return dist
