#!/usr/bin/env python
""" generated source for module Constant """
class Constant(ArithmeticExpression):
    """ generated source for class Constant """
    value = int()

    def __init__(self, value):
        """ generated source for method __init__ """
        super(Constant, self).__init__()
        self.value = value

    def evaluate(self):
        """ generated source for method evaluate """
        return self.value

