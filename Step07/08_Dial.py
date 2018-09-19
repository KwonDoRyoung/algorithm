# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    string = sys.stdin.readline().rstrip()
    sum = 0
    for s in str(string):
        if s in ['A', 'B', 'C']:
            sum += 3
        elif s in ['D', 'E', 'F']:
            sum += 4
        elif s in ['G', 'H', 'I']:
            sum += 5
        elif s in ['J', 'K', 'L']:
            sum += 6
        elif s in ['M', 'N', 'O']:
            sum += 7
        elif s in ['P', 'Q', 'R', 'S']:
            sum += 8
        elif s in ['T', 'U', 'V']:
            sum += 9
        elif s in ['W', 'X', 'Y', 'Z']:
            sum += 10
    sys.stdout.write("{}".format(sum))
