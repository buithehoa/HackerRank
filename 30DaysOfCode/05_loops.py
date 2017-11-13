#!/bin/python3

import sys

n = int(input().strip())
for x in range(1, 11):
    print("%d x %d = %d" % (n, x, n * x))
