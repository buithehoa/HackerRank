#!/bin/python3

import sys

def turn_me_upside_down(arr):
    arr.reverse()

    return arr

def solution():
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr = turn_me_upside_down(arr)

    print(" ".join(str(e) for e in arr))

if __name__ == '__main__':
    solution()
