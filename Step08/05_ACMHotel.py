# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())

    for _ in xrange(T):
        H, W, N = [int(i) for i in sys.stdin.readline().rstrip().split(" ")]
        Y = N % H
        if Y == 0:
            Y = H
            X = N // H
        else:
            Y = N % H
            X = N // H + 1
        if X < 10:
            sys.stdout.write("{}0{}\n".format(Y, X))
        else:
            sys.stdout.write("{}{}\n".format(Y, X))
