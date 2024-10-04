#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# https://www.hackerrank.com/challenges/mini-max-sum?isFullScreen=true
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    
    min_sum = 0
    for i in range(0, 4, 1):
      min_sum += arr[i]
      
    max_sum = 0
    for i in range(1, 5, 1):
      max_sum += arr[i]
    
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

