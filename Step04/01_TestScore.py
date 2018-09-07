# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    score = int(sys.stdin.readline())
    if (score >= 90) and (score <= 100):
        sys.stdout.write("A")
    elif (score >= 80) and (score <= 89):
        sys.stdout.write("B")
    elif (score >= 70) and (score <= 79):
        sys.stdout.write("C")
    elif (score >= 60) and (score <= 69):
        sys.stdout.write("D")
    else:
        sys.stdout.write("F")
