#!/usr/bin/python3
import sys

if len(sys.argv) == 1:
    print("Usage: python script.py <arguments>")
    sys.exit(1)

for i in range(1, len(sys.argv)):
    print(sys.argv[i])

