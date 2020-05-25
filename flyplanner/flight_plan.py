"""
A flight plan with a flight and a start date
"""
from .flight import Flight  # pylint: disable=import-error


class FlightPlan:
    """
    A flight plan with a flight and a start date
    """

    def __init__(self, flight: Flight):
        self.flight = flight

    def get_flight(self) -> Flight:
        """

        :return: The flight
        """
        return self.flight
