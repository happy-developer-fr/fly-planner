from flyplanner import geom


class City:
    def __init__(self, name: str, center: geom.Point):
        self.name = name
        self.center = center


class Cities:
    def __init__(self, cities: set[City]):
        self.cities = cities
