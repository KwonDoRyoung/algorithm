# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys


def factorial(n):
    result = 1
    for i in xrange(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    T = int(sys.stdin.readline().rstrip())
    for _ in xrange(T):
        k = int(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())
        count = 0
        if n == 1:
            count = 1
        else:
            count = int(factorial(n + k) / (factorial(k + 1) * factorial(n - 1)))
        sys.stdout.write("{}\n".format(count))
