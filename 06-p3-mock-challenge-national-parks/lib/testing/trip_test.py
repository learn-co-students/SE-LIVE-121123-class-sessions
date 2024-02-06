import pytest
from classes.national_park import NationalPark
from classes.trip import Trip
from classes.visitor import Visitor


class TestTrip:
    """Trip in trip.py"""

    # Test for Trip initialization
    def test_trip_initialization(self):
        """is initialized with a visitor, national_park, start_date and end_date"""
        visitor = Visitor("John Doe")
        national_park = NationalPark("Yellowstone")
        trip = Trip(visitor, national_park, "2024-01-01", "2024-01-07")
        assert isinstance(trip.visitor, Visitor)
        assert isinstance(trip.national_park, NationalPark)
        assert trip.start_date == "2024-01-01"
        assert trip.end_date == "2024-01-07"

    # Test for raising exceptions when setting invalid properties
    def test_trip_property_exceptions(self):
        visitor = "John Doe"
        national_park = "Yellowstone"
        trip = Trip(visitor, national_park, "2024-01-01", "2024-01-07")
        assert hasattr(trip, "visitor") == False
        assert hasattr(trip, "national_park") == False

        # uncomment the next five lines if using Exceptions
        # with pytest.raises(Exception):
        #     trip.visitor = "Not a Visitor"

        # with pytest.raises(Exception):
        #     trip.national_park = "Not a NationalPark"

    def test_get_all_trips(self):
        """has a class attr all populated with each Trip instance"""
        Trip.all = []
        visitor1 = Visitor("John Doe")
        visitor2 = Visitor("Jane Day")
        national_park = NationalPark("Yellowstone")
        trip1 = Trip(visitor1, national_park, "2024-01-01", "2024-01-07")
        trip2 = Trip(visitor2, national_park, "2024-11-10", "2024-11-15")

        assert len(Trip.all) == 2
        assert trip1 in Trip.all
        assert trip2 in Trip.all
