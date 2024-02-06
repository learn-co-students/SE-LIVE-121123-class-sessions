#!/usr/bin/env python3
import ipdb
from classes.national_park import NationalPark
from classes.trip import Trip
from classes.visitor import Visitor

if __name__ == "__main__":
    print("HELLO! :) let's debug :vibing_potato:")

    p1 = NationalPark("Yosemite")
    v1 = Visitor("Jeremy")
    t1 = Trip(v1, p1, "Sept 16", "Sept 23")

    ipdb.set_trace()
