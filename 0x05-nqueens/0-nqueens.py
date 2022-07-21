#!/usr/bin/python3
""" N queen script """
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print('Usage: nqueens N')
    exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if num < 4:
    print('N must be at least 4')
    exit(1)

print('suceeded')
