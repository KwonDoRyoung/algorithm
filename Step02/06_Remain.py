# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    num = sys.stdin.readline().split(" ")

    sys.stdout.write("{}\n".format((int(num[0]) + int(num[1])) % int(num[2])))
    sys.stdout.write("{}\n".format((int(num[0]) % int(num[2]) + int(num[1]) % int(num[2])) % int(num[2])))
    sys.stdout.write("{}\n".format((int(num[0]) * int(num[1])) % int(num[2])))
    sys.stdout.write("{}\n".format((int(num[0]) % int(num[2]) * int(num[1]) % int(num[2])) % int(num[2])))
    sys.stdout.flush()
