# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    numbers = sys.stdin.readline()
    result = 0
    for i in range(N):
        result = result + int(numbers[i])
    sys.stdout.write("{}".format(result))
    sys.stdout.flush()
