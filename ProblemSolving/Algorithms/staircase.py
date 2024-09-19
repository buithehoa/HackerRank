"""
https://www.hackerrank.com/challenges/staircase/problem
"""
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    space = ' '
    sharp = '#'
    for i in range(1, n + 1):
        print(space * (n - i), end='')
        print(sharp * i)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)

