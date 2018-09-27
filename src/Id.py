#!/usr/bin/env python
""" generated source for module Id """
class Id(ArithmeticExpression):
    """ generated source for class Id """
    ch = str()

    # 
    #      * @param ch - must be a valid identifier
    #      * @throws IllegalArgumentException if ch is not a valid identifier
    #      
    def __init__(self, ch):
        """ generated source for method __init__ """
        super(Id, self).__init__()
        if not LexicalAnalyzer.isValidIdentifier(ch):
            raise IllegalArgumentException("character is not a valid identifier")
        self.ch = ch

    def evaluate(self):
        """ generated source for method evaluate """
        return Memory.fetch(self.ch)

    def getChar(self):
        """ generated source for method getChar """
        return self.ch

