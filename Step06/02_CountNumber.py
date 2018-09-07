# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    C = int(sys.stdin.readline())

    N = A * B * C
    for i in range(10):
        count = 0
        for s in str(N):
            if int(s) == i:
                count += 1
        print(count)
