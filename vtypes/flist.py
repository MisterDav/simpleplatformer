import math

class FList():
    def __init__(self, *op):
        self.list = op

    def __add__(self, op): return [x + op for x in self.list]
    def __sub__(self, op): return [x - op for x in self.list]
    def __mul__(self, op): return [x * op for x in self.list]
    def __div__(self, op): return [x / op for x in self.list]