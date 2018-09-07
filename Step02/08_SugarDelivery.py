# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())

    i = 0
    while True:
        b = int((N - 3 * i) / 2)
        a = int(i - b)
        if 3 * a + 5 * b > N:
            sys.stdout.write("-1")
            break

        if (a < 0 or b < 0) or (not (b == (N - 3 * i) / 2 and a == i - (N - 3 * i) / 2)):
            i = i + 1
            continue

        else:
            sys.stdout.write("{}".format(i))
            break
