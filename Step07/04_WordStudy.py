# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    string = sys.stdin.readline().rstrip()
    check = [0 for _ in range(26)]
    for s in str(string):
        check[ord(s.upper()) - ord('A')] += 1

    if check.count(max(check)) >= 2:
        sys.stdout.write("{}".format("?"))
    else:
        sys.stdout.write("{}".format(chr(ord('A') + check.index(max(check)))))
