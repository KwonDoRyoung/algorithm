# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for i in range(1,10):
        sys.stdout.write("{} * {} = {}\n".format(N, i, N*i))
        sys.stdout.flush()