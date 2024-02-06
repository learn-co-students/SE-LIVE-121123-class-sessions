class Trip:

    all = []  # SSOT

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date  # TODO: make a property; check str type
        self.end_date = end_date
        self.__class__.all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, value):
        from classes.visitor import Visitor

        if isinstance(value, Visitor):
            self._visitor = value  # TODO: raise exception
        else:
            raise Exception

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, value):
        from classes.national_park import NationalPark

        if isinstance(value, NationalPark):
            self._national_park = value  # TODO: raise exception
        else:
            raise Exception

    def __repr__(self):
        return (
            f"<Trip | park: {self.national_park.name} | visitor: {self.visitor.name}>"
        )
