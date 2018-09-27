#!/usr/bin/env python
""" generated source for module Interpreter """
# Alexander Urbanyak
# CS4308(01)
# worked with Jason Walters - student in Dr. North's online CS4308 class
# Jason Walters assisted with testing
import java.io.FileNotFoundException

class Interpreter(object):
    """ generated source for class Interpreter """
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        try:
            prog.execute()
            # LexicalAnalyzer lex = new LexicalAnalyzer("test1.jl");
            # lex.printLex(); //print tokens and lexemes of the julia file
            # Memory.displayMemory(); // to see results of assignment statements
        except ParserException as e:
            e.printStackTrace()
        except FileNotFoundException as e:
            e.printStackTrace()
        except LexicalException as e:
            e.printStackTrace()


if __name__ == '__main__':
    import sys
    Interpreter.main(sys.argv)

