# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    n1, n2 = sys.stdin.readline().rstrip().split(" ")
    sys.stdout.write("{}".format(max(int(n1[::-1]), int(n2[::-1]))))
