# -*- coding: utf-8 -*-

# Python Future imports
from __future__ import unicode_literals, print_function

import sh
import re
import sys


def main():
    cmd = sh.pylint('--list-msgs')

    pattern = re.compile(r':(.+) \((.+)\): \*(.+)\*')

    for line in cmd.stdout.decode(sys.stdout.encoding or sys.stdin.encoding or "utf-8").splitlines():
        match = pattern.match(line)
        if match:
            print(match.groups())

if __name__ == '__main__':
    main()
