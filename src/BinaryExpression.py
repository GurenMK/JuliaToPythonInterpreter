#!/usr/bin/env python
""" generated source for module BinaryExpression """
class BinaryExpression(ArithmeticExpression):
    """ generated source for class BinaryExpression """
    expr1 = ArithmeticExpression()
    expr2 = ArithmeticExpression()
    op = ArithmeticOperator()

    # 
    #      * @param expr1 - cannot be null
    #      * @param expr2 - cannot be null
    #      * @throws IllegalArgumentException if either argument is null
    #      
    def __init__(self, op, expr1, expr2):
        """ generated source for method __init__ """
        super(BinaryExpression, self).__init__()
        if op == None:
            raise IllegalArgumentException("null arithmetic operator argument")
        if expr1 == None or expr2 == None:
            raise IllegalArgumentException("null expression argument")
        self.expr1 = expr1
        self.expr2 = expr2
        self.op = op

    def evaluate(self):
        """ generated source for method evaluate """
        value = 0
        if self.op==ADD_OP:
            self.op = ArithmeticOperator.ADD_OP
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op==SUB_OP:
            self.op = ArithmeticOperator.SUB_OP
            value = self.expr1.evaluate() - self.expr2.evaluate()
        elif self.op==MUL_OP:
            self.op = ArithmeticOperator.MUL_OP
            value = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.op==DIV_OP:
            self.op = ArithmeticOperator.DIV_OP
            value = self.expr1.evaluate() / self.expr2.evaluate()
        elif self.op==MOD_OP:
            self.op = ArithmeticOperator.MOD_OP
            value = self.expr1.evaluate() % self.expr2.evaluate()
        elif self.op==EXP_OP:
            self.op = ArithmeticOperator.EXP_OP
            value = int(Math.pow(self.expr1.evaluate(), self.expr2.evaluate()))
        elif self.op==REV_DIV_OP:
            self.op = ArithmeticOperator.REV_DIV_OP
            value = self.expr2.evaluate() / self.expr1.evaluate()
        return value

