#!/usr/bin/env python2
# pylint: disable=I0011, R0903, R0922, E1304, C0111, C0103, C0301, C0325, C1001, W0612
"""Testing Warning reports."""

if True:
    def w0101():
        return True
        # "W0101": 'Unreachable code',
        # "W0612": 'Unused variable %r',
        var = True
        # "W0107": 'Unnecessary pass statement',
        pass


    # "W0613": 'Unused argument %r',
    # "W0102": 'Dangerous default value %s as argument',
    def dangerous(a={1}):
        pass

    # "W0108": 'Lambda may not be necessary',
    TO_LIST = lambda x: list(x)

    # "W0109": 'Duplicate key %r in dictionary',
    DICT = {
        "key": "val",
        "key": "val",
    }

    # "W0141": 'Used builtin function %r',
    map(str, [1, 2])
    # "W0110": 'map/filter on lambda could be replaced by comprehension',
    assert filter(lambda x: x != 1, [1, 2, 3]) == [2, 3]


    for i in range(5):
        pass
    else:
        # "W0120": 'Else clause on loop without a break statement',
        # -> may not be on the same line as else !
        pass


    # "W0122": 'Use of exec',
    exec('pass')

    # "W0142": 'Used * or ** magic',
    zip(*[1, 2])

    # "W0105": 'String statement has no effect',
    "no effect"

    # "W0104": 'Statement seems to have no effect',
    1 + 1

    # "W0199": '''Assert called on a 2-uple. Did you mean 'assert x,y'?''',
    assert (1, 2)


    # "W0150": '%s statement in finally block may swallow exception',
    def w0106():
        try:
            return
        finally:
            return


    # "W0106": 'Expression "%s" is assigned to nothing',
    list() and tuple()


    class MetaClass(object):

        """To test meta class errors."""

        def __init__(self):
            pass

        def method(self, is_optional):
            """To test ???."""
            pass

        def not_overriden(self):
            """To test W0223."""
            raise NotImplementedError


        def abcd(self, aaa=1, bbbb=None):
            """hehehe"""
            print self, aaa, bbbb


    # "W0223": 'Method %r is abstract in class %r but is not overridden',
    class MyClass(MetaClass):

        """To test class errors."""

        _protected = True

        # "W0231": '__init__ method from base class %r is not called',
        def __init__(self, other_obj):
            self.public = other_obj

        @staticmethod
        def smethod(self):
            # "W0211": 'Static method with %r as first argument',
            pass

        def method(self):
            # "W0201": 'Attribute %r defined outside __init__',
            # "W0221": 'Arguments number differs from %s method',
            self.var = True

        def access_protected(self):
            # "W0212": 'Access to a protected member %s of a client class',
            print self.public._haha

        # "W0234": '__iter__ returns non-iterator',
        def __iter__(self):
            return 1

        # "W0222": 'Signature differs from %s method',
        def abcd(self, aaa, bbbb=None):
            """hehehe."""
            print self, aaa, bbbb

    # "W0401": 'Wildcard import %s',
    # "W0614": 'Unused import %s from wildcard import',
    from os.path import *

    # "W0410": '__future__ import is not the first non docstring statement',
    from __future__ import print_function

    # "W0331": 'Use of the <> operator',
    assert 1 <> 2

    # "W0333": 'Use of the `` operator',
    STR_REPR = `True`

    # "W0402": 'Uses of a deprecated module %r',
    import Bastion
    print(Bastion)

    # "W0404": 'Reimport %r (imported line %s)', TODO not generated
    import os
    assert os
    import os
    assert os

    # "W0611": 'Unused import %s',
    import sys

    # "W0633": 'Attempting to unpack a non-sequence%s',
    VARA, VARB = True


    # "W0701": 'Raising a string exception',
    def met0701():
        raise "Error"

    # "W0703": 'Catching too general exception %s',
    try:
        assert False
    except Exception:
        pass

    # "W1501": '"%s" is not a valid mode for open.',
    open('foo.bar', 'w', 2)
    open('foo.bar', 'rw')

    # "W1201": 'Specify string format arguments as logging function parameters',
    import logging
    logging.warn('%s, %s' % (4, 5))

    # "W1300": 'Format string dictionary key should be a string, not %s',
    print("%(1)s" % {1: "a"})

    # "W1301": 'Unused key %r in format string dictionary',
    print("%(a)s" % {"a": "a", "b": 1})

    # "W0622": 'Redefining built-in %r',
    from os import open

    # "W0301": 'Unnecessary semicolon',
    pass;


    # "W0702": 'No exception type(s) specified',
    try:
        pass
    except:
        pass

    # "W0711": 'Exception to catch is the result of a binary "%s" operation',
    __revision__ = 1
    try:
        __revision__ += 1
    except Exception or StandardError:
        print("caught1")
    except Exception and StandardError:
        print("caught2")


    # "W0631": 'Using possibly undefined loop variable %r',
    def do_stuff(some_random_list):
        """Not right."""
        for var in some_random_list:
            pass
        print(var)


    # Globals
    CONSTANT = 1


    def fix_contant(value):
        """all this is ok, but try not using global ;)."""
        # "W0603": 'Using the global statement',
        global CONSTANT
        print(CONSTANT)
        CONSTANT = value
    # "W0604": 'Using the global statement at the module level',
    global CSTE  # useless


    def other():
        """global behaviour test."""
        global HOP
        # "W0602": 'Using global for %r but no assignment is done',


    def define_constant():
        """ok but somevar is not defined at the module scope."""
        # "W0601": 'Global variable %r undefined at the module level',
        global SOMEVAR
        SOMEVAR = 2


    def new_style():
        """Some exceptions can be unpacked."""
        try:
            pass
        # "W0712": 'Implicit unpacking of exceptions is not supported in Python 3',
        # "W0623": 'Redefining name %r from %s in exception handler',
        except IOError as (new_style, tuple):  # W0623 twice
            print(new_style, tuple)


    class AAAA(object):

        """ancestor 1."""

        def __init__(self):
            print('init', self)
            # "W0233": '__init__ method from a non direct base class %r is called',
            BBBBMixin.__init__(self)


    class BBBBMixin(object):

        """ancestor 2."""

        def __init__(self):
            print('init', self)


    def getter(self):
        """interesting."""
        return self


    class HaNonNonNon:

        """bad usage."""

        # "W1001": 'Use of "property" on an old style class',
        method = property(getter, doc='hop')

        def __init__(self):
            pass


    def func_return_none():
        """function without return."""
        return None

    # "W1111": 'Assigning to function call which only returns None',
    A = func_return_none()


    class BofException:

        """mouais."""


    def fonction_bof2():
        """raise."""
        # "W0710": '''Exception doesn't inherit from standard "Exception" class''',
        # "W0121": 'Use raise ErrorClass(args) instead of raise ErrorClass, args.',
        raise BofException, 'hop'


    # "W0311": 'Bad indentation. Found %s %s, expected %s',
    def totoo():
     """docstring."""


    # "W0312": 'Found indentation with %ss instead of %ss',
    def tab_func():
    	"""yo."""


    # "W0332": 'Use of "l" as long integer identifier',
    __revision__ = 1l

    # "W0512": 'Cannot decode using encoding "%s", unexpected byte at position %d',
    # The next line is longer than 80 characters, because the file is encoded
    # in ASCII.
    THIS_IS_A_VERY_LONG_VARIABLE_NAME = 'Существительное Частица'  # With warnings.


    class MyOtherError(Exception):
        """Special exception class."""
        pass

    def test():
        # "W0621": 'Redefining name %r from outer scope (line %s)',
        for MyOtherError in range(5):
            pass

    # "W0623": "Redefining name %r from outer scope (line %s) in exception handler"
    try:
        pass
    except KeyError as MyOtherError:
        pass


    # "W0632": 'Possible unbalanced tuple unpacking with sequence%s: left side has %d label(s), right side has %d value(s)',
    first, second = 1, 2, 3
    first, second = (1, 2, 3)

    # "W0403": 'Relative import %r, should be %r',
    import errors_e
    assert errors_e
    # "W0406": 'Module import itself',
    import errors_w
    assert errors_w

# Could not be generated :
# "W0232": 'Class has no __init__ method',
# "W0704": '''Except doesn't do anything''',
