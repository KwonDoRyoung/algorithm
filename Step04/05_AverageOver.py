# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    C = int(sys.stdin.readline())

    for _ in range(C):
        case = [float(s) for s in sys.stdin.readline().split()]
        avg = sum(case[1:]) / case[0]
        goodStudents = 0
        for i in range(1, int(case[0] + 1)):
            if case[i] > avg:
                goodStudents += 1
        sys.stdout.write("{:.3f}%\n".format(float(goodStudents) / case[0] * 100.0))

        del case
        del avg
        del goodStudents
