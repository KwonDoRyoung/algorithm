# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    scale = [int(s) for s in sys.stdin.readline().split(" ")]
    if scale == [1, 2, 3, 4, 5, 6, 7, 8]:
        sys.stdout.write("ascending")
    elif scale == [8, 7, 6, 5, 4, 3, 2, 1]:
        sys.stdout.write("descending")
    else:
        sys.stdout.write("mixed")
    sys.stdout.flush()
