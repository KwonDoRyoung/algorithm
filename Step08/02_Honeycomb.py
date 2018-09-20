# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    n = 0
    while True:
        if N == 1:
            break
        else:
            if 3 * n * (n + 1) + 2 > N:
                if 3 * n * (n - 1) + 2 <= N:
                    break
                else:
                    n += 1
            else:
                n += 1

    sys.stdout.write("{}".format(n + 1))
