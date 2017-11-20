#!/bin/python3

import sys

entry_count = int(input())

entries = {}
for i in range(0, entry_count):
    entry = input().strip().split(' ')
    entries[entry[0]] = entry[1]

names = []
name = input()
while name:
    names.append(name)
    try:
        name = input()
    except EOFError:
        break

for i in range(0, len(names)):
    if names[i] in entries:
        print("%s=%s" % (names[i], entries[names[i]]))
    else:
        print("Not found")
