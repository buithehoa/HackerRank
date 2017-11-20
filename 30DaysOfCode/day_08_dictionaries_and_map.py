#!/bin/python3

import sys

def read_entries():
    entries = {}
    for i in range(0, entry_count):
        entry = input().strip().split(' ')
        entries[entry[0]] = entry[1]

    return entries

def read_names():
    names = []
    name = input()
    while name:
        names.append(name)
        try:
            name = input()
        except EOFError:
            break

    return names

def print_entries(names):
    for i in range(0, len(names)):
        if names[i] in entries:
            print("%s=%s" % (names[i], entries[names[i]]))
        else:
            print("Not found")

entry_count = int(input())
entries = read_entries()
names = read_names()

print_entries(names)
