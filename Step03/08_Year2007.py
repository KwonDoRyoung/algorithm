# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    x, y = sys.stdin.readline().split(" ")
    x = int(x)
    y = int(y)
    if ((x >= 1) and (x <= 12)) and ((y >= 1) and (y <= 31)):
        day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
        n_day = 0
        for month in range(1, x + 1):
            if month == x:
                n_day = n_day + y
                break

            elif month in [1, 3, 5, 7, 8, 10, 12]:
                n_day = n_day + 31

            elif month in [4, 6, 9, 11]:
                n_day = n_day + 30

            elif month in [2]:
                n_day = n_day + 28

            else:
                break

        sys.stdout.write("{}".format(day[n_day % 7]))
        sys.stdout.flush()
