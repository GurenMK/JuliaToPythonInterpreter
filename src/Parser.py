#!/usr/bin/env python
""" generated source for module Parser """
import java.io.FileNotFoundException

class Parser(object):
    """ generated source for class Parser """
    lex = LexicalAnalyzer()

    def __init__(self, fileName):
        """ generated source for method __init__ """
        self.lex = LexicalAnalyzer(fileName)

    def parse(self):
        """ generated source for method parse """
        tok = self.lex.getNextToken()
        match(tok, TokenType.FUNCTION_TOK)
        functionName = getId()
        tok = self.lex.getNextToken()
        match(tok, TokenType.LEFT_PAREN_TOK)
        tok = self.lex.getNextToken()
        match(tok, TokenType.RIGHT_PAREN_TOK)
        blk = getBlock()
        tok = self.lex.getNextToken()
        match(tok, TokenType.END_TOK)
        tok = self.lex.getNextToken()
        if tok.getTokType() != TokenType.EOS_TOK:
            raise ParserException("garbage at end of file")
        return Program(blk)

    def getBlock(self):
        """ generated source for method getBlock """
        blk = Block()
        tok = self.lex.getLookaheadToken()
        while isValidStartOfStatement(tok):
            blk.add(stmt)
            tok = self.lex.getLookaheadToken()
        return blk

    def getStatement(self):
        """ generated source for method getStatement """
        stmt = Statement()
        tok = self.lex.getLookaheadToken()
        if tok.getTokType() == TokenType.IF_TOK:
            stmt = getIfStatement()
        elif tok.getTokType() == TokenType.WHILE_TOK:
            stmt = getWhileStatement()
        elif tok.getTokType() == TokenType.PRINT_TOK:
            stmt = getPrintStatement()
        elif tok.getTokType() == TokenType.ID_TOK:
            stmt = getAssignmentStatement()
        elif tok.getTokType() == TokenType.FOR_TOK:
            stmt = getForStatement()
        else:
            raise ParserException("invalid statement at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber())
        return stmt

    def getAssignmentStatement(self):
        """ generated source for method getAssignmentStatement """
        var = getId()
        tok = self.lex.getNextToken()
        match(tok, TokenType.ASSIGN_TOK)
        expr = getArithmeticExpression()
        return AssignmentStatement(var, expr)

    def getPrintStatement(self):
        """ generated source for method getPrintStatement """
        tok = self.lex.getNextToken()
        match(tok, TokenType.PRINT_TOK)
        tok = self.lex.getNextToken()
        match(tok, TokenType.LEFT_PAREN_TOK)
        expr = getArithmeticExpression()
        tok = self.lex.getNextToken()
        match(tok, TokenType.RIGHT_PAREN_TOK)
        return PrintStatement(expr)

    def getForStatement(self):
        """ generated source for method getForStatement """
        tok = self.lex.getNextToken()
        match(tok, TokenType.FOR_TOK)
        var = getId()
        tok = self.lex.getNextToken()
        match(tok, TokenType.ASSIGN_TOK)
        expr1 = getArithmeticExpression()
        tok = self.lex.getNextToken()
        match(tok, TokenType.COL_TOK)
        expr2 = getArithmeticExpression()
        blk = self.getBlock()
        tok = self.lex.getNextToken()
        match(tok, TokenType.END_TOK)
        it = Iter(expr1, expr2)
        return ForStatement(var, it, blk)

    def getWhileStatement(self):
        """ generated source for method getWhileStatement """
        tok = self.lex.getNextToken()
        match(tok, TokenType.WHILE_TOK)
        expr = getBooleanExpression()
        blk = self.getBlock()
        tok = self.lex.getNextToken()
        match(tok, TokenType.END_TOK)
        return WhileStatement(expr, blk)

    def getIfStatement(self):
        """ generated source for method getIfStatement """
        tok = self.lex.getNextToken()
        match(tok, TokenType.IF_TOK)
        expr = getBooleanExpression()
        blk1 = self.getBlock()
        tok = self.lex.getNextToken()
        match(tok, TokenType.ELSE_TOK)
        blk2 = self.getBlock()
        tok = self.lex.getNextToken()
        match(tok, TokenType.END_TOK)
        return IfStatement(expr, blk1, blk2)

    def isValidStartOfStatement(self, tok):
        """ generated source for method isValidStartOfStatement """
        assert (tok != None)
        return tok.getTokType() == TokenType.ID_TOK or tok.getTokType() == TokenType.IF_TOK or tok.getTokType() == TokenType.WHILE_TOK or tok.getTokType() == TokenType.FOR_TOK or tok.getTokType() == TokenType.PRINT_TOK

    # 
    #      * implements the production <expr> -> <operator> <expr> <expr> | id | constant
    #      
    def getArithmeticExpression(self):
        """ generated source for method getArithmeticExpression """
        expr = ArithmeticExpression()
        tok = self.lex.getLookaheadToken()
        if tok.getTokType() == TokenType.ID_TOK:
            expr = getId()
        elif tok.getTokType() == TokenType.CONST_TOK:
            expr = getConstant()
        else:
            expr = getBinaryExpression()
        return expr

    # 
    #      * implements the production <expr> -> <operator> <expr> <expr>
    #      
    def getBinaryExpression(self):
        """ generated source for method getBinaryExpression """
        op = ArithmeticOperator()
        tok = self.lex.getNextToken()
        if tok.getTokType() == TokenType.ADD_TOK:
            match(tok, TokenType.ADD_TOK)
            op = ArithmeticOperator.ADD_OP
        elif tok.getTokType() == TokenType.SUB_TOK:
            match(tok, TokenType.SUB_TOK)
            op = ArithmeticOperator.SUB_OP
        elif tok.getTokType() == TokenType.MUL_TOK:
            match(tok, TokenType.MUL_TOK)
            op = ArithmeticOperator.MUL_OP
        elif tok.getTokType() == TokenType.DIV_TOK:
            match(tok, TokenType.DIV_TOK)
            op = ArithmeticOperator.DIV_OP
        elif tok.getTokType() == TokenType.REV_DIV_TOK:
            match(tok, TokenType.REV_DIV_TOK)
            op = ArithmeticOperator.REV_DIV_OP
        elif tok.getTokType() == TokenType.EXP_TOK:
            match(tok, TokenType.EXP_TOK)
            op = ArithmeticOperator.EXP_OP
        elif tok.getTokType() == TokenType.MOD_TOK:
            match(tok, TokenType.MOD_TOK)
            op = ArithmeticOperator.MOD_OP
        else:
            raise ParserException(" operator expected at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber())
        expr1 = self.getArithmeticExpression()
        expr2 = self.getArithmeticExpression()
        return BinaryExpression(op, expr1, expr2)

    def getBooleanExpression(self):
        """ generated source for method getBooleanExpression """
        op = RelativeOperator()
        tok = self.lex.getNextToken()
        if tok.getTokType() == TokenType.EQ_TOK:
            op = RelativeOperator.EQ_OP
        elif tok.getTokType() == TokenType.NE_TOK:
            op = RelativeOperator.NE_OP
        elif tok.getTokType() == TokenType.GT_TOK:
            op = RelativeOperator.GT_OP
        elif tok.getTokType() == TokenType.GE_TOK:
            op = RelativeOperator.GE_OP
        elif tok.getTokType() == TokenType.LT_TOK:
            op = RelativeOperator.LT_OP
        elif tok.getTokType() == TokenType.LE_TOK:
            op = RelativeOperator.LE_OP
        else:
            raise ParserException("relational operator expected at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber())
        expr1 = self.getArithmeticExpression()
        expr2 = self.getArithmeticExpression()
        return BooleanExpression(op, expr1, expr2)

    def getId(self):
        """ generated source for method getId """
        tok = self.lex.getNextToken()
        match(tok, TokenType.ID_TOK)
        return Id(tok.getLexeme().charAt(0))

    def getConstant(self):
        """ generated source for method getConstant """
        tok = self.lex.getNextToken()
        match(tok, TokenType.CONST_TOK)
        value = Integer.parseInt(tok.getLexeme())
        return Constant(value)

    def match(self, tok, tokType):
        """ generated source for method match """
        assert (tok != None and tokType != None)
        if tok.getTokType() != tokType:
            raise ParserException(tokType.name() + " expected at row " + tok.getRowNumber() + " and column " + tok.getColumnNumber())

