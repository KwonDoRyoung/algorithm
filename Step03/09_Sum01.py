# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    sys.stdout.write("{}".format(int(n * (n + 1) / 2)))
    sys.stdout.flush()
