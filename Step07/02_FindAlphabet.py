# coding=utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sys

if __name__ == "__main__":
    alphabet = [-1 for _ in range(26)]
    string = sys.stdin.readline().rstrip()
    for n, s in enumerate(str(string)):
        if alphabet[int(ord(s) - ord('a'))] == -1:
            alphabet[int(ord(s) - ord('a'))] = n
    for alpha in alphabet:
        sys.stdout.write("{} ".format(alpha))
