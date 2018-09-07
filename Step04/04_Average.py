# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    score = sorted([float(s) for s in sys.stdin.readline().split()], reverse=True)
    sum = 0
    for i in range(N):
        sum = sum + (score[i] / score[0]) * 100.0
    sys.stdout.write("{}".format(sum / N))
