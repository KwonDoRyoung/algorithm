# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for n in range(1, N + 1):
        sys.stdout.write("{}{}\n".format(" " * (N - n), "*" * n))
        sys.stdout.flush()
