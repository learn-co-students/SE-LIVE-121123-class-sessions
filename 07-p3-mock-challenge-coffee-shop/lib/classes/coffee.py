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

    def orders(self, new_order=None):
        from classes.order import Order

        pass

    def customers(self, new_customer=None):
        from classes.customer import Customer

        pass

    def num_orders(self):
        pass

    def average_price(self):
        pass

    def __repr__(self):
        return f"<Coffee {self.name}> "
