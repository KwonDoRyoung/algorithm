# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys


def checkSeries(num):
    if num < 100:
        return True
    else:
        if int(str(num)[1]) * 2 == int(str(num)[0]) + int(str(num)[2]):
            return True
        else:
            return False


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    count = 0
    for n in range(1, N + 1):
        if checkSeries(n):
            count += 1

    sys.stdout.write("{}".format(count))
