# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())

    for _ in range(T):
        R, string = sys.stdin.readline().rstrip().split(" ")
        for s in str(string):
            sys.stdout.write("{}".format(int(R) * s))
        sys.stdout.write("\n")
