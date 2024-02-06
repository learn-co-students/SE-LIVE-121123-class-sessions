#!/usr/bin/env python3
import ipdb
from classes.coffee import Coffee
from classes.customer import Customer
from classes.order import Order

if __name__ == "__main__":
    print("HELLO! :) let's debug")

    cof1 = Coffee("Mocha")
    cus1 = Customer("Loren")
    ord1 = Order(cus1, cof1, 3)

    ipdb.set_trace()
