class Visitor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if (
            isinstance(value, str)
            and 1 <= len(value) <= 15
            and not hasattr(self, "name")
        ):
            self._name = value
        else:
            raise Exception

    def trips(self):
        from classes.trip import Trip

        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return [*set([trip.national_park for trip in self.trips()])]

    def __repr__(self) -> str:
        return f"<Visitor name: {self.name}>"
