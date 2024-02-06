class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is str and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("Invalid name")

    def orders(self, new_order=None):
        from classes.order import Order

        pass

    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee

        pass
