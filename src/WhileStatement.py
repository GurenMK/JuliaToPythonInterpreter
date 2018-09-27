#!/usr/bin/env python
""" generated source for module WhileStatement """
class WhileStatement(Statement):
    """ generated source for class WhileStatement """
    expr = BooleanExpression()
    blk = Block()

    def __init__(self, expr, blk):
        """ generated source for method __init__ """
        super(WhileStatement, self).__init__()
        if expr == None:
            raise IllegalArgumentException("null boolean expression argument")
        if blk == None:
            raise IllegalArgumentException("null block argument")
        self.expr = expr
        self.blk = blk

    def execute(self):
        """ generated source for method execute """
        while self.expr.evaluate():

