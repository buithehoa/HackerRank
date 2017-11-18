#!/bin/python3

import sys

def consecutive_count(binary_string):
    count = 0
    max_count = 0
    for i in range(0, len(binary_string)):
        if binary_string[i] == '1':
            count += 1
        else:
            if count > max_count: max_count = count
            count = 0

    if count > max_count: max_count = count

    return max_count

if __name__ == "__main__":
    n = int(input().strip())
    bn = "{0:b}".format(n)

    print(consecutive_count(bn))
