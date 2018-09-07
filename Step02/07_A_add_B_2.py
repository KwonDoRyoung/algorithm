# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    n1 = sys.stdin.readline()
    n2 = sys.stdin.readline()
    sys.stdout.write("{}".format(int(n1)+int(n2)))
    sys.stdout.flush()