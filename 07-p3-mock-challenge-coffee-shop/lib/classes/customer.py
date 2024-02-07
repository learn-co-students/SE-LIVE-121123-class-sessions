from classes.order import Order


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

        return [order for order in Order.all if order.customer == self]

    def coffees(self, new_coffee=None):
        return [*set([order.coffee for order in self.orders()])]

    def create_order(self, coffee, price):
        Order(self, coffee, price)
