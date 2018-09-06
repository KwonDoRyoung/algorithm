# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    num = sys.stdin.readline().split(" ")

    sys.stdout.write("{}".format(int(num[0])+int(num[1])))
    sys.stdout.flush()