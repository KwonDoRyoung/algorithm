# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys


def d(num):
    sum = num
    for n in str(num):
        sum = sum + int(n)
    return sum


if __name__ == "__main__":
    nonSelfSet = set()
    num = 1
    while num <= 10000:
        nonSelfSet.add(d(num))
        num += 1
    num = 1
    while num <= 10000:
        if not (num in nonSelfSet):
            sys.stdout.write("{}\n".format(num))
        num += 1
