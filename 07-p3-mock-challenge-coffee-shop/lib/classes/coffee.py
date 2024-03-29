from classes.order import Order


class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is str and not hasattr(self, "_name"):
            self._name = value
        else:
            raise Exception("Coffee name is invalid")

    def orders(self):

        return [order for order in Order.all if order.coffee == self]  # like filter

    def customers(self):

        return list(set([order.customer for order in self.orders()]))  # like map

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        return sum([order.price for order in self.orders()]) / self.num_orders()

    def create_order(self, customer, price):
        Order(customer, self, price)

    def __repr__(self):
        return f"<Coffee {self.name}> "
