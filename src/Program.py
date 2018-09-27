#!/usr/bin/env python
""" generated source for module Program """
class Program(object):
    """ generated source for class Program """
    blk = Block()

    def __init__(self, blk):
        """ generated source for method __init__ """
        if blk == None:
            raise IllegalArgumentException("null block argument")
        self.blk = blk

    def execute(self):
        """ generated source for method execute """
        self.blk.execute()

