#!/usr/bin/env python
""" generated source for module Token """
class Token(object):
    """ generated source for class Token """
    rowNumber = int()
    columnNumber = int()
    lexeme = str()
    tokType = TokenType()

    # 
    #      * @param rowNumber - must be positive
    #      * @param columnNumber - must be positive
    #      * @param lexeme - cannot be null nor empty
    #      * @param tokType - cannot be null
    #      * @throws IllegalArgumentException if any precondition is not satisfied
    #      
    def __init__(self, rowNumber, columnNumber, lexeme, tokType):
        """ generated source for method __init__ """
        if rowNumber <= 0:
            raise IllegalArgumentException("invalid row number argument")
        if columnNumber <= 0:
            raise IllegalArgumentException("invalid column number argument")
        if lexeme == None or 0 == len(lexeme):
            raise IllegalArgumentException("invalid lexeme argument")
        if tokType == None:
            raise IllegalArgumentException("invalid TokenType argument")
        self.rowNumber = rowNumber
        self.columnNumber = columnNumber
        self.lexeme = lexeme
        self.tokType = tokType

    def getRowNumber(self):
        """ generated source for method getRowNumber """
        return self.rowNumber

    def getColumnNumber(self):
        """ generated source for method getColumnNumber """
        return self.columnNumber

    def getLexeme(self):
        """ generated source for method getLexeme """
        return self.lexeme

    def getTokType(self):
        """ generated source for method getTokType """
        return self.tokType

