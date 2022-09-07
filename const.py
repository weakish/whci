# adapted from http://code.activestate.com/recipes/65207-constants-in-python/

'''Why Python doesn't have constants?


Usage:

    import const
    # and bind an attribute ONCE:
    const.magic = 23
    # but NOT re-bind it:
    const.magic = 88      # raises const.ConstError
    # you may also want to add the obvious __delattr__

Note:

The original version from activestate doesn't work for python 3.
This version should work on python 3 and (not very early) python 2.
I've tested it on python 2.6 and python 3.1.

PEP 591 introduces the Final qualifier for type hint.
Use it instead.
'''

class _const:
    class ConstError(TypeError): pass
    def __setattr__(self,name,value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)"%name)
        self.__dict__[name]=value
import sys
sys.modules[__name__]=_const()

