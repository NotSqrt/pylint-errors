#!/usr/bin/env python
# pylint: disable=I0011, R0922, W0211, W0223, R0903, W0105, E0602
"""Generate Failure errors for pylint."""

if True:
    # "F0401": 'Unable to import %s',
    import not_locatable_module
    not_locatable_module.run()


    # "F0220": 'failed to resolve interfaces implemented by %s (%s)',
    class InterfaceCantBeFound(object):
        """docstring"""
        __implements__ = undefined

# Could not generate errors
# astroid error
# "F0002": '%s: %s',

# "F0003": 'ignored builtin module %s',
# "F0004": 'unexpected inferred value %s',
# "F0010": 'error while code parsing: %s',
# "F0202": 'Unable to check methods signature (%s / %s)',
