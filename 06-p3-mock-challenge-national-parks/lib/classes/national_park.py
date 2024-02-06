from classes.trip import Trip


class NationalPark:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str and not hasattr(self, "_name"):
            self._name = value

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return [*set([trip.visitor for trip in self.trips()])]

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        # max_visitor = None
        # max_visits = 0
        # for visitor in self.visitors():
        #     v_visits = len([trip for trip in self.trips() if trip.visitor == visitor])
        #     if v_visits > max_visits:
        #         max_visitor = visitor
        #         max_visits = v_visits
        # return max_visitor
        return max(
            self.visitors(),
            key=lambda v: len([t for t in self.trips() if t.visitor == v]),
        )

    @classmethod
    def most_visited(cls):
        pass

    def __repr__(self) -> str:
        return f"<NationalPark name: {self.name}>"
