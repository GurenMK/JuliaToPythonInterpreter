#!/usr/bin/env python
""" generated source for module BooleanExpression """
class BooleanExpression(object):
    """ generated source for class BooleanExpression """
    expr1 = ArithmeticExpression()
    expr2 = ArithmeticExpression()
    op = RelativeOperator()

    def __init__(self, op, expr1, expr2):
        """ generated source for method __init__ """
        if op == None:
            raise IllegalArgumentException("null relative operator argument")
        if expr1 == None or expr2 == None:
            raise IllegalArgumentException("null arithmetic expression argument")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        """ generated source for method evaluate """
        value = False
        if self.op == RelativeOperator.LE_OP:
            value = self.expr1.evaluate() <= self.expr2.evaluate()
        elif self.op == RelativeOperator.LT_OP:
            value = self.expr1.evaluate() < self.expr2.evaluate()
        elif self.op == RelativeOperator.GE_OP:
            value = self.expr1.evaluate() >= self.expr2.evaluate()
        elif self.op == RelativeOperator.GT_OP:
            value = self.expr1.evaluate() > self.expr2.evaluate()
        elif self.op == RelativeOperator.EQ_OP:
            value = self.expr1.evaluate() == self.expr2.evaluate()
        elif self.op == RelativeOperator.NE_OP:
            value = self.expr1.evaluate() != self.expr2.evaluate()
        return value

