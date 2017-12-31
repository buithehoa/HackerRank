# Day 25: Running Time and Complexity
# https://www.hackerrank.com/challenges/30-running-time-and-complexity/problem

import sys
import math

class PrimeNumber(object):
    @classmethod
    def is_prime(cls, n):
        if n == 1: return False

        sqrt = round(math.sqrt(n))
        for i in range(1, sqrt + 1):
            remainder = n % i
            if remainder == 0 and i != 1:
                return False

        return True

if __name__ == "__main__":
    t = int(input())
    n = []
    for i in range(t):
        n.append(int(input()))

    for i in range(t):
        if PrimeNumber.is_prime(n[i]):
            print('Prime')
        else:
            print('Not prime')
