#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
#

def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort(reverse=True)
    tallest = candles[0]
    tallest_count = 1
    
    for i in range(1, len(candles), 1):
        if candles[i] == tallest:
            tallest_count += 1
        else:
            break
    
    return tallest_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

