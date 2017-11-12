#!/bin/python3

import sys

t = int(input().strip())

test_cases = []
for x in range(0, t):
    test_case = input()
    test_cases.append(test_case)

for x in range(0, t):
    even = True
    even_indexed = ""
    odd_indexed = ""

    for y in range(0, len(test_cases[x])):
        if even:
            even_indexed += test_cases[x][y]
            even = False
        else:
            odd_indexed += test_cases[x][y]
            even = True

    print("%s %s" % (even_indexed, odd_indexed))
