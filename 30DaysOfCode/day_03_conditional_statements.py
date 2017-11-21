#!/bin/python3

import sys

def is_even(integer):
    return integer % 2 == 0

def is_odd(integer):
    return not is_even(integer)

N = int(input().strip())

if is_odd(N):
    print("Weird")
elif is_even(N):
    if 2 <= N <= 5:
        print("Not Weird")
    elif 6 <= N <= 20:
        print("Weird")
    else:
        print("Not Weird")
