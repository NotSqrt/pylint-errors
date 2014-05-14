"""Generate I errors for pylint."""

if True:
    # "I0010": 'Unable to consider inline option %r',
    # "pylint:disable-msg"

    # "I0011": 'Locally disabling %s',
    # pylint:disable=W0404

    # "I0012": 'Locally enabling %s',
    # pylint:enable=W0403


    # "I0022"
    # pylint: enable-msg=C0103

    # "I0020": 'Suppressed %s (from line %d)', TODO does not seem to work
    def suppressed():
        """A function with an unused variable, suppressed."""
        # pylint: disable=W0612
        var = 0


    # "I0021": 'Useless suppression of %s', TODO does not seem to work
    def meth10(obj):
        """Test double disable."""
        # pylint: disable=E1101
        # no error
        print obj.bla
        # pylint: disable=E1101
        print obj.blu

    # put this at the end of the file
    # "I0013": 'Ignoring entire file',
    # "I0014": 'Used deprecated directive'
    # pylint:disable-all

# not generated:
# "I0001": 'Unable to run raw checkers on built-in module %s',
