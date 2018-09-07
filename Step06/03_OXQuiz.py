# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    case = int(sys.stdin.readline())

    for _ in range(case):
        ox = sys.stdin.readline().rstrip()
        sum = 0
        score = 0
        for i in xrange(len(ox)):
            if ox[i] != "X":
                sum += score + 1
                score += 1
            else:
                score = 0
        sys.stdout.write("{}\n".format(sum))
        sys.stdout.flush()
