#!/usr/bin/python3
import sys
filename=sys.argv[1]
with open(filename) as f:
    for i in f.readlines():
        print(i,end="")