from classes.trip import Trip


class Visitor:
    def __init__(self, name):
        self.name = name

    def trips(self):
        pass

    def national_parks(self):
        pass
