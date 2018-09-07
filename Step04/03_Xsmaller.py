# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    N, X = sys.stdin.readline().split()
    N = int(N)
    X = int(X)
    A = sys.stdin.readline().split()

    for a in A:
        if int(a) < X:
            sys.stdout.write("{} ".format(a))
