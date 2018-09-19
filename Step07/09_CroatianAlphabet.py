# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    string = str(sys.stdin.readline().rstrip())
    count = 0
    k = 0
    for _ in range(len(string)):
        if k + 1 == len(string):
            count += 1
            break
        if string[k] in ["c", "s", "z"]:
            if string[k + 1] in ["=", "-"]:
                k += 2
            else:
                k += 1
        elif string[k] in ["l"]:
            if string[k + 1] in ["j"]:
                k += 2
            else:
                k += 1
        elif string[k] in ["n"]:
            if string[k + 1] in ["j"]:
                k += 2
            else:
                k += 1
        elif string[k] in ["d"]:
            if string[k + 1] in ["-"]:
                k += 2
            elif string[k + 1] in ["z"]:
                if string[k + 2] in ["="]:
                    k += 3
                else:
                    k += 1
            else:
                k += 1
        else:
            k += 1
        count += 1
        if k == len(string):
            break
    sys.stdout.write("{}".format(count))
