#!/bin/python3

# Day 20: Sorting
# https://www.hackerrank.com/challenges/30-sorting/problem

import sys

class BubbleSort:
    def __init__(self, a):
        self._a = a

    def sort(self):
        self._number_of_swaps = 0

        for i in range(len(self._a)):
            for j in range(len(self._a) - 1):
                if (self._a[j] > self._a[j + 1]):
                    tmp = self._a[j]
                    self._a[j] = self._a[j + 1]
                    self._a[j + 1] = tmp
                    self._number_of_swaps += 1

            if self._number_of_swaps == 0:
                break

    def print_stats(self):
        print("Array is sorted in %d swaps." % self._number_of_swaps)
        print("First Element: %d" % self._a[0])
        print("Last Element: %d" % self._a[-1])

if __name__  ==  "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    # Write Your Code Here

    bs = BubbleSort(a)
    bs.sort()
    bs.print_stats()
