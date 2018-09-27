#!/usr/bin/env python
""" generated source for module Iter """
import java.util.ArrayList

# stores two expression used in the ForStatement.java
class Iter(object):
    """ generated source for class Iter """
    expr1 = ArithmeticExpression()
    expr2 = ArithmeticExpression()
    it = ArrayList()

    def __init__(self, expr1, expr2):
        """ generated source for method __init__ """
        if expr1 == None or expr2 == None:
            raise IllegalArgumentException("null arithmetic expression argument")
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        """ generated source for method evaluate """
        self.it.add(self.expr1.evaluate())
        self.it.add(self.expr2.evaluate())
        return self.it

