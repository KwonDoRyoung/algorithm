# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    copy_N = N
    i = 0
    while True:
        i += 1
        if copy_N < 10:
            copy_N = 10 * copy_N + copy_N
        else:
            copy_N = (copy_N % 10) * 10 + ((copy_N // 10 + copy_N % 10) % 10)
        if copy_N == N:
            break
    sys.stdout.write("{}".format(i))
