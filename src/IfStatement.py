#!/usr/bin/env python
""" generated source for module IfStatement """
class IfStatement(Statement):
    """ generated source for class IfStatement """
    expr = BooleanExpression()
    blk1 = Block()
    blk2 = Block()

    def __init__(self, expr, blk1, blk2):
        """ generated source for method __init__ """
        super(IfStatement, self).__init__()
        if expr == None:
            raise IllegalArgumentException("null boolean expression argument")
        if blk1 == None or blk2 == None:
            raise IllegalArgumentException("null block argument")
        self.expr = expr
        self.blk1 = blk1
        self.blk2 = blk2

    def execute(self):
        """ generated source for method execute """
        if self.expr.evaluate():
            self.blk1.execute()
        else:
            self.blk2.execute()

