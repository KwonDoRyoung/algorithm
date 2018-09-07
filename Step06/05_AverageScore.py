# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    sum = 0
    for _ in range(5):
        n = int(sys.stdin.readline())
        n = n if n >= 40 else 40
        sum += n

    sys.stdout.write("{}".format(sum // 5))
    sys.stdout.flush()