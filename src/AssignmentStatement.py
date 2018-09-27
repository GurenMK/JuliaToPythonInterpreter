#!/usr/bin/env python
""" generated source for module AssignmentStatement """
import java.beans.Expression

class AssignmentStatement(Statement):
    """ generated source for class AssignmentStatement """
    expr = ArithmeticExpression()
    var = Id()

    # 
    #      * @param var - cannot be null
    #      * @param expr - cannot be null
    #      * @throws IllegalArgumentException if either argument is null
    #      
    def __init__(self, var, expr):
        """ generated source for method __init__ """
        super(AssignmentStatement, self).__init__()
        if var == None:
            raise IllegalArgumentException("null Id argument")
        if expr == None:
            raise IllegalArgumentException("null ArithmeticExpression argument")
        self.expr = expr
        self.var = var

    def execute(self):
        """ generated source for method execute """
        Memory.store(self.var.getChar(), self.expr.evaluate())

