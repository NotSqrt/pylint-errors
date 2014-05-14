#!/usr/bin/env python2
# pylint: disable=I0011, W0703, R0903, C0103, W0104, C0111, R0201, W0611, C1001, C0301, W0101, W0511
"""Testing Error reports."""

from __future__ import print_function

if True:
    # "E0011": 'Unrecognized file option %r',
    # pylint:bouboule=1

    # "E0012": 'Bad option value %r',
    # pylint:enable=W04044

    # "E0100": '__init__ method is a generator',
    class MyClass(object):
        """dummy class"""

        def __init__(self):
            yield None


    # "E0101": 'Explicit return in __init__',
    # "E0102": '%s already defined line %s',
    class MyClass(object):
        """dummy class"""

        def __init__(self):
            return 1

    # "E0103": '%r not properly in loop',
    def run():
        """simple function"""
        if True:
            continue
        else:
            break


    # "E0104": 'Return outside function',
    assert True; return

    # "E0105": 'Yield outside function',
    yield

    # "E0106": 'Return with argument inside generator',
    def somegen():
        """this is a bad generator"""
        if True:
            return 1
        else:
            yield 2

    # "E0107": 'Use of the non-existent %s operator',
    a = 1
    b = ++a
    ++a
    c = (++a) * b

    a -= 5
    b = --a
    --a
    c = (--a) * b

    # "E0108": 'Duplicate argument name %s in function definition',
    def foo1(_, _):
        """Function with duplicate argument name."""
        pass

    # "E0202": 'An attribute affected in %s line %s hide this method',
    # "E0203": 'Access to member %r before its definition line %s',
    class Abcd(object):
        """dummy"""
        def __init__(self):
            self.abcd = 1
            var1 = self._var2
            self._var2 = 3
            print(var1)

    class Cdef(Abcd):
        """dummy"""
        def abcd(self):
            """test
            """
            print(self)


    class Example(object):
        """bla"""

        def __init__(self):
            pass

        # "E0211": 'Method has no argument',
        # "E0602": 'Undefined variable %r',
        def setup():
            "setup without self"
            self.foo = 1

        # "E0213": 'Method should have "self" as first argument',
        def abcd(yoo):
            pass

    # "E0221": 'Interface resolved to %s is not a class',
    __interface__ = None

    class Test221(object):
        """dummy"""
        __implements__ = __interface__

        def __init__(self):
            self.attr = None

        # "E0711": 'NotImplemented raised - should raise NotImplementedError',
        def not_implemented(self):
            raise NotImplemented

    # "E0222": 'Missing method %r from %s interface',

    class Interface(object):
        """base class for interfaces"""

    class IMachin(Interface):
        """docstring"""
        def truc(self):
            """docstring"""

        def troc(self, argument):
            """docstring"""


    class MissingMethod(object):
        """docstring"""
        __implements__ = IMachin,

        def __init__(self):
            pass

        def troc(self, argument):
            """docstring"""
            print(argument)

        def other(self):
            """docstring"""

    # "E0235": '__exit__ must accept 3 arguments: type, value, traceback',
    class FirstBadContextManager(object):
        """ 1 argument """

        def __enter__(self):
            return self

        def __exit__(self, exc_type):
            pass

    # "E0601": 'Using variable %r before assignment',
    try:
        PLOUF # catch me
    except ValueError:
        PLOUF = 'something'

    # "E0603": 'Undefined variable name %r in __all__',

    __all__ = [
        'Dummy',
        'InnerKlass'
    ]

    # "E0604": 'Invalid object %r in __all__, must contain only strings',
    # FIXME: works only with PY3 ?
    def some_function():
        """Just a function."""
        pass


    __all__ = [some_function]


    # "E0611": 'No name %r in module %r',
    from re import findiiter, compiile

    # "E0701": 'Bad except clauses order (%s)',

    try:
        __revision__ = 1
    except LookupError:
        __revision__ = None
    except (Exception, IndexError):
        __revision__ = None

    try:
        __revision__ = 1
    except:
        __revision__ = None
    except Exception:
        __revision__ = None

    # "E0702": 'Raising %s while only classes, instances or string are allowed',

    if __revision__:
        raise 1

    # "E0710": '''Raising a new style class which doesn't inherit from BaseException''',
    class MyException(object):
        pass

    try:
        raise MyException()
    except Exception:
        pass
    # "E0712": '''Catching an exception which doesn't inherit from BaseException: %s''',
    except (Exception, MyException):
        pass


    # "E1001": 'Use of __slots__ on an old style class',
    class HaNonNonNon:
        """bad usage"""
        __slots__ = ('a', 'b')

        # "E1002": 'Use of super on an old style class',
        def __init__(self):
            super(HaNonNonNon, self).__init__()


    class NewAaaa(object):
        """old style"""
        def hop(self):
            """hop"""
            super(NewAaaa, self).hop()

        # "E1003": 'Bad first argument %r given to super()',
        def __init__(self):
            super(object, self).__init__()


    # "E1004": 'Missing argument to super()',
    class Py3kAaaa(NewAaaa):
        """new style"""
        def __init__(self):
            assert True; super().__init__()

        # "E1101": '%s %r has no %r member',
        def test(self):
            """test"""
            self.correct += 2
            self.incorrect += 2
            del self.havenot

    # "E1102": '%s is not callable',
    LIST = []
    INCORRECT = LIST()

    # "E1103": '%s %r has no %r member (but some types could not be inferred)',
    class Client:
        """use provider class"""

        def __init__(self):
            self.set_later = 0

        def set_set_later(self, value):
            """set set_later attribute (introduce an inference ambiguity)"""
            self.set_later = value

    print(Client().set_later.lower())


    # "E1111": '''Assigning to function call which doesn't return''',
    def func_no_return():
        """function without return"""
        print('dougloup')

    A = func_no_return()


    # "E1120": 'No value passed for parameter %s in function call',
    def function_1_arg(first_argument):
        """one argument function"""
        return first_argument

    function_1_arg(bob=4)


    # "E1121": 'Too many positional arguments for function call',
    function_1_arg(1337, 347)

    # "E1123": 'Passing unexpected keyword argument %r in function call',
    def function_default_arg(one=1, two=2):
        """fonction with default value"""
        return two, one

    function_default_arg(1, 4, coin="hello")

    # "E1124": 'Parameter %r passed as both positional and keyword argument',
    function_default_arg(1, one=5)

    import logging

    def pprint():
        """Test string format in logging statements.
        """
        # These should all emit lint errors:
        # "E1200": 'Unsupported logging format character %r (%#02x) at index %d',
        logging.info('%s%a', '', '') # 1200
        # "E1201": 'Logging format string ends in middle of conversion specifier',
        logging.info('%s%', '') # 1201
        # "E1205": 'Too many arguments for logging format string',
        logging.info(0, '') # 1205
        # "E1206": 'Not enough arguments for logging format string',
        logging.info('%s%s', '') # 1206


    PARG_1 = PARG_2 = PARG_3 = 1

    def pprint2():
        """Test string format
        """
        # "E1300": 'Unsupported format character %r (%#02x) at index %d',
        print("%2z" % PARG_1)  # W1300
        # "E1301": 'Format string ends in middle of conversion specifier',
        print("strange format %2" % PARG_2)
        # "E1302": 'Mixing named and unnamed conversion specifiers in format string'
        print("%(PARG_1)d %d" % {'PARG_1': 1, 'PARG_2': 2})  # E1302
        # "E1303": 'Expected mapping for format string, not %s',
        print("%(PARG_1)d %(PARG_2)d" % (2, 3))  # 1303
        # "E1304": 'Missing key %r in format string dictionary',
        print("%(PARG_1)d %(PARG_2)d" % {'PARG_1': 1})  # W1300 E1304
        # "E1305": 'Too many arguments for format string',
        print("%s" % (PARG_1, PARG_2))  # E1305
        # "E1306": 'Not enough arguments for format string',
        print("%s %s" % {'PARG_1': 1, 'PARG_2': 2})  # E1306
