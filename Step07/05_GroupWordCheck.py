# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline().rstrip())
    count = 0
    for _ in xrange(N):
        flag = 1
        string = str(sys.stdin.readline().rstrip())
        for s in string:
            if string.count(s) == 1:
                continue
            else:
                previous = string.index(s)
                present = string.index(s)
                for n in xrange(string.index(s), len(string)):
                    if s == string[n]:
                        previous = present
                        present = n
                    if present - previous > 1:
                        flag = 0
                        break
            if flag == 0:
                break
        if flag == 1:
            count += 1

    sys.stdout.write("{}".format(count))
