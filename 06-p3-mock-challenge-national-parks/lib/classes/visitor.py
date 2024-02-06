from classes.trip import Trip


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

    def trips(self):
        pass

    def national_parks(self):
        pass

    def __repr__(self) -> str:
        return f"<Visitor name: {self.name}>"
