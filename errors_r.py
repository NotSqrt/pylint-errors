#!/usr/bin/env python
# pylint: disable=I0011, E1304, C0111, C0103
"""Testing Refactoring reports."""

from __future__ import absolute_import

if True:
    # 'R0903': 'Too few public methods (%s/%s)'
    # 'R0201': 'Method could be a function'
    class Toto(object):
        """bla bal abl"""

        def function_method(self):
            """this method isn' a real method since it doesn't need self"""
            print 'hello'

    # pylint: disable=R0903

    # 'R0902': 'Too many instance attributes (%s/%s)'
    class Aaaa(object):
        """yo"""
        def __init__(self):
            self.aaaa = 1
            self.bbbb = 2
            self.cccc = 3
            self.dddd = 4
            self.eeee = 5
            self.ffff = 6
            self.gggg = 7
            self.hhhh = 8
            self.iiii = 9
            self.jjjj = 10
            self._aaaa = 1
            self._bbbb = 2
            self._cccc = 3
            self._dddd = 4
            self._eeee = 5
            self._ffff = 6
            self._gggg = 7
            self._hhhh = 8
            self._iiii = 9
            self._jjjj = 10
            self.tomuch = None

    # 'R0904': 'Too many public methods (%s/%s)'
    class Bbbb(object):
        """yo"""

        def meth1(self):
            """hehehe"""

        def meth2(self):
            """hehehe"""

        def meth3(self):
            """hehehe"""

        def meth4(self):
            """hehehe"""

        def meth5(self):
            """hehehe"""

        def meth6(self):
            """hehehe"""

        def meth7(self):
            """hehehe"""

        def meth8(self):
            """hehehe"""

        def meth9(self):
            """hehehe"""

        def meth10(self):
            """hehehe"""

        def meth11(self):
            """hehehe"""

        def meth12(self):
            """hehehe"""

        def meth13(self):
            """hehehe"""

        def meth14(self):
            """hehehe"""

        def meth15(self):
            """hehehe"""

        def meth16(self):
            """hehehe"""

        def meth17(self):
            """hehehe"""

        def meth18(self):
            """hehehe"""

        def meth19(self):
            """hehehe"""

        def meth20(self):
            """hehehe"""

        def meth21(self):
            """hehehe"""

    # 'R0921': 'Abstract class not referenced'
    class Cccc(object):
        """yo"""
        def __init__(self):
            pass

        def meth1(self):
            """hehehe"""
            raise NotImplementedError

        def meth2(self):
            """hehehe"""
            return 'Yo', self

    # 'R0922': 'Abstract class is only referenced %s times'
    class Dddd(object):
        """yo"""
        def __init__(self):
            pass

        def meth1(self):
            """hehehe"""
            raise NotImplementedError

        def meth2(self):
            """hehehe"""
            return 'Yo', self

    class Eeee(Dddd):
        """yo"""
    class Ffff(object):
        """yo"""
    class Gggg(object):
        """yo"""
    class Hhhh(object):
        """yo"""
    class Iiii(object):
        """yo"""
    class Jjjj(object):
        """yo"""

    # 'R0901': 'Too many ancestors (%s/%s)'
    class Llll(Aaaa, Bbbb, Ffff, Gggg, Hhhh, Iiii, Jjjj):
        """yo"""


    # 'R0911': 'Too many return statements (%s/%s)'
    def too_many_returns(arg):
        """is this real ?"""
        if arg == 1:
            return 1
        elif arg == 2:
            return 2
        elif arg == 3:
            return 3
        elif arg == 4:
            return 4
        elif arg == 5:
            return 5
        elif arg == 6:
            return 6
        elif arg == 7:
            return 7
        elif arg == 8:
            return 8
        elif arg == 9:
            return 9
        elif arg == 10:
            return 10
        return None

    # 'R0912': 'Too many branches (%s/%s)'

    def stupid_function(arg):
        """reallly stupid function"""
        if arg == 1:
            print 1
        elif arg == 2:
            print 2
        elif arg == 3:
            print 3
        elif arg == 4:
            print 4
        elif arg == 5:
            print 5
        elif arg == 6:
            print 6
        elif arg == 7:
            print 7
        elif arg == 8:
            print 8
        elif arg == 9:
            print 9
        elif arg == 10:
            print 10
        else:
            if arg < 1:
                print 0
            else:
                print 100
            arg = 0
        if arg:
            print None
        else:
            print arg

    # 'R0913': 'Too many arguments (%s/%s)'
    def stupid_function1(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9):
        """reallly stupid function"""
        print arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9

    # 'R0914': 'Too many local variables (%s/%s)'
    def stupid_function2(arg1, arg2, arg3, arg4, arg5):
        """reallly stupid function"""
        arg6, arg7, arg8, arg9 = arg1, arg2, arg3, arg4
        print arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9
        loc1, loc2, loc3, loc4, loc5, loc6, loc7 = arg1, arg2, arg3, arg4, arg5, \
     arg6, arg7
        print loc1, loc2, loc3, loc4, loc5, loc6, loc7

    # 'R0915': 'Too many statements (%s/%s)'
    def stupid_function3(arg):
        """reallly stupid function"""
        if arg == 1:
            print 1
        elif arg == 2:
            print 2
        elif arg == 3:
            print 3
        elif arg == 4:
            print 4
        elif arg == 5:
            print 5
        elif arg == 6:
            print 6
        elif arg == 7:
            print 7
        elif arg == 8:
            print 8
        elif arg == 9:
            print 9
        elif arg == 10:
            print 10
        elif arg < 1:
            print 0
            print 100
            arg = 0
        for val in range(arg):
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val
            print val

    # 'R0923': 'Interface not implemented'

    from logilab.common.interface import Interface

    class IAaaa(Interface):
        """yo"""

        def meth1(self):
            """hehehe"""

# Not generated
# 'R0401': 'Cyclic import (%s)'

# other types:
# R0001: Messages by category
# R0002: % errors / warnings by module
# R0003: Messages
# R0004: Global evaluation
# R0101: Statistics by type
# R0402: Modules dependencies graph
# R0701: Raw metrics
# R0801: Duplication
