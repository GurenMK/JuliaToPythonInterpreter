#!/usr/bin/env python
""" generated source for module ForStatement """
class ForStatement(Statement):
    """ generated source for class ForStatement """
    var = Id()
    it = Iter()

    # arrayList of size 2, index 0-start loop value, index 1-end loop value
    blk = Block()

    def __init__(self, var, it, blk):
        """ generated source for method __init__ """
        super(ForStatement, self).__init__()
        if var == None:
            raise IllegalArgumentException("null Id argument")
        if it == None:
            raise IllegalArgumentException("null iterator argument")
        if blk == None:
            raise IllegalArgumentException("null block argument")
        self.var = var
        self.it = it
        self.blk = blk

    def execute(self):
        """ generated source for method execute """
        # incrementing loop
        if self.it.evaluate().get(0) < self.it.evaluate().get(1):
            Memory.store(self.var.getChar(), self.it.evaluate().get(0))
            while Memory.fetch(self.var.getChar()) <= self.it.evaluate().get(1):
                self.blk.execute()
                i += 1
                Memory.store(self.var.getChar(), i)
        else:
            # decrementing loop
            Memory.store(self.var.getChar(), self.it.evaluate().get(0))
            while Memory.fetch(self.var.getChar()) >= self.it.evaluate().get(1):
                self.blk.execute()
                i -= 1
                Memory.store(self.var.getChar(), i)

