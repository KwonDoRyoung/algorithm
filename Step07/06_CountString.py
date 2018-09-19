# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    string = sys.stdin.readline().split()
    sys.stdout.write("{}\n".format(len(string)))
