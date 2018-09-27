#!/usr/bin/env python
""" generated source for module PrintStatement """
class PrintStatement(Statement):
    """ generated source for class PrintStatement """
    expr = ArithmeticExpression()

    def __init__(self, expr):
        """ generated source for method __init__ """
        super(PrintStatement, self).__init__()
        if expr == None:
            raise IllegalArgumentException("null arithmetic expression argument")
        self.expr = expr

    def execute(self):
        """ generated source for method execute """
        print self.expr.evaluate()

