#!/usr/bin/env python
""" generated source for module LexicalAnalyzer """
import java.io.File

import java.io.FileNotFoundException

import java.util.ArrayList

import java.util.List

import java.util.Scanner

class LexicalAnalyzer(object):
    """ generated source for class LexicalAnalyzer """
    tokens = List()

    def __init__(self, fileName):
        """ generated source for method __init__ """
        assert (fileName != None)
        self.tokens = ArrayList()
        sourceCode = Scanner(File(fileName))
        lineNumber = 0
        while sourceCode.hasNext():
            processLine(line, lineNumber)
            lineNumber += 1
        self.tokens.add(Token(lineNumber, 1, "EOS", TokenType.EOS_TOK))
        sourceCode.close()

    def processLine(self, line, lineNumber):
        """ generated source for method processLine """
        assert (line != None and lineNumber >= 1)
        index = 0
        index = skipWhiteSpace(line, index)
        while index < len(line):
            self.tokens.add(Token(lineNumber + 1, index + 1, lexeme, tokType))
            index += len(lexeme)
            index = skipWhiteSpace(line, index)

    def getTokenType(self, lexeme, lineNumber, columnNumber):
        """ generated source for method getTokenType """
        assert (lexeme != None and lineNumber >= 1 and columnNumber >= 1)
        tokType = None
        if Character.isLetter(lexeme.charAt(0)):
            if 1 == len(lexeme):
                if isValidIdentifier(lexeme.charAt(0)):
                    tokType = TokenType.ID_TOK
                else:
                    raise LexicalException("invalid lexeme at row number " + (lineNumber + 1) + " and column " + (columnNumber + 1))
            elif lexeme == "if":
                tokType = TokenType.IF_TOK
            elif lexeme == "function":
                tokType = TokenType.FUNCTION_TOK
            elif lexeme == "end":
                tokType = TokenType.END_TOK
            elif lexeme == "else":
                tokType = TokenType.ELSE_TOK
            elif lexeme == "for":
                tokType = TokenType.FOR_TOK
            elif lexeme == "while":
                tokType = TokenType.WHILE_TOK
            elif lexeme == "print":
                tokType = TokenType.PRINT_TOK
            else:
                raise LexicalException("invalid lexeme at row number " + (lineNumber + 1) + " and column " + (columnNumber + 1))
        elif Character.isDigit(lexeme.charAt(0)):
            if allDigits(lexeme):
                tokType = TokenType.CONST_TOK
            else:
                raise LexicalException("invalid lexeme at row number " + (lineNumber + 1) + " and column " + (columnNumber + 1))
        elif lexeme == "+":
            tokType = TokenType.ADD_TOK
        elif lexeme == "-":
            tokType = TokenType.SUB_TOK
        elif lexeme == "*":
            tokType = TokenType.MUL_TOK
        elif lexeme == "/":
            tokType = TokenType.DIV_TOK
        elif lexeme == "\\":
            tokType = TokenType.REV_DIV_TOK
        elif lexeme == "^":
            tokType = TokenType.EXP_TOK
        elif lexeme == "%":
            tokType = TokenType.MOD_TOK
        elif lexeme == "=":
            tokType = TokenType.ASSIGN_TOK
        elif lexeme == "(":
            tokType = TokenType.LEFT_PAREN_TOK
        elif lexeme == ""):
            tokType = TokenType.RIGHT_PAREN_TOK
        elif lexeme == ">=":
            tokType = TokenType.GE_TOK
        elif lexeme == ">":
            tokType = TokenType.GT_TOK
        elif lexeme == "<=":
            tokType = TokenType.LE_TOK
        elif lexeme == "<":
            tokType = TokenType.LT_TOK
        elif lexeme == "==":
            tokType = TokenType.EQ_TOK
        elif lexeme == "!=":
            tokType = TokenType.NE_TOK
        elif lexeme == ":":
            tokType = TokenType.COL_TOK
        else:
            raise LexicalException("invalid lexeme at row number " + (lineNumber + 1) + " and column " + (columnNumber + 1))
        return tokType

    def allDigits(self, s):
        """ generated source for method allDigits """
        assert (s != None)
        i = 0
        while i < len(s) and Character.isDigit(s.charAt(i)):
        return i == len(s)

    def getLexeme(self, line, lineNumber, index):
        """ generated source for method getLexeme """
        assert (line != None and lineNumber >= 1 and index >= 0)
        i = index
        while i < len(line) and not Character.isWhitespace(line.charAt(i)):
        return line.substring(index, i)

    def skipWhiteSpace(self, line, index):
        """ generated source for method skipWhiteSpace """
        assert (line != None and index >= 0)
        while index < len(line) and Character.isWhitespace(line.charAt(index)):
        return index

    def getNextToken(self):
        """ generated source for method getNextToken """
        if self.tokens.isEmpty():
            raise LexicalException("no more tokens")
        return self.tokens.remove(0)

    def getLookaheadToken(self):
        """ generated source for method getLookaheadToken """
        if self.tokens.isEmpty():
            raise LexicalException("no more tokens")
        return self.tokens.get(0)

    @classmethod
    def isValidIdentifier(cls, ch):
        """ generated source for method isValidIdentifier """
        # return ch == 'A' || ch == 'B' || ch == 'C' || ch == 'D';
        return Character.isLetter(ch)

    # print all tokens and lexemes from a julia file that was passed to the lexical analyzer
    # the lexical analyzer needs to be initialized in main class (Interpreter.java)
    def printLex(self):
        """ generated source for method printLex """
        # print all tokens and lexemes
        i = 0
        while i < len(self.tokens):
            print "The next token is: " + tokType + " **** Next lexeme is: " + lexeme
            i += 1

