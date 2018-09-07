# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    string = sys.stdin.readline()
    count = 1
    for s in string:
        if count % 10 == 0:
            sys.stdout.write("{}\n".format(s))
            count = 1
        else:
            sys.stdout.write("{}".format(s))
            count += 1
        sys.stdout.flush()