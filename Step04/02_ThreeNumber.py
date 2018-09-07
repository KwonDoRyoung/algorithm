# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    n1, n2, n3 = sys.stdin.readline().split()
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    if n1 >= n2:
        if n1 <= n3:
            print(n1)
        else:
            if n2 >= n3:
                print(n2)
            else:
                print(n3)
    else:
        if n2 <= n3:
            print(n2)
        else:
            if n1 >= n3:
                print(n1)
            else:
                print(n3)
