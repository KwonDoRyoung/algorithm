# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    N = str(sys.stdin.readline().rstrip())
    count = [0 for i in xrange(0, 9)]
    for s in N:
        if int(s) == 9 or int(s) == 6:
            count[6] += 1
        else:
            count[int(s)] += 1
    count[6] = int(count[6] / 2 + 0.5)
    sys.stdout.write("{}".format(max(count)))
