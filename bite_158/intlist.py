from statistics import mean, median
from decimal import Decimal


class IntList(list):
    def __init__(self, elements):
        # check when initializing?
        self.elements = list(elements)

    @property
    def mean(self):
        return mean(self.elements)

    @property
    def median(self):
        return median(self.elements)

    # over-ride append method
    def append(self, new):
        if not isinstance(new, (int, float, Decimal)):
            raise TypeError 
        self.elements.append(new)

    # overload __add__ and __ladd__
    def __add__(self, new):
        if not isinstance(new, (int, float)):
            raise TypeError("can only add an int or a float to the list")
        self.elements += new

    def __iadd__(self, new):
        if isinstance(new, list) and not all(isinstance(item, (int, float)) for item in new):
            raise TypeError
        elif not isinstance(new, (int, float)):
            raise TypeError('cannot add a non int/float')
        self.elements += new
