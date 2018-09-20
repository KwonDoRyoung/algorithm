# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    X = int(sys.stdin.readline().rstrip())
    n = 1
    while True:
        if ((n * (n - 1) // 2) < X) and (X <= (n * (n + 1) // 2)):
            break
        else:
            n += 1
    k = n if X - (n * (n - 1) // 2) == 0 else (X - (n * (n - 1) // 2))
    if n % 2 == 0:
        sys.stdout.write("{}/{}".format(k, n + 1 - k))
    else:
        sys.stdout.write("{}/{}".format(n + 1 - k, k))
